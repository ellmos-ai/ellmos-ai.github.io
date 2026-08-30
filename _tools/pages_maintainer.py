#!/usr/bin/env python3
"""Idempotenter 7-Tage-Maintainer für die öffentliche ellmos-Pages-Site."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path


WINDOW_DAYS = 7
WINDOW_ANCHOR = dt.datetime(2026, 1, 5, tzinfo=dt.timezone.utc)
SITE_FILES = (".nojekyll", "index.html", "skills.html", "bundles.html", "stack-composer.html")
CONTENT_FILES = ("index.html", "skills.html", "bundles.html", "stack-composer.html")


class MaintainerError(RuntimeError):
    """Fail-closed Fehler eines Maintainer-Laufs."""


def _utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _parse_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)


def window_bounds(moment: dt.datetime) -> tuple[dt.datetime, dt.datetime]:
    moment = moment.astimezone(dt.timezone.utc)
    width = dt.timedelta(days=WINDOW_DAYS)
    index = (moment - WINDOW_ANCHOR) // width
    start = WINDOW_ANCHOR + index * width
    return start, start + width


def _git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=check,
    )


def latest_site_commit_time(repo: Path) -> dt.datetime | None:
    result = _git(
        repo,
        "log",
        "-1",
        "--format=%cI",
        "--",
        *CONTENT_FILES,
        check=False,
    )
    return _parse_time(result.stdout.strip()) if result.returncode == 0 else None


def read_marker(marker: Path) -> dict:
    try:
        data = json.loads(marker.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return {"invalid": exc.__class__.__name__}
    return data if isinstance(data, dict) else {"invalid": "not-an-object"}


def check_status(repo: Path, marker: Path, now: dt.datetime | None = None) -> dict:
    now = now or _utcnow()
    start, end = window_bounds(now)
    marker_data = read_marker(marker)
    marker_time = _parse_time(marker_data.get("last_success_utc"))
    commit_time = latest_site_commit_time(repo)
    evidence = [value for value in (marker_time, commit_time) if value is not None]
    latest = max(evidence) if evidence else None
    due = latest is None or latest < start
    reasons: list[str] = []
    if marker_data.get("invalid"):
        reasons.append(f"Marker ungültig: {marker_data['invalid']}")
    if latest is None:
        reasons.append("weder erfolgreicher Marker noch Site-Inhaltscommit gefunden")
    elif due:
        reasons.append("letzter belegter Lauf liegt vor dem aktuellen 7-Tage-Fenster")
    else:
        reasons.append("Marker oder Site-Inhaltscommit liegt im aktuellen 7-Tage-Fenster")
    return {
        "status": "due" if due else "fresh",
        "due": due,
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "latest_evidence_utc": latest.isoformat() if latest else None,
        "marker_utc": marker_time.isoformat() if marker_time else None,
        "site_commit_utc": commit_time.isoformat() if commit_time else None,
        "reason": "; ".join(reasons),
    }


def _status_paths(repo: Path) -> list[str]:
    result = _git(repo, "status", "--porcelain=v1")
    return [line[3:].strip() for line in result.stdout.splitlines() if line.strip()]


def _assert_clean(repo: Path) -> None:
    dirty = _status_paths(repo)
    if dirty:
        raise MaintainerError(f"Pages-Worktree nicht sauber: {dirty}")


@contextlib.contextmanager
def run_lock(repo: Path):
    foreign = [path for path in repo.glob("LOCK*.txt") if path.name != "LOCK.pages-maintainer.txt"]
    if foreign:
        raise MaintainerError(f"aktiver Projektlock: {[path.name for path in foreign]}")
    lock = repo / "LOCK.pages-maintainer.txt"
    try:
        with lock.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(
                "owner: pages-maintainer\n"
                f"created: {_utcnow().isoformat()}\n"
                "expires_after: 6h\n"
                "mode: hard\n"
                "purpose: idempotenter Pages-Bau\n"
            )
    except FileExistsError as exc:
        raise MaintainerError("LOCK.pages-maintainer.txt existiert bereits") from exc
    try:
        yield
    finally:
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def _json_array_after(text: str, prefix: str) -> list:
    start = text.find(prefix)
    if start < 0:
        raise MaintainerError(f"Datenblock fehlt: {prefix}")
    start += len(prefix)
    try:
        value, _ = json.JSONDecoder().raw_decode(text[start:].lstrip())
    except json.JSONDecodeError as exc:
        raise MaintainerError(f"Datenblock ungültig: {prefix}") from exc
    if not isinstance(value, list):
        raise MaintainerError(f"Datenblock ist keine Liste: {prefix}")
    return value


def _canonical_skill_count(ai_root: Path) -> int:
    path = ai_root / ".SKILLS" / "registry" / "components.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    components = data.get("components")
    if not isinstance(components, list):
        raise MaintainerError(f"Skill-Registry ohne components[]: {path}")
    return len(components)


def _generator_skill_count(generator: Path, skills_repo: Path | None = None) -> int:
    if skills_repo is not None:
        registry = skills_repo / "registry" / "components.json"
        data = json.loads(registry.read_text(encoding="utf-8"))
        components = data.get("components")
        if not isinstance(components, list):
            raise MaintainerError(f"Generator-Registry ohne components[]: {registry}")
        return len(components)
    source = generator.read_text(encoding="utf-8")
    match = re.search(r'^SKILLS_REPO\s*=\s*r?["\']([^"\']+)["\']', source, re.MULTILINE)
    if not match:
        raise MaintainerError("SKILLS_REPO im Generator nicht auflösbar")
    registry = Path(match.group(1)) / "registry" / "components.json"
    data = json.loads(registry.read_text(encoding="utf-8"))
    components = data.get("components")
    if not isinstance(components, list):
        raise MaintainerError(f"Generator-Registry ohne components[]: {registry}")
    return len(components)


def verify_generator_inputs(
    ai_root: Path, generator: Path, skills_repo: Path | None = None
) -> None:
    canonical = _canonical_skill_count(ai_root)
    generator_count = _generator_skill_count(generator, skills_repo)
    if generator_count != canonical:
        raise MaintainerError(
            "Skill-Quelle des Generators ist nicht kataloggleich: "
            f"Generator={generator_count}, .AI/.SKILLS={canonical}. "
            "Kein Seitenbau mit veraltetem Klon."
        )


def _run_python(script: Path, *, cwd: Path, env: dict[str, str]) -> str:
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    combined = "\n".join(part.strip() for part in (result.stdout, result.stderr) if part.strip())
    if result.returncode != 0:
        raise MaintainerError(f"{script.name} fehlgeschlagen ({result.returncode}):\n{combined}")
    return combined


def verify_leak_gates(repo: Path, ai_root: Path) -> dict:
    modules = json.loads(
        (ai_root / ".MODULES" / "modules.catalog.json").read_text(encoding="utf-8")
    )["modules"]
    index = (repo / "index.html").read_text(encoding="utf-8")
    private_ids = sorted(
        module["id"] for module in modules if module.get("visibility") != "public"
    )
    leaks = [module_id for module_id in private_ids if module_id in index]
    if leaks:
        raise MaintainerError(f"Leak-Gate: nichtöffentliche Modul-IDs in index.html: {leaks}")
    forbidden = [token for token in ('vis:"priv"', 'vis:"cand"') if token in index]
    if forbidden:
        raise MaintainerError(f"Leak-Gate: private Sichtbarkeitsmarker in index.html: {forbidden}")
    for name in CONTENT_FILES:
        path = repo / name
        if not path.is_file() or path.stat().st_size == 0:
            raise MaintainerError(f"Build-Artefakt fehlt oder ist leer: {name}")
    skills = _json_array_after((repo / "skills.html").read_text(encoding="utf-8"), "const SKILLS=")
    expected_skills = _canonical_skill_count(ai_root)
    if len(skills) != expected_skills:
        raise MaintainerError(
            f"Skill-Zahl nach Build driftet: Site={len(skills)}, Registry={expected_skills}"
        )
    return {
        "private_module_ids_checked": len(private_ids),
        "skill_count": len(skills),
        "artifacts": list(CONTENT_FILES),
    }


def _atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temp, path)


def append_day_log(path: Path, marker: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    run_id = marker["run_id"]
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if run_id in existing:
        return
    verb = "Inhaltsänderung committet" if marker["content_changed"] else "kein Inhaltsdiff"
    line = (
        f"✓ ellmos-ai.github.io [{run_id}]: Generatoren + Leak-Gates grün; "
        f"{verb}; Site-Commit {marker['site_commit']}.\n"
    )
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)


def _commit_if_changed(repo: Path) -> tuple[bool, str]:
    changed = _status_paths(repo)
    unexpected = sorted(set(changed) - set(SITE_FILES))
    if unexpected:
        raise MaintainerError(f"Builder änderte unerwartete Dateien: {unexpected}")
    if not changed:
        return False, _git(repo, "rev-parse", "HEAD").stdout.strip()
    _git(repo, "add", "--", *changed)
    _git(repo, "commit", "-m", "build: refresh public site maps (maintainer)")
    return True, _git(repo, "rev-parse", "HEAD").stdout.strip()


def run_maintainer(
    repo: Path,
    ai_root: Path,
    marker: Path,
    day_log: Path,
    *,
    push: bool,
) -> dict:
    generator = ai_root / "_scripts" / "gen_ellmos_maps.py"
    builder = ai_root / "_scripts" / "build_pages_site.py"
    if not generator.is_file() or not builder.is_file():
        raise MaintainerError("Generator oder Pages-Builder fehlt")
    skills_repo = ai_root / ".SKILLS"
    verify_generator_inputs(ai_root, generator, skills_repo)
    with run_lock(repo):
        _assert_clean(repo)
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["ELLMOS_AI_ROOT"] = str(ai_root)
        env["ELLMOS_SKILLS_REPO"] = str(skills_repo)
        env["ELLMOS_PAGES_SITE"] = str(repo)
        generator_output = _run_python(generator, cwd=ai_root, env=env)
        builder_output = _run_python(builder, cwd=ai_root, env=env)
        gates = verify_leak_gates(repo, ai_root)
        changed, commit = _commit_if_changed(repo)
        if push and changed:
            _git(repo, "push", "origin", "HEAD")
        run_id = _utcnow().strftime("%Y%m%dT%H%M%SZ")
        payload = {
            "schema": "ellmos.pages-maintainer-marker.v1",
            "run_id": run_id,
            "last_success_utc": _utcnow().isoformat(),
            "window_days": WINDOW_DAYS,
            "site_commit": commit,
            "content_changed": changed,
            "pushed": bool(push and changed),
            "gates": gates,
        }
        _atomic_json(marker, payload)
        append_day_log(day_log, payload)
    return {
        **payload,
        "generator": generator_output,
        "builder": builder_output,
    }


def _default_paths() -> tuple[Path, Path, Path, Path]:
    repo = Path(__file__).resolve().parents[1]
    user = Path(os.environ.get("USERPROFILE", str(Path.home())))
    ai_root = Path(os.environ.get("ELLMOS_AI_ROOT", user / "OneDrive" / ".TOPICS" / ".AI"))
    marker = repo / "_tools" / ".state" / "pages-maintainer.json"
    day_log = (
        user
        / "OneDrive"
        / "Desktop"
        / "24-automation-logging"
        / "24.workstation.codex.txt"
    )
    return repo, ai_root, marker, day_log


def build_parser() -> argparse.ArgumentParser:
    repo, ai_root, marker, day_log = _default_paths()
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fälligkeit im 7-Tage-Fenster prüfen")
    mode.add_argument("--run", action="store_true", help="Generatoren, Gates und Commit ausführen")
    mode.add_argument(
        "--fallback",
        action="store_true",
        help="prüfen und nur bei Fälligkeit den Maintainer-Lauf ausführen",
    )
    parser.add_argument("--push", action="store_true", help="neuen Commit zusätzlich pushen")
    parser.add_argument("--repo", type=Path, default=repo)
    parser.add_argument("--ai-root", type=Path, default=ai_root)
    parser.add_argument("--marker", type=Path, default=marker)
    parser.add_argument("--day-log", type=Path, default=day_log)
    parser.add_argument("--json", action="store_true")
    return parser


def _print(payload: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return
    for key, value in payload.items():
        if key in {"generator", "builder"}:
            lines = str(value).splitlines()
            value = " | ".join(lines[-6:])
        print(f"{key}: {value}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        status = check_status(args.repo, args.marker)
        if args.check:
            _print(status, args.json)
            return 0
        if args.fallback and not status["due"]:
            _print({**status, "action": "skip"}, args.json)
            return 0
        result = run_maintainer(
            args.repo,
            args.ai_root,
            args.marker,
            args.day_log,
            push=args.push,
        )
        _print({**status, "action": "run", **result}, args.json)
        return 0
    except (MaintainerError, OSError, json.JSONDecodeError, subprocess.SubprocessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

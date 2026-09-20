import datetime as dt
import importlib.util
import json
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "_tools" / "pages_maintainer.py"
SPEC = importlib.util.spec_from_file_location("pages_maintainer", SCRIPT)
maintainer = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(maintainer)


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "site"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.email", "test@example.invalid")
    _git(repo, "config", "user.name", "Test")
    for name in maintainer.CONTENT_FILES:
        (repo / name).write_text(name, encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "initial")
    return repo


def test_check_uses_marker_for_successful_no_diff_run(tmp_path):
    repo = _repo(tmp_path)
    now = dt.datetime(2026, 8, 30, 12, tzinfo=dt.timezone.utc)
    marker = tmp_path / "marker.json"
    marker.write_text(json.dumps({"last_success_utc": now.isoformat()}), encoding="utf-8")

    result = maintainer.check_status(repo, marker, now=now)

    assert result["status"] == "fresh"
    assert result["marker_utc"] == now.isoformat()


def test_check_is_due_when_all_evidence_precedes_window(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    marker = tmp_path / "marker.json"
    marker.write_text(
        json.dumps({"last_success_utc": "2026-08-01T00:00:00+00:00"}), encoding="utf-8"
    )
    monkeypatch.setattr(
        maintainer,
        "latest_site_commit_time",
        lambda _repo: dt.datetime(2026, 8, 2, tzinfo=dt.timezone.utc),
    )

    result = maintainer.check_status(
        repo, marker, now=dt.datetime(2026, 8, 30, 12, tzinfo=dt.timezone.utc)
    )

    assert result["status"] == "due"


def test_commit_only_when_site_content_changed(tmp_path):
    repo = _repo(tmp_path)
    before = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()

    changed, same = maintainer._commit_if_changed(repo)
    assert changed is False
    assert same == before

    (repo / "index.html").write_text("neu", encoding="utf-8")
    changed, after = maintainer._commit_if_changed(repo)
    assert changed is True
    assert after != before


def test_verify_generator_inputs_rejects_stale_skill_clone(tmp_path):
    ai = tmp_path / "ai"
    canonical = ai / ".SKILLS" / "registry"
    canonical.mkdir(parents=True)
    canonical.joinpath("components.json").write_text(
        json.dumps({"components": [{}, {}]}), encoding="utf-8"
    )
    clone = tmp_path / "skills"
    (clone / "registry").mkdir(parents=True)
    (clone / "registry" / "components.json").write_text(
        json.dumps({"components": [{}]}), encoding="utf-8"
    )
    generator = tmp_path / "gen.py"
    generator.write_text(f'SKILLS_REPO = r"{clone}"\n', encoding="utf-8")

    try:
        maintainer.verify_generator_inputs(ai, generator)
    except maintainer.MaintainerError as exc:
        assert "Generator=1" in str(exc)
        assert ".AI/.SKILLS=2" in str(exc)
    else:
        raise AssertionError("veraltete Generatorquelle wurde nicht abgewiesen")


def test_verify_generator_inputs_accepts_explicit_canonical_skill_root(tmp_path):
    ai = tmp_path / "ai"
    canonical = ai / ".SKILLS" / "registry"
    canonical.mkdir(parents=True)
    canonical.joinpath("components.json").write_text(
        json.dumps({"components": [{}, {}]}), encoding="utf-8"
    )
    generator = tmp_path / "gen.py"
    generator.write_text('SKILLS_REPO = r"C:\\stale"\n', encoding="utf-8")

    maintainer.verify_generator_inputs(ai, generator, ai / ".SKILLS")


def test_default_paths_uses_host_system_and_actor(monkeypatch, tmp_path):
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    monkeypatch.delenv("ELLMOS_SYSTEM", raising=False)
    monkeypatch.delenv("SYNC_SLOT", raising=False)
    monkeypatch.delenv("ELLMOS_ACTOR", raising=False)
    monkeypatch.delenv("AUTOMATION_PROVIDER", raising=False)
    monkeypatch.setenv("TASKPLAN_PROVIDER", "claude-code")
    monkeypatch.setattr(maintainer.socket, "gethostname", lambda: "ASUS-GEI")

    day_log = maintainer._default_paths()[-1]

    assert day_log.name == "24.laptop.claude-code.txt"


def test_default_paths_separates_host_and_actor_combinations(monkeypatch):
    monkeypatch.setenv("ELLMOS_SYSTEM", "workstation")
    monkeypatch.setenv("ELLMOS_ACTOR", "codex")
    first = maintainer._default_paths()[-1]

    monkeypatch.setenv("ELLMOS_SYSTEM", "surface")
    monkeypatch.setenv("ELLMOS_ACTOR", "gemini")
    second = maintainer._default_paths()[-1]

    assert first.name == "24.workstation.codex.txt"
    assert second.name == "24.surface.gemini.txt"
    assert first != second

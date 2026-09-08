from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_ci_workflow_integrity():
    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_path.is_file(), "CI workflow file .github/workflows/ci.yml must exist"
    content = ci_path.read_text(encoding="utf-8")

    assert "cancel-in-progress: true" in content, "Workflow must cancel outdated runs"
    for runner in ("ubuntu-latest", "windows-latest", "macos-latest"):
        assert runner in content, f"Runner {runner} missing in CI matrix"
    for py in ('"3.10"', '"3.11"', '"3.12"', '"3.13"'):
        assert py in content, f"Python version {py} missing in CI matrix"
    assert "actions/checkout@v4" in content, "Workflow must use checkout@v4"
    assert "actions/setup-python@v5" in content, "Workflow must use setup-python@v5"
    assert "cache: 'pip'" in content, "Workflow must use pip caching"
    assert "ruff check" in content, "Workflow must execute ruff linter"
    assert "pytest" in content, "Workflow must execute pytest test suite"


def test_pyproject_pep621_metadata():
    pyproject_path = ROOT / "pyproject.toml"
    assert pyproject_path.is_file(), "pyproject.toml must exist"
    content = pyproject_path.read_text(encoding="utf-8")

    assert 'name = "ellmos-ai-github-io"' in content, "Project name must match"
    assert 'version = "0.1.0"' in content, "Version must match 0.1.0"
    assert 'license = "MIT"' in content, "License must be MIT"

    required_urls = [
        "Homepage",
        "Documentation",
        "Repository",
        "Issues",
        "Changelog",
        "Security",
        "Parent Organization",
        "Umbrella Ecosystem",
    ]
    for url in required_urls:
        assert f'"{url}"' in content or f"{url} =" in content, f"Missing URL: {url}"

    assert "[tool.pytest.ini_options]" in content, "pytest options must be configured"
    assert "[tool.ruff]" in content, "ruff must be configured"


def test_security_policy_contract():
    sec_path = ROOT / "SECURITY.md"
    assert sec_path.is_file(), "SECURITY.md must exist"
    content = sec_path.read_text(encoding="utf-8")

    assert "[English](#english)" in content and "[Deutsch](#deutsch)" in content, "Must be bilingual"
    assert "0.1.x" in content, "Supported version 0.1.x must be listed"
    assert "48 hours" in content or "48 Stunden" in content, "48h SLA must be documented"
    assert "security@ellmos.ai" in content, "Official security email must be present"
    assert "lukas@open-bricks.org" in content, "Umbrella security email must be present"
    assert "https://github.com/ellmos-ai/ellmos-ai.github.io/security/advisories" in content

    invariants = [
        "100% Static & Zero-Egress",
        "Fail-Closed Leak-Gates",
        "Deterministic & Idempotent",
        "Local-First & Non-Elevation",
        "Fail-Closed Lock Discipline",
    ]
    for inv in invariants:
        assert inv.lower() in content.lower(), f"Invariant missing: {inv}"


def test_site_artifacts_integrity():
    content_files = ["index.html", "bundles.html", "skills.html", "stack-composer.html"]
    for name in content_files:
        path = ROOT / name
        assert path.is_file(), f"Public artifact {name} missing"
        assert path.stat().st_size > 0, f"Public artifact {name} is empty"

    nojekyll = ROOT / ".nojekyll"
    assert nojekyll.is_file(), ".nojekyll marker must exist"

    license_file = ROOT / "LICENSE"
    assert license_file.is_file(), "LICENSE file must exist"


def test_site_leak_gates():
    index_path = ROOT / "index.html"
    assert index_path.is_file()
    index_content = index_path.read_text(encoding="utf-8")

    for forbidden in ('vis:"priv"', 'vis:"cand"'):
        assert forbidden not in index_content, f"Leak-Gate: {forbidden} found in index.html"


def test_readme_badges_and_parity():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    assert readme_en.is_file(), "README.md must exist"
    assert readme_de.is_file(), "README_de.md must exist"

    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

    for content in (content_en, content_de):
        assert "img.shields.io" in content, "Shields badges must be present"
        assert "SECURITY.md" in content, "Link to SECURITY.md required"
        assert "CHANGELOG.md" in content, "Link to CHANGELOG.md required"
        assert "llms.txt" in content, "Link to llms.txt required"
        assert "https://ellmos-ai.github.io" in content, "Link to live site required"


def test_llms_txt_contract():
    llms_path = ROOT / "llms.txt"
    assert llms_path.is_file(), "llms.txt must exist"
    content = llms_path.read_text(encoding="utf-8")

    assert "https://ellmos-ai.github.io" in content
    assert "https://github.com/ellmos-ai/ellmos-ai.github.io" in content
    assert "pages_maintainer.py" in content
    assert "SECURITY.md" in content


def test_changelog_integrity():
    changelog_path = ROOT / "CHANGELOG.md"
    assert changelog_path.is_file(), "CHANGELOG.md must exist"
    content = changelog_path.read_text(encoding="utf-8")

    assert "[0.1.0]" in content, "Release [0.1.0] must be in CHANGELOG.md"


def test_gitignore_hygiene():
    gitignore_path = ROOT / ".gitignore"
    assert gitignore_path.is_file(), ".gitignore must exist"
    content = gitignore_path.read_text(encoding="utf-8")

    assert "*.sync-conflict-*" in content, "Sync conflict pattern missing"
    assert ".pytest_cache/" in content, "pytest cache pattern missing"
    assert ".ruff_cache/" in content, "ruff cache pattern missing"
    assert "LOCK*.txt" in content, "LOCK pattern missing"

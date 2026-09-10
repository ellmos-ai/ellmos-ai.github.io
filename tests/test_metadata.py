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
    assert 'version = "0.1.1"' in content, "Version must match 0.1.1"
    assert 'license = "MIT"' in content, "License must be MIT"

    required_urls = [
        "Homepage",
        "Documentation",
        "Repository",
        "Issues",
        "Changelog",
        "Security",
        "Third-Party Licenses",
        "Marketing Log",
        "Parent Organization",
        "Umbrella Ecosystem",
    ]
    for url in required_urls:
        assert f'"{url}"' in content or f"{url} =" in content, f"Missing URL: {url}"

    assert "[tool.pytest.ini_options]" in content, "pytest options must be configured"
    assert 'addopts = "-ra -v"' in content, "pytest addopts must include -ra -v"
    assert "[tool.ruff]" in content, "ruff must be configured"


def test_security_policy_contract():
    sec_path = ROOT / "SECURITY.md"
    assert sec_path.is_file(), "SECURITY.md must exist"
    content = sec_path.read_text(encoding="utf-8")

    assert "[English](#english)" in content and "[Deutsch](#deutsch)" in content, "Must be bilingual"
    assert "0.1.x" in content, "Supported version 0.1.x must be listed"
    assert "48 hours" in content and "48 Stunden" in content, "48h SLA must be documented in both languages"
    assert "5 business days" in content or "5 Werktagen" in content, "5-day triage commitment required"
    assert "security@ellmos.ai" in content, "Official security email must be present"
    assert "lukas@open-bricks.org" in content, "Umbrella security email must be present"
    assert "https://github.com/ellmos-ai/ellmos-ai.github.io/security/advisories" in content

    invariants = [
        "INV-STATIC-01",
        "INV-LEAK-02",
        "INV-CATALOG-03",
        "INV-RUNAS-04",
        "INV-WINDOW-05",
        "INV-DIFF-06",
        "INV-LOCK-07",
        "INV-OS-08",
        "INV-CLIENT-09",
        "INV-SLA-10",
    ]
    for inv in invariants:
        assert inv in content, f"Security invariant missing: {inv}"


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
        assert "THIRD_PARTY_LICENSES.md" in content, "Link to THIRD_PARTY_LICENSES.md required"
        assert "MARKETING-LOG.txt" in content, "Link to MARKETING-LOG.txt required"
        assert "CHANGELOG.md" in content, "Link to CHANGELOG.md required"
        assert "llms.txt" in content, "Link to llms.txt required"
        assert "https://ellmos-ai.github.io" in content, "Link to live site required"
        assert "```mermaid" in content, "Mermaid diagrams required"
        assert "flowchart TB" in content, "Flowchart architecture diagram required"
        assert "sequenceDiagram" in content, "Lifecycle sequence diagram required"
        assert "INV-STATIC-01" in content and "INV-SLA-10" in content, "Invariants table required"
        assert "open-bricks" in content, "Umbrella reference required"


def test_readme_quick_navigation_parity():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

    nav_en_start = content_en.find("## Quick Navigation")
    nav_en_end = content_en.find("---", nav_en_start)
    nav_en_lines = [
        line.strip()
        for line in content_en[nav_en_start:nav_en_end].splitlines()
        if line.strip().startswith("- [")
    ]

    nav_de_start = content_de.find("## Schnellnavigation")
    nav_de_end = content_de.find("---", nav_de_start)
    nav_de_lines = [
        line.strip()
        for line in content_de[nav_de_start:nav_de_end].splitlines()
        if line.strip().startswith("- [")
    ]

    assert len(nav_en_lines) == 14, f"Expected 14 English nav items, found {len(nav_en_lines)}"
    assert len(nav_de_lines) == 14, f"Expected 14 German nav items, found {len(nav_de_lines)}"


def test_third_party_licenses_contract():
    license_doc = ROOT / "THIRD_PARTY_LICENSES.md"
    assert license_doc.is_file(), "THIRD_PARTY_LICENSES.md must exist"
    content = license_doc.read_text(encoding="utf-8")

    assert "MIT License" in content
    assert "Zero External Runtime Dependencies" in content
    assert "Python Standard Library" in content
    assert "pytest" in content
    assert "Ruff" in content


def test_marketing_log_contract():
    marketing_doc = ROOT / "MARKETING-LOG.txt"
    assert marketing_doc.is_file(), "MARKETING-LOG.txt must exist"
    content = marketing_doc.read_text(encoding="utf-8")

    assert "ELLMOS-AI / ELLMOS-AI.GITHUB.IO" in content
    assert "PRODUCT IDENTITY & MISSION" in content
    assert "TARGET PERSONAS & AUDIENCE MAPPING" in content
    assert "ARCHITECTURAL INVARIANTS & GOVERNANCE" in content
    assert "SEARCH KEYWORDS & CRAWLER DISCOVERABILITY INDEX" in content
    assert "ECOSYSTEM & CROSS-PROJECT SYNERGY" in content


def test_sibling_ecosystem_matrix():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

    siblings = [
        "ellmos-ai/coma",
        "ellmos-ai/clutch",
        "ellmos-ai/MarbleRun",
        "ellmos-ai/policy-registry",
        "ellmos-ai/system-explorer",
        "ellmos-ai/sqlite-transit-sync",
        "ellmos-ai/workflowhooker",
        "ellmos-ai/memoryhooker",
        "ellmos-ai/swarm_ai",
        "ellmos-ai/ellmos-filecommander-mcp",
        "ellmos-ai/ellmos-codecommander-mcp",
        "ellmos-ai/ellmos-controlcenter-mcp",
        "dev-bricks/DevCenter",
        "dev-bricks/CodeBox",
        "file-bricks/ProFiler",
        "open-bricks/open-bricks",
    ]

    for sibling in siblings:
        assert sibling in content_en, f"Sibling {sibling} missing in README.md"
        assert sibling in content_de, f"Sibling {sibling} missing in README_de.md"


def test_llms_txt_contract():
    llms_path = ROOT / "llms.txt"
    assert llms_path.is_file(), "llms.txt must exist"
    content = llms_path.read_text(encoding="utf-8")

    assert "https://ellmos-ai.github.io" in content
    assert "https://github.com/ellmos-ai/ellmos-ai.github.io" in content
    assert "pages_maintainer.py" in content
    assert "SECURITY.md" in content
    assert "INV-STATIC-01" in content
    assert "INV-SLA-10" in content


def test_changelog_integrity():
    changelog_path = ROOT / "CHANGELOG.md"
    assert changelog_path.is_file(), "CHANGELOG.md must exist"
    content = changelog_path.read_text(encoding="utf-8")

    assert "[0.1.1]" in content, "Release [0.1.1] must be in CHANGELOG.md"
    assert "[0.1.0]" in content, "Release [0.1.0] must be in CHANGELOG.md"


def test_gitignore_hygiene():
    gitignore_path = ROOT / ".gitignore"
    assert gitignore_path.is_file(), ".gitignore must exist"
    content = gitignore_path.read_text(encoding="utf-8")

    assert "*.sync-conflict-*" in content, "Sync conflict pattern missing"
    assert "*-conflict-*" in content, "Multi-host conflict pattern missing"
    assert "*-ASUS-GEI.*" in content, "ASUS host pattern missing"
    assert ".pytest_cache/" in content, "pytest cache pattern missing"
    assert ".ruff_cache/" in content, "ruff cache pattern missing"
    assert "LOCK" in content, "LOCK pattern missing"
    assert "LOCK*.txt" in content, "LOCK*.txt pattern missing"
    assert "LOCK.permissions.json" in content, "LOCK.permissions.json missing"

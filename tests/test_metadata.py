from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_ci_workflow_integrity():
    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_path.is_file(), "CI workflow file .github/workflows/ci.yml must exist"
    content = ci_path.read_text(encoding="utf-8")

    assert "cancel-in-progress: true" in content, "Workflow must cancel outdated runs"
    assert "permissions:" in content and "contents: read" in content, "Workflow must enforce least-privilege permissions"
    assert "timeout-minutes: 15" in content, "Workflow job must define timeout-minutes: 15"
    for runner in ("ubuntu-latest", "windows-latest", "macos-latest"):
        assert runner in content, f"Runner {runner} missing in CI matrix"
    for py in ('"3.10"', '"3.11"', '"3.12"', '"3.13"'):
        assert py in content, f"Python version {py} missing in CI matrix"
    assert "actions/checkout@v4" in content, "Workflow must use checkout@v4"
    assert "actions/setup-python@v5" in content, "Workflow must use setup-python@v5"
    assert "cache: 'pip'" in content, "Workflow must use pip caching"
    assert "ruff check" in content, "Workflow must execute ruff linter"
    assert "python -m pytest -ra -v" in content, "Workflow must execute pytest with -ra -v"


def test_pyproject_pep621_metadata():
    pyproject_path = ROOT / "pyproject.toml"
    assert pyproject_path.is_file(), "pyproject.toml must exist"
    content = pyproject_path.read_text(encoding="utf-8")

    assert 'name = "ellmos-ai-github-io"' in content, "Project name must match"
    assert 'version = "0.1.3"' in content, "Version must match 0.1.3"
    assert 'license = "MIT"' in content, "License must be MIT"
    assert 'license-files = ["LICENSE", "NOTICE", "THIRD_PARTY_LICENSES.md"]' in content

    required_urls = [
        "Homepage",
        "Documentation",
        "Repository",
        "Issues",
        "Bug Tracker",
        "Changelog",
        "Security",
        "Notice",
        "Third-Party Licenses",
        "Marketing Log",
        "LLM Context",
        "LLM Ready",
        "Parent Organization",
        "Umbrella Ecosystem",
    ]
    for url in required_urls:
        assert f'"{url}"' in content or f"{url} =" in content, f"Missing URL: {url}"

    for kw in ("mcp", "mcp-servers", "ai-agents", "agentic-workflows", "open-bricks", "zero-egress"):
        assert f'"{kw}"' in content, f"Missing keyword: {kw}"

    assert "[tool.pytest.ini_options]" in content, "pytest options must be configured"
    assert 'minversion = "7.0"' in content, "pytest minversion 7.0 must be configured"
    assert 'addopts = "-ra -v"' in content, "pytest addopts must include -ra -v"
    assert "norecursedirs =" in content, "pytest norecursedirs must be configured"
    assert "[tool.ruff]" in content, "ruff must be configured"
    assert 'select = ["E", "F", "W", "I", "B", "SIM", "C4"]' in content, "ruff select must have full ruleset"


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

    assert len(nav_en_lines) == 18, f"Expected 18 English nav items, found {len(nav_en_lines)}"
    assert len(nav_de_lines) == 18, f"Expected 18 German nav items, found {len(nav_de_lines)}"

    for i in range(1, 19):
        prefix = f"- [{i}."
        assert any(line.startswith(prefix) for line in nav_en_lines), f"English nav item {i} missing"
        assert any(line.startswith(prefix) for line in nav_de_lines), f"German nav item {i} missing"


def test_target_personas_contract():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    llms_doc = ROOT / "llms.txt"

    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")
    content_llms = llms_doc.read_text(encoding="utf-8")

    personas = ["[PERSONA-01]", "[PERSONA-02]", "[PERSONA-03]", "[PERSONA-04]"]
    for p in personas:
        assert p in content_en, f"Persona {p} missing in README.md"
        assert p in content_de, f"Persona {p} missing in README_de.md"
        assert p in content_llms, f"Persona {p} missing in llms.txt"


def test_comparative_matrix_contract():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

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
        assert content_en.count(inv) >= 2, f"Invariant {inv} must appear in both matrix and governance in README.md"
        assert content_de.count(inv) >= 2, f"Invariant {inv} must appear in both matrix and governance in README_de.md"


def test_statutory_notice_bgb_521():
    readme_de = ROOT / "README_de.md"
    content_de = readme_de.read_text(encoding="utf-8")

    assert "§ 521 BGB" in content_de, "German statutory notice (§ 521 BGB) missing in README_de.md"
    assert "Gefälligkeitsverhältnisses" in content_de, "Gratuitous service disclaimer missing"
    assert "Vorsatz und grobe Fahrlässigkeit" in content_de, "Statutory liability limitation missing"


def test_reciprocal_html_anchors():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

    anchor_checkpoints = [
        '<a id="1-features"></a>',
        '<a id="2-architecture"></a>',
        '<a id="3-target-personas--discoverability"></a>',
        '<a id="4-comparative-matrix-vs-alternatives"></a>',
        '<a id="5-dual-mermaid-diagrams"></a>',
        '<a id="6-governance--runtime-invariants"></a>',
        '<a id="7-interactive-web-applications-matrix"></a>',
        '<a id="8-module-circuit-map-deep-dive"></a>',
        '<a id="9-curated-bundle-recipes"></a>',
        '<a id="10-public-skill-library-viewer"></a>',
        '<a id="11-interactive-stack-composer-canvas"></a>',
        '<a id="12-pages-maintainer-automation--leak-gates"></a>',
        '<a id="13-verification-testing--quality-gates"></a>',
        '<a id="14-sibling-ecosystem--cross-project-topology"></a>',
        '<a id="15-third-party-licenses--open-source-auditing"></a>',
        '<a id="16-machine-readable-llm-context--agent-protocol"></a>',
        '<a id="17-changelog--project-history"></a>',
        '<a id="18-security-policy--statutory-notice"></a>',
    ]

    for anchor in anchor_checkpoints:
        assert anchor in content_en, f"Anchor {anchor} missing in README.md"
        assert anchor in content_de, f"Anchor {anchor} missing in README_de.md"


def test_third_party_licenses_contract():
    license_doc = ROOT / "THIRD_PARTY_LICENSES.md"
    assert license_doc.is_file(), "THIRD_PARTY_LICENSES.md must exist"
    content = license_doc.read_text(encoding="utf-8")

    assert "MIT License" in content
    assert "Zero External Runtime Dependencies" in content
    assert "Python Standard Library" in content
    assert "pytest" in content
    assert "Ruff" in content
    assert "Audit Date" in content and "2026-09-24" in content
    assert "**Audited Target Version:** 0.1.3" in content
    assert "[NOTICE](NOTICE)" in content
    assert "RunAsInvoker" in content
    assert "INV-STATIC-01" in content
    assert "INV-SLA-10" in content


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
    assert "DISCOVERABILITY, VISUAL ARCHITECTURE & METADATA AUDIT" in content


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
    assert "[PERSONA-01]" in content


def test_changelog_integrity():
    changelog_path = ROOT / "CHANGELOG.md"
    assert changelog_path.is_file(), "CHANGELOG.md must exist"
    content = changelog_path.read_text(encoding="utf-8")

    assert "## [Unreleased]" in content, "Unreleased section must be present in CHANGELOG.md"
    assert "[0.1.3]" in content, "Release [0.1.3] must be in CHANGELOG.md"
    assert "[0.1.2]" in content, "Release [0.1.2] must be in CHANGELOG.md"
    assert "[0.1.1]" in content, "Release [0.1.1] must be in CHANGELOG.md"
    assert "[0.1.0]" in content, "Release [0.1.0] must be in CHANGELOG.md"


def test_gitignore_hygiene():
    gitignore_path = ROOT / ".gitignore"
    assert gitignore_path.is_file(), ".gitignore must exist"
    content = gitignore_path.read_text(encoding="utf-8")

    assert "*.sync-conflict-*" in content, "Sync conflict pattern missing"
    assert "*-conflict-*" in content, "Multi-host conflict pattern missing"
    assert "* (kopie)*" in content, "Kopie pattern missing"
    assert "* (copy)*" in content, "Copy pattern missing"
    assert "*conflicted copy*" in content, "Conflicted copy pattern missing"
    assert "*-WORKSTATION*" in content, "Workstation pattern missing"
    assert "*-WORKSTATION.*" in content, "Workstation dot pattern missing"
    assert "*-WORKSTATION-LG*" in content, "Workstation LG pattern missing"
    assert "*-WORKSTATION-LG.*" in content, "Workstation LG dot pattern missing"
    assert "*-ASUS*" in content, "ASUS pattern missing"
    assert "*-ASUS-GEI*" in content, "ASUS host pattern missing"
    assert "*-MacBook*" in content, "MacBook pattern missing"
    assert ".pytest_cache/" in content, "pytest cache pattern missing"
    assert ".pytest_temp/" in content, "pytest temp directory pattern missing"
    assert ".ruff_cache/" in content, "ruff cache pattern missing"
    assert ".coverage.*" in content, "coverage glob pattern missing"
    assert ".tox/" in content, "tox cache pattern missing"
    assert "LOCK" in content, "LOCK pattern missing"
    assert "LOCK.user.*" in content, "LOCK.user.* pattern missing"
    assert "LOCK.until.*" in content, "LOCK.until.* pattern missing"
    assert "LOCK.condition.*" in content, "LOCK.condition.* pattern missing"
    assert ".automation-lock" in content, ".automation-lock pattern missing"
    assert "LOCK*.txt" in content, "LOCK*.txt pattern missing"
    assert "LOCK.permissions.json" in content, "LOCK.permissions.json missing"
    assert "uv.lock" in content, "uv.lock pattern missing"
    assert "!package-lock.json" in content, "package-lock.json whitelist missing"
    assert "*.rej" in content, "rej pattern missing"


def test_stale_workflow_contract():
    stale_path = ROOT / ".github" / "workflows" / "stale.yml"
    assert stale_path.is_file(), "Stale workflow file must exist"
    content = stale_path.read_text(encoding="utf-8")

    assert "actions/stale@v9" in content, "Stale action must use actions/stale@v9"
    assert "timeout-minutes: 10" in content, "Stale job must specify timeout-minutes: 10"
    assert "cancel-in-progress: true" in content, "Stale workflow must have concurrency protection"
    assert "cron: '30 1 * * *'" in content, "Stale workflow must run on daily cron schedule"
    assert "issues: write" in content, "Stale workflow must have write permission for issues"
    assert "pull-requests: write" in content, "Stale workflow must have write permission for pull requests"


def test_marketing_log_recency_and_audit():
    marketing_doc = ROOT / "MARKETING-LOG.txt"
    assert marketing_doc.is_file(), "MARKETING-LOG.txt must exist"
    content = marketing_doc.read_text(encoding="utf-8")

    assert "Audit Date: 2026-09-24" in content, "Marketing log must have 2026-09-24 audit date"
    assert "TECHNICAL HYGIENE & CI HARDENING AUDIT" in content, "Pfad A audit section must exist"
    assert "DISCOVERABILITY, VISUAL ARCHITECTURE & METADATA AUDIT" in content
    assert "Target Version: 0.1.3" in content, "Target version 0.1.3 must be recorded"


def test_readme_version_and_date_recency():
    readme_en = ROOT / "README.md"
    readme_de = ROOT / "README_de.md"
    assert readme_en.is_file() and readme_de.is_file()

    content_en = readme_en.read_text(encoding="utf-8")
    content_de = readme_de.read_text(encoding="utf-8")

    for content in (content_en, content_de):
        assert "version-0.1.3" in content, "Version badge 0.1.3 missing"
        assert "2026--09--24" in content, "Last-checked badge 2026-09-24 missing"


def test_llms_txt_version_and_date_recency():
    llms_path = ROOT / "llms.txt"
    assert llms_path.is_file()
    content = llms_path.read_text(encoding="utf-8")

    assert "- **Current Version**: 0.1.3" in content
    assert "- **Last Checked**: 2026-09-24" in content


def test_ci_timeout_minutes_contract():
    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    stale_path = ROOT / ".github" / "workflows" / "stale.yml"
    welcome_path = ROOT / ".github" / "workflows" / "welcome.yml"
    assert ci_path.is_file() and stale_path.is_file() and welcome_path.is_file()

    ci_content = ci_path.read_text(encoding="utf-8")
    stale_content = stale_path.read_text(encoding="utf-8")
    welcome_content = welcome_path.read_text(encoding="utf-8")

    assert "timeout-minutes: 15" in ci_content, "CI job must specify timeout-minutes: 15"
    assert "timeout-minutes: 10" in stale_content, "Stale job must specify timeout-minutes: 10"
    assert "timeout-minutes: 5" in welcome_content, "Welcome job must specify timeout-minutes: 5"


def test_welcome_workflow_contract():
    welcome_path = ROOT / ".github" / "workflows" / "welcome.yml"
    assert welcome_path.is_file(), "Welcome workflow file must exist"
    content = welcome_path.read_text(encoding="utf-8")

    assert "actions/first-interaction@v3" in content, "Welcome action must use first-interaction@v3"
    assert "timeout-minutes: 5" in content, "Welcome job must specify timeout-minutes: 5"
    assert "cancel-in-progress: true" in content, "Welcome workflow must have concurrency protection"
    assert "issues: write" in content, "Welcome workflow must have write permission for issues"
    assert "pull-requests: write" in content, "Welcome workflow must have write permission for pull requests"


def test_notice_attribution_contract():
    notice_path = ROOT / "NOTICE"
    assert notice_path.is_file(), "NOTICE attribution file must exist"
    content = notice_path.read_text(encoding="utf-8")

    assert "ellmos-ai-github-io" in content
    assert "Lukas Geiger" in content
    assert "ellmos-ai" in content
    assert "open-bricks" in content
    assert "MIT License" in content

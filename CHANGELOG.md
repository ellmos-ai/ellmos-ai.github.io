# Changelog

All notable changes to `ellmos-ai.github.io` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-09-10

### Added
- **Dual Mermaid Architectural Visualizations**: Integrated system architecture flowchart (`flowchart TB`) covering 5 operational layers (Client, Public Web Apps, Maintainer Layer, Security/Leak-Gate Isolation, Canonical Upstream Sources) and end-to-end maintenance/publishing sequence (`sequenceDiagram`) across both `README.md` and `README_de.md`.
- **10 Governance & Runtime Invariants**: Formalized and documented `INV-STATIC-01` through `INV-SLA-10` in `SECURITY.md`, `README.md`, `README_de.md`, and `llms.txt` covering 100% Static Zero-Egress, Fail-Closed Leak-Gates, Canonical Catalog Parity, Non-Elevation User Mode, Deterministic 7-Day Window Cadence, Atomic Content Commits, Fail-Closed Lock Discipline, Multi-OS Smoke Integrity, Pure Client-Side Execution, and 48h Response / 5-Day Triage SLA.
- **16-Repository Sibling Ecosystem Matrix**: Added structured cross-linking table connecting `ellmos-ai`, `dev-bricks`, `file-bricks`, `doc-bricks`, and `open-bricks` tools.
- **Third-Party License Inventory** (`THIRD_PARTY_LICENSES.md`): Full permissive open-source license accounting for 0 runtime frontend dependencies, Python standard library, pytest, and ruff.
- **Discoverability & Marketing Log** (`MARKETING-LOG.txt`): Repository-level discoverability, keyword inventory, audience personas, and metadata reference.
- **14-Point Quick Navigation**: Standardized 14-target quick navigation with 100% anchor parity between English and German documentation.
- **Contract Test Suite Expansion** (`tests/test_metadata.py`): Added contract tests asserting version 0.1.1, PEP 621 URLs, navigation anchors, dual Mermaid diagrams, 10 invariants table, ecosystem matrix, license accounting, and marketing log.

### Changed
- **Metadata & Tooling Updates** (`pyproject.toml`): Bumped version to `0.1.1`, configured pytest `addopts = "-ra -v"`, and added project URLs for Third-Party Licenses and Marketing Log.
- **.gitignore Hardening**: Hardened ignore rules against multi-host conflict files (`*-conflict-*`, `*.sync-conflict-*`, `*.sync-temp-*`, `*-ASUS-GEI.*`), lock variations (`LOCK`, `LOCK.*`, `*.lock`, `LOCK*.txt`, `LOCK.permissions.json`), and packaging scratch.
- **LLM Context Reference** (`llms.txt`): Updated to version 0.1.1, last-checked 2026-09-10, with explicit references to the 10 invariants and ecosystem matrix.

## [0.1.0] - 2026-09-08

### Added
- **GitHub Actions Multi-OS CI Workflow** (`.github/workflows/ci.yml`): Multi-OS Matrix (`ubuntu-latest`, `windows-latest`, `macos-latest`) across Python 3.10, 3.11, 3.12, and 3.13, using `actions/checkout@v4`, `actions/setup-python@v5` with pip caching (`cache: 'pip'`), automated concurrency cancellation (`cancel-in-progress: true`), Ruff linter, compileall bytecode verification, and Pytest test suite execution.
- **PEP 621 Standard Metadata** (`pyproject.toml`): Standardized ecosystem metadata, classifiers, and project URLs (Homepage, Documentation, Repository, Issues, Changelog, Security, Parent Organization, Umbrella Ecosystem) alongside Pytest and Ruff tool configurations.
- **Bilingual Security Policy** (`SECURITY.md`): Dual-language (English / Deutsch) security policy defining 5 core architectural security invariants (100% Static & Zero-Egress, Fail-Closed Leak-Gates, Deterministic & Idempotent Maintenance, Local-First & Non-Elevation, Fail-Closed Lock Discipline), supported versions matrix (`0.1.x`), 48h response SLA, and direct security contacts (`security@ellmos.ai`, `support@lukasgeiger.com`, `lukas@open-bricks.org`).
- **Automated Metadata & Hygiene Contract Suite** (`tests/test_metadata.py`): 9 contract tests verifying CI workflow integrity, PEP 621 metadata, security policy commitments, site artifact presence, leak-gate invariants, bilingual README parity, `llms.txt` correctness, changelog integrity, and `.gitignore` hygiene.
- **German README Parity** (`README_de.md`): Comprehensive German documentation matching `README.md` with Shields.io badges, architecture overview, maintenance documentation, and quick navigation.
- **Machine-Readable LLM Context** (`llms.txt`): Standardized documentation file for AI agents and LLMs detailing project scope, site artifacts, verification procedures, and maintainer workflows.

### Changed
- **.gitignore Hardening**: Added patterns for `.pytest_cache/`, `.ruff_cache/`, sync conflict artifacts (`*.sync-conflict-*`, `*.conflict`, `*-CONFLIT-*`), locks, and temporary files.
- **README.md Synchronization**: Added Shields.io status badges (CI, tests passed, Python 3.10-3.13, platforms, zero-egress privacy, local-first security, MIT license, ecosystem) and structured quick navigation.

## [0.0.1] - 2026-08-30

### Added
- **Interactive Ecosystem Maps**:
  - `index.html`: Module Circuit Map for functional ecosystem exploration (DE/EN, dark/light themes).
  - `bundles.html`: Bundle Recipes showing composition recipes, requirements, and module dependencies.
  - `skills.html`: Self-contained Skill Library with inline viewer and copy-to-clipboard functionality.
  - `stack-composer.html`: Interactive Stack Composer with composition rule enforcement and `stack.v2.json` export.
- **Pages Maintainer & Automation** (`_tools/pages_maintainer.py`, `_tools/FALLBACK-AUTOMATION.md`): 7-day windowed maintenance runner with fail-closed leak gates, catalog verification, and idempotent site content commits.
- **Initial Verification Suite** (`tests/test_pages_maintainer.py`): 5 unit tests for maintainer windows, change detection, and generator input validation.

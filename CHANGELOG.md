# Changelog

All notable changes to `ellmos-ai.github.io` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

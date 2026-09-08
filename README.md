<img src="assets/banner.png" width="100%" alt="ellmos-ai.github.io Banner">

# ellmos-ai.github.io — interactive maps of the ellmos ecosystem

[![CI](https://github.com/ellmos-ai/ellmos-ai.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/ellmos-ai/ellmos-ai.github.io/actions/workflows/ci.yml)
![Tests](https://img.shields.io/badge/tests-14%20passed-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Privacy](https://img.shields.io/badge/privacy-100%25%20Offline%20%2F%20Zero--Egress-brightgreen)
![Security](https://img.shields.io/badge/security-Local--First%20%2F%20Fail--Closed-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Ecosystem](https://img.shields.io/badge/ecosystem-ellmos--ai-blue)
![Umbrella](https://img.shields.io/badge/umbrella-open--bricks-orange)
[![LLM-Ready](https://img.shields.io/badge/LLM--Ready-llms.txt-blue)](llms.txt)

---

**[English](README.md)** | **[Deutsch](README_de.md)** | **[Live Site](https://ellmos-ai.github.io)** | **[Pages Overview](#pages-overview)** | **[Maintenance](#maintenance)** | **[Security Policy](SECURITY.md)** | **[Changelog](CHANGELOG.md)** | **[llms.txt](llms.txt)**

---

Live at **https://ellmos-ai.github.io**

## Pages Overview

| Page | What it shows |
|---|---|
| [`index.html`](https://ellmos-ai.github.io) | **Module Circuit Map** — the functional areas of the ellmos construction kit, how they work together, and every public module with its purpose (DE/EN, dark/light) |
| [`bundles.html`](https://ellmos-ai.github.io/bundles.html) | **Bundle Recipes** — the 13 released composition recipes (first rollout wave): which modules, skills and apps make up each bundle, with requirement levels |
| [`skills.html`](https://ellmos-ai.github.io/skills.html) | **Skill Library** — the public SKILL.md library, readable in place, copy-to-clipboard |
| [`stack-composer.html`](https://ellmos-ai.github.io/stack-composer.html) | **Stack Composer** — assemble your own stack from public modules, with live composition-rule checks and `stack.v2.json` export |

These pages are self-contained build artifacts (no build system in this repo, no external requests, no tracking). They are generated from the ellmos module catalogs in the private workspace and show the **public excerpt** of the ecosystem — the full system contains additional private modules and the recipe layer.

## Architecture & Security Invariants

As specified in [`SECURITY.md`](SECURITY.md):
- **100% Static & Zero-Egress**: All deployed pages are self-contained HTML/CSS/JS files without tracking or third-party requests.
- **Fail-Closed Leak-Gates**: The maintenance tool ensures no non-public module IDs (`vis:"priv"`, `vis:"cand"`) leak into public pages.
- **Deterministic Maintenance**: Idempotent maintenance cycles anchored to 7-day windows.
- **Local-First & Non-Elevation**: Runs fully in user-mode space without elevated permissions.
- **Fail-Closed Lock Discipline**: Prevents concurrent build conflicts through atomic lockfiles.

## Maintenance

`_tools/pages_maintainer.py` couples the generated site to the system-auditor's fixed seven-day window. It runs both workspace generators, keeps the publication gates fail-closed, and commits only when generated site content changed. Push is a separate `--push` flag.

```powershell
$env:PYTHONIOENCODING='utf-8'
python _tools/pages_maintainer.py --check
python _tools/pages_maintainer.py --run
```

The Desktop-app fallback command and scheduling hand-off are documented in [`_tools/FALLBACK-AUTOMATION.md`](_tools/FALLBACK-AUTOMATION.md). The repository contains no Desktop Scheduled Task or Codex automation definition.

## Verification & Testing

The repository includes an automated test suite with Pytest and Ruff linting:

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m ruff check .
python -m pytest -v
```

## Community & Ecosystem

- **Parent Organization**: https://github.com/ellmos-ai
- **Umbrella Organization**: https://github.com/open-bricks
- **Bug Tracker & Issues**: https://github.com/ellmos-ai/ellmos-ai.github.io/issues

## Lizenz / License

MIT — see [LICENSE](LICENSE).

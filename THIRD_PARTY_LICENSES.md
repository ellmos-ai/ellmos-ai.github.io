# Third-Party Licenses and Open-Source Notices

`ellmos-ai.github.io` is distributed under the terms of the [MIT License](LICENSE).
This document inventories all external dependencies, libraries, and open-source tooling used at runtime or during development and testing.

---

## 1. Web Frontend & Interactive Client Surfaces

### Zero External Runtime Dependencies (100% Self-Contained)
- **Architecture:** Pure native HTML5, modern CSS3, and Vanilla ECMAScript (JavaScript).
- **External CDN Calls:** None (0 external script/style/font requests).
- **Tracking / Telemetry:** None (0 analytics, 0 cookies, 0 beacons).
- **Offline / Local Execution:** All interactive functionality (dark/light theme switching, module circuit map filtering, bundle recipe inspection, skill library browser, and stack composer canvas) executes entirely within the client's web browser environment without third-party network interaction.

---

## 2. Maintenance & Validation Tooling

### Python Standard Library (`pathlib`, `json`, `subprocess`, `argparse`, `dataclasses`, `typing`, `datetime`)
- **Homepage:** https://www.python.org/
- **License:** Python Software Foundation License (PSFL) Version 2
- **Copyright:** (c) 2001-2026 Python Software Foundation
- **Usage:** Powers the idempotent site maintainer (`_tools/pages_maintainer.py`), fail-closed leak-gate verification, catalog parsing, file hashing, and automated test fixtures.

---

## 3. Development, Testing & Code Quality Dependencies

### pytest (`pytest`)
- **Homepage:** https://pytest.org/
- **License:** MIT License
- **Copyright:** (c) 2004-2026 Holger Krekel and pytest-dev contributors
- **Usage:** Automated test runner executing maintainer tests, leak-gate validation, metadata parity checks, and architectural invariant assertions.

### Ruff (`ruff`)
- **Homepage:** https://astral.sh/ruff
- **License:** MIT License / Apache License 2.0
- **Copyright:** (c) 2023-2026 Astral Software Inc.
- **Usage:** High-performance static Python linting, formatting, and AST analysis across `_tools/` and `tests/`.

---

## Summary of License Compliance & Invariants Certification

- **Audit Date:** 2026-09-18
- **Audited Target Version:** 0.1.3
- **Runtime Dependencies:** 0 external packages (100% self-contained native web frontend).
- **Execution Mode:** Unprivileged User-Mode (`RunAsInvoker`), 0 administrative privileges required.
- **Copyleft Contagion Risk:** 0% (All build and development dependencies are permissively licensed under MIT, Apache-2.0, or PSFL).

### Governance & Runtime Invariant Mapping

| Invariant | Description | Compliance Status |
|---|---|---|
| `INV-STATIC-01` | 100% Static & Zero Network Egress (0 CDNs, 0 telemetry) | Verified & Compliant |
| `INV-LEAK-02` | Fail-Closed Leak-Gates (blocks vis:priv & vis:cand) | Verified & Compliant |
| `INV-CATALOG-03` | Canonical Catalog Parity (matched against .SKILLS) | Verified & Compliant |
| `INV-RUNAS-04` | Local-First & Non-Elevation (RunAsInvoker User Mode) | Verified & Compliant |
| `INV-WINDOW-05` | Deterministic 7-Day Window Cadence (system-auditor) | Verified & Compliant |
| `INV-DIFF-06` | Atomic Content-Change Commits (gated by diffs) | Verified & Compliant |
| `INV-LOCK-07` | Fail-Closed Lock Discipline (LOCK.pages-maintainer.txt) | Verified & Compliant |
| `INV-OS-08` | Multi-OS Platform Parity & Smoke Integrity (Py 3.10-3.13) | Verified & Compliant |
| `INV-CLIENT-09` | Pure Client-Side Static Execution (offline browser JS) | Verified & Compliant |
| `INV-SLA-10` | 48h Response & 5-Day Triage SLA (SECURITY.md) | Verified & Compliant |

All tooling and build dependencies are permissively licensed (MIT, Apache-2.0, PSFL).
The deployed web pages contain no external third-party software libraries or copyleft code, ensuring full compliance and frictionless open-source distribution under the MIT license.

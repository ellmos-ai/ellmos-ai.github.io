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

## Summary of License Compliance

All tooling and build dependencies are permissively licensed (MIT, Apache-2.0, PSFL).
The deployed web pages contain no external third-party software libraries or copyleft code, ensuring full compliance and frictionless open-source distribution under the MIT license.

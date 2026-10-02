# Contributing to ellmos-ai.github.io / Mitwirken an ellmos-ai.github.io

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

Thank you for your interest in contributing to **ellmos-ai.github.io** (`ellmos-ai/ellmos-ai.github.io`), the official interactive public showcase, module circuit diagram explorer, curated bundle recipe catalog, and visual stack composer for the modular ellmos AI framework.

### 1. Architectural Principles & 10 Governance Invariants

All contributions must strictly adhere to our core architectural invariants:

1. **100% Static & Zero Network Egress (`INV-STATIC-01`)**: Pure client-side static web deployment. Zero external telemetry, zero tracking cookies, zero analytics beacons, and zero third-party CDNs. All scripts and styles are self-contained.
2. **Fail-Closed Leak-Gates (`INV-LEAK-02`)**: Automated verification during site building blocks any internal, draft, or candidate items (`vis: "priv"`, `vis: "cand"`) from leaking into public web artifacts.
3. **Canonical Catalog Parity (`INV-CATALOG-03`)**: Parity verification ensuring public skill descriptions and module definitions strictly mirror approved excerpts from the central catalog.
4. **Unprivileged User Mode (`INV-RUNAS-04`)**: Pure `RunAsInvoker` non-elevation user mode. All tools, generators, and test suites execute without root or administrative privileges.
5. **Deterministic Window Cadence (`INV-WINDOW-05`)**: Scheduled maintainer jobs operate on deterministic 7-day windows anchored to Mondays with full reproducibility.
6. **Atomic Content Commits (`INV-DIFF-06`)**: Automated site commits only occur when rendered content actually changes, preventing empty churn commits.
7. **Multi-Agent Lock Discipline (`INV-LOCK-07`)**: Strict adherence to canonical lock files (`LOCK.pages-maintainer.txt`, `LOCK-SYSTEM.md`) preventing race conditions during automation runs.
8. **Multi-OS Platform Parity (`INV-OS-08`)**: Deterministic testing across Ubuntu, Windows, and macOS runners (`ci.yml`) on Python 3.10 through 3.13.
9. **Pure Client-Side Static Execution (`INV-CLIENT-09`)**: All interactive components (theme switching, circuit map filtering, stack composition) execute entirely in the user's browser without server-side dependencies.
10. **Security Response SLA (`INV-SLA-10`)**: Binding 48-hour initial response SLA and 5-business-day triage commitment for all reported vulnerabilities via `security@ellmos.ai` and `lukas@open-bricks.org`.

### 2. Plan D Local Development Workflow

In accordance with our cross-system architecture (Plan D), the local git repository at `C:\_Local_DEV\repos\ellmos-ai.github.io` serves as the authoritative **Source of Truth**. Development, testing, and commits must take place exclusively in the canonical local clone.

```bash
# Clone the canonical repository
git clone https://github.com/ellmos-ai/ellmos-ai.github.io.git C:\_Local_DEV\repos\ellmos-ai.github.io
cd C:\_Local_DEV\repos\ellmos-ai.github.io

# Run automated test suite
pytest -ra -v

# Run static linting
ruff check .

# Verify Python bytecode compilation
python -m compileall -q _tools tests .
```

### 3. Version Freeze Discipline (`T-20260920-167562623`)

`ellmos-ai.github.io` operates under strict version-freeze discipline. Version `0.1.3` in `pyproject.toml` and documentation badges must not be incremented without explicit release authorization. All technical hygiene, documentation updates, and workflow additions are documented under `## [Unreleased]` in `CHANGELOG.md`.

### 4. Quality Gates

Before submitting a pull request, verify that all local quality gates pass:
1. `pytest`: 100% green test execution across all contract and unit suites.
2. `ruff check .`: Zero lint errors.
3. `python -m compileall -q _tools tests .`: Zero bytecode compilation errors.
4. `git diff --check`: Zero whitespace anomalies.
5. `git diff -G"version = "`: Zero unauthorized version bumps.

### 5. Statutory Notice (§ 521 BGB) & Liability Disclaimer

This software is provided free of charge as open-source software under the MIT License. In accordance with statutory German law (§ 521 BGB - Gefälligkeitsrecht), liability for defects in quality and title is strictly limited to intentional misconduct (*Vorsatz*) and gross negligence (*grobe Fahrlässigkeit*).

---

<a id="deutsch"></a>
## Deutsch

Vielen Dank für dein Interesse an einer Mitwirkung bei **ellmos-ai.github.io** (`ellmos-ai/ellmos-ai.github.io`), dem offiziellen interaktiven Web-Portal, Modul-Schaltplan-Explorer, kuratierten Bundle-Rezept-Katalog und visuellen Stack-Composer für das modulare ellmos KI-Framework.

### 1. Architektur-Prinzipien & 10 Governance-Invarianten

Alle Beiträge müssen unsere verbindlichen Kern-Invarianten strikt einhalten:

1. **100% Statisch & Zero Network Egress (`INV-STATIC-01`)**: Reine clientseitige statische Bereitstellung. Null ausgehende Telemetrie, null Tracking-Cookies, null Analyse-Beacons und null Drittanbieter-CDNs. Alle Skripte und Stylesheets sind vollständig autark.
2. **Fail-Closed Leak-Gates (`INV-LEAK-02`)**: Automatisierte Validierungsprüfungen beim Build verhindern das Durchsickern interner oder nicht-öffentlicher Entwürfe (`vis: "priv"`, `vis: "cand"`) in öffentliche Artefakte.
3. **Kanonische Katalog-Parität (`INV-CATALOG-03`)**: Paritätsprüfung stellt sicher, dass öffentliche Skill- und Modulbeschreibungen bitgenau den freigegebenen Auszügen des zentralen Katalogs entsprechen.
4. **Rechtefreier Benutzermodus (`INV-RUNAS-04`)**: Reiner `RunAsInvoker`-Benutzermodus ohne administrative Rechte. Alle Generatoren, Maintainer und Testsuiten laufen uneingeschränkt ohne Root-/Admin-Rechte.
5. **Deterministiche Fenster-Kadenz (`INV-WINDOW-05`)**: Geplante Maintainer-Jobs operieren auf reproduzierbaren 7-Tage-Fenstern mit Montags-Verankerung.
6. **Atomare Inhalts-Commits (`INV-DIFF-06`)**: Automatisierte Commits erfolgen nur bei echten Inhaltsänderungen der generierten Web-Seiten, um Leer-Commits zu vermeiden.
7. **Multi-Agenten Lock-Disziplin (`INV-LOCK-07`)**: Strikte Einhaltung des kanonischen Sperrsystems (`LOCK.pages-maintainer.txt`, `LOCK-SYSTEM.md`) zur Vermeidung von Parallelitätskonflikten.
8. **Plattformübergreifende CI-Parität (`INV-OS-08`)**: Deterministische Testmatrix über Ubuntu, Windows und macOS (`ci.yml`) auf Python 3.10 bis 3.13.
9. **Reine clientseitige Ausführung (`INV-CLIENT-09`)**: Alle interaktiven Komponenten (Farbschema-Umschaltung, Schaltplan-Filterung, Stack-Komposition) laufen vollständig im Browser des Nutzers ohne Backend.
10. **Sicherheits-Response SLA (`INV-SLA-10`)**: Verbindliche 48-Stunden-Erstantwortgarantie und 5-Werktage-Triage-Zusage für Sicherheitsmeldungen über `security@ellmos.ai` und `lukas@open-bricks.org`.

### 2. Plan D Lokaler Entwicklungsworkflow

Gemäß unserer systemweiten Architektur (Plan D) bildet das lokale Repository unter `C:\_Local_DEV\repos\ellmos-ai.github.io` die alleinige maßgebliche **Source of Truth**. Entwicklung, Tests und Commits finden ausschließlich im kanonischen lokalen Klon statt.

```bash
# Kanonischen Klon verwenden
git clone https://github.com/ellmos-ai/ellmos-ai.github.io.git C:\_Local_DEV\repos\ellmos-ai.github.io
cd C:\_Local_DEV\repos\ellmos-ai.github.io

# Testsuite ausführen
pytest -ra -v

# Linter ausführen
ruff check .

# Python Bytecode prüfen
python -m compileall -q _tools tests .
```

### 3. Versions-Freeze-Disziplin (`T-20260920-167562623`)

`ellmos-ai.github.io` unterliegt einer strikten Versions-Freeze-Disziplin. Die Version `0.1.3` in `pyproject.toml` und den Badges bleibt unverändert. Alle Verbesserungen, Hygiene-Maßnahmen und Ergänzungen werden unter `## [Unreleased]` in `CHANGELOG.md` erfasst.

### 4. Qualitäts-Tore (Quality Gates)

Vor jedem Pull Request müssen alle lokalen Prüfungen erfolgreich sein:
1. `pytest`: 100% bestandene Tests über alle Vertrags- und Modultests.
2. `ruff check .`: 0 Linter-Fehler.
3. `python -m compileall -q _tools tests .`: 0 Bytecode-Kompilierungsfehler.
4. `git diff --check`: 0 Formatierungs- oder Whitespace-Fehler.
5. `git diff -G"version = "`: 0 unautorisierte Versionsänderungen.

### 5. Gesetzlicher Haftungsausschluss (§ 521 BGB)

Diese Software wird unentgeltlich als Open-Source-Software unter den Bedingungen der MIT-Lizenz bereitgestellt. Gemäß § 521 BGB (Haftung bei Schenkung und Gefälligkeit) ist die Haftung des Betreibers und der Mitwirkenden für Sach- und Rechtsmängel auf Vorsatz und grobe Fahrlässigkeit beschränkt.

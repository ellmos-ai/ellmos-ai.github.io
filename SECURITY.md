# Security Policy / Sicherheitsrichtlinie

**[English](#english)** | **[Deutsch](#deutsch)**

---

<a name="english"></a>
## English

### Security & Privacy Invariants

`ellmos-ai.github.io` hosts the interactive maps, bundle recipes, skill directory, and stack composer for the ellmos ecosystem. Because it renders and visualizes public module architectures and component inventories, it strictly enforces the following 10 architectural security and runtime invariants:

| Invariant ID | Guarantee | Specification & Implementation Details |
|---|---|---|
| `INV-STATIC-01` | **100% Static & Zero Network Egress** | All deployed pages (`index.html`, `bundles.html`, `skills.html`, `stack-composer.html`) are self-contained static HTML/CSS/JavaScript documents. Zero external telemetry, zero tracking scripts, zero user analytics, and zero external third-party CDN dependencies. All rendering logic executes locally within the user's browser. |
| `INV-LEAK-02` | **Fail-Closed Leak-Gates** | The maintainer suite (`_tools/pages_maintainer.py`) strictly validates public site artifacts against canonical catalogs before publication. Private module identifiers and non-public visibility markers (`vis:"priv"`, `vis:"cand"`) trigger an immediate fail-closed abort. |
| `INV-CATALOG-03` | **Canonical Catalog Parity** | Skill catalog counts and module inventories must strictly match canonical `.SKILLS` and module registry definitions. Any discrepancy halts the generation process. |
| `INV-RUNAS-04` | **Local-First & Non-Elevation (User Mode)** | All build and maintenance scripts run completely unprivileged in standard user space (`RunAsInvoker`). Administrator or root privileges are never requested, required, or assumed. |
| `INV-WINDOW-05` | **Deterministic 7-Day Window Cadence** | Automated site maintenance is strictly bounded by deterministic 7-day windows anchored to Mondays, synchronized with `system-auditor` evidence runs. |
| `INV-DIFF-06` | **Atomic Content-Change Commits** | Git commits are generated exclusively when verified, leak-free site content has actually changed from HEAD, preventing noisy empty commits. |
| `INV-LOCK-07` | **Fail-Closed Lock Discipline** | Repository and workspace lock semantics (`LOCK.pages-maintainer.txt`, canonical LOCK rules) are enforced to ensure atomic runs and eliminate race conditions across multi-agent environments. |
| `INV-OS-08` | **Multi-OS Platform Parity & Smoke Integrity** | Automated GitHub Actions CI workflow runs on `ubuntu-latest`, `windows-latest`, and `macos-latest` across Python 3.10-3.13 with bytecode compilation gates and Ruff linter. |
| `INV-CLIENT-09` | **Pure Client-Side Static Execution** | Dark/light theme toggles, circuit map filtering, bundle recipe inspection, and stack composer logic run 100% in client-side JavaScript without backend servers or server-side state. |
| `INV-SLA-10` | **48h Response & 5-Day Triage SLA** | Mandatory 48-hour response SLA for initial vulnerability acknowledgment and 5 business days for complete triage assessment. |

### Supported Versions

| Version | Supported | Notes |
|---------|-----------|-------|
| `0.1.x` | :white_check_mark: | Active release stream |
| `< 0.1.0` | :x: | Legacy / pre-release revisions |

### Reporting a Vulnerability

If you discover a security vulnerability, leak-gate discrepancy, or unexpected information exposure in `ellmos-ai.github.io`:

1. **Do not open a public issue.**
2. Report the vulnerability privately via [GitHub Security Advisories](https://github.com/ellmos-ai/ellmos-ai.github.io/security/advisories) or directly to the security team at [security@ellmos.ai](mailto:security@ellmos.ai) (fallback: [support@lukasgeiger.com](mailto:support@lukasgeiger.com), [lukas@open-bricks.org](mailto:lukas@open-bricks.org)).
3. Please include detailed reproduction steps, environment details, relevant logs, and expected versus observed behavior.
4. **Service Level Agreement (SLA):** We acknowledge receipt within **48 hours** and provide a completed triage assessment and remediation schedule within **5 business days**.

---

<a name="deutsch"></a>
## Deutsch

### Sicherheits- & Datenschutz-Invarianten

`ellmos-ai.github.io` stellt die interaktiven Architekturkarten, Bundle-Rezepte, Skill-Bibliotheken und den Stack-Composer des ellmos-Ökosystems bereit. Da öffentliche Modulstrukturen und Komponenten-Inventare visualisiert werden, gelten 10 verbindliche Sicherheits- und Laufzeit-Invarianten:

| Invarianten-ID | Garantie | Spezifikation & Implementierungsdetails |
|---|---|---|
| `INV-STATIC-01` | **100% Static- & Zero-Egress-Invariante** | Alle bereitgestellten Webseiten (`index.html`, `bundles.html`, `skills.html`, `stack-composer.html`) sind vollständig in sich geschlossene statische Dokumente. Keine externe Telemetrie, keine Tracking-Skripte, keine Analysen, keine externen CDNs. Ausführung erfolgt lokal im Browser. |
| `INV-LEAK-02` | **Fail-Closed Leak-Gates** | Die Maintainer-Suite (`_tools/pages_maintainer.py`) prüft generierte Artefakte vor Publikation strikt gegen den kanonischen Katalog. Funde von `vis:"priv"` oder `vis:"cand"` führen zum sofortigen fail-closed Abbruch. |
| `INV-CATALOG-03` | **Kanonische Katalog-Parität** | Skill- und Modulzahlen müssen exakt mit der kanonischen `.SKILLS`-Registry und dem Modulinventar übereinstimmen. |
| `INV-RUNAS-04` | **Local-First & Keine Rechteausweitung (User-Mode)** | Alle Skripte und Werkzeuge laufen unprivilegiert im regulären Benutzerkontext (`RunAsInvoker`). Administrator- oder Root-Rechte werden weder benötigt noch angefordert. |
| `INV-WINDOW-05` | **Deterministische 7-Tage-Fenster-Wartung** | Automatisierte Wartungsläufe sind an feste 7-Tage-Fenster gekoppelt, synchronisiert mit den Evidenzläufen des `system-auditor`. |
| `INV-DIFF-06` | **Atomare inhaltsbasierte Commits** | Git-Commits werden ausschließlich erzeugt, wenn sich verifizierte, leak-geprüfte Seiteninhalte tatsächlich von HEAD unterscheiden. |
| `INV-LOCK-07` | **Fail-Closed Lock-Disziplin** | Transaktionale Sperrdateien (`LOCK.pages-maintainer.txt`, kanonische LOCK-Systemregeln) verhindern Nebenläufigkeitskonflikte und stellen atomare Abläufe sicher. |
| `INV-OS-08` | **Multi-OS Plattformparität & Smoke-Integrität** | Automatisiertes GitHub Actions CI über `ubuntu-latest`, `windows-latest` und `macos-latest` auf Python 3.10-3.13 mit Bytecode-Kompilierungsgate und Ruff-Linter. |
| `INV-CLIENT-09` | **Reine clientseitige statische Ausführung** | Farb- und Themenschemata, Filter der Modulkarte, Bundle-Inspektion und Stack-Composer laufen vollständig in clientseitigem JavaScript ohne Server-Backend. |
| `INV-SLA-10` | **48h Antwort- & 5-Tage-Triage-SLA** | Verbindliche 48-Stunden-Eingangsbestätigung sowie vollständige Triage- und Behebungszusage innerhalb von 5 Werktagen. |

### Unterstützte Versionen

| Version | Unterstützt | Hinweise |
|---------|-------------|----------|
| `0.1.x` | :white_check_mark: | Aktiver Release-Zweig |
| `< 0.1.0` | :x: | Frühere / experimentelle Stände |

### Melden einer Schwachstelle

Wenn Sie eine Sicherheitslücke oder unerwartete Offenlegung in `ellmos-ai.github.io` entdecken:

1. **Eröffnen Sie kein öffentliches Issue.**
2. Melden Sie die Schwachstelle vertraulich über [GitHub Security Advisories](https://github.com/ellmos-ai/ellmos-ai.github.io/security/advisories) oder direkt per E-Mail an [security@ellmos.ai](mailto:security@ellmos.ai) (Fallback: [support@lukasgeiger.com](mailto:support@lukasgeiger.com), [lukas@open-bricks.org](mailto:lukas@open-bricks.org)).
3. Bitte fügen Sie Reproduktionsschritte, Umgebungsdetails, Protokolle sowie das erwartete und beobachtete Verhalten bei.
4. **Service Level Agreement (SLA):** Wir bestätigen den Eingang innerhalb von **48 Stunden** und übermitteln innerhalb von **5 Werktagen** eine qualifizierte Triage-Einschätzung sowie den Behebungszeitplan.

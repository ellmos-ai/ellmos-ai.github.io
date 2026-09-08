# Security Policy / Sicherheitsrichtlinie

**[English](#english)** | **[Deutsch](#deutsch)**

---

<a name="english"></a>
## English

### Security & Privacy Invariants

`ellmos-ai.github.io` hosts the interactive maps, bundle recipes, skill directory, and stack composer for the ellmos ecosystem. Because it renders and visualizes public module architectures and component inventories, it strictly enforces the following architectural security invariants:

1. **100% Static & Zero-Egress Invariant**:
   - All deployed pages (`index.html`, `bundles.html`, `skills.html`, `stack-composer.html`) are completely self-contained static HTML/CSS/JavaScript documents.
   - Zero external telemetry, zero tracking scripts, zero user analytics, and zero external third-party CDN dependencies. All rendering logic executes locally and strictly inside the user's browser.
2. **Fail-Closed Leak-Gates & Content Verification**:
   - The maintainer suite (`_tools/pages_maintainer.py`) strictly validates public site artifacts against the canonical ecosystem catalog before any publication.
   - Private module identifiers and non-public visibility markers (`vis:"priv"`, `vis:"cand"`) are strictly blocked; any presence triggers an immediate fail-closed abort.
   - Skill catalog counts must strictly match canonical registry definitions; any discrepancy halts the generation process.
3. **Deterministic & Idempotent Maintenance**:
   - Automated site maintenance is strictly bounded by deterministic 7-day windows and explicit evidence tracking.
   - Git commits are created exclusively when verified, leak-free site content has actually changed.
4. **Local-First & Non-Elevation (User-Mode Operation)**:
   - All build and maintenance scripts run completely unprivileged in standard user space. Administrator or root privileges are never requested, required, or assumed.
5. **Fail-Closed Lock Discipline**:
   - Repository and workspace lock semantics (`LOCK.pages-maintainer.txt`, canonical LOCK rules) are enforced to ensure atomic runs and eliminate race conditions across multi-agent environments.

### Supported Versions

| Version | Supported | Notes |
|---------|-----------|-------|
| `0.1.x` | :white_check_mark: | Active release stream |
| `< 0.1.0` | :x: | Legacy / pre-release revisions |

### Reporting a Vulnerability

If you discover a security vulnerability or unexpected information exposure in `ellmos-ai.github.io`:

1. **Do not open a public issue.**
2. Report the vulnerability privately via [GitHub Security Advisories](https://github.com/ellmos-ai/ellmos-ai.github.io/security/advisories) or directly to the security team at [security@ellmos.ai](mailto:security@ellmos.ai) (fallback: [support@lukasgeiger.com](mailto:support@lukasgeiger.com), [lukas@open-bricks.org](mailto:lukas@open-bricks.org)).
3. Please include detailed reproduction steps, environment details, relevant logs, and expected versus observed behavior.
4. We acknowledge receipt within 48 hours and coordinate remediation releases promptly.

---

<a name="deutsch"></a>
## Deutsch

### Sicherheits- & Datenschutz-Invarianten

`ellmos-ai.github.io` stellt die interaktiven Architekturkarten, Bundle-Rezepte, Skill-Bibliotheken und den Stack-Composer des ellmos-Ökosystems bereit. Da öffentliche Modulstrukturen und Komponenten-Inventare visualisiert werden, gelten verbindliche Sicherheitsinvarianten:

1. **100% Static- & Zero-Egress-Invariante**:
   - Alle bereitgestellten Webseiten (`index.html`, `bundles.html`, `skills.html`, `stack-composer.html`) sind vollständig in sich geschlossene statische HTML/CSS/JavaScript-Dokumente.
   - Keine externe Telemetrie, keine Tracking-Skripte, keine Nutzeranalysen und keine externen CDN-Abhängigkeiten. Die gesamte Logik läuft lokal im Webbrowser des Nutzers.
2. **Fail-Closed Leak-Gates & Inhaltsverifikation**:
   - Die Maintainer-Suite (`_tools/pages_maintainer.py`) prüft die generierten Artefakte vor jeder Publikation strikt gegen den kanonischen Modulkatalog.
   - Nicht-öffentliche Modul-IDs und private Sichtbarkeitsmarker (`vis:"priv"`, `vis:"cand"`) werden strikt blockiert; Funde führen zum sofortigen fail-closed Abbruch.
   - Skill-Zahlen müssen exakt mit der kanonischen Skill-Registry übereinstimmen.
3. **Deterministische & idempotente Wartung**:
   - Automatisierte Wartungsläufe sind an feste 7-Tage-Fenster und belastbare Evidenzen gekoppelt.
   - Git-Commits werden ausschließlich erzeugt, wenn sich verifizierte, leak-geprüfte Seiteninhalte tatsächlich geändert haben.
4. **Local-First & Keine Rechteausweitung (User-Mode-Betrieb)**:
   - Alle Skripte und Werkzeuge laufen unprivilegiert im regulären Benutzerkontext. Administrator- oder Root-Rechte werden weder benötigt noch angefordert.
5. **Fail-Closed Lock-Disziplin**:
   - Transaktionale Lock-Dateien (`LOCK.pages-maintainer.txt`, kanonische LOCK-Systemregeln) verhindern Nebenläufigkeitskonflikte und stellen atomare Abläufe sicher.

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
4. Wir bestätigen den Eingang innerhalb von 48 Stunden und koordinieren umgehend eine Behebung.

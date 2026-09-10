<img src="assets/banner.png" width="100%" alt="ellmos-ai.github.io Banner">

# ellmos-ai.github.io — Interaktive Karten des ellmos-Ökosystems

**Offizielles öffentliches Webportal, interaktive Modul-Schaltpläne, Bundle-Rezepte, Skill-Bibliothek und visueller Stack-Composer für das modulare ellmos KI-Framework.**

<p align="center">
  <a href="https://github.com/ellmos-ai/ellmos-ai.github.io"><img src="https://img.shields.io/badge/version-0.1.1-blue" alt="Version 0.1.1"></a>
  <a href="https://github.com/ellmos-ai/ellmos-ai.github.io/actions/workflows/ci.yml"><img src="https://img.shields.io/badge/CI-passing-brightgreen" alt="CI Status"></a>
  <a href="tests/"><img src="https://img.shields.io/badge/tests-18%20passed%20%7C%20100%25%20green-brightgreen" alt="Tests 18 Passed"></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue" alt="Python 3.10+"></a>
  <a href="https://github.com/ellmos-ai/ellmos-ai.github.io"><img src="https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20macOS-blue" alt="Plattformen"></a>
  <a href="https://ellmos-ai.github.io"><img src="https://img.shields.io/badge/web%20ui-Statisches%20HTML5%20%26%20Vanilla%20JS-informational" alt="Web UI"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/privacy-100%25%20Offline%20%2F%20Zero--Egress-success" alt="Datenschutz: Zero-Egress"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/security-Local--First%20%2F%20Non--Elevation-success" alt="Sicherheit: Non-Elevation"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/security%20SLA-48h%20Response%20%7C%205d%20Triage-blue" alt="Sicherheits-SLA"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/badge/code%20style-ruff-black" alt="Code-Stil: Ruff"></a>
  <a href="https://github.com/ellmos-ai"><img src="https://img.shields.io/badge/ecosystem-ellmos--ai-informational" alt="Ökosystem: ellmos-ai"></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/umbrella-open--bricks-blueviolet" alt="Dachorganisation: open-bricks"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/LLM--Ready-llms.txt-orange" alt="LLM-Ready"></a>
  <a href="https://github.com/ellmos-ai/ellmos-ai.github.io"><img src="https://img.shields.io/badge/last--checked-2026--09--10-blue" alt="Zuletzt geprüft"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="Lizenz: MIT"></a>
</p>

<p align="center"><a href="README.md">English</a> · <strong>Deutsch</strong> · <a href="https://ellmos-ai.github.io">Live-Portal</a></p>

> [!NOTE]
> Für KI-Agenten-Kontext, maschinenlesbare Schemata und architektonische Invarianten siehe [`llms.txt`](llms.txt).
> Alle bereitgestellten Webseiten laufen zu 100% offline im Browser des Nutzers – ohne externe Telemetrie, ohne Tracking und ohne Drittanbieter-CDNs.

---

## Schnellnavigation

- [Interaktive Ökosystem-Übersicht](#interaktive-ökosystem-übersicht)
- [Systemarchitektur & Datenfluss](#systemarchitektur--datenfluss)
- [Wartungs- & Publikationssequenz](#wartungs--publikationssequenz)
- [Seiten- & Funktionsmatrix](#seiten--funktionsmatrix)
- [Governance- & Laufzeit-Invarianten](#governance--laufzeit-invarianten)
- [Pages-Maintainer-Automation](#pages-maintainer-automation)
- [Verifikation & Tests](#verifikation--tests)
- [Geschwister-Tools & Ökosystem](#geschwister-tools--ökosystem)
- [Sicherheitsrichtlinie](SECURITY.md)
- [Drittanbieter-Lizenzen](THIRD_PARTY_LICENSES.md)
- [Marketing-Log](MARKETING-LOG.txt)
- [Änderungsprotokoll](CHANGELOG.md)
- [llms.txt](llms.txt)
- [Lizenz & Governance](#lizenz--governance)

---

## Interaktive Ökosystem-Übersicht

Live erreichbar unter **https://ellmos-ai.github.io**

`ellmos-ai.github.io` dient als öffentliche visuelle Oberfläche des modularen ellmos-Baukastens. Es überführt interne Modulregister, Kompositionsrezepte und KI-Agenten-Skills in benutzer- und maschinenlesbare statische Weboberflächen:

1. **Modul-Schaltplan** ([`index.html`](https://ellmos-ai.github.io)): Visuelles, domänenspezifisch gegliedertes Schaltbild, das Interaktionen und Protokolle zwischen Modulen (MCP-Server, Proxys, Runner, Werkzeuge) darstellt.
2. **Bundle-Rezepte** ([`bundles.html`](https://ellmos-ai.github.io/bundles.html)): Interaktive Übersicht über 13 kuratierte Bereitstellungsrezepte mit klaren Pflicht- und Optionskomponenten für spezifische Agentenprofile.
3. **Skill-Bibliothek** ([`skills.html`](https://ellmos-ai.github.io/skills.html)): Durchsuchbarer Katalog aller öffentlichen Agenten-Skills (`SKILL.md`) mit integriertem Betrachter und Zwischenablage-Funktion.
4. **Stack-Composer** ([`stack-composer.html`](https://ellmos-ai.github.io/stack-composer.html)): Interaktive visuelle Arbeitsfläche zur Zusammenstellung valider Modul-Stacks mit Live-Regelprüfung und Export nach `stack.v2.json`.

---

## Systemarchitektur & Datenfluss

```mermaid
flowchart TB
    subgraph Client["1. Browser-Client & Oberflächen-Schicht"]
        UI["Webbrowser-Client<br/>(Desktop, Tablet, Mobil)"]
        Theme["Theme & lokaler Zustand<br/>(Dunkel- / Hell-Modus, reines Vanilla JS)"]
        Offline["100% Clientseitige Engine<br/>(Null externe Requests, Null CDNs)"]
    end

    subgraph Pages["2. Öffentliche interaktive Web-Apps"]
        P1["index.html<br/>Modul-Schaltplan"]
        P2["bundles.html<br/>13 kuratierte Bundle-Rezepte"]
        P3["skills.html<br/>Öffentliche Skill-Bibliothek"]
        P4["stack-composer.html<br/>Interaktiver Stack-Composer"]
    end

    subgraph Maintainer["3. Automatisierte Wartungs-Schicht"]
        PM["_tools/pages_maintainer.py<br/>(Deterministischer Fenster-Runner)"]
        State["_tools/.state/<br/>(Fenstergrenzen & Lauf-Evidenzen)"]
        DiffCheck["Atomare Diff-Prüfung<br/>(Inhaltsbasierter Commit-Gate)"]
    end

    subgraph Security["4. Sicherheits- & Leak-Gate-Isolation"]
        LG["Fail-Closed Leak-Gates<br/>(Blockiert vis:priv & vis:cand)"]
        CatCheck["Kanonische Skill-Parität<br/>(Abgleich gegen .SKILLS-Registry)"]
        Invoker["Keine Rechteausweitung<br/>(RunAsInvoker User-Mode)"]
    end

    subgraph Upstream["5. Kanonische Upstream-Quellen"]
        Cat["Private Modulkataloge<br/>(Ausschließlich freigegebene Auszüge)"]
        SkillsReg[".SKILLS Kanonischer Ordner<br/>(Markdown-Skill-Dateien)"]
        GitRepo["Git-Repository HEAD<br/>(Branch main)"]
    end

    UI --> Theme
    Theme --> Offline
    Offline --> Pages
    P1 --> UI
    P2 --> UI
    P3 --> UI
    P4 --> UI

    PM --> State
    PM --> Security
    Security --> Upstream
    Security --> LG
    Security --> CatCheck
    Security --> Invoker
    PM --> DiffCheck
    DiffCheck --> Pages
    DiffCheck --> GitRepo
```

---

## Wartungs- & Publikationssequenz

```mermaid
sequenceDiagram
    autonumber
    actor Admin as Maintainer / Automation
    participant Runner as pages_maintainer.py
    participant Guard as Lock- & Fenster-Gate
    participant Catalog as Upstream-Modulkatalog
    participant Leak as Fail-Closed Leak-Gate
    participant Artifacts as Web-Artefakte (HTML)
    participant Tests as Pytest & Ruff Gates
    participant Git as Git-Repository / Pages CDN
    actor User as Webbrowser-Nutzer

    Admin->>Runner: Starte Wartungszyklus (--check / --run)
    Runner->>Guard: Prüfe 7-Tage-Fenster & fordere atomaren Lock an
    Guard-->>Runner: Fenster bestätigt & Lock gewährt
    Runner->>Catalog: Lese Modulkataloge & .SKILLS-Inventar
    Runner->>Leak: Prüfe generierte HTML-Dateien auf vis:priv / vis:cand
    alt Leak entdeckt oder Skill-Zahl unstimmig
        Leak-->>Runner: Fail-Closed Verletzung festgestellt
        Runner-->>Admin: Sofortiger Abbruch (0 Artefakte verändert)
    else Keine Leaks & Parität verifiziert
        Leak-->>Runner: Prüfung erfolgreich (100% sauber)
        Runner->>Artifacts: Schreibe aktualisierte index, bundles, skills, stack-composer
        Runner->>Tests: Führe Pytest & Ruff-Analyse aus
        Tests-->>Runner: Alle Tests bestanden (100% grün)
        alt Generierter Inhalt unterscheidet sich von HEAD
            Runner->>Git: Erzeuge atomaren Git-Commit & Push
            Git-->>Admin: Reinen Stand auf origin/main gepusht
        else Inhalt identisch zu HEAD
            Runner-->>Admin: Idempotenter No-Op (0 Commits erzeugt)
        end
        Runner->>Guard: Gib atomaren Lock frei
    end

    User->>Git: Rufe https://ellmos-ai.github.io auf
    Git-->>User: Liefere in sich geschlossenes statisches HTML/CSS/JS
    User->>User: Clientseitiges interaktives Filtern & Stack-Komposition
```

---

## Seiten- & Funktionsmatrix

| Seite | Datei | Hauptfunktionen | Zielgruppe | Datenschutz & Ausführung |
|---|---|---|---|---|
| **Modul-Schaltplan** | [`index.html`](https://ellmos-ai.github.io) | Visuelle Darstellung funktionaler Cluster, Modulsuche, Tooltips mit Modulzweck, zweisprachige Beschreibungen. | Entwickler, Architekten, KI-Agenten | 100% clientseitiges Rendering, null Telemetrie |
| **Bundle-Rezepte** | [`bundles.html`](https://ellmos-ai.github.io/bundles.html) | 13 vorkomponierte Ökosystem-Rezepte, Komponenten-Aufschlüsselung, Modulstufen (Pflicht / Optional). | Systemintegratoren, Teams | Reine statische Tabellen, sofortiger Offline-Filter |
| **Skill-Bibliothek** | [`skills.html`](https://ellmos-ai.github.io/skills.html) | Direkter Betrachter für öffentliche `SKILL.md`-Dokumente, thematische Gliederung, Markdown-Kopierfunktion. | Prompt-Engineers, Agenten | Lokaler DOM-Reader, null externe APIs |
| **Stack-Composer** | [`stack-composer.html`](https://ellmos-ai.github.io/stack-composer.html) | Visuelle Arbeitsfläche zum Zusammenstellen von Stacks, Live-Validierung von Kompatibilitätsregeln, Export nach `stack.v2.json`. | Framework-Ingenieure, DevOps | Im Browser generiertes JSON, direkter Download |

---

## Governance- & Laufzeit-Invarianten

Das Projekt garantiert 10 verbindliche Betriebs- und Architektur-Invarianten:

| Invarianten-ID | Garantie | Spezifikation & Implementierungsdetails | Sicherheits- & Betriebsvorteil |
|---|---|---|---|
| `INV-STATIC-01` | **100% Static- & Zero-Egress-Invariante** | Alle Webseiten (`index.html`, `bundles.html`, `skills.html`, `stack-composer.html`) sind autarke statische Dokumente ohne externe Telemetrie, Tracking-Skripte oder Fremd-CDNs. | Vollständige Privatsphäre; das Nutzungsverhalten und zusammengestellte Stacks verbleiben auf dem lokalen Gerät. |
| `INV-LEAK-02` | **Fail-Closed Leak-Gates** | Die Maintainer-Suite (`_tools/pages_maintainer.py`) prüft Web-Artefakte vor der Publikation strikt gegen die Kanonik. Funde von `vis:"priv"` oder `vis:"cand"` stoppen den Lauf sofort. | Vollständiger Schutz vor unbeabsichtigter Veröffentlichung interner Modul-IDs oder Entwicklungsstände. |
| `INV-CATALOG-03` | **Kanonische Katalog-Parität** | Skill-Zahlen und Modulinventare müssen exakt mit der kanonischen `.SKILLS`-Registry und dem Modulverzeichnis übereinstimmen. | Garantiert, dass die öffentliche Dokumentation stets 100% synchron mit den tatsächlichen Fähigkeiten ist. |
| `INV-RUNAS-04` | **Local-First & Keine Rechteausweitung (User-Mode)** | Alle Build- und Wartungsskripte laufen unprivilegiert im regulären Benutzerkontext (`RunAsInvoker`). Administrator- oder Root-Rechte werden weder benötigt noch angefordert. | Sichere Ausführung nach dem Least-Privilege-Prinzip ohne Risiko von Rechteausweitungen auf Entwicklergeräten oder CI-Runnern. |
| `INV-WINDOW-05` | **Deterministische 7-Tage-Fenster-Wartung** | Automatisierte Wartungsläufe sind strikt an deterministische 7-Tage-Fenster (montags verankert) gebunden und mit den Läufen des `system-auditor` synchronisiert. | Vorhersehbare Wartungszyklen ohne überflüssige Unruhe oder erratische Mikro-Commits. |
| `INV-DIFF-06` | **Atomare inhaltsbasierte Commits** | Git-Commits werden ausschließlich erzeugt, wenn sich verifizierte, leak-geprüfte Seiteninhalte tatsächlich von HEAD unterscheiden. | Saubere, nachvollziehbare Commit-Historie ohne leere Geister-Commits oder reine Zeitstempel-Verschiebungen. |
| `INV-LOCK-07` | **Fail-Closed Lock-Disziplin** | Transaktionale Sperrdateien (`LOCK.pages-maintainer.txt`, kanonische LOCK-Systemregeln) verhindern Nebenläufigkeitskonflikte und stellen atomare Abläufe sicher. | Zuverlässiger Schutz vor Dateibeschädigungen durch gleichzeitige Generatorläufe in Multi-Agenten-Umgebungen. |
| `INV-OS-08` | **Multi-OS Plattformparität & Smoke-Integrität** | Automatisierter GitHub Actions CI-Workflow über `ubuntu-latest`, `windows-latest` und `macos-latest` auf Python 3.10-3.13 mit Bytecode-Kompilierung und Ruff-Linter. | Nahtlose plattformübergreifende Zuverlässigkeit für alle Skripte und Verifikations-Routinen. |
| `INV-CLIENT-09` | **Reine clientseitige statische Ausführung** | Dunkel-/Hell-Modus, Filter der Modulkarte, Bundle-Inspektion und Stack-Composer laufen vollständig in clientseitigem JavaScript ohne Server-Backend. | Extrem schnelle Ladezeiten, null Serverinfrastruktur-Kosten und robuste Offline-Nutzbarkeit. |
| `INV-SLA-10` | **48h Antwort- & 5-Tage-Triage-SLA** | Verbindliche 48-Stunden-Eingangsbestätigung sowie vollständige Triage- und Behebungszusage innerhalb von 5 Werktagen. | Professioneller, verlässlicher Sicherheits- und Schwachstellenmeldeprozess auf Enterprise-Niveau. |

---

## Pages-Maintainer-Automation

Das Repository enthält ein dezidiertes Wartungsskript, welches die generierten Webseiten an das 7-Tage-Fenster des `system-auditor` koppelt. Es führt Generatoren aus, validiert Leak-Gates und committet Änderungen atomar:

```powershell
# Vorab-Prüfung ohne Dateimodifikationen
$env:PYTHONIOENCODING='utf-8'
python _tools/pages_maintainer.py --check

# Generierung ausführen und Web-Artefakte prüfen
python _tools/pages_maintainer.py --run

# Generierung ausführen und geprüfte Änderungen auf origin/main pushen
python _tools/pages_maintainer.py --run --push
```

Anweisungen für Ausfall-Automationen und Übergabe-Richtlinien sind in [`_tools/FALLBACK-AUTOMATION.md`](_tools/FALLBACK-AUTOMATION.md) dokumentiert.

---

## Verifikation & Tests

Das Repository erzwingt automatisierte Vertragsprüfungen über Pytest und Ruff-Linting:

```powershell
# Ruff statische Code-Analyse ausführen
$env:PYTHONIOENCODING='utf-8'
python -m ruff check .

# Python Bytecode-Integrität kompilieren
python -m compileall -q _tools tests

# Vollständige automatisierte Testsuite ausführen
python -m pytest -ra -v
```

Die Verifikation umfasst:
- CI-Workflow-Konfiguration und Multi-OS-Matrix
- PEP 621 Metadaten-Vollständigkeit und URLs
- Zweisprachige Sicherheitsrichtlinie und 48h/5d SLA-Zusagen
- Existenz und Mindestgröße der statischen Web-Artefakte
- Leak-Gate-Invariante gegen private Sichtbarkeitsmarker
- Zweisprachige README- und Anker-Parität
- Integrität der KI-Agenten-Referenzen (`llms.txt`)
- Multi-Host-Synchronisationskonflikte und Sperrdatei-Regeln in `.gitignore`

---

## Geschwister-Tools & Ökosystem

`ellmos-ai.github.io` visualisiert und vernetzt das modulare Werkzeug-Ökosystem über `ellmos-ai`, `dev-bricks`, `file-bricks`, `doc-bricks` und `open-bricks`:

| Tool | Repository | Schwerpunkt & Rolle im Ökosystem |
|---|---|---|
| **coma** | [ellmos-ai/coma](https://github.com/ellmos-ai/coma) | Multi-Agent Job Board & Provider-Routing-Bridge |
| **clutch** | [ellmos-ai/clutch](https://github.com/ellmos-ai/clutch) | Provider-neutrales Routing für Einzelaufgaben |
| **MarbleRun** | [ellmos-ai/MarbleRun](https://github.com/ellmos-ai/MarbleRun) | Sequenzielle Agenten-Schleifen & Kettenausführung |
| **policy-registry** | [ellmos-ai/policy-registry](https://github.com/ellmos-ai/policy-registry) | Policy-Governance & Berechtigungs-Autorität |
| **system-explorer** | [ellmos-ai/system-explorer](https://github.com/ellmos-ai/system-explorer) | Systemweite Topologie & Stack-Inspektion |
| **sqlite-transit-sync** | [ellmos-ai/sqlite-transit-sync](https://github.com/ellmos-ai/sqlite-transit-sync) | Sichere SQLite-Snapshot- & Sync-Pipeline |
| **workflowhooker** | [ellmos-ai/workflowhooker](https://github.com/ellmos-ai/workflowhooker) | Workflow-Hooking & Lifecycle-Event-Interceptor |
| **memoryhooker** | [ellmos-ai/memoryhooker](https://github.com/ellmos-ai/memoryhooker) | Agenten-Gedächtnis-Injektion & Provenienz-Tracking |
| **swarm_ai** | [ellmos-ai/swarm_ai](https://github.com/ellmos-ai/swarm_ai) | LLM-Schwarmintelligenz & Konsens-Voting-Toolkit |
| **ellmos-filecommander-mcp** | [ellmos-ai/ellmos-filecommander-mcp](https://github.com/ellmos-ai/ellmos-filecommander-mcp) | Local-First FileCommander MCP-Server |
| **ellmos-codecommander-mcp** | [ellmos-ai/ellmos-codecommander-mcp](https://github.com/ellmos-ai/ellmos-codecommander-mcp) | Local-First CodeCommander MCP-Server |
| **ellmos-controlcenter-mcp** | [ellmos-ai/ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp) | Zentrales Steuerzentrum für KI-Tools & Profile |
| **DevCenter** | [dev-bricks/DevCenter](https://github.com/dev-bricks/DevCenter) | Entwickler-Arbeitsplatz-Hub & Prozesssteuerung |
| **CodeBox** | [dev-bricks/CodeBox](https://github.com/dev-bricks/CodeBox) | Mehrsprachige Code-Ausführung & Plugin-Plattform |
| **ProFiler** | [file-bricks/ProFiler](https://github.com/file-bricks/ProFiler) | Local-First Datei-Analyse & Datenschutz-Ampel |
| **open-bricks** | [open-bricks/open-bricks](https://github.com/open-bricks) | Dachorganisation für offene Entwicklerwerkzeuge |

---

## Sicherheitsrichtlinie & Datenschutz-SLA

`ellmos-ai.github.io` garantiert eine 100% Zero-Egress statische Ausführung. Vollständige Sicherheitshinweise, Meldewege für Schwachstellen, unterstützte Versionen sowie unser verbindliches 48-Stunden-Antwort- / 5-Tage-Triage-SLA finden Sie in [`SECURITY.md`](SECURITY.md).

---

## Lizenz & Governance

Bereitgestellt unter den Bedingungen der **MIT-Lizenz** — siehe [LICENSE](LICENSE) für Details.
Hinweise zu Drittanbieter-Komponenten und Freigaben sind in [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) dokumentiert.
Projektbezogene Marketing-, Auffindbarkeits- und Keyword-Einträge werden in [MARKETING-LOG.txt](MARKETING-LOG.txt) gepflegt.

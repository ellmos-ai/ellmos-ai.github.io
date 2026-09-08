<img src="assets/banner.png" width="100%" alt="ellmos-ai.github.io Banner">

# ellmos-ai.github.io — Interaktive Karten des ellmos-Ökosystems

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

**[English](README.md)** | **[Deutsch](README_de.md)** | **[Live-Webseite](https://ellmos-ai.github.io)** | **[Seitenübersicht](#seitenübersicht)** | **[Wartung](#wartung)** | **[Sicherheitsrichtlinie](SECURITY.md)** | **[Changelog](CHANGELOG.md)** | **[llms.txt](llms.txt)**

---

Erreichbar unter **https://ellmos-ai.github.io**

## Seitenübersicht

| Seite | Inhalt & Funktion |
|---|---|
| [`index.html`](https://ellmos-ai.github.io) | **Module Circuit Map** — Die Funktionsbereiche des ellmos-Baukastens, ihr Zusammenspiel und alle öffentlichen Module mit Zweckbeschreibung (DE/EN, Dark/Light-Design) |
| [`bundles.html`](https://ellmos-ai.github.io/bundles.html) | **Bundle Recipes** — Die 13 veröffentlichten Kompositionsrezepte (erste Rollout-Welle): Module, Skills und Anwendungen jedes Bundles mit Anforderungsprofilen |
| [`skills.html`](https://ellmos-ai.github.io/skills.html) | **Skill Library** — Öffentliche SKILL.md-Bibliothek mit integriertem Betrachter und Copy-to-Clipboard-Funktion |
| [`stack-composer.html`](https://ellmos-ai.github.io/stack-composer.html) | **Stack Composer** — Interaktive Zusammenstellung individueller Stacks aus Modulen mit Live-Prüfung von Kompositionsregeln und `stack.v2.json`-Export |

Diese Seiten sind vollständig in sich geschlossene Build-Artefakte (kein Build-System im Repository, keine externen Requests, kein Tracking). Sie werden aus den internen Modulkatalogen generiert und stellen den **öffentlichen Auszug** des Ökosystems dar — das Gesamtsystem umfasst weitere nicht-öffentliche Module und die Rezepturschicht.

## Architektur & Sicherheitsinvarianten

Gemäß [`SECURITY.md`](SECURITY.md) gelten folgende Kerninvarianten:
- **100% Static & Zero-Egress**: Alle bereitgestellten Webseiten sind autarke HTML/CSS/JS-Dateien ohne Tracking oder externe Netzwerkaufrufe.
- **Fail-Closed Leak-Gates**: Das Wartungswerkzeug verhindert strikt, dass interne oder nicht-öffentliche Modul-IDs (`vis:"priv"`, `vis:"cand"`) in öffentliche Seiten gelangen.
- **Deterministische Wartung**: Idempotente Wartungszyklen gekoppelt an feste 7-Tage-Fenster.
- **Local-First & Unprivilegierter Betrieb**: Ausführung vollständig im User-Space ohne Administratorrechte.
- **Fail-Closed Lock-Disziplin**: Verhindert Nebenläufigkeitskonflikte durch atomare Sperrdateien.

## Wartung

`_tools/pages_maintainer.py` koppelt die generierte Seite an das feste 7-Tage-Fenster des `system-auditor`. Es führt beide Generatoren aus, prüft die Leak-Gates fail-closed und committet ausschließlich bei einem Inhaltsunterschied. Push erfolgt über das separate `--push`-Flag.

```powershell
$env:PYTHONIOENCODING='utf-8'
python _tools/pages_maintainer.py --check
python _tools/pages_maintainer.py --run
```

Der Desktop-Fallback-Befehl und die Übergabe an die Rollenverwaltung sind in [`_tools/FALLBACK-AUTOMATION.md`](_tools/FALLBACK-AUTOMATION.md) dokumentiert.

## Verifikation & Tests

Das Repository verfügt über eine automatisierte Testsuite mit Pytest und Ruff-Linting:

```powershell
$env:PYTHONIOENCODING='utf-8'
python -m ruff check .
python -m pytest -v
```

## Community & Ökosystem

- **Dachorganisation**: https://github.com/ellmos-ai
- **Umbrella-Ecosystem**: https://github.com/open-bricks
- **Bug Tracker & Issues**: https://github.com/ellmos-ai/ellmos-ai.github.io/issues

## Lizenz / License

MIT — siehe [LICENSE](LICENSE).

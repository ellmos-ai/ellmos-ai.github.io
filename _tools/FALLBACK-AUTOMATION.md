# Pages-Maintainer und Desktop-Fallback

Der Pages-Maintainer verwendet dasselbe feste 7-Tage-Raster wie der `system-auditor`
(Anker: Montag, 2026-01-05). `--check` wertet den letzten Commit der vier generierten
Site-Dateien und den Marker `_tools/.state/pages-maintainer.json` aus. Der Marker belegt
auch erfolgreiche Läufe ohne Inhaltsdiff.

## Manuelle Befehle

```powershell
$env:PYTHONIOENCODING='utf-8'
python "C:\_Local_DEV\repos\ellmos-ai.github.io\_tools\pages_maintainer.py" --check
python "C:\_Local_DEV\repos\ellmos-ai.github.io\_tools\pages_maintainer.py" --run
```

`--run` führt `gen_ellmos_maps.py` und `build_pages_site.py` aus, prüft die
Leak-Gates und committet nur bei einem Inhaltsdiff. Ohne `--push` findet kein Push statt.

## Aufruf für den vom Master einzubauenden Desktop-Fallback

```powershell
$env:PYTHONIOENCODING='utf-8'
python "C:\_Local_DEV\repos\ellmos-ai.github.io\_tools\pages_maintainer.py" --fallback --push
```

Empfohlener Cron-Ausdruck: `23 9 * * *` (täglich um 09:23 lokaler App-Zeit). Die tägliche
Prüfung erzeugt keine täglichen Builds: `--fallback` läuft nur einmal je Auditor-Fenster und
überspringt ein bereits belegtes Fenster. Claude Desktop Scheduled Task und Codex Automation
sollen denselben Befehl verwenden; die Automationen selbst werden vom TICKET-MASTER angelegt.

Vor dem Aktivieren muss der Master einmal `--check` und einmal `--fallback` ohne `--push`
ausführen. Ein Push bleibt explizit am Flag erkennbar. Bei einem schmutzigen Worktree, einem
Projektlock, einem Katalog-/Generator-Versatz oder einem Leak-Gate-Fehler bricht das Skript
fail-closed ab.

## MAINTAINER-Rolle

Ohne Änderung am `task-master`-Repo kann der Rollenweg gestartet werden mit:

```powershell
python -m taskplan launch --role maintainer --provider codex
```

Die konkrete Daueraufgabe bleibt dieses Skript; TASKPLAN ist nur der optionale Rollen-Launcher.

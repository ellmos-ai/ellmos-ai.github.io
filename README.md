<img src="assets/banner.png" width="100%" alt="ellmos-ai.github.io Banner">

# ellmos-ai.github.io — interactive maps of the ellmos ecosystem

Live at **https://ellmos-ai.github.io**

| Page | What it shows |
|---|---|
| [`index.html`](https://ellmos-ai.github.io) | **Module Circuit Map** — the functional areas of the ellmos construction kit, how they work together, and every public module with its purpose (DE/EN, dark/light) |
| [`bundles.html`](https://ellmos-ai.github.io/bundles.html) | **Bundle Recipes** — the 13 released composition recipes (first rollout wave): which modules, skills and apps make up each bundle, with requirement levels |
| [`skills.html`](https://ellmos-ai.github.io/skills.html) | **Skill Library** — the public SKILL.md library, readable in place, copy-to-clipboard |
| [`stack-composer.html`](https://ellmos-ai.github.io/stack-composer.html) | **Stack Composer** — assemble your own stack from public modules, with live composition-rule checks and `stack.v2.json` export |

These pages are self-contained build artifacts (no build system in this repo, no external
requests, no tracking). They are generated from the ellmos module catalogs in the private
workspace and show the **public excerpt** of the ecosystem — the full system contains
additional private modules and the recipe layer.

## Maintenance

`_tools/pages_maintainer.py` couples the generated site to the system-auditor's fixed
seven-day window. It runs both workspace generators, keeps the publication gates fail-closed,
and commits only when generated site content changed. Push is a separate `--push` flag.

```powershell
$env:PYTHONIOENCODING='utf-8'
python _tools/pages_maintainer.py --check
python _tools/pages_maintainer.py --run
```

The Desktop-app fallback command and scheduling hand-off are documented in
[`_tools/FALLBACK-AUTOMATION.md`](_tools/FALLBACK-AUTOMATION.md). The repository contains no
Desktop Scheduled Task or Codex automation definition.

Org overview: https://github.com/ellmos-ai · Umbrella: https://github.com/open-bricks

## Lizenz / License

MIT — see [LICENSE](LICENSE).

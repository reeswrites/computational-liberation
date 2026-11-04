# Scoreboard

One row per run, appended by the engine (`phil rules check-all --scoreboard docs/scoreboard.md`, `phil rules diff --baseline data/verdicts-baseline.json --scoreboard docs/scoreboard.md`; ablation rows when `phil rules ablate` gains the flag). Never typed by hand. `verdict_changes` is against `data/verdicts-baseline.json` (regenerate the baseline only in a commit that says why). The direction the author asked to track (2026-11-04): blind rediscovery hits, drift count per preregistration, ASSUMED marks outstanding, uncounted rows, z3 unknowns, council reds/ambers. The last three of those still live in the review files and plans, not here.

| date | engine | command | rows | verdict_changes | z3_unknowns | wall_s | inconsistent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-04 | dirty+5275d11 | rules diff | 123 | 0 | 0 | 0.2 | - |

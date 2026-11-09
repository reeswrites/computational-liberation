| date | engine | command | rows | verdict_changes | z3_unknowns | wall_s | inconsistent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-04 | dirty+5275d11 | rules diff | 123 | 0 | 0 | 0.2 | - |
| 2026-11-04 | dirty+faefef1 | rules diff | 123 | 0 | 0 | 4.9 | - |
| 2026-11-04 | 83061ce | rules diff | 123 | 0 | 0 | 3.9 | - |

## Preregistration calibration

Rows are pasted from the skeleton `scripts/checks.sh` prints; `?` means unknown. Seat counts are says-it/over/under/cannot (card-only seat).

| batch | date | rows predicted to move | rows moved | drift items | seat counts (says-it/over/under/cannot) | notes |
| --- | --- | --- | --- | --- | --- | --- |
| faithfulness 3a | 2026-11-08 | 0 | 0 | 1 | 11/1/0/0 | drift: pytest count (38 predicted, 40 actual) |
| faithfulness 3c | 2026-11-09 | 0 | 0 | 2 | 7/0/1/0 (card-only); correctness 7 green/1 amber/0 red, 7 correct; faithfulness 5 faithful/1 understates/1 overstates | drift in wording/counts only (cps R1 ranked not deregulated; rule-count figure); iso exact-level pairing swap reported; pytest: 40 passed |
| P2 coverture-us-ssi | 2026-11-08 | 0 of 177 old rows (15 added) | 0 of 177 old rows (15 added) | 1 | ? | drift: cannot_contract holds_to_k predicted, violated (S7); 14 of 15 properties as predicted; pytest 38 passed |
| SSI revision 2 (cohabits) | 2026-11-09 | 4 of 192 | 4 of 192 (the same four) | 7 | 8/1/4/2 (card-only; the 2 cannot-tell rows paused the batch until the fix pass); correctness 8 green/3 amber/0 red; faithfulness 5 faithful/1 understates/2 overstates/0 cannot tell | 0 unpredicted rows; drift is brief-vs-data and two flagged deviations from rulings as worded (property formulas edited; only R1 to default capacity), no verdict drift; baseline regenerated 192 -> 192 rows; pytest: 40 passed |
| priority slice 3 | 2026-11-09 | 0 of 192 (0 transfer edges in 7 entries) | 0 of 192 (0 edges) | 5 | scope 5 green/7 amber/0 red | null graph as predicted; cost predictions missed (hit rate 52-55% vs 45-50%; kibbutz 13.5 min vs under 5); T11 count unchanged |

checks.sh timings: fill in the first serial vs concurrent full run here (2026-11-09 speed pass)

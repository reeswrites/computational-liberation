# priority slice 3: pairwise transfer graph and `rebundling`

## Slice 3: preregistered 2026-11-09, before any transfer run

Status: preregistration. Dataset at computational-liberation main d5d3a92 (33 entries, 43 properties). Engine at ENGINE_PIN e46f6ea (semantically equal to engine main 50ed97f, which only dropped the stale dataset copy); the slice-3 engine work sits on engine branch `claude/slice3-transfer-graph-caf95a`, cut from 50ed97f. Baseline 192 rows (k=6, strict, step_mode one). Inputs read: plans/priority.md (Design, Slices, Decisions, Open questions), plans/priority-slice1-results.md, plans/priority-slice2.md and its results, docs/ablation/2026-11-09-batch3c/ (kibbutz loads), docs/claims.md T1 and T11, docs/decisions/0016-failure-mode-axes.md, docs/decisions/0014, docs/glossary.md "rebundling", the seven entries' YAML sources.

**What these predictions are blind to, and what they are not blind to.**
- No transfer graph, no doubly-ablated run and no `rebundling` check has been run on any dataset entry, in the engine's fixture (`data/example/`, which holds `coverture-household`, the MWPA chain's ancestor) or anywhere else except a hand-built toy (below).
- Not blind: the first-order loads. Kibbutz loads are the committed 2026-11-09 rerun. The MWPA first-order tables in the slice 1 and 2 results predate three dataset commits, so a first-order `phil rules ablate --k 6,8` was rerun today on the six `mwpa-*` entries at engine 50ed97f to get current loads (tops unchanged from slice 1 revision 5). That is the input the task names ("current loads"), not a transfer run.
- Not blind: the engine code. `transfer_graph`, `phil rules transfer` and the derived check were written and unit-tested before this commit, on one toy only: the engine test fixture `t-keeper` with a duplicated exit bar, where the answer is known by construction (two edges of weight 1, both rebundling). The definitions in "Build" below were fixed by writing that code and are stated here before any dataset result exists.

### Scope

In scope: the pairwise transfer graph on `kibbutz-childrens-house` and the six MWPA entries (`mwpa-creditor-exemption`, `mwpa-property`, `mwpa-earnings`, `mwpa-sole-trader`, `mwpa-suit`, `mwpa-property-narrowed`) at k=6 and k=8, strict, step_mode one; the `rebundling` check on the same seven; the RuleCache hit rate and wall time (priority.md open question 2); the T1 out-transfer observation, reported either way; the T11 row.

Out of scope: any change to an entry, a rule, a strand tag, an existing property or an existing verdict; `kibbutz-childrens-house-no-implicit` and the other 25 entries; cut sets and sequencing (slice 4); `step_mode many` and `compliance sanctioned`; a gate criterion (none is added; `rules_gate.py` is untouched); ENGINE_PIN (unchanged in this PR; the bump follows the engine merge).

### Build (engine; design fixed here)

1. **Weight.** For rules r1 != r2 of entry E: `weight(r1 -> r2) = load(r2 | E \ r1) - load(r2 | E)`, where `load(r2 | X)` is the ordinary slice-1 ablation load of r2 in X (base X, delete r2). A positive weight is a directed edge. A negative weight is listed as `relief`, never an edge.
2. **Two graphs, never combined.** Freedom graph: `load_freedom_up` (the load the ranking reads; priority.md revision 2 (b)). Goods graph: `load_goods_primary` (docs/plan.md step 8: goods via each good's `primary_measure`). Differences in `load_freedom_down`, `load_freedom`, `load_goods_guaranteed`, `load_goods_possible` are kept per pair as `deltas` and are not edges.
3. **Deletions only** (ASSUMED, not ratified). The `~prohibit` variant of a `may` is neither a source nor a target.
4. **Unranked rows.** An edge whose source is `deregulated` in E, or whose target is `deregulated` in E or in E \ r1, is shown with the flag `unranked`, is never a rebundling edge and is left out of out-transfer. A source whose deletion leaves no compliant trace has no out-edges; a pair whose target load is undefined (no compliant trace) is listed as `undefined`.
5. **"Tying" means the reading, not the hand tag.** A rebundling edge is a freedom edge, ranked on both sides, whose target reads `tying` in E \ r1 under the primary column (up > 0, no goods family lost in its primary sense). The hand tag `strand` is printed beside it and decides nothing. `rebundling(E, r1)` holds when r1 has such an edge.
6. **Where the property lives.** `rebundling` is not a trace formula, so it cannot be a `formal` over one entry. It is a property in the properties file with `kind: failure_mode`, `check: rebundling`, a new *derived* check kind in the engine: `run_all` answers it with `reachable` (some r1 has a rebundling edge at k; the reason names every edge) or `open` (none found at k). That is what lets `phil rules check`, `check-all`, `verdicts` and `diff` see it for any entry that lists it in `expected_properties`. Ablation never reads a derived property (no load, no recursion). Alternative not taken: a report-only output of `phil rules transfer`, invisible to check-all.
7. **Dataset rows wait for the pin.** The current pin's loader rejects `check: rebundling`, so `src/properties.yaml`, the seven `expected_properties` lines and the baseline rows cannot land in this PR without breaking CI. This slice checks the property through an overlay properties file (the committed `properties.json` plus the one `rebundling` row) and records the verdicts in Results; the dataset rows are a follow-up with the ENGINE_PIN bump. The engine's own fixture carries the property so engine CI's check-all sees it.
8. **Cost.** n rules cost 1 + n + n(n-1)/2 distinct institutions per k; (r1, r2) and (r2, r1) share the doubly-ablated one through RuleCache. `phil rules transfer` runs serially so the hit counters are exact.

### Predictions

Commands (engine branch, dataset files of this worktree): `phil rules transfer --entry <id> --k 6,8 --json <id>.json`, one process per entry, cold cache; then `phil rules check --inst <id> --prop rebundling` with the overlay.

**P1. Baseline and suite.** `phil rules diff --baseline data/verdicts-baseline.json` on the engine branch: 0 changed, 0 added, 0 removed of 192. `phil rules check-all`: 192/192. Engine `pytest -m "not llm"`: all pass (the count rises by the new tests). No existing first-order ablation row changes.

**P2. Freedom graph (load_freedom_up), all seven entries, k=6 and k=8: no edge.** Reason: every ranked up-load in these entries is one family carried by one disability on a default-capacity action (MWPA: R4 `no_standing`, R6 `cannot_exit`, R7 `cannot_contract`, R19 `no_standing_against_spouse`; kibbutz: R2 `care_assigned_by_sex`, R4 `cannot_exit`). An edge needs redundancy (two rules that each suffice for one unfreedom, so neither carries it until the other is gone) and I find no such pair: no family has two bars. Per entry:

| entry | rules | predicted freedom edges | predicted relief (negative weight) | confidence |
| --- | --- | --- | --- | --- |
| mwpa-creditor-exemption | 10 | none | none | medium-high |
| mwpa-property | 10 | none | none | medium-high |
| mwpa-earnings | 11 | none | none | medium |
| mwpa-sole-trader | 11 | none | none | medium |
| mwpa-suit | 12 | none | none | medium |
| mwpa-property-narrowed | 12 | none | none | medium |
| kibbutz-childrens-house | 6 | none | R1 -> R2 = -1 and R2 -> R1 = -1 (`care_assigned_by_sex`; both pairs involve the deregulated R1) | medium |

Kibbutz relief, the reason: R1 (deregulated) and R2 each flip `care_assigned_by_sex` persists > fails alone, so the unfreedom needs both; once either is gone it already fails and the other has nothing left to flip (load 1 > 0). That is the opposite of rebundling: a conjunctive pair, not a redundant one.

**P3. Goods graph (load_goods_primary), all seven entries, both k: no edge, no relief.** MWPA: R2 carries its two primary-guaranteed families alone in E and still alone in E \ r1 for every r1; R3 loses only `mutual_household_care` under the guaranteed measure, which is not that good's primary measure. Kibbutz: every primary goods load is 0 in E and stays 0 (the R4 row is a gain, and gains are not loads). Confidence medium.

**P4. Deltas that are not edges.**
- D1 (medium): in `mwpa-earnings`, `mwpa-sole-trader` and `mwpa-suit`, R14 -> R13 has `freedom_down` +1 (0 > 1, family `financial_dependence`): with R14 gone the entry behaves like `mwpa-property`, where R13 alone keeps `financial_dependence` violated. Both rows are deregulated, so this is a transfer between two protections, not an edge in the graph. The reverse pair R13 -> R14 has `freedom_down` delta 0 (medium-low: it assumes `financial_dependence_unpropertied` shares the family).
- D2 (medium): MWPA R3 -> R2 has `goods_guaranteed` -1 (4 > 3) and R2 -> R3 has `goods_guaranteed` -1 (1 > 0), both through `mutual_household_care`, in all six MWPA entries.
- No other nonzero delta is predicted. I expect a few I did not think of; each is a drift line.

**P5. Rebundling.** No rebundling edge in any of the seven entries at either k. The derived check returns `open` on all seven, with `z3_unknown` false. It returns `reachable` only on the toy. Confidence: as P2.

**P6. Hygiene.** No inconsistent source, no undefined pair, no uncounted pair, no k-disagreement in any entry.

**P7. Cost.** Cold-cache hit rate per entry between 45% and 50% (the formula 1 - (1 + n + n(n-1)/2) / (1 + 2n + n(n-1)) gives 48.8% at n=6 and 49.5 to 49.7% at n=10 to 12); a second run on the warm cache is 100%. Serial time per MWPA entry for k=6,8 together: 15 to 40 minutes (the first-order rerun cost about 10 s per institution run on average, and an entry needs 112 to 158 distinct runs over two k); kibbutz under 5 minutes. Total under 3 CPU-hours.

**P8. T1 observation (floor strands have the highest out-transfer).** With no ranked freedom edge, out-transfer is 0 for every rule and the comparison is a tie at zero: uninformative, T1 stays `untested`. The only transfer I predict from a floor-side rule is D1 (R14, a floor strand in the glossary's sense, to R13, another), which is a protection-to-protection delta outside the graph.

**P9. T11.** The property is written and checkable, so the "written" count moves from 3 of 4 to 4 of 4 who-pays modes. I predict it fires on no dataset entry in scope, so T11's status stays `untested` and the row must say so: a property that is reachable only on a constructed toy is a definition, not a finding. Two known tensions to put to the scope seat rather than resolve: ADR 0016 files rebundling at lowest layer 3 and says who-pays modes "need a new actor or institution", while this is a layer-1 relation over the rule set as written; and docs/glossary.md defines rebundling as "the same strands recombined under new names or roles", which is not the transfer edge of priority.md.

**Falsifiers.**
- F1: any ranked freedom edge in any of the seven entries (P2 fails for that entry; if its target reads tying, P5 fails too).
- F2: any goods edge (P3).
- F3: the derived check and `phil rules transfer` disagree on any entry (an engine defect, not a finding).
- F4: diff moves a row (stop; this slice adds analysis and may not move a verdict).
- F5: hit rate outside 45 to 50% on a cold cache, or an entry over 40 minutes serial (P7).

### Drift rule

Any result other than the above is recorded in Results against the prediction it contradicts and never edited into this section. Stop conditions: a changed or removed diff row, or F3. A prediction that failed gets a row in docs/negative-results.md, as does a property that fires nowhere in scope.

**Nothing above "### Results" is edited after the first transfer run.** This section is committed before any such run.

### Results (2026-11-09; preregistration commit 56d3e4a; engine branch `claude/slice3-transfer-graph-caf95a` at d763cb4, source hash differs from the baseline's as expected; dataset d5d3a92)

Outputs: docs/ablation/2026-11-09-slice3/ (one `.txt` per entry, `transfer-summary.json`). Seven `phil rules transfer` processes ran at once, each serial, each on a cold cache.

**Headline.** No transfer edge, in either graph, in any of the seven entries, at k=6 or k=8. `rebundling` is `open` on all seven. The prediction of emptiness held; the slice's plan-level pass test ("graph matches preregistered edges") is met by a preregistered empty graph, which is a null result and is logged as one (N74). The two cost predictions failed (N75).

| # | Prediction | Result |
| --- | --- | --- |
| P1 | diff 0 changed, 0 added, 0 removed of 192; check-all 192/192; engine suite passes | **held**: "0 changed, 0 added, 0 removed (of 192 rows)" (with "note: engine source hash differs from the baseline's"); "agreement: 192/192 = 100%"; engine `pytest -m "not llm"` 613 passed, 25 skipped before the fixture expectation was added (final count in the engine PR) |
| P2 | freedom graph: no edge in seven entries; kibbutz relief R1 -> R2 = -1 and R2 -> R1 = -1 | **held** in all seven, both k. Kibbutz relief exactly as predicted; no relief anywhere else |
| P3 | goods graph: no edge, no relief | **held** in all seven, both k |
| P4 D1 | R14 -> R13 `freedom_down` +1 in earnings, sole-trader, suit; reverse pair 0 | **held** in all three, both k; R13 -> R14 has no delta |
| P4 D2 | R3 -> R2 and R2 -> R3 `goods_guaranteed` -1 in all six MWPA entries | **held** in all six, both k |
| P4 | no other nonzero delta | **held**: the deltas above are the only ones in `transfer-summary.json` |
| P5 | no rebundling edge; derived check `open` on all seven, `z3_unknown` false; `reachable` on the toy | **held**: `phil rules check --inst <id> --prop rebundling` (overlay properties file, k=6 and k=8) prints `open` for all seven; the toy is engine test `test_derived_check_through_run_all` |
| P6 | no inconsistent source, undefined pair, uncounted pair or k-disagreement | **held** |
| P7 | cold hit rate 45 to 50%; MWPA entry 15 to 40 min serial; kibbutz under 5 min; under 3 CPU-hours | **miss** on two of four (drift 1, 2). Hit rates: kibbutz 55% (422/774), MWPA 52% each (2422/4662, 2422/4662, 2906/5586, 2906/5586, 3590/6908, 3434/6594). Times: creditor-exemption 1083 s, property 1089 s, earnings 1225 s, sole-trader 1217 s, suit 1295 s, property-narrowed 1512 s (18 to 25 min, in range); kibbutz 812 s (13.5 min, out of range). Total 8233 s = 2.3 CPU-hours (in range); 25 min wall |
| P8 | out-transfer is 0 for every rule; T1 comparison a tie at zero | **held**: uninformative; T1 stays `untested` (N76) |
| P9 | property written and checkable (4 of 4 written); fires on no entry in scope; T11 stays `untested` | **held** as predicted; see Council for whether "4 of 4" may be claimed at all |

**Falsifiers.** F1 no. F2 no. F3 no (the derived check and `phil rules transfer` agree on all seven; see drift 3 for why that agreement is weaker than it looks). F4 no. F5 **fired** (hit rate above 50% in every entry).

**Transfer edges found.** None. What the run did find, outside the graphs:
- Kibbutz R1 and R2 are a conjunctive pair for `care_assigned_by_sex`: either deletion flips it persists > fails, so each loses its load once the other is gone (relief -1 both ways). Cutting either is enough; nothing rebundles.
- MWPA R13 and R14 are substitute protections for `financial_dependence` where both exist (earnings, sole-trader, suit): R13 carries no protection load while R14 stands and carries one once R14 is gone. This is the only load that rises anywhere, it is a `freedom_down` (protection) load, and both rows are deregulated `may` deletions, so by the preregistered design it is a delta, not an edge.
- MWPA R2 and R3 jointly guarantee `mutual_household_care`: each loses one guaranteed-measure family once the other is gone.

**T1 observation.** Floor strands do not have the highest out-transfer, and neither does anything else: every rule's out-transfer is 0 in both graphs. The one rising load in the data runs from a floor-side rule (R14, earnings) to another floor-side rule (R13, property), in the protection direction. That is not evidence for or against floor-first.

**Drift (recorded, nothing above "### Results" edited).**
1. P7 hit rate: predicted 45 to 50%, observed 52 to 55%. The formula counted one cache question per (institution, property) and assumed all are distinct. Two properties with the same formal text share a cache key, so the second is a hit inside a single cold run: one cold `run_all` on kibbutz at k=6 shows 1 hit in 9 questions. The direction of the miss is harmless; the model of the cache was wrong.
2. P7 kibbutz time: predicted under 5 min, observed 13.5 min for 44 distinct institutions over two k, about 18 s each against the 10 s I assumed (seven processes ran at once, and k=8 costs more than the average I took from the first-order rerun). The MWPA range held only because it was wide.
3. Not a failed prediction, a defect found while checking F3: the derived check builds its graph without the cross-entry majority table of check kinds (`run_all` sees one entry), while `phil rules transfer` uses it. On the six MWPA entries the two therefore ask one property under a different check kind (56 to 79 cache misses on an otherwise warm cache, exactly one per institution; kibbutz 0). Verdicts agree here, but the two paths are not guaranteed to. Recorded for the fix pass.
4. P2's kibbutz row said "both pairs involve the deregulated R1". R5 and R6 are deregulated in E too (three unranked rules, not one). No effect on any number.
5. The plan's slice-3 file list names `properties.json` and the ADR path `docs/adr/`; the property source is `data/institutions/src/properties.yaml` and ADRs live in `docs/decisions/`. The dataset rows did not land (Build item 7), so "property written" means: written in the engine fixture and checked on the dataset through an overlay.

**Reproduction.** From the engine checkout at d763cb4, with `D=<this repo>/data/institutions`: `phil rules transfer --entry <id> --k 6,8 --institutions $D/institutions.json --properties $D/properties.json --json <id>.json`; then `phil rules check --inst <id> --prop rebundling --k 6 --institutions $D/institutions.json --properties <overlay>` where the overlay is `properties.json` plus the `rebundling` row of the engine's `data/example/properties.json`.

### Council

(scope seat, ADR 0014: "does this batch move the thin path in docs/plan.md, or open a front? Name what should be parked." SEATS.md has no standing brief for it; the brief is written from that line in SEATS.md's format and recorded in the review file.)

### Post-council fix pass

(appended only)

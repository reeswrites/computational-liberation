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

### Results

(empty until the run)

### Council

(scope seat, ADR 0014: "does this batch move the thin path in docs/plan.md, or open a front? Name what should be parked." SEATS.md has no standing brief for it; the brief is written from that line in SEATS.md's format and recorded in the review file.)

### Post-council fix pass

(appended only)

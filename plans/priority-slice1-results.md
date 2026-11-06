# Priority slice 1: ablation results (25 entries)

Status: engine 343a0e9 (includes the fix pass). Run 2026-11-05, k=6 and k=8, 25 entries, 235 rules. Totals: inconsistent_after 0, uncounted 0, k-disagreements 0 (no rule changes verdict between k=6 and k=8 in any entry). Drift is recorded below, nothing tuned. Ranking uses `load_freedom` (unsigned: up plus down) over rules that are not deregulated.

## Preregistered vs observed (plans/priority.md, Decisions item 5)

| entry | expected | observed top (load, up+down) | expected rule's load | result |
| --- | --- | --- | --- | --- |
| coverture-household | R6 | R6 (3, 3+0) | 3 | hit |
| kibbutz-childrens-house | R2 | R4 (2, 2+0) | 1 (1+0) | miss |
| footbinding | R3 | R9 (2, 2+0) | 1 (1+0) | miss |
| mwpa-property | R11 | R6 (3, 3+0) | 0 | miss |
| ectogenesis | R5 | R4 (1, 0+1) | 0 | miss |

Score: 1/5. Loads are identical at k=6 and k=8.

## Full ranking (k=6; top ranked rule, load, deregulated-not-ranked / total rules)

| entry | top | load (up+down) | dereg/rules |
| --- | --- | --- | --- |
| coverture-household | R6 | 3 (3+0) | 4/9 |
| police-crisis | R4 | 2 (2+0) | 8/10 |
| cps | R10 | 2 (2+0) | 7/11 |
| crisis-team | none | 0 | 6/9 |
| paternity-quota | R1 | 1 (0+1) | 3/9 |
| transferable-leave | none | 0 | 4/9 |
| companion-ownership | R6 | 3 (3+0) | 7/12 |
| companion-guardianship | R6 | 3 (3+0) | 8/12 |
| companion-guardian-renamed | R6 | 3 (3+0) | 7/12 |
| lease | none | 0 | 3/5 |
| public-library | none | 0 | 5/6 |
| naming-convention | none | 0 | 2/2 |
| kibbutz-childrens-house | R4 | 2 (2+0) | 5/8 |
| kibbutz-childrens-house-no-implicit | R4 | 2 (2+0) | 5/7 |
| airline-flight | R4 | 3 (3+0) | 4/6 |
| mwpa-creditor-exemption | R6 | 3 (3+0) | 6/12 |
| mwpa-property | R6 | 3 (3+0) | 6/12 |
| mwpa-earnings | R6 | 3 (3+0) | 7/13 |
| mwpa-sole-trader | R6 | 3 (3+0) | 8/13 |
| mwpa-suit | R6 | 3 (3+0) | 7/13 |
| mwpa-property-narrowed | R6 | 3 (3+0) | 8/14 |
| footbinding | R9 | 2 (2+0) | 8/10 |
| footbinding-no-pledge | R9 | 2 (2+0) | 6/8 |
| ectogenesis | R4 | 1 (0+1) | 5/7 |
| gestational-surrogacy | R4 | 1 (0+1) | 4/6 |

No ties at the top in any entry. Five entries rank no rule above 0.

## What the misses say

Facts, then the reading.

(i) Exit twins. 17 of 25 entries have a top rule that flips both `dependent_cannot_exit` and `subject_cannot_exit` (reachable to open). The dataset README calls these the same form, so one prohibition on leaving counts twice. Coverture R6 (3) adds `subject_cannot_exit_persists` on top. Reading: the exit prohibition tops by construction wherever it exists, so the ranking cannot say much else until the twins are merged.

(ii) Kibbutz R2 carries one property (`care_assigned_by_sex`, persists to fails), R4 carries the twins (2). Footbinding R3 carries one (`binding_practised`, persists to fails), R9 the twins (2). The preregistered intuition was about which rule matters; the scorer counts properties, and the twins count twice. Not a finding about the institutions.

(iii) mwpa-property R11 flips nothing. Twelve properties are applicable: dependent_cannot_exit, subject_cannot_exit, subject_cannot_exit_persists, no_standing, care_and_sanction_same_role, care_assigned_by_sex, financial_dependence, financial_dependence_unpropertied, cannot_contract, plus the failure modes double_burden, creditor_shield, backlash. None flips on deleting R11, including `creditor_shield` (a failure mode, listed not counted: no failure-mode flips). The cause was not diagnosed here. R13 (`may hold_property`, deregulated, not ranked) flips `financial_dependence` violated to holds_to_k (0+1). Reading: the properties as encoded do not read the thing the act changed.

(iv) Ectogenesis. R4 tops at 1 with a freedom_down flip: deleting `may provide_care` leaves only the female `must`, so `care_assigned_by_sex` goes violated to holds_to_k. R5 reads 0 because `female_parent_care_persists` reads `persists` with or without R5 (council finding 6). The T3 test is uninformative, not refuted. Same pattern in gestational-surrogacy (R4, 0+1) and paternity-quota (R1, 0+1).

(v) Deregulation. 136 of 148 `may` rules (92%) are deregulated-not-ranked; 12 are "permission removed". 23 of 25 entries have most of their `may` rules deregulated (the exceptions: paternity-quota 3 of 7, transferable-leave 4 of 8). Under strict enabledness most permissions are each action's sole regulator, so the "permission removed" reading of decision 3 applies to few rules. Deregulated rows still carry flips (kibbutz R1 care_assigned_by_sex 1+0, mwpa-property R13 0+1, crisis-team R5 0+3); they are shown, not ranked.

## Council findings (2026-11-05 review, written before the fix pass)

Addressed: 1 and 2 (deregulation flag, excluded from ranking, derived power noted), 3 (orphan column), 4 (z3-unknown flag from `_check`, not message text), 7 (check kinds in header), 8 (stronger tests), 9 (`--summary`, zero-uncounted check). Partly: 5, flips are signed and reported up+down, but ranking still uses the unsigned sum. Stands: 6, R5 is property-blind.

## Pass test (plans/priority.md, layer 4)

Written test: deterministic and stable across k; rediscovers kibbutz R2 and ectogenesis R5; labels at least one strand mismatch, reported not fixed. Observed: runs on all 25 with zero silent errors; stable across k=6 and 8 (0 disagreements; step_mode not varied in this run); rediscovery fails both named cases (kibbutz R2 is second at 1, ectogenesis R5 is 0); strand mismatches against hand tags were not tabulated in this run. Verdict: runs, stable, 1/5 on the preregistered tops. Weakened; not passed.

## Decisions waiting on the author

a. Count property families, not properties (merge the exit twins), or keep.
b. Rank on `load_freedom_up` only, or the unsigned sum.
c. Deregulated deletions: keep excluded (ASSUMED option a), add the prohibit variant, or count them.
d. A property R5 actually carries (council: invariant-shaped companion) before re-running the ectogenesis expectation.
e. Re-preregister the five tops under a to d as revision 2; v1 stays in the record.

## Reproduction

`cd /Users/rees/Documents/computational-liberation && uv run phil rules ablate --k 6,8 --json ablate-25-v2.json --summary ablate-25-summary.json > ablate-25-v2.txt`

Outputs from this run: `/private/tmp/claude-501/-Users-rees-Documents/3aaae34a-2247-402e-bd6d-424feea4d706/scratchpad/ablate-25-v2.{txt,json}` and `ablate-25-summary.json`.

Decisions (a)-(e) settled 2026-11-05: families, freedom-up ranking, prohibit variant, `care_duty_on_women`, revision-2 preregistration. Recorded in plans/priority.md "Slice 1 revision 2".

## Revision 2 run (2026-11-05, engine 26688d6)

**Status.** Engine 26688d6, k=6 and 8, 25 entries. Totals: 0 inconsistent, 0 uncounted. k-disagreements: 0 (no rule's load differs between k=6 and k=8; `step_mode` not varied). 383 rows including `~prohibit`.

### Preregistered vs observed

| entry | preregistered top | observed top(s), load_freedom_up | families | result |
| --- | --- | --- | --- | --- |
| coverture-household | R6 | R6, 1 | cannot_exit | hit |
| kibbutz-childrens-house | R2 (tie with R4) | R2 and R4, 1 each | R2 care_assigned_by_sex; R4 cannot_exit | hit (tie) |
| footbinding | R3 (R9 carries cannot_exit) | R3 and R9, 1 each | R3 binding_practised; R9 cannot_exit | hit (tie) |
| mwpa-property | R7 | R6, 1; R7 reads 0 | R6 cannot_exit | **miss** |
| ectogenesis | R5 | R5, 1; R4 and R4~prohibit read 0 up (1 down) | R5 care_duty_on_women | hit |

Score 4/5 (v1 was 1/5; stays in the record). Coverture R4 and R7 were expected to tie R6 and read 0 (same cause as the miss below); the named top still hit. mwpa-property R11 reads 0 as preregistered.

### Full ranking (k=6 and 8 agree)

| entry | top rules | load_freedom_up | not ranked: deregulated | not ranked: offcondition_free | rows |
| --- | --- | --- | --- | --- | --- |
| coverture-household | R6 | 1 | 4 | 3 | 13 |
| police-crisis | R4 | 1 | 6 | 3 | 16 |
| cps | R10 | 1 | 5 | 4 | 16 |
| crisis-team | none | 0 | 5 | 3 | 14 |
| paternity-quota | none | 0 | 3 | 3 | 16 |
| transferable-leave | none | 0 | 4 | 4 | 17 |
| companion-ownership | R6 | 1 | 7 | 6 | 19 |
| companion-guardianship | R6 | 1 | 8 | 7 | 20 |
| companion-guardian-renamed | R6 | 1 | 7 | 6 | 19 |
| lease | none | 0 | 3 | 3 | 8 |
| public-library | none | 0 | 5 | 4 | 11 |
| naming-convention | none | 0 | 2 | 0 | 4 |
| kibbutz-childrens-house | R2, R4 | 1 | 5 | 2 | 13 |
| kibbutz-childrens-house-no-implicit | R4 | 1 | 5 | 2 | 12 |
| airline-flight | R4 | 1 | 4 | 2 | 10 |
| mwpa-creditor-exemption | R6 | 1 | 6 | 5 | 18 |
| mwpa-property | R6 | 1 | 6 | 5 | 18 |
| mwpa-earnings | R6 | 1 | 7 | 6 | 20 |
| mwpa-sole-trader | R6 | 1 | 8 | 6 | 21 |
| mwpa-suit | R6 | 1 | 7 | 5 | 22 |
| mwpa-property-narrowed | R6 | 1 | 8 | 7 | 22 |
| footbinding | R3, R9 | 1 | 8 | 7 | 18 |
| footbinding-no-pledge | R3, R9 | 1 | 6 | 5 | 14 |
| ectogenesis | R5 | 1 | 4 | 2 | 12 |
| gestational-surrogacy | R5 | 1 | 3 | 1 | 10 |
Totals: 136 deregulated deletions; 148 `~prohibit` rows, of which 101 offcondition_free (not ranked, ASSUMED b) and 47 ranked.

### The mwpa-property miss, diagnosed

`cannot_contract` is `(forall w) is_subject w -> not can_contract w`, and `can_contract` is a derived power fluent (ADR 0013) computed from enabledness. The engine lowers `(enabled X)` as FALSE for an unregulated action (rules_lower.py ~617; first review finding 2), while the ABM and the layer-1 README treat unregulated actions as always enabled. Deleting the sole prohibition R7 therefore makes `contract` unregulated and fire-able, yet `can_contract` stays false: the property still holds, load 0. Same for coverture R4 and R7. Consequence: under current semantics a cut of a sole prohibition on a derived-power property can never score, so R6 (exit; derived `can_exit`, with `may leave` R8 remaining) dominates. This is an engine semantics decision (derived power for unregulated actions), not a dataset fix. Changing it would change preregistered layer-1 verdicts across the dataset and needs its own preregistration. Recorded as drift, not tuned.

### Other observations

- Entries ranking nothing above 0 (six, not five): crisis-team, paternity-quota, transferable-leave, lease, public-library, naming-convention. transferable-leave and naming-convention have no flips of any sign. The other four flip only in the freedom-down direction (load-bearing protections) or in unranked deregulated/offcondition_free rows (e.g. lease R4, public-library R4 deregulated; paternity-quota R8~prohibit offcondition_free), so nothing ranked moves up. Few applicable freedom properties (1 to 5) in all six.
- `~prohibit` rows: 101 offcondition_free, 47 ranked, of 148.
- Mixed families (up and down in one family): 0 occurrences, so ASSUMED mixed-neither was never exercised.
- Review findings addressed by fix passes: deregulation may-only plus `sole_rule`; offcondition_free prohibit rows not ranked (ASSUMED b); mixed families counted as neither (ASSUMED); label suppression; pipeline tests. Reviews: docs/reviews/2026-11-05-ablation-slice1-review.md and 2026-11-05-ablation-slice1-rev2-review.md. The `care_duty_on_women` formula carries a one-step grace chosen after seeing the plain form fail (disclosed in "Slice 1 revision 2" note d).

### Pass test (plans/priority.md, layer 4)

The test requires: deterministic and stable across `k` and across `step_mode`; rediscovers kibbutz R2 and ectogenesis R5; labels at least one strand mismatch against hand tags, reported not fixed. Observed: runs on all 25 with zero silent errors; stable across k=6,8 (0 disagreements); `step_mode` not varied in this run; kibbutz R2 (tied top) and ectogenesis R5 (top) rediscovered; strand mismatches not tabulated in this run; 4/5 on the revision-2 tops. The test as written does not allow "passed": two of its clauses (`step_mode` stability, strand-mismatch label) are unevidenced here. Verdict: runs, stable across k, rediscovery met, 4/5, incomplete on two clauses, and weakened on semantics by the derived-power finding.

### Decisions waiting on the author

1. Derived power for unregulated actions: keep false (status quo; cuts of sole prohibitions on power properties stay invisible) or true (consistent with "always enabled"; re-preregister layer 1 before changing).
2. Ratify ASSUMED b (offcondition_free not ranked) and mixed-neither.
3. Record the one-step-effect convention for action obligations in an ADR and fix the stale `care_duty_on_women` gloss.
4. Slice 2 go/no-go.

### Reproduction

`cd /Users/rees/Documents/computational-liberation && uv run phil rules ablate --k 6,8 --json ablate-25-v4.json --summary ablate-25-v4-summary.json`

Outputs: `/private/tmp/claude-501/-Users-rees-Documents/3aaae34a-2247-402e-bd6d-424feea4d706/scratchpad/ablate-25-v4.{txt,json}` and `ablate-25-v4-summary.json`.

## Derived-power decision: evidence (2026-11-05)

Question: `(enabled a ...)` is constant false for an action no `may`/`must` names (ADR 0013 amendment 2026-11-03), so cutting a sole prohibition never moves a power property (mwpa-property R7 scores 0 on `cannot_contract`).

Experiment: patched `rules_lower.py` so a nameless action reads enabled (disabilities still subtract), ran `phil rules check-all --json --no-cache` on all 25 entries, reverted. Diff against the committed semantics (`base.json`/`alt.json` in the session scratchpad; not kept):

- 14 preregistered layer-1 verdicts flip. `financial_dependence` and `financial_dependence_unpropertied` go holds_to_k -> violated under coverture itself (a coverture wife "owns earnings" because nothing names `keep_earnings`); `double_burden` reachable from coverture on; `creditor_shield` reachable in four MWPA entries. That is the 2026-11-03 MWPA backtest broken at its root, plus the police/guardianship falsifier the amendment was written for.
- 18 derived fluents across the dataset read a nameless action: `contract`, `keep_earnings`, `hold_property`, `control_property`, `sue`, `reassign`. All are liberties the encoding withholds by silence, not powers a rule grants.
- Side note: the uncached run reports 7 rows the cached baseline lacks (`dependent_cannot_exit` on six entries, `subject_cannot_exit` on coverture); applicability, not verdicts. Cache may be stale; check before slice 2.

Options:

(a) Keep false. Cost: prohibition-only strands are invisible to `load_freedom` through derived powers. Document as a known blind spot; mwpa R7 stays a miss.
(b) Flip to true. Rejected by the experiment: 14 flips, coverture reads liberal.
(c) Per-action `liberty` flag (encoder choice, preregistered). A liberty action is enabled whenever no disability on it holds, granted or not; a power action keeps the amendment's semantics. Initially only `contract` in the coverture chain is a liberty (R7 is a disability on something people do by default; R15 then grants it anyway). Predicted layer-1 blast radius: zero flips (R7 holds through mwpa-earnings; R15 covers sole-trader on). Predicted ablation change: R7 scores on `cannot_contract` in coverture, mwpa-property, mwpa-earnings, mwpa-property-narrowed; coverture top may become a three-way tie R6/R7/R4. Needs: schema field on action decls, both lowerings (`rules_lower`, `rules_reference`), ADR 0013 amendment 3, tests, re-preregistration of the coverture-chain ablation tops before rerun, and the ADR 0013 monotonicity polarity rule re-checked for liberty actions (a `must_not` on a liberty is now the only thing that moves it).

Recommendation: (c).

## Revision 3 run (2026-11-04 local, headed 2026-11-05; engine 9cf3672, liberty flag)

Preregistration: plans/priority.md "Slice 1 revision 3" (commit 98ae2f2, before the engine or dataset change). Dataset change: `liberty: true` on `contract` in coverture-household, inherited by six mwpa-* entries (7 entries, 7 JSON lines). Engine: ADR 0013 amendment 2026-11-05.

| # | Prediction | Result |
|---|---|---|
| 1 | Zero layer-1 verdict changes across 25 entries | **held**: 0 flips, row by row against the committed-semantics baseline (`check-all --no-cache`) |
| 2 | R7 deletion flips `cannot_contract` holds_to_k -> violated (freedom up) in five entries; not deregulated; no prohibit variant | **held**: load_freedom_up 1 at k=6 and k=8 in coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings; `deregulated` false, `sole_rule` true; no R7~prohibit row |
| 3 | coverture and mwpa-property tops become {R6, R7}; kibbutz R2, footbinding R3, ectogenesis R5 unchanged; rediscovery 5/5 | **held**: tops exactly {R6, R7} in all five chain entries (R4 did not join); other 20 entries' tops unchanged; 5/5 |
| 4 | Non-liberty entries byte-identical to revision 2 apart from timing | **held**: 18 of 18 identical after stripping timing fields |
| 5 | Metamorphic tests pass unchanged | **held**: 536 pass, no test touched |

Totals: 25 entries, inconsistent_after 0, uncounted 0, k_disagreement empty on every R7 row. Drift from the revision-3 preregistration: none.

**Calibration disclosure (added after docs/reviews/2026-11-05-liberty-flag-rev3-review.md, item 5).** The fifth hit is not a blind hit. The sequence was: revision-2 miss on mwpa-property R7; diagnosis of the engine's blind spot on that item; a full-dataset experiment that computed which verdicts move under each semantics; a preregistration of a semantics that, by construction, turns that item into a hit; the run. Prediction 3 could not have failed short of a coding error. The flag was applied to the one action that missed. The honest score history is 1/5 blind (v1), 4/5 after fixes that saw the misses (revision 2), 5/5 after a semantics change motivated by the remaining miss (revision 3). "5/5" is a calibration result: the instrument now does what it was told to do on a known-answer item. It is not rediscovery evidence and is not cited as such in docs/claims.md (L21, weakened). Any future rediscovery claim needs an entry set the semantics was not tuned on.

**Date convention.** Headings and review file names dated 2026-11-05 in this batch were written late on 2026-11-04 local time (EST); commit timestamps are authoritative. From here on, dates follow the local commit date.

**ABM effect (review item 2).** `philengine/abm/model.py` gates an agent's available actions on `Reference.power`, so after the liberty flag `contract w` is a lawful candidate for every unmarried wife agent in the seven coverture-chain entries. It has no effects and zero payoff, but the random-lawful-candidate draw changes RNG consumption, so the frozen layer-2 gate record (engine 0abf7a4) is not guaranteed to reproduce on those entries. Recorded in ADR 0013 and plans/layer2-abm.md; rerun 2026-11-04 at engine 3da984b: all four criteria reproduce (plans/layer2-abm.md "Gate rerun 2026-11-04, after the default-capacity change").

**Author decisions from the revision-3 review** (docs/reviews/2026-11-05-liberty-flag-rev3-review.md):
1. One convention for default capacities. The dataset now has two: the `liberty` flag (contract only) and an implicit universal `may ... when true` (leave in six entries, sleep_home, refuse_binding, and sue via R9's complement). The implicit-may convention would have produced the same R7 flip with no engine change. Options: (i) flag sue, leave, sleep_home, refuse_binding and delete the implicit `may` rows (R4 `sue` starts to score in the coverture chain; implicit-may rows leave the ablation denominators); (ii) un-flag contract and give it `may contract when true` like leave; (iii) keep both and write the rule for which to use. Either (i) or (ii) needs a preregistered blast radius first.
2. Rename `liberty`. The reviewer is right that contracting is a Hohfeldian power and the mechanism is "default capacity of that kind of agent, removed only by an express disability" vs "power conferred by a rule". Proposed name: `default_capacity`. One-commit-old field, cheap now.
3. Sanctioned `must_not` on a flagged action: code ignores it (only disabilities bar the capacity); the ADR gloss implies it should bar. Under the "capacity" reading the code is right (capacity exists, exercise is punished). Pin with a test either way.
4. Layer 2: rerun the gate on the seven coverture-chain entries once the spawn-parallel engine change lands, or accept the record as not reproducing on those entries.

Honest limits: the flag is an encoder's judgment and this run flagged exactly one action; the result shows the semantics does what the preregistration said, not that `contract` is the right and only liberty in the dataset. A council seat should check the flag against Blackstone (encoding faithfulness) and look for other prohibition-withheld liberties the encoder left as powers (`sue` under companion-*? `leave`?).

Found while running: a cached `check-all` printed 116 distinct (institution, property) rows where an uncached run printed 123. Diagnosed by a builder: not the cache key (it already covers the full entry, the property's formal text and check kind, k, init, compliance, step_mode, engine source hash and z3 version) but a cache hit that kept the stored property NAME. `subject_cannot_exit` and `dependent_cannot_exit` have identical formal text and share an entry, so a hit returned the twin's name and the two rows collapsed under one key in the diff script. Verdicts were never wrong. Fixed in the engine (`res.property = name` on hit, tests in tests/test_rules_cache.py); the uncached diffs above are unaffected.

Reproduction: `cd computational-liberation && uv run phil rules check-all --json --no-cache` and `uv run phil rules ablate --k 6,8 --json ablate-25-v5.json --summary ablate-25-v5-summary.json`. Outputs in the session scratchpad, not kept.

## Revision 4 run (2026-11-04 local; engine faefef1 for layer 1)

Preregistration: plans/priority.md "Slice 1 revision 4" (a7ca980, before the dataset edit 2d83419 and the engine rename faefef1).

| # | Prediction | Result |
|---|---|---|
| 1 | Zero layer-1 verdict flips | **held**: `phil rules diff --baseline data/verdicts-baseline.json --no-cache`: 0 changed, 0 added, 0 removed of 123 |
| 2 | Gate (a)-(f) passes; care+control cluster, airline control and crisis-team exclusion unchanged | **held**: GATE PASS; (b) the three pairs partial(care+control) at guard+strands, crisis-team none at every level, controls none; (c) distance 1; (d) kibbutz; (e) 123/123; (f) rename detected |
| 3 | R4 (`must_not sue` when married) deletion flips `no_standing` reachable -> open in six entries; `no_standing_persists` does not flip; load_freedom_up 1; not deregulated | **held**: exactly that in coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings, mwpa-sole-trader; `families_up` = [no_standing] only; `deregulated` false; `k_disagreement` empty |
| 4 | Tops {R4, R6, R7} in five chain entries, {R4, R6} in mwpa-sole-trader, {R6} in mwpa-suit; all 18 other entries unchanged from revision 3 | **held**, every entry |
| 5 | 48 fewer rows per k; the deleted ids leave the not-ranked lists; inconsistent_after 0, uncounted 0 | **held**: 383 -> 335 rows per k; totals 0 / 0. The kept explicit permissions (crisis-team R5/R9, police R10, public-library R4, mwpa R15/R16) are absent from `deregulated_not_ranked`, as the default-capacity skip intends |
| 6 | No rediscovery claim | none made |

Engine for the ablation: 7dc108c (spawn-parallel, `--workers 4`, 86 s wall for 25 entries at k=6,8). Two engine commits were used for this revision: faefef1 for the layer-1 diff and gate, 7dc108c for the ablation; the layer-1 semantics (rules_lower, rules_reference, rules_checks, sexpr) are identical between them (the source hash the baseline records did not change). The first diff run exited 1 after printing "0 changed, 0 added, 0 removed" because the scoreboard append raised on a prose header; the cached rerun exited 0. The scoreboard rows marked `dirty+` were written while other builders' uncommitted edits (abm/, rules_ablate.py) sat in the engine tree, none of them in the layer-1 semantics. Drift from the revision-4 preregistration: none. Clauses that could not fail as written, per docs/reviews/2026-11-04-capacity-convention-rev4-review.md item 7: prediction 5's "the deleted ids leave the not-ranked lists" (a deleted rule cannot appear in any list), prediction 6 (a disclaimer, not a prediction), and prediction 2's airline clause (airline-flight has no `isomorphic_to` expectation, so "still matches" was never checked by the gate). They are recorded as not testable rather than held. Reproduction: `cd computational-liberation && uv run phil rules ablate --k 6,8 --workers 4 --json ablate-25-v6.json --summary ablate-25-v6-summary.json`.

## Revision 4b run (2026-11-04 local; engine 21ec685)

Preregistration: plans/priority.md "Slice 1 revision 4b" (f12b061, before the engine edit).

| # | Prediction | Result |
|---|---|---|
| 1 | Exactly one row changes: mwpa-suit `R16~prohibit` leaves `offcondition_free_not_ranked`, ranks with a freedom_down flip on no_standing, up 0 | **held**: row-by-row diff against the revision-4 output finds that one row; `offcondition_free` false, down 1, up 0, flip no_standing freedom_down |
| 2 | No top set changes | **held**: scoreboard top_rule_changes 0 |
| 3 | All other rows identical apart from timing | **held** (334 of 335 rows per k identical) |
| 4 | Layer 1 untouched | not run; the change is in rules_ablate only (the layer-1 source hash is unchanged) |

Council item 7 (docs/reviews/2026-11-04-capacity-convention-rev4-review.md): the spawn-equality test now covers a default-capacity action and a non-true-condition `may`; no serial artefact is kept. Reproduction: `uv run phil rules ablate --k 6,8 --workers 4 --json ablate-25-v8.json --summary ablate-25-v8-summary.json --prev ablate-25-v7-summary.json --scoreboard docs/scoreboard-ablate.md`.

## Slice 1 close-out run (2026-11-06; engine 27e24c0 = ENGINE_PIN, before revision 5)

Preregistration: plans/priority.md "Slice 1 close-out" (9b81737, before any run). Dataset: 26 entries, 219 rules, 345 rows per k (690 over k=6,8).

### (i) step_mode

`rules_lower.STEP_MODES` = (`one`, `many`). Three full runs: `one` twice, `many` once, k=6 and 8, `--workers 4`. Compared per (entry, row id, k) on every field except timing.

| # | Prediction | Result |
|---|---|---|
| 1 | Top sets identical in all 26 entries, both k | **held** |
| 2 | Every ranked row's load_freedom_up identical (clause criterion) | **held**: 690 of 690 rows identical on every field, ranked or not |
| 3 | Some rows differ elsewhere, at most 10 per k | **drift (in the stable direction)**: 0 rows differ. The cause is upstream: `check-all --no-cache --step-mode many` gives the same verdict as `one` on all 134 layer-1 rows. No property verdict in the dataset, base or ablated, depends on whether two actions may share a step at k <= 8 |
| 4 | inconsistent_after 0, uncounted 0, k-disagreements 0 in both modes | **held** |
| 5 | The two `one` runs identical | **held**: 690 of 690 |

That the flag is live in the ablation path was checked on a two-action toy (goal needs a1 and a2, k=1): under `many` the prohibit variant of R1 flips the goal reachable -> open, under `one` nothing flips. So the zero is the dataset's, not a dropped flag. Reading: the clause passes, but on this dataset it cannot discriminate: it shows no instability, not robustness to an interleaving effect the dataset never exercises. A step-mode-sensitive entry (two parties who must act in the same step) would be needed to test it properly. Recorded; nothing tuned. Gap noted: the ablation JSON and summary do not record `step_mode` (the check-all JSON does); the runs here are labelled by file name only.

### (ii) strand mismatches (k=6; k=8 identical)

Method as preregistered: a rule's reading uses its ranked rows (deletion, and `~prohibit` for a `may`); up/down = max over them. Goods load is 0 everywhere because no goods property exists, so "tying" here means "freedom load >= 1, goods unmeasured"; every label is provisional until slice 2.

| class | tag | count | rules |
|---|---|---|---|
| reads tying, agrees | tying | 18 | R4 (sue; no_standing) in coverture-household, -us, mwpa-creditor-exemption, -property, -property-narrowed, -earnings, -sole-trader; R7 (contract; cannot_contract) in the same less sole-trader; kibbutz-childrens-house R2 (care_assigned_by_sex); footbinding, footbinding-no-pledge R3 (binding_practised); ectogenesis, gestational-surrogacy R5 (care_duty_on_women) |
| **M1: reads tying, tagged otherwise** | rival | **18** | exit and refusal bars, all on the `cannot_exit` family: R6 in coverture-household, -us and the six mwpa-*; police-crisis R4; cps R10; companion-ownership, -guardianship, -guardian-renamed R6; kibbutz-childrens-house and -no-implicit R4 (sleep_home); airline-flight R4; footbinding and -no-pledge R9 (refuse_binding) |
| M1 | superadditive | 0 | |
| **M3: reads protection (up 0, down >= 1), tagged tying** | tying | **6** | police-crisis R10 (`may sue`; ~prohibit down on no_standing); crisis-team R9 (`may sue`; same); mwpa-suit R16 (`may sue`; same); cps R8 (`must counsel_appointed` when case_open; deletion down on no_standing); mwpa-sole-trader R15 and mwpa-suit R15 (`may contract`; ~prohibit down on cannot_contract) |
| M2: tying unconfirmed (up 0, down 0) | tying | 26 | police-crisis R1, R6; cps R1, R5, R6; crisis-team R1, R6; paternity-quota R2, R7; transferable-leave R7; companion-ownership R9, R11; companion-guardianship R11; companion-guardian-renamed R9, R11; lease R5; airline-flight R6; R11 (creditor must_not attach) in the six mwpa-*; mwpa-suit R19 (one flip, unsigned on this engine); ectogenesis R6; gestational-surrogacy R6 |
| reads protection, no tag comparison | rival / superadditive | 5 / 2 | crisis-team R5, paternity-quota R1, public-library R4, ectogenesis R1, gestational-surrogacy R2 / ectogenesis R4, gestational-surrogacy R4 |
| no reading (up 0, down 0) | rival / superadditive | 14 / 33 | not readable without goods load |
| not readable (no ranked row) | tying / rival / superadditive | 43 / 42 / 12 | every row deregulated or offcondition_free |

Total 219 rules.

| # | Prediction | Result |
|---|---|---|
| 6 | 36 read tying; 18 tagged tying agree (the listed rules) | **held** exactly |
| 7 | M1 = 18, all rival, none superadditive, the listed exit/refusal bars, all cannot_exit | **held** exactly |
| 8 | M3 at least 1 (mwpa-suit R16), 1 to 5 in all | **drift**: 6. R16 is there; the other five are the same shape (a permission to sue or contract, tagged tying, whose prohibition would remove standing or contract) plus cps R8, an obligation (appoint counsel) that carries the child's standing. The range was too low; the direction held |
| 9 | M2 20 to 45, including mwpa-suit R19, the chain's R11, tying obligations in police-crisis, cps and the leave pair | **held**: 26, all named groups present |
| 10 | Clause passes (at least one mismatch labelled); no tag edited | **held**: 24 mismatches labelled (18 M1, 6 M3); no tag touched |

Reading, facts first: the hand tags call every exit bar `rival` while the ablation finds exit bars the most load-bearing rules in 18 entries; and six rules tagged `tying` are, on the ablation, permissions or duties whose removal costs the subject standing or contract (the tag seems to follow "part of the bundle" where the ablation reads "protection inside the bundle"). Which is right is the strand-tag redesign's question (docs/plan.md), not this run's. Tags are not edited.

### Layer-4 pass test: final verdict

| clause | evidence | status |
|---|---|---|
| deterministic | two `one` runs, 690/690 rows identical; spawn-workers equality test | met |
| stable across k (preregistered 6, 8) | 0 k-disagreements, both modes | met |
| stable across step_mode | 690/690 rows identical | met, **uninformative on this dataset** (no verdict depends on step_mode) |
| rediscovers kibbutz R2, ectogenesis R5 | R2 tied top, R5 top | met after fixes that saw the misses (revision-3 calibration disclosure: not blind evidence; L21 stays weakened) |
| labels at least one strand mismatch, reported not fixed | 18 M1, 6 M3 | met |

**Verdict: passed as written**, with two disclosures that limit what the pass means: the rediscovery clause is a calibration result, not a blind one, and the step_mode clause was met on a dataset that does not exercise interleaving. Slice 1 is closed on these terms. Drift: prediction 3 (no row moved at all) and prediction 8 (6 M3, above the 1-5 range).

Reproduction: `cd computational-liberation && uv run phil rules ablate --k 6,8 --workers 4 --step-mode one --json A-one.json --summary A-one-summary.json` (and `A-one2`, and `--step-mode many` to `A-many`); `uv run phil rules check-all --json --no-cache --step-mode many|one`. Outputs in the session scratchpad (`/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/A-*.json`, with the comparison script `cmp.py` and the strand tabulation `strand.py`), not kept.

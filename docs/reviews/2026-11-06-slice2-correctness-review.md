# Correctness review: priority slice 2 (philosophy-engine a16691b; run 725c63d + 7383e7a) — 2026-11-06

Fresh agent, correctness seat (ADR 0014); did not build, encode or coordinate this slice. Read-only on both repositories; this file is the only write. Second encoder: agent, not someone living under the institution (ADR 0012).

Subject: philosophy-engine a16691b (goods) and c69aaf1 (dataset sync, = ENGINE_PIN); computational-liberation 725c63d (dataset), 7383e7a (plans/priority-slice2-results.md), against plans/priority-slice2.md as committed at cd2f895 (`git diff cd2f895 HEAD -- plans/priority-slice2.md` is empty). Both trees were clean at the pins.

What I ran (outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/council-s2/`, not kept):

- The reproduction line in full, `phil rules ablate --k 6,8 --workers 4 --json --summary --readings --scoreboard <copy>` on the 27-entry dataset (7m23s). I recomputed every headline quantity from the JSON with my own script (`analyse.py`), not from the builder's readings file.
- E3: the same run with `--properties` = properties.json minus the five goods, compared field by field on every non-goods field (`cmp.py`).
- E1: `git archive` of e27127b and a16691b into scratch, both run on the 480bb6d dataset (26 entries, k=6,8), compared the same way.
- A vacuity probe (`probe_vacuity.py`). For every entry where a goods property or alternative applies, it runs persists, invariant and reachable on the unablated entry at k=6 and k=8, plus the two vacuity flags.
- A reachability probe on kibbutz-childrens-house (`probe_kib.py`).
- Six mutations of rules_ablate.py in a scratch copy, run against tests/test_rules_ablate_goods.py + tests/test_rules_ablate.py (47 tests).
- computational-liberation `pytest -q`: 32 passed.

## Reproduction

| claim | reproduced |
| --- | --- |
| N(T) = N(F) = 3, {R4 no_standing, R6 cannot_exit, R7 cannot_contract} | yes, k=6 and k=8 |
| G(T) = 5 (R2 4, R3 1), G(F) = 4 (R2 3, R3 1), both encoders | yes; no `~prohibit` row of a base rule carries goods in either end state |
| R2 in F loses cared_for, known_carer, mutual_household_care, not provided_for (R20 still provides) | yes (`provided_for` stable > stable) |
| C: T holds_to_k, F violated; R: 1 (R14) vs 1 (R20) | yes (R13 flips no financial_dependence-family property) |
| readings: 11 read rows, 6 agree, 0 mismatch, 5 no row; the per-row table in 4.2 | yes, row for row, k=6 = k=8 |
| no reading differs by encoder (`contested_readings` 0) | yes |
| `provided_for` vs `provided_for@encoder-2`: same state in all 254 rows where read | yes, 254 rows, 0 differ |
| uncounted 0, inconsistent_after 0, k-disagreements 0, 712 rows | yes |
| E1: 690/690 rows identical on pre-existing fields, goods fields empty | yes (690/690; 0 non-empty goods rows) |
| E3: 712/712 identical on non-goods fields with and without the goods | yes |
| scoreboard row `27 \| 356 \| 0 \| 0 \| 0 \| · \| 24 \| 0` | yes. top_rule_changes shows `-` in my run because I passed no `--prev`. |

The numbers stand. The findings below are about what the numbers mean and what the tests would catch.

## Findings

1. **[major] "absent" as built is "no bearer", not "the good never holds".** rules_ablate.py:99 reads `absent` from `res.vacuous`. That flag is set at rules_checks.py:361 when the implication premise is unreachable (`antecedent`, rules_checks.py:204) or when no `is_*` fluent ever holds. For every slice-2 good, which is an implication guarded on the bearer, a vacuous formula is one that is *true at every step*.

   Section 2 of the preregistration gives encoders the opposite gloss: "a `persists` that is vacuous (the formula never holds in any compliant trace) reads as 'the good is absent'". Both encoders wrote in that sense: "In kibbutz the good is absent from the start ... until sleep_home" (data/institutions/goods-encoding/encoder-1.yaml:31; encoder-2.yaml:31). Section 4.1 predicted the same: kibbutz `child_with_family` "absent (R4 bars `sleep_home`)", with R4 deletion gaining it.

   With the one-step grace every bearer-guarded formula is true at step 0. A good *barred* for an existing subject therefore reads `fails`, so `fragile`, the same state as a good that is guaranteed but may lapse. I checked this directly. In kibbutz-childrens-house the home disjunct never holds for an existing subject at k=6 or 8 (`reachable` → open). With R4 deleted it is reachable. Yet `child_with_family` is fragile > fragile on the R4 row: no gain is recorded.

   So the lattice as implemented is: stable > {may lapse, or barred} > {no subject exists}. The code matches section 6's letter ("absent (persists, vacuous)", using the existing flag). It does not match section 2's stated meaning, and the difference decides two preregistered rows: kibbutz `child_with_family` base absent, and kibbutz R4 gained 1.

   The results file reports both as misses (4.1, 4.2 "gained missed"). It puts them down to "already fragile" without saying that the instrument cannot represent "barred" at all. Not a code bug against section 6. It is an instrument property the results should name, because it also produces F2 (finding 5).

2. **[minor] The vacuity probe found no misread in the base states.** I checked all 140 base (entry, good, k) cells, primary and alternative:
   - every `stable` is also `invariant` holds_to_k, so no good that fails to hold reads stable;
   - every `fragile` formula is reachable;
   - no `absent` has a reachable antecedent;
   - there is no base `absent` anywhere.

   Vacuity is computed on the same `Grounded` system as the check (same k, init `declared`, compliance strict, rules_checks.py:357-361), so the before/after states of a row are comparable. Across k the goods k-disagreement block (rules_ablate.py:500ff) catches a subject who becomes reachable only at k=8. None occurred.

   Two latent soundness gaps, neither firing in this run:
   - (a) `subject_exists` looks at *any* `is_*` fluent (rules_checks.py:226). A good whose antecedent is reachable reads `absent` in an entry where no `is_*` fluent holds. `mutual_household_care` (antecedent `married`) is the exposed one; in the coverture family `marry` sets `is_subject`, so it does not bite.
   - (b) Unknowns are handled asymmetrically. An undecided antecedent is uncounted (rules_ablate.py:101-102). An undecided `subject_exists` (None) leaves `vacuous` False, and the good reads `stable`. ASSUMED drift item 4 covers only the first.

3. **[minor] Contested alternatives are kept apart, but the test that should prove it cannot fail on pooling.** In the code, `<name>@<encoder>` is evaluated as its own property (expand_contested, called in both `ablate` and `ablate_multi_k`). It is excluded from `flips`, `load_goods` (rules_ablate.py:424) and summaries, and it enters only `goods_alt_states` and `load_goods_by_encoder`.

   I checked this as mutation M2: replacing the filtered dict at :424 with all of `gstates` pools the alternative into `load_goods`. All 47 tests still pass. tests/test_rules_ablate_goods.py:89 gives the *alternative* the never-flipping formula and the same family as the primary, so a union of families is still 1. The test needs the reverse: an alternative that is lost while the primary is not, asserting `load_goods == 0`.

   The run is unaffected: the one contested pair differs in 0 of 254 rows, so pooling would have produced the same numbers. That is also why the run cannot show separation; only the code reading and the toy test can.

   Two further points:
   - `load_goods_by_encoder` picks the alternative by encoder *position* (`i > 0`, :429-433) across all goods. That is right only while every goods property lists its primary first.
   - If an alternative is uncounted while the primary is counted, that good drops out of the encoder's view (:434) without falling back or being noted. Neither case occurred.

4. **[minor] Tests miss the decisions this slice turns on.** Mutations that survive all 47 tests:
   - M1 swaps the order of `fragile` and `absent` in `GOODS_ORDER` (:87). This is the ordering behind F2, and nothing pins it. The only fragile ↔ absent move in the tests is absent → stable, which is a gain under either order.
   - M2 pools alternatives (finding 3).
   - M5 deletes the goods k-disagreement block (:500ff). No test has a goods state that differs by k.

   Mutations that are caught:
   - M3: ignore vacuity (3 tests fail);
   - M6: undecided vacuity read as stable (1 fails);
   - M7: never use the alternative (1 fails).

   The preregistered test list (section 6) is otherwise covered, and the validator rejections are thorough. Fix: three small fixtures, one per surviving mutation.

5. **[major, interpretation] F2 (ectogenesis R1~prohibit) is an instrument property, not a correctness bug and not a faithful reading of the good.** The mechanism, reproduced:
   - R1 (`provider may start_gestation`, condition `true`) prohibited means nothing is ever gestated or decanted, so `is_subject` never holds.
   - All three goods turn vacuous: fragile > absent, lost 3.
   - With up 0 the row reads constitutive.
   - gestational-surrogacy R2~prohibit does the same (lost 2), information only.

   The code does exactly what section 6 specifies, given finding 1's reading of "absent". The engine's own toy test asserts this behaviour (tests/test_rules_ablate_goods.py:101-103: "no subject is ever enrolled ... stable > absent"). It is pinned behaviour, committed at 14:35, before the dataset (14:46) and the run (15:00).

   But it is not what the goods say. Each good is "for" a subject (section 3). A rule whose removal means no subject exists has not taken care from anyone. The instrument ranks "no child" below "a child whose care may lapse" and advises "redesign, do not cut" for the permission to gestate.

   The results file handles F2 honestly: it reports the firing and names the vacuity route. It also leaves the order as a council design question (results:98). I agree, and add that section 2's own gloss of "vacuous" already disagrees with the engine's flag (finding 1). So the preregistration did not, in substance, define this state the way the code computes it.

   Options for the author:
   - (a) a fourth state, "no bearer", outside the order, so no lost and no gain;
   - (b) define absent as "bearer reachable, good never holds after the grace" (a reachable check on premise ∧ ¬conclusion with no ∧ conclusion step), which would also give kibbutz R4 its gain;
   - (c) keep the order and say in every reading that "lost" includes "no subject".

   Until one is chosen, F2's firing measures this definition, not where goods load sits.

6. **[minor] Drift is recorded honestly; `Property.entries` was not post-hoc.**
   - The need for `entries` follows from the merge log (89c4e28, 14:21: "both wrote `child_with_family` as one disjunct per entry ... accepting the constant-false warning"). Both encoders' notes state it. The engine adaptation landed at 14:35, before any goods entered the dataset or any run.
   - It is disclosed in the engine commit message ("Adaptation (not in section 6)") and as drift item 2.
   - Its effect is limited to making `child_with_family` applicable in cps, kibbutz and ectogenesis. For the other goods every named fluent is declared where they are read: the coverture root change declares `has_own_income` family-wide.
   - The formulas in properties.yaml are character-identical (after whitespace) to encoder 1's, and the alternative to encoder 2's. Encoder 2's `known_carer` and `child_with_family` differ textually and were merged as equivalent. I did not rerun the z3 equivalence.

   Two notes:
   - (i) `entries` lowers undeclared fluents as false with only a warning. A misspelt fluent in a listed entry would be read silently as constant false. A check that each listed entry declares at least one fluent of every disjunct would close that.
   - (ii) The F2 mechanism was visible in the builder's toy test before the run. Not preregistering it was correct, since section 4 could not be edited, but the results could say it was foreseeable.

   Drift items 1 and 3-11 match what I see.

7. **[minor] The 4.1 "why fragile" paragraph is right but incomplete for kibbutz.** The `release` explanation (results:43) covers `cared_for` and `known_carer`. For `child_with_family` the cause is finding 1: barred reads fragile. The R4 "gained missed" row should cite that, not just the fragile base.

## Section 6 conformance (item 1 of the brief)

- **Schema** (schemas_rules.py:207-264): matches. `polarity: good` is required on goods and rejected elsewhere. `contested` is required (`[]` = equivalent). There are at least two distinct encoders, `check: persists`, and each alternative must parse.
- **Goods direction:** state-based, not verdict-based. A persists > persists change in vacuity is read (:385-393). `lost`/`gained`/`mixed` are per family, and mixed counts in neither.
- **Readings and agreement:** as section 4 defines them.
- **summarize / scoreboard_stats:** the added columns are present.
- **readings_table:** includes unranked rows and goods-only changes (drift 7).
- **Other:** no freedom column moves (E1, E3 reproduced).

## Verdict: weakened

The engine implements section 6 as written. Every headline number reproduces independently: N 3 = 3, G 5 vs 4 under both encoders, C, R 1 vs 1, 11 read rows (6 agree / 5 no row), 0 encoder disagreement, 254/254 `provided_for` rows equal, E1 690/690, E3 712/712.

The verdict is weakened, not supported, for two reasons:

- The goods state the slice turns on, "absent", is computed as "no subject exists". Section 2 and both encoders meant "the good never holds". As a result the instrument cannot represent a barred good (kibbutz `child_with_family`, R4's gain). It also counts the non-creation of a subject as a loss of that subject's goods, which is the whole of F2 (findings 1 and 5).
- The tests would not catch a pooled alternative, a swapped fragile/absent order, or a dropped goods k-disagreement (findings 3 and 4).

The route comparison does not depend on either issue: every goods change in T and F is stable > fragile under a must-be duty. The comparison stands as reported. The readings outside coverture, and F2, should be read as properties of this state definition.

The author has to decide what "absent" means (finding 5, options a-c). Then the kibbutz and ectogenesis rows should be rerun under that definition before the readings table is called a result.

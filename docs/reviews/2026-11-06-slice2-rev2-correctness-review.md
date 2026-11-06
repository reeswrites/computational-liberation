# Correctness review: priority slice 2, revision 2 (philosophy-engine a4ea4b3; ENGINE_PIN 7a67c21; dataset e519609, 28b4528, d503de7) — 2026-11-06

Fresh agent, correctness seat (ADR 0014). I did not build, encode or coordinate this slice or its revision 1, and I did not write the revision-1 reviews. Both repositories were read-only for me; this file is my only write. Second encoder: agent, not someone living under the institution (ADR 0012).

Subject: philosophy-engine a4ea4b3 (R2.1, R2.2), plus a87cb2e and 7a67c21 (data-only syncs: `git diff a4ea4b3 7a67c21` touches only data/institutions/*.json). computational-liberation e519609 (D1), 28b4528 (D2), d503de7 (D3 and the results' "Revision 2" section), checked against plans/priority-slice2.md "Revision 2" as committed at cf29916 (`git diff cf29916 HEAD -- plans/priority-slice2.md` is empty). Both trees were clean, and computational-liberation's data/institutions/*.json is byte-identical to the engine's at the pin.

What I ran (outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/council-r2/`, not kept):

- **Engine copy.** `git archive 7a67c21` into scratch (`eng/`), run with `PYTHONPATH` so that the repo was never imported or written.
- **D3 run.** The reproduction line on the D3 dataset: `rules ablate --k 6,8 --workers 4 --json --summary --readings --scoreboard <copy> --prev <revision-1 summary>`, about 11 min. I recomputed every headline quantity from the JSON with my own script (`analyse.py`).
- **D1 run.** The same on D1, from `git show e519609:data/institutions/*.json`. I compared it field by field with the revision-1 run (`cmp_r1.py`); the revision-1 baseline is the predecessor seat's independent run, which equals the builder's `ablate-27-s2.json`.
- **Mutations.** Eight mutants of the engine, each in its own scratch copy, plus an unmutated control. Each ran against tests/test_rules_ablate_goods.py and tests/test_rules_ablate.py (76 tests).
- **Test suites.** The full engine suite on the scratch copy: 609 passed, 2 skipped. computational-liberation `pytest -q -p no:cacheprovider`: 32 passed.
- **Probes.** Direct `reachable` queries on cps R2~prohibit, a reading of ectogenesis R4/R5, and loader probes for the `subject` checks.

## Reproduction

My D3 run's JSON, summary and readings table are byte-identical to the builder's `run2/ablate-27-r2*` files, and my D1 JSON is identical to the builder's `ablate-D1.json`. The scoreboard row is `27 | 356 | 0 | 0 | 0 | 0 | 34 | 0`; the engine column reads `unknown` in my copy only because the scratch tree is not a git checkout.

| claim | reproduced |
| --- | --- |
| n/a rows: exactly ectogenesis R1~prohibit (cared_for, known_carer, child_with_family fragile > n/a), gestational-surrogacy R2~prohibit (cared_for, known_carer fragile > n/a), airline-flight R1~prohibit (stable > n/a); lost 0 under both measures at k=6 and 8; no base cell n/a | yes. Ectogenesis and surrogacy are ranked, up 0, down 1; airline is unranked, up 1 |
| kibbutz: child_with_family base absent; R4 absent > fragile, possible gained 1, guaranteed gained 0 | yes, k=6 and 8 |
| kibbutz R3: no goods change, possible lost 0 | yes (all three goods unchanged) |
| ectogenesis R4~prohibit: possible lost 3 (cared_for, known_carer, child_with_family fragile > absent), guaranteed 0, constitutive, both encoders | yes |
| chosen_mutual_care: base absent in nine coverture-family entries; only R6 moves it (absent > fragile, possible gained 1, guaranteed 0) | yes: 18 rows (nine entries, k=6 and 8), no other mover, lost 0 everywhere |
| route comparison: N 3 = 3 {R4, R6, R7}; G guaranteed 5 (R2 4, R3 1) vs 4 (R2 3, R3 1); G possible 0 = 0; possible gained 1 = 1 (R6); guaranteed gained 0 = 0 | yes, k=6 and 8, both encoders |
| 13 rows, both measures; totals guaranteed 10 read / 6 agree / 4 no row, possible 9 / 5 / 4 | yes (readings table identical) |
| summary: constitutive only ectogenesis and gestational-surrogacy [R4~prohibit]; guarantee_carrying [R2, R3] in nine coverture-family entries, [R2] in airline-flight; hard cases empty; contested_readings 0 | yes |
| goods_rows 34 (predicted 33; extra cps R2~prohibit) | yes |
| uncounted 0, uncounted_reasons {}, inconsistent_after 0, k-disagreements 0, 712 rows; encoder load differences 0; 254 alternative cells, 0 differing from the primary | yes |
| E1r2 (D1 vs revision 1): 0 non-goods differences in 712 rows (flips including goods persists flips, uncounted, check kinds, entry not_applicable, k-disagreement); 0 guaranteed-transition differences in 1924 goods cells; every revision-1 `absent` cell (14, all in the three rows) now `not_applicable`; `load_goods_guaranteed` = revision-1 `load_goods` everywhere else, 0 in those rows (revision 1: 2, 3, 2) | yes |
| E3r2/E4r2 (D3 vs revision 1, same comparison): the only non-goods differences are the `strand` of coverture-floor R20 and R20~prohibit at k=6 and 8 | yes |

The headline numbers stand. I did not rerun the iso or gate items (drift 3, E2r2 gate lines).

## Findings

1. **[minor] "Never stable when undecided" is pinned by tests only at the first of the four queries.** The code is correct: each query in `goods_queries` returns `(None, reason)` on anything but sat or unsat (philosophy-engine philengine/rules_checks.py:249-274), and `goods_state_reason` turns that into uncounted (rules_ablate.py:106-114). But three mutants of my own design survive all 76 tests:
   - M10 reads an undecided guaranteed query as stable (`inv.verdict != "violated"` at :269);
   - M11 reads an undecided possible query as absent (`!= "sat"` at :263);
   - M12 reads `no_witness_within_k` as absent (:258).

   The only undecided-query test, test_4c (tests/test_rules_ablate_goods.py:219), makes every goods query unknown, so the subject query short-circuits and the later three branches are never reached. R2.2 4c names only the subject query, so the builder met R2.2's letter. R2.1's sentence "an undecided z3 result at any step is uncounted ... never stable" rests on code reading for three of the four queries. This is the same class of gap as revision-1 finding 2(b), one level down. The run is unaffected: 0 uncounted, 0 unknown. Fix: three monkeypatched fixtures that make only one phase unknown (for M10, unknown only inside `check_invariant` during the goods phase), plus a fixture where the bearer first exists at step k (for M12).

2. **[minor] Loader edges of the `subject` check.** In every case the property still fails to load, or the deviation errs toward refusing:
   - (a) A subject naming a free step variable (e.g. `t0`) raises a raw `z3.Z3Exception: Sort mismatch` out of `load_properties`, not a `RulesLoadError` with exit 2. rules_goods.py:52 treats every unbound symbol as an agent constant. The load still fails, but with a traceback.
   - (b) The per-entry check treats an undeclared fluent in the subject as an error even in an entry listed in `entries` (rules_ablate.py:358). R2.1 asked for "the same rule as `formal`, including `entries`". That rule would accept the fluent and lower it as false, which would turn the good silently `not_applicable`. The stricter check is the better one, but it is a deviation from the letter and should be recorded.
   - (c) Only `Ant -> Subj` is checked (schemas_rules.py:283), as specified. An over-broad subject (one that holds without a bearer) passes and would turn a "no bearer" row into `no_witness_within_k` (uncounted) rather than `not_applicable`. The six subjects in the dataset are the obvious ones, so nothing bites.

3. **[minor, latent] `possible` asks for the whole formula at one step.** The possible query is `Wit(t) ∧ Good(t)` (rules_checks.py:260), and `Good` quantifies over every binding. With two bearers whose goods can hold only at different steps, the good would read `absent` although it is possible for each bearer. The grounding has one agent per role (rules_lower.py:4), and every goods formula in the dataset has a single bearer role, so this cannot bite here. It matters if a good is ever written over several bearer roles.

4. **[resolved] Revision-1 findings.**
   - Finding 1 ("absent" meant "no bearer"): fixed. The engine computes four states from the good's own subject, with witness steps. Test 5b pins the step-0 grace, and my M13 (`Wit = Subj` everywhere) is killed by it. Test 5a pins the barred good, and in the dataset kibbutz R4 now gains 1.
   - Finding 5 (F2): ectogenesis R1~prohibit and gestational-surrogacy R2~prohibit read `not_applicable`, lost 0.
   - Finding 3 (contested alternatives): selection by name (M9 killed per the record; code at rules_ablate.py:511-519 reads `alternative_name(n, e)` with `e != encoders[0]`); an uncounted alternative is listed for its encoder (test_2b).
   - Findings 2(a) and 2(b): closed by test_4b (M8) and test_4c (M6'), with the caveat in finding 1.

   The three revision-1 survivors are now killed:

   | mutant | tests failing |
   | --- | --- |
   | M1a, fragile/absent swapped in `measure_value` | 13, including the 16-pair table, 5a, 5c, 5d, 2, 3 and the CLI test |
   | M1b (mine), absent relabelled fragile in `goods_queries` | 7: 5a, 5b, 5d, 5e, 2, 3, all-four-states |
   | M2, families computed over the alternatives too (rules_ablate.py:499) | 1: test_2_alternative_flips_primary_does_not_never_pooled |
   | M5, goods k block emptied (rules_ablate.py:601) | 1: test_3_goods_state_differing_by_k_is_a_k_disagreement_with_unchanged_verdicts |

   The control copy passes 76/76. Still open from revision 1: 6(i). `entries` lowers an undeclared fluent in `formal` as false with only a warning, and kibbutz `child_with_family`'s absent base state depends on two disjuncts lowered that way. That is the intended reading here, but a misspelt fluent would look the same.

5. **[minor, interpretation] The new constitutive rows are genuine consequences of the encodings, not artefacts. I probed both.**
   - **cps R2~prohibit (drift 1).** `report_received` is `initial_free`, R1 obliges `investigate` at step 0, and that act opens the case and creates the subject. So services before the case opens cannot reach a subject. In the D3 encoding the query "subject and care at one step" is `open` after the prohibit and `reachable` before. The results' gloss "the prohibit leaks off-condition" is true but beside the point: the leak exists only before any bearer does.
   - **ectogenesis R4~prohibit.** The impossibility combines two things: the prohibit forbids the only carer, and strict compliance prunes traces where R5's `must provide_care` (female parent) meets the prohibit. The result is correct as encoded. It belongs under the strict-compliance caveat that the results apply only to coverture rows.

6. **[minor] Drift items 1-4 are honest and complete as far as I can check. Nothing was post-hoc in the engine or the predictions.**
   - **Timeline.**

     | time | event |
     | --- | --- |
     | 15:40 | preregistration cf29916 |
     | 15:41 | bundle files written |
     | 15:41:57-59 | encoder outputs |
     | 15:42 | merge commit |
     | 15:59:28 | engine commit and mutation record |
     | 15:59:46 | D1 run starts |
     | 16:19-16:27 | D3 run |
     | 16:36 | results commit |

     The predictions file is unchanged since cf29916.
   - **Drift 1** (goods_rows 34) is reproduced.
   - **Drift 2** follows from R2.1's own rule "no reading = unread". The preregistration contradicts itself here, and the results resolve it toward the rule.
   - **Drift 4.** The coverture-floor name, `source_text` and notes changes are, by my field-level diff of institutions.json 28b4528 → d503de7, the only changes besides R20's strand. None is read by any check.
   - **Drift 3** (iso) I did not rerun.
   - **R2.5 changes.** The `goods_note` card key and the build.py strip are R2.5 work, reported under the checklist rather than as drift. That is acceptable, since R2.5 asked for card notes written after the run.
   - **Encoder timing (for the faithfulness seat).** The two encoders finished about one minute after the bundle was written. That is consistent with 12 tool calls each, but the faithfulness seat should look at it.

## R2.1 conformance (item 1 of the brief)

| R2.1 item | conformance |
| --- | --- |
| `subject` key | required on goods and rejected elsewhere; an alternative may carry its own (`expand_contested` falls back to the primary's, rules_ablate.py:149) |
| loader checks | parse; `Ant -> Subj` with fluents uninterpreted, `antecedent` identical to rules_checks.antecedent; per-entry declared fluents and free variables are checked (finding 2) |
| four states | four queries in the specified order on the same `Grounded` system (rules_checks.py:249-274) |
| witness | the premise when the formula has implication shape, else `Subj` |
| `not_applicable` | read from the good's own subject, never from `is_*` |
| `persists` verdict | still run and reported in `flips`, never read by a state |
| measures | `goods_transition` gives "neither" for any pair with `not_applicable`; guaranteed and possible are computed separately, with separate lost/gained and families |
| readings | `constitutive` comes only from `possible`; `guarantee-carrying` only from `guaranteed` |
| contested alternatives | by name, never in primary loads, flips or summaries |
| goods k-disagreement | on the full state pair, including counted-vs-uncounted |

I found no path by which a state is misassigned in this dataset. Revision 1's two named routes are closed:
- the subject check is tied to the good's own subject, not to `is_*` fluents;
- the step-0 grace no longer counts as the good holding, because step 0 is not a witness step for a `succ`-guarded premise.

## Verdict: supported

The engine implements R2.1 as written. Every R2.2 mutation the builder named, and the three that survived revision 1, are killed in my scratch rerun. Every headline number reproduces from an independent run, byte-identical to the builder's:
- the three n/a rows (lost 0);
- kibbutz R4 possible gained 1 and R3 lost 0;
- ectogenesis R4~prohibit possible lost 3;
- `chosen_mutual_care` absent in nine entries, with only R6 gaining;
- the route comparison (N 3 = 3, G guaranteed 5 vs 4, G possible 0 = 0, possible gained 1 = 1);
- E1r2 (0 non-goods differences and 0 guaranteed-transition differences across 712 rows).

The drift is recorded honestly, and nothing in the predictions or engine was changed after the run.

The findings are minor:
- three surviving mutants show that "never stable when undecided" is tested only at the subject query (finding 1);
- the loader has two rough edges (finding 2);
- one latent multi-bearer limit is not exercised by this dataset (finding 3).

None changes a reported number, since the run has no undecided query. I recommend adding the three fixtures from finding 1 before this engine is used on entries where z3 can time out. The constitutive rows outside coverture (ectogenesis R4~prohibit, cps R2~prohibit) are real consequences of the encodings under strict compliance. They should carry the same strict-compliance caveat as the coverture rows.

# Correctness review: priority slice 2, revision 3 (philosophy-engine 42df8af; ENGINE_PIN 7859726; dataset ea65a7f, b24cb36, e1d051a) — 2026-11-06

Fresh agent, correctness seat (ADR 0014). I did not build, encode, gloss or coordinate this slice or any earlier revision of it, and I wrote none of its earlier reviews. Both repositories were read-only for me; this file is my only write. Second encoder: agent, not someone living under the institution (ADR 0012).

Subject: philosophy-engine 42df8af (R3.1, R3.2), with 0472661, 605cff4 and 7859726 as data-only syncs (`git diff 42df8af 7859726 -- philengine` is empty, and `git diff 0472661 42df8af -- data` is empty). computational-liberation ea65a7f (D4), b24cb36 (D5), 1c512b9 (encoders) and e1d051a (D6, experiment, results), checked against plans/priority-slice2.md "Revision 3" as committed at 8e512f3 (`git diff 8e512f3 HEAD -- plans/priority-slice2.md` is empty). Both trees were clean. computational-liberation's data/institutions/*.json is byte-identical to the engine's at the pin.

What I ran (outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/council-r3/`, not kept):

- **Engine copies.** `git archive 7859726` into scratch (`eng/`), and `git archive c53d132` (`eng_c53/`) for the fix-pass baseline. Both ran with `PYTHONPATH` and `PYTHONDONTWRITEBYTECODE`, so neither repository was imported or written.
- **Five fresh ablation runs**, each `rules ablate --k 6,8 --workers 4 --json --summary --readings` on all 27 entries:
  - FIX: fix-pass data c53d132 on c53d132 code;
  - D4: data 0472661 on 42df8af code;
  - D5: data 605cff4;
  - D6: the committed data;
  - blind-1 and blind-2: D6's properties with the six goods replaced by each blind encoder's own `formal`, `subject` and `entries`.
  
  I compared the runs leaf by leaf with my own scripts (`cmp.py`, `an_d6.py`, `an_exp.py`, `prim.py`).
- **Probes.** On coverture-household and coverture-floor, each minus {}, {R6}, {R3}, {R5, R6}, {R3, R6}, {R2, R3, R6} and {R2, R3, R5, R6}: `without_rule`, then `run_all` goods states at k = 6 and 8. I evaluated the D6 formula and revision 2's formula side by side.
- **z3 equivalence.** My own translator (`equiv.py`): first-order, sorts agent and step, every fluent including `succ` an uninterpreted predicate. It does not reuse scripts/goods_equiv.py. It covers formal and subject, dataset vs blind-1 vs blind-2, for all six goods, plus the dataset's `provided_for` alternative.
- **Mutations.** Each mutant in its own scratch copy, run against tests/test_rules_ablate_goods.py, test_rules_ablate.py, test_rules_obliged.py and test_rules_meta.py with `-m "not slow"` (201 tests):
  - an unmutated control (201 passed);
  - my own implementations of MO1 to MO6 and MP1 to MP3;
  - ten mutants of my own (OWN1 to OWN10).
- **computational-liberation** `pytest -q -p no:cacheprovider`: 38 passed (including the O5 pins).

## Reproduction

| claim | reproduced |
| --- | --- |
| **E2r3**: D5 identical to D4 in every field | yes. 0 leaf differences in the ablation JSON, 0 in the summary; readings tables byte-identical |
| **E1r3**: D4 identical to the fix-pass run apart from the new primary fields | yes. FIX (c53d132 code and data) vs D4: 0 differences outside keys naming `primary`, `top_goods_rules`, `top_load_goods_primary` or `hard_cases_primary`. Both have 356 rows, `goods_rows` 34, `contested_readings` 0 |
| R3.1 table: every primary cell, summary lists | yes (D6 run, k = 6 and 8). R2 lost {cared_for, provided_for} carrying (guaranteed) in eight coverture-family entries; coverture-floor R2 {cared_for}; R3 unread; airline-flight R2 {cared_for}; ectogenesis R4~prohibit {child_with_family, known_carer} and gestational-surrogacy R4~prohibit {known_carer} carrying (possible); cps R2~prohibit carrying (possible), unranked; companion R1~prohibit gained cared_for; kibbutz R4 gained child_with_family |
| 13 rows, primary column | yes: 10 read; R2 carrying (guaranteed); R3 unread; R4, R7 tying; R6 tying (strand rival, no row) |
| **D6 headline**: `chosen_mutual_care` absent in nine coverture-family entries; no single deletion moves it | yes. absent > absent in every row of all nine entries at k = 6 and 8; no alternative differs; 0 movers |
| D5 → D6: 270 leaf differences in the nine R6 rows plus 42 in cps (drift 1) | yes: 312 = 9 × 30 (R6) + 3 × 14 (cps R8, R11, R11~prohibit); summary identical |
| `goods_rows` 34 > 25; 356 rows; 0 uncounted, 0 inconsistent_after, 0 k-disagreements | yes |
| probes: {R5, R6} absent (revision-2 formula stable); {R3, R6} absent (rev. 2 fragile); {R2, R3, R6} fragile; {R2, R3, R5, R6} fragile; {R6} absent (rev. 2 fragile); {R3} absent | yes, identically in coverture-household and coverture-floor, k = 6 and 8 |
| z3: blind-1 ~ blind-2 equivalent on 1 of 6 (`mutual_household_care`); **0 of 12** blind formulas equivalent to the dataset's; the dataset's `provided_for` alternative equivalent to neither | yes, every cell of the formal/subject table |
| experiment: 41 (entry, good) base pairs differ; 34 contested (row, k, column) cells; **3 ranked rows** at k = 6 (airline-flight R2 guaranteed; ectogenesis R4~prohibit primary; gestational-surrogacy R4~prohibit possible and primary) | yes. `load_freedom_up` and ranked status are identical across D6, blind-1 and blind-2 in every row, so the cross-run reading comparison is the engine's own |
| 13 rows, blind columns: coverture R2 carrying (possible) in both; R3 carrying (possible) in both; ectogenesis R4~prohibit blind-1 unread, blind-2 carrying (possible) | yes; every other row the same in all three |
| combined form refused (drift 4) | yes. Loading r3/experiment-properties.yaml as one properties file raises the R2.1 subject error in paternity-quota and transferable-leave (blind-2 `known_carer` subject names `is_subject`) |

Every headline number of the D6 run, the probes, E1r3, E2r3 and the experiment reproduces from my own runs. I did not rerun check-all, diff, gate, drop-one, iso or the full engine suite.

## Mutations

| mutant | what it does | tests failing |
| --- | --- | --- |
| MO1 | `may` obliges | 10 (O1 engine x2, O2 x2, O4a, O4c, O3 action fixture x4) |
| MO2 | a disability (must_not, or_else null) cancels the obligation | 7 |
| MO3 | condition ignored | 14 |
| MO4 | state aims dropped (action musts only) | 10 |
| MO5 | the free condition variable is fixed to the first agent | 8 |
| MO6 | MO1 in both engine and reference | 8, none of them the differential: the O1 hand pins catch it |
| OWN1 | `must_not` obliges | 8 |
| OWN2 | only sanctioned musts oblige | 14 |
| OWN3 | instance arguments ignored (any must on the aim obliges every tuple) | 5 (O5 tiny; O3 household x4) |
| OWN4 | condition read at t+1 | 15 |
| OWN5 | condition read at t-1 | 15 |
| OWN6 | obliged drops sanctioned musts under `compliance="sanctioned"` | 1 (O2[R9]) |
| OWN7 | engine **and** reference: only unsanctioned musts oblige | 9 (O1 reference hand pins x2, O2 or_else, O4b, ...) |
| MP1 | the primary column reads the other measure | 5 |
| MP2 | pooling: primary lost if either measure is lost | 5 |
| MP3 | an alternative reads its own measure (default possible) | 2 |
| OWN8 | carrying suffix from the first lost family only | 1 (P1b) |
| OWN9 | `top_goods_rules` ranked by possible lost | 1 (P5) |
| OWN10 | `contested_readings` ignores the primary column | 1 (P2b) |

All are killed. For MO1 to MO6 and MP1 to MP3, my independent mutants fail exactly the counts in the 42df8af record (10, 7, 14, 10, 8, 8; 5, 5, 2).

## `obliged` against R3.2 (item 1)

| R3.2 clause | implementation |
| --- | --- |
| every `must`, sanctioned or not; `or_else` plays no part | `Grounded.obliged` filters on `ri.rule.deontic == "must"` only (philengine/rules_lower.py:686-697); the reference's `Reference.obligation` does likewise (philengine/rules_reference.py:338-345); OWN2 and OWN7 killed |
| `may` and `must_not` never oblige; a disability does not cancel | no `may`/`must_not` term in either function; MO1, MO2, OWN1 killed |
| independent of `default_capacity` and compliance | neither function reads either flag; O4c, O2; OWN6 killed (by one test only) |
| action and state aims | instance check against `action_instances` or `fluent_tuples` (rules_lower.py:690-693); rule instances carry both kinds; MO4 killed |
| free condition variables existential | via the shared `cond_at` (rules_lower.py:916-926); MO5 killed |
| condition at t, defined at k | `cond_at(ri, t)`; derived Bools are defined for t in 0..k (rules_lower.py:944-946); OWN4 and OWN5 killed |
| non-instance false | yes; the O1 pointwise test pins it |
| loader: AIM declared action or non-derived fluent, arity; cycle through a must condition; error in a property or rule condition; "never obliged" warning | rules_lower.py:501-518, 413-431, 941-943; O6 |
| reference independent of the lowering | `obligation` reads `rule_insts + state_rules` and `cond_holds`; it shares no code with `Grounded.obliged` apart from the parser; MO6 and OWN7 caught by the hand pins |

I found no deviation from R3.2 in the code.

## Primary column (item 2)

- `primary_transition` reads the R2.1 transition under `primary_measure_of`, which is always the primary property's measure (rules_ablate.py:149-157).
- Families: lost if a member is lost and none is gained (:615-630).
- `primary_reading` gives tying, carrying (suffix from the set of lost families' measures), hard case (primary) or unread (:218-226).
- `summarize` adds `primary_carrying`, `hard_cases_primary`, `top_goods_rules` and `top_load_goods_primary`, ranked on `load_goods_primary`; `top_rules` is unchanged (:713-738).
- `contested_readings` iterates over all three columns (:737).
- `scoreboard_stats.goods_rows` reads only the two measures (:758), as R3.1 says.
- Loader: required on goods; reason one line, at most 200 characters; rejected on non-goods and on alternatives; family-shared (schemas_rules.py:214-235, 320-333, 477-485).

This conforms to R3.1.

## Findings

1. **[major, reporting] Two preregistered O5 dataset pins fail as written; they were rewritten after being run, and the results say neither.**
   - R3.2 O5 (plans/priority-slice2.md:551-552) pins two formulas:
     - `(forall ((h agent) (w agent)) (<=> (married h w t) (and (care_obliged h w t) (care_obliged w h t))))` holds_to_k in coverture-household;
     - `(forall ((h agent) (w agent)) (not (care_obliged w h t)))` holds_to_k without R3.
   - Both are **violated**. Over all ordered pairs, `married(wife, husband)` is false while both duties hold, and once R3 is deleted R2 still obliges the husband (`care_obliged(husband, wife)`).
   - The builder wrote corrected pins and pinned the as-typed forms at `violated` (computational-liberation tests/test_dataset_claims.py:246-257, 279-288; philosophy-engine tests/test_rules_obliged.py:356-360, 416-421). The engine is right; the preregistration's quantifiers were wrong.
   - However, the test comments say "drift, plans/priority-slice2-results.md 'Revision 3'", and the drift list there (plans/priority-slice2-results.md:562-571) has no such item. RF3.3 is reported as "no ... dataset pin failure (O5)" (:529) without saying that the pins as preregistered fail.
   - Rewriting a failing preregistered check after the run is the kind of change the drift list exists for.
   - Fix: add a drift item quoting both as-typed pins, their verdicts and the rewritten forms, and amend the RF3.3 row to "fired as typed (preregistration error, engine correct); held as rewritten".
   - This changes no number.

2. **[minor] The "conflict check reports it" premise of R3.2 is false for conditions with a free variable, and the promised record is missing.**
   - R3.2 (plans/priority-slice2.md:498) says that a must plus a disability on one instance "is a deontic conflict, which the existing conflict check reports".
   - `check_deontic_conflict` (philosophy-engine philengine/rules_checks.py:121-137) lowers each condition with its free variables unbound. An unbound agent name lowers a fluent to constant false, so such a pair is never reported. The O1 fixture's R4/R6 is an example.
   - The 42df8af message and tests/test_rules_obliged.py:181-183 say this limit is "recorded in the revision-3 results"; it is not there.
   - No dataset entry has a must and a must_not on one aim with a free-variable condition (my scan of all rules: every free-variable condition is on a may or must_not, apart from cps R6 `contact_mother` and lease R5 `rent_paid`, which no must_not names). So nothing is affected.
   - Fix: record it as a known limit in the results.

3. **[minor] Unrecorded drift on the `care_obliged` entry set.**
   - R3.2 lists 24 entries, including footbinding and footbinding-no-pledge, and predicts the fluent constant false in "footbinding and the paternity pair" (plans/priority-slice2.md:517-526).
   - D5 declares it in 22 entries: the footbinding pair declares no `provides_care`. It is constant false in **cps** and the paternity pair (cps has no must on `provides_care`).
   - Only the b24cb36 commit message says so; the results' drift list does not. Since cps `cared_for`/`known_carer` never read `care_obliged` in the dataset, nothing moves. It should be in the drift list.

4. **[minor] The split-run inputs are not committed and cannot be rebuilt from the reproduction line alone.**
   - r3/experiment-properties.yaml is the combined form, which the engine refuses (drift 4).
   - A per-encoder properties file with `encoders: [blind-N]` is refused by the loader ("kind goods requires encoders naming at least two encoders"). I used `[blind-N, blind-other]` with `contested: []`. On that reconstruction every reported number reproduced, so the coordinator's choice evidently did not matter, but the reproduction line (plans/priority-slice2-results.md:576) should say how it was done. Better still, commit the two scratch property files beside experiment-properties.yaml.

5. **[minor, latent, pre-existing] The engine and the reference differ on several free condition variables.**
   - The engine's `cond_at` takes free-variable bindings from `_typed_domains`, which requires the free variables to be pairwise distinct (rules_lower.py:722-729, 916-926).
   - The reference's `cond_holds` takes the plain product (rules_reference.py:348-353).
   - With two or more free variables in one condition, `obliged` and `enabled` could disagree between the two. No rule in the dataset has more than one free condition variable, and the O3 fixtures have one, so the differential cannot see it. This is outside revision 3's scope; it is noted because `obliged` now inherits it.

6. **[minor] Some semantic clauses are pinned by a single test.**
   - OWN6 (obliged becoming compliance-dependent) is killed only by O2[R9].
   - OWN3 (instance arguments ignored) is killed only by the household fixture. The ward fixture has one tuple per aim, so it cannot distinguish OWN3.
   - Neither is a defect. A second carer or ward in the O1 fixture would harden OWN3, and an O1 pin under `compliance="sanctioned"` on the full PINS set with `or_else` set would harden OWN6 (it exists for PINS, but only O2's breach probe distinguishes the mutant).

7. **[resolved / sound] The split-form experiment (drift 4) is a sound substitute, and slightly more faithful than the combined form would have been.**
   - The combined form is refused, as reported.
   - In a combined run, an expanded alternative takes the primary's `entries`. Where the alternative is not applicable but the primary is, the encoder's view silently falls back to the primary's states (rules_ablate.py:598-608). Blind-2 would then have been read through blind-1's states or entries in places, notably `cared_for` in ectogenesis with `can_sanction` lowered as false.
   - The split runs evaluate each encoder only where its own formula and its own entries put it.
   - Freedom loads, ranked status and `inconsistent_after` are identical across the two runs and D6 in every row (checked). So contested readings computed across the runs are exactly the engine's `summarize` definition applied to two encoder views.
   - The one consequence, blind-2 `cared_for` not evaluated in ectogenesis, is recorded in drift 4. It moves no contested reading: ectogenesis R4~prohibit's primary difference comes from `known_carer`.

8. **[note] The drift list is otherwise honest.**
   - Drift 1: D5 → D6's 42 cps leaves are exactly the faithfulness batch, and the faithfulness batch moves no goods field.
   - Drifts 4 and 6 reproduce.
   - The predictions file is unchanged since 8e512f3. Engine code was committed (19:11) before the D4/D5 runs reported in b24cb36 (19:25), and before the D6 sync (19:48).
   - I found nothing changed after results that should have been preregistered, apart from finding 1's pin rewrite and finding 3's entry set.
   - The X1 "borderline" call (drift 5) is a faithfulness matter and I did not judge it.

## Verdict: supported

`obliged` implements R3.2 as written, in the engine and in an independent reference:
- every listed mutation is killed, with the same counts as the builder's record;
- my ten further mutants are killed too.

The primary column and the goods ranking follow R3.1. E1r3 and E2r3 hold on my own runs (0 differences). The D6 headline reproduces: absent in nine entries, no single mover, `goods_rows` 25, probes {R5, R6} absent, {R3, R6} absent and {R2, R3, R6} fragile, with the revision-2 control. So do the experiment's 3 ranked contested rows, 41 base differences, 0 of 12 blind formulas z3-equivalent to the dataset's, and 1 of 6 blind pairs equivalent.

The one major finding is a reporting gap, not a computation error. Two O5 pins failed as preregistered and were rewritten, and the results claim no pin failure and list no drift for it. It should be added before revision 3 is called a result. The rest are minor.

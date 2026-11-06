# Slice 2: goods properties, a second encoder, and the floor route

Status: preregistration, written 2026-11-06 before any goods formula, engine change, dataset change or run. Author decision 6 of 2026-11-06 (plans/priority.md "Decisions settled 2026-11-06"): slice 2 goes ahead, core plus the floor route. Parent plan: plans/priority.md (Design: `load_goods`, readings table; "Slices" item 2; "Candidate for slice 2: floor route vs title route"; decision 4 of 2026-11-04). Results go in plans/priority-slice2-results.md; nothing in this file is edited to match them. Drift is recorded there.

Second encoder: agent, not someone living under the institution (ADR 0012). Every slice-2 report, results file, card note and council review repeats that sentence.

## 1. Scope and pass test

**In scope.** (a) Five goods properties (section 3), each written as a formula by two fresh agents independently (section 2); (b) engine: `polarity: good`, `contested` and `encoders` required on `kind: goods`, a goods flip direction, `load_goods` lost/gained, the reading per row (section 6); (c) the readings table on the care+control cluster (coverture-household, police-crisis, cps) plus kibbutz-childrens-house and ectogenesis; (d) one counterfactual entry, `coverture-floor`, and the title-route vs floor-route comparison computed from single-rule ablation on the two end states (section 5).

**Out of scope.** Transfer graph and `rebundling` (slice 3), cut sets and sequencing (slice 4), the disagreement locator (slice 5; slice 2 only produces its inputs), any ABM run (layer 2 frozen), any forward claim (ADR 0004): `coverture-floor` is a counterfactual encoding, and every result is a statement about encodings (ADR 0011).

**Pass.** All of:
1. At least 3 goods properties are in `properties.yaml` with `encoders` naming both encoders, each formula written by an encoder who saw neither the other's formulas nor sections 4 and 5 of this file (transcript audit, section 2).
2. Every logically non-equivalent pair is kept: encoder 1's formula in `formal`, encoder 2's in `contested`; the merge log lists each pair and its equivalence result; nothing is merged away.
3. The readings table (section 4 format) is produced at k=6 and k=8 for coverture-household, police-crisis and cps, and for kibbutz-childrens-house and ectogenesis, per encoder, with zero silent errors (`uncounted`, `inconsistent_after` and k-disagreements listed, not dropped). Strand-tag agreement is tabulated.
4. `coverture-floor` is encoded as section 5 states, its layer-1 verdicts and ablation are compared with section 5's predictions, and the route comparison (section 5, quantities N, G, C, R) is computed and stated with the preregistered consequence.
5. Every report carries the ADR 0012 sentence above.

**Fail.** Fewer than 3 goods with two independent encodings; a contested alternative dropped or merged; a missing table row for any of the five entries; an error row not listed; a prediction edited after a run. A missed prediction is a result, not a failure (no threshold asserted, per the ASSUMED-numbers rule in plans/layer2-abm.md).

**Council.** Faithfulness seat (ADR 0014), fresh reviewer: (i) back-translation: reads each goods formula without the gloss, writes its own gloss, compares with section 3; (ii) judges whether a constitutive reading of an imposed, implicit duty (coverture R3, prediction 4.3) launders that duty as a good; (iii) checks `coverture-floor` R20 against "material floor" in docs/glossary.md and the Sequence in docs/theory.md; (iv) audits both encoder transcripts against the section 2 protocol. Card-only seat for `coverture-floor` once its card exists.

## 2. Independence protocol

1. **Two fresh agents.** Encoder 1 and encoder 2 are separate agents started with no prior context, run in parallel, never a builder, coordinator or reviewer of this slice, and never shown slice-2 results. Encoder 1's formula is the primary (`formal`); fixed now, before either runs.
2. **Input bundle, identical for both**, assembled by the coordinator into a scratch directory outside both repositories and hashed (hash recorded in the results file):
   - section 3 of this file verbatim (ids, glosses, entries), and nothing else from this file;
   - the property-formula conventions: the "Conventions" bullet on property `formal` in data/institutions/README.md (state formula, `t` free, fluent applications carry `t` last, sorts `agent` and `step`, `succ(t, t2)` for t+1), three freedom properties with their formulas as style examples (`cannot_contract`, `subject_cannot_exit_persists`, `care_duty_on_women`, the last for the one-step grace of action obligations), and the goods conventions: check kind `persists`; a `persists` that is vacuous (the formula never holds in any compliant trace) reads as "the good is absent"; write the good so that its holding is good for the named party;
   - per entry named in section 3: roles, fluents (name, arity, gloss, `derived` definition), actions with effects, `initial`, `initial_free`. **Not** the rules, cards, expected verdicts, ablation outputs, or sections 4 to 7. For `coverture-floor` the vocabulary is section 5's (the entry does not exist yet).
   ASSUMED: withholding the rules costs some accuracy (an encoder cannot see which fluents a rule forces) and is chosen so that no formula can be aimed at a rule the predictions name.
3. **Output.** Each writes one file, `<scratch>/slice2/encoder-<n>/goods.yaml`: per good, `formal`, a one-line back-gloss, the entries it is written for, and `not_expressible: {entry: reason}` where the vocabulary cannot carry the good. No new fluents. No engine command except the coordinator-provided syntax validator (`philengine.rules_lower.validate_property` on the bundle's vocabulary); no check, ablation or verdict.
4. **No contact.** Neither encoder reads the other's directory, this file beyond the bundle, the engine's tests or the results. Compliance is by instruction and is audited: the coordinator lists every file read and command run in each transcript; any breach marks that encoder's formulas for the affected good as not independent (the good then does not count toward pass item 1).
5. **Merge (coordinator, not an encoder).** Per good and per applicable entry: z3 validity of `A <-> B` with all fluents uninterpreted over the entry's vocabulary. Valid in every applicable entry: one `formal`, `contested: []`, merge log "equivalent". Otherwise `contested: [{encoder: encoder-2, formal: B, note}]`, including when the two read the same at k=6 and 8 ("same effect" is reported, not merged). A `not_expressible` from one encoder goes into the note and marks that entry's reading contested. A syntax error goes back to the same encoder once, fix limited to syntax, logged.
6. **Disagreement is output.** A `contested` alternative is evaluated in every run beside the primary and reported in its own columns; loads are never pooled, averaged or chosen between (docs/intent.md; ADR 0012). Alternatives are the input slice 5's locator takes.

## 3. Goods list (glosses only; formulas are the encoders' job)

Each good is `kind: goods`, `polarity: good`, `check: persists`, its own `family`. "Entries" is where encoders write for and section 4 predicts; ablation also reads the property wherever its fluents are declared, and those rows are information only. The comparison entries are coverture-household-us, mwpa-earnings and coverture-floor (section 5).

| id | good, for whom | entries | why a good (superadditive product), not a freedom |
| --- | --- | --- | --- |
| `cared_for` | The subject of the institution (the wife, the person in crisis, the child) receives care, and once care has begun it does not lapse while the relation that brings the care lasts. | coverture-household, police-crisis, cps, kibbutz-childrens-house, ectogenesis; comparison entries | The care strand is tagged superadditive in every one of these (coverture R2, police R2, cps R2/R4, kibbutz R3, ectogenesis R4): care arrives as part of the bundle that also holds control. Its absence bars the subject from nothing; it is what unbundling can lose ("losing care is the real danger of unbundling", docs/glossary.md "material floor"). |
| `mutual_household_care` | Two adults in one household each care for the other: both spouses. | coverture-household; comparison entries | The glossary's own superadditive example, "being known by one person who is also housemate and co-parent"; it exists only when both care strands (coverture R2 and R3) hold together. It is a product, not a power either spouse holds. |
| `known_carer` | The dependent is cared for by the same person over time, so the carer knows them ("being known", docs/intent.md flourishing): the subject. | coverture-household, cps, kibbutz-childrens-house, ectogenesis; comparison entries | Continuity is what a rota, a caseworker or a single carer produces or fails to produce; it is a property of how care is bundled with a role, not something the subject is permitted or barred from doing. |
| `child_with_family` | The child lives with, or is cared for by, its own parents or household rather than apart from them (co-parenting intact): the child. | cps, kibbutz-childrens-house, ectogenesis | Priority.md's named example of a good ("co-parenting intact"); the family-preservation strand (cps R4) and the children's house (kibbutz R4) are exactly where it is kept or removed. Having it is good for the child; it is not exit or standing. |
| `provided_for` | The subject's subsistence is secured, whether by a carer's maintenance or by means in her own right: the wife. | coverture-household; comparison entries | The capability reading of plans/disability.md item 2: support counts as enabling. Coverture R2 (necessaries, superadditive) produces it; `financial_dependence` asks the opposite, independence-shaped question (are the means hers), so the two can disagree, which is the point. |

Rejected as goods: voice and standing (`has_standing`, counsel) are freedoms in docs/intent.md's list; pleasure and meaning have no vocabulary in any entry.

## 4. Preregistered readings

**Definitions (engine, section 6).** Per ranked row: `up` = load_freedom_up; `lost` = goods families moving to a worse state (stable > fragile > absent; stable = `persists` non-vacuous, fragile = `fails`, absent = `persists` vacuous); `gained` = the reverse, shown, never counted in `load_goods`. Reading: **tying** if up > 0 and lost = 0; **constitutive** if lost > 0 and up = 0; **hard case** if both; unread if neither. "High" in the priority.md table means > 0 (ASSUMED; no threshold). A row with only freedom_down is a protection, not a reading. Strand-tag agreement: tying tag with tying reading, superadditive with constitutive = agree; any other pairing with a reading = mismatch; rival tag = "no row" (the table has no rival reading); tag with no reading = unread.

**Why the predictions look as they do.** Under strict compliance a goods flip needs a rule whose deletion lets the good lapse. Must-be care duties with a breaker (coverture R2/R3, police R2, kibbutz R3) do; a deleted `may` is deregulated and an off-condition prohibit leaks (slice-1 conventions), so permission-borne care (cps R2, ectogenesis R4) reads only in unranked rows, except where the prohibit binds everywhere or the action stays regulated (ectogenesis R4 `~prohibit`).

**4.1 Base states (unablated) and rules carrying goods**, primary formula, k=6 and 8 alike:

| entry | good | base state | lost > 0 (ranked) | gained > 0 | contested predicted |
| --- | --- | --- | --- | --- | --- |
| coverture-household | cared_for | stable | R2 | none | no |
| coverture-household | mutual_household_care | stable | R2, R3 | none | no |
| coverture-household | known_carer | stable | R2 | none | no |
| coverture-household | provided_for | stable | R2 | none | yes (own means included or not) |
| police-crisis | cared_for | stable | R2 | none | yes: an encoder that guards on `is_subject` rather than the response makes the base fragile (the subject can `leave` before custody) and R2 reads 0 |
| cps | cared_for | stable | none (R2 deregulated; R2~prohibit offcondition_free, lost 1, unranked) | none | no |
| cps | known_carer | stable | none | none | no |
| cps | child_with_family | fragile (removal reachable) | none (R4 only if a formula reads `in_home_considered`) | none | yes, or `not_expressible` (no parent-care fluent) |
| kibbutz-childrens-house | cared_for | stable under a carer-guarded formula, fragile under a child-level one (`release` is unregulated and drops care) | R3 (carer-guarded only) | none | yes |
| kibbutz-childrens-house | known_carer | stable | R3, R2 (without R2 a male member can follow the released metapelet) | none | yes |
| kibbutz-childrens-house | child_with_family | absent (R4 bars `sleep_home`) | none | R4 | no |
| ectogenesis | cared_for, known_carer, child_with_family | stable (care never lapses once begun) | R4~prohibit (care becomes impossible: non-female parents barred, female ones in conflict with R5) | none | yes (existential vs universal shape) |

R5 in ectogenesis reads lost 0 (R4 still permits care). Confidence: high on coverture and police R2; medium on kibbutz and ectogenesis; low on cps child_with_family.

**4.2 Readings table and strand agreement (primary formula):**

| entry | rule (tag) | up | lost | reading | agreement |
| --- | --- | --- | --- | --- | --- |
| coverture-household | R2 (superadditive) | 0 | 4 | constitutive | agree |
| coverture-household | R3 (superadditive, implicit) | 0 | 1 | constitutive | agree |
| coverture-household | R4 (tying) | 1 | 0 | tying | agree |
| coverture-household | R6 (rival) | 1 | 0 | tying | no row |
| coverture-household | R7 (tying) | 1 | 0 | tying | agree |
| police-crisis | R2 (superadditive) | 0 | 1 | constitutive | agree |
| police-crisis | R4 (rival) | 1 | 0 | tying | no row |
| cps | R10 (rival) | 1 | 0 | tying | no row |
| kibbutz-childrens-house | R2 (tying, implicit) | 1 | 1 | hard case | mismatch |
| kibbutz-childrens-house | R3 (superadditive) | 0 | 2 | constitutive | agree |
| kibbutz-childrens-house | R4 (rival) | 1 | 0 (gained 1) | tying | no row |
| ectogenesis | R4~prohibit (superadditive) | 0 | 3 | constitutive | agree |
| ectogenesis | R5 (tying, implicit) | 1 | 0 | tying | agree |

Every other ranked rule in these entries: unread. Totals: 13 read rows, 8 agree, 1 mismatch (kibbutz R2), 4 rival no-row. Expected headline: in the care+control cluster the care strands read constitutive and the exit and standing bars read tying ("keep the care, drop the control"), except cps, whose care strand is a permission the instrument cannot read in a ranked row.

**4.3 Encoder agreement.** Predicted: at least 2 of the 5 goods have logically non-equivalent formulas; at least one rule's reading differs by encoder (most likely kibbutz R3 or R2, or police R2); coverture's readings agree across encoders. Zero disagreement is reported as zero; it is not evidence that goods can be encoded without the encoder's picture of the good (both encoders are agents of one model; priority.md open question), only that this pair converged.

**4.4 Unchanged rows.** Adding the goods changes no freedom column in any row of any entry (families are per kind). k-disagreements 0, `inconsistent_after` 0, `uncounted` 0.

**Falsifiers** (each reported, none fixed in place):
- F1: a tying-tagged rule other than kibbutz R2 reads constitutive or hard case.
- F2: a ranked row of a `may` rule (permission removed, or a ranked prohibit) in the five entries carries lost > 0, other than ectogenesis R4~prohibit: the claim that goods load sits in must-be duties fails.
- F3: coverture R3 reads lost 0 on `mutual_household_care` under both encoders.
- F4: any ranked cps row carries lost > 0.
- F5: police R4 reads hard case (an encoder read the subject's own exit as loss of care).
- F6: a freedom column changes in any row when the goods are added (engine defect, not a result).

The coverture R3 prediction is the slice's faithfulness item: the instrument would advise "redesign, do not cut" for the wife's implicit, sanctioned care duty because a good rests on it. That is what the readings table says the encoding implies, and the council's question (ii) is whether the good was written in a way that launders the duty.

## 5. The floor route: `coverture-floor`

**Base: `coverture-household-us`.** Reasons: (1) the title route to compare against is the MWPA chain, whose base it has been since the 2026-11-05 split, so both routes start from one rule set; (2) its R6 is the US reading (no exit at her own will), the exit bar the chain carries; (3) the English `coverture-household` is a gate (b) cluster member with precommitted iso claims, and the floor is a counterfactual on the US frame, not a reading of Blackstone. Rule for rule the two bases are identical, so the coverture-household predictions in section 4 carry over. Rejected: basing it on `mwpa-creditor-exemption`, which would make the two end states differ by route rules only, but would put the floor on a debtor-relief statute and make `creditor_shield` reachable (R1 stands, the husband manages what he conveys); recorded as a later variant, not built.

**Encoding** (counterfactual; notes say so; provenance `unverified`, source "plans/priority-slice2.md §5"):
- Root change, on `coverture-household` and inherited by the whole coverture family: action `draw_subsistence(w)`, no effects, not a default capacity; derived fluent `has_own_income(w) := (enabled draw_subsistence w)`, gloss "w has an income in her own right from outside the marriage". No rule names the action in any existing entry, so the fluent is false there, as `hold_property` and `keep_earnings` already are under coverture.
- `coverture-floor` extends `coverture-household-us`; `initial_free: [female, acquired_property, earns]` and the `arg_roles` of `mwpa-creditor-exemption`, so both end states quantify over the same exogenous worlds. One rule added: **R20** `wife may draw_subsistence w when true`, or_else null, implicit false, strand `superadditive` (ASSUMED placeholder: a floor is not a strand of the bundle and the tag vocabulary has no slot for it; recorded for the strand-tag redesign in docs/plan.md). No R13, no R14, R1 kept: no property grant.
- Deviation from the candidate wording (`must provide_subsistence w when (is_subject w)`), stated before any run: (a) the dataset encodes a resource as a derived power over the holder's action (R13, R14); a state duty with no matching power would leave every financial property blind, and an action `must` either fills the one action slot each step (the ADR 0009 problem that made coverture R2/R3 must-be) or, once deleted, leaves an unregulated action that fires freely; so the floor is the wife's entitlement, the correlative of the state's duty (ASSUMED: the engine has no duty/claim pairing); (b) condition `true`, not `(is_subject w)`: `is_subject` is set only by `marry`, so the candidate's floor was an allowance for wives, while the glossary's floor is "regardless of any relationship". For subjects the two read the same at layer 1.

**New freedom properties** (`kind: freedom`, `polarity: unfreedom`, family `financial_dependence`, `check: invariant`):
- `financial_dependence_means`: every subject lacks any means of her own, counting income as well as property and earnings: `(forall ((w agent)) (=> (is_subject w t) (and (not (controls_own_property w t)) (not (owns_earnings w t)) (not (has_own_income w t)))))`.
- `financial_dependence_margin`: the same for every subject who has neither acquired property nor earns: `(forall ((w agent)) (=> (and (is_subject w t) (not (acquired_property w t)) (not (earns w t))) (and (not (controls_own_property w t)) (not (owns_earnings w t)) (not (has_own_income w t)))))`. Flagged `by_construction` in advance for coverture-floor: R13 and R14 are conditioned on acquired property and on earning, R20 on nothing, so the margin verdicts restate the conditions.

**Layer-1 predictions** (`check-all --no-cache`, k=6, strict):
1. Zero verdict changes in the 26 existing entries after the root change; `diff --baseline`: 0 changed, 0 removed; added rows only for coverture-floor. Gate PASS, (b) unchanged (no rule changes). Layer 2 not rerun (frozen); ASSUMED unaffected, since a nameless non-capacity action is never an ABM candidate.
2. coverture-floor: `financial_dependence` **holds_to_k** and `financial_dependence_unpropertied` **holds_to_k**. This sharpens the candidate's "violated": both formulas read only property and earnings, so they cannot see a floor. That they are blind to it is the author's point about the instrument: as written, material independence means title.
3. coverture-floor: `financial_dependence_means` **violated**, `financial_dependence_margin` **violated** (by construction).
4. In the other eight coverture-family entries, `financial_dependence_means` has exactly the verdict of `financial_dependence`, and `financial_dependence_margin` is holds_to_k in all eight (no title rule reaches a wife with neither property nor wages).
5. coverture-floor: `double_burden` **unreachable_open**. This sharpens the candidate's "still reachable": the formula needs `owns_earnings`, which only R14 grants. The candidate's substance, that the care rule R3 is untouched, is tested instead by R3 reading the same in both end states (below).
6. coverture-floor: `creditor_shield` **unreachable_open**, by construction (no creditor role; `transferred` and `can_attach` undeclared, ASSUMED lowered as false, as in coverture-household today). On Capture the title route wins by construction: deleting R1 is what closes `creditor_shield` in mwpa-property. Reported, not scored.
7. Unchanged from the US base: subject_cannot_exit and dependent_cannot_exit reachable, no_standing reachable, cannot_contract holds_to_k, care_and_sanction_same_role holds_to_k, care_assigned_by_sex violated.

**Ablation predictions** (k=6 and 8 agree):
- Tops {R4, R6, R7} at load_freedom_up 1, families no_standing, cannot_exit, cannot_contract (same as mwpa-earnings after revision 4).
- R20 deleted: deregulated, not ranked; freedom_down 1 (family financial_dependence, via means and margin), lost 0. R20~prohibit: ranked (its condition is `true`), freedom_down 1, up 0, lost 0: a protection, unread.
- R2: lost 3 (cared_for, mutual_household_care, known_carer), **not** provided_for, because the floor still provides when the husband may neglect. In mwpa-earnings R2 loses 4: a wife with neither property nor wages has only R2. R3: lost 1 in both. R1 and R5: unranked in both (a deregulated `may`, an offcondition_free prohibit).
- Confound check (the title end state also carries R10 to R12 and the chain's `initial_free`): R2 to R7 rows (up, lost, families) are identical in coverture-household-us and mwpa-creditor-exemption. If not, the comparison is reported with the confound named and a clean title variant (US base minus R1 plus R13, R14) is the follow-up, not built here.

**The comparison.** End states T = `mwpa-earnings` (title route: R1 deleted, R13 and R14 added) and F = `coverture-floor` (floor route: R20 added). B(E) = rules of coverture-household-us still in E (T: R2 to R7; F: R1 to R7). From the ablation output, per encoder where goods enter, at k=6 and at k=8:
- **N(E)**, primary: |{r in B(E), ranked deleted row, load_freedom_up(r) > 0}|, the bonds left behind, with their families.
- **G(E)**, secondary: sum over r in B(E) of lost(r), the goods that still rest on a base strand.
- **C(E)**, reported: verdict of `financial_dependence_margin` (by construction).
- **R(E)**, reported: route rules with any financial_dependence-family flip, ranked or not (T: R13, R14; F: R20; by construction).
Winner: lower N; on a tie, lower G; C and R never decide.

Predicted: N(T) = N(F) = 3 ({R4, R6, R7}, same families): **a tie on bonds left**. G(T) = 5, G(F) = 4: **the floor route leaves fewer goods resting on the husband's duty**. C: T holds_to_k, F violated; R: 2 vs 1. Statement to expect: both routes leave the same formal bonds; the floor makes the wife's provision stop depending on R2. That fits T1's reason for a floor (survival not depending on being chosen) and says nothing about floor *first*, which is an ordering claim. Two limits are stated in advance. First, the title route's one cut, R1, is invisible to N: R1 is a `may` (unranked) and no freedom formula reads the husband's management. Second, the per-state top load along each route is 1 everywhere (US, creditor-exemption, property, earnings; floor), so path flatness separates nothing.

What changes the plan:
- N(F) > N(T): the floor leaves more bonds. T1 gets a layer-1 counter-instance in docs/claims.md, and slice 4 takes title-first as the default ordering on the coverture chain.
- N(F) < N(T): not predicted. First audit for a transfer effect of R20 on a base rule (slice 3's object), then report it as layer-1 support for the floor in this pair, and coverture-floor becomes a preregistered slice-3 entry.
- Tie, and R2 still carries `provided_for` in F under both encoders: the goods as written do not see own-income provision. The comparison is uninformative at layer 1 and T1's layer-5 test moves to another case (plans/disability.md item 4).
- Tie as predicted: T1 stays a hypothesis. Slice 4 receives two preregistered must-go-together candidates, {R2, R20} for `provided_for` in F and {R4, R6, R7} in both end states.

**What slice 4 would add, and is not used here.** Set deletion: the floor's effect on `provided_for` is redundancy, which single-rule ablation shows only as "neither R2 nor R20 alone carries it"; {R2, R20} together would. Must-go-together sets, ordering by max-load flatness (floor-first vs title-first), and out-transfer (slice 3; T1's "floor strands have the highest out-transfer"). Slice 2's comparison is two entries' single-rule ablations side by side, nothing more.

## 6. Engine work (design only; philosophy-engine)

Built on slice 1 revision 5 (plans/priority.md: `UNFREEDOM` deleted, `flip_direction` reads `kind`, `Property.polarity: Literal["unfreedom"] | None`, freedom requires `unfreedom`). Names below that revision 5 has not yet fixed are ASSUMED and follow whatever it lands.

- **`schemas_rules.py`**: `polarity: Literal["unfreedom", "good"] | None`; new `ContestedAlternative(encoder: str, formal: str, note: str = "")`; `Property.contested: list[ContestedAlternative] | None = None`; `Property.encoders: list[str] = []`. Validator: `kind == "goods"` requires `polarity == "good"`, `contested is not None` (an empty list means the encoders' formulas were equivalent), `len(set(encoders)) >= 2`, `check == "persists"`; `polarity == "good"` on any other kind is a load error. Each alternative's `formal` parses like `formal`.
- **`rules_ablate.py`**: one direction table read from `polarity`: present = {reachable, holds_to_k, persists}, absent = {open, violated, fails}; for `unfreedom`, present to absent is freedom_up (revision 5). For `good`, `goods_state(res)` = stable (persists, not vacuous) | fragile (fails) | absent (persists, vacuous) | None (any other verdict, error or z3 unknown: uncounted). A move down that order is `lost`, up is `gained`. `load_goods` counts families lost (the priority.md column, now signed); new `load_goods_gained`, `goods_families_lost`, `goods_families_gained`, `goods_families_mixed` (both ways, counted in neither, as for freedom). Each contested alternative is evaluated as its own property `<name>@<encoder>` and reported in `load_goods_by_encoder: {encoder: (lost, gained, families)}`, never added to `load_goods`. `reading(row)` and `reading_by_encoder` as section 4; `strand_agreement(tag, reading)` gives agree | mismatch | no_row | unread. `summarize` adds per entry `constitutive`, `hard_cases`, `contested_readings`; `scoreboard_stats` adds `goods_rows` and `contested_readings`.
- **`cli_rules.py`**: `phil rules ablate` prints lost/gained and the reading per row; `--readings PATH` writes the section 4.2 table (entry, rule, tag, up, lost per encoder, reading per encoder, agreement).
- **`scoreboard.py`** and docs/scoreboard-ablate.md: two columns (`goods_rows`, `contested_readings`), header changed in the same commit as the engine (the 2026-11-04 append failure on a prose header is the precedent).
- **Tests** (`tests/test_rules_ablate.py`, schema tests): `goods_state` mapping, including vacuous persists = absent; toy entry with a must-be care duty and a breaker, where deleting the duty gives lost 1 and a constitutive reading; toy disability whose deletion yields a good, gained 1 and `load_goods` 0; two contested formulas with different flips, where `load_goods` equals the primary's and the alternative appears only in `load_goods_by_encoder`; validator rejections (goods without `contested`, with one encoder, with `polarity: unfreedom`, with check `invariant`; freedom with `polarity: good`); spawn equality (workers 1 vs 4) on a goods fixture. Dataset test: every goods property has two encoders and a `contested` key.
- **Dataset side** (computational-liberation): goods entries in `data/institutions/src/properties.yaml` (gloss from section 3, `encoders`, `contested`, `history` naming this file and the merge log); `build.py` passes the keys through.

Preregistered predictions for the engine change, checked before the goods enter the dataset: (E1) on the revision-5 dataset every ablation row is identical apart from the new zero-valued goods columns; (E2) `pytest -q` passes in both repositories and `check-all` is unchanged (it reads expected_properties only); (E3) after the goods enter, only goods columns change (prediction 4.4).

## 7. Order of work and agents

1. **Preregistration**: this file, committed alone (coordinator).
2. **Bundle** (coordinator): assemble and hash the section 2 bundle outside both repos.
3. **Encoder 1 and encoder 2**, in parallel: two fresh agents, the bundle only, output outside the repos; transcripts kept.
4. **Merge and `contested`** (coordinator): validate, run the equivalence checks, write the merge log to plans/priority-slice2-results.md. Goods do not enter `properties.yaml` until step 5's engine accepts them.
5. **Engine change** (builder in philosophy-engine): section 6; E1 and E2 checked on unchanged rows; then the goods enter the dataset, E3 checked.
6. **coverture-floor** (dataset builder): root change, entry, the two freedom properties, its card; layer-1 predictions 1 to 7 checked (`check-all --no-cache`, `diff --baseline`, gate).
7. **Run**: `phil rules ablate --k 6,8 --readings ...` on all 27 entries; section 4 table, encoder agreement, confound check, N/G/C/R; results and drift to plans/priority-slice2-results.md.
8. **Council**: faithfulness seat (section 1), card-only seat for coverture-floor; findings answered before anything is called a result.

Encoders never see steps 4 to 8 before both have submitted, and they are not reused as builders or reviewers.

## Author decisions after the council (2026-11-06; reviews docs/reviews/2026-11-06-slice2-correctness-review.md and 2026-11-06-slice2-faithfulness-review.md, both weakened)

Taken before revision 2 is preregistered; the revision-1 run and its results file stay as recorded.
1. **Four goods states.** `not_applicable`: no subject exists in any compliant trace (outside the ranking; never a loss or a gain). `absent`: a subject exists and the good never holds for it. `fragile`: the good can hold and can lapse. `stable`: a rule guarantees it. Fixes the ectogenesis/surrogacy "no child = goods lost" artefact (F2) and the kibbutz `child_with_family` / R4 row.
2. **Two measures, side by side, never combined.** The current measure is renamed **guaranteed** (stable vs not). A second column, **possible**, says whether the good can happen at all under the rules (reachable for an existing subject). "Constitutive" (redesign, do not cut) is used only when deleting a rule makes a good impossible, not when it removes a guarantee.
3. **Chosen-care good.** A new good: both spouses care for each other, the wife can exit, and her care carries no sanction. Written by two fresh encoders under the section 2 protocol, with the full encoder prompt inside the hashed bundle this time (merge-log disclosure). Meanwhile the revision-1 R3 row is reported only as "guaranteed only by R3, an implicit sanctioned duty; not advice to keep it".
Also (no decision needed; fix pass): kill the three surviving test mutants (fragile/absent order, contested pooling, goods k-disagreement); the vacuity check reads the good's own subject, and an undecided subject check is uncounted, not stable; cards carry a goods note and the ADR 0012 sentence; R20 is labelled an income-access floor, not the glossary's material floor, and its strand placeholder is removed; G's 5-vs-4 is labelled by construction; lost counts are reported per strand as well as per formula; the strict-compliance caveat sits beside coverture goods rows.

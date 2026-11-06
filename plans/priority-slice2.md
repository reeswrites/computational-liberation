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

## Revision 2 (preregistered 2026-11-06, before any engine change, encoding or run)

Status: preregistration of revision 2, written after the revision-1 run (plans/priority-slice2-results.md, 7383e7a), both council reviews (docs/reviews/2026-11-06-slice2-correctness-review.md, 2026-11-06-slice2-faithfulness-review.md) and the author decisions above. Everything above this heading stays as committed; revision-2 results go in a new "Revision 2" section of plans/priority-slice2-results.md, with drift recorded there and nothing here edited to match.

**What these predictions are blind to.** The author of this section read the revision-1 run outputs (`readings-27-s2.md`, `ablate-27-s2.json` in the slice-2 scratch run directory), the engine at c69aaf1 and the entry YAML. The predictions below are therefore **not blind about revision 1**: every revision-1 state and load is known. They are blind only about revision 2's new semantics (the `not_applicable` and `absent` states, the `possible` measure) and about the new good: no revision-2 query, probe or z3 call was run, and no new encoder has been started. Where a prediction rests on reading an entry's rules rather than on a known revision-1 number, it says so and gives a confidence.

Second encoder: agent, not someone living under the institution (ADR 0012).

### R2.1 Engine semantics (philosophy-engine; design only)

**Subject declaration.** Every `kind: goods` property gains a required key `subject`: a state formula with `t` free and no other free variable, true at step `t` exactly when some bearer of the good (the party the good is for) exists at `t`. A contested alternative may carry its own `subject`; absent that, it uses the primary's. Loader checks: `subject` parses and names only fluents the property's applicable entries declare (same rule as `formal`, including `entries`); and the formula's premise implies the subject: with `antecedent(formal)` as in rules_checks.py (existential closure of the implication premise under the universal prefix), `Ant(t) -> Subj(t)` must be valid with every fluent uninterpreted (z3, as scripts/goods_equiv.py). A formula without implication shape skips the second check. Failure is a load error, not a warning. The old `vacuity()` (any `is_*` fluent, rules_checks.py:226) is unchanged and still feeds freedom and other non-goods properties; goods no longer read it.

Subjects for the five revision-1 goods, fixed here (from section 3's "for whom" column and each formula's guard; no formula changes):

| good | `subject` |
| --- | --- |
| `cared_for`, `known_carer`, `child_with_family`, `provided_for` | `(exists ((s agent)) (is_subject s t))` |
| `mutual_household_care` | `(exists ((h agent) (w agent)) (married h w t))` |

`chosen_mutual_care` (R2.3): the encoders write it; predicted equivalent in effect to `(exists ((h agent) (w agent)) (married h w t))`.

**Witness steps.** Let `Good(t)` be the lowered `formal` at `t` and `Subj(t)` the lowered `subject`. `Wit(t)` = `Ant(t)` when `formal` has implication shape, else `Subj(t)`. A witness step is a step where the formula's premise holds for some binding, so the formula says something about the good there. This removes the step-0 grace artefact (correctness review finding 1): a guarded formula is true at the step a subject first appears only because its premise (`is_subject` at `t0` and `t`) is false there, and that step is not a witness step, so it can never count as the good holding.

**The four states**, per (entry, good, k, side of the row), on the same `Grounded` system as every check (strict compliance, init `declared`, step_mode `one`), decided in this order:

1. **Subject query** `S = sat(system ∧ ∨_{t=0..k} Subj(t))`. unsat: `not_applicable`. unknown: uncounted (reason `subject_unknown`).
2. **Witness query** `W = sat(system ∧ ∨_{t=0..k} Wit(t))`. unsat: uncounted (reason `no_witness_within_k`: a bearer exists but too late for the premise within k). unknown: uncounted (`witness_unknown`).
3. **Possible query** `P = sat(system ∧ ∨_{t=0..k} (Wit(t) ∧ Good(t)))`. unsat: `absent` (a bearer exists and the good never holds at a witness step of any compliant trace). unknown: uncounted (`possible_unknown`).
4. **Guaranteed query**: the `invariant` check of `formal` (no compliant trace has a step where `Good` is false). `holds_to_k`: `stable`. `violated`: `fragile` (the good can hold and fails somewhere). unknown: uncounted (`guaranteed_unknown`).

An undecided z3 result at any step is uncounted, listed with its reason in `uncounted` and `uncounted_reasons`, and **never stable** (closes correctness review finding 2(b)). The `persists` verdict is still run and reported as the property's `verdict` (schema keeps `check: persists` on goods), so `flips` keeps its revision-1 content, but no goods state reads it. `invariant` replaces `persists` for the guarantee because it has no vacuity loophole (a formula false from its first witness step onward never "persists-fails"); the correctness review found every revision-1 `stable` cell also `invariant` holds_to_k and every `fragile` cell `fails`, so the guaranteed bit is predicted identical to revision 1's on every cell that was not `absent` (E1r2). Possibility and guarantee are bounded within k, like every verdict. Name clash: the existing row field `RuleAblation.not_applicable` (properties not evaluated in an entry because their fluents are undeclared) keeps its meaning and is documented as such; the goods state is the string `not_applicable` inside `goods_states`, printed `n/a` in the readings table.

**Two measures, never combined.** For a counted state, `guaranteed` = (state is `stable`), `possible` = (state is `fragile` or `stable`). Per goods property and row (before, after):
- either side `not_applicable`: no loss and no gain under either measure; the property is listed in `goods_not_applicable` (information) and the move is shown in the goods-changes column. A deletion that prevents any bearer from existing is outside the ranking.
- either side uncounted: listed, counted in neither measure.
- **guaranteed lost**: stable before, fragile or absent after; **guaranteed gained**: the reverse.
- **possible lost**: fragile or stable before, absent after (the good becomes impossible for an existing bearer); **possible gained**: the reverse.

So stable > absent is lost under both; stable > fragile only under guaranteed; fragile > absent only under possible. Per family as before: a family is lost if some member is lost and none gained, gained the reverse, mixed (both) counted in neither. Gains are shown, never counted in a load.

**Fields** (rules_ablate.RuleAblation): `goods_states` / `goods_alt_states` values in {not_applicable, absent, fragile, stable}; `load_goods_guaranteed`, `load_goods_guaranteed_gained`, `goods_families_guaranteed_{lost,gained,mixed}`; `load_goods_possible`, `load_goods_possible_gained`, `goods_families_possible_{lost,gained,mixed}`; `goods_not_applicable`; `uncounted_reasons`; `load_goods_by_encoder: {encoder: {"guaranteed": {lost, gained, families_lost, families_gained}, "possible": {...}}}`. `load_goods` and `load_goods_gained` are removed (renamed, not aliased, so no consumer reads the old meaning silently; the builder updates every consumer in both repos, including cli_rules and the scoreboard). MultiKAblation.to_dict carries both measures per k.

**Readings.** Two reading columns per encoder, from `up` = load_freedom_up and the measure's lost count:
- **possible** (the reading decision 2 names): tying (up > 0, lost 0), **constitutive** (lost > 0, up 0: deleting the rule makes a good impossible), hard case (both), unread. Only this column feeds `summarize`'s `constitutive` and `hard_cases`.
- **guaranteed**: tying, **guarantee-carrying** (lost > 0, up 0: deleting the rule removes a guarantee), hard case (guarantee), unread. Feeds a new summary list `guarantee_carrying` (and `hard_cases_guaranteed`). The word "constitutive" is never used for this column.
- Strand agreement per column: tying tag with tying = agree; superadditive tag with constitutive (possible) or guarantee-carrying (guaranteed) = agree; rival tag with a reading = no row; untagged (`strand: null`, R2.5) with a reading = untagged; any other pairing with a reading = mismatch; no reading = unread.
- `summarize` per entry: `constitutive`, `hard_cases`, `guarantee_carrying`, `hard_cases_guaranteed`, `contested_readings` (ranked rules whose reading differs by encoder under either measure), `goods_not_applicable_rows`. Ranking (top rules by load_freedom_up) is unchanged.
- `readings_table` columns: entry, rule, ranked, tag, k, up, then for each measure and each encoder: lost, gained, reading, agreement; last, goods changes (all four states, `n/a` included). A row is printed when up > 0 or any goods state changes (n/a moves included).
- `scoreboard_stats` header unchanged: `goods_rows` = rows at ks[0] with a counted lost or gained under either measure; `contested_readings` as above.

**Contested alternatives** stay in their own columns: each `<name>@<encoder>` is evaluated as its own property with its own four states; never in the primary loads, flips or summaries. Two fixes from the correctness review (finding 3): the alternative for an encoder is chosen **by name** (`<name>@<e>` exists and `e` is not the property's `encoders[0]`), not by the encoder's position across goods; and if an encoder's alternative is uncounted while the primary is counted, the good is listed in that encoder's `uncounted` (not dropped silently and not replaced by the primary). Encoder labels are roles: `encoder-1` is the primary column, `encoder-2` the alternative column, for revision-1 and revision-2 goods alike (R2.3).

**k-disagreement** (rules_ablate.py:500ff kept and extended): a goods property is listed when its (before, after) state pair under either measure, or its n/a move, differs across k, including when every verdict string is unchanged.

### R2.2 Test requirements (tests/test_rules_ablate_goods.py; the builder runs each named mutation and records that it fails at least one test)

1. **State transition table (kills M1, the fragile/absent order swap).** A unit test of the transition function over all 16 (before, after) pairs of the four states, asserting lost / gained / neither under each measure, including: fragile > absent = possible lost, guaranteed neither; absent > fragile = possible gained; stable > absent = lost under both; any pair with `not_applicable` = neither. Plus a fixture row (item 5c) that really produces fragile > absent and asserts `load_goods_possible == 1`. Any swap of fragile and absent in an order or predicate fails it.
2. **Contested pooling (kills M2).** Fixture where the **alternative flips and the primary does not**: the primary's formula stays stable across the deletion (e.g. trivially true for a bearer), the alternative is the care formula that goes stable > fragile and, in a second row, fragile > absent. Assert `load_goods_guaranteed == 0` and `load_goods_possible == 0`, `load_goods_by_encoder["e2"]` lost 1 under the respective measure, `reading_by_encoder` differs, and the alternative's name is not in `flips`. Pooling all states into the primary load fails it. Also: (a) a goods property whose `encoders` are `[e2, e1]` (primary e2) with an e1 alternative, asserting e1's view uses the alternative (kills position-based selection); (b) an alternative made uncounted (monkeypatched unknown) while the primary is counted, asserting it is listed for that encoder.
3. **Goods k-disagreement (kills M5, deleting the goods k block).** Fixture in which care can first hold only after a chain of actions longer than the smaller k, so at the smaller k the row reads absent > absent and at the larger k fragile > absent, with the persists verdict string `fails` on both sides at both k (so the flips-based block cannot catch it). Assert `k_disagreement == [<good>]` and the scoreboard `k_disagreements` counts it.
4. **not_applicable.** (a) A ranked prohibit of the only act that creates the bearer: before fragile or stable, after `not_applicable`; both loads 0, both readings unread, the rule absent from `constitutive` and `guarantee_carrying`, listed in `goods_not_applicable`. This replaces, deliberately, the revision-1 assertion at tests/test_rules_ablate_goods.py:101-103 that pins stable > absent for "no subject is ever enrolled"; the commit message says so. (b) The good's own subject is read, not any `is_*` fluent: a good guarded on `married` in a fixture where no `is_*` fluent ever holds but marriage is reachable reads `fragile` or `stable`, not `not_applicable` (closes correctness review finding 2(a)). (c) Undecided subject query (monkeypatched unknown) gives uncounted with reason `subject_unknown`, never stable (the revision-1 engine read stable). (d) Loader: goods without `subject` rejected; `subject` naming an undeclared fluent rejected; a premise that does not imply the subject rejected.
5. **The possible measure.** (a) Barred good: a disability bars the only action that realises the good for a bearer present from step 0; base `absent`; deleting the disability gives `fragile`, possible gained 1, guaranteed unchanged (the kibbutz R4 shape). (b) Step-0 grace: a one-step-grace formula whose bearer exists at step 0 and whose good can never hold reads `absent`, not `fragile`. (c) Guarantee removed, possibility kept: deleting a must-be care duty with a free breaker and a free restorer gives stable > fragile, guaranteed lost 1, possible lost 0, readings guarantee-carrying / unread, rule in `guarantee_carrying`, not in `constitutive`. (d) Made impossible: a ranked prohibit of the only care permission for an existing bearer gives fragile > absent, possible lost 1, reading constitutive. (e) A formula without implication shape uses `Subj` as its witness.
6. **Kept from revision 1, updated to the new fields**: validator rejections, `expand_contested` idempotence, adding goods changes no freedom column, `entries` applicability, CLI readings table (new column header asserted), spawn equality workers 1 vs 4 on a fixture carrying all four states and a contested alternative, dataset test (every goods property has two encoders, a `contested` key and a `subject`).

Mutations the builder runs and records (scratch copy, as the correctness review did): M1 (swap fragile/absent anywhere in the state predicates), M2 (pool alternatives into the primary load), M5 (delete the goods k block), M6' (undecided subject read as stable), M8 (subject from any `is_*` fluent), M9 (alternative chosen by position). Each must be killed.

### R2.3 The chosen-care good, the encoder bundle and the existing goods

**Existing five goods: not re-encoded.** Revision 2 changes the instrument (states, measures, subject), not the goods. Re-encoding them at the same time would put two changes between revision 1 and revision 2, so no row could be attributed to either; the correctness review reproduced every revision-1 number and the faithfulness review's back-translation found the formulas say what their glosses say apart from known, recorded limits (police `is_subject` never cleared; `child_with_family` three goods under one name; `provided_for` partly freedom-shaped). Those limits are reported beside the rows they touch, and a re-encoding with the corrected conventions and no shared-fluent instruction is a later, separate experiment. The `formal` and `contested` texts in properties.yaml stay byte-identical; only `subject` is added (table above).

**New good** (`kind: goods`, `polarity: good`, `check: persists`, `family: chosen_mutual_care`; gloss only, the formula is the encoders' job):

| id | good, for whom | entries | why a good |
| --- | --- | --- | --- |
| `chosen_mutual_care` | A married couple care for each other (the husband for the wife and the wife for the husband) while the wife can leave the marriage and no one holds a power to sanction her: care both give and she is free not to give. For the wife, within the couple. "Can leave" is read at the fluent level as her permitted, unsanctioned way out at that step. "Her care carries no sanction" is read at the fluent level as: at that step no one holds a power to coerce her. The vocabularies record who holds a power to sanction whom, not which duty a sanction enforces, so this is the closest reading they allow; it is stricter than the gloss (any sanction power counts, not only one attached to her care). | coverture-household, coverture-household-us, mwpa-earnings, coverture-floor | Mutual care that is chosen rather than imposed (docs/theory.md: "turning imposed bundles into chosen ones"). It separates chosen from imposed mutual care, which `mutual_household_care` cannot (faithfulness review finding 3, option i). |

Ablation also reads it wherever its fluents are declared. Only the coverture family declares `married`, so it is read in the nine coverture-family entries (the four listed plus coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-sole-trader, mwpa-suit, mwpa-property-narrowed as information rows) and in no other entry. Known limit, stated now: no fluent says whether her care is obliged, so a formula cannot see the wife's care duty itself; exit and no-sanction are the fluent-level proxies for "chosen".

**Protocol**: section 2 as before (two fresh agents never used in this slice or its reviews, run in parallel, encoder 1 primary, no contact, transcripts audited, coordinator merge by z3 validity of `A <-> B` with fluents uninterpreted, applied to `formal` and to `subject` separately: either non-equivalent makes the pair contested, with the alternative carrying its own subject). Changes from revision 1: the full encoder prompt is a file inside the hashed bundle, and nothing outside the bundle is given to the encoders.

**Bundle** (scratch directory outside both repos, hashed; manifest committed beside the revision-1 one in data/institutions/goods-encoding/):
- `prompt.md`: the prompt below, with the placeholders `<N>`, `<BUNDLE>`, `<OUT>`. The coordinator substitutes them and pastes the result verbatim as each encoder's entire first message; the manifest records the template hash and the hash of each substituted text, and the two must differ only in `<N>`.
- `goods-list.md`: the `chosen_mutual_care` row of the table above, verbatim (header plus that row), and nothing else from this file.
- `conventions.md`: the "Property `formal`" bullet of data/institutions/README.md "Conventions", verbatim; two style examples with name, gloss and formal only: `cannot_contract` (gloss "No subject may contract in her own name.") and `subject_cannot_exit_persists` (gloss "Every subject has no permitted exit. Vacuous before any subject exists."), formulas as in properties.yaml; `care_duty_on_women` is dropped (its gloss names ectogenesis rules and it carried the grace both revision-1 encoders copied); and the goods conventions below, verbatim.
- `vocab/`: the four revision-1 vocabulary files for coverture-household, coverture-household-us, mwpa-earnings, coverture-floor, byte-identical (checked against the revision-1 manifest). No rules, cards, verdicts, ablation output, results, reviews or other goods.
- `validate.sh`: the revision-1 validator, unchanged (syntax and declared fluents of any formula, no verdicts); encoders run it on both `formal` and `subject`.

Goods conventions text (for `conventions.md`, verbatim):

> ## Goods conventions
>
> - A goods property is a state formula `formal` (`t` free) whose holding is good for the named party, plus a `subject` formula (`t` free, no other free variable) that is true at `t` exactly when some bearer of the good exists at `t`. If `formal` has the shape `(forall (...) (=> P Q))`, `P` must imply `subject`.
> - Witness steps: if `formal` has that shape, the steps where `P` holds for some binding; otherwise the steps where `subject` holds. At other steps the formula is true without saying anything about the good.
> - The engine reads each goods property, per entry and within a bounded number of steps, in one of four states: not applicable (no compliant trace has a bearer); absent (a bearer exists, but the good holds at no witness step of any compliant trace); fragile (the good holds at some witness step of some compliant trace, and some compliant trace has a step where it fails); stable (it holds at every step of every compliant trace, and a bearer exists).
> - Use only fluents, roles and actions declared in the entry's vocabulary; add no new fluents. `(enabled <action> <args>)` is not available in property formulas unless a derived fluent wraps it.

**Encoder prompt (the full text of `prompt.md`; no other instruction is given):**

> You are encoder `<N>` for one goods property in a research dataset of institutions encoded as rules. You work alone. Another encoder is doing the same task separately; you will not see their work and they will not see yours.
>
> **Access rules.**
> - Read only the files in the bundle directory `<BUNDLE>`: `prompt.md` (this text), `goods-list.md`, `conventions.md`, the files in `vocab/`, and `validate.sh`. Do not open any other file or directory: not the repositories computational-liberation or philosophy-engine, not their plans, docs, data, tests or history, not any other scratch directory, and not the other encoder's output.
> - The only command you may run is the bundle's validator: `bash <BUNDLE>/validate.sh <entry-id> '<formula>'`. It checks syntax and declared fluents only and reports no verdicts. Run no other command: no engine check, no search, no web access.
> - Write exactly one file, `<OUT>/encoder-<N>/goods.yaml`, and nothing else anywhere.
> - At the end, list in your reply every file you read and every command you ran.
>
> **Task.**
> - Write one state formula `formal` for the good `chosen_mutual_care` in `goods-list.md`, and its `subject` formula, following `conventions.md` and the vocabulary of each entry listed for the good.
> - Encode the gloss. You are not shown the entries' rules; do not guess at rules or write the formula so that it comes out one way or another in any entry.
> - Write one formula for all listed entries if their vocabularies allow it. If an entry's vocabulary cannot carry the good, or part of it, record that entry under `not_expressible` with the reason, and say in `notes` what your formula reads there instead.
> - Use only fluents declared in the entry's vocabulary; never invent a fluent, role or action. If the validator warns that a fluent is undeclared in a listed entry, either rewrite the formula or record `not_expressible` for that entry, and say which in `notes`.
> - Validate `formal` and `subject` in every listed entry and copy the validator's one-line result for each.
> - If the coordinator returns a syntax error after you submit, you may fix the syntax once; no other change.
>
> **Output format** (YAML, exactly these keys):
>
> ```yaml
> encoder: encoder-<N>
> bundle_files_read: [<every bundle file you read>]
> goods:
> - id: chosen_mutual_care
>   formal: '<state formula, t free>'
>   subject: '<state formula, t free: some bearer of the good exists at t>'
>   back_gloss: '<one line: what your formula says, in plain words>'
>   entries: [<entry ids the formula is written for>]
>   validated: {<entry-id>: '<validator result for formal; validator result for subject>'}
>   not_expressible: {<entry-id>: '<reason>'}   # {} if none
>   notes: '<choices you made, readings of the gloss you rejected and why>'
> ```

The revision-1 instruction "prefer a formula that uses only fluents shared across them" is **dropped**: the faithfulness review (finding 6) links it to both encoders guarding on `is_subject` and to the police and kibbutz misses, and for one good over four coverture-family vocabularies that share every fluent the good needs it has no work to do.

**Dataset entry** (after the merge): `chosen_mutual_care` in properties.yaml with the gloss above, `subject`, `encoders: [encoder-1, encoder-2]` (role labels; `history` names them as the revision-2 fresh agents, distinct from the revision-1 encoders, and gives the bundle hash and merge-log line), `entries` the four listed, `contested` per the merge. Merge log: a "Revision 2" section appended to data/institutions/goods-encoding/merge-log.md, with both transcripts audited as before.

### R2.4 Predictions for the revision-2 run

Run: `phil rules ablate --k 6,8 --readings ...` on all 27 entries, per encoder, as section 7 step 7. All predictions hold at k=6 and k=8 alike (goods k-disagreements 0). Confidence is high where a row only renames a known revision-1 state, and given per row otherwise.

**Base states (unablated).**

| entry | good | revision 1 | revision 2 | confidence |
| --- | --- | --- | --- | --- |
| nine coverture-family entries | cared_for, mutual_household_care, known_carer, provided_for (both encoders) | stable | stable | high |
| nine coverture-family entries | chosen_mutual_care (both encoders) | (new) | **absent**: while married the exit bar holds, so the good fails at every witness step | high |
| police-crisis | cared_for, known_carer | fragile | fragile (care reachable after dispatch) | high |
| cps | cared_for, known_carer, child_with_family | fragile | fragile (services and a non-removed child with a parent reachable) | medium (action-slot crowding by cps's obligations not traced) |
| kibbutz-childrens-house | cared_for, known_carer | fragile | fragile (care holds from step 0) | high |
| kibbutz-childrens-house | child_with_family | fragile | **absent** (R4 bars `sleep_home`; the other disjuncts' fluents are undeclared and lowered false) | high |
| ectogenesis | cared_for, known_carer, child_with_family | fragile | fragile (decant, register, care: first witness with care at step 5) | medium-high |
| airline-flight | cared_for, known_carer | stable | stable | high |
| gestational-surrogacy, crisis-team, companion-*, kibbutz-no-implicit | cared_for, known_carer | fragile | fragile | medium |

No base cell reads `not_applicable` and no cell is uncounted (no `no_witness_within_k` at k=6 or 8).

**The 13 preregistered reading rows** (section 4.2), primary; encoder 2 identical. Columns: up / lost / reading / agreement, per measure.

| entry | rule (tag) | guaranteed | possible | against section 4.2 |
| --- | --- | --- | --- | --- |
| coverture-household | R2 (superadditive) | 0 / 4 / guarantee-carrying / agree | 0 / 0 / unread | 4.2's "constitutive" held only as a guarantee; R2's deletion leaves every good possible (`marry` sets care, `maintain` is free) |
| coverture-household | R3 (superadditive, implicit) | 0 / 1 / guarantee-carrying / agree | 0 / 0 / unread | **R3 under possible: deleting R3 leaves mutual care possible (`marry` sets both strands, `keep_house` is free), so R3 is not constitutive.** Guaranteed column reported only as "guaranteed only by R3, an implicit sanctioned duty; not advice to keep it" (decision 3) |
| coverture-household | R4 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| coverture-household | R6 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row; **possible gained 1** (chosen_mutual_care absent > fragile) | held; the gain is new |
| coverture-household | R7 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| police-crisis | R2 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | miss stands (as encoded no rule guarantees the goods, and none makes them impossible) |
| police-crisis | R4 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | held |
| cps | R10 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | held |
| kibbutz-childrens-house | R2 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 4.2's hard case missed (known_carer stays possible: the metapelet's care holds from step 0) |
| kibbutz-childrens-house | R3 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | miss stands (with R3 deleted care is still possible; it was never guaranteed: `release` is unregulated) |
| kibbutz-childrens-house | R4 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row; **possible gained 1** (child_with_family absent > fragile) | **4.2's "gained 1" now held, under possible**; guaranteed gained 0 (sleeping home is permitted, never guaranteed) |
| ectogenesis | R4~prohibit (superadditive) | 0 / 0 / unread | **0 / 3 / constitutive / agree** (cared_for, known_carer, child_with_family fragile > absent) | **4.2 held, under possible**: with R4 prohibited, `provide_care` is regulated only by R5's `must`, which R4~prohibit forbids in the same condition, so no compliant trace has care for a decanted child. Medium-high confidence |
| ectogenesis | R5 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |

Totals, five entries: guaranteed **10 read rows, 6 agree, 0 mismatch, 4 no row**; possible **9 read rows, 5 agree (coverture R4, R7; kibbutz R2; ectogenesis R4~prohibit, R5), 0 mismatch, 4 no row**. Every other ranked row in the five entries is unread under both measures (protections carry only freedom_down). Expected headline, possible column: "no single deletion makes a coverture good impossible; deleting the exit bar makes chosen mutual care possible; in ectogenesis, prohibiting the parent's permission to care makes care impossible". Guaranteed column: as revision 1 with "constitutive" renamed "guarantee-carrying".

**F2 and the no-subject rows.** Ectogenesis R1~prohibit: cared_for, known_carer, child_with_family fragile > **not_applicable** (no gestation, no decant, no subject); lost 0 under both measures; reading unread under both; with freedom_down 1 it is a protection. Revision-1 F2, reapplied to both measures ("a ranked `may`-rule row in the five entries other than ectogenesis R4~prohibit carries lost > 0"), **is predicted not to fire**. Information rows, same mechanism: gestational-surrogacy R2~prohibit (cared_for, known_carer fragile > n/a; lost 0) and airline-flight R1~prohibit (stable > n/a; lost 0, so it reads tying from its up 1, no longer hard case). These three are the only rows in the 27 entries with an n/a move (`goods_not_applicable_rows`). Gestational-surrogacy R4~prohibit (information): cared_for, known_carer fragile > absent, possible lost 2, constitutive, by the same mechanism as ectogenesis R4~prohibit.

**Kibbutz.** child_with_family base **absent** under the new semantics (both measures 0); R4 deleted: absent > fragile, possible gained 1, guaranteed gained 0; no other kibbutz row moves it. R3 deleted: no goods change (care stays possible; it was never guaranteed).

**The chosen-care good.** Base absent in all nine coverture-family entries under both encoders. Single-rule rows:
- **R6 deleted** (the exit bar): absent > fragile, **possible gained 1**; guaranteed unchanged (0 > 0: neglect, `neglect_house` and `misbehave` stay free, so it is never guaranteed). In all nine entries. This is the one rule whose deletion makes the good possible.
- **R5** (chastise when married and misbehaving): R5 and R5~prohibit are unranked in every coverture-family entry and move nothing. R5's sanction power needs `misbehaves`, which starts false, so it does not block the good at the steps after marriage; it would show only jointly with R6 (with R6 deleted the good is fragile partly because `misbehave` can enable chastisement). The {R5, R6} pair is a slice-4 question, not read here.
- **R3, R2, R4, R7, R1 and the route rules** (R10 to R14, R17, R18, R20): no change (absent > absent).
- So no rule carries the good under either measure (lost 0 everywhere), and R3 reads lost 0 on it under both. That is the faithful outcome the faithfulness review predicted for option (i) ("coverture reads never; R3 reads lost 0"). Under the guaranteed measure the good is invisible in every row.
- Encoder agreement: the two formulas may differ logically (e.g. sanction quantified over every agent or only over the husband; with or without a care-continuity clause); predicted **same effect**: identical states in every row, `contested_readings` 0, no `not_expressible` (every listed entry declares `married`, `provides_care`, `can_exit`, `can_sanction`).

**Route comparison** (T = mwpa-earnings, F = coverture-floor; per encoder; k=6 and 8; G now per measure, plus gains reported):

| quantity | T | F | note |
| --- | --- | --- | --- |
| N | 3 (R4, R6, R7) | 3 (same) | unchanged: tie |
| G, guaranteed | 5 (R2 4, R3 1) | 4 (R2 3, R3 1) | unchanged from revision 1; **by construction**, the same margin case as C (faithfulness finding 7); R2's 4 or 3 formulas read 1 strand |
| G, possible | 0 | 0 | tie: no base-rule deletion makes any good impossible on either route |
| gained over base rules, possible | 1 (R6, chosen_mutual_care) | 1 (R6, chosen_mutual_care) | equal |
| gained over base rules, guaranteed | 0 | 0 | |
| C | holds_to_k | violated | unchanged, by construction |
| R | 1 (R14) | 1 (R20) | unchanged |

Winner rule (section 5) applied per measure: guaranteed: tie on N, F lower on G (by construction); possible: tie on N and on G. Consequence: the section-5 branch "tie as predicted" still applies (T1 stays a hypothesis; slice-4 candidates {R2, R20} and {R4, R6, R7} unchanged). Added statement to expect: the floor's goods advantage is about guarantee only (the wife's provision stops depending on R2 being kept), not about what is possible; that matches T1's stated reason (survival not depending on being chosen) and says nothing about order.

**E-style predictions.**
- **E1r2.** Engine change on dataset D1 = the revision-1 dataset (725c63d) plus the five `subject` keys and nothing else: in all 712 rows at k=6 and 8, every non-goods field is identical to the revision-1 run (ablate-27-s2.json): loads, families, flip directions, non-goods flips, `uncounted` of non-goods properties, ranking flags, `inconsistent_after`, k-disagreements, top rules in all 27 entries. Goods: the guaranteed transition of every (row, good, encoder) equals revision 1's stable/not-stable transition, except in the three n/a rows; every revision-1 `absent` cell (all are after-states in ectogenesis R1~prohibit, gestational-surrogacy R2~prohibit, airline-flight R1~prohibit) reads `not_applicable`; so `load_goods_guaranteed` equals revision-1 `load_goods` in every row except those three (3, 2, 2 > 0). The persists verdicts, and hence goods entries in `flips`, are unchanged.
- **E2r2.** `pytest -q` passes in both repositories; `check-all --no-cache` 146/146; `diff --baseline` 0 changed, 0 added, 0 removed; gate PASS, criterion (b) detail and `scripts/drop_one_match.py` output identical (layer 1 reads `expected_properties` only, and no entry expects a goods property).
- **E3r2.** Adding `chosen_mutual_care` (D2 = D1 + the good): every field of every other property identical between the D1 and D2 runs; only chosen_mutual_care's states and the possible loads or gains it enters change, i.e. the R6 rows of the nine coverture-family entries (possible gained 1).
- **E4r2.** R20's strand set to null (R2.5) changes only the `strand` field of the coverture-floor R20 and R20~prohibit rows (and their agreement cell, now "untagged"; both rows are unread); no verdict, gate or iso result changes (coverture-floor has no iso claims).
- **Totals.** `uncounted` 0 (goods reasons included), `inconsistent_after` 0, k-disagreements 0. Scoreboard row: `goods_rows` 33 (18 coverture-family R2/R3, 9 coverture-family R6, airline R2, companion-ownership and companion-guardian-renamed R1~prohibit (guaranteed gained 2 each, as in revision 1), kibbutz R4, ectogenesis R4~prohibit, gestational-surrogacy R4~prohibit), `contested_readings` 0, `top_rule_changes` 0 against the revision-1 summary. Summary `constitutive` non-empty only in ectogenesis and gestational-surrogacy ([R4~prohibit]); `guarantee_carrying` [R2, R3] in the nine coverture-family entries and [R2] in airline-flight; `hard_cases` and `hard_cases_guaranteed` empty.
- **Layer 1.** No verdict effect. `build.py --check`: 27 institutions, 34 properties (one new goods row; six goods gain `subject`), cards unchanged except the R2.5 card notes and R20's strand display. ASSUMED: run time at most twice revision 1's 7m23s (four goods queries per property and side instead of two).

**Falsifiers** (each reported, none fixed in place):
- RF1: ectogenesis R1~prohibit or gestational-surrogacy R2~prohibit reads any state other than `not_applicable` after, or carries lost > 0 under either measure.
- RF2: kibbutz child_with_family base is not `absent`, or the kibbutz R4 row's possible gained is not 1.
- RF3: any coverture-family row carries possible lost > 0 for any good (R3 on mutual_household_care included).
- RF4: ectogenesis R4~prohibit's possible lost is not 3.
- RF5: chosen_mutual_care base is not `absent` in some coverture-family entry, or a row other than R6 changes it, or R6 does not make it possible.
- RF6: any reading differs by encoder (chosen_mutual_care or provided_for).
- RF7: the guaranteed column differs from revision 1 anywhere outside the three n/a rows, or any non-goods field differs (E1r2, E3r2: an engine defect, not a result).
- RF8: any uncounted goods cell, any `no_witness_within_k`, or any goods k-disagreement.
- RF9: a ranked row in the five entries other than ectogenesis R4~prohibit reads constitutive or hard case under possible.

### R2.5 Fix pass (no prediction; checklist)

- [ ] Cards: a one-line goods note in the cards of coverture-household, police-crisis, cps, kibbutz-childrens-house, ectogenesis, coverture-household-us, mwpa-earnings and coverture-floor (through the entry source that build.py renders, cards are generated), giving the revision-2 readings under both measures and the ADR 0012 sentence; written after the run. For police-crisis, cps, kibbutz and ectogenesis the note says "as encoded, no rule guarantees these goods", not "care is fragile here".
- [ ] coverture-floor R20: `plain`, notes and card call it "an unconditional income-access floor for the wife", not the glossary's material floor (faithfulness finding 10); `strand: null` with the engine accepting `Strand | None` (key still required; null = untagged, outside the bundle; `+strands` iso levels treat null as its own tag), recorded in R20's `choices` and docs/plan.md's strand-tag item.
- [ ] Route comparison: G's 5-vs-4 labelled "by construction: the same margin case as C" wherever it is stated.
- [ ] Per-strand counts: every lost count in the results tables is followed by the number of distinct strands the lost formulas read (e.g. "R2: 4 formulas, 1 strand, `provides_care(h, w)`"); goods counts are never read as "goods lost".
- [ ] Strict-compliance caveat beside every coverture goods row: under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented.
- [ ] Revision-1 results wording carried forward as the reviews asked (pass item 1 as protocol independence only; encoder 2 the closer reading of `provided_for`'s gloss; the prompt disclosure named in results 4.2 and 4.3).

### R2.6 Order of work and pass test

1. This section, committed alone. 2. Bundle assembled and hashed (coordinator). 3. Two fresh encoders in parallel, bundle only. 4. Merge, merge-log section (coordinator). 5. Engine (builder, philosophy-engine): R2.1 and R2.2, mutation record; E1r2 and E2r2 on D1. 6. Dataset: `subject` keys (D1), then the new good (D2, E3r2), then the R20 fix (E4r2). 7. Run on all 27 entries; results, drift and the R2.4 tables in the revision-2 section of plans/priority-slice2-results.md. 8. Council: correctness seat (states, measures, tests, mutations) and faithfulness seat (back-translation of `chosen_mutual_care` and its subject, transcript audit, whether the fluent-level "no sanction" reading is faithful); findings answered before anything is called a result; then the card notes.

Pass: the engine implements R2.1 with every R2.2 test and every listed mutation killed; `chosen_mutual_care` encoded by two audited fresh encoders from a hashed bundle that contains the prompt; the run produces both measures for the 13 rows, the n/a rows, the kibbutz rows, the route comparison and the new good, per encoder, at k=6 and 8, with uncounted, inconsistent_after and k-disagreements listed; the R2.5 checklist done; every report carries the ADR 0012 sentence. Fail: a revision-1 formula changed; a contested alternative pooled or dropped; a prediction edited after the run; the encoders given any instruction outside the bundle. A missed prediction is a result.

## Author decisions after the revision-2 council (2026-11-06)

1. **Primary measure per good**, a field on each goods property with a one-line reason; both columns are still reported, and goods ranking reads the primary one. Mapping (proposed by the assistant, accepted by the author as a value call, not a finding): `guaranteed` for `cared_for` and `provided_for` (a dependent's care or subsistence that is merely allowed is not enough); `possible` for `chosen_mutual_care`, `mutual_household_care`, `known_carer`, `child_with_family` (relational goods: forcing them is meaningless or is itself control).
2. **Care duty visible by derivation**: the engine derives an `obliged` fluent from the rules (true when some rule forces the act or state), the way power fluents are derived from enablement (ADR 0013); no hand tags. `chosen_mutual_care` is then re-glossed and re-encoded to exclude obliged care. Preregistered; lands before slice 4.
3. **Stronger independence test**: a blind gloss author (a fresh agent that sees docs/theory.md and docs/intent.md only, never rules, cards, plans, predictions or results) writes the goods glosses; the second encoder is a non-Claude model called through its API with the same hashed bundle, and the coordinator validates its output (one syntax-fix round, as before). Run as a separate experiment against the current encodings, not a replacement.
4. Source verification: the author runs plans/sourcing-verify-session.md in a local session.

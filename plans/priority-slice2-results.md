# Priority slice 2: results (goods, second encoder, floor route)

Status: run 2026-11-06. Preregistration: plans/priority-slice2.md (cd2f895); nothing in it was edited. Engine: philosophy-engine a16691b (goods) + c69aaf1 (dataset sync) = ENGINE_PIN c69aaf1. Dataset: computational-liberation 725c63d (27 entries, 33 properties). Merge inputs: data/institutions/goods-encoding/ (89c4e28; bundle hash `127e9627fe78b47537b19e7a35fad8b6770f0cfc47188420337103cf357c7cb0`, per-file hashes in `bundle-manifest.sha256`).

**Second encoder: agent, not someone living under the institution (ADR 0012).** Both encoders are instances of one model given one bundle, and both copied the one-step grace from the `care_duty_on_women` style example (merge log). Every agreement below between "encoder-1" and "encoder-2" measures that model's consistency, not agreement between people.

All quantities are statements about encodings (ADR 0011); `coverture-floor` is a counterfactual (ADR 0004). Builder only: no council seat (section 1 "Council", section 7 step 8) has reviewed anything here yet.

## Headline

- **Route comparison (section 5): as predicted.** N(T) = N(F) = 3 ({R4, R6, R7}; families no_standing, cannot_exit, cannot_contract): a tie on bonds left. G(T) = 5, G(F) = 4 under both encoders: the floor route leaves fewer goods resting on the husband's duty, because R2 no longer carries `provided_for` in F. C: T holds_to_k, F violated (by construction). R: **1 vs 1, predicted 2 vs 1** (miss, see drift). Consequence (section 5 table, "tie as predicted"): T1 stays a hypothesis; slice 4 receives the must-go-together candidates {R2, R20} for `provided_for` in F and {R4, R6, R7} in both end states.
- **Readings: held in the coverture family, missed elsewhere.** 9 of the 13 preregistered rows read as predicted. The four misses (police R2, kibbutz R2, kibbutz R3, ectogenesis R4~prohibit) have one cause: in police-crisis, cps, kibbutz-childrens-house and ectogenesis every goods property is already **fragile** in the unablated entry (predicted stable in most), so no deletion can lose it except by making it vacuous (absent). Falsifier F2 fires once (ectogenesis R1~prohibit, by that vacuity route); F1, F3, F4, F5, F6 do not.
- **Encoders: no reading differs.** One of five goods is contested (`provided_for`; predicted at least two), and the contested pair has identical states in all 254 rows where it is read.
- **Pass test (section 1): items 1 to 5 met**, with the same-model caveat on item 1; not yet "a result" in the section 7 sense until the council (step 8) has run.

## Section 6: engine predictions

| # | Prediction | Result |
| --- | --- | --- |
| E1 | On the revision-5 dataset every ablation row identical apart from new zero-valued goods columns | **held**. Baseline first produced on e27127b with the then-current dataset (26 entries, k=6,8): 690 rows. New engine (a16691b) on the same dataset: 690 of 690 rows identical on every pre-existing field; new fields (`load_goods_gained`, `goods_families_*`, `goods_states`, `goods_alt_states`, `load_goods_by_encoder`) zero or empty in all 690; summary identical apart from the new empty lists |
| E2 | `pytest -q` passes in both repositories; `check-all` unchanged | **held**. Engine 577 passed, 2 skipped (live LLM) before the sync, 580 passed after (the dataset-parametrised tests gain coverture-floor); this repo 31 passed before, 32 after (new goods dataset test); `diff --baseline` 0 changed before the dataset change |
| E3 | After the goods enter, only goods columns change (= 4.4) | **held**. Same dataset with and without the five goods (properties.json filtered): 712 of 712 rows identical on every non-goods field (loads, families, flip directions, non-goods flips, uncounted, ranking flags, k-disagreement); top rules identical in all 27 entries. Against the e27127b baseline, 682 of 690 old rows are identical on freedom fields and 8 (mwpa-property R13 and R13~prohibit, mwpa-property-narrowed R13, k=6 and 8) differ only in `flip_directions`, which now also lists the new freedom property `financial_dependence_means` (same family, so every load and family column is unchanged). That change comes from section 5's freedom properties, not from the goods |

## Section 4

### 4.1 Base states (unablated), primary formula; identical at k=6 and k=8

| entry | good | predicted base | observed base | predicted lost > 0 (ranked) | observed lost > 0 (ranked) | gained > 0 | contested predicted / observed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| coverture-household | cared_for | stable | stable | R2 | R2 | none | no / no |
| coverture-household | mutual_household_care | stable | stable | R2, R3 | R2, R3 | none | no / no |
| coverture-household | known_carer | stable | stable | R2 | R2 | none | no / no |
| coverture-household | provided_for | stable | stable (both encoders) | R2 | R2 (both encoders) | none | yes / yes in formula, no in any reading |
| police-crisis | cared_for | stable | **fragile** | R2 | **none** | none | yes / no (both encoders guarded on `is_subject`: the named risk happened under both) |
| cps | cared_for | stable | **fragile** | none | none | none | no / no |
| cps | known_carer | stable | **fragile** | none | none | none | no / no |
| cps | child_with_family | fragile | fragile | none | none | none | yes or not_expressible / neither (equivalent) |
| kibbutz-childrens-house | cared_for | stable (carer-guarded) / fragile (child-level) | fragile (both encoders wrote child-level) | R3 (carer-guarded only) | none | none | yes / no |
| kibbutz-childrens-house | known_carer | stable | **fragile** | R3, R2 | **none** | none | yes / no |
| kibbutz-childrens-house | child_with_family | absent | **fragile** | none | none | **none** (R4 predicted) | no / no |
| ectogenesis | cared_for, known_carer, child_with_family | stable | **fragile** (all three) | R4~prohibit | **R1~prohibit** (fragile > absent) | none | yes / no |

Why fragile (traces from `phil rules check --trace`, persists check): police-crisis, `withdraw(officer, subject)` (and the subject's own `leave`) clears care while `is_subject` stays (encoder 1's own note foresaw this for `leave`); cps, a subject with an open case need never receive services (R2 is a permission); kibbutz, `release(committee, metapelet)` is unregulated and drops care (section 4.1's own conditional); ectogenesis, a decanted child need never be registered to a parent, so no carer is bound (R4 is a permission and R5 binds only a registered female parent). Information rows outside the five entries: stable in airline-flight and in all nine coverture-family entries; fragile in crisis-team, companion-*, kibbutz-no-implicit, gestational-surrogacy.

### 4.2 Readings table (ranked rows; primary; k=6 and k=8 identical)

| entry | rule (tag) | predicted up / lost / reading / agreement | observed up / lost [enc-1] / lost [enc-2] / reading / agreement | |
| --- | --- | --- | --- | --- |
| coverture-household | R2 (superadditive) | 0 / 4 / constitutive / agree | 0 / 4 / 4 / constitutive / agree | held |
| coverture-household | R3 (superadditive, implicit) | 0 / 1 / constitutive / agree | 0 / 1 / 1 / constitutive / agree | held |
| coverture-household | R4 (tying) | 1 / 0 / tying / agree | 1 / 0 / 0 / tying / agree | held |
| coverture-household | R6 (rival) | 1 / 0 / tying / no row | 1 / 0 / 0 / tying / no row | held |
| coverture-household | R7 (tying) | 1 / 0 / tying / agree | 1 / 0 / 0 / tying / agree | held |
| police-crisis | R2 (superadditive) | 0 / 1 / constitutive / agree | 0 / 0 / 0 / unread | **miss** (base fragile) |
| police-crisis | R4 (rival) | 1 / 0 / tying / no row | 1 / 0 / 0 / tying / no row | held |
| cps | R10 (rival) | 1 / 0 / tying / no row | 1 / 0 / 0 / tying / no row | held |
| kibbutz-childrens-house | R2 (tying, implicit) | 1 / 1 / hard case / mismatch | 1 / 0 / 0 / tying / agree | **miss** (known_carer fragile in base) |
| kibbutz-childrens-house | R3 (superadditive) | 0 / 2 / constitutive / agree | 0 / 0 / 0 / unread | **miss** (base fragile) |
| kibbutz-childrens-house | R4 (rival) | 1 / 0 (gained 1) / tying / no row | 1 / 0 (gained 0) / 0 / tying / no row | reading held; gained missed |
| ectogenesis | R4~prohibit (superadditive) | 0 / 3 / constitutive / agree | 0 (down 1) / 0 / 0 / unread (a protection) | **miss** (base fragile) |
| ectogenesis | R5 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / 0 / tying / agree | held |
| ectogenesis | R1~prohibit (rival) | not predicted (unread) | 0 (down 1) / 3 / 3 / constitutive / no row | **unpredicted** (F2) |

Every other ranked row in the five entries is unread (protections such as police R10~prohibit and cps R8 carry only freedom_down). Totals: **11 read rows, 6 agree, 0 mismatch, 5 no row** (predicted 13, 8, 1, 4). Unranked rows with a reading (information): kibbutz R1 and R1~prohibit (deregulated / leaks; superadditive tag, tying reading).

Strand agreement, primary and encoder 2 identical: agree = coverture R2, R3, R4, R7; kibbutz R2; ectogenesis R5. No row = coverture R6, police R4, cps R10, kibbutz R4, ectogenesis R1~prohibit.

Expected headline ("in the care+control cluster the care strands read constitutive and the exit and standing bars read tying, except cps"): **holds for coverture only.** In police-crisis and cps the exit bars read tying as predicted but the care strands are unread, because the goods as written are fragile in the unablated entries; kibbutz and ectogenesis likewise. What the instrument as built can read is a must-be care duty whose good is guaranteed in the base (coverture R2, R3 and their MWPA/floor descendants; airline-flight R2). This is a statement about the formulas and the entries together: neither encoder wrote a relation-guarded form (police `responding`, kibbutz `assigned`) because the bundle's style example and the cross-entry vocabulary led both to `is_subject` (both encoders' notes say so).

### 4.3 Encoder agreement

| prediction | result |
| --- | --- |
| at least 2 of 5 goods logically non-equivalent | **miss**: 1 (`provided_for`); merge log, z3 |
| at least one rule's reading differs by encoder | **miss**: 0 (`contested_readings` 0 in every entry, scoreboard column 0) |
| coverture's readings agree across encoders | held |

Zero reading disagreement is reported as zero. It is not evidence that goods can be encoded without the encoder's picture of the good (plans/priority.md open question): two instances of one model, one bundle, one shared style example.

**Contested `provided_for`, side by side** (primary = encoder 1, maintenance only from a husband she is married to; alternative = encoder 2, maintenance from anyone who provides care). Read in 254 rows (9 coverture-family entries, k=6 and 8); the two columns differ in **0** rows.

| entry | base [enc-1] | base [enc-2] | R2 deleted [enc-1] | R2 deleted [enc-2] | other rows |
| --- | --- | --- | --- | --- | --- |
| coverture-household, coverture-household-us, mwpa-creditor-exemption, mwpa-property, mwpa-earnings, mwpa-sole-trader, mwpa-suit, mwpa-property-narrowed | stable | stable | stable > fragile (lost) | stable > fragile (lost) | unchanged in both |
| coverture-floor | stable | stable | stable (not lost) | stable (not lost) | unchanged in both (R20 deleted or prohibited: still stable, R2 provides) |

The z3 counterexample (care from someone she is not married to, no means of her own) is a state no checked trace of these entries separates within k=8: the formulas are logically different but read the same here, which the merge protocol reports as "same effect", not merged.

### 4.4 Unchanged rows

Held: no freedom column changes in any row when the goods are added (E3 above). k-disagreements 0 (goods state changes included), `inconsistent_after` 0, `uncounted` 0 (all 712 rows, both k).

### Falsifiers

| | fired? | detail |
| --- | --- | --- |
| F1 tying rule other than kibbutz R2 reads constitutive / hard case | no | in the five entries no tying-tagged ranked row carries lost > 0. Information only: airline-flight R1~prohibit (tying, unranked: leaks off-condition) reads hard case (stable > absent for cared_for and known_carer) |
| F2 ranked `may` row (permission removed or ranked prohibit) in the five entries with lost > 0, other than ectogenesis R4~prohibit | **yes** | ectogenesis R1~prohibit (`provider may start_gestation` when true, prohibited; ranked since the condition is true): lost 3, all fragile > absent. No gestation, no subject, so the goods hold only vacuously. The goods load did not sit in a must-be duty: it sat in the act that creates the subject. Same pattern, information only, in gestational-surrogacy R2~prohibit (lost 2). Whether "no subject is ever created" should count as losing the subject's goods is a design question for the council (the stable > fragile > absent order makes absent the worst state) |
| F3 coverture R3 lost 0 on mutual_household_care under both encoders | no | lost 1 under both. The faithfulness item stands: the readings table says the wife's implicit, sanctioned care duty (R3) should be redesigned, not cut, because `mutual_household_care` rests on it. Council question (ii) (does the good launder the duty) is open |
| F4 a ranked cps row with lost > 0 | no | |
| F5 police R4 reads hard case | no | police R4 lost 0 (cared_for is already fragile in the base, so the subject's exit cannot lose it) |
| F6 a freedom column changes when the goods are added | no | E3 |

## Section 5: coverture-floor and the route comparison

**Layer-1 predictions** (`check-all --no-cache`, k=6, strict):

| # | Prediction | Result |
| --- | --- | --- |
| 1 | Zero verdict changes in the 26 existing entries after the root change; diff: 0 changed, 0 removed, added only coverture-floor; gate PASS, (b) unchanged | **held**: check-all 146/146; `diff --baseline` 0 changed, 12 added (all coverture-floor), 0 removed; gate PASS, criterion (b) detail identical to the pre-change run; `scripts/drop_one_match.py` (coverture-household is a gate (b) cluster member) gives the same nine b=FAIL rows as before (coverture-household R2, R5, R6; police-crisis R2, R3, R4; cps R3, R4, R10), output identical line for line |
| 2 | coverture-floor `financial_dependence` and `financial_dependence_unpropertied` holds_to_k | **held** (blind to the floor, as stated) |
| 3 | `financial_dependence_means` violated, `financial_dependence_margin` violated (by construction) | **held** |
| 4 | In the other eight coverture-family entries `financial_dependence_means` = `financial_dependence`; `financial_dependence_margin` holds_to_k in all eight | **held** at k=6 and k=8: means = financial_dependence in all eight (holds_to_k in coverture-household, -us, mwpa-creditor-exemption; violated in mwpa-property, -earnings, -sole-trader, -suit, -property-narrowed); margin holds_to_k in all eight |
| 5 | `double_burden` unreachable_open | **held** |
| 6 | `creditor_shield` unreachable_open (by construction) | **held** (not scored) |
| 7 | Unchanged from the US base: exit and dependent exit reachable, no_standing reachable, cannot_contract holds_to_k, care_and_sanction_same_role holds_to_k, care_assigned_by_sex violated | **held** |

**Ablation predictions** (k=6 and k=8 agree: held):

| Prediction | Result |
| --- | --- |
| Tops {R4, R6, R7} at load_freedom_up 1, families no_standing, cannot_exit, cannot_contract | **held** (coverture-floor and mwpa-earnings) |
| R20 deleted: deregulated, not ranked; freedom_down 1 (financial_dependence via means and margin); lost 0 | **held** |
| R20~prohibit: ranked, freedom_down 1, up 0, lost 0 (a protection, unread) | **held** |
| R2: lost 3 in F (not provided_for); lost 4 in T | **held** under both encoders |
| R3: lost 1 in both | **held** |
| R1 and R5 unranked in both | **held** (F: R1 deregulated, R1~prohibit and R5~prohibit leak, R5 deregulated; T: R5, R5~prohibit) |
| Confound check: R2 to R7 rows identical in coverture-household-us and mwpa-creditor-exemption | **held**: every R2 to R7 row (and R5~prohibit) identical on up, down, families, lost, goods families, per-encoder loads and ranking flags. No clean title variant is needed |

**Route comparison** (T = mwpa-earnings, F = coverture-floor; per encoder; k=6 and k=8 identical):

| quantity | T (title) | F (floor) | predicted |
| --- | --- | --- | --- |
| N (ranked base rules with up > 0) | 3: R4 no_standing, R6 cannot_exit, R7 cannot_contract | 3: same rules, same families | 3 = 3 (tie) |
| G (sum of lost over base rules), encoder 1 | 5 (R2 4, R3 1) | 4 (R2 3, R3 1) | 5 > 4 |
| G, encoder 2 | 5 | 4 | (same) |
| C (`financial_dependence_margin`) | holds_to_k | violated | holds_to_k / violated |
| R (route rules with a financial_dependence-family flip, any row) | **1**: R14 | 1: R20 | **2** (R13, R14) / 1 |

Winner rule: lower N, then lower G. N ties; G is lower for F under both encoders: **the floor route leaves fewer goods resting on a base strand**, and the difference is exactly `provided_for` on R2. Preregistered consequence (section 5, "tie as predicted"; the "R2 still carries provided_for in F" branch does not apply, since R2 does not carry it in F under either encoder): T1 stays a hypothesis; slice 4 receives two preregistered must-go-together candidates, {R2, R20} for `provided_for` in F and {R4, R6, R7} in both end states. The two stated limits hold: R1, the title route's one cut, is invisible to N (deregulated `may`, no freedom formula reads the husband's management), and the per-state top load is 1 along both routes, so path flatness separates nothing. This fits T1's reason for a floor (survival not depending on being chosen) and says nothing about floor *first*.

## Pass test (section 1)

1. **Met in form.** Five goods in properties.yaml, `encoders: [encoder-1, encoder-2]`, both transcripts audited with no breach (merge log). Caveat carried into the verdict: the two encoders are the same model given the same bundle, so "independent" means protocol-independent, not independent pictures of the good. Second encoder: agent, not someone living under the institution (ADR 0012).
2. **Met.** The one non-equivalent pair (`provided_for`) is kept: encoder 1 in `formal`, encoder 2 in `contested` with the merge-log note; evaluated in its own columns in every run (`provided_for@encoder-2`), never pooled.
3. **Met.** Readings table at k=6 and k=8 for all five entries, per encoder (`phil rules ablate --readings`); uncounted 0, inconsistent_after 0, k-disagreements 0, all listed; strand agreement tabulated above.
4. **Met.** coverture-floor encoded as section 5 states (deviation (a)/(b) and the superadditive placeholder recorded in R20's `choices`); all seven layer-1 and all ablation predictions compared; N, G, C, R computed and the consequence stated.
5. **Met** for this file, the dataset (property `history`, coverture-floor notes and card) and the commit messages.

Verdict: **passed with disclosures**: the misses above are results (no threshold was asserted); the same-model caveat limits what pass item 1 shows; F2 fired through the vacuity route, which the goods-state order itself produces. Per section 7, nothing here is called a result until the faithfulness seat (back-translation, the R3 laundering question, R20 against the glossary's "material floor", the transcript audit) and the coverture-floor card seat have run and their findings are answered.

## Drift (recorded, nothing edited in the preregistration)

1. **Section 6 names `rules_ablate.UNFREEDOM`**: revision 5 (engine e27127b) replaced it with `Property.kind` plus a loader-required `polarity: unfreedom`. Adapted as instructed: `polarity: Literal["unfreedom", "good"]`, goods require `polarity: good`; freedom direction unchanged. A note, not a prediction edit.
2. **`Property.entries` (not in section 6).** `child_with_family` is written one disjunct per entry, so it names a fluent every entry lacks; under the existing applicability rule (every fluent declared) it would be read nowhere. The engine now treats a property as applicable in the entries it lists (section 3's "entries" column, copied from encoder 1) even with undeclared fluents (lowered as false, warned), and by the old rule elsewhere.
3. **`load_goods_by_encoder` semantics (ASSUMED).** For an encoder other than the primary, the load uses its alternative where it wrote a contested one and the primary elsewhere (an equivalent formula is read through the primary).
4. **Undecided vacuity is uncounted (ASSUMED).** A persists whose antecedent z3 could not decide is neither stable nor absent. Never occurred (uncounted 0).
5. **k-disagreement now includes goods state changes** that differ by k, also when the verdict string is unchanged (persists to persists, vacuity changed). None occurred.
6. **Scoreboard header** (`goods_rows`, `contested_readings`) changed in this repo's commit 725c63d, not "in the same commit as the engine": the engine (a16691b) and the scoreboard file live in different repositories. Old rows carry "-".
7. **`--readings` writes markdown** and includes unranked rows (column `ranked`) and rows whose only change is a goods state, so the table also carries the information rows.
8. **R(T) = 1, predicted 2.** In mwpa-earnings, deleting R13 flips no financial_dependence-family property: a wage-earning wife with R14 keeps `financial_dependence` and `financial_dependence_means` violated, and the margin and unpropertied forms do not read property. R does not decide the comparison.
9. **E2 test counts**: 577 + 2 skipped before the dataset sync, 580 + 2 after; this repo 31 then 32.
10. **The baseline** (`data/verdicts-baseline.json`) was regenerated after the run: 146 rows, the 12 added rows are exactly coverture-floor's preregistered expectations (0 removed, 0 changed; engine_hash unchanged). Only preregistered added rows entered it.
11. Not run here: the council (section 7 step 8). The provenance migration report (data/institutions/provenance-migration-report.md) is a dated 2026-11-05 snapshot and was not regenerated; `migrate_provenance.py` reruns as a no-op with R20 present (129 own rules).

## Reproduction

`cd computational-liberation && uv run phil rules ablate --k 6,8 --workers 4 --json ablate-27-s2.json --summary ablate-27-s2-summary.json --readings readings-27-s2.md --prev base-e27127b-summary.json --scoreboard docs/scoreboard-ablate.md` (base-e27127b: the revision-5 engine on the 26-entry dataset, run first for E1). Scoreboard row: `2026-11-06 | c69aaf1 | rules ablate | 27 | 356 | 0 | 0 | 0 | 1 | 24 | 0` (top_rule_changes 1 = coverture-floor, new). E3 isolation: the same command with `--properties` set to properties.json minus the five goods. Layer 1: `build.py --check` ok (27 institutions, 33 properties, 28 cards); `pytest -q` 32 passed; `check-all --no-cache` 146/146; `diff --baseline` 0 changed, 12 added, 0 removed (before the baseline update); `gate` PASS. Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/slice2/run/`, not kept.

## Revision 2

Status: run 2026-11-06. Preregistration: plans/priority-slice2.md "Revision 2" (cf29916); nothing in it was edited. Engine: philosophy-engine a4ea4b3 (R2.1, R2.2) + a87cb2e (D1 sync) + 7a67c21 (D2/D3 sync) = **ENGINE_PIN 7a67c21**. Dataset: computational-liberation e519609 (D1: `subject` on the five goods), 28b4528 (D2: `chosen_mutual_care`), then the R2.5 fix pass (D3: coverture-floor R20 `strand: null` and its label, card goods notes) in the commit that adds this section. Merge inputs for the new good: data/institutions/goods-encoding/merge-log.md "Revision 2" and `r2/` (68d8eb2; bundle2 hash `7962473270d59000b21a0a5afae434725e1946d9d19e292e5d9cc5fbad93a5da`).

**Second encoder: agent, not someone living under the institution (ADR 0012).** The revision-2 encoders are two fresh instances of one model given one bundle; agreement between them measures that model's consistency, not agreement between people.

All quantities are statements about encodings (ADR 0011); `coverture-floor` is a counterfactual (ADR 0004). Builder only: the revision-2 council (R2.6 step 8: correctness and faithfulness seats) has not run, so nothing here is yet called a result in that sense.

How to read the goods columns (wording revised in the fix pass after the revision-2 council). Two measures, never combined: **guaranteed** (the rules as obeyed force the good: every strictly compliant trace within k has it at every witness step; state stable; the force may come from a duty, from a prohibition of what breaks it, or from a vocabulary in which nothing unsets the fluent) and **possible** (the good can hold under the rules as obeyed, within k, at one witness step, for some bearer in some starting world: fragile or stable; not continuity, and blind to a bearer class for whom it is impossible while it stays possible for another). **Fragile** = holds somewhere, fails somewhere (not "a held good lapses"). Every "constitutive" (possible-lost) row so far is a **prohibition of the care act** itself, labelled so in the readings output; it is not evidence of a constitutive bundle in the glossary's sense. For `chosen_mutual_care` the guaranteed column is **not meaningful** (a good defined as freely given cannot be "forced"; see "The chosen-care good"). Definitions: docs/glossary.md "Goods measures (slice 2)". Lost counts are counts of goods formulas (families); each is followed by the number of distinct strands the lost formulas read, and no count is read as "goods lost". **Strict-compliance caveat, applying to every coverture-family goods row below:** under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented.

### Headline

- **Every R2.4 prediction about the 13 rows, the base states, the n/a rows, kibbutz, ectogenesis, the new good and the route comparison held**, at k=6 and k=8, under both encoders. No falsifier (RF1 to RF9) fired.
- Possible column: no single deletion makes a coverture good impossible; deleting the exit bar (R6) moves `chosen_mutual_care` absent > fragile, in all nine coverture-family entries and in no other row (her care duty R3 still binds in that row and the formula cannot see it: not "chosen care becomes possible"; fix pass); in ectogenesis, prohibiting the parent's permission to care (R4~prohibit) makes care impossible (constitutive, 3 formulas, 1 strand: a prohibition of the care act itself, under strict compliance). Guaranteed column: as revision 1 with "constitutive" renamed "guarantee-carrying".
- The no-subject artefact is gone: ectogenesis R1~prohibit, gestational-surrogacy R2~prohibit and airline-flight R1~prohibit read `not_applicable` after, lost 0 under both measures (revision-1 F2 does not fire).
- **Misses (drift, recorded):** scoreboard `goods_rows` 34, predicted 33 (an unpredicted information row, cps R2~prohibit, possible lost 2); E4r2's "agreement cell untagged" (the R20 rows have no reading, so their cell reads `unread`, and neither row is printed in the readings table); one iso distance at `exact+strands` changes for an unclaimed pair. Details under Drift.
- **Pass test (R2.6): met** as a builder's verdict, pending the council.

### E-style predictions

| # | Prediction | Result |
| --- | --- | --- |
| E1r2 | D1 (revision-1 dataset + five `subject` keys): every non-goods field of all 712 rows identical to revision 1; guaranteed transition equal to revision 1's stable/not-stable transition except in the three n/a rows; every revision-1 `absent` cell reads `not_applicable`; `load_goods_guaranteed` = revision-1 `load_goods` except those three rows (3, 2, 2 > 0); persists verdicts and goods flips unchanged | **held**. 712 rows compared field by field: 0 non-goods differences (loads, families, flip directions, non-goods and goods flips, uncounted, ranking flags, inconsistent_after, k-disagreements); 0 guaranteed-transition differences; the n/a cells are exactly airline-flight R1~prohibit, ectogenesis R1~prohibit, gestational-surrogacy R2~prohibit (k=6 and 8), each revision-1 `absent` now `not_applicable`; `load_goods_guaranteed` (primary and both encoders) equals revision-1 `load_goods` in every other row, and is 0 in those three (revision 1: 2, 3, 2) |
| E2r2 | `pytest -q` passes in both repositories; check-all 146/146; `diff --baseline` 0/0/0; gate PASS, (b) detail and `scripts/drop_one_match.py` identical | **held** on D1 and again on D3. Engine 609 passed, 2 skipped (live LLM); this repo 32 passed (the dataset test updated for six goods, see drift 6); check-all --no-cache 146/146; diff 0 changed, 0 added, 0 removed; gate PASS (D1 and D3), and on D3 the full gate output is identical to the revision-1 run's line for line; drop_one_match output identical (D1 and D3) |
| E3r2 | D2 = D1 + `chosen_mutual_care`: every field of every other property identical; only the new good's states and the loads it enters change, i.e. the R6 rows of the nine coverture-family entries (possible gained 1) | **held**. D1 vs D2 runs: 0 differences other than `chosen_mutual_care`'s own states and families; it changes state in exactly 18 rows (R6, nine entries, k=6 and 8), absent > fragile, possible gained 1, guaranteed gained 0 |
| E4r2 | R20 `strand: null` changes only the `strand` field of coverture-floor R20 and R20~prohibit (agreement cell "untagged"; both rows unread); no verdict, gate or iso result changes | **held in the ablation** (D2 vs D3 runs: exactly 4 differences, `strand` of R20 and R20~prohibit at k=6 and 8; no verdict changes; gate output identical). Two details differ from the wording (drift 2, 3): the agreement cell of an unread row is `unread`, and `phil rules iso --all --with-strands` changes one unclaimed distance |

### Base states (unablated; primary and encoder 2 identical; k=6 and k=8 identical)

| entry | good | predicted | observed |
| --- | --- | --- | --- |
| nine coverture-family entries | cared_for, mutual_household_care, known_carer, provided_for (both encoders) | stable | stable (formula limit: three of `provided_for`'s four disjuncts are power fluents) |
| nine coverture-family entries | chosen_mutual_care (both encoders) | absent | absent |
| police-crisis | cared_for, known_carer | fragile | fragile |
| cps | cared_for, known_carer, child_with_family | fragile (medium) | fragile (formula limit: the cps disjunct of `child_with_family` is freedom-shaped; `provides_care` is the caseworker's services) |
| kibbutz-childrens-house | cared_for, known_carer | fragile | fragile |
| kibbutz-childrens-house | child_with_family | absent | absent (formula limit: `child_with_family` is three goods under one name; here only its sleep-at-home disjunct can hold) |
| ectogenesis | cared_for, known_carer, child_with_family | fragile (medium-high) | fragile |
| airline-flight | cared_for, known_carer | stable | stable |
| gestational-surrogacy, crisis-team, companion-*, kibbutz-no-implicit | cared_for, known_carer | fragile (medium) | fragile |

No base cell reads `not_applicable`; no cell is uncounted (no `no_witness_within_k` or any other reason) at k=6 or 8: **held**.

For police-crisis, cps, kibbutz-childrens-house and ectogenesis: as encoded, no rule guarantees these goods, so the guaranteed column cannot read their care strands. This is not a finding that care is fragile in those institutions (faithfulness review finding 5).

### The 13 preregistered rows (k=6 and k=8 identical; encoder 2 identical to encoder 1)

Columns per measure: up / lost / reading / agreement. Coverture rows carry the strict-compliance caveat above.

| entry | rule (tag) | guaranteed, predicted | guaranteed, observed | possible, predicted | possible, observed | |
| --- | --- | --- | --- | --- | --- | --- |
| coverture-household | R2 (superadditive) | 0 / 4 / guarantee-carrying / agree | 0 / 4 (1 strand, `provides_care(h, w)`) / guarantee-carrying / agree | 0 / 0 / unread | 0 / 0 / unread | held |
| coverture-household | R3 (superadditive, implicit) | 0 / 1 / guarantee-carrying / agree | 0 / 1 (1 strand, `provides_care(w, h)`) / guarantee-carrying / agree | 0 / 0 / unread | 0 / 0 / unread | held. Guaranteed only by R3, an implicit sanctioned duty; deleting it removes the guarantee of the husband's receipt of household labour (a good for the party who holds the sanction); not advice to keep it. Under possible, R3 is not constitutive |
| coverture-household | R4 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| coverture-household | R6 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | 1 / 0 / tying / no row; possible gained 1 | 1 / 0 / tying / no row; possible gained 1 (chosen_mutual_care absent > fragile) | held. R3 still binds her in this row; the good's formula cannot see the duty (fix pass) |
| coverture-household | R7 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| police-crisis | R2 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | held (revision-1 miss stands: as encoded no rule guarantees the goods and none makes them impossible) |
| police-crisis | R4 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | same | same | held |
| cps | R10 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | same | same | held |
| kibbutz-childrens-house | R2 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | same | same | held (section 4.2's hard case still missed) |
| kibbutz-childrens-house | R3 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | held |
| kibbutz-childrens-house | R4 (rival) | 1 / 0 / tying / no row; gained 0 | 1 / 0 / tying / no row; gained 0 | 1 / 0 / tying / no row; possible gained 1 | 1 / 0 / tying / no row; possible gained 1 (child_with_family absent > fragile) | held: section 4.2's "gained 1" now holds, under possible. Formula limit: `child_with_family` is three goods under one name; here it reads its sleep-at-home disjunct alone (the cps and ectogenesis disjuncts lower false in kibbutz) |
| ectogenesis | R4~prohibit (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 3 / constitutive / agree | 0 / 3 (1 strand, `provides_care(intended_parent, child)`) / constitutive / agree | held: section 4.2 holds under possible. Label: prohibition of the care act (the "agree" is by construction: the goods read `provides_care`, the row forbids it). Strict-compliance caveat: the impossibility also rests on strict compliance pruning the traces where R5's `must provide_care` meets the prohibit |
| ectogenesis | R5 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | same | same | held |

Totals, five entries (primary; encoder 2 identical): guaranteed **10 read rows, 6 agree, 0 mismatch, 4 no row** (predicted the same); possible **9 read rows, 5 agree, 0 mismatch, 4 no row** (predicted the same). Every other ranked row in the five entries is unread under both measures: held.

### n/a rows, kibbutz, information rows

- Rows with an n/a move (`goods_not_applicable_rows`), exactly the three predicted: ectogenesis R1~prohibit (cared_for, known_carer, child_with_family fragile > n/a; lost 0 under both; unread under both; down 1, a protection), gestational-surrogacy R2~prohibit (cared_for, known_carer fragile > n/a; lost 0), airline-flight R1~prohibit (stable > n/a; lost 0; up 1, so tying; unranked). **Held.** Revision-1 F2 reapplied to both measures does not fire.
- gestational-surrogacy R4~prohibit (information): cared_for, known_carer fragile > absent, possible lost 2 (1 strand), constitutive (label: prohibition of the care act; strict compliance as ectogenesis): **held**.
- Kibbutz: child_with_family base absent; R4 deleted absent > fragile, possible gained 1, guaranteed gained 0; no other row moves it; R3 deleted no goods change: **held**. Formula limit: the reading rests on the sleep-at-home disjunct alone (the cps and ectogenesis disjuncts lower false here, as `entries` allows).
- **Unpredicted information row:** cps R2~prohibit (the caseworker's `may provide_services` when a case is open, prohibited; not ranked: the prohibit leaks off-condition): cared_for, known_carer fragile > absent, possible lost 2 (1 strand: `provides_care(social_worker, child)`, which in the cps vocabulary is the caseworker's services), constitutive (label: prohibition of the care act). The leak off-condition is beside the point: before a case opens no bearer exists, so services then reach no subject (correctness review finding 5). Formula limit for the cps rows: `child_with_family`'s cps disjunct ("case open, not in custody, a parent exists") is freedom-shaped, and no cps fluent records parental care. Revision 1 could not see it (fragile > fragile under the old states). It is not ranked, so it is not in `constitutive` and RF9 does not reach it; it is the one extra `goods_rows` row (drift 1).
- companion-ownership and companion-guardian-renamed R1~prohibit: guaranteed gained 2 (1 strand) each, as in revision 1.

### The chosen-care good

| prediction | result |
| --- | --- |
| base absent in all nine coverture-family entries, both encoders | held |
| R6 deleted: absent > fragile, possible gained 1, guaranteed unchanged, in all nine | held (18 rows, k=6 and 8) |
| R5 and R5~prohibit unranked and move nothing | held |
| R3, R2, R4, R7, R1 and the route rules: absent > absent | held (no row other than R6 changes it) |
| no rule carries the good: lost 0 everywhere under both measures; R3 lost 0 on it | held. R3's lost 0 here carries no information about R3: the good is absent before and after (fix pass) |
| encoder agreement: same effect in every row, `contested_readings` 0, no `not_expressible` | held. The merged formulas are z3-equivalent (`contested: []`), so encoder 2's column is the primary's; neither encoder recorded `not_expressible` (merge log) |

The {R5, R6} pair (sanction and exit together) is a slice-4 question and is not read here.

Fix-pass caveats (faithfulness review majors 1 and 2; formula unchanged):
- **Guaranteed column not meaningful for this good.** A good defined as care "she is free not to give" cannot be forced by the rules; if it read stable, some rule would compel it, so stable would be evidence of imposition, not of the good. "Guaranteed unchanged" above is correct as a number and is not a reading. Marked on the property (`measure_note` in properties.yaml).
- **The no-sanction clause is idle under strict compliance.** R3's `or_else` is R5, whose condition is `misbehaves` (set by the free action `misbehave`), not her neglect; she never breaches R3 in a compliant trace, so `can_sanction` is false at nearly every married step. The gloss's claim that the reading is "stricter than the gloss" is wrong in the direction that matters: the one sanction attached to her care is invisible.
- **The preregistered R6-row rationale was wrong.** "neglect, neglect_house and misbehave stay free": `neglect` and `neglect_house` are not compliant while married (R2, R3 are must-be); `misbehave` is the only lapse route. Drift in the reasoning, not in a number.
- **With R5 and R6 removed the good reads stable, guaranteed by R2 and R3** (reviewer's probe, scratch `fr2/`: deleting R3 there reads guarantee-carrying, guaranteed lost 2, `chosen_mutual_care` and `mutual_household_care`; deleting R2, guaranteed lost 5; in the R6-only variant deleting R5 or R5~prohibit moves it fragile > stable). The formula cannot see whether her care is obliged, so obligated care reads as chosen once exit and chastisement are gone.

### Route comparison (T = mwpa-earnings, F = coverture-floor; per encoder; k=6 and k=8 identical)

| quantity | T | F | predicted | |
| --- | --- | --- | --- | --- |
| N (ranked base rules with up > 0) | 3 (R4, R6, R7) | 3 (same) | 3 = 3 | held: tie |
| G, guaranteed | 5: R2 4 formulas (1 strand, `provides_care(h, w)`), R3 1 (1 strand) | 4: R2 3 (1 strand), R3 1 (1 strand) | 5 / 4 | held; **by construction: the same margin case as C** (`provided_for` on R2 for a wife with neither property nor wages) |
| G, possible | 0 | 0 | 0 / 0 | held: tie |
| gained over base rules, possible | 1 (R6, chosen_mutual_care) | 1 (R6, chosen_mutual_care) | 1 / 1 | held |
| gained over base rules, guaranteed | 0 | 0 | 0 / 0 | held |
| C (`financial_dependence_margin`) | holds_to_k | violated | unchanged, by construction | held (check-all, diff 0 changed) |
| R | 1 (R14) | 1 (R20) | 1 / 1 | held |

Winner rule per measure: guaranteed: tie on N, F lower on G (by construction); possible: tie on N and on G. Section 5's branch "tie as predicted" applies: T1 stays a hypothesis; slice 4 keeps the candidates {R2, R20} and {R4, R6, R7}. The floor's goods advantage is about guarantee only (her income access, as `provided_for` reads it (an income she may draw), stops depending on R2 being kept), not about what is possible, and says nothing about order. Formula limit beside these rows: three of `provided_for`'s four disjuncts are power fluents (`has_own_income := enabled draw_subsistence`, an action with no effects); the floor's G advantage runs through that freedom-shaped disjunct, and no subsistence is delivered. R20 is an unconditional income-access floor for the wife, not the glossary's material floor.

### Totals

| prediction | result |
| --- | --- |
| uncounted 0 (goods reasons included), inconsistent_after 0, k-disagreements 0 | held (712 rows; goods k-disagreement read on the full state pair) |
| `goods_rows` 33 | **34** (miss: cps R2~prohibit, drift 1) |
| `contested_readings` 0, `top_rule_changes` 0 against the revision-1 summary | held |
| `constitutive` only ectogenesis and gestational-surrogacy ([R4~prohibit]); `guarantee_carrying` [R2, R3] in the nine coverture-family entries and [R2] in airline-flight; `hard_cases`, `hard_cases_guaranteed` empty | held |
| build.py --check: 27 institutions, 34 properties; cards unchanged except the R2.5 notes and R20's strand display | held, plus coverture-floor's name and summary line (drift 4) |
| run time at most twice revision 1's 7m23s | held: 8m12s (D1), 8m38s (D2), 8m20s (D3) |

Scoreboard row (docs/scoreboard-ablate.md): `2026-11-06 | 7a67c21 | rules ablate | 27 | 356 | 0 | 0 | 0 | 0 | 34 | 0`.

### Falsifiers

| | fired? | detail |
| --- | --- | --- |
| RF1 ectogenesis R1~prohibit or gestational-surrogacy R2~prohibit not n/a after, or lost > 0 | no | both n/a, lost 0 under both measures |
| RF2 kibbutz child_with_family base not absent, or R4 possible gained not 1 | no | |
| RF3 any coverture-family row with possible lost > 0 | no | R3 on mutual_household_care: possible 0 under both encoders |
| RF4 ectogenesis R4~prohibit possible lost not 3 | no | 3 |
| RF5 chosen_mutual_care base not absent somewhere, a row other than R6 changes it, or R6 does not make it possible | no | |
| RF6 any reading differs by encoder | no | 0 rows with any encoder load difference |
| RF7 guaranteed column differs from revision 1 outside the n/a rows, or any non-goods field differs | no | E1r2, E3r2 |
| RF8 any uncounted goods cell, `no_witness_within_k`, or goods k-disagreement | no | |
| RF9 a ranked row in the five entries other than ectogenesis R4~prohibit reads constitutive or hard case under possible | no | |

### Engine (R2.1, R2.2) and the mutation record

Implemented as R2.1 (philosophy-engine a4ea4b3): required `subject` on goods (and an optional one per contested alternative), loader checks (parse; per applicable entry only declared fluents, a `RulesLoadError` at CLI load and in ablation; `Ant(t) -> Subj(t)` valid with fluents uninterpreted, in the property validator); the four states from four queries in order (subject, witness, possible, guaranteed = invariant), any undecided query uncounted with its reason and never stable; two measures never combined, n/a pairs neither and listed; `load_goods` removed; alternatives chosen by name, an uncounted alternative listed for its encoder; readings per measure (`constitutive` only under possible, `guarantee-carrying` under guaranteed); strand agreement with `untagged`; goods k-disagreement on the state pair; `Strand | None`. Tests: tests/test_rules_ablate_goods.py, rewritten per R2.2 (49 tests); the revision-1 assertion pinning stable > absent for "no subject is ever enrolled" is replaced on purpose (now stable > not_applicable).

Mutations, each run in a scratch copy of the engine against tests/test_rules_ablate_goods.py + tests/test_rules_ablate.py (76 tests): **all killed**.

| mutation | killed by |
| --- | --- |
| M1 (a) fragile/absent swapped in the possible predicate | 13 tests, including the 16-pair transition table and 5d |
| M1 (b) fragile/absent labels swapped in the state queries | 9 tests, including 5a, 5b, 5d |
| M2 alternatives pooled into the primary load | test_2_alternative_flips_primary_does_not_never_pooled |
| M5 goods k-disagreement block deleted | test_3_goods_state_differing_by_k_is_a_k_disagreement_with_unchanged_verdicts |
| M6' undecided subject read as stable | test_4c_undecided_subject_query_is_uncounted_never_stable (and test_2b) |
| M8 subject from any `is_*` fluent | test_4b_the_goods_own_subject_is_read_not_any_is_fluent |
| M9 alternative chosen by encoder position | test_2a_alternative_chosen_by_name_not_by_encoder_position |

### R2.5 fix pass

- [x] Cards: a "Goods (slice 2)" section in the cards of coverture-household, police-crisis, cps, kibbutz-childrens-house, ectogenesis, coverture-household-us, mwpa-earnings and coverture-floor, from a card-only entry key `goods_note` (build.py strips it from the engine JSON and never inherits it through `extends`), giving the revision-2 readings under both measures and the ADR 0012 sentence; police-crisis, cps, kibbutz and ectogenesis say "as encoded, no rule guarantees these goods", not "care is fragile here". Written after the run.
- [x] coverture-floor R20: `plain`, `choices`, entry notes, `source_text`, entry name and card call it an unconditional income-access floor for the wife, not the glossary's material floor; `strand: null` (engine `Strand | None`, key still required, `+strands` iso treats null as its own tag), recorded in R20's `choices` and in docs/plan.md's strand-tag item.
- [x] Route comparison: G's 5-vs-4 labelled "by construction: the same margin case as C" (above and in the mwpa-earnings and coverture-floor card notes).
- [x] Per-strand counts after every lost count in this section.
- [x] Strict-compliance caveat stated once at the top of this section for every coverture-family goods row, and in the four coverture-family card notes.
- [x] Revision-1 wording carried forward (next subsection).

### Revision-1 wording, carried forward (as the reviews asked; revision-1 text above is left as recorded)

- **Pass item 1 (revision 1)**: met as protocol independence only (no contact; transcripts audited by the coordinator and re-checked by the council). Not independent pictures of the good: two instances of one model with one prompt and one bundle, sharing a style example (`care_duty_on_women`), the goods conventions (including the misdefinition of "absent" that revision 2 corrects) and an instruction to prefer shared fluents. The 4/5 equivalent formulas measure that model's consistency.
- **`provided_for`**: encoder 2's formula (maintenance from anyone who provides care) is the closer reading of the gloss ("a carer's maintenance"); encoder 1's narrows it to the husband. No reachable state in these entries separates them (0 of 254 rows in revision 1; 0 rows here).
- **Prompt disclosure (results 4.2 and 4.3)**: the revision-1 encoder prompts carried an instruction outside the hashed bundle, "prefer a formula that uses only fluents shared across them", which is one common cause, with the style example, of both encoders guarding on `is_subject` and of the police and kibbutz misses. Revision 2 put the full prompt inside the hashed bundle and dropped that instruction.

### Pass test (R2.6)

1. Engine implements R2.1 with every R2.2 test and every listed mutation killed: **met** (above).
2. `chosen_mutual_care` encoded by two audited fresh encoders from a hashed bundle that contains the prompt: **met** (coordinator's merge log "Revision 2": 12 calls each, no breach; bundle hash above). Protocol independence only (same caveat as revision 1: one model). A new shared input (fix pass, faithfulness finding 9): the gloss fixed the fluent-level reading (`can_exit`, `can_sanction`), and its author, the preregistration author, had seen the rules, the revision-1 outputs and the predictions; the encoders chose only quantifier form, so their equivalence was expected and is not evidence about the good.
3. The run produces both measures for the 13 rows, the n/a rows, the kibbutz rows, the route comparison and the new good, per encoder, at k=6 and 8, with uncounted, inconsistent_after and k-disagreements listed: **met** (all 0).
4. R2.5 checklist done: **met**.
5. Every report carries the ADR 0012 sentence: **met** (this section, the card notes, `chosen_mutual_care`'s history, the commit messages).

Fail conditions: no revision-1 formula changed (formal and contested byte-identical; only `subject` added); no contested alternative pooled or dropped; no prediction edited; the encoders were given nothing outside the bundle (merge log). Verdict: **passed** (builder), with the drift below; not called a result until the R2.6 step 8 council has run and its findings are answered. docs/claims.md: not changed (the plan changes it only on N(F) > N(T), which did not occur).

### Drift (recorded; nothing edited in the preregistration)

1. **`goods_rows` 34, predicted 33.** The extra row is cps R2~prohibit (information, not ranked: possible lost 2, fragile > absent for cared_for and known_carer). The prediction's list of goods rows did not include it. It does not touch any ranked reading, RF4 (revision 1, "a ranked cps row with lost > 0") or RF9.
2. **E4r2's agreement cell.** The R20 and R20~prohibit rows have no reading under either measure, so by R2.1's own rule ("no reading = unread") their agreement reads `unread`, not `untagged`; `untagged` appears only for a null-strand row with a reading. Neither row is printed in the readings table (up 0, no goods change).
3. **Iso output.** `phil rules iso --all --with-strands` (exact level) changes for one unclaimed pair, naming-convention ~ coverture-floor: rule distance 7 > 8, add/remove distance 8 > 10 (the strand-on match of R1 to R20 is gone); `iso` stays False. No claimed pair, gate criterion or gate line changes (gate output identical before and after).
4. **coverture-floor name and summary line** changed with the R20 label (R2.5 names `plain`, notes and card; the entry name "Coverture with a material floor" and `source_text` said the same thing, so they were relabelled too). Engine JSON changes: the entry name, `source_text` and R20's strand; nothing a check reads.
5. **Where the loader checks run.** The parse and `Ant -> Subj` checks are in the property validator (`load_properties` rejects); the per-entry declared-fluent check needs the institutions, so it runs at `phil rules` load (exit 2) and in ablation (`RulesLoadError`). Goods results no longer carry the old vacuity flags (`antecedent_reachable`, `subject_exists` are not computed for goods).
6. **This repo's dataset test** (tests/test_dataset_claims.py) pinned the five revision-1 goods; it now lists six and asserts a `subject` on each. Before that update, `pytest -q` failed once on D2/D3 for that reason only.
7. **Engine test helper**: tests/test_rules_meta.py's rename helper renamed the role `subject` inside the new `subject` key; it now restores schema field names.
8. **Persists unknown with counted states** (ASSUMED): the goods state does not read the persists verdict, so if persists alone were undecided the state would be counted and only the flip omitted. Never occurred.
9. **Scoreboard row** appended from the saved D3 run (`scoreboard_stats` on the JSON rebuilt into row objects; the rebuilt `summarize` equals the saved summary exactly), because the run was made before the engine sync commit; the engine tree it ran on (a4ea4b3 code + D3 data) is 7a67c21's.
10. **Three full runs**, not one: D1 (E1r2, also the phase-1 intermediate), D2 (E3r2), D3 (E4r2 and the reported numbers). Every table above is D3; D1 and D2 give the same numbers apart from the new good and R20's strand.
11. **The per-entry subject check is stricter than R2.1's wording** (recorded in the fix pass, correctness review minor 2(b); no code change). R2.1 asked for "the same rule as `formal`, including `entries`"; that rule would accept an undeclared fluent in a `subject` in a listed entry and lower it false, silently turning the good `not_applicable`. The engine (rules_ablate.goods_subject_errors) refuses it in every applicable entry, listed or not. No current subject names an undeclared fluent, so nothing changes.

### Reproduction

`cd computational-liberation && uv run phil rules ablate --k 6,8 --workers 4 --json ablate-27-r2.json --summary ablate-27-r2-summary.json --readings readings-27-r2.md --prev ablate-27-s2-summary.json` (the revision-1 summary), then the scoreboard row as drift 9. E1r2: the same on D1 (e519609) compared with revision 1's ablate-27-s2.json; E3r2: D1 vs D2 (28b4528); E4r2: D2 vs D3. Layer 1: `build.py --check` ok (27 institutions, 34 properties, 28 cards); `pytest -q` 32 passed; `check-all --no-cache` 146/146; `diff --baseline` 0/0/0; `gate` PASS; `scripts/drop_one_match.py` identical. Mutations: a scratch copy of the engine with one string replacement per mutation. Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/slice2/run2/`, not kept.

## Revision 2 fix pass

Status: 2026-11-06, after the revision-2 council (docs/reviews/2026-11-06-slice2-rev2-correctness-review.md: supported; docs/reviews/2026-11-06-slice2-rev2-faithfulness-review.md: weakened narrowly). No new predictions; nothing here changes a verdict, a goods state or a reading. Engine: philosophy-engine 969f1d8 (tests, loader edge, label) + c53d132 (data sync) = **ENGINE_PIN c53d132**. Wording in the "Revision 2" section above was revised in place where listed below (numbers untouched); everything else there stands as recorded.

**Second encoder: agent, not someone living under the institution (ADR 0012).**

### Findings and what was done

| finding | done / how |
| --- | --- |
| Correctness 1: M10, M11, M12 survive (undecided guaranteed read as stable; undecided possible read as absent; no witness read as absent) | **done.** tests/test_rules_ablate_goods.py test_4e, test_4f (a fixture making only the n-th goods query unknown) and test_4g (a tiny entry where the bearer exists but no witness step does). Each mutant run in its own scratch copy against the goods and ablate tests (81): control 81 passed; M10, M11, M12 each fail exactly their test (1 failed, 80 passed). |
| Correctness 2(a): `subject` with a free step variable raises a raw z3 Sort mismatch | **done.** The property validator turns it into a load error ("does not type-check ... only t may be free"): `RulesLoadError`, exit 2 (test_4h). |
| Correctness 2(b): per-entry subject check stricter than R2.1's wording | **recorded**, no code change: drift 11 of "Revision 2". |
| Correctness 2(c): only `Ant -> Subj` is checked; an over-broad subject passes | recorded here; no dataset subject is over-broad. Not changed. |
| Correctness 3: `possible` needs the whole formula at one step | **documented** as a known limit in `rules_checks.goods_queries`' docstring and here: a good written over several bearer roles whose goods hold at different steps would read absent. Every dataset good has one bearer role, one agent per role. |
| Correctness 4 / faithfulness: strict-compliance caveat on ectogenesis R4~prohibit (and cps R2~prohibit) | **done** in the 13-rows table, the information rows and the ectogenesis card. |
| Faithfulness 1-2: `chosen_mutual_care` | **done, formula unchanged.** Guaranteed column marked not meaningful for this good (results "The chosen-care good", fix-pass caveats; `measure_note` on the property in properties.yaml, a free-text key the engine ignores, like `history`; card notes). Recorded: the no-sanction clause is idle under strict compliance; the preregistered R6-row rationale ("neglect stays free") was wrong (`misbehave` is the only lapse route); with R5 and R6 removed the good reads guaranteed by R2 and R3 (reviewer's probe). Headline and R6 row reworded: R6's deletion moves the good absent > fragile while R3 still binds; not "chosen care becomes possible". |
| Faithfulness 3: "constitutive" marks only prohibitions of the care act | **done.** Label-only engine change: `possible_lost_label` = "prohibition of the care act" when a `~prohibit` row prohibits an action that sets a fluent in the consequent of a possible-lost good; printed beside the reading in the readings table (`constitutive (prohibition of the care act)`), listed in the summary's `constitutive_labels`; no count, load, reading or agreement reads it (test_5d, test_5f). In the rerun it labels exactly the possible-lost rows so far: ectogenesis R4~prohibit, gestational-surrogacy R4~prohibit, cps R2~prohibit. Also in the results rows, the "how to read" paragraph, the ectogenesis and cps cards. Possible agreement on ectogenesis R4~prohibit is by construction. |
| Faithfulness 4-5: definitions worded too strongly; possible is existential | **done**: "how to read" paragraph: guaranteed = the rules as obeyed force it; possible = can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world; fragile = holds somewhere, fails somewhere. Same wording in the eight card notes and docs/glossary.md. |
| Faithfulness 6: R3 row lost the "husband's receipt" clause; R3 lost 0 on the chosen good cited as evidence | **done**: clause restored in the R3 row and the four coverture-family card notes; the chosen-care table says R3's lost 0 there carries no information. |
| Faithfulness 7: "her provision stops depending on R2" | **done**: "her income access, as `provided_for` reads it (an income she may draw), stops depending on R2", with the power-fluent limit beside the route rows and in the coverture-floor card. |
| Faithfulness 8: formula limits of `child_with_family` and `provided_for` not beside their rows | **done**: base-states table, the kibbutz R4 row, the kibbutz and cps information bullets, the route paragraph; kibbutz, cps and coverture-floor cards. |
| Faithfulness 9: the gloss chose the fluents (undisclosed shared input) | **done**: pass item 2 now reads protocol independence only, plus the new shared input (the gloss fixed `can_exit`, `can_sanction`; its author had seen the rules and predictions; equivalence expected, not evidence about the good). |
| Glossary: no entries for the measures and reading words | **done**: docs/glossary.md "Goods measures (slice 2)": guaranteed, possible, guarantee-carrying, not applicable, fragile, and constitutive (reading) distinguished from constitutive bundle; one dataset example each. |
| Open since revision 1 (6(i)): undeclared fluent in a listed entry lowers false with a warning | **skipped (recorded).** Making it a load error in a listed entry would change current rows: `child_with_family` lists cps, kibbutz-childrens-house and ectogenesis, and names undeclared fluents in all three (cps: `at_home`; kibbutz: `parent`, `case_open`, `in_custody`; ectogenesis: `at_home`, `case_open`, `in_custody`), so the good would fail to load there. The design of the three-goods-under-one-name formula depends on this lowering. Stays a warning; the kibbutz reading rests on it (formula limit, above). |

### What can be reported now

Each as a statement about encodings under strict compliance, within k = 6 and 8 (mirrors the faithfulness review). All of revision 1's "can report now" list stands, plus:

- **Guaranteed column.** In the nine coverture-family entries, R2 and R3 are the only guarantee-carrying rules (R2: 4 formulas, 1 strand; R3: 1 formula, 1 strand). The R3 row carries: guaranteed only by R3, an implicit sanctioned duty; deleting it removes the guarantee of the husband's receipt of household labour; not advice to keep it.
- **Possible column.** No single deletion makes any encoded coverture good impossible. In ectogenesis (and gestational-surrogacy), prohibiting the parent's care act makes care impossible: a prohibition of care itself, not evidence of a constitutive bundle. In kibbutz, the children's house rule R4 makes `child_with_family` (its sleep-at-home disjunct) impossible, and deleting it makes that possible.
- **No-subject rows.** Ectogenesis R1~prohibit and its two siblings are not applicable: no bearer exists, so nothing is lost.
- **`chosen_mutual_care`.** Under coverture as encoded, no compliant trace has mutual care while the wife has a permitted way out. The exit bar R6 is the only single rule whose deletion changes that; her care duty R3 still binds in that row, and the formula cannot see it.
- **Route comparison.** Tie on N and on G possible. G guaranteed 5 vs 4 is by construction (the margin case) and runs through income access. T1 stays a hypothesis.
- **Encoder agreement on the new good.** Protocol independence, audited. Equivalence was expected because the gloss fixed the fluents.

### Not yet reportable

- Any slice-4 use of `chosen_mutual_care` (the {R5, R6} pair reads obligated care as chosen and guaranteed); "chosen care becomes possible"; any guaranteed reading of this good.
- "Constitutive" without the prohibition-of-the-care-act caveat.
- Either measure in the glossary's sense beyond the definitions now in docs/glossary.md (guaranteed is not "a rule protects the good"; possible is not "the good is available to everyone").

### Rerun against revision 2 (no verdict, goods state or reading changed)

- **Ablation** (`uv run phil rules ablate --k 6,8 --workers 4 --json --summary --readings --prev <revision-1 summary>` on ENGINE_PIN c53d132, 8m34s), compared with the revision-2 run (`run2/ablate-27-r2*`): JSON and summary identical once the label fields (`possible_lost_label` per row, `constitutive_labels` per entry) are removed; readings table identical once the suffix " (prohibition of the care act)" is removed (12 labelled cells: ectogenesis and gestational-surrogacy R4~prohibit, cps R2~prohibit, k=6 and 8, both encoders); the text report identical apart from its own output paths. The label is set on exactly those six rows (k=6, 8) and on no other.
- **Layer 1**: `build.py --check` ok (27 institutions, 34 properties, 28 cards; institutions.json unchanged, properties.json gains only `measure_note`); `pytest -q` 32 passed; `check-all --no-cache` 146/146; `diff --baseline` 0 changed, 0 added, 0 removed; `gate` PASS, output identical to the revision-2 run line for line; `scripts/drop_one_match.py` identical. Engine suite 614 passed, 2 skipped (609 + test_4e, 4f, 4g, 4h, 5f).
- Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/fixpass/` (mutation record `mutations.txt`, comparison `cmp_fp.py`), not kept. No scoreboard row appended (no new numbers).

## Revision 3

Status: 2026-11-06. Revision 3 as preregistered in plans/priority-slice2.md "Revision 3" (8e512f3), R3.6 steps 3 to 7: the primary measure (D4), the derived `obliged` and `care_obliged` (D5), the re-glossed and re-encoded `chosen_mutual_care` (D6), and the blind-gloss experiment against D6. Step 8 (council) is still to come; nothing below is called a result until its findings are answered. Engine: philosophy-engine 42df8af (R3.1, R3.2) + data syncs 0472661 (D4), 605cff4 (D5), 7859726 (D6) = **ENGINE_PIN 7859726** (the D6 sync changes data only; engine code is 42df8af's). Every quantity is a statement about encodings (ADR 0011), strict compliance, k = 6 and 8.

**Second encoder: agent, not someone living under the institution (ADR 0012).** All encoders in this revision (the two dataset encoders and the two blind encoders) are fresh Claude agents: their agreement measures one model's consistency, not agreement across models or between people. The non-Claude encoder was **not run** (no API key); its prompt is inside bundle3x's hash (merge log "Revision 3: encoders").

### Headline

- **`chosen_mutual_care`, obliged version (D6).** The re-gloss author chose variant **B, E+** (both spouses' obliged care excluded; exit and no-sanction kept). Both dataset encoders wrote z3-equivalent formulas that add `(not (care_obliged h w t))` and `(not (care_obliged w h t))` to revision 2's. As encoded, the good is **absent in the base of all nine coverture-family entries and in every single-deletion row**: R6's row is now absent > absent (revision 2: absent > fragile), because R2 and R3 still oblige care there. No single rule moves it; scoreboard `goods_rows` 34 > 25. Probes on coverture-household (and, as extra information, the other three listed entries): with R5 and R6 deleted it reads **absent** (revision 2's formula: stable, obliged care read as chosen; the laundering is gone); with R3 and R6 deleted, absent (R2 still obliges him); with R2, R3 and R6 deleted, **fragile**, and also with R5 deleted. It is never stable. Every R3.5 prediction for variant B held; no RF3 falsifier fired (RF3.3: the two O5 pins as typed fire, a preregistration error with the engine correct; they hold as rewritten, drift 10). *Fix pass:* the base absence is by construction (R2 and R3 oblige care at every married step); R2, R3 and R6 each bar the good on their own; it becomes possible, at one step, with all three deleted even though R5 (the husband's chastisement power) remains, because the no-sanction clause reads only an enabled power ("Revision 3 fix pass").
- **Blind-gloss experiment.** With glosses written from theory.md and intent.md only, two fresh Claude encoders agree (z3) on 1 of 6 goods (`mutual_household_care`), and **none** of the twelve blind formulas is z3-equivalent to the dataset's. Run against D6 at k = 6 and 8: 41 (entry, good) base states differ between some two of the three columns; three of the 13 preregistered rows read differently (coverture-household R2: carrying (guaranteed) > carrying (possible); R3: unread > carrying (possible); ectogenesis R4~prohibit: blind-1 unread); 3 ranked rows carry a contested reading between the blind encoders (revision 2: 0). One replacement candidate (`mutual_household_care`) and one conditional candidate (`cared_for`) were referred to the author, pending the faithfulness seat; none acted on. The dataset's formulas are unchanged. *Fix pass:* the council recommends replacing neither (condition 3 fails for both); the reportable headline is restated in "Revision 3 fix pass": 1 of 6 agree; ids do not fix the goods; the cause of the drop is not isolated; one model.

### D4 and D5 (R3.1, R3.2): recorded from the step-3 run

As reported in computational-liberation b24cb36 and philosophy-engine 42df8af (outputs in the session scratchpad `r3run/`, not kept): the D4 ablation is identical to the fix-pass rerun apart from the new primary fields (**E1r3 held**); every primary cell of R3.1's table, the 13-row totals (10 read, 6 agree, 0 mismatch, 4 no row) and the summary lists (`primary_carrying`, `hard_cases_primary` empty, `top_goods_rules`) came out as computed; D5 is identical to D4 in every field (**E2r3 held**). Engine tests O1 to O6 and P1 to P5 pass; mutations MP1 to MP3 and MO1 to MO6 are all killed (record in the 42df8af message); engine suite 656 passed, 2 skipped. Layer 1 on D5: build ok, pytest 38 passed, check-all 146/146, diff 0/0/0, gate PASS identical, drop-one identical. **Value call, reported as such:** under the author's measure per good, coverture R3 carries no good in any row; its only revision-2 load was a guarantee of `mutual_household_care`, which the author reads as possible-primary. *Fix pass wording:* this follows from the value call **and** the dataset's `mutual_household_care` formula, not from the value call alone: the possible measure cannot tell forced from free mutual care, so R3's imposition is not visible on the primary column ("carries no good" is not "imposes no cost on any good"); under both blind formulas R3 reads carrying (possible), a reading the faithfulness review judged unfaithful (finding 3).

### Baseline for D6: the dataset moved between D5 and D6 (drift 1)

The branch merged faithfulness batch 2 (cps R8 'would not benefit' exception with the free fluent `would_not_benefit`; P1 prose fixes) after the D5 run. R3.5's predictions were written before it. D6 is therefore compared with **D5'** = the dataset at 1c512b9 (D5 + the faithfulness batch), run on the same engine. D5' vs D5: 42 leaf differences, all in cps: R8, R11 and R11~prohibit lose their freedom load (`no_standing` open > reachable, freedom_down, at k = 6 and 8; load_freedom 1 > 0). No goods field, summary list or readings-table line differs. None of R3.5's rows is a cps row except cps R10 (tying, no row) and cps R2~prohibit (unranked), both unchanged. So the faithfulness batch moves no revision-3 prediction; its own effect is recorded here as drift with its cause, not as a failed prediction.

### D6 (R3.4, R3.5): `chosen_mutual_care` replaced

**Dataset entry.** `gloss`: the re-gloss author's, verbatim (r3/regloss.yaml). `formal` and `subject`: 3d encoder 1 (primary). `contested: []` (merge: formal equivalent, universal vs negated existential over the sanctioning agent; subject identical). `encoders: [encoder-1, encoder-2]` as the revision-3 dataset encoders, with bundle3d's hash and the merge-log section in `history`. Revision 2's gloss, formal, subject, `measure_note` and `history` moved verbatim into `history`. `measure_note` rewritten (guaranteed column still not meaningful; the obligation is now visible; the re-gloss author's note that a general spousal duty of mutual support would also make the good unattainable, since the fluent cannot say which rule obliges). `primary_measure: possible` and its reason kept. No other property changed (the five revision-1 goods' `formal`, `subject` and `contested` are byte-identical).

**Variant.** The re-gloss author's answers: `excludes_obliged_care_of: both`, `exit_condition: true`, `no_sanction_condition: true`, i.e. **B (E+)**, one of the preregistered variants.

**Run.** `phil rules ablate --k 6,8` on all 27 entries (8m18s), compared with D5' leaf by leaf: 270 leaf differences, all in the R6 row of the nine coverture-family entries (30 fields each: `chosen_mutual_care` absent > fragile becomes absent > absent; possible and primary gained 1 > 0, both encoders, both k). Summary identical to D5'. Readings table: only those R6 rows' goods columns.

| row (nine coverture-family entries) | R3.5 prediction, B | D6 result | held |
| --- | --- | --- | --- |
| base | absent (R2 and R3) | absent in all nine, k = 6 and 8 | yes |
| R6 deleted | absent > absent | absent > absent (D5': absent > fragile) | yes |
| R3 deleted | absent > absent (R2 still obliges him) | absent > absent | yes |
| R2, R4, R5, R7, R1, R5~prohibit, R1~prohibit, route rules | absent > absent | absent > absent (no row moves the good) | yes |
| `top_goods_rules`, `primary_carrying` | unchanged from D4 | unchanged (summary identical to D5') | yes |
| scoreboard `goods_rows` | 34 > 25 | **25** | yes |
| encoders | same states in every row (high); z3-equivalent (medium) | same states in every row; z3-equivalent (merge) | yes |
| guaranteed column | never stable | never stable | yes |

**Probes** (base goods state of `chosen_mutual_care` in a scratch copy of coverture-household minus the set, rebuilt with the engine's `without_rule`; information, not ablation rows, not slice 4; k = 6 and 8 identical). Revision 2's formula is evaluated beside it as a control, and the same probes were run on coverture-household-us, mwpa-earnings and coverture-floor (identical results in all four).

| deleted set | R3.5 prediction, B | D6 formula | revision-2 formula (control) | held |
| --- | --- | --- | --- | --- |
| {R5, R6} | absent | **absent** | stable | yes (RF3.5 not fired: the laundering is gone) |
| {R3, R6} | absent (R2) | absent | fragile | yes |
| {R2, R3, R6} | fragile | **fragile** | fragile | yes (RF3.7 not fired) |
| {R2, R3, R5, R6} | fragile | fragile | fragile | yes |
| {R6} (as the ablation row) | absent | absent | fragile | yes |
| {R3} | absent | absent | absent | yes |

Under {R3, R6}, `mutual_household_care` reads fragile and the other goods stable; under {R2, R3, R6} every coverture good reads fragile (nothing forces care once both duties go).

**What it says, and what it does not.** As encoded, under coverture no compliant trace has mutual care that neither spouse is obliged to give, and no single rule's deletion changes that: the husband's maintenance duty (R2) and the wife's household duty (R3) each oblige care on their own, and the exit bar (R6) bars exit on top. The good becomes possible only when both duties and the exit bar go, and then at one step, not throughout (the re-gloss's "throughout" is not expressed; under the possible measure one witness step suffices), **even though R5, the husband's power to chastise her, remains**: the no-sanction clause reads only a power enabled at that step, and R5's condition (`misbehaves`) starts false, so the clause is idle under strict compliance. Slice 4 must not read `chosen_mutual_care`'s possible column as "free of domination". The base absence is by construction (the O5 pin: R2 and R3 oblige care at every married step, so the not-obliged conjuncts fail there), and the absence is overdetermined (R2, R3 and R6 each bar it; single-deletion ablation cannot attribute it). This is a statement about the encoding of one good, under strict compliance; it is not a finding that chosen care is impossible in any real marriage, and, as the re-gloss author noted, any general duty of mutual support (as in many modern civil codes) would make the good unattainable in the same way.

### The blind-gloss experiment (R3.3 e, R3.6 step 6)

**Formulas** (dataset: data/institutions/properties.json at D6; blind: r3/3x-encoder-{1,2}.yaml; the experiment's property file: r3/experiment-properties.yaml, never in src/properties.yaml). Back-glosses, short:

| good | dataset (primary) | blind-1 | blind-2 |
| --- | --- | --- | --- |
| `cared_for` | every continuing subject receives care from someone | every subject receives care from someone else who holds no power to sanction them | every subject receives care from someone who holds no power to sanction them (ectogenesis left out of its entries) |
| `mutual_household_care` | each spouse provides care to the other | both directions of care, and `care_obliged` symmetric between spouses | equivalent to blind-1 |
| `known_carer` | every continuing subject has a carer who also cared at the previous step, if anyone did | everyone receiving care from another has a carer who still cares at the next step | every subject has a carer who also cared at the previous step (unless newly a subject) |
| `child_with_family` | one disjunct per entry (at home; parent cares; case open and not in custody) | cps only: a child with a parent and in no danger is not in custody | cps only: has a parent and is not in custody, unless in danger |
| `provided_for` | maintained by her husband, or means of her own (contested: by anyone) | income of her own (independent, or earnings she owns) and care from someone else | care from someone and means of her own (income, owned earnings or controlled property) |
| `chosen_mutual_care` | (D6) care both ways, not obliged either way, she can exit, no one can sanction her | any subject in a care relation: care both ways, not obliged either way, she can exit and has an income of her own | married couples: care both ways, not obliged either way, she can exit and has means of her own |

**z3 equivalence** (fluents uninterpreted, as scripts/goods_equiv.py; D = dataset primary at D6):

| good | formal D~b1 | D~b2 | b1~b2 | subject D~b1 | D~b2 | b1~b2 |
| --- | --- | --- | --- | --- | --- | --- |
| `cared_for` | different | different | different | equiv | equiv | equiv |
| `mutual_household_care` | different | different | **equiv** | equiv | equiv | equiv |
| `known_carer` | different | different | different | different | equiv | different |
| `child_with_family` | different | different | different | equiv | equiv | equiv |
| `provided_for` | different | different | different | equiv | equiv | equiv |
| `chosen_mutual_care` | different | different | different | different | equiv | different |

The dataset's `provided_for` alternative (encoder-2) is equivalent to neither blind formula.

**How it was run (drift 4).** The spec's single scratch properties.json (blind-1 as `formal`, blind-2 as a contested alternative) is refused by the engine's R2.1 subject check: blind-2's `known_carer` subject names `is_subject`, undeclared in paternity-quota and transferable-leave, where blind-1's `known_carer` (which names only `provides_care` and `succ`) applies. The experiment was therefore run in split form: one scratch properties.json per blind encoder, each = D6's with the six goods replaced by that encoder's own `formal`, `subject` and `entries` (so each encoder's goods apply where its own entries and its own fluents put them), `phil rules ablate --k 6,8` on all 27 entries each (blind-1 5m, blind-2 5m). Per-encoder readings are then the two runs' readings, and contested readings are computed as the engine defines them (`summarize`: ranked rows at k = 6 whose reading differs by encoder in any column), across the two runs. r3/experiment-properties.yaml records the combined form (encoder 1's `entries` on each property; the note on `cared_for`'s alternative gives encoder 2's).


**Reading the differences.** Most of the blind-vs-dataset movement traces to three encoding choices, each visible in the formulas above, none a defect *(fix pass: "none a defect" means none an engine or procedure error; the faithfulness review judged the blind `mutual_household_care` unfaithful to its own gloss in coverture and the blind `cared_for` a different good, care without domination; findings 3 and 4)*. Blind goods, like the dataset's, were also evaluated in entries outside their encoders' `entries` (companion entries, airline-flight, crisis-team); the blind `cared_for` "absent" in the companion entries is such an extrapolation:
- `mutual_household_care` (blind, both): requiring `care_obliged` to be symmetric makes deleting either spouse's duty leave a one-sided duty, so R2 and R3 each make the good impossible (stable > absent) and read **carrying (possible)** and constitutive in all nine coverture-family entries; under the dataset formula R3 is unread (primary) and guarantee-carrying.
- `cared_for` (blind, both): excluding care from a carer who holds a power to sanction makes it fragile, not stable, in the coverture family (the husband holds the chastisement power while R5 stands; deleting R5 makes it stable, an unranked row) and absent in the companion entries; deleting R2 then moves nothing, so airline-flight R2 and coverture R2 lose their guaranteed-primary load for this good.
- `provided_for` (blind, both): means of her own are required, so maintenance by the husband no longer counts; the good reads absent or fragile instead of stable, and R2 moves it only in coverture-floor (stable > fragile; its base is stable there through R20's income access and R2's care).
- `known_carer` (blind-1 forward continuity vs blind-2 backward continuity): the encoders' main disagreement; blind-1 reads it fragile across the coverture family and stable in cps, ectogenesis and gestational-surrogacy, blind-2 the reverse pattern. It produces the contested readings on ectogenesis and gestational-surrogacy R4~prohibit and airline-flight R2.

**Predictions X1 to X7** (none a falsifier of the instrument; a miss is a result):

| | prediction | result | held |
| --- | --- | --- | --- |
| X1 | the free list names at least 3 of the six topics | **2** clearly (care received: `receiving_care`; secured subsistence: `income`, `financial_independence`, `housing`); a third only if `being_known` (being known by others, no carer named) counts as "a continuing, knowing carer"; mutual care in a household, child with family and chosen or unimposed care do not appear | **borderline**: missed on the strict reading, held only on the lenient one |
| X2 | at most 4 of six blind pairs z3-equivalent; `mutual_household_care` likeliest equivalent; `child_with_family`, `provided_for`, `chosen_mutual_care` likeliest contested | 1 of 6 (`mutual_household_care`); the three named are contested | yes |
| X3 | at least one `not_expressible` | many: blind-1 records them on all six goods (cared_for in ectogenesis; partial in every listed entry of four goods; child_with_family in kibbutz and ectogenesis), blind-2 likewise | yes |
| X4 | `contested_readings` >= 1 in some entry | **3 ranked rows** (engine definition, k = 6): airline-flight R2 (guaranteed: blind-1 unread, blind-2 guarantee-carrying), ectogenesis R4~prohibit (primary: blind-1 unread, blind-2 carrying (possible)), gestational-surrogacy R4~prohibit (possible and primary); 34 cells counting unranked rows and both k | yes |
| X5 | at most 2 of six blind primaries z3-equivalent to the dataset's | **0** (and 0 for blind-2) | yes (RF3.9 not fired) |
| X6 | on the 13 rows the blind primary differs from the dataset in at least one row (likeliest police-crisis R2) | 3 rows differ: coverture-household R2 and R3, ectogenesis R4~prohibit; police-crisis R2 reads unread in all three columns (the blind `cared_for` reads it fragile > fragile there too) | yes; the named locus wrong |
| X7 | if the blind `chosen_mutual_care` gloss mentions duty or being made to care, at least one encoder uses `care_obliged`, and then base absent and R6 absent > absent | the gloss says "must not be imposed by law, economics or norm" (imposition, not "duty" in words); **both** encoders use `care_obliged` both ways; base absent in all nine entries and R6 absent > absent, both encoders, both k | yes |

**Replacement candidates** (R3.3 e; referred to the author for a revision-4 preregistration; **none acted on**; condition 3, the faithfulness seat's back-translation, is still to come). *Fix pass: condition 3 fails for both candidates; the council recommends no replacement; the author decides ("Revision 3 fix pass", author decisions open).*
- **`mutual_household_care`: candidate.** (1) blind-1 and blind-2 z3-equivalent; (2) its primary reading differs from the dataset's on ranked rows of the five entries (coverture-household R3 unread > carrying (possible); R2 carrying (guaranteed) > carrying (possible)) and its base agrees (stable). (3) pending.
- **`cared_for`: conditional candidate.** (2) holds (base stable > fragile in the coverture family; coverture R2's reading). (1) holds on every row of every entry where both blind formulas apply (500 cells, no state differs), but not literally "in every row": blind-2 left ectogenesis out of its entries (its sanction clause is not expressible there), so its formula does not apply in ectogenesis, where blind-1's reads fragile. Whether that applicability difference fails (1) is the author's call.
- **`chosen_mutual_care`: not a candidate.** (1) holds (same states in every row: absent everywhere, like the dataset) but (2) fails: no reading or base state differs from D6.
- **`known_carer`, `child_with_family`, `provided_for`: not candidates** (the blind encoders disagree in states: `known_carer` in 13 entries, `child_with_family` in cps, `provided_for` in the five MWPA entries). Input for slice 5, with these loci: `known_carer`'s direction of continuity (forward vs backward); `child_with_family`'s danger exception (guard vs disjunct; blind-1 reads it stable in cps, blind-2 fragile); `provided_for`'s means of her own (whether controlled property counts).

**Uncounted, inconsistent_after, k-disagreements** (both blind runs and D6): **none** in all three (0 uncounted cells, 0 inconsistent_after, 0 k-disagreement rows; every base state and every row identical at k = 6 and 8 in every column). Goods not-applicable rows: D6 3 (airline-flight R1~prohibit, ectogenesis R1~prohibit, gestational-surrogacy R2~prohibit); blind-1 7 (those three, plus ectogenesis and gestational-surrogacy R4~prohibit for `known_carer`, whose subject needs care from another, and paternity-quota R1 and R1~prohibit, where blind-1's `known_carer` applies); blind-2 3 (the same three as D6).

**What the experiment can and cannot show.** It measures agreement between two instances of one model encoding a gloss written without the instrument. Agreement dropped from 4 of 5 (revision 1) and 1 of 1 (revision 2), both with non-blind glosses, to 1 of 6. ~~The earlier convergence depended largely on the gloss fixing the fluents~~ (fix pass: withdrawn as a causal claim; the drop is consistent with faithfulness revision-2 finding 9, but the prompt, vocabulary and conventions also changed, so the cause is not isolated; restated headline in "Revision 3 fix pass"). No blind formula is equivalent to the dataset's, because the blind author wrote different goods under the same ids, and the readings that depend on encoder choice are listed above. It cannot show agreement across models or between people: two Claude instances share priors, and the non-Claude encoder was not run.

### Falsifiers (R3.5)

| | falsifier | fired |
| --- | --- | --- |
| RF3.1 | D4 vs D5 differ in any field, or a layer-1 verdict changes | no (D5 = D4; check-all, diff, gate, drop-one unchanged at D5 and again at D6) |
| RF3.2 | a primary cell differs from R3.1's table, or a measure field / `top_rules` differs from the fix-pass rerun | no |
| RF3.3 | an obliged differential disagreement (O3) or dataset pin failure (O5) | O3: no (engine suite 656 passed). O5: **fired as typed** (preregistration error, engine correct): the two coverture pins are violated as written; **held as rewritten** (computational-liberation pytest 38 passed at D6, with the as-typed forms pinned at `violated`). Drift 10; first reported by the revision-3 correctness review (finding 1) |
| RF3.4 | under B, `chosen_mutual_care` not absent in some coverture-family base, or R6 not absent > absent | no |
| RF3.5 | probe {R5, R6} not absent | no (absent; revision-2 formula: stable) |
| RF3.6 | under B, any single-rule row moves `chosen_mutual_care` | no |
| RF3.7 | {R2, R3, R6} reads absent (B) | no (fragile) |
| RF3.8 | a stable cell for `chosen_mutual_care`, a goods uncounted cell, `no_witness_within_k`, a goods k-disagreement or `inconsistent_after` | no (none in D6, nor in either blind run) |
| RF3.9 | X5 fails | no (0 of 6) |

**No RF3 falsifier fired, apart from RF3.3's O5 half as typed** (fix pass: the two coverture pins were mis-quantified in the preregistration and fire as written; the engine is right; drift 10).

### Layer 1 at D6

`build.py --check`: ok, 27 institutions, 34 properties, 28 cards (institutions.json unchanged by D6; properties.json changes only `chosen_mutual_care`; six cards change only their goods note). `pytest -q`: 38 passed (computational-liberation, including the O5 `care_obliged` pins); philosophy-engine 656 passed, 2 skipped on the synced data. `check-all --no-cache`: 146/146 agreement. `diff --baseline` (data/verdicts-baseline.json at HEAD): 0 changed, 0 added, 0 removed of 146. `gate`: PASS, output identical to the D5 run line for line. `scripts/drop_one_match.py`: identical to the D5 run. No verdict reads `chosen_mutual_care` outside the ablation, so none moved. Scoreboard row appended (docs/scoreboard-ablate.md): `2026-11-06 | 7859726 | rules ablate | 27 | 356 | 0 | 0 | 0 | 0 | 25 | 0` (`top_rule_changes` against D5'; `contested_readings` 0 in the dataset).

### Pass test (R3.6)

| item | status |
| --- | --- |
| engine implements R3.1 and R3.2, every listed test passing, every listed mutation killed | **pass** (42df8af) |
| E1r3 and E2r3 hold | **pass** |
| `chosen_mutual_care` re-glossed by an audited fresh agent from its bundle only, encoded by two audited fresh encoders from a hashed bundle containing the prompt, and run | **pass** (merge log "Revision 3"; D6 above) |
| blind-gloss experiment on all six goods: blind author audited, message order kept; two audited fresh Claude encoders; hashed bundles; results side by side at k = 6 and 8 with uncounted, inconsistent_after and k-disagreements listed | **pass**, with the split-run departure (drift 4) and the bundle departures (drift 2) |
| non-Claude encoder recorded as not run, procedure and prompt hashed | **pass** (bundle3x includes prompt-api.md) |
| every report carries the ADR 0012 sentence | **pass** |
| fail: a `formal`, `subject` or `contested` of the five revision-1 goods changes | not triggered (properties.yaml diff touches only `chosen_mutual_care`) |
| fail: an experiment formula enters src/properties.yaml | not triggered (scratch properties.json only; r3/experiment-properties.yaml is outside src/) |
| fail: a gloss author or encoder given anything outside its bundle | not triggered (audits in the merge log) |
| fail: the free list written after the ids were shown | not triggered (the ids were moved out of the bundle while it was written; hash recorded first) |
| fail: a contested alternative pooled or dropped | not triggered (each blind encoder its own column; the dataset's `provided_for` alternative kept) |
| fail: a prediction edited after a run | not triggered (plans/priority-slice2.md unchanged) |

**Verdict: revision 3 passes steps 1 to 7, pending the step-8 council** (correctness seat: `obliged`, the primary column, tests and mutations, E1r3/E2r3; faithfulness seat: back-translation of the new `chosen_mutual_care` and each blind formula, transcript audits, the primary mapping, and condition 3 of the replacement rule).

### Drift (recorded; nothing edited in the preregistration)

1. **Dataset baseline moved** (faithfulness batch 2, merged from `sourcing-verify` after the D5 run): cps R8, R11, R11~prohibit freedom load 1 > 0 at both k; no goods change. D6 is compared with D5' (above). The police R2 experiment (P3) is not in the dataset. diff/gate/drop-one are against data/verdicts-baseline.json at HEAD.
2. **Bundle departures** (merge log "Revision 3: encoders", coordinator decisions): the validator is a new validate.sh (the revision-2 one built coverture-floor from the revision-1 hand vocab) *(fix pass: first written "self-contained"; it loads the live institutions.json, rules included, and outputs syntax and declared-fluent checks only)*; vocab diffs against revision 1 are not "`care_obliged` only" (the dataset had since gained `has_own_income` / `draw_subsistence`, `would_not_benefit` and the real coverture-floor entry); cps `defaults` kept in its vocab; goods-list.md format chosen by the assembler; prompt-api.md inside bundle3x (one encoder saw its name in a listing and did not open it).
3. **Gloss procedure stricter than the spec**: prompt-gloss-2.md was moved out of glossbundle3 while message 1 ran (the spec left it on disk), then restored with its hash re-verified (merge log "Revision 3: gloss authors").
4. **Experiment run in split form**: the combined scratch property is refused by the engine's R2.1 subject check (blind-2's `known_carer` subject names `is_subject`, undeclared in the two leave entries where blind-1's applies). Each blind encoder ran in its own scratch properties.json with its own `entries`; contested readings computed across the two runs with the engine's definition. Consequence: blind-2's `cared_for` is not evaluated in ectogenesis (outside its own entries), where a combined run would have evaluated it on blind-1's entries.
5. **X1 judged borderline** (strictly 2 of 6 topics; 3 only if `being_known` counts).
6. **Extra information, not preregistered**: probes also on coverture-household-us, mwpa-earnings and coverture-floor, the {R6} and {R3} probes, and revision 2's formula as a control (all consistent).
7. **History carries more than R3.4 names**: besides revision 2's gloss and formal, its subject, `measure_note` and `history` moved into `history` verbatim, so nothing is lost.
8. **Card goods notes**: updated for coverture-household, coverture-household-us, mwpa-earnings and coverture-floor (chosen care, primary measure) and ectogenesis and kibbutz-childrens-house (primary measure). The cps and police-crisis notes were left alone: another session owns edits to those entries (faithfulness batch). For the record, cps R2~prohibit reads carrying (possible) under the primary column (unranked) and police-crisis has no primary load.
9. **ENGINE_PIN** moves from 605cff4 to 7859726, a data-only sync (pattern c53d132); engine code unchanged.
10. **O5 dataset pins rewritten after they were run** (added in the fix pass; revision-3 correctness review, finding 1). R3.2 O5 pins, as typed: (a) coverture-household `(forall ((h agent) (w agent)) (<=> (married h w t) (and (care_obliged h w t) (care_obliged w h t))))` holds_to_k; (b) coverture-household minus R3 `(forall ((h agent) (w agent)) (not (care_obliged w h t)))` holds_to_k. Both are **violated**: over every ordered pair, `married(wife, husband)` is false while both duties hold, and with R3 deleted R2 still obliges the husband (`care_obliged(husband, wife)`). The pins were mis-quantified; the engine is right. Rewritten forms, which hold: (a) `(forall ((h agent) (w agent)) (iff (or (married h w t) (married w h t)) (and (care_obliged h w t) (care_obliged w h t))))`; (b) `(not (care_obliged wife husband t))`, plus `(care_obliged husband wife t)` reachable. The as-typed forms are pinned at `violated` beside them (computational-liberation tests/test_dataset_claims.py `O5`, `test_care_obliged_pin_coverture_without_R3`; philosophy-engine tests/test_rules_obliged.py `test_O5_household_pins_mirror_the_dataset_pins`). RF3.3 amended accordingly. No number changes.
11. **`care_obliged` entry set: 22, not 24; constant false in cps, not footbinding** (fix pass; correctness finding 3). R3.2 lists 24 entries including footbinding and footbinding-no-pledge, and predicts the fluent constant false in "footbinding and the paternity pair". D5 declares it in 22: the footbinding pair declares no `provides_care`, so it gets none. It is constant false in **cps** (no `must` names `provides_care` there) and the paternity pair. Recorded before only in the b24cb36 commit message. cps `cared_for` and `known_carer` never read `care_obliged`, so nothing moves.
12. **Conflict-check premise false for free-variable conditions** (fix pass; correctness finding 2). R3.2 says a must and a disability on one instance "is a deontic conflict, which the existing conflict check reports". `rules_checks.check_deontic_conflict` lowers each condition with its free variables unbound; an unbound agent name lowers a fluent to constant false, so such a pair can go unreported (the O1 fixture's R4/R6 is one). The 42df8af message and the O1 test comment promised this record; it was missing. No dataset entry has a must and a must_not on one aim with a free-variable condition (every free-variable condition is on a may or must_not, apart from cps R6 `contact_mother` and lease R5 `rent_paid`, which no must_not names), so nothing is affected. Known limit 1 in the fix pass and the rules_lower module doc.

### Reproduction

Dataset: computational-liberation at this commit, `uv run python data/institutions/build.py --write --cards`. D5' and D6: `uv run phil rules ablate --k 6,8 --workers 4 --json --summary --readings` (D5': `--institutions/--properties` copies of data/institutions/*.json at 1c512b9; D6: the committed data, with `--scoreboard docs/scoreboard-ablate.md --prev <D5' summary>`). Probes: a scratch script applying `rules_ablate.without_rule` per set and reading `rules_checks.run_all` goods states at k = 6 and 8. Experiment: two properties.json (D6's with the six goods replaced by r3/3x-encoder-1.yaml's, resp. -2's, formal, subject and entries, `contested: []`, and `encoders: [blind-1, blind-2]`, resp. `[blind-2, blind-1]`, since the loader requires at least two encoders on a goods property; committed in the fix pass as r3/experiment-split/blind-1-properties.json and blind-2-properties.json, byte-identical to the files run), each run with the same ablate command (`--properties` that file); equivalence with the scripts/goods_equiv.py logic on formal and subject. Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/r3d6/`, not kept.

### Side-by-side tables (D6 vs blind-1 vs blind-2)

#### Base states (unablated), D6 dataset primary | blind-1 | blind-2 (k=6 = k=8 unless shown; '-' = not applicable in that entry)

| entry | good | D6 | blind-1 | blind-2 |
| --- | --- | --- | --- | --- |
| coverture-household | cared_for | stable | fragile | fragile |
| coverture-household | mutual_household_care | stable | stable | stable |
| coverture-household | known_carer | stable | fragile | stable |
| coverture-household | provided_for | stable | absent | absent |
| coverture-household | chosen_mutual_care | absent | absent | absent |
| police-crisis | cared_for | fragile | fragile | fragile |
| police-crisis | known_carer | fragile | fragile | fragile |
| cps | cared_for | fragile | fragile | fragile |
| cps | known_carer | fragile | stable | fragile |
| cps | child_with_family | fragile | stable | fragile |
| crisis-team | cared_for | fragile | fragile | fragile |
| crisis-team | known_carer | fragile | fragile | fragile |
| paternity-quota | known_carer | - | fragile | - |
| transferable-leave | known_carer | - | fragile | - |
| companion-ownership | cared_for | fragile | absent | absent |
| companion-ownership | known_carer | fragile | fragile | fragile |
| companion-guardianship | cared_for | fragile | absent | absent |
| companion-guardianship | known_carer | fragile | fragile | fragile |
| companion-guardian-renamed | cared_for | fragile | absent | absent |
| companion-guardian-renamed | known_carer | fragile | fragile | fragile |
| kibbutz-childrens-house | cared_for | fragile | fragile | fragile |
| kibbutz-childrens-house | known_carer | fragile | fragile | fragile |
| kibbutz-childrens-house | child_with_family | absent | - | - |
| kibbutz-childrens-house-no-implicit | cared_for | fragile | fragile | fragile |
| kibbutz-childrens-house-no-implicit | known_carer | fragile | fragile | fragile |
| airline-flight | cared_for | stable | fragile | fragile |
| airline-flight | known_carer | stable | fragile | stable |
| coverture-household-us | cared_for | stable | fragile | fragile |
| coverture-household-us | mutual_household_care | stable | stable | stable |
| coverture-household-us | known_carer | stable | fragile | stable |
| coverture-household-us | provided_for | stable | absent | absent |
| coverture-household-us | chosen_mutual_care | absent | absent | absent |
| mwpa-creditor-exemption | cared_for | stable | fragile | fragile |
| mwpa-creditor-exemption | mutual_household_care | stable | stable | stable |
| mwpa-creditor-exemption | known_carer | stable | fragile | stable |
| mwpa-creditor-exemption | provided_for | stable | absent | absent |
| mwpa-creditor-exemption | chosen_mutual_care | absent | absent | absent |
| mwpa-property | cared_for | stable | fragile | fragile |
| mwpa-property | mutual_household_care | stable | stable | stable |
| mwpa-property | known_carer | stable | fragile | stable |
| mwpa-property | provided_for | stable | absent | fragile |
| mwpa-property | chosen_mutual_care | absent | absent | absent |
| mwpa-earnings | cared_for | stable | fragile | fragile |
| mwpa-earnings | mutual_household_care | stable | stable | stable |
| mwpa-earnings | known_carer | stable | fragile | stable |
| mwpa-earnings | provided_for | stable | fragile | fragile |
| mwpa-earnings | chosen_mutual_care | absent | absent | absent |
| mwpa-sole-trader | cared_for | stable | fragile | fragile |
| mwpa-sole-trader | mutual_household_care | stable | stable | stable |
| mwpa-sole-trader | known_carer | stable | fragile | stable |
| mwpa-sole-trader | provided_for | stable | fragile | fragile |
| mwpa-sole-trader | chosen_mutual_care | absent | absent | absent |
| mwpa-suit | cared_for | stable | fragile | fragile |
| mwpa-suit | mutual_household_care | stable | stable | stable |
| mwpa-suit | known_carer | stable | fragile | stable |
| mwpa-suit | provided_for | stable | fragile | fragile |
| mwpa-suit | chosen_mutual_care | absent | absent | absent |
| mwpa-property-narrowed | cared_for | stable | fragile | fragile |
| mwpa-property-narrowed | mutual_household_care | stable | stable | stable |
| mwpa-property-narrowed | known_carer | stable | fragile | stable |
| mwpa-property-narrowed | provided_for | stable | absent | fragile |
| mwpa-property-narrowed | chosen_mutual_care | absent | absent | absent |
| coverture-floor | cared_for | stable | fragile | fragile |
| coverture-floor | mutual_household_care | stable | stable | stable |
| coverture-floor | known_carer | stable | fragile | stable |
| coverture-floor | provided_for | stable | stable | stable |
| coverture-floor | chosen_mutual_care | absent | absent | absent |
| ectogenesis | cared_for | fragile | fragile | - |
| ectogenesis | known_carer | fragile | stable | fragile |
| ectogenesis | child_with_family | fragile | - | - |
| gestational-surrogacy | cared_for | fragile | - | - |
| gestational-surrogacy | known_carer | fragile | stable | fragile |

Base k-disagreements: none. Base differences between any two columns: 41 (entry, good) pairs.

#### Rows where some column moves a good and the three columns' transitions differ (k=6; k=8 identical unless marked)

| entry | rule | ranked | good | D6 | blind-1 | blind-2 |
| --- | --- | --- | --- | --- | --- | --- |
| coverture-household | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| coverture-household | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-household | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| coverture-household | R2 | yes | provided_for | stable>fragile | absent | absent |
| coverture-household | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-household | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| coverture-household | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| cps | R2~prohibit | no | known_carer | fragile>absent | stable | fragile>absent |
| cps | R3 | no | child_with_family | fragile | stable>fragile | fragile |
| cps | R3~prohibit | no | child_with_family | fragile | stable>fragile | fragile |
| paternity-quota | R1 | yes | known_carer | - | fragile>not_applicable | - |
| paternity-quota | R1~prohibit | yes | known_carer | - | fragile>not_applicable | - |
| companion-ownership | R1~prohibit | no | cared_for | fragile>stable | absent | absent |
| companion-ownership | R10 | no | cared_for | fragile | absent>fragile | absent>fragile |
| companion-ownership | R10~prohibit | no | cared_for | fragile | absent>fragile | absent>fragile |
| companion-guardianship | R10 | no | cared_for | fragile | absent>fragile | absent>fragile |
| companion-guardianship | R10~prohibit | no | cared_for | fragile | absent>fragile | absent>fragile |
| companion-guardian-renamed | R1~prohibit | no | cared_for | fragile>stable | absent | absent |
| companion-guardian-renamed | R10 | no | cared_for | fragile | absent>fragile | absent>fragile |
| companion-guardian-renamed | R10~prohibit | no | cared_for | fragile | absent>fragile | absent>fragile |
| kibbutz-childrens-house | R4 | yes | child_with_family | absent>fragile | - | - |
| airline-flight | R1~prohibit | no | cared_for | stable>not_applicable | fragile>not_applicable | fragile>not_applicable |
| airline-flight | R1~prohibit | no | known_carer | stable>not_applicable | fragile | stable>not_applicable |
| airline-flight | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| airline-flight | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| airline-flight | R3 | no | cared_for | stable | fragile>stable | fragile>stable |
| airline-flight | R3~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| coverture-household-us | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| coverture-household-us | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-household-us | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| coverture-household-us | R2 | yes | provided_for | stable>fragile | absent | absent |
| coverture-household-us | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-household-us | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| coverture-household-us | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-creditor-exemption | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-creditor-exemption | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-creditor-exemption | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-creditor-exemption | R2 | yes | provided_for | stable>fragile | absent | absent |
| mwpa-creditor-exemption | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-creditor-exemption | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-creditor-exemption | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-property | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-property | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-property | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-property | R2 | yes | provided_for | stable>fragile | absent | fragile |
| mwpa-property | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-property | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-property | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-property | R13 | no | provided_for | stable | absent | fragile>absent |
| mwpa-property | R13~prohibit | no | provided_for | stable | absent | fragile>absent |
| mwpa-earnings | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-earnings | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-earnings | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-earnings | R2 | yes | provided_for | stable>fragile | fragile | fragile |
| mwpa-earnings | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-earnings | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-earnings | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-earnings | R14 | no | provided_for | stable | fragile>absent | fragile |
| mwpa-earnings | R14~prohibit | no | provided_for | stable | fragile>absent | fragile |
| mwpa-sole-trader | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-sole-trader | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-sole-trader | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-sole-trader | R2 | yes | provided_for | stable>fragile | fragile | fragile |
| mwpa-sole-trader | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-sole-trader | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-sole-trader | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-sole-trader | R14 | no | provided_for | stable | fragile>absent | fragile |
| mwpa-sole-trader | R14~prohibit | no | provided_for | stable | fragile>absent | fragile |
| mwpa-suit | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-suit | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-suit | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-suit | R2 | yes | provided_for | stable>fragile | fragile | fragile |
| mwpa-suit | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-suit | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-suit | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-suit | R14 | no | provided_for | stable | fragile>absent | fragile |
| mwpa-suit | R14~prohibit | no | provided_for | stable | fragile>absent | fragile |
| mwpa-property-narrowed | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| mwpa-property-narrowed | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-property-narrowed | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| mwpa-property-narrowed | R2 | yes | provided_for | stable>fragile | absent | fragile |
| mwpa-property-narrowed | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| mwpa-property-narrowed | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-property-narrowed | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| mwpa-property-narrowed | R13 | no | provided_for | stable | absent | fragile>absent |
| mwpa-property-narrowed | R13~prohibit | no | provided_for | stable | absent | fragile>absent |
| coverture-floor | R2 | yes | cared_for | stable>fragile | fragile | fragile |
| coverture-floor | R2 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-floor | R2 | yes | known_carer | stable>fragile | fragile | stable>fragile |
| coverture-floor | R2 | yes | provided_for | stable | stable>fragile | stable>fragile |
| coverture-floor | R3 | yes | mutual_household_care | stable>fragile | stable>absent | stable>absent |
| coverture-floor | R5 | no | cared_for | stable | fragile>stable | fragile>stable |
| coverture-floor | R5~prohibit | no | cared_for | stable | fragile>stable | fragile>stable |
| coverture-floor | R20 | no | provided_for | stable | stable>absent | stable>absent |
| coverture-floor | R20~prohibit | yes | provided_for | stable | stable>absent | stable>absent |
| ectogenesis | R1~prohibit | yes | cared_for | fragile>not_applicable | fragile>not_applicable | - |
| ectogenesis | R1~prohibit | yes | known_carer | fragile>not_applicable | stable>not_applicable | fragile>not_applicable |
| ectogenesis | R1~prohibit | yes | child_with_family | fragile>not_applicable | - | - |
| ectogenesis | R4~prohibit | yes | cared_for | fragile>absent | fragile>absent | - |
| ectogenesis | R4~prohibit | yes | known_carer | fragile>absent | stable>not_applicable | fragile>absent |
| ectogenesis | R4~prohibit | yes | child_with_family | fragile>absent | - | - |
| gestational-surrogacy | R2~prohibit | yes | cared_for | fragile>not_applicable | - | - |
| gestational-surrogacy | R2~prohibit | yes | known_carer | fragile>not_applicable | stable>not_applicable | fragile>not_applicable |
| gestational-surrogacy | R4~prohibit | yes | cared_for | fragile>absent | - | - |
| gestational-surrogacy | R4~prohibit | yes | known_carer | fragile>absent | stable>not_applicable | fragile>absent |

105 (row, good) pairs. Row-level k-disagreements across the three columns: none.

#### Primary readings that differ between D6 and either blind encoder (k=6)

| entry | rule | ranked | D6 | blind-1 | blind-2 |
| --- | --- | --- | --- | --- | --- |
| coverture-household | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| coverture-household | R3 | yes | unread | carrying (possible) | carrying (possible) |
| cps | R2~prohibit | no | carrying (possible) | unread | carrying (possible) |
| airline-flight | R2 | yes | carrying (guaranteed) | unread | unread |
| coverture-household-us | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| coverture-household-us | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-creditor-exemption | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-creditor-exemption | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-property | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-property | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-earnings | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-earnings | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-sole-trader | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-sole-trader | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-suit | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-suit | R3 | yes | unread | carrying (possible) | carrying (possible) |
| mwpa-property-narrowed | R2 | yes | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| mwpa-property-narrowed | R3 | yes | unread | carrying (possible) | carrying (possible) |
| coverture-floor | R2 | yes | carrying (guaranteed) | carrying (both) | carrying (both) |
| coverture-floor | R3 | yes | unread | carrying (possible) | carrying (possible) |
| coverture-floor | R20 | no | unread | carrying (guaranteed) | carrying (guaranteed) |
| coverture-floor | R20~prohibit | yes | unread | carrying (guaranteed) | carrying (guaranteed) |
| ectogenesis | R4~prohibit | yes | carrying (possible) | unread | carrying (possible) |
| gestational-surrogacy | R4~prohibit | yes | carrying (possible) | unread | carrying (possible) |

24 rows. Ranked rows in the five entries: [('coverture-household', 'R2'), ('coverture-household', 'R3'), ('ectogenesis', 'R4~prohibit')]

#### The 13 preregistered rows, primary reading (k=6; k=8 identical unless shown)

| entry | rule | D6 | blind-1 | blind-2 |
| --- | --- | --- | --- | --- |
| coverture-household | R2 | carrying (guaranteed) | carrying (possible) | carrying (possible) |
| coverture-household | R3 | unread | carrying (possible) | carrying (possible) |
| coverture-household | R4 | tying | tying | tying |
| coverture-household | R7 | tying | tying | tying |
| coverture-household | R6 | tying | tying | tying |
| police-crisis | R2 | unread | unread | unread |
| police-crisis | R4 | tying | tying | tying |
| cps | R10 | tying | tying | tying |
| kibbutz-childrens-house | R2 | tying | tying | tying |
| kibbutz-childrens-house | R3 | unread | unread | unread |
| kibbutz-childrens-house | R4 | tying | tying | tying |
| ectogenesis | R4~prohibit | carrying (possible) | unread | carrying (possible) |
| ectogenesis | R5 | tying | tying | tying |

Rows where a blind column differs from D6: [('coverture-household', 'R2'), ('coverture-household', 'R3'), ('ectogenesis', 'R4~prohibit')]

#### Contested readings between blind-1 and blind-2 (reading differs by encoder on a row; any of the three columns; k=6 and 8)

- cps R2~prohibit k=6 primary: blind-1 unread / blind-2 carrying (possible) (unranked)
- cps R2~prohibit k=8 primary: blind-1 unread / blind-2 carrying (possible) (unranked)
- cps R3 k=6 guaranteed: blind-1 guarantee-carrying / blind-2 unread (unranked)
- cps R3 k=8 guaranteed: blind-1 guarantee-carrying / blind-2 unread (unranked)
- cps R3~prohibit k=6 guaranteed: blind-1 guarantee-carrying / blind-2 unread (unranked)
- cps R3~prohibit k=8 guaranteed: blind-1 guarantee-carrying / blind-2 unread (unranked)
- airline-flight R2 k=6 guaranteed: blind-1 unread / blind-2 guarantee-carrying
- airline-flight R2 k=8 guaranteed: blind-1 unread / blind-2 guarantee-carrying
- mwpa-property R13 k=6 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property R13 k=8 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property R13~prohibit k=6 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property R13~prohibit k=8 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-earnings R14 k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-earnings R14 k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-earnings R14~prohibit k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-earnings R14~prohibit k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-sole-trader R14 k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-sole-trader R14 k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-sole-trader R14~prohibit k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-sole-trader R14~prohibit k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-suit R14 k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-suit R14 k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-suit R14~prohibit k=6 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-suit R14~prohibit k=8 possible: blind-1 constitutive / blind-2 unread (unranked)
- mwpa-property-narrowed R13 k=6 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property-narrowed R13 k=8 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property-narrowed R13~prohibit k=6 possible: blind-1 unread / blind-2 constitutive (unranked)
- mwpa-property-narrowed R13~prohibit k=8 possible: blind-1 unread / blind-2 constitutive (unranked)
- ectogenesis R4~prohibit k=6 primary: blind-1 unread / blind-2 carrying (possible)
- ectogenesis R4~prohibit k=8 primary: blind-1 unread / blind-2 carrying (possible)
- gestational-surrogacy R4~prohibit k=6 possible: blind-1 unread / blind-2 constitutive
- gestational-surrogacy R4~prohibit k=6 primary: blind-1 unread / blind-2 carrying (possible)
- gestational-surrogacy R4~prohibit k=8 possible: blind-1 unread / blind-2 constitutive
- gestational-surrogacy R4~prohibit k=8 primary: blind-1 unread / blind-2 carrying (possible)

34 (row, k, column) cells; entries: ['airline-flight', 'cps', 'ectogenesis', 'gestational-surrogacy', 'mwpa-earnings', 'mwpa-property', 'mwpa-property-narrowed', 'mwpa-sole-trader', 'mwpa-suit']

#### Totals per run (uncounted, inconsistent_after, k-disagreements, goods n/a rows)

- **D6**: summary totals {'entries': 27, 'inconsistent_after': 0, 'uncounted': 0}; uncounted cells 0; inconsistent_after 0; k-disagreement rows 0; goods n/a rows 3
  - n/a: ('airline-flight', 'R1~prohibit', ('cared_for', 'known_carer'))
  - n/a: ('ectogenesis', 'R1~prohibit', ('cared_for', 'child_with_family', 'known_carer'))
  - n/a: ('gestational-surrogacy', 'R2~prohibit', ('cared_for', 'known_carer'))
- **blind-1**: summary totals {'entries': 27, 'inconsistent_after': 0, 'uncounted': 0}; uncounted cells 0; inconsistent_after 0; k-disagreement rows 0; goods n/a rows 7
  - n/a: ('airline-flight', 'R1~prohibit', ('cared_for',))
  - n/a: ('ectogenesis', 'R1~prohibit', ('cared_for', 'known_carer'))
  - n/a: ('ectogenesis', 'R4~prohibit', ('known_carer',))
  - n/a: ('gestational-surrogacy', 'R2~prohibit', ('known_carer',))
  - n/a: ('gestational-surrogacy', 'R4~prohibit', ('known_carer',))
  - n/a: ('paternity-quota', 'R1', ('known_carer',))
  - n/a: ('paternity-quota', 'R1~prohibit', ('known_carer',))
- **blind-2**: summary totals {'entries': 27, 'inconsistent_after': 0, 'uncounted': 0}; uncounted cells 0; inconsistent_after 0; k-disagreement rows 0; goods n/a rows 3
  - n/a: ('airline-flight', 'R1~prohibit', ('cared_for', 'known_carer'))
  - n/a: ('ectogenesis', 'R1~prohibit', ('known_carer',))
  - n/a: ('gestational-surrogacy', 'R2~prohibit', ('known_carer',))

#### Summary lists that differ from D6 (k=6)

- coverture-household (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- coverture-household (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- airline-flight (blind-1): `primary_carrying` ['R2'] -> []; `top_goods_rules` ['R2'] -> []; `top_load_goods_primary` 1 -> 0; `guarantee_carrying` ['R2'] -> []
- airline-flight (blind-2): `primary_carrying` ['R2'] -> []; `top_goods_rules` ['R2'] -> []; `top_load_goods_primary` 1 -> 0
- coverture-household-us (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- coverture-household-us (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-creditor-exemption (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-creditor-exemption (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-property (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-property (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-earnings (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-earnings (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-sole-trader (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-sole-trader (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-suit (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-suit (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-property-narrowed (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- mwpa-property-narrowed (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R3']; `top_goods_rules` ['R2'] -> ['R2', 'R3']; `top_load_goods_primary` 2 -> 1; `constitutive` [] -> ['R2', 'R3']
- coverture-floor (blind-1): `primary_carrying` ['R2'] -> ['R2', 'R20~prohibit', 'R3']; `top_load_goods_primary` 1 -> 2; `constitutive` [] -> ['R2', 'R20~prohibit', 'R3']; `guarantee_carrying` ['R2', 'R3'] -> ['R2', 'R20~prohibit', 'R3']
- coverture-floor (blind-2): `primary_carrying` ['R2'] -> ['R2', 'R20~prohibit', 'R3']; `top_load_goods_primary` 1 -> 2; `constitutive` [] -> ['R2', 'R20~prohibit', 'R3']; `guarantee_carrying` ['R2', 'R3'] -> ['R2', 'R20~prohibit', 'R3']
- ectogenesis (blind-1): `primary_carrying` ['R4~prohibit'] -> []; `top_goods_rules` ['R4~prohibit'] -> []; `top_load_goods_primary` 2 -> 0
- ectogenesis (blind-2): `top_load_goods_primary` 2 -> 1
- gestational-surrogacy (blind-1): `primary_carrying` ['R4~prohibit'] -> []; `top_goods_rules` ['R4~prohibit'] -> []; `top_load_goods_primary` 1 -> 0; `constitutive` ['R4~prohibit'] -> []

## Revision 3 fix pass

Status: 2026-11-06, after the revision-3 council (docs/reviews/2026-11-06-slice2-rev3-correctness-review.md: **supported**, one major reporting gap; docs/reviews/2026-11-06-slice2-rev3-faithfulness-review.md: **weakened (narrowly)**). No new predictions; nothing here changes a verdict, a goods state, a reading or a load (rerun below). Engine: philosophy-engine 672564d (two tests, module-doc known limits; no behaviour change) = **ENGINE_PIN 672564d** (the engine's data copy is byte-identical to the dataset's; no data sync needed). Wording in the "Revision 3" section above was amended in place where listed below, each amendment marked *fix pass*; numbers untouched.

**Second encoder: agent, not someone living under the institution (ADR 0012).**

### Findings and what was done

| finding | done / how |
| --- | --- |
| Correctness 1 [major]: two O5 pins fail as typed; rewritten after the run; the results claimed no pin failure | **done.** Drift 10 quotes both as-typed pins, their verdict (violated) and the rewritten forms. RF3.3 row amended: "fired as typed (preregistration error, engine correct); held as rewritten"; the "No RF3 falsifier fired" line and the D6 headline say so. Test comment in tests/test_dataset_claims.py now points at drift 10. No number changes. |
| Correctness 2: conflict check misses must / disability pairs whose condition has a free variable; promised record missing | **done.** Drift 12; known limit 1 below; rules_lower module doc ("known limits"); the O1 test comment points here. No dataset entry affected. |
| Correctness 3: `care_obliged` in 22 entries, not 24; constant false in cps, not footbinding | **done.** Drift 11; the CARE_OBLIGED_ENTRIES comment cites it. Nothing moves. |
| Correctness 4: split-run inputs not committed; reproduction line incomplete | **done.** data/institutions/goods-encoding/r3/experiment-split/blind-1-properties.json and blind-2-properties.json, byte-identical to the scratch files run (sha256 f28367f6… and 56a0db44…): D6's properties with the six goods replaced by that encoder's `formal`, `subject` and `entries`, `contested: []`, and **`encoders: [blind-1, blind-2]`** (resp. **`[blind-2, blind-1]`**), since the loader requires a goods property to name at least two encoders. Never in src/. Reproduction line says so. |
| Correctness 5: engine (`_typed_domains`, pairwise distinct) and reference (plain product) differ with two or more free condition variables | **recorded** as known limit 2 below and in the rules_lower module doc and the `cond_at` comment. Latent: no dataset rule has more than one free condition variable. Not changed. |
| Correctness 6: OWN6 and OWN3 each killed by one test | **done.** philosophy-engine tests/test_rules_obliged.py: `test_O2b_obliged_lowering_is_the_same_under_sanctioned_compliance` (Grounded.obliged pointwise under `compliance="sanctioned"`, plus the probes) and `test_O1b_instance_arguments_select_the_obliged_tuple` (a must-be on one tuple of an untyped fluent; engine and reference). Mutation record (scratch copies, goods/ablate/obliged/meta tests, `-m "not slow"`, 203 tests): control 203 passed; OWN3 6 failed (now also O1b); OWN6 2 failed (now also O2b). Engine suite 658 passed, 2 skipped. |
| Faithfulness F1 [major]: card sentence "no single rule stands between the couple and chosen mutual care" inverts the probes; absence by construction | **done.** Replaced in the four coverture-family cards (coverture-household, -us, mwpa-earnings, coverture-floor): absent in the base by construction (R2 and R3 oblige care at every married step, the dataset's `care_obliged` pins); each of R2, R3 and R6 on its own bars it, so no single deletion makes it possible; possible (fragile) only with all three deleted, R5 present or not. Same in the D6 paragraph, the glossary ("obliged" example) and docs/overview.md 5b. Also stated: any spousal duty of care or support would bar it the same way; it does not distinguish coverture from later marriage law. |
| F2 [major]: no-sanction clause idle; the good becomes possible with R5 intact | **done (reporting).** Caveat in the D6 paragraph, the headline, the four cards and overview 5b: possible with R2, R3, R6 deleted **even though R5 (the husband's power to chastise her) remains**; the clause reads only a power enabled at that step, and `misbehaves` starts false. **Slice 4 must not read `chosen_mutual_care`'s possible column as "free of domination".** The encoding fix (a derived fluent for a standing sanction power, engine work like `obliged`) is listed under author decisions; not done. |
| F3 [major]: blind `mutual_household_care` unfaithful; R3 carrying (possible) re-launders R3 | **recorded.** Unfaithful in its central case: `provides_care` lumps the husband's maintenance (R2) with the wife's household labour (R3), so `care_obliged` looks symmetric under coverture and R3 reads carrying (possible), constitutive. The dataset reading is the less misleading one. Neither formula measures how household work is distributed: the good is not faithfully expressible in this vocabulary. **Prerequisite for any replacement: a vocabulary split** (a maintenance fluent and a household-labour fluent; the actions `maintain` and `keep_house` exist), then re-gloss and re-encode. |
| F4 [major]: blind `cared_for` is a different good | **recorded.** It is care without domination: it folds the freedom property `care_and_sanction_same_role` into a good, hides the care/control tension the project reports separately, and is not expressible in ectogenesis (blind-2 dropped it; blind-1 kept it with the clause lowered false). If wanted, **preregister it as a separate good**, not a substitute. |
| F5 [major]: "a consequence of the value call, not of the encodings" | **done.** Corrected in the D4 paragraph, the glossary ("primary measure"), and the four coverture-family cards: under the value call **and** the dataset's `mutual_household_care` formula, R3 carries no good on the primary column; the possible measure cannot tell forced from free mutual care, so R3's imposition is not visible there; under both blind formulas R3 reads carrying (possible), judged unfaithful (F3). The glossary's "possible" entry now says it cannot tell forced from free. |
| F6 [major]: the experiment's causal headline overclaims | **done.** Restated in the results ("What the experiment can and cannot show", headline) and the merge log as the review's reportable form (below). The suggested cheap control (two fresh encoders on bundle3x with the revision-1 glosses substituted; about 4 of 5 would point to the gloss as the cause) is a **proposed follow-up, not run**. |
| Council: no replacement | **recorded**: both candidates fail condition 3; the council recommends replacing neither. Listed under author decisions open. |
| Minor 7: "throughout" | **done.** D6 paragraph and cards: possible at one step, not throughout; glossary "possible" says a good glossed "throughout" is read at one step. |
| Minor 8: 3d encoders' equivalence expected (revision-2 finding 9 recurs) | **recorded**: the re-gloss restates the `care_obliged`, `can_exit` and `can_sanction` glosses almost verbatim, so the two dataset encoders were left only quantifier form; their z3 equivalence was expected and is **not evidence about the good**. |
| Minor 9: validator "self-contained" | **done.** Merge log and drift 2: validate.sh "loads the live data/institutions/institutions.json, rules included", through the engine, at the manifest's recorded hash and engine pin; outputs syntax and declared-fluent checks only; not self-contained. |
| Minor 10: audit not re-auditable from the repository | **done** (commit cfcef29): data/institutions/goods-encoding/r3/audit/ holds, per agent, the tool-call listing (timestamp, tool, path or command) and the transcript's sha256 (transcript-hashes.sha256). The merge log's two audit paragraphs now point there and list what no record can show (harness system prompt, prior model knowledge, the coordinator's choice of ids). Gloss-author handbacks now listed. |
| Minor 11: card coverage | **done.** Revision-3 goods notes added to airline-flight (R2 carrying (guaranteed) for `cared_for`), gestational-surrogacy (R4~prohibit carrying (possible), prohibition of the care act) and the five MWPA cards without one (mwpa-creditor-exemption, -property, -property-narrowed, -sole-trader, -suit: R2 and R3 read as in coverture-household). Each says the entry is outside every good's `entries` list, so its readings are extrapolation. The blind `cared_for` "absent" in the companion entries is marked as extrapolation in "Reading the differences". cps and police-crisis cards untouched (another session owns them). |
| Correctness 7, 8; faithfulness 12, 13 | green / sound; nothing to do. |

### Known limits (engine; neither affects the dataset)

1. **Deontic-conflict check and free variables.** `rules_checks.check_deontic_conflict` lowers each condition with its free variables unbound; an unbound agent name lowers a fluent to constant false, so a must / disability pair on one instance whose condition has a free variable can go unreported. R3.2's "which the existing conflict check reports" holds only for conditions without free variables (drift 12).
2. **Several free condition variables.** The engine's `cond_at` binds them pairwise distinct (`_typed_domains`); the reference's `cond_holds` takes the plain product. With two or more free variables in one condition, `enabled`, `obliged` and compliance could differ between the two, and the O3 differential (one free variable per fixture) cannot see it. No dataset rule has more than one. Pre-existing; `obliged` inherits it.

### Author decisions open

1. **Replacement candidates: the council recommends none.** `mutual_household_care` (blind) is unfaithful to its gloss and re-launders R3; `cared_for` (blind) is a different good. The author decides; nothing changes until a revision-4 preregistration.
2. **`mutual_household_care`, vocabulary split.** If the author wants the good "how the household's work is distributed", the prerequisite is splitting `provides_care` into maintenance and household labour, then re-gloss and re-encode (F3).
3. **Care without domination** as a separate good, preregistered on its own, if wanted (F4).
4. **Standing sanction power.** A derived fluent for a sanction power whose condition can become true (engine work, like `obliged`), so the no-sanction clause stops being idle (F2). Until then the caveat above binds slice 4.
5. **Value call on "imposed".** `chosen_mutual_care` excludes both spouses' obliged care, which is stricter than theory.md's imposed-vs-chosen bundle (exit and alternatives); three readings by one model agree, but the call is the author's to own (faithfulness section 2 (a)).
6. **Cheap control for the experiment** (F6): run or not.

### What can be reported now

Each a statement about encodings, under strict compliance, at k = 6 and 8 (the faithfulness review's list). Revision 2 fix pass's list stands, except its `chosen_mutual_care` bullet, which this replaces.

- **`chosen_mutual_care` (D6).** Under coverture as encoded, no compliant trace has mutual care that no rule obliges either spouse to give while she can leave. This is by construction: R2 and R3 oblige care at every married step. R2, R3 and R6 each bar the good on their own, so no single deletion moves it. With all three deleted it becomes possible, at one step, **even though the husband's power to chastise her (R5) remains**, because the sanction clause reads only an enabled power. The revision-2 laundering ({R5, R6} read stable) is gone. Any spousal support duty would make the good unattainable in the same way.
- **Primary column.** R2 is carrying (guaranteed) for `cared_for` and `provided_for` in the coverture family, and for `cared_for` in airline-flight. In ectogenesis (and gestational-surrogacy), R4~prohibit is carrying (possible), a prohibition of the care act. **R3, value call:** under the author's value call *and the dataset formula*, R3 carries no good on the primary column; the possible measure cannot see forced care.
- **Blind-gloss experiment.** With glosses written from theory.md and intent.md alone, two Claude encoders agreed on **1 of 6** goods. No blind formula equals the dataset's, because the blind author wrote different goods for the same ids: **the ids do not fix the goods**. The theory documents alone did not yield mutual care, chosen care or child-with-family. The drop from revision 1's 4 of 5 is consistent with the gloss having fixed the fluents, but **the cause is not isolated** (the gloss content, the prompt's cross-entry instruction, the vocabulary and the conventions also changed). **One model throughout**; the non-Claude encoder was not run. Proposed control not run.
- **Replacement candidates.** None. `mutual_household_care` is not faithfully expressible until the care fluent separates maintenance from household labour. A blind-style `cared_for` would be a new good, care without domination, to preregister separately if wanted.
- **Dataset encoders' agreement on D6.** Protocol independence, audited (r3/audit/). Equivalence was expected: the re-gloss restates the fluent glosses.

### Not yet reportable

- That the absence of `chosen_mutual_care` distinguishes coverture from later marriage law (no entry tests that).
- Any use of `chosen_mutual_care`'s possible column, in slice 4 or elsewhere, as "free of domination"; that deleting R2, R3 and R6 yields chosen care free of domination.
- "R3 carries no good ... not of the encodings"; "carries no good" read as "imposes no cost on any good".
- "The earlier convergence depended largely on the gloss" as a demonstrated cause; anything about agreement across models or between people.
- Any guaranteed reading of `chosen_mutual_care` (unchanged).

### Rerun against the fix pass (no verdict, goods state, reading or load changed)

- **Ablation** on ENGINE_PIN 672564d, the reproduction line's three runs (`uv run phil rules ablate --k 6,8 --workers 4 --json --summary --readings`): D6 on the committed data (8m38s), blind-1 and blind-2 on r3/experiment-split/blind-{1,2}-properties.json (4m52s, 5m07s). Compared leaf by leaf with the revision-3 outputs (`r3d6/ablate-{D6,XA,XB}`): **0 differences** in each JSON and each summary; the three readings tables byte-identical; the text reports identical apart from the scoreboard line (this rerun appended no row). No label or wording field differs either: the fix pass touched no engine output.
- **Layer 1**: `build.py --check` ok (27 institutions, 34 properties, 28 cards; institutions.json and properties.json unchanged, nine cards' goods notes changed or added); `pytest -q` 38 passed; `check-all --no-cache` identical to the D6 run (146/146); `diff --baseline` 0 changed, 0 added, 0 removed of 146; `gate` identical line for line; `scripts/drop_one_match.py` identical. Engine suite 658 passed, 2 skipped (656 + O1b, O2b).
- Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/fp3/` (mutation copies, runs), not kept. No scoreboard row appended (no new numbers).

### Drift after the L1 restatement merge (2026-11-06, engine b00fdc2)

The `sourcing-verify` merge (1d306e8) landed the L1 restatement: police-crisis re-encoded to WIC 5150 (the facility cares during the hold, R2, and holds, R11; the officer detains, R3, and may use force, R5). Slice 2's ablation rerun on the merged dataset (`uv run phil rules ablate --k 6,8 --workers 4 --json --summary --readings`), compared leaf by leaf with the revision 3 fix-pass outputs: every pre-existing row of every entry is identical, police-crisis included (freedom loads, goods states under both measures and both encoders, primary column, readings). The only change is two new rows, police-crisis R11 and R11~prohibit, each listed and not ranked (`deregulated_not_ranked`, `offcondition_free_not_ranked`), load 0 and goods reading unread at k=6 and 8. No top set changes; the readings table is unchanged. So no slice-2 reported result depends on which police role carries care. Drop-one (scripts/drop_one_match.py) after the merge: gate (b) fails on exactly coverture R2/R5/R6, police R2/R4/R11, cps R3/R4/R10.

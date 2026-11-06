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

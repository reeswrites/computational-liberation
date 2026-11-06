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

How to read the goods columns. Two measures, never combined: **guaranteed** (a rule guarantees the good: state stable) and **possible** (the good can hold at a witness step for an existing bearer: fragile or stable). Lost counts are counts of goods formulas (families); each is followed by the number of distinct strands the lost formulas read, and no count is read as "goods lost". **Strict-compliance caveat, applying to every coverture-family goods row below:** under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented.

### Headline

- **Every R2.4 prediction about the 13 rows, the base states, the n/a rows, kibbutz, ectogenesis, the new good and the route comparison held**, at k=6 and k=8, under both encoders. No falsifier (RF1 to RF9) fired.
- Possible column: no single deletion makes a coverture good impossible; deleting the exit bar (R6) makes chosen mutual care possible, in all nine coverture-family entries and in no other row; in ectogenesis, prohibiting the parent's permission to care (R4~prohibit) makes care impossible (constitutive, 3 formulas, 1 strand). Guaranteed column: as revision 1 with "constitutive" renamed "guarantee-carrying".
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
| nine coverture-family entries | cared_for, mutual_household_care, known_carer, provided_for (both encoders) | stable | stable |
| nine coverture-family entries | chosen_mutual_care (both encoders) | absent | absent |
| police-crisis | cared_for, known_carer | fragile | fragile |
| cps | cared_for, known_carer, child_with_family | fragile (medium) | fragile |
| kibbutz-childrens-house | cared_for, known_carer | fragile | fragile |
| kibbutz-childrens-house | child_with_family | absent | absent |
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
| coverture-household | R3 (superadditive, implicit) | 0 / 1 / guarantee-carrying / agree | 0 / 1 (1 strand, `provides_care(w, h)`) / guarantee-carrying / agree | 0 / 0 / unread | 0 / 0 / unread | held. Guaranteed only by R3, an implicit sanctioned duty; not advice to keep it. Under possible, R3 is not constitutive |
| coverture-household | R4 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| coverture-household | R6 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | 1 / 0 / tying / no row; possible gained 1 | 1 / 0 / tying / no row; possible gained 1 (chosen_mutual_care absent > fragile) | held |
| coverture-household | R7 (tying) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | 1 / 0 / tying / agree | held |
| police-crisis | R2 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | held (revision-1 miss stands: as encoded no rule guarantees the goods and none makes them impossible) |
| police-crisis | R4 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | same | same | held |
| cps | R10 (rival) | 1 / 0 / tying / no row | 1 / 0 / tying / no row | same | same | held |
| kibbutz-childrens-house | R2 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | same | same | held (section 4.2's hard case still missed) |
| kibbutz-childrens-house | R3 (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | 0 / 0 / unread | held |
| kibbutz-childrens-house | R4 (rival) | 1 / 0 / tying / no row; gained 0 | 1 / 0 / tying / no row; gained 0 | 1 / 0 / tying / no row; possible gained 1 | 1 / 0 / tying / no row; possible gained 1 (child_with_family absent > fragile) | held: section 4.2's "gained 1" now holds, under possible |
| ectogenesis | R4~prohibit (superadditive) | 0 / 0 / unread | 0 / 0 / unread | 0 / 3 / constitutive / agree | 0 / 3 (1 strand, `provides_care(intended_parent, child)`) / constitutive / agree | held: section 4.2 holds under possible |
| ectogenesis | R5 (tying, implicit) | 1 / 0 / tying / agree | 1 / 0 / tying / agree | same | same | held |

Totals, five entries (primary; encoder 2 identical): guaranteed **10 read rows, 6 agree, 0 mismatch, 4 no row** (predicted the same); possible **9 read rows, 5 agree, 0 mismatch, 4 no row** (predicted the same). Every other ranked row in the five entries is unread under both measures: held.

### n/a rows, kibbutz, information rows

- Rows with an n/a move (`goods_not_applicable_rows`), exactly the three predicted: ectogenesis R1~prohibit (cared_for, known_carer, child_with_family fragile > n/a; lost 0 under both; unread under both; down 1, a protection), gestational-surrogacy R2~prohibit (cared_for, known_carer fragile > n/a; lost 0), airline-flight R1~prohibit (stable > n/a; lost 0; up 1, so tying; unranked). **Held.** Revision-1 F2 reapplied to both measures does not fire.
- gestational-surrogacy R4~prohibit (information): cared_for, known_carer fragile > absent, possible lost 2 (1 strand), constitutive: **held**.
- Kibbutz: child_with_family base absent; R4 deleted absent > fragile, possible gained 1, guaranteed gained 0; no other row moves it; R3 deleted no goods change: **held**.
- **Unpredicted information row:** cps R2~prohibit (the caseworker's `may provide_services` when a case is open, prohibited; not ranked: the prohibit leaks off-condition): cared_for, known_carer fragile > absent, possible lost 2 (1 strand: `provides_care(social_worker, child)`, which in the cps vocabulary is the caseworker's services), constitutive. Revision 1 could not see it (fragile > fragile under the old states). It is not ranked, so it is not in `constitutive` and RF9 does not reach it; it is the one extra `goods_rows` row (drift 1).
- companion-ownership and companion-guardian-renamed R1~prohibit: guaranteed gained 2 (1 strand) each, as in revision 1.

### The chosen-care good

| prediction | result |
| --- | --- |
| base absent in all nine coverture-family entries, both encoders | held |
| R6 deleted: absent > fragile, possible gained 1, guaranteed unchanged, in all nine | held (18 rows, k=6 and 8) |
| R5 and R5~prohibit unranked and move nothing | held |
| R3, R2, R4, R7, R1 and the route rules: absent > absent | held (no row other than R6 changes it) |
| no rule carries the good: lost 0 everywhere under both measures; R3 lost 0 on it | held (the faithful outcome the faithfulness review predicted for option (i)) |
| encoder agreement: same effect in every row, `contested_readings` 0, no `not_expressible` | held. The merged formulas are z3-equivalent (`contested: []`), so encoder 2's column is the primary's; neither encoder recorded `not_expressible` (merge log) |

The {R5, R6} pair (sanction and exit together) is a slice-4 question and is not read here.

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

Winner rule per measure: guaranteed: tie on N, F lower on G (by construction); possible: tie on N and on G. Section 5's branch "tie as predicted" applies: T1 stays a hypothesis; slice 4 keeps the candidates {R2, R20} and {R4, R6, R7}. The floor's goods advantage is about guarantee only (her provision stops depending on R2 being kept), not about what is possible, and says nothing about order. R20 is an unconditional income-access floor for the wife, not the glossary's material floor.

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
2. `chosen_mutual_care` encoded by two audited fresh encoders from a hashed bundle that contains the prompt: **met** (coordinator's merge log "Revision 2": 12 calls each, no breach; bundle hash above). Same caveat as revision 1: one model, protocol independence.
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

### Reproduction

`cd computational-liberation && uv run phil rules ablate --k 6,8 --workers 4 --json ablate-27-r2.json --summary ablate-27-r2-summary.json --readings readings-27-r2.md --prev ablate-27-s2-summary.json` (the revision-1 summary), then the scoreboard row as drift 9. E1r2: the same on D1 (e519609) compared with revision 1's ablate-27-s2.json; E3r2: D1 vs D2 (28b4528); E4r2: D2 vs D3. Layer 1: `build.py --check` ok (27 institutions, 34 properties, 28 cards); `pytest -q` 32 passed; `check-all --no-cache` 146/146; `diff --baseline` 0/0/0; `gate` PASS; `scripts/drop_one_match.py` identical. Mutations: a scratch copy of the engine with one string replacement per mutation. Outputs in `/tmp/claude-0/-home-user/602c9851-0b06-5dd0-a31e-00ab948ba10a/scratchpad/slice2/run2/`, not kept.

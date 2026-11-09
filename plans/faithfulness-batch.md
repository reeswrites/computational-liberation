# Faithfulness batch 3: decision brief for the author (drafted 2026-11-08, nothing applied)

Read against: `plans/sourcing.md` "Faithfulness findings" and "Faithfulness batch 2"; `plans/informal-rules.md` "Sanctioner and kind review"; `data/institutions/README.md` Conventions; `docs/plan.md` "Where to pick up" item 2; `docs/surprises.md`. Dataset at main 54e0c85: 33 entries, baseline 192 rows (k=6, strict, step_mode one), ENGINE_PIN 81d5b9e. Every rule named below was re-read in `data/institutions/src/*.yaml` today; none of the Part A items has been edited since batch 2 (git log on those files shows only the kind/sanctioner migration and the var_roles freeze).

Each item ends with a recommendation and its tradeoff. The recommendation carries weight, not authority: the author rules, then agents apply the rulings under the preregistrations in Part C.

## 1. Scope, and what this batch is not

In scope: the still-open sourcing findings (Part A), the kind reclassification table and the `sanctioner: none` implied-sanction candidates (Part B), and removing `sanctioner_review: derived` from every rule the batch reviews.

Not in scope, and refused if an agent drifts into it:
- No new entries, roles added only where a ruling below says so (none recommended).
- No verdict is "fixed" to match. `expected_properties` changes only where a preregistration names the row and the new value before the run; a run that disagrees is drift, entered in `docs/surprises.md`, never edited away (CONTRIBUTING, standing process).
- `phil rules diff --baseline data/verdicts-baseline.json` may show a changed row only where the preregistration predicted that exact row. Any other changed row stops the batch (Part C stop conditions).
- Gate (b) precommitted pairs (`isomorphic_to` sub-signatures on coverture-household, cps, police-crisis) are not touched. Nothing here edits a match row: coverture R2/R5/R6, police R2/R4/R11, cps R3/R4/R10 (the drop-one set).
- The ablation ranking tables of slices 1 and 2 are not re-derived; `phil rules ablate --entry X` is rerun only for the entries named per item, and reported as exploratory unless a prediction is written.
- Shanley, Stone, Mackie 1996 body, Spiro, Gavron, Geddes & Tennyson 2013 stay unread (closed access); nothing below pretends otherwise.

## 2. Part A: sourcing faithfulness items (still open)

Eight items. Batch 2 already landed: the mwpa-suit R16/R19 prose, coverture-us R6 `plain`, cps R1 re-pin to WIC 328 (provenance only), cps R11 `plain`, cps R8 (exception fluent), police-crisis R2/R11 (facility cares and holds), police R7/R12 (WIC 5152). Those are not re-listed.

Semantics that fix the predictions below (engine read today): `kind` is read only by `validate_institution` (`rules_lower.py` 322-327: a `strategy` with an `or_else` is an error; `sanctioner none` with an `or_else`, or a sanctioner with no `or_else`, is an error). `implicit` is read by gate (d) (`rules_gate.py` 276-277) and printed in ablation rows. The iso skeleton reads deontic, aim pattern, erased conditions and **whether `or_else` is non-null** (`rules_iso.py` 123, 221); it does not read `kind`, `sanctioner`, `plain`, `source` or `provenance`. `build.py` strips `plain`, `choices`, `provenance`, `sanctioner_review` from the JSON; `source` reaches the JSON but nothing reads it.

### A1. cps R1: the investigation duty is wider than WIC 328

Finding: R1 is `social_worker must (investigate w c) when (report_received c)`; WIC 328(a) (opened) triggers on "cause to believe" a child is described in s. 300 and scopes the inquiry to what the worker "deems necessary"; the only remaining pin is `cal-wic-328 s. 328(a)`. Residue from batch 2: the free-text `source` still opens "Cal. WIC 328 / Penal Code 11165.14: reports must be investigated" although P1 said 11165.14 is no longer cited.

Options:
- Re-source (prose): strike the 11165.14 clause from `source`; reword `plain` to "must open an investigation it deems necessary when it has cause to believe the child is described in s. 300; encoded as: every received report" and leave the rule. Zero engine effect.
- Re-encode (a): add free fluent `cause_to_believe(c)` to `initial_free`; R1 condition `(and (report_received c) (cause_to_believe c))`. Re-encode (b): `must` to `may` (the "deems necessary" discretion). (b) is wrong for the dataset: the duty exists; it is the trigger that is narrower.

Preregistered expectation for re-encode (a), k=6: cps rows unchanged (care_and_sanction_same_role holds_to_k: an implication, fewer reachable worlds cannot break it; care_assigned_by_sex, dependent_cannot_exit, subject_cannot_exit reachable: the world with cause_to_believe true still reaches them; no_standing_persists fails: the failing world remains). `phil rules diff` 0 changed of 192. Gate (b) PASS (R1 outside every sub-signature). UNSURE: the partial-match rule count in `phil rules iso` for cps~police-crisis ("4/10|9") may drop by one if cps R1 is currently paired with police R1 at guard level (both `must <act> when <one received-fluent>`); gate (b) reads only the sub-signature pairs, so this is a report change, not a gate change. Ablation `--entry cps`: R1 had no flips in batch 2; with a conjunctive trigger its deletion still deregulates `investigate`, so no flip expected; rerun and report.

Cost: 1 fluent, 1 condition, `initial_free`; ablation rerun for cps (minutes). Recommendation: re-encode (a) plus the prose fix. The statute's trigger is a real narrowing and it costs one free fluent; the tradeoff is one more exogenous fluent in cps's world space (seven already) for a verdict that does not move, so the gain is faithfulness and a card line that says what the statute says.

### A2. cps R11: standing through a guardian, not through counsel

Finding: R11 is `child may (petition c) when (counsel_appointed c)`; `has_standing(c) := (enabled petition c)`. WIC 388(a)(1) gives the petition to "the child ... through a properly appointed guardian"; 317(e) makes counsel the representative; 326.5 lets the attorney be the CAPTA guardian ad litem. Batch 2 reworded `plain` to say the simplification; the `source` string still reads "317(e): ... so the child claims in its own name through counsel".

Options:
- Re-source: align `source` with `plain` (counsel stands in for the guardian ad litem by 326.5; a disclosed simplification). No rule change.
- Re-encode: new fluent `guardian_appointed(c)`, either free (in `initial_free`) or set by a court action `appoint_guardian(court, c)`; R11 condition becomes `(guardian_appointed c)`; `counsel_appointed` then feeds nothing but R8.

Preregistered expectation for re-encode: no_standing_persists stays `fails` (the court's `can_claim_for` via `reassign_custody` under free `substantial_danger` already defeats the forall; and the guardian world gives standing as counsel did). Other four cps rows unchanged. Diff 0 of 192. Side effect worth naming: R8 (P2's exception) would then be idle for every property, not just at k=6; batch 2's reading "the exception is idle at k=6" becomes "the exception touches no property", which weakens the point of having landed P2.

Cost: 1 fluent (+1 action if established), R11 condition, derived fluent untouched; ablation rerun for cps. Recommendation: re-source only. In California dependency practice the appointed attorney is the guardian ad litem (326.5), so "counsel appointed" is the ordinary case rather than a distortion; re-encoding would spend a fluent to sever the one link that makes R8 matter. Tradeoff: the card keeps saying "counsel" where the statute says "guardian", disclosed in `plain`.

### A3. kibbutz-childrens-house R5 (visits "at any time") and R1 (unsourced committee)

Finding, R5: `male_member may (visit male_member child) when true`; the Wikipedia revision read (2026-06-23) has children visiting parents "for 2-3 hours a day" and fathers bonding "through quality time". `visit` has no effects and no derived fluent reads it. R1: `committee may (assign committee x) when (member x)`; no read passage names a committee or an assignment; provenance is `recalled` + `unverified`.

Options, R5:
- Re-source: reword `plain` to "may visit the child during the daily visiting time (2-3 hours; the read page has the children visiting the parents)"; rule unchanged.
- Re-encode: free fluent `visiting_time` in `initial_free`; R5 condition `(visiting_time)`. The no-implicit variant inherits it (it extends the base and does not replace R5).

Expectation for re-encode: none. `visit` sets nothing, so no property can see the condition; kibbutz and kibbutz-no-implicit rows unchanged (care_and_sanction_same_role violated, care_assigned_by_sex persists / fails, subject_cannot_exit reachable); gate (d) unchanged (R5 explicit in both, still matched); diff 0 of 192. Ablation: R5 load stays 0 (it was never ranked).

Options, R1: (i) leave `unverified`, extend `source` with the sentence "no read text names the committee; the work-assignment committee (sidur avoda) is the encoder's reconstruction; Spiro 1956 / Gavron 2000 are the leads, lending-only"; (ii) a human with an archive.org borrow searches Spiro or Tiger & Shepher for the assignment body and pins it. No rule option: R1 is the permission R2 (L6's implicit rule) bars, and the pair is built on it.

Cost: trivial either way; no ablation rerun needed (kibbutz R2 top-tie in slice 1 is untouched). Recommendation: R5 re-encode with the free fluent (cheapest honest fix, and the condition then reads what the page says), R1 option (i) now and (ii) when a borrow is available. Tradeoff: a fluent that constrains nothing, added only so the rule stops saying "at any time"; the alternative is a card that discloses the gap in prose and a rule that keeps overstating.

### A4. public-library R3: suspension without the warning step

Finding: R3 is `librarian may (suspend lb p) when (and (present p) (disruptive p))`; the Berkeley policy (opened, p. 2) warns first (B.1) and suspends on "Continued disruption" (B.2). public-library's one row is dependent_cannot_exit `open` (expected unreachable_open); it is a negative control, not a cluster member.

Options:
- Re-source: re-gloss the fluent: `disruptive` := "continued disruption after the B.1 instruction" (fluent gloss and `plain`: "may suspend a patron who continues to be disruptive after being warned (B.2)"). Rule unchanged.
- Re-encode: new action `warn(lb, p)` setting `warned(p)`; new rule R7 `librarian may (warn lb p) when (and (present p) (disruptive p))`; R3 condition gains `(warned p)`.

Expectation for re-encode: none. `can_exit(p) := (enabled leave p)` and `leave` is a default capacity no rule bars, so dependent_cannot_exit stays open; diff 0 of 192. Gate (b) controls: public-library has no `provides_care` fluent, so a new `may` rule cannot produce a care+control form; `not_isomorphic_to_control` unchanged. Ablation not needed (no slice ranks this entry).

Cost: re-gloss is prose; re-encode is 1 action, 1 fluent, 1 rule, 1 condition. Recommendation: re-gloss. The engine can see no difference, the entry is a control whose job is to not match, and a graduated sanction is a feature worth encoding only when a property reads it (none does). Tradeoff: the two-step structure the policy actually has stays out of the dataset; if the author wants Ostrom-style graduated sanctions as a future property, re-encode now while the source is open.

### A5. coverture-household R4 (and -us R4): the abjured-realm exception

Finding: R4 is `wife must_not (sue w) when (married h w)`, or_else null (disability); Blackstone Bk I ch 15 (opened) excepts a husband who "has abjured the realm, or is banished" (she then sues as a feme sole). The provenance note already records the gap; `plain` does not. coverture-household-us replaces R4 with the same text, so both files carry it; mwpa-suit drops R4.

Options:
- Re-source: `plain` gains "(unless the husband has abjured the realm or is banished)" in both files. No rule change.
- Re-encode: free fluent `husband_absent(h)` (abjured or banished) in `initial_free`; R4 condition `(and (married h w) (not (husband_absent h)))` in both files.

Expectation for re-encode: no_standing stays `reachable` in coverture-floor, coverture-household, -us, both composites and the five mwpa entries that inherit R4 (existential property; the husband-present world is still there); `has_standing` is read by nothing forall-shaped in these entries. Diff 0 of 192. Gate (b): R4 outside the sub-signatures, PASS. UNSURE: the iso partial-match count for coverture~cps / ~police may change by one if R4 is currently paired at guard level (cps and police have no `sue` rule, so probably not). Ablation `--entry coverture-household`: R4 deletion still deregulates `sue`, so its exit/standing flips are unchanged; rerun and report.

Cost: 1 fluent and 2 conditions (English and US files), coverture ablation rerun. Recommendation: re-source (prose) only; the finding is marked "minor" and the exception is exogenous to everything the cluster reads. Tradeoff: the exception stays prose; the card-only seat should accept a disclosed exception, and if it does not, re-encode is cheap and predicted clean.

### A6. coverture-household R7 (and -us R7): "void, or at least voidable"

Finding: R7 is `wife must_not (contract w) when (married h w)`, or_else null (disability); Blackstone's sentence says her deeds and acts during coverture are "void, or at least voidable", introduced (council 2026-11-06) as acts done "by his compulsion"; the second fragment concerns compacts between the spouses, not her capacity with third parties. The row is the stronger reading. `cannot_contract(w) := forall subject w, not (enabled contract w)`.

Options:
- Re-source: keep the disability; re-pin to the passage that states the incapacity rather than the compulsion sentence (Bk I ch 15's "the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband" and the "she cannot ... without her husband" run), and add to `plain` "(Blackstone: void or at least voidable; encoded as no power)". No rule change.
- Re-encode: a voidable act binds until avoided, so the faithful shape is `wife may (contract w)` plus `husband may (avoid h w)` (new action), or a sanctioned `must_not` with the husband's avoidance as `or_else`. Under ADR 0013 a sanctioned `must_not` only punishes exercise, so `contract` becomes enabled.

Expectation for re-encode: **cannot_contract holds_to_k -> violated** in coverture-floor, coverture-household, coverture-household-us, coverture-us-hospital-visitation, mwpa-creditor-exemption, mwpa-earnings, mwpa-property, mwpa-property-narrowed (8 rows); coverture-us-ssi, mwpa-sole-trader, mwpa-suit already violated (3 rows unchanged). Diff 8 changed of 192. The sole-trader minimal pair (mwpa-sole-trader = mwpa-earnings minus R7) then separates nothing on cannot_contract, and the MWPA backtest's `sole_trader` direction row loses its property. Iso: adding an `or_else` to R7 changes its skeleton key (`or_else is not None` is read), but R7 is in no sub-signature, so gate (b) PASS; UNSURE whether the English~US exact-level identity claim, if any exists, reads it. Ablation: R7 rows change for every entry in the chain; slice-1 ranking of coverture would need a rerun.

Cost: large (two files, 8 baseline rows, backtest ground truth, claims that name cannot_contract, both composites). Recommendation: re-source. Blackstone's general doctrine, and every secondary source the dataset cites, treat a married woman's contracts with third parties as void at common law; the quoted sentence is about acts under compulsion and is the wrong pin, not evidence that the power existed. Tradeoff: the dataset keeps a hard disability where the primary text, read literally at that sentence, says "voidable"; the author accepts a doctrinal reading over a literal one and the card says so. Needs the author's ruling because it decides whether the MWPA chain's contract column survives.

### A7. coverture-household-us R6: consent divorce as a second exit

Finding: R6 is `wife must_not (leave w) when (married h w)`, or_else null; Stevenson & Wolfers (opened) support "consent of both spouses or a demonstration of marital fault", not "no unilateral divorce in any US state before 1969" (nine states predate 1964). Batch 2 fixed `plain`. Residue: the entry's `source_text` (line 172) still says "Exit: no US state had unilateral divorce before 1969", the wrong sentence; and the R6 `source` string still opens "UNVERIFIED (leads, not opened 2026-11-05 ...)" ahead of the verification-pass text. Consent divorce (and B2's fault divorce, recorded 2026-11-05 as a later experiment) are exits the row does not encode. `leave` has no effects in coverture.

Options:
- Re-source (prose): rewrite `source_text`'s exit sentence to the consent-or-fault reading; trim R6's `source` so the opened text leads. No rule change.
- Re-encode (experiment first, on a copy, as B2 was planned): free fluent `exit_ground(h, w)` ("the husband consents to a divorce, or his fault is proved; exogenous"); R6 condition `(and (married h w) (not (exit_ground h w)))`. One fluent covers B1's two exits; a split into `consents` and `fault_proved` buys nothing a property reads.

Expectation for the re-encode experiment: subject_cannot_exit and dependent_cannot_exit stay `reachable` in -us, both composites and the six mwpa entries (existential; the no-ground world remains); no row changes because `leave` sets no fluent; diff 0 of 192. The MWPA chain's "standing before exit" reading (plans/backtest-mwpa.md) is unaffected as a verdict but its prose ("no exit at her own will") must say "no exit without his consent or his fault". Ablation: coverture R6 is the slice-1 top rule on load_freedom (L21's one blind hit); R6 deletion still deregulates `leave`, so its flips persist; UNSURE whether the conditioned R6 keeps the top rank alone or ties (the `R6~prohibit` variant may differ). Rerun `--entry coverture-household-us` and report. Note the English entry is not touched: coverture-household R6 (L1's match row) stays as it is, and the composites compose the US entry, so the composites' R6 moves with it.

Cost: 1 fluent, 1 condition in one file; ablation rerun for -us; prose in backtest-mwpa.md. Recommendation: prose fix now; the exit experiment as its own preregistration (Part C, batch 3d), landing only on the author's say-so. The author chose B1 on 2026-11-05 with B2 deferred; this is B2 plus consent, and it changes what "exit" means for the whole MWPA chain even though no verdict moves. Tradeoff: landing it makes the US entry say what the sources say at the price of an exogenous fluent that the exit properties, being existential, cannot see; not landing it keeps a row the card-only seat will keep flagging.

### A8. naming-convention R1, R2: design-only support; 25% not universal

Finding: R1 `member may (use_old m) when true`, R2 `member may (use_new m) when true`; Centola et al. 2018 (accepted manuscript, opened) support both only through the design (free-text entry each round, "occasional switching"), with no sentence stating a permission; the 25% threshold is "not expected to be a universal value". Residue: both `source` strings still say "NOT OPENED ... cited from memory, UNVERIFIED" while provenance says `opened`. The 25% lives in docs/theory (T7, untested) and the layer-2 gate band, not in any rule.

Options:
- Re-source: rewrite `source` to the manuscript (design sentences), `plain` to "may use the old/new name in any round (the game's free-text entry; a design feature, not a stated rule)"; retag `kind: strategy` (Part B row, the clearest case). No rule change.
- Re-encode: make `use_old`/`use_new` `default_capacity: true` and drop both rules (README convention: default capacities are not written as `may ... true`). Layer 1: `new_convention_adopted` stays `reachable` (both actions enabled by default). Layer 2 (frozen) needs a `may` rule per action under ADR 0015 A6, so the entry would stop running in `phil abm gate` (b); and a zero-rule entry has nothing to ablate.

Recommendation: re-source plus `strategy`. Tradeoff: two rules stay in the dataset that the dataset's own default-capacity convention says should not exist as rules; they stay because layer 2's enabledness convention (A6) needs them, which is a known inconsistency between the two layers' conventions worth a one-line note in the README, not a fix here.

## 3. Part B: kind reclassification and implied sanctions

Confirmed by reading: retagging `kind` cannot move a verdict, an iso match, a gate criterion or an ablation row. `kind` is read once, in `validate_institution`, to reject `strategy` with a non-null `or_else`. Every candidate for `strategy` below has `or_else: null` (checked: police-crisis R1, cps R6, paternity-quota R7, transferable-leave R7, ectogenesis R5, gestational-surrogacy R5, crisis-team R7, naming-convention R1, R2). What IS read: `implicit` (gate (d), ablation rows), `or_else` presence (iso skeleton, ablation), `default_capacity` (enabledness), `strand` (+strands iso levels, ablation strand agreement). So the rule for this part: a row that changes only `kind` is prose to the engine; a row that drops a rule, adds an `or_else` or touches `implicit` is an encoding change.

One prerequisite before any retag is reviewed: the cards do not show `kind` or the `sanctioner` value (build.py prints "(implicit)" and "(sanctioner derived, unreviewed)" in the deontic cell, nothing else). The card-only seat cannot judge a retag it cannot see. build.py needs a `kind` column and the sanctioner value in the "or else" cell first (a build change, no YAML; cards regenerate; no JSON change).

### B1. norm -> formal (written law tagged implicit for another reason)

| Rows | Reason |
|---|---|
| crisis-team R8 (WIC 5150(a)) | a statute |
| paternity-quota R9, transferable-leave R9 | reconstruction of the scheme |
| companion R6, R9, R11 (+ guardianship and renamed copies) | leash/impound law, property and standing doctrine |
| mwpa-* R10 (Blackstone creditor reach), R12 (Chused, trustee conveyance) | treatise and statute |
| footbinding R10 (explicit pledge commitment) | the pledge is an explicit act |

Verdict movement: none (kind only). `implicit` stays true on all of them: it marks "a norm nobody writes down" for gate (d) and the ablation rows, and the README says a rule can be implicit and formal. Source check before retag: crisis-team R8 is `recalled`, companion R6/R9/R11 are `unverified` (no text opened: "leash law" and "animals cannot sue" are general knowledge), paternity-quota/transferable-leave R9 are `unverified` reconstructions. `formal` means "written and enforced by a named body"; a rule with no opened text should not be promoted to `formal` on the strength of the reviewer's memory. Recommendation: retag crisis-team R8 (the 5150(a) text is opened on police-crisis R3 and the same words apply), mwpa R10/R12 (Blackstone Bk II ch 29 opened; Chused cited), footbinding R10; hold companion R6/R9/R11 and the R9 leave rows at `norm` with a `source` note "written law in substance, text not opened; retag when opened". Tradeoff: three entries keep a tag the reviewer thinks wrong, so that `formal` keeps meaning "we read the writing".

### B2. norm -> strategy (regularity nobody sanctions)

| Rows | Reason |
|---|---|
| police-crisis R1 (dispatch routine) | dispatch practice; nothing in 5150 requires it |
| cps R6 ("mother called first") | practice, unsanctioned |
| paternity-quota R7, transferable-leave R7 | the pattern the quota was introduced to break |
| ectogenesis R5, gestational-surrogacy R5 | "care-norm ... no sanction" |
| crisis-team R7 | the team can call police; practice |

Verdict movement: none; `validate` passes (all `or_else: null`). Caveat that matters: five of these are `must` rules (police R1, cps R6, the two R7s, the two R5s). The engine's `obliged` reads any `must` "sanctioned or not" (README), so `care_obliged` and the goods' guaranteed measure already treat them as duties; a `strategy must` is a contradiction in Bicchieri's terms (a strategy has no deontic bite) but not in the engine's. Options: (i) retag to `strategy` and accept "must" as "the regularity, written as an obligation so the engine can see who carries it"; (ii) leave `norm` and set `sanctioner: none` reviewed, reading "norm" loosely. Source check: none of the seven has an opened source; the retag rests on the encoder's own description ("implicit: ... practice"). Recommendation: (i) for police R1, cps R6, crisis-team R7, the leave R7s (the encoder's own `source` says unsanctioned practice in each case); for ectogenesis/surrogacy R5 see B6, where the same rows appear with the opposite proposal. Tradeoff: `strategy` on a `must` rule tells the reader "nobody enforces this" while the engine keeps enforcing it under strict compliance; the card must say both.

### B3. norm -> drop (default capacity)

| Rows | Reason |
|---|---|
| footbinding R2 (`family may leave_unbound`) | added for ADR 0015 A6 |
| kibbutz R8 (`metapelet may neglect when assigned`) | added for ADR 0015 A6 |

This row group is an encoding change, not a retag: the rule count changes, two ablation rows vanish, and the no-implicit / no-pledge variants inherit the drop. Faithful alternative per the README convention: mark `leave_unbound` and `neglect` `default_capacity: true` and drop the rules. Layer 1: a default-capacity action is enabled unless a disability bars it (`rules_lower.py` 737-741), which is what the `may ... when true` gave; so footbinding (binding_practised persists, marriage_requires_binding holds_to_k, exits reachable) and kibbutz rows are predicted unchanged, diff 0 of 192. Gate (d): R8 is in both kibbutz and its variant, so the diff set is unchanged. Layer 2 (frozen): ADR 0015 A6 wanted a `may` rule per enabled action; UNSURE whether the ABM honours `default_capacity` (grep found it only in `rules_lower.py`), so dropping these may make the footbinding ABM breaker unavailable if layer 2 is ever thawed. Recommendation: convert both to `default_capacity` in their own small preregistration (Part C, 3c), with the ABM question recorded as a known limit rather than tested. Tradeoff: the dataset stops carrying two rules that exist only for a frozen layer, at the risk of a one-line fix later if that layer thaws.

### B4. formal -> norm (practices tagged as written)

| Rows | Reason |
|---|---|
| kibbutz R1, R3, R4, R5 | Wikipedia practice source, no by-law |
| footbinding R1, R4, R6, R7 | Mackie convention, unwritten |

Verdict movement: none. Source check: kibbutz rows rest on the Wikipedia page (opened) and Tiger & Shepher (unverified); footbinding rows on Mackie's abstract (snippet) and three Wikipedia pages (recalled). `norm` = "unwritten, sanctioned by people": kibbutz R3 has `or_else R6` (peers, reviewed) so `norm` fits; R1, R4, R5 are permissions and a disability with no sanction, where `norm` means "practice" rather than "sanctioned". footbinding R6/R7 are the marriage-market sanction in Mackie's account (an unbound daughter is unmarriageable), which makes R1/R6/R7 a norm cluster in his sense even though each `may` carries no `or_else`. Recommendation: retag all eight; the sources, thin as they are, nowhere mention a written rule, and `formal` is the claim that needs writing. Tradeoff: kibbutz R4 (`child must_not sleep_home`, a disability) becomes a `norm` disability, a combination the README's "disability" bullet did not anticipate (it says a disability "is not a norm someone enforces"); the README bullet needs one clause: a disability can be customary.

### B5. formal -> strategy

| Rows | Reason |
|---|---|
| naming-convention R1, R2 | Centola tipping convention with no sanction |

Verdict movement: none; `validate` passes. Source check done (A8). Recommendation: retag, with A8's prose. Tradeoff: as A8.

### B6. `sanctioner: none` rows whose source implies a sanction the encoding never gave an `or_else`

These are encoding changes: a new `or_else` flips the iso skeleton bit for that rule (`rules_iso.py` 123) and, where the sanction needs a new action or role, changes the signature.

| Row | Implied sanction | What it would take | Can it move a verdict? |
|---|---|---|---|
| companion-ownership R5 (`owner must provides_care when owns`) | Penal Code 597(b) misdemeanour (`unverified`) | `or_else` to a prosecute rule; R4 `may prosecute when abandoned` does not fit (wrong condition), so a new R12 `state may (prosecute state o) when (and (owns o a) (not (provides_care o a)))`; `sanctioner: state`; copies in guardianship and renamed | **Verdicts: none** as long as `can_sanction` stays `(or (enabled euthanize o a) (exists x (enabled transfer o a x)))`. If the author also widens `can_sanction` to read `prosecute`, care_and_sanction_same_role holds_to_k -> **violated** in all three companion entries (owner cares, state sanctions), the same unbundling the police re-encode exposed. Iso: companion-ownership ~ companion-guardian-renamed stays exact if both get the rule; guardianship ≠ ownership (L5) stays. |
| lease R2 (`landlord must habitable when leased`) | Civ. Code 1942 repair-and-deduct or rent withholding (text not opened; 1941 is) | new action `repair_and_deduct(t)` and rule; `or_else`; sanctioner has no fitting value (the counterparty is not state/institution/peers/family/self): a vocabulary gap | None (dependent_cannot_exit open; no `provides_care` in lease, so gate (b) controls unaffected) |
| ectogenesis R5, gestational-surrogacy R5 | Kleven motherhood penalty (peers) | a `peers` role and a penalise action in both entries; cardinality | None under strict compliance; but this row contradicts B2, where the same rules go to `strategy` |
| coverture R2 (`husband must provides_care when married`) | necessaries enforced through creditors (inference, not text) | a creditor role and action; `or_else` on R2 | **Do not touch.** R2 is the care leg of all three precommitted pairs (coverture R2 ~ cps R4 ~ police R2) and `load_bearing: true`; the iso skeleton reads `or_else is not None`, so an `or_else` on R2 alone breaks the care match and fails gate (b) outright. |

Recommendation: companion R5 as its own experiment on a copy, in two steps (R12 + `or_else`, then the `can_sanction` widening), each predicted before the run; the second step is the interesting one and the author should decide whether companion-ownership is meant to pass care_and_sanction_same_role (the dataset's note says the owner both cares and may euthanise, which is the bundle the property is for; the state's power is a second sanctioner, as the officer was). lease R2: open Civ. Code 1942 first; if opened, encode with a `sanctioner` value the author names (proposal: add `counterparty` to the vocabulary, an engine schema change, or use `state` on the ground that the remedy is court-backed). ectogenesis/surrogacy R5: `strategy` (B2), not a peers sanction; Kleven's penalty is a labour-market outcome, and calling it a peer sanction on a rule would be an encoder's story. coverture R2: no. Tradeoff on companion: a second preregistration and a probable violated row in three entries, which is a finding about the encoding of `can_sanction` (it reads only the owner's powers) more than about pet ownership; the alternative is leaving an opened-statute sanction unencoded while the entry claims a bundled sanctioner.

### B7. Leftovers from the sanctioner review

- ectogenesis R3 `or_else R6` (registry reprimand; `sanctioner: institution`, derived): the registry sanction is an encoder invention (ectogenesis.yaml line 212). Options: drop the `or_else` (R3 becomes an unsanctioned `must`, sanctioner none; the R6 rule stays or goes) or leave with a `source` note. Expectation for dropping: none under strict compliance (ectogenesis rows: birth_labor_rival violated, care_assigned_by_sex violated, care_decoupled_from_birth reachable, solo_care reachable); the iso skeleton bit on R3 flips, and ectogenesis~gestational-surrogacy is claimed iso at guard (surrogacy replaces R3, so check whether the replacement keeps `or_else R6`; if only one side drops it, the guard-level claim fails). Recommendation: drop in both files, predicted clean on verdicts, with the iso claim named in the preregistration.
- `sanctioner_review: derived` on every rule the batch touches is removed once reviewed; the key is YAML-only and the cards stop printing "unreviewed".

## 4. Part C: ordering and preregistration

Four preregistrations, run in this order; each is written in plans/sourcing.md (Part A items) or plans/informal-rules.md (Part B items) and committed before its first run, with `phil rules diff --baseline data/verdicts-baseline.json --no-cache`, `phil rules gate`, `scripts/drop_one_match.py`, `build --check` and `pytest` as the fixed checks.

**3a. Prose and provenance (lands; no engine effect).** cps R1 `source` (strike 11165.14), cps R11 `source` aligned with `plain`, coverture-us `source_text` exit sentence and R6 `source` lead, coverture R4 `plain` exception (both files), coverture R7 re-pin and disclosure (both files), kibbutz R1 note, naming-convention `source` rewrite, public-library `disruptive` re-gloss. Prediction: 0 changed of 192, gate PASS unchanged, check-all 192/192. Certain, by the same argument as batch 2 P1 (`plain`/`source`/`provenance` do not reach the lowering). Council: card-only seat only (does each plain line now say what the source says).

**3b. Kind and sanctioner retags (lands; no engine effect).** Prerequisite: build.py card columns for `kind` and the sanctioner value. Then B1 (crisis-team R8, mwpa R10/R12, footbinding R10), B2 (police R1, cps R6, crisis-team R7, paternity-quota and transferable-leave R7, ectogenesis and surrogacy R5), B4 (eight rows), B5 (two rows), and `sanctioner_review` removal across them. Prediction: `phil rules diff` 0 changed of 192; `build --check` ok (no `strategy` with `or_else`); gate unchanged; ablation untouched. Council: faithfulness seat reads each retag against the cited text (and refuses any B1 promotion whose text is not opened); card-only seat reads the new columns.

**3c. Re-encodes predicted clean (land).** A1 cps R1 (`cause_to_believe`), A3 kibbutz R5 (`visiting_time`), B3 (footbinding R2 and kibbutz R8 to `default_capacity`), B7 ectogenesis R3 `or_else` drop. Prediction per item as above; combined: 0 changed of 192, gate PASS, drop-one set unchanged, check-all 192/192; `phil rules iso` partial counts for cps~police may shift by one rule (reported, not a stop); ectogenesis~surrogacy guard claim holds (both files edited). Ablation reruns `--entry cps`, `--entry kibbutz-childrens-house`, `--entry footbinding`, `--entry ectogenesis`: exploratory, no ranking prediction beyond "R1/R5 loads 0; the dropped rows absent". Council: correctness (new free fluents add worlds: confirm no forall property became vacuous; confirm `default_capacity` enabledness equals the dropped `may`), faithfulness, card-only.

**3d. Experiments on copies (do not land without a ruling), one preregistration each.** A7 US exit ground (`exit_ground`), A6 R7 voidable (only if the author rejects the re-source recommendation; 8 rows predicted to move), B6 companion R5 sanction in two steps. Each reports diff rows, gate, iso and ablation against its predictions; landing any of them is a second, separate decision with its own expected_properties edits named in advance.

What the council must see, every batch: the preregistration commit hash, the diff/gate/drop-one output verbatim, the surprises ledger entry (or "none"), and for the card-only seat the regenerated cards of every touched entry. The faithfulness seat gets the source excerpts already in `provenance`, not the YAML.

Stop conditions (any one stops the batch before the next step; the preregistration is not edited): a `phil rules diff` row moves that the preregistration did not name; `build --check` fails on a kind/sanctioner/or_else rule; gate (b) reports a precommitted pair unmatched; `scripts/drop_one_match.py` names a different set from coverture R2/R5/R6, police R2/R4/R11, cps R3/R4/R10; check-all falls below 192/192 on a batch predicted clean; the card-only seat answers "cannot tell" on a touched rule (that fails the entry on legibility and the batch pauses for a fix pass, per ADR 0014).

## 5. Decision table

| Item | Recommendation | Needs author ruling? | Can move a verdict? |
|---|---|---|---|
| A1 cps R1 | re-encode with `cause_to_believe` + prose fix | no (apply unless vetoed) | no (iso partial count may shift) |
| A2 cps R11 | re-source only; keep counsel as the guardian ad litem stand-in | yes (re-encode would idle R8 entirely) | no |
| A3 kibbutz R5 | re-encode with `visiting_time` | no | no |
| A3 kibbutz R1 | note as unsourced; pin when a borrow is possible | no | no |
| A4 public-library R3 | re-gloss `disruptive` as continued disruption after warning | yes (re-encode is the alternative) | no |
| A5 coverture R4 (both files) | prose exception only | no | no |
| A6 coverture R7 (both files) | re-source and re-pin; keep the disability | **yes** | re-encode: yes, 8 cannot_contract rows and the sole-trader pair |
| A7 coverture-us R6 | prose now; exit-ground experiment on a copy | **yes** (B1 was the author's 2026-11-05 choice) | no on verdicts; changes what "exit" means in the MWPA chain |
| A8 naming-convention R1, R2 | re-source; `kind: strategy` | no | no |
| B1 norm -> formal | retag crisis-team R8, mwpa R10/R12, footbinding R10; hold companion R6/R9/R11 and leave R9s until text is opened | yes (the hold) | no |
| B2 norm -> strategy | retag all seven; `must` kept, card says unenforced | yes (`strategy must` reading) | no |
| B3 norm -> drop | `default_capacity` on `leave_unbound`, `neglect`; drop R2/R8 | yes (layer-2 A6 limit) | predicted no; rule count and ablation rows change |
| B4 formal -> norm | retag all eight; README disability clause | no | no |
| B5 formal -> strategy | retag | no | no |
| B6 companion R5 | experiment: R12 + or_else, then widen `can_sanction` | **yes** | step 2: yes, care_and_sanction_same_role in 3 entries |
| B6 lease R2 | open Civ. Code 1942 first; sanctioner vocabulary gap | yes (vocabulary) | no |
| B6 ectogenesis/surrogacy R5 | `strategy`, not a peers sanction | yes (two review rows conflict) | no |
| B6 coverture R2 | do not touch | no | yes if touched: breaks the care leg, gate (b) FAIL |
| B7 ectogenesis R3 registry sanction | drop `or_else` in both files | no | no on verdicts; iso guard claim must hold both sides |
| Card columns for kind/sanctioner | build.py change before 3b | no | no |

## 6. Author rulings (2026-11-08, after reading sections 2–5; nothing above edited)

| Item | Ruling |
|---|---|
| A1 cps R1 | apply as recommended (re-encode with `cause_to_believe`, prose fix) |
| A2 cps R11 | re-source only; counsel stands in for the guardian ad litem (326.5), disclosed |
| A3 kibbutz R5 / R1 | apply as recommended |
| A4 public-library R3 | re-gloss `disruptive` as continued disruption after the warning; no new rule |
| A5 coverture R4 | prose exception only |
| A6 coverture R7 | **re-source, keep the disability**; re-pin to the incapacity passage; card says "encoded as no power" |
| A7 coverture-us R6 | **prose fix now**; `exit_ground` experiment as its own preregistration (3d), lands only on a later say-so |
| A8 naming-convention | re-source; `kind: strategy` |
| B1 norm → formal | **retag only the four with opened text** (crisis-team R8, mwpa R10/R12, footbinding R10); hold companion R6/R9/R11 and the leave R9s at `norm` with the "text not opened" note |
| B2 norm → strategy | **retag all seven**, `must` kept; the card states both: nobody enforces it, the engine still reads a duty. Resolves the ectogenesis/surrogacy R5 double listing in favour of `strategy` |
| B3 norm → drop | **convert to `default_capacity`** in their own preregistration (3c); ABM question recorded as a known limit |
| B4, B5 | apply |
| B6 companion R5 | **two-step experiment on a copy** (R12 + `or_else`, then widen `can_sanction`), each predicted before its run; land decision after step 2 |
| B6 lease R2 | open Civ. Code 1942 first; sanctioner vocabulary question deferred until then |
| B6 coverture R2 | do not touch |
| B7 ectogenesis R3 | apply |
| Card columns | apply before 3b |

Also ruled today, outside this brief: SSI revision 2 item 1 (add `cohabits`) and item 5 (sex unencoded), plans/ssi-entry.md; hospital "guarantee lost, possibility kept" = displaced, to the patient, plans/informal-rules.md.

## 7. Sub-batch 3d experiments (on copies; nothing lands)

Preregistered 2026-11-08 on worktree branch fb-3d (off main ede08bc; ENGINE_PIN e46f6ea), before any run. Every edit below is made on a copy of `data/institutions/` in the session scratchpad (`.../scratchpad/batch3d/<variant>/`), built with that copy's own `build.py --write` (it resolves `src/` next to itself), and run with `--institutions`/`--properties` pointing at the copy. Nothing under `data/`, `docs/cards` or the baseline is touched; the control copy (`clean/`) rebuilds byte-identical to the committed JSON (checked before this text was written). Fixed checks per variant: `phil rules diff --baseline data/verdicts-baseline.json --no-cache`, `phil rules check-all --no-cache`, `phil rules gate`, `phil rules iso --pair` for the pairs named. Drift rule as everywhere: this section is not edited after a run; results go under "Results" below it, with the drift named.

### 7.1 Experiment 1: US exit ground (A7)

Edit (copy of `coverture-household-us.yaml` only): `fluents_add` a fluent `exit_ground` (arity 2, no `arg_roles`; gloss: the husband consents to a divorce, or his marital fault is proved; exogenous: no action sets it) and R6 `conditions: (and (married h w) (not (exit_ground h w)))`, `plain` reworded to match. Design note, found while reading the engine before writing this (rules_lower.py module doc "init"): the US entry declares no `initial`/`initial_free`, so it runs in `empty` mode, where a fluent no effect touches is free at t=0 and persists; the brief's "add to `initial_free`" is therefore satisfied by declaring the fluent, and adding an `initial_free` list to the US file would switch it to `declared` mode and pin `female`, `acquired_property`, `earns` false, a different experiment. Consequence that the brief did not state: coverture-floor, the six mwpa entries (own `initial_free: [female, acquired_property, earns]`) and both composites (`initial_free: [acquired_property, earns]`) are in `declared` mode and do not list `exit_ground`, so there it is pinned false at t=0 and the conditioned R6 is extensionally the committed R6. The experiment as scoped changes the semantics of one entry; a landing would have to add `exit_ground` to four `initial_free` lists (floor, mwpa-creditor-exemption, the two composites) for the chain to inherit the exit, and that is listed under the landing decision, not run here.

Predictions (stated before the run):
- P1.1 `diff`: 0 changed, 0 added, 0 removed of 192. In -us, `subject_cannot_exit` and `dependent_cannot_exit` are existential, and the world with `exit_ground(husband, wife)` false at t=0 remains; `leave` sets nothing and no other property or goods formula reads `can_exit` except `chosen_mutual_care`, which `care_obliged` already blocks at every married step. In the ten descendants the fluent is pinned false (design note).
- P1.2 `check-all`: 192/192. `gate`: PASS, every criterion as on main (the US entry is not a CLUSTER member; (b) reads only coverture-household, police-crisis, cps claims).
- P1.3 `iso --pair coverture-household-us coverture-household`: the entry's own `isomorphic_to` claim at `exact` FAILS (R6's condition structure now differs: `and`/`not`/`exit_ground` against `married`); with `--cond guard` the pair still matches (both R6 conditional). This does not reach the gate but is a landing cost: the -us claim would have to be downgraded to `guard` (or the fluent read as the paper's consent-or-fault and the claim rewritten).
- P1.4 `ablate --entry coverture-household-us --k 6,8 --workers 4 --step-mode one`, against a control run of the same command on the clean copy: identical rows. The brief says UNSURE whether R6 keeps the top load_freedom rank alone; my prediction is that it keeps it alone with the same flipped properties as the control, because `exit_ground` enters only R6 and the deleted-R6 variant does not contain it; R6 is a `must_not`, so it has no `~prohibit` row that could read the condition differently. No row names `exit_ground`.

### 7.2 Experiment 2: companion R5 sanction (B6), two steps plus one diagnostic

Files: copies of `companion-ownership.yaml` and `companion-guardian-renamed.yaml` (the renamed entry is a standalone file with its own R5 and `can_sanction`; `companion-guardianship` `extends` ownership and inherits both edits). Both entries already have a `state` role and a `prosecute(state, o)` action regulated by R4.

Step 1 edit: add R12 `state may (prosecute state o) when (and (owns o a) (not (provides_care o a)))` (renamed: `(prosecute state g)`, `var_roles g: guardian`), `kind: formal`, `strand: rival`, `sanctioner: none`, `or_else: null`, source Cal. Penal Code 597(b) marked UNVERIFIED (the section was not opened for this experiment; it is cited from R5's own provenance item, `verification: unverified`). R5: `or_else: R12`, `sanctioner: state`. Predictions: P2.1 `diff` 0 changed of 192 (under `strict` compliance `or_else` plays no part in the lowering; `can_sanction` reads only euthanize and transfer; `(enabled prosecute ...)` is read by nothing). P2.2 `check-all` 192/192, `gate` PASS with (f) unchanged: `iso --pair companion-ownership companion-guardian-renamed` still a pure rename (both get R12 and the `or_else` bit), `iso --pair companion-ownership companion-guardianship` still not iso at distance 1 (R9). P2.3 the copy's `build.py --write` validates (R5 is `formal`, so the strategy/or_else rule does not fire; `sanctioner: state` matches the new `or_else`).

Step 2 edit (on top of step 1): widen `can_sanction` in both files to `(or (enabled euthanize o a) (exists ((x agent)) (enabled transfer o a x)) (exists ((x agent)) (and (enabled prosecute o x) (owns x a))))`, read as: o holds a power to coerce a if o may prosecute a's owner. Run twice: 2a-i with the fluent's `arg_roles: [owner, animal]` kept, 2a-ii with `arg_roles` removed. Predictions: P2.4 (2a-i) 0 changed of 192: the tuple `can_sanction(state, animal)` lies outside `arg_roles` and is constant false by the engine's typing rule, so the widened body is inert by construction. P2.5 (2a-ii), my prediction against the brief's: `care_and_sanction_same_role` STAYS `holds_to_k` in all three companion entries, 0 changed of 192. Reason: the property conjoins `provides_care x y` with `can_sanction z y` at the same step; `provides_care` is typed `[owner, animal]` so the only carer is the owner; R12 is enabled only while `(not (provides_care owner animal))`; the two cannot co-hold. The brief's "violated in all three" would need a sanction power that stands while care is given (as police R11's `hold` stands under `danger`), which 597(b) as encoded does not: the prosecution is for the breach, and the derived power is live only during the breach. P2.6 `gate` PASS; (b) control set unchanged (the (b) criterion does not read companion entries).

Diagnostic 2b (mechanism check only, not a landing candidate; it is an unfaithful "standing threat" reading of 597(b)): on top of 2a-ii, change R12's condition to `(owns o a)`. Predictions: P2.7 `care_and_sanction_same_role` `holds_to_k` → `violated` in exactly companion-ownership, companion-guardianship, companion-guardian-renamed: 3 changed of 192, nothing else. P2.8 `gate`: (e) agreement falls by 3 rows but stays above 0.60 (PASS); (f) unchanged (both edited alike). If 2b flips and 2a-ii does not, the brief's suspicion is confirmed in a sharper form: the verdict is about how `can_sanction` encodes the time at which a sanction power is held (live during the breach vs standing), not about pet ownership.

Commands, verbatim pattern (`P=/Users/rees/Documents/computational-liberation/.venv/bin/phil`, `V=<variant dir>`): `$P rules diff --baseline data/verdicts-baseline.json --institutions $V/institutions.json --properties $V/properties.json --no-cache`; `$P rules check-all ... --no-cache`; `$P rules gate ...`; `$P rules iso --pair A B ...`; `$P rules ablate --entry coverture-household-us --k 6,8 --workers 4 --step-mode one ... --json $V/ablate-us.json --summary $V/ablate-us-summary.json`.

### 7.3 Results (run 2026-11-08 after commit 527ebf0; engine e46f6ea, z3 5.3.3, k=6 strict step_mode one; scratch `batch3d/{clean,exp1,exp2s1,exp2s2i,exp2s2ii,exp2b}`, not kept)

Every variant's copy built (`wrote institutions.json (33) and properties.json (43)`); the control copy rebuilt byte-identical to the committed JSON.

**Experiment 1 (exit_ground).** `diff`: `0 changed, 0 added, 0 removed (of 192 rows)`. `check-all` / gate (e): `agreement 192/192 = 100%`. `GATE PASS`, (b) line identical to main. P1.1, P1.2 held. `iso --pair coverture-household-us coverture-household`: `iso=False pure_rename=False distance=1 matched=6/7|7 strands=off cond=exact` (`unmatched coverture-household-us: R6; coverture-household: R7`; the matcher pairs -us R7 with base R6, `action map: contract->leave`); with `--cond guard`: `iso=True pure_rename=True distance=0 matched=7/7|7`. P1.3 held, with one unpredicted detail: at exact the matcher crosses R7 onto R6, so the report names R7, not R6, as the unmatched base rule. Ablation (`--entry coverture-household-us --k 6,8 --workers 4 --step-mode one`), control vs exp1: ranked block identical in order and loads, R4, R6, R7 each `load_freedom 1/1`, R2 and R3 `0/0` (goods only); R6 row, control: `dependent_cannot_exit:reachable>open[freedom_up], subject_cannot_exit:reachable>open[freedom_up], subject_cannot_exit_persists:persists>fails[freedom_up]`; exp1: `dependent_cannot_exit:reachable>open[freedom_up], subject_cannot_exit:reachable>open[freedom_up]`. Drift against P1.4, two parts: (i) R6 does not hold the top rank alone in either run; it is a three-way tie with R4 and R7 at 1/1 (the brief's "slice-1 top rule" is coverture-household's row, and in the US entry the tie pre-exists this experiment; my "keeps it alone" was wrong about the control, not about the change); (ii) the rows are not identical: the forall-shaped `subject_cannot_exit_persists` (an ablation-only check here, not in -us's `expected_properties` or the baseline) already fails in exp1's base, because the world with `exit_ground` true at t=0 gives the wife `can_exit` at every step, so deleting R6 no longer flips it. The existential exit twins are blind to the fluent, as predicted; the persists twin sees it. No row names `exit_ground`. Reading: landed, `exit` for the MWPA chain would mean "no dissolution without the husband's consent or his proved fault" rather than "no exit at her own will", and the chain would see it only if `exit_ground` is added to the four `initial_free` lists (floor, mwpa-creditor-exemption, both composites), since in `declared` mode it is pinned false; the baseline would not move, but the -us `isomorphic_to: coverture-household exact` claim would have to be downgraded to `guard`, and the persists twin of the exit property would stop holding wherever the fluent is free.

**Experiment 2 (companion R5 sanction).** Step 1: `diff` `0 changed, 0 added, 0 removed (of 192 rows)`; `agreement 192/192`; `GATE PASS`, (f) `renamed~ownership iso=True pure_rename=True; guardianship~ownership iso=False distance=1 (R9 vs R9)`; `iso --pair companion-ownership companion-guardian-renamed`: `iso=True pure_rename=True distance=0 matched=12/12|12 ... cond=exact`, R12->R12 matched; ownership ~ guardianship `iso=False distance=1 matched=11/12|12` (R9 unmatched). P2.1, P2.2, P2.3 held. Step 2a-i (body widened, `arg_roles` kept): `0 changed, 0 added, 0 removed (of 192 rows)`, `192/192`, `GATE PASS`. P2.4 held: the widening is inert while `can_sanction` is typed `[owner, animal]`. Step 2a-ii (`arg_roles` removed): `3 changed, 0 added, 0 removed (of 192 rows)`, rows `companion-guardian-renamed`, `companion-guardianship`, `companion-ownership`: `care_and_sanction_same_role [invariant]: holds_to_k -> violated`; `agreement 189/192 = 98%`; `GATE PASS` with (b) line identical to main and (f) unchanged (iso pair still `pure_rename=True`, guardianship still `distance=1 (R9 vs R9)`). **Drift against P2.5**: the brief's prediction held and mine failed. The counterexample (`check --trace`, companion-ownership): t=2 `transfer(owner, animal, court)` (R1's `o2` is untyped, warning `R1: untyped variable(s) ['o2'] range over all agents`, so the court can take title); t=4 `abandon(owner, animal)` by the former owner, unbarred because R3 is conditioned on `owns`, which sets the sticky `abandoned(animal)`; t=5 `acquire(owner, animal)`; t=6 `provides_care(owner, animal)` and `can_sanction(state, animal)` both true. The live power is R4 (`prosecute when abandoned`), not R12: `abandoned` never clears, so once set the state's prosecution power stands under renewed care. R12 itself behaves as I predicted (its condition is the negation of care), which the diagnostic confirms from the other side. Diagnostic 2b (R12 on `(owns o a)`): `3 changed ... (of 192 rows)`, the same three rows `holds_to_k -> violated`, `189/192`, `GATE PASS`, (f) unchanged. P2.7, P2.8 held. Reading: the flip is a finding about how `can_sanction` is encoded, not about pet ownership, and more specifically than the brief suspected: widening the fluent to prosecution makes it read every prosecute rule, and the one that bites is the pre-existing abandonment rule through a fluent (`abandoned`) nothing ever resets and a transfer to an untyped third party, a route a faithful 597(b) rule (R12 as conditioned) cannot open on its own. Landing step 2 as a verdict about ownership would be an encoder's artefact until `abandoned` is cleared by `acquire`/`impound` and R1's `o2` is typed.

Surprises for docs/surprises.md (to be entered by whoever lands or closes this sub-batch; none entered here, since the ledger is under the other agent's files): S-3d-1 the persists twin flip under exit_ground (artefact of scope: a free exogenous fluent is visible to forall properties, invisible to existential ones; predicted direction, unpredicted row); S-3d-2 the 2a-ii flip via R4 and sticky `abandoned` (artefact candidate; my prediction wrong, the brief's right for a reason neither stated).

Landing decision: author.
- Exp 1 would touch: `data/institutions/src/coverture-household-us.yaml` (fluent, R6 condition, plain, `isomorphic_to` level exact -> guard), `initial_free` of coverture-floor, mwpa-creditor-exemption and both `_composites.yaml` entries, cards for the ten descendants, plans/backtest-mwpa.md exit prose; baseline rows: none; claims: the -us exact-iso note in docs/claims.md and the MWPA "standing before exit" reading.
- Exp 2 step 1 would touch: `companion-ownership.yaml`, `companion-guardian-renamed.yaml` (R12, R5 `or_else`/`sanctioner`), three cards, plans/informal-rules.md B6 row; baseline rows: none; claims: none (L5 and gate (f) unchanged).
- Exp 2 step 2 would touch the same two files (`can_sanction` body and `arg_roles`) plus `expected_properties` of three entries, three baseline rows (`care_and_sanction_same_role` holds_to_k -> violated), and the care+control bundle reading of the companion entries in docs/claims.md; not recommended before the `abandoned` reset and `o2` typing are fixed and re-predicted.

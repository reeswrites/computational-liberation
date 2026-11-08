# ssi-marriage-penalty entry and pair (2026-11-08)

Status: PREREGISTERED (commit ba5b4b0, before any run); RUN 2026-11-08, results recorded under "Results" below; COUNCIL DONE 2026-11-08 (docs/reviews/2026-11-08-ssi-{correctness,faithfulness,card-only}.md; faithful with reservations); MECHANICAL FIX PASS APPLIED (wording, pins, levels; no verdict moved); REVISION 2 AWAITS THE AUTHOR (section at the end). The preregistration sections are unedited. Written and committed before the first `phil rules check`, `ablate` or `diff` over either entry. Engine: ENGINE_PIN b5fd019. Branch `ssi-entry`. Inputs: plans/sourcing-worklist-marriage.md section 5 (Entry 2) and its Gaps, docs/connections.md section 4 (C2), plans/disability.md (SSI), plans/composition.md, ADR 0018, data/institutions/src/lease.yaml as the model.

## What was built

- `data/institutions/src/ssi-marriage-penalty.yaml`: roles claimant, spouse, agency. Base fluents `married`, `cohabits`, `holds_out`, `resources_under_limit`; derived power fluents `couple_rate`, `couple_limit`, `individual_rate`, `individual_limit`, `eligible` (each reads `enabled` of an agency action, the convention of `can_sanction` and `has_standing`). Seven rules: R1 agency may pay a benefit; R2 may apply the couple rate when married; R3 may apply the couple resource limit when married; R4 may apply the couple rate when cohabiting and holding out (the displaced gate); R5, R6 individual rate and limit when neither married nor holding out; R7 disability: must_not pay when resources are not under the limit. `function:` on R2 (`penalises_marriage_rate`), R3 (`penalises_marriage_limit`), R4 (`extends_penalty_to_holding_out`).
- `ssi-marriage-penalty-individual`: the pair, penalty removed. R2, R3, R4 dropped; R5, R6 lose their marital-status condition. **Holding out is dropped, not kept**: with no couple rate there is nothing for the test to gate, and no reform text was read that retains it (S. 73 of 2025 is an unopened lead).
- Five new properties in `properties.yaml`, which are encoding checks (each restates one rule), not findings (the 34 older ones all need fluents this entry does not declare): `married_couple_rated`, `married_couple_limited` (both freedom/unfreedom, invariant: the penalty holding), `penalty_reaches_unmarried` (failure_mode, reachable), `married_rated_individually` (structure, reachable: the penalty absent), `over_limit_ineligible` (freedom/unfreedom, invariant). Names, formulas and kinds are fixed here, before the run.
- Six bibliography works in `data/sources/rules.yaml`. Every provenance excerpt was carried from the worklist, whose fetches returned model summaries rather than raw text; none was re-opened by the builder. After the council all carried rows are `snippet` (ADR 0017 s.3), not `opened`; the faithfulness seat confirmed 416.1802(b)(1) and (d)(1), 416.1806(a)(3) and 1382(a)(3)(A)-(B) verbatim from raw text.

## Declared deviations from the brief (before the run)

1. R4 has `sanctioner: none`, not `state`, because R4 is an agency `may` power with no duty to sanction (the engine also rejects a sanctioner without an `or_else`). Overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule. This is not "no sanction in any source". The displaced reading therefore cannot use a sanctioner difference; it can read attribute sets only. (Wording corrected after the council, 2026-11-08; the earlier reason was wrong.)
2. Rules are `may` powers, not the statute's mandatory `must`: an action `must` fires every step and blocks every other action (ADR 0009), and a must-be needs the establishing action to carry the rate. The penalty is therefore represented as a power the rules grant. Because an action no rule names stays free in traces, only the derived fluents see the rules; this is why every property here reads a derived fluent.
3. Holding out is a second route to the couple rate on the same aim as R2, not a rewrite of `married`, because a derived fluent cannot read `married or holds_out`.
4. Dollar amounts ($2,000 / $3,000; $994 / $1,491) are not representable; only which limit and rate the agency may apply.
5. "Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to benefits rules by the author, 2026-11-08."

## Preregistered verdicts (k = 6 and 8, `--init declared`, strict, step-mode one)

| Property | ssi-marriage-penalty | ssi-marriage-penalty-individual |
|---|---|---|
| married_couple_rated | holds_to_k (non-vacuous) | violated |
| married_couple_limited | holds_to_k (non-vacuous) | violated |
| penalty_reaches_unmarried | reachable | unreachable_open |
| married_rated_individually | unreachable_open | reachable |
| over_limit_ineligible | holds_to_k (non-vacuous) | holds_to_k |

The 34 older properties: all `not_applicable` on both entries (no fluent they need is declared except `married`, which no older property reads alone). Any older property that turns out applicable is a miss on this line.

Why these: in the base, R2 gives every married pair the couple-rate power, R3 the limit power, R4 gives the power to a cohabiting holding-out pair (so a non-married pair can have it), nothing grants an individual rate to a married pair (R5's condition excludes marriage), and R7 bars payment over the limit. In the pair no rule names `apply_couple_rate` or `apply_couple_limit`, so the derived couple fluents are constant false (the engine warns), and R5 grants the individual rate to married pairs.

## Preregistered ablation of the base (`phil rules ablate --entry ssi-marriage-penalty`, k 6,8)

Flips expected, per deleted rule, among the five new properties:

| Deleted | Expected flip | Rationale |
|---|---|---|
| R1 | none | R7 still names `pay_benefit`, but no `may` remains, so `eligible` is false throughout, which makes `over_limit_ineligible` true as before. A deregulation flag may appear; it is not a verdict flip. |
| R2 | married_couple_rated holds_to_k -> violated | a married pair that is not holding out has no couple-rate power; R4 does not cover it |
| R3 | married_couple_limited holds_to_k -> violated | nothing else grants the couple limit |
| R4 | penalty_reaches_unmarried reachable -> unreachable_open | the only non-marriage route to the couple rate is gone |
| R5 | none | no property reads the individual rate except through `married`, and R5 excludes marriage |
| R6 | none | no property reads `individual_limit` |
| R7 | over_limit_ineligible holds_to_k -> violated | R1 still grants the power and nothing bars it |

Total expected flips: 4 rules with one flip each (R2, R3, R4, R7); three rules with none (R1, R5, R6). `function:` predictions are the same three rows: deleting R2, R3, R4 flips respectively the property named; an unsupported function (no flip) would be recorded as such.

## C2, first half (docs/connections.md section 4)

Claim as written: an SSI/Medicaid asset-and-marriage entry will not match the care+control cluster at any level, and deleting its marriage-penalty rule alone flips nothing among the existing properties.

Preregistered here:

- (i) `phil rules iso` of `ssi-marriage-penalty` against coverture-household, police-crisis, cps and lease reports no match at any level (the entry has no care strand and no `provides_care`, `is_subject`, `can_sanction` or `can_exit`).
- (ii) Deleting R2 (and, separately, R3) flips none of the 34 older properties, because all 34 are `not_applicable` on the standalone entry.
- Expected reading: (ii) holds **vacuously**. A check over properties that are not applicable cannot fail, so it is evidence recorded, not evidence for. The claim stays `untested` unless an older property is applicable and unflipped. The flips in the table above (R2 flips `married_couple_rated`) are among five new properties written for this entry; the claim as written names the existing ones, so they neither support nor refute it. The second half (deleting it in the composite flips `financial_dependence`) is P2 and is not run here.

## `phil rules diff` over the existing 27 entries

Expected: 0 changed, 0 removed over the baseline's rows; new rows only for the two new entries (and possibly none, if the baseline file lists only its own entries). Properties added to `properties.json` are `not_applicable` on every older entry (each names fluents only the SSI entries declare, `couple_rate` and the like, or reads `married` with `individual_rate`), so no old row should move. Anything else is recorded, not tuned.

## Drift and surprises

Any result other than the tables above is recorded below against the row it contradicts, in the entry that follows this section, and never edited into the preregistration; an unpredicted flip also gets a row in docs/surprises.md.

## Results (run 2026-11-08, engine b5fd019, k 6 and 8, declared, strict, step-mode one)

Recorded against the preregistration; nothing above was edited.

**Verdicts.** `phil rules check` on both entries at k=6 and k=8: all 10 property verdicts match the table (5/5 on each entry at each k; `open` is the engine's word for unreachable_open). Both entries pass with no vacuity flags. The pair prints two warnings (derived `couple_rate`, `couple_limit` name actions no rule regulates), as predicted. The older properties: not applicable (the ablation header reads "5 properties applicable, 35 not applicable"; the dataset lists 39 properties, and the header's 40 is explained: `expand_contested` adds the contested-reading variant `provided_for@encoder-2`, so 39 becomes 40; on the raw 39 the split is 5 applicable and 34 not (correctness review, item 5)).

**Ablation of the base** (`phil rules ablate --entry ssi-marriage-penalty`). Expected flips held: R2 -> married_couple_rated holds_to_k > violated; R3 -> married_couple_limited holds_to_k > violated; R4 -> penalty_reaches_unmarried reachable > open; R7 -> over_limit_ineligible holds_to_k > violated; R1, R5, R6 -> no flip. `function:` predictions on R2, R3, R4 all fired (none unsupported). Total 4 of 4 predicted flips, 0 of 3 predicted non-flips contradicted.

Drift and readings, recorded, not tuned:

1. **R4's prohibit variant flips a second property.** `R4~prohibit` (the engine's prohibit variant of a `may`, a disability on the couple-rate power under the holding-out condition) flips `married_couple_rated` as well as `penalty_reaches_unmarried`. Not preregistered (the preregistration covered deletion only). Reason: the disability bars `apply_couple_rate` for any pair that is cohabiting and holding out, including a married pair, so married holding-out pairs lose the power. An artifact of what a prohibit of R4 means, not a finding about SSI. Logged as a surprise (docs/surprises.md S5, artifact).
2. **Deregulation flags.** R1, R3, R5, R6 are each the sole regulator of their action, so the engine files their deletion under "deregulated, not ranked" (action becomes unregulated, derived power zeroed). R3 flips `married_couple_limited` but is excluded from the ranking for that reason; R2 and R4 share `apply_couple_rate`, so both are ranked. The preregistration expected a possible flag on R1 only. Reading, not a miss: it means the ranked load table undercounts R3, and the unranked row is the one to read.
3. **Load is zero for R4 in the ranked table.** `penalty_reaches_unmarried` is a failure_mode, which the engine lists but does not count toward load_freedom. R4's flip is real and listed, its `load_freedom` is 0/0. Not predicted in those words.
4. **Isomorphism (C2 (i)).** `phil rules iso` of the entry against coverture-household, police-crisis, cps and lease: iso False at exact and at guard, with and without strands, `care+control: -` in every run. Wording after the council: exact 0/7; guard 1/7 (R2 -> police-crisis R3, agency -> officer); care+control '-' in every run; weak evidence of non-match, since at guard any conditional `may` pairs with any other. The preregistration said "no match at any level"; one run is not literally empty: against police-crisis at the guard level the matcher reports a partial 1/7 pairing, R2 -> R3 (agency -> officer, apply_couple_rate -> detain), a single conditional `may`, which is not a cluster and not iso. Recorded as drift in my wording (partial pairings exist at guard), not as a match. Pair against base: iso False at guard, 2/7 matched (R1, R7), distance 5.
5. **C2 (ii) held vacuously, as preregistered.** All 34 older properties are not_applicable on the entry; deleting R2 or R3 flips none of them because none is run. A check that could not have failed.

**`phil rules diff --baseline data/verdicts-baseline.json`** (after `build.py --write --cards` then `--check`: ok, 29 institutions, 39 properties, 30 cards; pytest 38 passed):

```
note: engine source hash differs from the baseline's
ssi-marriage-penalty: added x5 (married_couple_limited holds_to_k, married_couple_rated holds_to_k, married_rated_individually open, over_limit_ineligible holds_to_k, penalty_reaches_unmarried reachable)
ssi-marriage-penalty-individual: added x5 (married_couple_limited violated, married_couple_rated violated, married_rated_individually reachable, over_limit_ineligible holds_to_k, penalty_reaches_unmarried open)
0 changed, 10 added, 0 removed (of 156 rows)   exit 0
```

The 27 existing entries are clean. The preregistration guessed "possibly none" new rows; the ten additions are the two new entries' own rows.

## Not done here (named, not hidden)

- Mechanical fix pass (2026-11-08): the three council files were read and the wording, pins and levels fixed; every verdict row is unchanged (`phil rules check` output for both entries identical before and after; `phil rules diff` 0 changed, 10 added, 0 removed).
- No composite. `ssi-marriage-penalty` with `coverture-household-us` is P2 (plans/composition.md) and the second half of C2.
- The council has run (see Status); the self-review checklist below is kept as written before it.
- No raw-source re-opening by the builder in the fix pass: carried rows are `snippet`, and R2's 1382(b)(2) pin and R7's 1382(a)(1)(B) bar pin are `unverified` (pins supplied by the faithfulness seat's raw read).

## What P2 will need (composite with coverture-household-us)

1. **Aliases:** `coverture-household-us`: husband -> partner_a, wife -> partner_b; this entry: claimant -> one of them (the claimant may be either; the choice decides whose penalty `financial_dependence` reads), spouse -> the other, agency stays a third role. `married` is typed [claimant, spouse] and coverture's is untyped, so typed wins by the unification table; confirm the arg order matches (h, w) after aliasing.
2. **A shared fluent that carries SSI into `financial_dependence`.** The property reads `is_subject`, `controls_own_property`, `owns_earnings`; this entry declares none and writes none. Without one, deleting R2 in the composite flips nothing the older properties read, and C2's second half fails by construction, not by the claim. Options to preregister: declare `is_subject` on the claimant; have the benefit supply `has_own_income` (coverture's is derived `(enabled draw_subsistence w)`, so a same-name derived fluent with a different definition is a unification error, ADR 0018); or add an SSI-specific `means_tested_income` fluent and a new property. This is an entry change and should be preregistered.
3. **Derived-fluent names in common:** none now (`couple_rate`, `eligible` and the rest are new to the dataset), so no conflict, but `eligible` and `individual_rate` need `exists g` over the agency role, which composition must keep typed.
4. **Prohibit/deregulation reading:** R3 and R1, R5, R6 land under "deregulated, not ranked" in the entry; in a composite, check that the composite's ranking does not hide them again.
5. **A dollar-valued penalty is out of scope** of the engine's boolean fluents; P2 can show where load moves, not how large the penalty is.

## Self-review checklist (council pending)

The council could not be spawned. These are what each seat must check; the batch is marked **council pending** until they run.

**Correctness seat** (does the engine mean what the entry says?):
- Does every derived fluent actually read the rule it is named for? Probe by deleting R2 and reading `couple_rate`, and by deleting R4 with a married holding-out pair.
- Is the `exists ((g agent))` over the agency role really one agent, and does `(enabled apply_couple_rate g c s)` respect the attribute scoping (agency only)?
- The R4~prohibit double flip: confirm it is the disability reading and not a lowering bug; confirm the base R2/R4 overlap (both name `apply_couple_rate`) makes R2 deletion non-deregulating.
- Is `resources_under_limit` initial-true the only initial literal needed, and does `init declared` honour it? Does `over_limit_ineligible` hold only because R7 is a hard must_not (not vacuously because `accumulate` is unreachable)? Check the vacuity flags and the antecedent reachability by trace.
- The invariant `married_couple_rated` is `holds_to_k` at k=6 and 8; is `marry` reachable at k=6 (so it is not vacuous)?
- Does `married_rated_individually` unreachable_open mean "not within k" only, never "safe"?

**Faithfulness seat** (does the entry say what the sources say?):
- Re-open the six sources raw (the worklist's fetches were summaries): confirm every excerpt carried into `provenance`, including the worklist's own typo in 416.1802 ("calculated"), and upgrade or downgrade the levels.
- R2 and R3 are `may`, the statute is mandatory: is the power reading acceptable, or must a state-obligation encoding be tried? R4 should be checked against 416.1806 (a)(3) in full: the reg says opposite sex; POMS covers same-sex pairs; the encoding follows POMS.
- R7's bar (over the limit, no payment) rests on no excerpt (unverified); open 42 U.S.C. 1382(a)(3)(A) and 20 CFR 416.1205.
- R5 and R6 conditions (neither married nor holding out) are the encoder's complement; the three tests in 416.1806 (a)(1)-(3) are not all encoded (formal marriage, and (a)(3) holding out; the other test is not read).
- The `sanctioner: none` on R4 against the brief's `state`: decide whether to invent the recovery or appeal sanction, with a source, or to accept none.
- 2026 rates and limits are an unverified lead; `penalty` size is nowhere in the encoding.
- The pair keeps R1 and R7 and drops holding out; confirm no reform text keeps the test.

**Card-only seat** (reading the generated cards without the source):
- Read `docs/cards/ssi-marriage-penalty.md` and `docs/cards/ssi-marriage-penalty-individual.md` only: can the reader say what `couple_rate` means, that it is a power not an applied rate, and which rule makes a married pair penalised? Is the word "penalty" defined? Is `holds_out` readable as conduct?
- Does the card show the weakest provenance per rule (R1 and R7 unverified) and the dropped holding-out rule in the pair?
- Do the card's property names (`married_couple_rated`) read as the penalty holding, and `married_rated_individually` as the penalty absent, without the plan?

Council pending.

## Revision 2 (author decisions)

Items the council raised that could move a verdict or change a rule. The mechanical pass did not touch them.

1. **Cohabitation condition on R2 and R3.** The source states the couple rate and limit for a spouse "with whom he or she is living" (416.1801(c); 1382(a)(1)(B)(i)); the rules carry `married` alone, so a separated married pair gets the couple rate. Add `cohabits`, or keep the gap declared. Same complement gap on R5 and R6.
2. **`must` on a state fluent with an establishing action, or `may`.** The lease R2 pattern (ADR 0009 must-be) is available here; `may ... when true` was a choice, not forced (correctness item 3). Either try the must-be encoding or label the entry "power reading only".
3. **R1 and the pair's R5/R6 as `default_capacity`** instead of `may ... when true` (cards/README.md convention).
4. **One-rule pair choice.** The pair is a 5-rule reform pair. Candidates: drop R3 alone (flips married_couple_limited) or drop R4 alone (flips penalty_reaches_unmarried).
5. **R4: follow POMS or the text as written.** The rule follows POMS SI 00501.152 (same-sex couples included); 416.1806(a)(3) says opposite sex. Also unencoded: `unrelated`, and timing (`at or after the time you apply`).
6. **Two unrun checks** (correctness item 9): whether `(exists ((g agent)) ...)` is limited to the agency role (rather than any agent), and R4 deletion on a married holding-out pair.

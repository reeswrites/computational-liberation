# ssi-marriage-penalty entry and pair (2026-11-08)

Status: PREREGISTERED, not yet run. Written and committed before the first `phil rules check`, `ablate` or `diff` over either entry. Engine: ENGINE_PIN b5fd019. Branch `ssi-entry`. Inputs: plans/sourcing-worklist-marriage.md section 5 (Entry 2) and its Gaps, docs/connections.md section 4 (C2), plans/disability.md (SSI), plans/composition.md, ADR 0018, data/institutions/src/lease.yaml as the model.

## What was built

- `data/institutions/src/ssi-marriage-penalty.yaml`: roles claimant, spouse, agency. Base fluents `married`, `cohabits`, `holds_out`, `resources_under_limit`; derived power fluents `couple_rate`, `couple_limit`, `individual_rate`, `individual_limit`, `eligible` (each reads `enabled` of an agency action, the convention of `can_sanction` and `has_standing`). Seven rules: R1 agency may pay a benefit; R2 may apply the couple rate when married; R3 may apply the couple resource limit when married; R4 may apply the couple rate when cohabiting and holding out (the displaced gate); R5, R6 individual rate and limit when neither married nor holding out; R7 disability: must_not pay when resources are not under the limit. `function:` on R2 (`penalises_marriage_rate`), R3 (`penalises_marriage_limit`), R4 (`extends_penalty_to_holding_out`).
- `ssi-marriage-penalty-individual`: the pair, penalty removed. R2, R3, R4 dropped; R5, R6 lose their marital-status condition. **Holding out is dropped, not kept**: with no couple rate there is nothing for the test to gate, and no reform text was read that retains it (S. 73 of 2025 is an unopened lead).
- Five new properties in `properties.yaml` (the 34 older ones all need fluents this entry does not declare): `married_couple_rated`, `married_couple_limited` (both freedom/unfreedom, invariant: the penalty holding), `penalty_reaches_unmarried` (failure_mode, reachable), `married_rated_individually` (structure, reachable: the penalty absent), `over_limit_ineligible` (freedom/unfreedom, invariant). Names, formulas and kinds are fixed here, before the run.
- Six bibliography works in `data/sources/rules.yaml`. Every `opened` level and excerpt is carried from the worklist, whose fetches returned model summaries rather than raw text; none was re-opened here.

## Declared deviations from the brief (before the run)

1. R4 has `sanctioner: none`, not `state`. The engine rejects a sanctioner without an `or_else`, and the only candidate sanction (recovery of overpayments, appeal) is in no opened source. The displaced reading therefore cannot use a sanctioner difference; it can read attribute sets only.
2. Rules are `may` powers, not the statute's mandatory `must`: an action `must` fires every step and blocks every other action (ADR 0009), and a must-be needs the establishing action to carry the rate. The penalty is therefore represented as a power the rules grant. Because an action no rule names stays free in traces, only the derived fluents see the rules; this is why every property here reads a derived fluent.
3. Holding out is a second route to the couple rate on the same aim as R2, not a rewrite of `married`, because a derived fluent cannot read `married or holds_out`.
4. Dollar amounts ($2,000 / $3,000; $994 / $1,491) are not representable; only which limit and rate the agency may apply.
5. Consent guard note (plans/consent-guard-note-DRAFT.md): ruled not applicable to benefits rules by the author, 2026-11-08.

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

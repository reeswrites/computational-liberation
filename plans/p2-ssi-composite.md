# P2: coverture-us-ssi composite (C2 second half)

Status: PREREGISTERED (committed before `_composites.yaml` is edited and before any `build.py`, `check`, `ablate` or `diff` over the composite). Written 2026-11-08 on branch `p2-ssi-composite`, from main 9964717, ENGINE_PIN 81d5b9e. Inputs read: plans/ssi-entry.md ("What P2 will need", revision-2 items NOT done here), plans/composition.md (P1, P1b, P2), ADR 0018, docs/reviews/2026-11-08-hospital-slice.md, docs/connections.md section 4, the two source entries. The preregistration sections below are never edited after the run; results go under "Results".

## Spec

Composite `coverture-us-ssi`, members `coverture-household-us`, `ssi-marriage-penalty`.

- Aliases: `coverture-household-us: {husband: partner_a, wife: partner_b}`; `ssi-marriage-penalty: {claimant: partner_a, spouse: partner_b}`; `agency` stays its own third role (typed `exists ((g agent))` and the `g` variable are frozen to `agency` before union).
- **Why claimant -> partner_a.** `married` is typed `[claimant, spouse]` in the SSI entry and untyped in coverture, where `marry(h, w)` sets `married(h, w)`: husband first. After aliasing, coverture sets `married(partner_a, partner_b)`; the SSI rules read `(married c s)` with `c` = claimant, so claimant -> partner_a and spouse -> partner_b make the two the same ground atom. The typed side wins by the unification table, giving `married[partner_a, partner_b]`. The other mapping (claimant -> partner_b) would make SSI read `married(partner_b, partner_a)`, which coverture never sets: the rules would be dead in the composite. The choice also decides whose `resources_under_limit` the entry initialises (claimant, so partner_a, the husband). The claimant being the husband is an assumption of the composite, not of SSI (either spouse may be the claimant); the claimant-as-wife composite is a second one, not this one. It matters for `financial_dependence` only if the property reads the claimant's fluents, which it does not (see below).
- `initial: ['female(partner_b)']`. The SSI member's own `initial` `(resources_under_limit claimant)` is inherited through the alias as `(resources_under_limit partner_a)`; the composite adds nothing else for SSI.
- `initial_free: [acquired_property, earns]`, exactly as the first composite, for the same reason (declared mode makes every unlisted fluent false at t=0; these two are coverture's exogenous fluents). Two other fluents no action sets in the SSI member: none (every SSI base fluent has setter actions).
- Roles after union: partner_a, partner_b, agency (3). Rule ids `coverture_household_us__R1..R7`, `ssi_marriage_penalty__R1..R7`.
- Expected build conflict (predicted, not yet seen): **`marry` is declared in both members with different effects** (coverture: sets married, is_subject, provides_care; SSI: sets married only). The unification table errors on a differing action. This is the one name both members share (coverture actions: marry, hold_property, keep_earnings, maintain, neglect, keep_house, neglect_house, control_property, chastise, misbehave, draw_subsistence, leave, sue, contract; SSI actions: marry, divorce, cohabit, separate, present_as_married, cease_holding_out, accumulate, spend_down, apply_couple_rate, apply_couple_limit, apply_individual_rate, apply_individual_limit, pay_benefit). Fluent names are disjoint apart from `married`, which unifies. **P2b, preregistered here with the prediction:** if the build errors on `marry`, rename the SSI member's action `marry` to `wed` in `ssi-marriage-penalty.yaml` (and anything that names it: the pair inherits by `extends`; no rule or property names the action), a pure rename with no semantic change. Expected consequence: `phil rules diff` 0 changed on the 177 rows after the rename, and the SSI standalone verdicts unchanged. In the composite, `wed` then offers a second route to `married` that does not set `is_subject`. This is a modelling consequence recorded, not tuned. If the rename moved any old row, that is a miss.

## Preregistered expectations

**Build and check.** `build.py --write --cards` succeeds after P2b (and not before, predicted); `--check` ok; `phil rules check --inst coverture-us-ssi` and `check-all` pass. Warnings: exactly the six the coverture member prints today (three derived-fluent warnings for `controls_own_property`, `has_own_income`, `owns_earnings`; undeclared `can_claim_for`, `transferred`, `can_attach`) and none from SSI (the base prints none). No vacuity flag. `phil rules diff --baseline data/verdicts-baseline.json`: 0 changed, 0 removed over the 177 old rows; the composite's rows are additions.

**Q2 again.** The composite's applicable property set equals coverture-household-us's applicable set united with ssi-marriage-penalty's five. The six properties (cared_for, chosen_mutual_care, double_burden, financial_dependence, financial_dependence_unpropertied, provided_for) are applicable with no variant; backlash, creditor_shield (forced via expected_properties), no_standing_against_spouse stay as on coverture alone (fluent reasons). No older property becomes applicable because of the SSI fluents.

**Verdicts, k = 6 and 8, declared, strict, step-mode one** (the first composite's table plus the SSI table):

| Property | Expected |
|---|---|
| dependent_cannot_exit | reachable |
| subject_cannot_exit | reachable |
| care_and_sanction_same_role | holds_to_k |
| no_standing | reachable |
| care_assigned_by_sex | violated |
| financial_dependence | holds_to_k |
| financial_dependence_unpropertied | holds_to_k |
| cannot_contract | holds_to_k |
| double_burden | unreachable_open |
| creditor_shield | unreachable_open |
| married_couple_rated | holds_to_k |
| married_couple_limited | holds_to_k |
| penalty_reaches_unmarried | reachable |
| married_rated_individually | unreachable_open |
| over_limit_ineligible | holds_to_k |

Reason: SSI actions touch no coverture fluent except `married` (and `wed`, after P2b, only `married`); coverture actions touch no SSI fluent except `married`; interleaving under one action per step lengthens traces only, and k = 6 still holds `wed`, `cohabit`, `present_as_married`, then the derived power at the next step.

**C2, second half (docs/connections.md section 4, as written):** "deleting [the SSI marriage-penalty rule] in the composite flips `financial_dependence`." Made exact: in `phil rules ablate --entry coverture-us-ssi`, the rows `ssi_marriage_penalty__R2` (couple rate) and `ssi_marriage_penalty__R3` (couple limit), and also both deleted together (a scratch probe, since `ablate` deletes one rule per row), flip `financial_dependence`.

- **If it flipped** (not expected): direction `holds_to_k` -> `violated`, and the party that loses is partner_b (the wife, the subject; `is_subject` is set for her by `marry`): she would acquire a resource under her own control only by the SSI rule's removal. Mechanism would have to be a derived fluent the property reads, `controls_own_property` or `owns_earnings`, enabled through an SSI rule.
- **Expected (about 95%): it does not flip, in any of R2, R3, both, or any of the 14 rules.** `financial_dependence` reads `is_subject`, `controls_own_property` (= `enabled hold_property`) and `owns_earnings` (= `enabled keep_earnings`). No SSI rule names `hold_property` or `keep_earnings` or sets `is_subject`; both derived fluents are constant false in the composite exactly as in coverture alone (the warnings already say so). The property is therefore independent of the SSI rules by construction. **If it does not flip, C2 fails as written**: the claim named a connection the encodings do not contain, because `financial_dependence` reads coverture fluents the SSI rules never touch (plans/ssi-entry.md "What P2 will need", item 2, already said so). This is the result I expect and preregister, not a surprise to be explained away. The register then marks C2b `refuted` as written, with the review requirement pending. What the composite can still show, and does not test the claim: the SSI rows flip the SSI properties as they do standalone (R2 -> married_couple_rated holds_to_k -> violated; R3 -> married_couple_limited holds_to_k -> violated, under deregulated-not-ranked; R4 -> penalty_reaches_unmarried reachable -> open; R7 -> over_limit_ineligible holds_to_k -> violated; R1, R5, R6 no flip), and no coverture property flips on any SSI rule and no SSI property on any coverture rule except via `married` (none expected: no coverture rule deletion changes `married` or the SSI derived fluents). Ablation rows for coverture rules equal coverture-household-us's own.
- Carriage: with no shared fluent, a connection claim reduced to "the same couple holds both institutions" is true of the composite's roles but not of any property verdict; the nine husband/wife properties apply (Q2) and carry nothing from SSI.

## Drift rule

Any result other than the above is recorded in "Results" against the row it contradicts and never edited into this section; an unpredicted flip also gets a row in docs/surprises.md (S7).

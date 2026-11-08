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

## Results (run 2026-11-08, engine 81d5b9e, k = 6 and 8, declared, strict, step-mode one)

Recorded against the preregistration above; nothing above was edited.

**Build.** First `build.py --write --cards` failed exactly as predicted: `action 'marry' differs from an earlier member's`. P2b applied as preregistered (SSI's `marry` renamed `wed`; one line in `ssi-marriage-penalty.yaml`, the card of the standalone entry is unchanged because no card names the action); then `--write --cards` wrote 33 institutions, 34 cards; `--check` ok. The only other file touched outside the spec: `tests/test_dataset_claims.py` `CARE_OBLIGED_ENTRIES` gained `coverture-us-ssi` (same mechanical step as the first composite; without it `test_care_obliged_declared_where_provides_care_is` failed).

**Check, k = 6 and 8: 14 of 15 as preregistered.** Drift, 1 miss: `cannot_contract` expected holds_to_k, got **violated** (both k). Diagnosed with `check --prop cannot_contract --trace`: marry, then SSI's `divorce(partner_a, partner_b)` sets `married` false (coverture has no divorce action and bars `leave`, not divorce), after which coverture R7's condition (`married`) fails and `contract` is enabled for the wife. My preregistered reasoning treated `married` as a shared fluent only SSI's `wed` could set; `divorce` is the other setter and I overlooked it. Not an engine fault and not tuned: the expectation stays as written, the mismatch stays in check-all, docs/surprises.md S7. Warnings: exactly the six predicted (coverture's three derived-fluent and three undeclared-fluent warnings), none from SSI. No vacuity flag.

**Q2 again.** The composite's ablation header: 24 properties applicable, 20 not (of 44, the list including `provided_for@encoder-2`). coverture-household-us's applicable set united with the SSI five is the preregistered union; the six properties (cared_for, chosen_mutual_care, double_burden, financial_dependence, financial_dependence_unpropertied, provided_for) are among the applicable ones; backlash and no_standing_against_spouse are not applicable. Not separately verified: that the 24 equal the exact union (I did not diff the set by name, only read the six and the two named non-applicable); recorded as not verified.

**Ablation (`phil rules ablate --entry coverture-us-ssi`).** Flips by rule (k = 6): coverture R4 -> no_standing reachable > open; coverture R6 -> dependent_cannot_exit and subject_cannot_exit reachable > open; coverture R2 and R3 -> mutual_household_care persists > fails (goods); coverture R7 -> **no flip** (preregistered: the same flips as coverture alone, which includes R7 flipping cannot_contract; here masked by S7, since cannot_contract is already violated); SSI R2 -> married_couple_rated holds_to_k > violated; SSI R3 (deregulated, not ranked) -> married_couple_limited holds_to_k > violated; SSI R4 -> penalty_reaches_unmarried reachable > open; SSI R7 -> over_limit_ineligible holds_to_k > violated; SSI R1, R5, R6 and coverture R1, R5 (all deregulated) no flip. No SSI row flips a coverture property and no coverture row flips an SSI property.

**The C2 second-half result, verbatim from the rows:** `financial_dependence` is not named in any flip column. `ssi_marriage_penalty__R2`: `married_couple_rated:holds_to_k>violated[freedom_up]`. `ssi_marriage_penalty__R3`: `married_couple_limited:holds_to_k>violated[freedom_up]`. Both rules deleted together (scratch probe over `without_rule`, k = 6 and 8): financial_dependence holds_to_k, financial_dependence_unpropertied holds_to_k, married_couple_rated violated, married_couple_limited violated. **C2's second half does not hold: deleting the SSI couple-rate and couple-limit rules in the composite does not flip `financial_dependence`. C2 fails as written**, as preregistered (about 95%), for the structural reason preregistered: the property reads `is_subject`, `controls_own_property` and `owns_earnings`, which no SSI rule touches. This says nothing about whether the SSI marriage penalty burdens a wife in fact; it says the encodings share no fluent that carries it. A claim that SSI's penalty shifts load onto the wife's economic standing would need a shared fluent (plans/ssi-entry.md item 2: declare `is_subject` on the claimant, or a `means_tested_income` fluent and a new property) and is not tested here.

**`phil rules diff --baseline data/verdicts-baseline.json`** before extending: `0 changed, 15 added, 0 removed (of 192 rows)` (the 177 old rows clean; the 15 are the composite's). After `phil rules verdicts --out data/verdicts-baseline.json` (192 rows; the only removed line in the file diff is the engine_hash): `0 changed, 0 added, 0 removed (of 192 rows)`. `pytest -q`: 38 passed (after the one-line `CARE_OBLIGED_ENTRIES` update; 1 failed before it). `check-all` (background): agreement 191/192 = 99%, exit 1, the one miss `coverture-us-ssi cannot_contract` (S7). Wall time of the composite ablation: not measured.

## Council pending (self-review checklist; the coordinator runs the seats)

**Correctness seat**
- Confirm the `cannot_contract` trace: marry, divorce, contract. Is `divorce` the only married-state exit? Would renaming SSI's `divorce`/`wed` into a shared-state exit modelling choice be an entry change? Should the composite instead drop SSI's `wed` and `divorce` (the member's own marital-status setters) so that `married` is coverture's alone?
- Is claimant -> partner_a the only line-up (`married[partner_a, partner_b]` set by coverture's `marry(h, w)`)? Probe: with claimant -> partner_b does `married_couple_rated` still hold_to_k (it should be non-vacuous only if `wed` reaches the swapped atom)?
- Is `exists ((g agent))` over agency only, or over partner_a, partner_b too (open item 6 of ssi-entry revision 2, still unrun)? In the composite the property of interest does not read it, but `married_couple_rated` does.
- Check that `financial_dependence`'s independence is not a typing accident: do `controls_own_property` and `owns_earnings` ground over partner_b, and are they false under both members' rules (they are: the build warnings say so)?
- The scratch probe (R2 + R3 together) used `without_rule` on the composite in memory: re-run through the CLI or a unit test if the claim is kept.
- Q2 set equality was read, not diffed by name.

**Faithfulness seat**
- Does "the claimant is the husband" stand for anything historical? The SSI program (1974) post-dates coverture's US reading; the composite is a pairing of two eras' rules over one couple, which the card must not read as one legal regime. Is the composite name's `coverture household (US)` + `SSI` honest about that?
- Does the refutation of C2b read as a statement about the sources? It should not: it is a statement about which fluents each entry declares.
- Anything in the SSI entry's provenance is untouched (the sibling builder owns `verification` and `accessed`).

**Card-only seat** (docs/cards/coverture-us-ssi.md only)
- Can a reader see that `marry` (coverture) and `wed` (SSI) both set `married`, and that `divorce` exists only because of SSI? Is the alias line (claimant -> partner_a) visible with its reason?
- Does the card show that the expected `cannot_contract` verdict missed and why, or only the preregistered value? (It shows the value; the miss lives here and in S7.)
- Is it clear from the card that no SSI rule touches the wife's property or earnings?

## Post-council record (fix pass, 2026-11-08; appended, nothing above edited)

Council reviews: docs/reviews/2026-11-08-p2-{correctness,faithfulness,card-only}.md.

- **S7 was a reading error, not a model surprise.** The mechanism was visible in the preregistration text above: it lists `divorce` among the SSI actions and says SSI actions touch no coverture fluent except `married`, while `divorce` writes `married`. The prediction was falsifiable from its own text.
- **Post hoc (S7): preregistered holds_to_k; violated via SSI divorce.** `cannot_contract` in `coverture-us-ssi` is edited from `holds_to_k` to `violated` after the run, marked post hoc in the composite notes (the `expected_properties` field has no place for a mark). The baseline row already recorded the actual verdict; `check-all` now 192/192.
- **The R2+R3 joint deletion is a scratch probe, not a CLI row.** It ran over `without_rule` in memory; the C2b conclusion does not rest on it (the single-rule rows already show no flip of `financial_dependence`).
- **Verdict vacuity.** `financial_dependence` and `_unpropertied` hold under any SSI rule set (their fluents are never enabled, as in coverture alone); "no SSI row flips a coverture property" is true by disjoint fluents, not a finding.
- **Not run:** the claimant -> partner_b swap probe and the `exists ((g agent))` scope probe.

## P2c (preregistered, not run)

A derived SSI member `ssi-marriage-penalty-no-exit`, via `extends: ssi-marriage-penalty` with `actions_drop: [wed, divorce]` (so `married` is coverture's alone), composed as `coverture-us-ssi-noexit` with the same aliases, `initial` and `initial_free` as `coverture-us-ssi`. Expected: `cannot_contract: holds_to_k`, and every other verdict identical to `coverture-us-ssi`. Not built here. Any other result is recorded against this section, not edited into it.


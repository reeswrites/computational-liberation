# Connections: how the literatures meet at the rule level

Written 2026-11-04 after the author asked how feminist, disability, race, animal, anarchist and abolitionist theories of liberation connect when "it is all connected and necessary" but the rules look unrelated. Answer: they already meet in three places the dataset has, and are missing in two places it does not. This file makes the meeting points a table with holes, and preregisters the one claim that would show the connection is real rather than asserted.

## 1. Where they already meet

**Shared vocabulary.** Every entry uses the same fluent names for the same meanings (`is_subject`, `provides_care`, `can_exit`, `has_standing`, `can_sanction`, `can_claim_for`). Isomorphism is matched on those names, so when police, child protective services and the coverture household match at guard+strands, no one asserted the match; the rules did ([data/institutions/README.md](../data/institutions/README.md), gate (b)). A disability or race entry written in the same vocabulary either matches an existing cluster or does not, and the engine says which.

**One rule schema.** Since slice 1 revision 4, a default capacity is what a person of that kind can do unless an express disability removes it (ADR 0013). The rule that removes it has one shape across literatures:

| Literature | Rule (ADICO) | Entry |
|---|---|---|
| Feminist / coverture | wife `must_not contract` when married, `or_else` null | coverture-household R7 |
| Feminist / coverture | wife `must_not sue` when married | coverture-household R4 |
| State control / abolition | detainee `must_not leave` when in custody | police-crisis R4, cps R10 |
| Animal | animal `must_not sue` when true | companion-* R11 |
| Disability (parked) | ward `must_not contract` / `decide` when under guardianship | plans/disability.md, not encoded |
| Race (parked) | applicant `must_not apply` when record; buyer `must_not buy` when district redlined | plans/race-entries.md, not encoded |

Status-based removal of a default capacity. Same deontic, same `or_else`, same aim kind; only the attribute and the status fluent differ. The liberatory move is the same rule edit each time: delete the disability, or make its condition something the subject can change.

**One cut.** Family abolition, prison abolition, disability justice and the anarchist critique of domination say the same thing in rules: keep `provides_care`, remove `can_sanction` from the carer, restore the capacity, add exit. The README's forms table is literature-neutral for that reason. The failure modes are shared too: `double_burden`, `creditor_shield`, the rename test, `backlash` are checked identically on every entry.

## 2. The matrix

Rows are the forms of liberation in the README. Columns are the literatures the author has brought in. A cell names the entry that carries that form for that literature; an empty cell is an encoding to do. Parked handoffs are in `plans/`.

| Form | Feminist | Abolition (police, CPS, family) | Animal | Disability | Race | Anarchist (domination) |
|---|---|---|---|---|---|---|
| Exit | coverture R6; mwpa chain | police R4, cps R10, crisis-team; kibbutz | companion R6 | Olmstead (parked) | | needs `can_exit` leg of the predicate |
| Standing | coverture R4; mwpa-suit | police R10 (may sue); crisis-team R9 | companion R11 (no standing, faithful) | guardianship vs supported decision-making (parked) | ban-the-box (parked) | |
| Material independence | mwpa-property, -earnings, -sole-trader; coverture-floor (candidate) | | | SSI/Medicaid asset limits (parked) | redlining, GI bill ~ reparations (parked) | |
| Bodily / reproductive autonomy | footbinding pair; ectogenesis pair | | companion `reproduction_controlled_by_owner` | embryo screening (parked, contested) | | |
| Care decoupled from sex / birth | kibbutz pair; paternity-quota pair; ectogenesis | kibbutz | | care webs (parked, needs voice) | | |
| Non-domination (care ≠ sanction) | coverture `care_and_sanction_same_role` | police, cps, crisis-team (the cluster) | companion-* | institutional vs community care (parked) | | the predicate itself (parked) |
| Recognition (care counts as work) | not encoded; slice 2 goods | | | | | |
| Voice (say over the rules) | not encoded | not encoded | | supported decision-making (parked) | | needs the collective-choice rule kind (parked) |

Reading the holes: recognition and voice are empty in every column, so they are the dataset's gaps rather than any literature's. Race and anarchist columns are empty because their handoffs are parked, not because the forms do not apply. Disability has a parked entry in five of eight rows, which is why it is a good next batch.

## 3. What is missing

**Composition.** A person lives under several institutions at once: marriage and benefits and employment. The SSI marriage rule is a benefits rule whose condition reads a marriage fluent. Every entry today is isolated, so load that moves from one bundle to another is invisible, and that movement is the author's whack-a-mole thesis. Needed: an engine operation that composes two institutions over their shared fluents into one rule set (roles unioned, fluents unified by name, rules concatenated with ids prefixed), and ablation over the composite. The cross-institution transfer graph falls out: cut coverture R1 and see whether `financial_dependence` is carried by an employment rule instead. Engine ADR to write; one new CLI verb; the dataset already shares names, so the first composite (coverture-household + a benefits entry) needs only the benefits entry. Sketch: `plans/composition.md` (written 2026-11-07; it adds role aliases and binding freeze, which this paragraph did not anticipate).

**Voice.** A rule kind whose object is another rule (`X may change_rule R when C`). It closes the empty row above, gives the domination predicate its third leg, and is the only way to encode guardianship vs supported decision-making and Ostrom's rules-for-changing-rules. One engine change serves the anarchist and the disability columns at once.

## 4. The connection claim, preregistered (not run)

Written before any of the entries it names exist. The claim that the literatures connect at the rule level is this, and it can fail:

- C1. A guardianship/conservatorship entry written in the shared vocabulary will match coverture-household at guard+strands with the sub-signature {provides_care ~ provides_care, sanction ~ sanction, exit bar ~ exit bar} and will not match crisis-team at any level. If it matches only at guard, the connection is structural but the strand tags differ, which is itself a finding about which strand disability justice calls tying.
- C2. An SSI/Medicaid asset-and-marriage entry will not match the care+control cluster at any level (it has no care strand), and its load will show only in a composite with a marriage entry: deleting its marriage-penalty rule alone flips nothing preregistered, deleting it in the composite flips `financial_dependence`.
- C3. Supported decision-making will be one rule apart from guardianship (the voice rule) and will differ on `no_standing`, not on `care_and_sanction_same_role`: the care and the sanction stay, the say over the rule moves.
- C4. The status-removal schema in section 1 will be detected as a rename-class isomorphism between coverture R7 and the guardianship contract bar (ADR 0010 level exact under attribute renaming), without a human tag saying so.

Where the literatures do not connect, the engine is not asked to make them: embryo screening (reproductive freedom against disabled flourishing), animal lineage, title against floor are disagreement rows. The disagreement locator names the property they split on; the author decides.

Status: C1-C4 untested, entries not encoded. Enter them in docs/claims.md when the disability batch is scheduled, not before.

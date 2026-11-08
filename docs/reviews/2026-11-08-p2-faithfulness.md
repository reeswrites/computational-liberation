# Encoding-faithfulness review: composite coverture-us-ssi (P2, 2026-11-08)

Fresh agent, faithfulness seat (ADR 0014). Not the builder. Read-only apart from this file; engine not re-run. A composite has no sources, so the tests are whether aliases and `initial` state a possible world and whether composition changed any member rule.

## Findings (red = unfaithful, amber = reservation, green = faithful)

- **Era not stated: red.** Claimant-as-husband is a defensible world (SSI has no sex rule for claimants; the notes say the choice is the composite's). But coverture-household-us is Blackstone (1765) read as pre-MWPA US law and SSI is 1974 onward; no one lived under both. Neither `_composites.yaml` notes nor the card says "constructed, not historical"; the only caveat is a question in the plan's council checklist. The card's Roles section sets "the husband; the legal person the marriage keeps" beside the SSA with no era note. Fix: add to notes and card preamble that this is a constructed world pairing two eras' rules over one couple, asking what the rules do, not what any couple lived.
- **`divorce`: red, an SSI finding independent of the composite.** `divorce` in ssi-marriage-penalty.yaml is a bare setter of `married` false. No rule uses it, and no excerpt or source mentions divorce: 416.1802 as carried says only that benefits depend on marital status at the start of the month. It is an encoder convenience, unsourced and unflagged. Harmless alone, but in the composite it is the only route out of coverture R7's condition, so `cannot_contract` is violated (S7). That is an artifact of an unsourced action, not a finding about coverture, and coverture's R6 bars `leave`, not divorce. Fix: mark `divorce` in the SSI notes as an unsourced encoder action; state on the card that the S7 miss comes from it.
- **P2b rename `marry` to `wed`: green on content, amber on place.** The member diff is one line. No `plain`, `source`, condition or aim changed, and no rule names the action, so what PR #6's faithfulness review read is unchanged. Doing it in the member file was the only route (ADR 0018 has no action aliasing) and was preregistered. But SSI's notes never mention `wed`, so its record is silent on a change. Fix: one sentence in SSI notes naming the rename and why.
- **`female(partner_b)`: green.** Coverture declares `female/1` and `care_assigned_by_sex` reads it; SSI declares no sex fluent, and R4 carries no sex condition. The inherited `resources_under_limit(partner_a)` is SSI's own `initial` carried through the alias. `initial_free` repeats the first composite's choice for coverture's exogenous fluents.
- **Shared `married`: green with a caveat.** Coverture declares it arity 2, untyped (gloss "h and w are married"); SSI types it `[claimant, spouse]`. After aliasing both are `married(partner_a, partner_b)`, typed side wins, and `(married h w)` and `(married c s)` ground to one atom. The caveat: husband-first order is imposed on SSI, which treats the pair symmetrically. The plan states this; the card does not.
- **Notes and card honesty: amber.** The plan is candid (preregistration, C2b refuted about shared fluents rather than SSI's effect on wives, S7). The card is not: it shows `divorce` and `wed` as ordinary actions, shows the preregistered `cannot_contract: holds_to_k` that the check missed, omits that the council is pending, and carries unverified provenance (coverture R3 and R6, snippet-level SSI) only per rule.

## Close

- Red: era statement missing; `divorce` unsourced.
- Amber: member-file rename unrecorded in SSI notes; husband-first order; card caveats.
- Green: `female`, initial, typing agreement, no member rule's text or sources altered.

**Verdict: faithful with reservations**, pending the two red fixes. Composition changed no rule's text or sources; the world it states is constructed and must say so.

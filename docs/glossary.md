# Glossary

Wording follows `plans/institutions-phase0.md`. Structural terms describe encodings, not moral standing.

- **bundle**: the set of rules that together make up one institution or one arrangement of rights and duties.
- **strand**: one rule or thread in a bundle, tagged by what holds it there (`rival | superadditive | tying`).
- **rival input**: a strand only one party or one body can supply at a time (one bed, one pregnancy); it resists unbundling as a scheduling fact, not a value.
- **superadditive**: a strand whose good exists only as a product of the bundle (being known by one person who is also housemate and co-parent); unbundling is possible but costs legibility.
- **tying**: a strand glued to the bundle by law, wages or norm with no production link to the rest; it exists to protect a monopoly and is the strand liberation removes first.
- **contingent bundle**: held together by economics or law, not by the goods themselves; unbundling frees the parts.
- **constitutive bundle**: the good exists only because the parts come together; unbundling deletes the good instead of freeing it, so the honest move is choosing bundles, not escaping them.
- **material floor**: care, health, housing and income provided regardless of any relationship, so that no one's survival depends on being chosen; built first because losing care is the real danger of unbundling.
- **equal standing (exit, voice, recognition)**: a subject can leave (exit), contest rules (voice), and be counted as a party to claims (recognition).
- **real freedom**: the practical ability to act on a permitted option, not only its formal permission.
- **non-domination**: no party holds a rule-backed power to interfere arbitrarily with another's choices.
- **dark twin**: capital rebundles the freed strand into a product: unbundling done by capital rather than by the subject, the labor kept and the protections stripped (the gig economy for jobs; agribusiness owning the meat substitutes). Who-pays axis, ADR 0016.
- **displacement**: control or burden moved to another party or place rather than removed. Who-pays axis, ADR 0016.
- **backlash**: the change threatens an equilibrium enough to provoke active reaction, typically a rule added to reinforce the existing bundle against a change or substitute (MWPA `narrowed` branch: a court power that reinstates the husband's control). Who-pays axis, ADR 0016.
- **rebundling**: the same strands recombined under new names or roles, so the structure returns. Who-pays axis, ADR 0016.
- **capture**: a party the change was not written for gains the new power or shelter (MWPA `creditor_shield`: husbands moving assets to wives to dodge creditors). Rule axis, ADR 0016.
- **perverse incentive**: the payoffs a rule creates reward behaviour that undermines the property it was meant to secure (compliance theatre). Rule axis, ADR 0016.
- **dead letter**: the rule passes and adoption never crosses threshold. Time axis, ADR 0016.
- **erosion**: practice drifts back while the rule stays on the books; a narrowing encoded as a court power is backlash, not erosion (ADR 0016 amendment 2026-11-04). Time axis, ADR 0016.
- **enforcement decay**: the `or_else` exists but stops firing, so a sanctioned norm becomes unsanctioned (kibbutz). Time axis, ADR 0016.
- **lock-in**: the change succeeds and then cannot be revised; Ostrom's self-revising-rules principle is the guard. Time axis, ADR 0016.
- **cosmetic reform** (a Rule-axis failure mode, ADR 0016): a change (such as a role rename) that leaves the structure isomorphic to the original.
- **implicit rule**: a norm nobody writes down (`implicit: true`), encoded because it is often the one worth contesting.
- **ADICO**: Ostrom's Institutional Grammar statement form: Attribute, Deontic, aIm, Conditions, Or else.
- **fluent**: a state predicate that varies over time, written `Holds(fluent, args, t)`.
- **bounded unrolling**: giving fluents and actions a step index 0..k (default k = 6) with frame axioms, inside Z3.
- **reachable**: some compliant trace reaches the property within k steps (a permission, not a prediction).
- **open**: the solver did not find a trace, or timed out; beyond the bound this is never read as safe.
- **holds_to_k**: the property holds at every step of every compliant trace up to k.
- **violated**: a compliant trace breaks the property; a counterexample trace is returned.
- **persists**: once the property holds, it keeps holding up to k (reform durability).
- **isomorphism (structural)**: equivalence of canonical rule skeletons under a role and predicate bijection, reported with matched sub-signature and unmatched rules; never moral equivalence.
- **minimal pair**: two institutions differing by one rule, used to test that near-identical encodings are told apart.
- **gate**: the set of criteria an encoding run must pass, including rediscovery of known findings, before results are used.
- **backtest**: checking the engine's verdicts against historical cases with known outcomes before any forward claim.

## Gate

Source: `docs/interpreting-results.md` section 4. "Phase 0 test" numbers are from `docs/theory.md` line ~171.

| Letter | What it checks | Phase 0 test |
|---|---|---|
| (a) | The 14 institutions load; no load-bearing must-be rule is inert. | none |
| (b) | The care+control trio matches at its precommitted level; `lease` and `public-library` do not; the crisis team matches nothing. | (1) cluster police, CPS, coverture household; exclude the crisis team |
| (c) | The minimal pair is one rule apart and differs on the named property. | (2) separate paternity quota from transferable leave |
| (d) | `care_assigned_by_sex` persists with implicit R2 and fails without it. | (3) the kibbutz failure |
| (e) | Verdicts agree with preregistered expectations (minimum 60%). | none |
| (f) | A pure rename is detected (`pure_rename`) and guardianship is not ownership. | none numbered (claims L3 ties (c)/(f) to test (2); L5 covers rename) |

## Further terms

- **precommitted**: fixed in the dataset entry before the run; applies to the iso level per claim (`docs/decisions/0010-iso-abstraction-levels.md`, `docs/interpreting-results.md` section 3).
- **preregistered**: expected verdicts written before any run and never edited to match results (`CONTRIBUTING.md`, `docs/plan.md`).
- **care+control cluster**: police-crisis, CPS and the coverture household, which share a care duty, a control permission on the same subject, and an exit bar (`docs/decisions/0010-iso-abstraction-levels.md`).
- **council**: fresh reviewer agents, never the builder, convened after every batch with four seats (`docs/decisions/0014-review-council.md`).
- **load-bearing**: a must-be rule the gate counts on to constrain behaviour; gate (a) fails if one is inert (`docs/interpreting-results.md`).
- **inert**: a must-be rule no compliant trace can breach within k, so it constrains nothing (`docs/interpreting-results.md` section 2).
- **vacuous**: a `holds_to_k` that is true only because the antecedent never occurs (`docs/interpreting-results.md` section 2).
- **must-be**: an ADICO aim that is a fluent (state obligation) rather than an action (philosophy-engine ADR 0009, `../philosophy-engine/docs/decisions/0009-state-obligations.md`).
- **guard / strands / level**: iso switches. Level is `exact` (literal conditions) or `guard` (conditions reduced to conditional or unconditional); strands adds the human-assigned rival/superadditive/tying tags (`docs/interpreting-results.md` section 3).
- **power fluent**: a fluent derived from what the rules enable, `(enabled ACTION ...)`, never asserted as an effect (philosophy-engine ADR 0013, `../philosophy-engine/docs/decisions/0013-derived-power-fluents.md`).
- **negative control**: an institution (`lease`, `public-library`) that must not match a cluster at its precommitted level (`docs/decisions/0010-iso-abstraction-levels.md`, `docs/interpreting-results.md` section 4).
- **expected-match control**: an institution preregistered to match structurally, `airline-flight` (in-flight custody); gate (b) has no mode for it yet (`docs/interpreting-results.md` section 4, `docs/plan.md`).
- **post hoc**: a property or expectation chosen or edited after seeing verdicts; must be marked as such (`docs/interpreting-results.md` section 6, claims M4, L15).
- **sanctioned norm**: an implicit rule encoded as a `must_not` with an `or_else` sanction, as kibbutz R2 (`docs/interpreting-results.md` section 5, `data/institutions/README.md`).
- **assurance**: what lets people leave a bundle together; solidarity as a stag hunt (`docs/theory.md`, "How liberation starts").
- **surplus**: slack that makes room to see a bundle as a bundle (`docs/theory.md`, "How liberation starts").
- **Layer 1-5**: the roadmap layers: 1 Entailment, 2 Frequency, 3 Backtest, 4 Priority, 5 Sequence (`docs/theory.md`, roadmap table). TODO author: one-line definitions of layers 2-5 beyond the table.

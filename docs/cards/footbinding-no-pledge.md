# footbinding-no-pledge

**Footbinding without the pledge action (minimal pair for gate (a))**

> Construction: footbinding with both pledge actions (leave_unbound_pledge, accept_match_pledge) and their rules R4 and R10 deleted (R10 since 2026-11-04, encoding review finding 2); pledged stays declared but nothing sets it. Historically the pre-1874 situation (no pledge associations).

## Roles

- **family**: the household deciding for a daughter (Mackie's 'parents' who bind, or pledge not to); the institutional sort, not a demographic (ADR 0011)
- **daughter**: the subject: the girl whose feet are bound or left unbound; bound in childhood, so she decides nothing
- **suitor**: the family of a prospective groom: the marriage-market counterparty whose expectations hold the convention

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | family | may | `(bind family daughter)` | `(is_subject daughter)` | none | tying | A family may bind its daughter when she is a subject of the institution (Mackie 1996). | Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):9... https://www.jstor.org/stable/2096305 |
| R2 | family | may (implicit) | `(leave_unbound family daughter)` | `(is_subject daughter)` | none | tying | (practice, not written) A family may leave its daughter unbound when she is a subject of the institution. | implicit: leaving a daughter unbound is always physically open to the family; R3... |
| R3 | family | must not (implicit) | `(leave_unbound family daughter)` | `(is_subject daughter)` | R5 `(reject_match suitor daughter)` | tying | (practice, not written) A family must not leave its daughter unbound when she is a subject, or else the suitor may reject the match (R5) (Mackie 1996). | SANCTIONED NORM (implicit; a convention, not a written rule): a family that leav... https://www.jstor.org/stable/2096305 |
| R5 | suitor | may (implicit) | `(reject_match suitor daughter)` | `(and (is_subject daughter) (not (bound daughter)) (not (pledged family)) (not (pledged suitor)))` | none | rival | (practice, not written) A suitor may reject the match when the daughter is a subject, is not bound, and neither the family nor the suitor has pledged (Mackie 1996). | implicit: the marriage market refuses an unbound bride (R3's or_else), 'maintain... https://www.jstor.org/stable/2096305 |
| R6 | suitor | may | `(accept_match suitor daughter)` | `(and (is_subject daughter) (or (bound daughter) (pledged family) (pledged suitor)))` | none | tying | A suitor may accept the match when the daughter is a subject and is bound, or the family or the suitor has pledged (Mackie 1996). | the convention from the groom's side: a bound daughter is acceptable; an unbound... https://www.jstor.org/stable/2096305 |
| R7 | family | may | `(marry_off family daughter)` | `(and (is_subject daughter) (or (bound daughter) (pledged family)))` | none | tying | A family may marry off its daughter when she is a subject and is bound or the family has pledged (Mackie 1996). | the marriage condition: Mackie, 'Ending Footbinding and Infibulation: A Conventi... https://www.jstor.org/stable/2096305 |
| R9 | daughter | must not (disability) (implicit) | `(refuse_binding daughter)` | `(is_subject daughter)` | none | rival | (practice, not written) The daughter cannot refuse binding while she is a subject: no such power exists (ADR 0013). | binding is done to a young girl by her family: she has no say. A disability (or_... |

**Default capacities** (enabled unless an express disability bars them): refuse_binding

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| binding_practised | freedom | persists | Footbinding is in force: some subject (the current cohort's daughter) has bound feet at step t. The layer-2... |
| marriage_requires_binding | freedom | holds_to_k | Mackie's convention: whenever a family can marry off a subject, she is bound or the family has pledged (an... |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |

## Pairs

Extends [footbinding](footbinding.md); one line per change:
- R4 dropped: A family may take the anti-footbinding pledge for its daughter when she is a subject (pledge associations, 1874 onward).
- R10 dropped: (practice, not written) A suitor may take the pledge to accept an unbound bride (the sons' half of the pledge) when the daughter is a subject.
- actions dropped: leave_unbound_pledge, accept_match_pledge
- fields overridden: minimal_pair_of
Minimal pair of [footbinding](footbinding.md), differing in rule R4,R10; no layer-1 property separates the pair.
Not isomorphic to: coverture-household, police-crisis, cps

## Notes

PREREGISTERED (2026-11-04, before any run): the same four verdicts as footbinding (persists, holds_to_k, reachable, reachable): pledges change nothing at layer 1. The pair is the gate (a) 'pledge actions exist' half: crit_a reads _has_pledges on `footbinding` itself, so this entry is the dataset's record of what the no-pledge world looks like and `differs_on` is null by design (no layer-1 property separates them). At layer 2 the preregistration is the plan's: binding persists here under every module. PREREGISTERED (2026-11-04, encoding review finding 2, written and committed before the first run with the suitor pledge): adding accept_match_pledge(suitor, daughter) [effect pledged(suitor)] with rule R10 suitor may accept_match_pledge, and reading (pledged suitor) in R5 (and-not) and R6 (or), changes NO layer-1 verdict in footbinding or footbinding-no-pledge: binding_practised persists, marriage_requires_binding holds_to_k, subject_cannot_exit and dependent_cannot_exit reachable in both; the new pledge only lifts the sanction R5 (and widens R6), R3 is unconditional, R7 is untouched, and pledged is a fluent per role (footbinding-no-pledge strips BOTH pledge actions and both pledge rules R4 and R10, so nothing sets pledged(suitor) there). Iso: still none at every level against the care+control cluster; isomorphic_to nothing. Expected warnings unchanged (can_sanction, provides_care, has_standing, can_claim_for undeclared). Layer 2 (information, not an expectation): pledged(suitor) is role-level too (A2), so one suitor's pledge lifts R5 for every suitor, the same coarseness as pledged(family): the A2 caveat now applies on both sides; gate (a)'s _has_pledges reading is unchanged (true via either pledge) and ablate_pledges strips both. If any verdict flips, the drift is recorded here and the expectations are not edited. RESULT (2026-11-04, after the run, commit b6f48aa preceding it): no drift. check-all 115/115 with all four verdicts as preregistered in both entries; `phil rules gate` PASS; pytest 15 passed; no warning printed for either entry (none was printed before the change either). ABM information, `--seeds 5 --steps 60 --modules material,coordination`: bound 1.0 in every seed (persistence), pledged 0.667 over seeds, i.e. true on the family and the suitor role tuple and not the daughter's: the A2 caveat on both sides, as the preregistration said; breach, sanction and unavoidable rates 0. Drift 2026-11-04 (encoding review finding 3): marriage_requires_binding is by construction (marriageable is derived from R7's enabledness and R7's condition is bound-or-pledged, so the property restates the rule); kept in expected_properties for the record, not evidence; the property carries by_construction: true, which the engine ignores. Layer 1 has one cohort (encoding review 2026-11-04 finding 4): one daughter, bound at t=0, and `married` never clears, so no trace shows a per-cohort binding decision before the market; a `new_cohort` action clearing bound/married is deferred to the author.

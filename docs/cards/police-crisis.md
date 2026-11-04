# police-crisis

**Armed police response to mental-health crisis (Cal. WIC 5150)**

> 'When a person, as a result of a mental health disorder, is a danger to others, or to themselves, or gravely disabled, a peace officer, ... designated members of a mobile crisis team, or professional person designated by the county may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours for assessment, evaluation, and crisis intervention.' 'A...

## Roles

- **officer**: peace officer dispatched to the call; armed
- **subject**: the person in crisis
- **dispatcher**: 911 dispatch; chooses who responds

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | dispatcher | must (implicit) | `(dispatch_officer d o s)` | `(call_received s)` | none | tying | (practice, not written) The dispatcher must dispatch an officer to a subject when a call about that subject has been received. | implicit: police are the default responder to a crisis call; nothing in WIC 5150... |
| R2 | officer | must | `(provides_care o s)` | `(and (responding o s) (in_crisis s))` | none | superadditive | The officer providing care to the subject must hold when the officer is responding to the subject and the subject is in crisis (Cal. WIC 5150). | Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_... https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R3 | officer | may | `(detain o s)` | `(and (responding o s) (in_crisis s) (danger s))` | none | rival | The officer may detain the subject when responding to a subject who is in crisis and there is danger (Cal. WIC 5150). | Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_... https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R4 | subject | must not (disability) | `(leave s)` | `(in_custody s)` | none | rival | The subject cannot leave while in custody: no such power exists (Cal. WIC 5150). | Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_... https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R5 | officer | may | `(use_force o s)` | `(and (in_custody s) (resists s))` | none | rival | The officer may use force on the subject when the subject is in custody and resists. | use-of-force authority incident to lawful custody; general peace-officer powers.... |
| R6 | officer | may | `(carry_weapon o)` | `true` | none | tying | The officer may carry a weapon at any time. | officers respond armed; standard equipment policy. UNVERIFIED (general knowledge; no source opened) |
| R7 | officer | must | `(release o s)` | `(and (in_custody s) (not (danger s)))` | none | superadditive | The officer must release the subject when the subject is in custody and there is no danger (Cal. WIC 5150). | Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_... https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R8 | subject | may | `(petition_review s)` | `(in_custody s)` | none | tying | The subject may petition for review of the hold when the subject is in custody (Cal. WIC 5275). | Cal. WIC 5275 certification review / habeas; subject keeps standing. UNVERIFIED... |
| R10 | subject | may | `(sue s)` | `true` | none | tying | The subject may sue in their own name at any time. | an adult keeps legal capacity to sue in their own name; a 5150 hold does not rem... |

**Default capacities** (enabled unless an express disability bars them): leave, sue

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |
| no_standing | freedom | unreachable_open | No role may start a claim whose condition refers to the subject's interest and whose effect changes the sub... |

## Pairs

[crisis-team](crisis-team.md) is a minimal pair of this entry (rule R3).
Isomorphic to: cps (guard+strands), coverture-household (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

## Notes

The same role (officer) is bound to care (R2, assess) and empowered to detain (R3) and use force (R5): care_and_sanction_same_role. subject_cannot_exit is reachable with scope=interaction only (the 72-hour hold), not institution; report the scope. Pitfalls: (1) R1 is the implicit rule that makes this police-crisis rather than crisis-team; the statute itself also names mobile crisis teams as holders of the 5150 power, so an encoder reading only the statute will not see why armed officers are the ones who come; (2) a trivial encoding that ignores or_else on R4 will cluster this with crisis-team (plan: worked pitfall); (3) no_standing is unreachable_open, not 'safe': the subject keeps has_standing via R8, but the bound k=6 says nothing beyond it. Armed status (R6) is a tying strand: it is not required by 5150 and is what the crisis-team reform removes. ADR 0009: R2 is a state obligation ('on an ongoing basis' is a state); R1 stays an action obligation but dispatch consumes the call. Exogenous triggers (call_received, in_crisis, danger, resists) are initial_free, since under init=declared a fluent no action sets would otherwise be pinned false and no call could ever arrive.

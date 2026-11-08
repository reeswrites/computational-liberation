# crisis-team

**Unarmed crisis response team, referral only (Denver STAR model)**

> Denver's STAR pilot 'dispatches a mental health clinician and a paramedic to low-level emergencies' instead of police; since June 2020 it 'has responded to more than 600 calls ... many of them related to homelessness, mental illness and substance abuse — not criminal activity.' The team is described as unarmed; in one case it picked up a woman's medication and 'connected her with housing'. KUNC, 'In Denver, unarmed mental health workers respond to hundreds of 911 calls instead of police' (2020-11-17), read at https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **responder**: clinician + paramedic team; unarmed, no custody power
- **subject**: the person in crisis
- **dispatcher**: 911 dispatch; routes eligible calls to the team
- **officer**: police, called only if the responder requests

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | dispatcher | must (sanctioner derived, unreviewed) | `(dispatch_team d r s)` | `(and (call_received s) (eligible s))` | none | tying | The dispatcher must dispatch a team to the subject when a call about the subject has been received and the subject is eligible (Denver STAR). | recalled | [full source under Sources, R1](#src-r1) https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police |
| R2 | responder | must (sanctioner derived, unreviewed) | `(provides_care r s)` | `(and (responding r s) (in_crisis s))` | none | superadditive | The responder providing care to the subject must hold when the responder is responding to the subject and the subject is in crisis (Denver STAR). | recalled | [full source under Sources, R2](#src-r2) https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police. |
| R3 | responder | may (sanctioner derived, unreviewed) | `(refer r s)` | `(responding r s)` | none | superadditive | The responder may refer the subject (for example to medication pick-up or housing) when responding to the subject (Denver STAR). | recalled | Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police (medication pick-up, housing connection; referral is the output) |
| R4 | responder | must not (disability) (sanctioner derived, unreviewed) | `(detain r s)` | `true` | none | rival | The responder cannot detain the subject at any time: no such power exists (Denver STAR). | recalled | [full source under Sources, R4](#src-r4) https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police |
| R5 | subject | may (sanctioner derived, unreviewed) | `(leave s)` | `true` | none | rival | The subject may leave at any time (Denver STAR, voluntary encounter). | recalled | Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police (voluntary encounter) |
| R6 | responder | must not (disability) (sanctioner derived, unreviewed) | `(carry_weapon r)` | `true` | none | tying | The responder cannot carry a weapon at any time: no such power exists (Denver STAR, unarmed). | recalled | Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police (unarmed) |
| R7 | responder | may (implicit) (sanctioner derived, unreviewed) | `(request_police r o s)` | `(and (responding r s) (danger s))` | none | tying | (practice, not written) The responder may request police for the subject when responding to the subject and there is danger. | unverified | implicit rebundling path: the team can call police when a scene turns violent; practice, not written policy in the source read. UNVERIFIED (general knowledge; no source opened) |
| R8 | officer | may (implicit) (sanctioner derived, unreviewed) | `(detain o s)` | `(and (responding o s) (danger s))` | none | rival | (practice, not written) The officer may detain the subject when responding to the subject and there is danger (Cal. WIC 5150). | recalled | [full source under Sources, R8](#src-r8) https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R9 | subject | may (sanctioner derived, unreviewed) | `(sue s)` | `true` | none | tying | The subject may sue in their own name at any time. | unverified | an adult keeps legal capacity to sue in their own name; a voluntary encounter does not touch it. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(s) = sue enabled |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue

## Variables

- R1: `d` = dispatcher (rule var_roles); `r` = responder (rule var_roles); `s` = subject (rule var_roles)
- R2: `r` = responder (rule var_roles); `s` = subject (rule var_roles)
- R3: `r` = responder (rule var_roles); `s` = subject (rule var_roles)
- R4: `r` = responder (rule var_roles); `s` = subject (rule var_roles)
- R5: `s` = subject (rule var_roles)
- R6: `r` = responder (rule var_roles)
- R7: `r` = responder (rule var_roles); `o` = officer (rule var_roles); `s` = subject (rule var_roles)
- R8: `o` = officer (rule var_roles); `s` = subject (rule var_roles)
- R9: `s` = subject (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police (low-level calls involving mental illness, homelessness, substance use are routed to the clinician-paramedic van). [ADR 0009: one-off action obligation; dispatch consumes call_received]

- `kunc-2020-denver-star` (date n/a): **recalled**

<a id="src-r2"></a>
**R2**: Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police. [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] dispatch_team establishes provides_care(r, s); assess restores it, withdraw breaks it

- `kunc-2020-denver-star` (date n/a): **recalled**

**R3**

- `kunc-2020-denver-star` (date n/a): **recalled**

<a id="src-r4"></a>
**R4**: Denver STAR (Support Team Assisted Response), KUNC 2020-11-17; https://www.kunc.org/2020-11-17/in-denver-unarmed-mental-health-workers-respond-to-hundreds-of-911-calls-instead-of-police ('non-police response'; the team holds no custody power; or_else null because this is an absence of power, not a prohibition with a penalty). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(responder, s) = detain enabled, which this disability makes false

- `kunc-2020-denver-star` (date n/a): **recalled**

**R5**

- `kunc-2020-denver-star` (date n/a): **recalled**

**R6**

- `kunc-2020-denver-star` (date n/a): **recalled**

**R7**

- no work named: **unverified** (rationale: implicit rebundling path: the team can call police when a scene turns violent; practice, not written policy in the source read)

<a id="src-r8"></a>
**R8**: Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_and_inst_code_section_5150 (the peace officer the team calls holds the 5150 custody power the team lacks; the rebundling path R7 opens). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(officer, s) = detain enabled

- `cal-wic-5150` (s. 5150(a); US-CA; date n/a): **recalled**

**R9**

- no work named: **unverified** (rationale: an adult keeps legal capacity to sue in their own name; a voluntary encounter does not touch it)


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_and_sanction_same_role | structure | violated | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| subject_cannot_exit | freedom | unreachable_open | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| dependent_cannot_exit | freedom | unreachable_open | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| no_standing | freedom | unreachable_open | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |

## Pairs

Minimal pair of [police-crisis](police-crisis.md), differing in rule R3.
Not isomorphic to: police-crisis, cps, coverture-household

<details><summary>Encoder notes (engine internals)</summary>

Same care rules as police-crisis (R2 assess, R3 refer) with the sanction rule R3-of-police replaced by R4 (must_not detain). So care_and_sanction_same_role is violated (care without can_sanction) and subject_cannot_exit is unreachable within k, which must be reported as 'open', never 'safe'. Pitfalls: (1) a trivial encoding that ignores or_else and deontics will see 'assess' in both and cluster them (plan: worked pitfall); (2) R7 is the implicit rebundling path: with it, a compliant trace exists in which an officer with can_sanction enters the scene, so care_and_sanction_same_role can hold again at a later step for the officer, though not for the responder; the check must report which role; (3) R4 has or_else null by design, it is an absence of power; lowering it as a sanctioned prohibition would invent a sanctioner. minimal_pair_of points at police-crisis R3 because that is the one rule whose replacement flips the verdict; the armed/unarmed and dispatch-eligibility differences (R1, R6) are tying-strand differences, not the sanction difference. ADR 0009: R2 is a state obligation, mirroring police-crisis R2; exogenous triggers (call_received, eligible, in_crisis, danger) are initial_free.

</details>

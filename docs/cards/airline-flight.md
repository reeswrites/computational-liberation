# airline-flight

**Airline flight (permanent negative control, EXPECTED to match the care+control cluster)**

> Reconstruction, not a quotation: a flight's crew must care for passengers aboard, may restrain a disruptive passenger, and a passenger must not leave in flight (may leave on the ground); the passenger may complain. Supplied by the third review (2026-11-03) as a structural negative control for the care+control match.

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
- **(implicit)**: not written as a rule in the cited source; reconstructed from it or from practice. The source cell gives the rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it. The "Default capacities" list under the table names the bearer role for each.
- **free fluent**: an input the model varies, not set by any rule; a when cell that names one waits on a fact the world supplies (a report arrives, it is visiting time), not on something a role does. Listed with its gloss under "Free fluents" below the table.
- **(replaced) / (added)** after a row id: this entry `extends` another, and the row replaces the base entry's row of that id, or adds one; the base card holds the original wording.
- **linked to no rule**: a sanction-shaped rule (such as `may reprimand`) that no row's or else points at; it fires on no breach and is kept for the record only.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **crew**: cabin crew; serves and may restrain
- **passenger**: a passenger aboard; the counterparty

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | crew | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(board c p)` | `(not (aboard p))` | none | tying | The crew may board the passenger when the passenger is not aboard. | unverified | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR 91.11 / 121.580 (interference with crew; crew may restrain) and flight-attendant duties are named by the reviewer from general knowledge. UNVERIFIED (general knowledge; no source opened) |
| R2 | crew | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provides_care c p)` | `(aboard p)` | none | superadditive | The crew providing care to the passenger must hold when the passenger is aboard (14 CFR 121.571 supports only a briefing and assistance duty; the general in-flight care duty is unverified). | unverified | [full source under Sources, R2](#src-r2) https://www.law.cornell.edu/cfr/text/14/121.571 |
| R3 | crew | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(restrain c p)` | `(and (aboard p) (disruptive p))` | none | rival | The crew may restrain the passenger when the passenger is aboard and disruptive (14 CFR 91.11 / 121.580, unverified). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | passenger | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave p)` | `(aboard p)` | none | rival | The passenger cannot leave while aboard: no such power exists (14 CFR 91.11 / 121.580, unverified). | unverified | [full source under Sources, R4](#src-r4) |
| R6 | passenger | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(complain p)` | `true` | none | tying | The passenger may complain at any time. | unverified | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR 91.11 / 121.580 (interference with crew; crew may restrain) and flight-attendant duties are named by the reviewer from general knowledge. UNVERIFIED (general knowledge; no source opened) (a passenger may complain) |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend):

- `disruptive(passenger)`: p is behaving disruptively (exogenous); no action in this institution sets it.

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4):

- `leave`: A passenger (the who cell of R4; the action parameter is untyped) may leave unless a rule forbids it; rule rows naming it: R4 (must not, a disability).

## Variables

- R1: `c` = crew (rule var_roles); `p` = passenger (rule var_roles)
- R2: `c` = crew (rule var_roles); `p` = passenger (rule var_roles)
- R3: `c` = crew (rule var_roles); `p` = passenger (rule var_roles)
- R4: `p` = passenger (rule var_roles)
- R6: `p` = passenger (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- `cfr-14-91-11` (US; date n/a): **unverified**
- `cfr-14-121-580` (US; date n/a): **unverified**

<a id="src-r2"></a>
**R2**: 14 CFR 121.571 'Briefing passengers before takeoff', read 2026-11-04 at https://www.law.cornell.edu/cfr/text/14/121.571 (ecfr.gov redirected to a block page): (a) 'shall insure that all passengers are orally briefed by the appropriate crewmember'; (a)(3) a required crewmember assigned to the flight must individually brief each person who may need another person's help to reach an exit. That is a crew duty toward passengers aboard, but narrower than the rule's provides_care (maintenance, services): the general in-flight care duty is UNVERIFIED (no text opened states it; 14 CFR 121.391, read at https://www.law.cornell.edu/cfr/text/14/121.391, only sets the number of flight attendants 'to provide the most effective egress of passengers'). 14 CFR 91.11 / 121.580 dropped 2026-11-04: they only forbid interference with crew. [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] board establishes provides_care; attend restores it, withdraw breaks it Verification pass: 14 CFR 121.391 read 2026-11-06 at https://www.law.cornell.edu/cfr/text/14/121.391: (d) 'flight attendants required by this section shall be located as near as practicable to required floor level exits and shall be uniformly distributed throughout the airplane in order to provide the most effective egress of passengers in event of an emergency evacuation'.

- `cfr-14-121-571` (s. 121.571(a), (a)(3); US; date n/a): **opened** 2026-11-04: "shall insure that all passengers are orally briefed by the appropriate crewmember" <https://www.law.cornell.edu/cfr/text/14/121.571>
- `cfr-14-121-391` (s. 121.391(d); US; date n/a): **opened** 2026-11-06: "flight attendants required by this section shall be located as near as practicable to required floor level exits and shall be uniformly distributed throughout the airplane in order to provide the most effective egress of passengers in event of an emergency evacuation" <https://www.law.cornell.edu/cfr/text/14/121.391>
- no work named: **unverified** (the general in-flight care duty: UNVERIFIED (no text opened states it))

<a id="src-r3"></a>
**R3**: Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR 91.11 / 121.580 (interference with crew; crew may restrain) and flight-attendant duties are named by the reviewer from general knowledge. UNVERIFIED (general knowledge; no source opened) (crew may restrain a disruptive passenger)

- `cfr-14-91-11` (US; date n/a): **unverified**
- `cfr-14-121-580` (US; date n/a): **unverified**

<a id="src-r4"></a>
**R4**: Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR 91.11 / 121.580 (interference with crew; crew may restrain) and flight-attendant duties are named by the reviewer from general knowledge. UNVERIFIED (general knowledge; no source opened) (a passenger cannot leave in flight). [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.] [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(p) = leave enabled (a default capacity), which this disability makes false aboard

- `cfr-14-91-11` (US; date n/a): **unverified**
- `cfr-14-121-580` (US; date n/a): **unverified**

**R6**

- `cfr-14-91-11` (US; date n/a): **unverified**
- `cfr-14-121-580` (US; date n/a): **unverified**


## Goods (slice 2)

Slice 2 revision 3 (plans/priority-slice2-results.md, "Revision 3" and "Revision 3 fix pass"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world); the primary column reads each good under the author's value call (R3.1). This entry is not in any good's entries list: the readings below evaluate the dataset's goods formulas here as extrapolation, as for every goods row outside a good's listed entries. R2 (the crew's unsanctioned duty of care to a passenger aboard) is guarantee-carrying for cared_for and known_carer (stable > fragile when deleted) and, on the primary column, carrying (guaranteed) for cared_for (known_carer is possible-primary and stays possible). Under strict compliance R2's duty reads as delivered care. Prohibiting R1 (boarding) means no passenger is ever aboard: the goods are not applicable there, outside the ranking, not lost. In the blind-gloss experiment (formulas not adopted) R2 carries no primary load under either blind cared_for formula, and its guaranteed reading differs between the two blind encoders. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |

## Pairs

No pair relations.

<details><summary>Encoder notes (engine internals)</summary>

EXPECTED-MATCH control (`expected_control_match: true`; third review 2026-11-03). PREREGISTERED before any run: airline-flight matches police-crisis, cps and coverture-household at guard+strands (care R2 superadditive ~ care, R3 rival ~ chastise/detain/remove, R4 exit bar ~ exit bar). The match is structural: in-flight custody has the same care + restraint + exit-bar form, so it is a finding about the form, not a failure of the encoding. Retagging R2 superadditive -> tying removes every match: the strand tags are load-bearing and the tags are human inputs. Why it is not in `not_isomorphic_to_control`: gate (b) fails on any match, and the gate has no expected-match mode (philosophy-engine is not edited here); `rules_gate` still lists it as an ordinary dataset entry. Expectations copied from police-crisis minus no_standing and are unverified until check-all. 6 rules (the review's list), not 10.

</details>

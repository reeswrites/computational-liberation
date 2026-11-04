# cps

**Child protective services: family support bundled with investigation and removal (Cal. WIC 306)**

> 'Any social worker in a county welfare department ... may ... (2) Take into and maintain temporary custody of, without a warrant, a child who has been declared a dependent child ... or who the social worker has reasonable cause to believe ... has an immediate need for medical care or is in immediate danger of physical or sexual abuse.' '(f) Before taking a child into custody, a social worker sh...

## Roles

- **social_worker**: county child-welfare worker; offers services and may remove
- **child**: the child the report concerns
- **parent**: the child's parent or caretaker
- **court**: juvenile court; decides dependency and custody

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | social_worker | must | `(investigate w c)` | `(report_received c)` | none | tying | The social worker must investigate the child's case when a report about the child has been received. | Cal. WIC 328 / Penal Code 11165.14: reports must be investigated; the same worke... |
| R2 | social_worker | may | `(provide_services w c)` | `(case_open c)` | none | superadditive | The social worker may provide services to the child when the case is open (Cal. WIC 16501). | Cal. WIC 16501 family maintenance / preservation services. UNVERIFIED (general k... |
| R3 | social_worker | may | `(remove w c)` | `(and (case_open c) (immediate_danger c))` | none | rival | The social worker may remove the child when the case is open and the child is in immediate danger (Cal. WIC 306). | Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_... https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R4 | social_worker | must | `(in_home_considered w c)` | `(and (case_open c) (immediate_danger c))` | none | superadditive | The social worker having considered keeping the child at home must hold when the case is open and the child is in immediate danger (Cal. WIC 306). | Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_... https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R5 | parent | must (implicit) | `(cooperates p c)` | `(case_open c)` | R3 `(remove w c)` | tying | (practice, not written) The parent cooperating with the case must hold when the case is open, or else the social worker may remove the child (R3). | implicit: non-cooperation is read as risk and feeds the removal decision; practi... |
| R6 | social_worker | must (implicit) | `(contact_mother w p)` | `(and (case_open c) (parent p c) (female p) (not (contacted w p)))` | none | tying | (practice, not written) The social worker must contact the mother when the case is open, she is the child's parent, and she has not yet been contacted. | implicit: the mother is the parent called first and held responsible (plan: 'the... |
| R7 | court | may | `(reassign_custody court p c)` | `(and (case_open c) (not (best_interest p c)))` | none | tying | The court may reassign custody of the child when the case is open and the parent's custody is not in the child's best interest (Cal. WIC 361). | Cal. WIC 361 / 361.2: court may remove from or place with a parent on best-inter... |
| R8 | court | must | `(counsel_appointed c)` | `(case_open c)` | none | tying | The child having appointed counsel must hold when the case is open (Cal. WIC 317). | Cal. WIC 317: counsel appointed for the child in dependency proceedings. UNVERIF... |
| R10 | child | must not (disability) | `(leave c)` | `(in_custody c)` | none | rival | The child cannot leave while in custody: no such power exists (Cal. WIC 306). | Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_... https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R11 | child | may | `(petition c)` | `(counsel_appointed c)` | none | tying | The child may petition in its own name when counsel has been appointed for the child (Cal. WIC 317(e)). | Cal. WIC 317(e): appointed counsel represents the child's interests in the proce... |

**Default capacities** (enabled unless an express disability bars them): leave

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |
| no_standing_persists | freedom | fails | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Va... |
| care_assigned_by_sex | freedom | reachable | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |

## Pairs

Isomorphic to: police-crisis (guard+strands), coverture-household (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

## Notes

Care (R2, services) and sanction (R3, removal) sit in one role, and R5 makes the care relationship itself the lever: refusing services is a condition for the sanction. That is the structure shared with police-crisis (assess + detain) and coverture (maintain + chastise). R7 is the court-reassigns-on-best-interest rule that companion-guardianship adds to companion-ownership; the iso with that entry is partial (R7 only) and structural. Pitfalls: (1) R5 and R6 are implicit; dropping R6 makes care_assigned_by_sex unreachable and looks like a success (same failure shape as the kibbutz entry); (2) no_standing_persists 'fails' because R7 and R8/R11 give the child a claim path (can_claim_for court c derived from R7, has_standing derived from R11 under appointed counsel), unlike the animal entries; (3) 'reachable' for subject_cannot_exit is permission, not frequency. Only WIC 306 was read; R1, R2, R7, R8 cite sections from memory and are marked UNVERIFIED in source. ADR 0009: R4, R5 and R8 are state obligations and R1/R6 one-off action obligations (consumed trigger / guard); as per-step action obligations R1, R4, R5, R6 and R8 all fired at every open-case step, so under one action per step remove could never fit (subject_cannot_exit open). Exogenous triggers (report_received, immediate_danger, parent, female, best_interest) are initial_free.

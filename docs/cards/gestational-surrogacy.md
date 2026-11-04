# gestational-surrogacy

**Gestational surrogacy: the rival input moves to another body (control for ectogenesis)**

> Construction, not a statute: gestational surrogacy as the control for ectogenesis (plans/ectogenesis.md section 1). Statute citations still to be added (state surrogacy acts vary). UNVERIFIED: no statute or case opened.

## Roles

- **intended_parent**: the person or couple who will raise the child; the carer; the institutional sort, not a demographic (ADR 0011)
- **child**: the subject: the child, a subject only once born (is_subject is set only by a birth action)
- **provider**: the clinic or lab that starts, transfers, implants or decants gestation
- **registry**: vital records / court: registers parentage and reprimands
- **gestator**: the surrogate whose body carries the child; the rival input (one body, a short window; docs/theory.md 'Pregnancy, birth, nursing')

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R2 (replaced) | provider | may | `(implant provider gestator child)` | `true` | none | rival | The provider may implant an embryo in the gestator for the child at any time (gestational surrogacy). | gestational surrogacy: the clinic implants an embryo in the gestator. Statute ci... |
| R3 (replaced) | gestator | must | `(give_birth gestator child)` | `(gestates gestator child)` | R6 `(reprimand registry x)` | rival | The gestator must give birth to the child when she is gestating it, or else the registry may reprimand (R6). | the gestator carries to term and gives birth; the rival input sits in one body.... |
| R4 | intended_parent | may | `(provide_care intended_parent child)` | `(and (parent intended_parent child) (is_subject child))` | none | superadditive | An intended parent may provide care for the child when a registered parent of the child and the child is a born subject. | care by any registered parent of a born child is permitted, men included; nothin... |
| R5 | intended_parent | must (implicit) | `(provide_care intended_parent child)` | `(and (parent intended_parent child) (is_subject child) (female intended_parent))` | R6 `(reprimand registry x)` | tying | (practice, not written) A female intended parent must provide care for the child when a registered parent of the child and the child is a born subject, or else the registry may reprimand (R6). | implicit sanctioned norm (a care-norm, not a written rule): the female registere... |
| R6 | registry | may | `(reprimand registry x)` | `true` | none | tying | The registry may reprimand at any time (the sanction for R3 and R5). | the registry's sanction for R3 and R5 (or_else target). Condition 'true' as in k... |
| R7 | registry | may | `(register_parentage registry intended_parent child)` | `(is_subject child)` | none | tying | The registry may register an intended parent as parent of the child when the child is a born subject, with no birth condition. | parentage is registered for any born child; NO birthing_parent condition (ASSUME... |

**Default capacities** (enabled unless an express disability bars them): none

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| birth_labor_rival | structure | holds_to_k | Any gestation is held by exactly one body: whenever c is in gestation, exactly one agent gestates c. holds_... |
| care_decoupled_from_birth | structure | unreachable_open | Care exists for a born child and no one is its birthing parent. is_subject guards against pre-birth vacuity... |
| solo_care_by_non_birthing_parent | structure | reachable | Some non-birthing parent is the sole carer of the child at step t. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |

## Pairs

Extends [ectogenesis](ectogenesis.md); one line per change:
- R1 dropped: A provider may start gestation of a child at any time (Firestone 1970).
- R2 replaced: was "The provider may transfer the child to the device when the child is in gestation (Firestone 1970)." now "The provider may implant an embryo in the gestator for the child at any time (gestational surrogacy)."
- R3 replaced: was "The provider must decant the child when the child has been gestated ex utero, or else the registry may reprimand (R6) (Firestone 1970)." now "The gestator must give birth to the child when she is gestating it, or else the registry may reprimand (R6)."
- roles added: gestator
- fluents dropped: gestated_ex_utero
- fluents changed: birthing_parent
- fluents added: gestates
- actions dropped: start_gestation, transfer_to_device, decant
- actions added: implant, give_birth
- fields overridden: expected_properties, isomorphic_to, not_isomorphic_to, minimal_pair_of
[ectogenesis](ectogenesis.md) is a minimal pair of this entry (rule R1,R2,R3).
Isomorphic to: ectogenesis (guard)
Not isomorphic to: ectogenesis, coverture-household, police-crisis, cps, kibbutz-childrens-house

## Notes

Control: the rival input moves to a weaker party (failure mode Displacement; the model case is the global care chain; layer 3). The minimal pair is recorded on ectogenesis. Revision 2 (2026-11-04): start_gestation merged into implant per plans/ectogenesis.md v2; v1 drift 1 stays in the record. ASSUMED author decisions (2026-11-04, from the encoder's brief, not from the plan file): R2+R3 substituted counts as a minimal pair; E R2/R3 tagged `superadditive` by hand (no new strand value; claim L11 is refuted for this reason, plan section 5c); R7 has no birthing_parent condition; R5 triggers on female(p) (role not body: Kleven, docs/theory.md); no leave action, so the plan's leave_reserved_for_non_birthing_parent row is dropped; neither entry is in CONTROLS (ectogenesis is not registered as a care-without-control control); gestator consent is out of scope. BY CONSTRUCTION, flagged in advance (plan section 5): birth_labor_rival in ectogenesis restates R2's effect list (gestates is never set there), and care_decoupled_from_birth in ectogenesis is reachable because decant omits birthing_parent (the only non-trivial leg is R7's missing birth condition); both properties carry by_construction: true, which the engine ignores. Treat those two verdicts as information, as marriage_requires_binding was, not as evidence; non-circular evidence needs layer 2/3. Also by construction: gestated_ex_utero exists only to mark an absence. PREREGISTERED (plans/ectogenesis.md section 3, before any run; layer 1, init declared, strict compliance, k=6). gestational-surrogacy: birth_labor_rival holds_to_k; care_decoupled_from_birth unreachable_open; solo_care_by_non_birthing_parent reachable; care_assigned_by_sex violated. ectogenesis: birth_labor_rival violated; care_decoupled_from_birth reachable; solo_care_by_non_birthing_parent reachable; care_assigned_by_sex violated. Headline difference: birth_labor_rival. Iso (ADR 0010, about 65% confident): ectogenesis ~ surrogacy iso at guard, not iso at guard+strands (R2/R3 rival to superadditive tag flip), not iso at exact; ectogenesis not iso coverture-household / police-crisis / cps / kibbutz-childrens-house (no control permission over the subject, no exit bar, so the care+control sub-signature fails); vs transferable-leave / paternity-quota a guess of partial at guard+strands, two legs (R5~R7 implicit must-care by attribute; R4~R5 may care), about 40% confident. Failure modes (ADR 0016): surrogacy Displacement (layer 3); ectogenesis Dark twin (layer 3), Capture (needs a new rule), Dead letter (layer 2); R5 surviving is partial reform, no mode. Layer 2 not required.

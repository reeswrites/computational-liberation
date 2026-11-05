# gestational-surrogacy

**Gestational surrogacy: the rival input moves to another body (control for ectogenesis)**

> Construction, not a statute: gestational surrogacy as the control for ectogenesis (plans/ectogenesis.md section 1). Statute citations still to be added (state surrogacy acts vary). UNVERIFIED: no statute or case opened.

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.

## Roles

- **intended_parent**: the person or couple who will raise the child; the carer; the institutional sort, not a demographic (ADR 0011)
- **child**: the subject: the child, a subject only once born (is_subject is set only by a birth action)
- **provider**: the clinic or lab that starts, transfers, implants or decants gestation
- **registry**: vital records / court: registers parentage and reprimands
- **gestator**: the surrogate whose body carries the child; the rival input (one body, a short window; docs/theory.md 'Pregnancy, birth, nursing')

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R2 (replaced) | provider | may | `(implant provider gestator child)` | `true` | none | rival | The provider may implant an embryo in the gestator for the child at any time (gestational surrogacy). | unverified | gestational surrogacy: the clinic implants an embryo in the gestator. Statute citations still to be added (state surrogacy acts vary). UNVERIFIED: no statute or case opened. |
| R3 (replaced) | gestator | must | `(give_birth gestator child)` | `(gestates gestator child)` | R6 `(reprimand registry x)` | rival | The gestator must give birth to the child when she is gestating it, or else the registry may reprimand (R6). | unverified | the gestator carries to term and gives birth; the rival input sits in one body. Statute citations still to be added (state surrogacy acts vary). UNVERIFIED: no statute or case opened. Gestator consent and the right to keep the child are out of scope (ASSUMED author decision 2026-11-04). |
| R4 | intended_parent | may | `(provide_care intended_parent child)` | `(and (parent intended_parent child) (is_subject child))` | none | superadditive | An intended parent may provide care for the child when a registered parent of the child and the child is a born subject. | unverified | [full source under Sources, R4](#src-r4) |
| R5 | intended_parent | must (implicit) | `(provide_care intended_parent child)` | `(and (parent intended_parent child) (is_subject child) (female intended_parent))` | none | tying | (practice, not written) A female intended parent must provide care for the child when a registered parent of the child and the child is a born subject; no sanction is attached. | unverified | [full source under Sources, R5](#src-r5) |
| R6 | registry | may | `(reprimand registry x)` | `true` | none | tying | The registry may reprimand at any time (the sanction for R3). | unverified | [full source under Sources, R6](#src-r6) |
| R7 | registry | may | `(register_parentage registry intended_parent child)` | `(is_subject child)` | none | tying | The registry may register an intended parent as parent of the child when the child is a born subject, with no birth condition. | unverified | [full source under Sources, R7](#src-r7) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R2: no variables
- R3: no variables
- R4: no variables
- R5: no variables
- R6: `x` = unbound (encoder to fix)
- R7: no variables

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R2**

- no work named: **unverified** (rationale: gestational surrogacy: the clinic implants an embryo in the gestator. Statute citations still to be added (state surrogacy acts vary))

**R3**

- no work named: **unverified** (rationale: the gestator carries to term and gives birth; the rival input sits in one body. Statute citations still to be added (state surrogacy acts vary))

<a id="src-r4"></a>
**R4**: care by any registered parent of a born child is permitted, men included; nothing here bars it. UNVERIFIED: no text opened for this rule (plans/ectogenesis.md section 2: Firestone 1970 ch.1 and ch.10 are cited from memory; the one network probe, an archive.org search, returned HTTP 200 and no text was read or downloaded)

- no work named: **unverified** (rationale: care by any registered parent of a born child is permitted, men included; nothing here bars it)

<a id="src-r5"></a>
**R5**: implicit norm (a care-norm, not a written rule; no sanction): the female registered parent of a born child must care for it. The condition names female and parent, NOT birthing_parent: the Kleven finding in docs/theory.md (adoptive mothers take the same hit, so role not body carries it). ASSUMED decision (author, 2026-11-04): trigger on female(p), so the norm survives the loss of the body. Not load-bearing at layer 1: it fires either way, so 'the tying strand outlives the rival input' is carried by the encoding, not discovered. UNVERIFIED: no text opened for this rule (plans/ectogenesis.md section 2: Firestone 1970 ch.1 and ch.10 are cited from memory; the one network probe, an archive.org search, returned HTTP 200 and no text was read or downloaded)

- no work named: **unverified** (rationale: implicit norm (a care-norm, not a written rule; no sanction): the female registered parent of a born child must care for it. The condition names female and parent, NOT birthing_parent: the Kleven finding in docs/theory.md (adoptive mothers take the same hit, so role not body carries it). ASSUMED dec...)

<a id="src-r6"></a>
**R6**: the registry's sanction for R3 (or_else target; R5's link removed 2026-11-04). Condition 'true' as in kibbutz-childrens-house R6; x is untyped (the sanctioned party differs by rule). UNVERIFIED: no text opened for this rule (plans/ectogenesis.md section 2: Firestone 1970 ch.1 and ch.10 are cited from memory; the one network probe, an archive.org search, returned HTTP 200 and no text was read or downloaded)

- no work named: **unverified** (rationale: the registry's sanction for R3 (or_else target; R5's link removed 2026-11-04). Condition 'true' as in kibbutz-childrens-house R6; x is untyped (the sanctioned party differs by rule))

<a id="src-r7"></a>
**R7**: parentage is registered for any born child; NO birthing_parent condition (ASSUMED author decision, 2026-11-04; the legal default today keys it to the birth, which would make care_decoupled_from_birth unreachable in E). UNVERIFIED: no text opened for this rule (plans/ectogenesis.md section 2: Firestone 1970 ch.1 and ch.10 are cited from memory; the one network probe, an archive.org search, returned HTTP 200 and no text was read or downloaded)

- no work named: **unverified** (rationale: parentage is registered for any born child; NO birthing_parent condition (ASSUMED author decision, 2026-11-04; the legal default today keys it to the birth, which would make care_decoupled_from_birth unreachable in E))


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| birth_labor_rival | structure | holds_to_k | Any gestation is held by exactly one body: whenever c is in gestation, exactly one agent gestates c. holds_to_k where the rival input sits in a body (gestational-surrogacy, preregistered); violated where gestation can be in a device (ectogenesis, preregistered), BY CONSTRUCTION (see history). Headline property of the ectogenesis pair (plans/ectogenesis.md section 3). |
| care_decoupled_from_birth | structure | unreachable_open | Care exists for a born child and no one is its birthing parent. is_subject guards against pre-birth vacuity (is_subject is set only by a birth action). Preregistered reachable in ectogenesis and unreachable_open in gestational-surrogacy (plans/ectogenesis.md section 3). |
| solo_care_by_non_birthing_parent | structure | reachable | Some non-birthing parent is the sole carer of the child at step t. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |

## Pairs

Extends [ectogenesis](ectogenesis.md); one line per change:
- R1 dropped: A provider may start gestation of a child at any time (Firestone 1970).
- R2 replaced: was "The provider may transfer the child to the device when the child is in gestation (Firestone 1970)." now "The provider may implant an embryo in the gestator for the child at any time (gestational surrogacy)."
- R3 replaced: was "The provider must decant the child when the child has been gestated ex utero, or else the registry may reprimand (R6) (Firestone 1970)." now "The gestator must give birth to the child when she is gestating it, or else the registry may reprimand (R6)."
- adds role gestator (the surrogate whose body carries the child; the rival input (one body, a short window; docs/theory.md 'Pregnancy, birth, nursing'))
- removes fluent gestated_ex_utero
- changes fluent birthing_parent (p gave birth to c): arg roles becomes ["gestator", "child"]
- adds fluent gestates (x's body carries c (surrogacy only))
- removes action start_gestation
- removes action transfer_to_device
- removes action decant
- adds action implant (does: in_gestation(child) := true, gestates(gestator, child) := true)
- adds action give_birth (does: birthing_parent(gestator, child) := true, is_subject(child) := true, in_gestation(child) := false, gestates(gestator, child) := false)
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
[ectogenesis](ectogenesis.md) is a minimal pair of this entry (rule R1,R2,R3).
Isomorphic to: ectogenesis (guard)
Not isomorphic to: ectogenesis, coverture-household, police-crisis, cps, kibbutz-childrens-house

<details><summary>Encoder notes (engine internals)</summary>

Control: the rival input moves to a weaker party (failure mode Displacement; the model case is the global care chain; layer 3). The minimal pair is recorded on ectogenesis. Revision 2 (2026-11-04): start_gestation merged into implant per plans/ectogenesis.md v2; v1 drift 1 stays in the record. ASSUMED author decisions (2026-11-04, from the encoder's brief, not from the plan file): R2+R3 substituted counts as a minimal pair; E R2/R3 tagged `superadditive` by hand (no new strand value; claim L11 is refuted for this reason, plan section 5c); R7 has no birthing_parent condition; R5 triggers on female(p) (role not body: Kleven, docs/theory.md); no leave action, so the plan's leave_reserved_for_non_birthing_parent row is dropped; neither entry is in CONTROLS (ectogenesis is not registered as a care-without-control control); gestator consent is out of scope. BY CONSTRUCTION, flagged in advance (plan section 5): birth_labor_rival in ectogenesis restates R2's effect list (gestates is never set there), and care_decoupled_from_birth in ectogenesis is reachable because decant omits birthing_parent (the only non-trivial leg is R7's missing birth condition); both properties carry by_construction: true, which the engine ignores. Treat those two verdicts as information, as marriage_requires_binding was, not as evidence; non-circular evidence needs layer 2/3. Also by construction: gestated_ex_utero exists only to mark an absence. PREREGISTERED (plans/ectogenesis.md section 3, before any run; layer 1, init declared, strict compliance, k=6). gestational-surrogacy: birth_labor_rival holds_to_k; care_decoupled_from_birth unreachable_open; solo_care_by_non_birthing_parent reachable; care_assigned_by_sex violated. ectogenesis: birth_labor_rival violated; care_decoupled_from_birth reachable; solo_care_by_non_birthing_parent reachable; care_assigned_by_sex violated. Headline difference: birth_labor_rival. Iso (ADR 0010, about 65% confident): ectogenesis ~ surrogacy iso at guard, not iso at guard+strands (R2/R3 rival to superadditive tag flip), not iso at exact; ectogenesis not iso coverture-household / police-crisis / cps / kibbutz-childrens-house (no control permission over the subject, no exit bar, so the care+control sub-signature fails); vs transferable-leave / paternity-quota a guess of partial at guard+strands, two legs (R5~R7 implicit must-care by attribute; R4~R5 may care), about 40% confident. Failure modes (ADR 0016): surrogacy Displacement (layer 3); ectogenesis Dark twin (layer 3), Capture (needs a new rule), Dead letter (layer 2); R5 surviving is partial reform, no mode. Layer 2 not required.

</details>

# lease

**Residential lease (negative control: care duty + eviction power, tenant may leave)**

> 'The lessor of a building intended for the occupation of human beings must, in the absence of an agreement to the contrary, put it into a condition fit for such occupation, and repair all subsequent dilapidations thereof, which render it untenantable.' Cal. Civ. Code s. 1941, read at https://california.public.law/codes/ca_civ_code_section_1941. A tenant 'is guilty of unlawful detainer' who continues in possession after default in rent or 'after a neglect or failure to perform other conditions or covenants of the lease' and three days' notice, Cal. Code Civ. Proc. s. 1161(2)-(3), read at https://california.public.law/codes/ca_civ_proc_code_section_1161. A hiring for an unspecified term ends when 'one of the parties gives written notice to the other of that party's intention to terminate the same', Cal. Civ. Code s. 1946, read at https://california.public.law/codes/ca_civ_code_section_1946.

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

- **landlord**: the lessor
- **tenant**: the lessee; the counterparty, not a dependent

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | landlord | may | `(lease_to l t)` | `(not (leased l t))` | none | tying | The landlord may lease to the tenant when the premises are not already leased to the tenant. | unverified | a lease is formed by agreement. UNVERIFIED (general knowledge; no source opened) |
| R2 | landlord | must | `(habitable l t)` | `(leased l t)` | none | superadditive | The premises being habitable must hold when leased to the tenant, the landlord being bound (Cal. Civ. Code 1941). | opened | [full source under Sources, R2](#src-r2) https://california.public.law/codes/ca_civ_code_section_1941. |
| R3 | landlord | may | `(evict l t)` | `(and (leased l t) (not (rent_paid t)))` | none | rival | The landlord may evict the tenant when the premises are leased and rent has not been paid (Cal. Code Civ. Proc. 1161). | recalled | Cal. Code Civ. Proc. s. 1161(2)-(3) (tenant guilty of unlawful detainer who continues in possession after default in rent, or after neglect or failure to perform other conditions or covenants of the lease, and three days' notice); https://california.public.law/codes/ca_civ_proc_code_section_1161 |
| R4 | tenant | may | `(vacate t)` | `(leased l t)` | none | rival | The tenant may vacate when the premises are leased to the tenant (Cal. Civ. Code 1946). | recalled | [full source under Sources, R4](#src-r4) https://california.public.law/codes/ca_civ_code_section_1946 |
| R5 | tenant | must | `(rent_paid t)` | `(leased l t)` | R3 `(evict l t)` | tying | Rent being paid must hold for the tenant when the premises are leased, or else the landlord may evict (R3) (Cal. Code Civ. Proc. 1161). | recalled | [full source under Sources, R5](#src-r5) https://california.public.law/codes/ca_civ_proc_code_section_1161 |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R1: `l` = landlord (action lease_to, effects); `t` = tenant (action lease_to, effects)
- R2: `l` = landlord (fluent habitable); `t` = tenant (fluent habitable)
- R3: `l` = landlord (action evict, effects); `t` = tenant (action evict, effects)
- R4: `t` = tenant (action vacate, effects); `l` = landlord (fluent leased)
- R5: `t` = tenant (fluent rent_paid); `l` = landlord (fluent leased)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- no work named: **unverified** (rationale: a lease is formed by agreement)

<a id="src-r2"></a>
**R2**: Cal. Civ. Code s. 1941 ('The lessor of a building intended for the occupation of human beings must ... put it into a condition fit for such occupation, and repair all subsequent dilapidations thereof, which render it untenantable'); https://california.public.law/codes/ca_civ_code_section_1941. [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] let establishes habitable; repair restores it, withhold_repairs breaks it Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_civ_code_section_1941: 'The lessor of a building intended for the occupation of human beings must, in the absence of an agreement to the contrary, put it into a condition fit for such occupation, and repair all subsequent dilapidations thereof, which render it untenantable'.

- `cal-civ-1941` (s. 1941; US-CA; date n/a): **opened** 2026-11-06: "The lessor of a building intended for the occupation of human beings must, in the absence of an agreement to the contrary, put it into a condition fit for such occupation, and repair all subsequent dilapidations thereof, which render it untenantable"

**R3**

- `cal-ccp-1161` (s. 1161(2)-(3); US-CA; date n/a): **recalled**

<a id="src-r4"></a>
**R4**: Cal. Civ. Code s. 1946 (a hiring of real property for an unspecified term is terminated by either party's written notice); https://california.public.law/codes/ca_civ_code_section_1946 (either party may terminate by notice; the tenant's exit is permitted and unsanctioned). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(t) = vacate enabled

- `cal-civ-1946` (s. 1946; US-CA; date n/a): **recalled**

<a id="src-r5"></a>
**R5**: Cal. Code Civ. Proc. s. 1161(2)-(3) (tenant guilty of unlawful detainer who continues in possession after default in rent, or after neglect or failure to perform other conditions or covenants of the lease, and three days' notice); https://california.public.law/codes/ca_civ_proc_code_section_1161 (default in rent is the breach that opens eviction). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] let establishes rent_paid; pay_rent restores it, default_rent breaks it (sanction R3)

- `cal-ccp-1161` (s. 1161(2)-(3); US-CA; date n/a): **recalled**


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | unreachable_open | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |

## Pairs

Not isomorphic to: coverture-household, police-crisis, cps

<details><summary>Encoder notes (engine internals)</summary>

Negative control for gate (b). It has the two legs the review (finding 4) showed were enough for the old matcher, a superadditive must (R2, habitable) and a rival may on the same counterparty by the same attribute (R3, evict), and lacks the third: no must_not binds the tenant, who may vacate (R4). If the cluster matcher reports a care+control form here, the form is too loose. dependent_cannot_exit is unreachable because can_exit(t) is derived from R4, which is enabled whenever leased. The breakers withhold_repairs and default_rent exist so that R2 and R5 are not inert.

</details>

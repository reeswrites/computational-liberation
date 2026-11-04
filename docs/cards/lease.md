# lease

**Residential lease (negative control: care duty + eviction power, tenant may leave)**

> 'The lessor of a building intended for the occupation of human beings must, in the absence of an agreement to the contrary, put it into a condition fit for such occupation, and repair all subsequent dilapidations thereof, which render it untenantable.' Cal. Civ. Code s. 1941, read at https://california.public.law/codes/ca_civ_code_section_1941. A tenant 'is guilty of unlawful detainer' who cont...

## Roles

- **landlord**: the lessor
- **tenant**: the lessee; the counterparty, not a dependent

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | landlord | may | `(lease_to l t)` | `(not (leased l t))` | none | tying | The landlord may lease to the tenant when the premises are not already leased to the tenant. | a lease is formed by agreement. UNVERIFIED (general knowledge; no source opened) |
| R2 | landlord | must | `(habitable l t)` | `(leased l t)` | none | superadditive | The premises being habitable must hold when leased to the tenant, the landlord being bound (Cal. Civ. Code 1941). | Cal. Civ. Code s. 1941 ('The lessor of a building intended for the occupation of... https://california.public.law/codes/ca_civ_code_section_1941. |
| R3 | landlord | may | `(evict l t)` | `(and (leased l t) (not (rent_paid t)))` | none | rival | The landlord may evict the tenant when the premises are leased and rent has not been paid (Cal. Code Civ. Proc. 1161). | Cal. Code Civ. Proc. s. 1161(2)-(3) (tenant guilty of unlawful detainer who cont... https://california.public.law/codes/ca_civ_proc_code_section_1161 |
| R4 | tenant | may | `(vacate t)` | `(leased l t)` | none | rival | The tenant may vacate when the premises are leased to the tenant (Cal. Civ. Code 1946). | Cal. Civ. Code s. 1946 (a hiring of real property for an unspecified term is ter... https://california.public.law/codes/ca_civ_code_section_1946 |
| R5 | tenant | must | `(rent_paid t)` | `(leased l t)` | R3 `(evict l t)` | tying | Rent being paid must hold for the tenant when the premises are leased, or else the landlord may evict (R3) (Cal. Code Civ. Proc. 1161). | Cal. Code Civ. Proc. s. 1161(2)-(3) (tenant guilty of unlawful detainer who cont... https://california.public.law/codes/ca_civ_proc_code_section_1161 |

**Default capacities** (enabled unless an express disability bars them): none

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | unreachable_open | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |

## Pairs

Not isomorphic to: coverture-household, police-crisis, cps

## Notes

Negative control for gate (b). It has the two legs the review (finding 4) showed were enough for the old matcher, a superadditive must (R2, habitable) and a rival may on the same counterparty by the same attribute (R3, evict), and lacks the third: no must_not binds the tenant, who may vacate (R4). If the cluster matcher reports a care+control form here, the form is too loose. dependent_cannot_exit is unreachable because can_exit(t) is derived from R4, which is enabled whenever leased. The breakers withhold_repairs and default_rent exist so that R2 and R5 are not inert.

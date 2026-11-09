# footbinding-no-pledge

**Footbinding without the pledge action (minimal pair for gate (a))**

> Construction: footbinding with both pledge actions (leave_unbound_pledge, accept_match_pledge) and their rules R4 and R10 deleted (R10 since 2026-11-04, encoding review finding 2); pledged stays declared but nothing sets it. Historically the pre-1874 situation (no pledge associations).

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **family**: the household deciding for a daughter (Mackie's 'parents' who bind, or pledge not to); the institutional sort, not a demographic (ADR 0011)
- **daughter**: the subject: the girl whose feet are bound or left unbound; bound in childhood, so she decides nothing
- **suitor**: the family of a prospective groom: the marriage-market counterparty whose expectations hold the convention

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | family | may [kind: norm; sanctioner: none] | `(bind family daughter)` | `(is_subject daughter)` | none | tying | (practice, not written) A family may bind its daughter when she is a subject of the institution (Mackie 1996). | unverified | [full source under Sources, R1](#src-r1) https://www.jstor.org/stable/2096305 |
| R2 | family | may (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(leave_unbound family daughter)` | `(is_subject daughter)` | none | tying | (practice, not written) A family may leave its daughter unbound when she is a subject of the institution. | unverified | implicit: leaving a daughter unbound is always physically open to the family; R3 is what sanctions it. Per ADR 0015 A6 every action an agent may take needs a may rule. UNVERIFIED (reconstructed from the convention account; no primary text opened) |
| R3 | family | must not (implicit) [kind: norm; sanctioner: peers] (sanctioner derived, unreviewed) | `(leave_unbound family daughter)` | `(is_subject daughter)` | R5 `(reject_match suitor daughter)` | tying | (practice, not written) A family must not leave its daughter unbound when she is a subject, or else the suitor may reject the match (R5) (Mackie 1996). | unverified | [full source under Sources, R3](#src-r3) https://www.jstor.org/stable/2096305 |
| R5 | suitor | may (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(reject_match suitor daughter)` | `(and (is_subject daughter) (not (bound daughter)) (not (pledged family)) (not (pledged suitor)))` | none | rival | (practice, not written) A suitor may reject the match when the daughter is a subject, is not bound, and neither the family nor the suitor has pledged (Mackie 1996). | unverified | [full source under Sources, R5](#src-r5) https://www.jstor.org/stable/2096305 |
| R6 | suitor | may [kind: norm; sanctioner: none] | `(accept_match suitor daughter)` | `(and (is_subject daughter) (or (bound daughter) (pledged family) (pledged suitor)))` | none | tying | (practice, not written) A suitor may accept the match when the daughter is a subject and is bound, or the family or the suitor has pledged (Mackie 1996). | unverified | [full source under Sources, R6](#src-r6) https://www.jstor.org/stable/2096305 |
| R7 | family | may [kind: norm; sanctioner: none] | `(marry_off family daughter)` | `(and (is_subject daughter) (or (bound daughter) (pledged family)))` | none | tying | (practice, not written) A family may marry off its daughter when she is a subject and is bound or the family has pledged (Mackie 1996). | recalled | [full source under Sources, R7](#src-r7) https://www.jstor.org/stable/2096305 |
| R9 | daughter | must not (disability) (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(refuse_binding daughter)` | `(is_subject daughter)` | none | rival | (practice, not written) The daughter cannot refuse binding while she is a subject: no such power exists (ADR 0013). | unverified | [full source under Sources, R9](#src-r9) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): refuse_binding

## Variables

- R1: no variables
- R2: no variables
- R3: no variables
- R5: no variables
- R6: no variables
- R7: no variables
- R9: no variables

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):999-1017 (1996), abstract (read 2026-11-04 as a search-index snippet, the article itself not opened: https://www.jstor.org/stable/2096305 paywalled, PDF mirrors unreachable from this session): 'Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market'; 'A Schelling coordination diagram explains how the three methods of the Chinese campaign to abolish footbinding succeeded in bringing it to a quick end'; 'The convention hypothesis predicts that promotion of such pledge associations would help bring female genital mutilation to an end' [F for these sentences; body [R]] (the practice; each step is a cohort decision, so the rule stays enabled while a subject exists). UNVERIFIED (reconstructed from the convention account; no primary text opened) as a rule: no text says a family 'may' bind, the convention presupposes it Retagged norm 2026-11-08 (batch 3b, B4 ruling): Mackie's convention is unwritten; the marriage market, not a body, enforces it.

- `mackie-1996` (abstract; date n/a): **snippet** 2026-11-04: "Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market"
- no work named: **unverified** (the rule (a family 'may' bind) is reconstructed from the convention account; no primary text opened: UNVERIFIED as a rule)

**R2**

- no work named: **unverified** (rationale: implicit: leaving a daughter unbound is always physically open to the family; R3 is what sanctions it. Per ADR 0015 A6 every action an agent may take needs a may rule)

<a id="src-r3"></a>
**R3**: SANCTIONED NORM (implicit; a convention, not a written rule): a family that leaves a daughter unbound loses her on the marriage market: Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):999-1017 (1996), abstract (read 2026-11-04 as a search-index snippet, the article itself not opened: https://www.jstor.org/stable/2096305 paywalled, PDF mirrors unreachable from this session): 'Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market'; 'A Schelling coordination diagram explains how the three methods of the Chinese campaign to abolish footbinding succeeded in bringing it to a quick end'; 'The convention hypothesis predicts that promotion of such pledge associations would help bring female genital mutilation to an end' [F for these sentences; body [R]]. or_else R5 (the suitor's rejection) is the market sanction; the norm is stated unconditionally because it is the wider society's expectation, and it is the SANCTION (R5) that a pledge association lifts, not the norm. Tying: binding is tied to marriage, which is Mackie's whole point

- `mackie-1996` (abstract; date n/a): **snippet** 2026-11-04: "maintained by interdependent expectations on the marriage market"
- no work named: **unverified** (implicit sanctioned norm: a convention, not a written rule; the abstract supports the convention, no text states the norm)

<a id="src-r5"></a>
**R5**: implicit: the marriage market refuses an unbound bride (R3's or_else), 'maintained by interdependent expectations on the marriage market' (Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):999-1017 (1996), abstract (read 2026-11-04 as a search-index snippet, the article itself not opened: https://www.jstor.org/stable/2096305 paywalled, PDF mirrors unreachable from this session): 'Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market'; 'A Schelling coordination diagram explains how the three methods of the Chinese campaign to abolish footbinding succeeded in bringing it to a quick end'; 'The convention hypothesis predicts that promotion of such pledge associations would help bring female genital mutilation to an end' [F for these sentences; body [R]]); NOT enabled once the family or the suitor has pledged, because pledged families' sons marry only unbound women (Anti-footbinding pledge associations: Heavenly Foot Society (Xiamen, 1874, MacGowan) and the Tian Zu Hui / Natural Foot Society (Shanghai, 1895, Alicia Little; Chinese reformers' societies from 1897, claimed membership ~300,000): members pledged not to bind their daughters' feet and not to let their sons marry women with bound feet (Wikipedia 'Tian Zu Hui', 'Heavenly Foot Society', 'Foot Emancipation Society', read 2026-11-04 as search snippets only, pages not opened: [R]; Mackie 1996 names the same two-part pledge for the FGC analogue, abstract [F]); (pledged suitor) added 2026-11-04, encoding review finding 2): that lapse of the sanction is the mechanism. Rival: a match refused here is a match made elsewhere. Strand tag by analogy with the house exit pattern, not from the source (encoding review 2026-11-04 finding 6). UNVERIFIED (reconstructed from the convention account; no primary text opened) as a rule

- `mackie-1996` (abstract; date n/a): **snippet** 2026-11-04: "maintained by interdependent expectations on the marriage market"
- `wikipedia-tian-zu-hui` (date n/a): **recalled**
- `wikipedia-heavenly-foot-society` (date n/a): **recalled**
- `wikipedia-foot-emancipation-society` (date n/a): **recalled**
- no work named: **unverified** (implicit: the market's refusal of an unbound bride, reconstructed from the convention account: UNVERIFIED as a rule)

<a id="src-r6"></a>
**R6**: the convention from the groom's side: a bound daughter is acceptable; an unbound one only inside the pledge association, on either side's pledge (Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):999-1017 (1996), abstract (read 2026-11-04 as a search-index snippet, the article itself not opened: https://www.jstor.org/stable/2096305 paywalled, PDF mirrors unreachable from this session): 'Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market'; 'A Schelling coordination diagram explains how the three methods of the Chinese campaign to abolish footbinding succeeded in bringing it to a quick end'; 'The convention hypothesis predicts that promotion of such pledge associations would help bring female genital mutilation to an end' [F for these sentences; body [R]]; Anti-footbinding pledge associations: Heavenly Foot Society (Xiamen, 1874, MacGowan) and the Tian Zu Hui / Natural Foot Society (Shanghai, 1895, Alicia Little; Chinese reformers' societies from 1897, claimed membership ~300,000): members pledged not to bind their daughters' feet and not to let their sons marry women with bound feet (Wikipedia 'Tian Zu Hui', 'Heavenly Foot Society', 'Foot Emancipation Society', read 2026-11-04 as search snippets only, pages not opened: [R]; Mackie 1996 names the same two-part pledge for the FGC analogue, abstract [F]); (pledged suitor) added 2026-11-04, encoding review finding 2). UNVERIFIED (reconstructed from the convention account; no primary text opened) as a rule Retagged norm 2026-11-08 (batch 3b, B4 ruling): Mackie's convention is unwritten; the marriage market, not a body, enforces it.

- `mackie-1996` (abstract; date n/a): **snippet** 2026-11-04: "maintained by interdependent expectations on the marriage market"
- `wikipedia-tian-zu-hui` (date n/a): **recalled**
- `wikipedia-heavenly-foot-society` (date n/a): **recalled**
- `wikipedia-foot-emancipation-society` (date n/a): **recalled**
- no work named: **unverified** (the groom-side convention, reconstructed from the convention account: UNVERIFIED as a rule)

<a id="src-r7"></a>
**R7**: the marriage condition: Mackie, 'Ending Footbinding and Infibulation: A Convention Account', ASR 61(6):999-1017 (1996), abstract (read 2026-11-04 as a search-index snippet, the article itself not opened: https://www.jstor.org/stable/2096305 paywalled, PDF mirrors unreachable from this session): 'Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market'; 'A Schelling coordination diagram explains how the three methods of the Chinese campaign to abolish footbinding succeeded in bringing it to a quick end'; 'The convention hypothesis predicts that promotion of such pledge associations would help bring female genital mutilation to an end' [F for these sentences; body [R]] ('interdependent expectations on the marriage market'); Brown, Bossen, Gates & Satterthwaite-Phillips, 'Marriage Mobility and Footbinding in Pre-1949 Rural China', J. Asian Studies 71(4):1035-1067 (2012), abstract only (search snippet, 2026-11-04, [R]): in a sample of 7,314 rural women footbinding did not guarantee a better marriage (two-thirds did not marry up); the marriage-market reading is Mackie's, and this entry encodes it as the convention, not as a claim that binding bought mobility (the data qualify mobility, not marriageability as encoded). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] marriageable(f, d) = marry_off enabled (R7) Retagged norm 2026-11-08 (batch 3b, B4 ruling): Mackie's convention is unwritten; the marriage market, not a body, enforces it.

- `mackie-1996` (abstract; date n/a): **snippet** 2026-11-04: "maintained by interdependent expectations on the marriage market"
- `brown-bossen-gates-satterthwaite-phillips-2012` (abstract; date n/a): **recalled**

<a id="src-r9"></a>
**R9**: binding is done to a young girl by her family: she has no say. A disability (or_else null), the subject-side exit bar per ADR 0013. [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.] Strand tag by analogy with the house exit pattern, not from the source (encoding review 2026-11-04 finding 6). UNVERIFIED (reconstructed from the convention account; no primary text opened) (age at binding and the mother's role are general knowledge, no text opened; implicit set True 2026-11-04, encoding review finding 6: an UNVERIFIED rule with no text opened is implicit)

- no work named: **unverified** (rationale: binding is done to a young girl by her family: she has no say. A disability (or_else null), the subject-side exit bar per ADR 0013. Strand tag by analogy with the house exit pattern, not from the source (encoding review 2026-11-04 finding 6))


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| binding_practised | freedom | persists | Footbinding is in force: some subject (the current cohort's daughter) has bound feet at step t. The layer-2 gate (a) reads it on the ABM state (philengine/abm/gate.py A_PROP). Layer 1: persists under the sanctioned norm (preregistered 2026-11-04); collapse is a layer-2 claim. |
| marriage_requires_binding | freedom | holds_to_k | Mackie's convention: whenever a family can marry off a subject, she is bound or the family has pledged (an unbound daughter is marriageable only inside a pledge association). holds_to_k in both footbinding entries (preregistered 2026-11-04) BY CONSTRUCTION, see history: information, not a verdict. Non-vacuous: marriageable(family, daughter) is true at t=0. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |

## Pairs

Extends [footbinding](footbinding.md); one line per change:
- R4 dropped: (practice, not written) A family may take the anti-footbinding pledge for its daughter when she is a subject (pledge associations, 1874 onward).
- R10 dropped: (the pledge associations' written pledge; text not opened) A suitor may take the pledge to accept an unbound bride (the sons' half of the pledge) when the daughter is a subject.
- removes action leave_unbound_pledge
- removes action accept_match_pledge
- overrides minimal_pair_of
- overrides notes
Minimal pair of [footbinding](footbinding.md), differing in rule R4,R10; no layer-1 property separates the pair.
Not isomorphic to: coverture-household, police-crisis, cps

<details><summary>Encoder notes (engine internals)</summary>

PREREGISTERED (2026-11-04, before any run): the same four verdicts as footbinding (persists, holds_to_k, reachable, reachable): pledges change nothing at layer 1. The pair is the gate (a) 'pledge actions exist' half: crit_a reads _has_pledges on `footbinding` itself, so this entry is the dataset's record of what the no-pledge world looks like and `differs_on` is null by design (no layer-1 property separates them). At layer 2 the preregistration is the plan's: binding persists here under every module. PREREGISTERED (2026-11-04, encoding review finding 2, written and committed before the first run with the suitor pledge): adding accept_match_pledge(suitor, daughter) [effect pledged(suitor)] with rule R10 suitor may accept_match_pledge, and reading (pledged suitor) in R5 (and-not) and R6 (or), changes NO layer-1 verdict in footbinding or footbinding-no-pledge: binding_practised persists, marriage_requires_binding holds_to_k, subject_cannot_exit and dependent_cannot_exit reachable in both; the new pledge only lifts the sanction R5 (and widens R6), R3 is unconditional, R7 is untouched, and pledged is a fluent per role (footbinding-no-pledge strips BOTH pledge actions and both pledge rules R4 and R10, so nothing sets pledged(suitor) there). Iso: still none at every level against the care+control cluster; isomorphic_to nothing. Expected warnings unchanged (can_sanction, provides_care, has_standing, can_claim_for undeclared). Layer 2 (information, not an expectation): pledged(suitor) is role-level too (A2), so one suitor's pledge lifts R5 for every suitor, the same coarseness as pledged(family): the A2 caveat now applies on both sides; gate (a)'s _has_pledges reading is unchanged (true via either pledge) and ablate_pledges strips both. If any verdict flips, the drift is recorded here and the expectations are not edited. RESULT (2026-11-04, after the run, commit b6f48aa preceding it): no drift. check-all 115/115 with all four verdicts as preregistered in both entries; `phil rules gate` PASS; pytest 15 passed; no warning printed for either entry (none was printed before the change either). ABM information, `--seeds 5 --steps 60 --modules material,coordination`: bound 1.0 in every seed (persistence), pledged 0.667 over seeds, i.e. true on the family and the suitor role tuple and not the daughter's: the A2 caveat on both sides, as the preregistration said; breach, sanction and unavoidable rates 0. Drift 2026-11-04 (encoding review finding 3): marriage_requires_binding is by construction (marriageable is derived from R7's enabledness and R7's condition is bound-or-pledged, so the property restates the rule); kept in expected_properties for the record, not evidence; the property carries by_construction: true, which the engine ignores. Layer 1 has one cohort (encoding review 2026-11-04 finding 4): one daughter, bound at t=0, and `married` never clears, so no trace shows a per-cohort binding decision before the market; a `new_cohort` action clearing bound/married is deferred to the author.

</details>

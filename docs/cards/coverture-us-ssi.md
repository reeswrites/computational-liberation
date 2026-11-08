# coverture-us-ssi

**Composite: coverture household (US) + SSI marriage penalty, the husband as claimant and the wife as spouse**

> composite of: coverture-household-us, ssi-marriage-penalty

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

**Constructed world (ADR 0018):** composed from coverture-household-us, ssi-marriage-penalty for check claim C2b (second half of C2): does deleting SSI R2 or R3 flip financial_dependence (`phil rules ablate --entry coverture-us-ssi`); not a historical institution; the members span 1787–2008 (from provenance effective_date where present).

Council: docs/reviews/2026-11-08-p2-correctness.md, 2026-11-08-p2-faithfulness.md, 2026-11-08-p2-card-only.md

## Members

A composite (ADR 0018): the members' roles are unioned after the aliases below, fluents unified by name, rules concatenated under `<member>__` prefixes. Each rule row below is the member's rule, unchanged except for the renamed roles; its plain line and sources are the member's.

- [coverture-household-us](coverture-household-us.md): husband → partner_a, wife → partner_b
- [ssi-marriage-penalty](ssi-marriage-penalty.md): claimant → partner_a, spouse → partner_b

Initial literals: `(resources_under_limit partner_a)`, `female(partner_b)` (init mode `declared`; fluents not listed start false)

Free at t=0: `acquired_property`, `earns`

Role map: **partner_a** = husband in coverture-household-us = claimant in ssi-marriage-penalty; **partner_b** = wife in coverture-household-us = spouse in ssi-marriage-penalty

Alias map (original role gloss):
- husband (coverture-household-us) → partner_a: the husband; the legal person the marriage keeps
- wife (coverture-household-us) → partner_b: the feme covert; her legal existence is suspended during marriage
- claimant (ssi-marriage-penalty) → partner_a: the person who applies for or receives SSI (the benefit's subject)
- spouse (ssi-marriage-penalty) → partner_b: the other person of the pair, a legal spouse or a cohabitant who holds out as one

Actions (name(parameters): what they set; a member's rules permit, oblige or bar them; `from member` is the entry that declares the action):
- `marry(h, w)` [h: partner_a; w: partner_b]: married(h, w), is_subject(w), provides_care(h, w), provides_care(w, h) (from member: coverture-household-us)
- `hold_property(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `keep_earnings(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `maintain(h, w)` [h: partner_a; w: partner_b]: provides_care(h, w) (from member: coverture-household-us)
- `neglect(h, w)` [h: partner_a; w: partner_b]: not provides_care(h, w) (from member: coverture-household-us)
- `keep_house(w, h)` [w: partner_b; h: partner_a]: provides_care(w, h) (from member: coverture-household-us)
- `neglect_house(w, h)` [w: partner_b; h: partner_a]: not provides_care(w, h) (from member: coverture-household-us)
- `control_property(h, w)` [h: partner_a; w: partner_b]: no effect (from member: coverture-household-us)
- `chastise(h, w)` [h: partner_a; w: partner_b]: no effect (from member: coverture-household-us)
- `misbehave(w)` [w: partner_b]: misbehaves(w) (from member: coverture-household-us)
- `draw_subsistence(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `leave(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `sue(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `contract(w)` [w: partner_b]: no effect (from member: coverture-household-us)
- `wed(c, s)` [c: partner_a; s: partner_b]: married(c, s) (from member: ssi-marriage-penalty)
- `divorce(c, s)` [c: partner_a; s: partner_b]: not married(c, s) (from member: ssi-marriage-penalty)
- `cohabit(c, s)` [c: partner_a; s: partner_b]: cohabits(c, s) (from member: ssi-marriage-penalty)
- `separate(c, s)` [c: partner_a; s: partner_b]: not cohabits(c, s), not holds_out(c, s) (from member: ssi-marriage-penalty)
- `present_as_married(c, s)` [c: partner_a; s: partner_b]: holds_out(c, s) (from member: ssi-marriage-penalty)
- `cease_holding_out(c, s)` [c: partner_a; s: partner_b]: not holds_out(c, s) (from member: ssi-marriage-penalty)
- `accumulate(c)` [c: partner_a]: not resources_under_limit(c) (from member: ssi-marriage-penalty)
- `spend_down(c)` [c: partner_a]: resources_under_limit(c) (from member: ssi-marriage-penalty)
- `apply_couple_rate(g, c, s)` [c: partner_a; s: partner_b]: no effect (from member: ssi-marriage-penalty)
- `apply_couple_limit(g, c, s)` [c: partner_a; s: partner_b]: no effect (from member: ssi-marriage-penalty)
- `apply_individual_rate(g, c, s)` [c: partner_a; s: partner_b]: no effect (from member: ssi-marriage-penalty)
- `apply_individual_limit(g, c, s)` [c: partner_a; s: partner_b]: no effect (from member: ssi-marriage-penalty)
- `pay_benefit(g, c)` [c: partner_a]: no effect (from member: ssi-marriage-penalty)

## Roles

- **partner_a**: the husband; the legal person the marriage keeps
- **partner_b**: the feme covert; her legal existence is suspended during marriage
- **agency**: the Social Security Administration, which decides marital status and applies the rate and the limit

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| coverture_household_us__R1 | partner_a | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone II.29). | opened | [full source under Sources, coverture_household_us__R1](#src-coverture_household_us__r1) https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: |
| coverture_household_us__R2 | partner_a | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R2](#src-coverture_household_us__r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| coverture_household_us__R3 | partner_b | must (implicit) [kind: norm; sanctioner: family] (sanctioner derived, unreviewed) | `(provides_care w h)` | `(married h w)` | coverture_household_us__R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (coverture_household_us__R5). | unverified | [full source under Sources, coverture_household_us__R3](#src-coverture_household_us__r3) |
| coverture_household_us__R4 | partner_b | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R4](#src-coverture_household_us__r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| coverture_household_us__R5 | partner_a | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R5](#src-coverture_household_us__r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| coverture_household_us__R6 | partner_b | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only). | opened | [full source under Sources, coverture_household_us__R6](#src-coverture_household_us__r6) https://www.nber.org/system/files/working_papers/w10175/w10175.pdf |
| coverture_household_us__R7 | partner_b | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R7](#src-coverture_household_us__r7) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| ssi_marriage_penalty__R1 | agency | may [kind: formal; sanctioner: none] | `(pay_benefit g c)` | `true` | none | tying | The agency may pay the claimant a benefit (42 U.S.C. 1382(a)); the encoder's grant, so that the resource bar in ssi_marriage_penalty__R7 has a power to remove. | unverified | The SSI payment power, 42 U.S.C. 1382(a). UNVERIFIED as a rule row: no excerpt supports a bare grant of the power to pay; it is the encoder's skeleton so that R7 (the resource bar) removes something. Sanctioner none: the sources opened name no enforcement of the agency's payment duty. |
| ssi_marriage_penalty__R2 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(married c s)` | none | tying | The agency may rate the claimant and the other person as a couple, counting combined income at the couple rate, when they are married (20 CFR 416.1802(b)(1); 42 U.S.C. 1382(b)(2)). The source states this for a spouse "with whom he or she is living" (20 CFR 416.1801(c); 42 U.S.C. 1382(a)(1)(B)(i)); the rule encodes marriage alone (cohabitation condition not encoded; revision 2 item). | unverified | [full source under Sources, ssi_marriage_penalty__R2](#src-ssi_marriage_penalty__r2) https://www.law.cornell.edu/cfr/text/20/416.1802 |
| ssi_marriage_penalty__R3 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_limit g c s)` | `(married c s)` | none | tying | The agency may apply the couple resource limit ($3,000) when they are married (42 U.S.C. 1382(a)(3)(A)). The source states the couple limit for an individual with a spouse "with whom he is living" (42 U.S.C. 1382(a)(1)(B)(i)); the rule encodes marriage alone (cohabitation condition not encoded; revision 2 item). Note, the CRS reading, not the text: two individuals may hold $4,000 together, so the couple limit is the lower. | snippet | [full source under Sources, ssi_marriage_penalty__R3](#src-ssi_marriage_penalty__r3) https://www.law.cornell.edu/uscode/text/42/1382 |
| ssi_marriage_penalty__R4 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(and (cohabits c s) (holds_out c s))` | none | tying | The agency may rate cohabitants as a couple, as if married, when they live together and lead people to believe they are husband and wife. Text as written (20 CFR 416.1806(a)(3)): "an unrelated person of the opposite sex ... at or after the time you apply". The encoding follows POMS SI 00501.152, which applies the test to same-sex couples, so the formal rule carries no sex condition. | snippet | [full source under Sources, ssi_marriage_penalty__R4](#src-ssi_marriage_penalty__r4) https://www.law.cornell.edu/cfr/text/20/416.1806 |
| ssi_marriage_penalty__R5 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_rate g c s)` | `(not (or (married c s) (and (cohabits c s) (holds_out c s))))` | none | tying | The agency may rate the claimant as an individual when the pair are neither married nor holding out. The individual-rate consequence for the unmarried is from CRS RL33675 (snippet); 20 CFR 416.1802(d)(1) says only that benefits depend on whether you are married. | snippet | [full source under Sources, ssi_marriage_penalty__R5](#src-ssi_marriage_penalty__r5) https://www.everycrsreport.com/reports/RL33675.html |
| ssi_marriage_penalty__R6 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_limit g c s)` | `(not (or (married c s) (and (cohabits c s) (holds_out c s))))` | none | tying | The agency may apply the individual resource limit ($2,000) when the pair are neither married nor holding out (42 U.S.C. 1382(a)(3)). | snippet | 42 U.S.C. 1382(a)(3)(B) as carried from the worklist (summarising fetch; not re-opened; level snippet): '$2,000 on January 1, 1989' for an individual, '$3,000 on January 1, 1989' for a couple. The complement condition is the encoder's reading. |
| ssi_marriage_penalty__R7 | agency | must not (disability) [kind: formal; sanctioner: none] | `(pay_benefit g c)` | `(not (resources_under_limit c))` | none | rival | The agency cannot pay the claimant a benefit while the claimant's countable resources exceed the applicable limit: no such power exists (the bar is an eligibility condition, 42 U.S.C. 1382(a)(1)(B), (a)(2)(B); the limits are in (a)(3)(A)-(B)). | unverified | [full source under Sources, ssi_marriage_penalty__R7](#src-ssi_marriage_penalty__r7) https://www.law.cornell.edu/uscode/text/42/1382 |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- coverture_household_us__R1: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R2: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R3: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R4: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R5: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R6: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R7: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- ssi_marriage_penalty__R1: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles)
- ssi_marriage_penalty__R2: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles); `s` = partner_b (rule var_roles)
- ssi_marriage_penalty__R3: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles); `s` = partner_b (rule var_roles)
- ssi_marriage_penalty__R4: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles); `s` = partner_b (rule var_roles)
- ssi_marriage_penalty__R5: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles); `s` = partner_b (rule var_roles)
- ssi_marriage_penalty__R6: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles); `s` = partner_b (rule var_roles)
- ssi_marriage_penalty__R7: `g` = agency (rule var_roles); `c` = partner_a (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-coverture_household_us__r1"></a>
**coverture_household_us__R1**: Blackstone, Commentaries on the Laws of England, Book II ch. 29 'Of Title by Succession, Marriage, and Judgment' (1766), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: chattels 'which belonged formerly to the wife, are by act of law vested in the husband' and 'the husband hath therein an immediate and absolute property, devolved to him by the marriage' (long s modernised from the OCR). Re-sourced 2026-11-04: Book I ch. 15 (the earlier citation; https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/, the husband and wife are one person in law) says 'I speak not at present of the rights of property' and so did not support this rule.

- `blackstone-1766-bk2-ch29` (Bk II ch 29; England; date n/a): **opened** 2026-11-04: "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage"

<a id="src-coverture_household_us__r2"></a>
**coverture_household_us__R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband is bound to provide his wife with necessaries by law, as much as himself' (long s modernised from the OCR).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "The husband is bound to provide his wife with necessaries by law, as much as himself" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

<a id="src-coverture_household_us__r3"></a>
**coverture_household_us__R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

- no work named: **unverified** (rationale: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it)

<a id="src-coverture_household_us__r4"></a>
**coverture_household_us__R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own' ... 'neither can she be sued, without making the husband a defendant' (long s modernised from the OCR; the same passage excepts a husband who 'has abjured the realm, or is banished').

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own ... neither can she be sued, without making the husband a defendant" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

<a id="src-coverture_household_us__r5"></a>
**coverture_household_us__R5**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband also (by the old law) might give his wife moderate correction' ... 'the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour' (long s modernised from the OCR). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/. The condition (misbehaves w) is set by the free action misbehave, which no rule regulates: the encoder's way to make Blackstone's condition reachable.

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-04: "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"

<a id="src-coverture_household_us__r6"></a>
**coverture_household_us__R6**: UNVERIFIED (leads, not opened 2026-11-05; network fetches blocked): Stevenson & Wolfers, 'Bargaining in the Shadow of the Law: Divorce Laws and Family Distress', Quarterly Journal of Economics 121(1) (2006), NBER w10175, on unilateral (no-fault) divorce adopted state by state from 1969; New York's 1787 divorce act (absolute divorce for adultery only, until the 1966 reform) as one state's fault statute (plans/sourcing-worklist-mwpa.md, Jurisdiction mismatch B). Reading (option B1): R6 encodes no exit at her own will. A judicial divorce on the husband's proved fault (grounds varied by state; South Carolina had none) is an exit this encoding does not represent (option B2, a later preregistered experiment, plans/sourcing.md). The English sources of coverture-household R6 (Shanley 1989, Stone 1990, on England before the Matrimonial Causes Act 1857) are not cited here. [ADR 0013: or_else null: the exit bar is a disability, not a prohibition the subject answers for. Power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married Verification pass: Stevenson & Wolfers read 2026-11-06 at https://www.nber.org/system/files/working_papers/w10175/w10175.pdf (the NBER working paper of December 2003, not the QJE version): 'from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault)' ... 'prior to unilateral divorce, a partner wishing to dissolve the marriage could leave' ... 'However, in such a situation, a legal divorce is not granted'; its Table 1 lists 'Pre-existing Unilateral Divorce statutes (predate beginning of sample in 1964)' in nine states (Alaska, Louisiana, Maryland, North Carolina, Oklahoma, Utah, Virginia, Vermont, West Virginia), so the paper does not say that no state had unilateral divorce before 1969. New York, Laws of 1787 ch. 69 (passed 30 March 1787), read 2026-11-06 through the OCR at https://archive.org/download/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787_djvu.txt: 'in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor' (long s modernised; letters clipped at line starts restored).

- `stevenson-wolfers-2006` (s. 2; Table 1; date n/a): **opened** 2026-11-06: "from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault) ... prior to unilateral divorce, a partner wishing to dissolve the marriage could leave ... However, in such a situation, a legal divorce is not granted" <https://www.nber.org/system/files/working_papers/w10175/w10175.pdf>
- `us-ny-laws-1787-divorce` (ch. 69, s. 1; US-NY; date 1787-03-30): **opened** 2026-11-06: "in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor"

<a id="src-coverture_household_us__r7"></a>
**coverture_household_us__R7**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable' ... 'all compacts made between husband and wife, when single, are voided by the intermarriage' (long s modernised; the OCR prints 'converture' in the first passage).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable ... all compacts made between husband and wife, when single, are voided by the intermarriage" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

**ssi_marriage_penalty__R1**

- no work named: **unverified** (encoder skeleton; 42 U.S.C. 1382(a) is the program statute (ssi-usc-1382a) but the grant row rests on no excerpt)

<a id="src-ssi_marriage_penalty__r2"></a>
**ssi_marriage_penalty__R2**: 20 CFR 416.1802 'Effects of marriage on eligibility and amount of benefits' (https://www.law.cornell.edu/cfr/text/20/416.1802), as carried from plans/sourcing-worklist-marriage.md section 5 (a summarising fetch, not raw text; not re-opened for this row; level snippet): 'we will count your combined income and calculated the benefit amount for you as a couple.' (the worklist's quotation, typo included) and '(d)(1) Benefits depend on whether you are married or not married at the beginning of each month.' The couple federal rate is lower than two individual rates (42 U.S.C. 1382(b)(2), not (a)(1)(B), per the faithfulness review's raw read; 1974 base rates $1,752 individual, $2,628 couple per the worklist; 2026 rates $994 / $1,491 are an unverified lead). Sanctioner none: no enforcement of the agency's duty is in the text read. Read as a power (`may`), not an applied rate; the statute is mandatory, which the encoding does not carry.

- `ssi-cfr-416-1802` (s. 416.1802(b)(1); (d)(1); US; date n/a): **snippet** 2026-11-08: "we will count your combined income and calculated the benefit amount for you as a couple. ... (d)(1) Benefits depend on whether you are married or not married at the beginning of each month." <https://www.law.cornell.edu/cfr/text/20/416.1802>
- `ssi-usc-1382a` (s. 1382(b)(2); US; date n/a): **unverified** <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-ssi_marriage_penalty__r3"></a>
**ssi_marriage_penalty__R3**: 42 U.S.C. 1382(a)(3)(A)-(B) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (first 100,000 of 170,641 characters, through a summarising fetch; not re-opened; level snippet): '$3,000 on January 1, 1989' for a couple and '$2,000 on January 1, 1989' for an individual (Pub. L. 98-369 s. 2611, not indexed to inflation; the 1.5 ratio is arithmetic). A pair of individuals may hold $4,000 together, so the couple limit is the lower of the two. Sanctioner none: no enforcement in the text read. The 2026 limits equal the 1989 figures per an unverified search-summary lead.

- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **snippet** 2026-11-08: "$3,000 on January 1, 1989 ... $2,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-ssi_marriage_penalty__r4"></a>
**ssi_marriage_penalty__R4**: 20 CFR 416.1806 (https://www.law.cornell.edu/cfr/text/20/416.1806), as carried from the worklist (a summarising fetch; not re-opened; level snippet): someone is a spouse for SSI purposes where (a)(3) 'You and an unrelated person of the opposite sex are living together in the same household' and 'you both lead people to believe that you are husband and wife.' POMS SI 00501.150 (TN 80, 02-25): 'Living together in the same household and holding themselves out as a married couple to the community in which they live.' POMS SI 00501.152 (TN 85, 12-25): 'both individuals lead people in the community in which they reside to believe they are a married couple'. POMS covers same-sex couples per a search summary; the Cornell regulation text still says opposite sex. This is the displaced gate: a conduct test that carries the couple rate to unmarried pairs. Sanctioner none (see notes): R4 is an agency `may` power with no duty to sanction, and the engine rejects a sanctioner without an or_else. Unencoded qualifiers: the regulation's `unrelated` and `at or after the time you apply`; the opposite-sex limit is deliberately not encoded (POMS). Overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule.

- `ssi-cfr-416-1806` (s. 416.1806(a)(3); US; date n/a): **snippet** 2026-11-08: "You and an unrelated person of the opposite sex are living together in the same household ... you both lead people to believe that you are husband and wife." <https://www.law.cornell.edu/cfr/text/20/416.1806>
- `ssi-poms-si-00501-150` (SI 00501.150; US; date n/a): **snippet** 2026-11-08: "Living together in the same household and holding themselves out as a married couple to the community in which they live." <https://secure.ssa.gov/poms.nsf/lnx/0500501150>
- `ssi-poms-si-00501-152` (SI 00501.152; US; date n/a): **snippet** 2026-11-08: "both individuals lead people in the community in which they reside to believe they are a married couple" <https://secure.ssa.gov/poms.nsf/lnx/0500501152>

<a id="src-ssi_marriage_penalty__r5"></a>
**ssi_marriage_penalty__R5**: CRS RL33675 (https://www.everycrsreport.com/reports/RL33675.html), as carried from the worklist (summarising fetch; not re-opened): 'a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income.' (so the unmarried are rated as individuals). 20 CFR 416.1802(d)(1) as in R2 (it does not itself state an individual rate for the unmarried). The complement condition (not married and not holding out) is the encoder's reading of the three tests in the worklist.

- `ssi-crs-rl33675` (US; date 2008-01-30): **snippet** 2026-11-08: "a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income." <https://www.everycrsreport.com/reports/RL33675.html>
- `ssi-cfr-416-1802` (s. 416.1802(d)(1); US; date n/a): **snippet** 2026-11-08: "Benefits depend on whether you are married or not married at the beginning of each month." <https://www.law.cornell.edu/cfr/text/20/416.1802>

**ssi_marriage_penalty__R6**

- `ssi-usc-1382a` (s. 1382(a)(3)(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-ssi_marriage_penalty__r7"></a>
**ssi_marriage_penalty__R7**: 42 U.S.C. 1382(a)(1)(B) and (a)(2)(B) (the bar: eligible only if resources are not more than the limit; pin from the faithfulness seat's raw read, not re-opened by the builder) and (a)(3)(A)-(B) (the limits) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (summarising fetch; not re-opened; level snippet): the resource limits '$2,000 on January 1, 1989' (individual) and '$3,000 on January 1, 1989' (couple). A disability, not a sanctioned prohibition, hence or_else null. That exceeding the limit bars payment is read from the eligibility condition in (a)(1)(B); the `must_not` form is a reading of 'eligible only if'.

- `ssi-usc-1382a` (s. 1382(a)(1)(B); (a)(2)(B); US; date n/a): **unverified** <https://www.law.cornell.edu/uscode/text/42/1382>
- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989 ... $3,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| cannot_contract | freedom | violated | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |
| married_couple_rated | freedom | holds_to_k | Whenever two people are married, the benefits agency holds the power to rate them as a couple (the couple federal rate, combined income): marriage brings the couple rate. Its holding is the SSI marriage penalty (preregistered plans/ssi-entry.md, 2026-11-08); read as a power the rules grant (derived), not as an applied rate. |
| married_couple_limited | freedom | holds_to_k | Whenever two people are married, the agency holds the power to apply the couple resource limit. Its holding is the resource half of the SSI marriage penalty (plans/ssi-entry.md). |
| penalty_reaches_unmarried | failure_mode | reachable | Some pair who are not married are rated as a couple: the penalty reaches people the marriage rule alone would not touch, through a test of conduct (holding out). Reachable when a holding-out gate exists; open when only legal marriage gates the couple rate (plans/ssi-entry.md). |
| married_rated_individually | structure | unreachable_open | Some married pair are rated as individuals: marriage does not by itself bring the couple rate. The mirror of married_couple_rated, preregistered to separate ssi-marriage-penalty from its individual-rate pair (plans/ssi-entry.md). |
| over_limit_ineligible | freedom | holds_to_k | A claimant whose countable resources exceed the applicable limit is not eligible for payment. Its holding is the resource test itself (42 U.S.C. 1382(a)(3)); the encoding reads the limit as a boolean, not a dollar amount (plans/ssi-entry.md). |

## Pairs

No pair relations.

<details><summary>Encoder notes (engine internals)</summary>

P2 composite (plans/p2-ssi-composite.md, preregistered 2026-11-08 before the build): tests the second half of claim C2 (docs/connections.md section 4). Claimant -> partner_a so that the SSI rules' (married c s) is the same atom as coverture's married(h, w) after aliasing; the claimant being the husband is an assumption of this composite, not of SSI. Sex by female(partner_b) in initial; acquired_property and earns free as in the first composite. C2b is read from `phil rules ablate --entry coverture-us-ssi`, rows ssi_marriage_penalty__R2 and R3: predicted NOT to flip financial_dependence (it reads is_subject, controls_own_property and owns_earnings, which no SSI rule touches), so C2 fails as written. Not a cluster member; no iso claims; takes no part in the gate. Post hoc (S7): cannot_contract was preregistered holds_to_k and is edited to violated after the run; violated via SSI divorce (an unsourced encoder action that un-marries a coverture pair, so R7's married condition fails). The edit follows the repo post hoc convention (docs/interpreting-results.md section 6); the baseline row already records the actual verdict. Constructed world (ADR 0018): pairs 1765 coverture with 1974+ SSI over one couple; not a historical regime.

</details>

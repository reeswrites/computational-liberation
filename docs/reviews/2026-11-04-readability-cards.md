# Card-only council review, 2026-11-04 (ADR 0014, fifth seat)

Reviewer read ONLY docs/cards/*.md, docs/decisions/0014-review-council.md, docs/glossary.md, and the web sources listed in section 3. No YAML, JSON, build.py, plans/ or other reviews were opened. Where a card did not say enough, the answer is "cannot tell", as the ADR instructs.

## 0. How verdicts were given

Per rule, two legs:

- (a) does the plain-English line say what the who / deontic / aim / when / or-else cells say;
- (b) is the rule a faithful reading of the source cell, checked against the fetched source where one was fetched.

Rubric for (b), stated so it can be argued with:

- **faithful**: the cited source was fetched and supports the rule; or the source cell gives a citation that was not fetched and the rule is a plausible reading of it; or the rule is an implicit / unverified rule whose rationale on the card is enough for a lay reader to accept it (common knowledge, or supported by the card's own quoted sources).
- **unfaithful**: (a) fails, or the fetched source does not say what the rule says (wrong section, dropped condition, broader than the text).
- **cannot tell**: the source cell is a rationale only and the claim is non-obvious; the source cell is truncated before the evidence; the sanction (or-else) is an encoder construction with nothing behind it; or the citation's applicability cannot be judged from the card.

Rules inherited unchanged by a delta entry are judged again on that entry (same verdict unless the context changes it), because the seat judges cards, not lineages. 211 rule rows were judged across 25 cards (about 120 distinct rules).

## 1. Per-rule lines

Format: entry | rule | verdict | clause.

### naming-convention
- naming-convention | R1 | faithful | plain = cells; trivially true of a two-name naming game; source unverified by the card's own admission but nothing to misread.
- naming-convention | R2 | faithful | as R1.

### airline-flight
- airline-flight | R1 | faithful | plain = cells; boarding is the obvious precondition; no source needed.
- airline-flight | R2 | unfaithful | 14 CFR 91.11 (fetched) only forbids passengers from assaulting or interfering with crew; it imposes no care duty on crew, so the pointer does not support the rule (the builder's "unverified" flag is confirmed as wrong).
- airline-flight | R3 | cannot tell | plain = cells; the cited reg grants no restraint power (that lives in 49 USC 44902 / Tokyo Convention / captain's authority, none cited), so the card gives no source to check.
- airline-flight | R4 | faithful | plain = cells; a physical fact (cannot leave an aircraft in flight) that needs no statute; the cited reg is irrelevant but harmless.
- airline-flight | R6 | faithful | plain = cells; obvious.

### companion-ownership
- companion-ownership | R1 | unfaithful | Penal Code 597s (fetched) says only that wilful abandonment is a misdemeanor; it says nothing about property status or transfer, so the citation does not support the rule (builder's doubt confirmed; a property-status source such as Civ. Code 655 or Penal Code 491 is what is missing).
- companion-ownership | R2 | faithful | plain = cells; owner-requested veterinary euthanasia is common knowledge; UNVERIFIED disclosed.
- companion-ownership | R3 | faithful | 597s(a) fetched: "Every person who willfully abandons any animal is guilty of a misdemeanor"; plain = cells incl. or-else R4.
- companion-ownership | R4 | faithful | prosecution follows from the misdemeanor; plain = cells.
- companion-ownership | R5 | faithful | 597(b) not fetched but is the failure-to-provide-sustenance section; plausible; plain = cells (must-be wording is awkward but accurate).
- companion-ownership | R6 | faithful | implicit; leash/confinement norm is common knowledge; plain = cells.
- companion-ownership | R7 | faithful | impound of animals at large is common knowledge; UNVERIFIED disclosed.
- companion-ownership | R8 | faithful | incident of ownership; common knowledge.
- companion-ownership | R9 | faithful | plain = cells; "animals are property so no court acts in the animal's interest" is common knowledge and the Alaska card itself says Alaska 2016 was the first exception; but no citation given for a gate-(f) load-bearing rule.
- companion-ownership | R10 | faithful | plain = cells; obvious; the odd condition (feed only when not already providing care) is an engine artefact the plain line reproduces honestly.
- companion-ownership | R11 | faithful | implicit; an animal cannot sue in its own name; common knowledge.

### companion-guardianship
- companion-guardianship | R1 | unfaithful | as companion-ownership R1 (597s does not state property status or transfer).
- companion-guardianship | R2 | faithful | as ownership R2.
- companion-guardianship | R3 | faithful | as ownership R3 (checked).
- companion-guardianship | R4 | faithful | as ownership R4.
- companion-guardianship | R5 | faithful | as ownership R5.
- companion-guardianship | R6 | faithful | as ownership R6.
- companion-guardianship | R7 | faithful | as ownership R7.
- companion-guardianship | R8 | faithful | as ownership R8.
- companion-guardianship | R9 (replaced) | unfaithful | Alaska Stat. 25.24.160(a)(5) (fetched) lets a divorce court assign ownership "taking into consideration the well-being of the animal"; the rule makes it a standing power at any time while owned, conditioned on "not best interest"; the notes disclose the generalisation as UNVERIFIED, but the rule as written is broader than the text on both when and standard.
- companion-guardianship | R10 | faithful | as ownership R10.
- companion-guardianship | R11 | faithful | as ownership R11.

### companion-guardian-renamed
- companion-guardian-renamed | R1 | unfaithful | R.I. Gen. Laws 4-13-41 (fetched) says only that "owner" may be interchanged with "guardian"; it grants no transfer power; the rename source is right for the role name, wrong as the source of the rule.
- companion-guardian-renamed | R2 | faithful | as ownership R2.
- companion-guardian-renamed | R3 | faithful | as ownership R3 (checked).
- companion-guardian-renamed | R4 | faithful | as ownership R4; (a) nit: the plain line says "abandoning owner" in an entry whose role is guardian.
- companion-guardian-renamed | R5 | faithful | as ownership R5.
- companion-guardian-renamed | R6 | faithful | as ownership R6.
- companion-guardian-renamed | R7 | faithful | as ownership R7.
- companion-guardian-renamed | R8 | faithful | as ownership R8.
- companion-guardian-renamed | R9 | faithful | as ownership R9; consistent with the R.I. text (words interchangeable, no new power).
- companion-guardian-renamed | R10 | faithful | as ownership R10.
- companion-guardian-renamed | R11 | faithful | as ownership R11.

### coverture-household
- coverture-household | R1 | unfaithful | Blackstone I.15 (fetched) says "I speak not at present of the rights of property"; the husband's control of the wife's property is not in the cited chapter (builder's citation doubt confirmed; the rule is true of coverture, the cite is wrong).
- coverture-household | R2 | faithful | Blackstone I.15: "The husband is bound to provide his wife with necessaries by law"; plain = cells; "no sanction attached" matches or-else none (the chapter gives liability for her debts, not a sanction on him).
- coverture-household | R3 | cannot tell | implicit; household labour as the wife's is common knowledge, but the or-else link (failure of housework -> chastisement) is the encoder's and the source cell says "not in Blackstone's text, assumed".
- coverture-household | R4 | faithful | Blackstone I.15: "she can bring no action for redress without her husband's concurrence"; disability reading (no or-else) is right.
- coverture-household | R5 | unfaithful | Blackstone I.15 calls moderate correction "the old law", says it was "confined within reasonable bounds", and permits restraint of liberty only "in case of any gross misbehaviour"; the rule drops that condition and permits chastisement whenever married; plain = cells, so the defect is in the reading.
- coverture-household | R6 | unfaithful | the cited chapter contains no exit bar (closest: an eloping wife forfeits necessaries); the disability is real in the period's divorce law but that is not what is cited.
- coverture-household | R7 | faithful | Blackstone I.15: deeds and acts done by her during coverture "are void, or at least voidable", and she cannot covenant with her husband; a fair reading of "cannot contract".

### cps
- cps | R1 | faithful | WIC 328 / PC 11165.14 cited (not fetched); reports must be investigated is a plausible reading; plain = cells.
- cps | R2 | faithful | WIC 16501 family-maintenance services cited; plausible; plain = cells.
- cps | R3 | faithful | WIC 306(a)(2) (fetched): custody without warrant when the child "is in immediate danger of physical or sexual abuse" etc.; plain = cells.
- cps | R4 | faithful | WIC 306(f) (fetched): "Before taking a child into custody, a social worker shall consider whether the child may remain safely in their residence"; plain = cells (must-be wording awkward but accurate).
- cps | R5 | cannot tell | implicit; "non-cooperation feeds the removal decision" is a non-obvious causal practice claim with a rationale only.
- cps | R6 | cannot tell | implicit; source cell is cut off at "(plan: 'the..." so the evidence for "mother called first" is not on the card.
- cps | R7 | unfaithful | WIC 361 (fetched) removes a child only on clear and convincing evidence of substantial danger with no reasonable means of protection; "best interest" appears only for educational decisions; the rule's "not best_interest" condition is not the statute's standard (builder's doubt confirmed).
- cps | R8 | faithful | WIC 317 counsel for the child; plausible (317(c) has an exception the rule omits); plain = cells.
- cps | R10 | faithful | WIC 306 "take into and maintain temporary custody"; maintained custody implies no exit; plain = cells.
- cps | R11 | cannot tell | 317(e) is about appointed counsel's duties; the card does not say which petition a child brings "in its own name", so the aim cannot be matched to the cite.

### crisis-team
- crisis-team | R1 | faithful | KUNC 2020 (not fetched) describes dispatch of the team to eligible low-level calls; "must" is the encoder's strengthening of a described practice; plain = cells.
- crisis-team | R2 | faithful | clinician + paramedic respond; plausible; plain = cells.
- crisis-team | R3 | faithful | the article's medication / housing example is quoted on the card; plain = cells.
- crisis-team | R4 | faithful | "unarmed, no custody power" is the article's description; disability reading is right; plain = cells.
- crisis-team | R5 | faithful | voluntary encounter; plausible; plain = cells.
- crisis-team | R6 | faithful | "described as unarmed"; plain = cells.
- crisis-team | R7 | faithful | implicit; a team calling police when a scene turns violent is common knowledge and the rationale says so; plain = cells.
- crisis-team | R8 | faithful | WIC 5150(a) (fetched) gives a peace officer the custody power; note the condition drops in_crisis / mental-disorder that police-crisis R3 keeps for the same section; plain = cells.
- crisis-team | R9 | faithful | adult capacity to sue; common knowledge; plain = cells.

### ectogenesis
- ectogenesis | R1 | faithful | instantiates Firestone's demand (unverified, from memory, disclosed); plain = cells.
- ectogenesis | R2 | faithful | as R1.
- ectogenesis | R3 | cannot tell | the registry sanction for failing to decant is an encoder construction with nothing behind it; Firestone gives no institution.
- ectogenesis | R4 | faithful | plain = cells; "born subject" reads correctly given the role line "is_subject is set only by a birth action"; construction disclosed.
- ectogenesis | R5 | cannot tell | the mother-must-care norm is common knowledge, but a registry that reprimands a non-caring mother is invented; "born subject" wording is fine.
- ectogenesis | R6 | cannot tell | invented sanctioner; condition true.
- ectogenesis | R7 | cannot tell | ASSUMED on the card; no source; the "no birth condition" is the entry's hypothesis, not a reading.

### footbinding
- footbinding | R1 | faithful | Mackie 1996 (abstract quoted on card; secondary sources fetched); plain = cells.
- footbinding | R2 | faithful | implicit; physically open to the family; obvious.
- footbinding | R3 | faithful | Mackie's marriage-market sanction (secondary sources fetched: the practice persisted because an unbound daughter was unmarriageable); sanctioned-norm reading is right; plain = cells.
- footbinding | R4 | faithful | pledge associations confirmed by fetched secondary sources (parents pledged not to bind daughters); plain = cells.
- footbinding | R10 | faithful | the sons' half (not to let sons marry bound women) confirmed by fetched secondary sources; the card assigns it to the suitor role, which is the groom's family; plain = cells. Builder flagged; holds.
- footbinding | R5 | faithful | the market's refusal lapses for pledged families; matches Mackie's mechanism; plain = cells (long condition rendered correctly).
- footbinding | R6 | faithful | plain = cells; the convention from the groom's side.
- footbinding | R7 | faithful | plain = cells; marriage condition.
- footbinding | R9 | faithful | implicit; bound in childhood, no say; common knowledge; plain = cells.

### footbinding-no-pledge
- footbinding-no-pledge | R1 | faithful | as footbinding R1.
- footbinding-no-pledge | R2 | faithful | as footbinding R2.
- footbinding-no-pledge | R3 | faithful | as footbinding R3.
- footbinding-no-pledge | R5 | faithful | as footbinding R5; the (not pledged) conjuncts are inert here, which the diff explains.
- footbinding-no-pledge | R6 | faithful | as footbinding R6.
- footbinding-no-pledge | R7 | faithful | as footbinding R7.
- footbinding-no-pledge | R9 | faithful | as footbinding R9.

### gestational-surrogacy
- gestational-surrogacy | R2 (replaced) | cannot tell | "Statute citations still to be added"; no source; plain = cells.
- gestational-surrogacy | R3 (replaced) | cannot tell | no source; and "gestator must give birth or else the registry reprimands" is doubtful on its face (no surrogacy regime sanctions a surrogate for not carrying to term), so a lay reader cannot accept it unsourced.
- gestational-surrogacy | R4 | faithful | as ectogenesis R4.
- gestational-surrogacy | R5 | cannot tell | as ectogenesis R5.
- gestational-surrogacy | R6 | cannot tell | as ectogenesis R6.
- gestational-surrogacy | R7 | cannot tell | as ectogenesis R7.

### kibbutz-childrens-house
- kibbutz-childrens-house | R1 | faithful | Wikipedia (cited, not fetched): committee staffs the house; plausible; plain = cells.
- kibbutz-childrens-house | R2 | cannot tell | the practice ("the nanny position was always a woman's role") is supported by the card's own quote; the or-else (committee reprimanded for assigning a man) is unsourced, and that sanction is what makes it a sanctioned norm rather than a disability.
- kibbutz-childrens-house | R3 | faithful | metapelet care duty supported by the quote; plain = cells; or-else R6 unsourced but the duty is.
- kibbutz-childrens-house | R4 | faithful | "communal sleeping arrangements" quoted; disability reading is right; plain = cells.
- kibbutz-childrens-house | R5 | faithful | "visited their parents for 2-3 hours a day" quoted; the rule reverses direction (member visits child) but plain = cells; acceptable.
- kibbutz-childrens-house | R6 | cannot tell | implicit sanctioner with rationale only; the builder's own flag; nothing on the card says the committee reprimands anyone.
- kibbutz-childrens-house | R8 | cannot tell | the source cell says it exists for an engine rule (ADR 0015 A6); it describes no practice, so there is nothing to be faithful to.

### kibbutz-childrens-house-no-implicit
- kibbutz-childrens-house-no-implicit | R1 | faithful | as kibbutz R1.
- kibbutz-childrens-house-no-implicit | R3 | faithful | as kibbutz R3.
- kibbutz-childrens-house-no-implicit | R4 | faithful | as kibbutz R4.
- kibbutz-childrens-house-no-implicit | R5 | faithful | as kibbutz R5.
- kibbutz-childrens-house-no-implicit | R6 | unfaithful | (a) fails: the plain line says "the sanction for R3 and R2" but this entry drops R2; stale text on a generated card.
- kibbutz-childrens-house-no-implicit | R8 | cannot tell | as kibbutz R8.

### lease
- lease | R1 | faithful | obvious; UNVERIFIED disclosed.
- lease | R2 | faithful | Civ. Code 1941 quoted on the card; plain = cells.
- lease | R3 | faithful | CCP 1161(2) unlawful detainer for non-payment (not fetched, plausible); plain = cells.
- lease | R4 | faithful | Civ. Code 1946 notice to terminate (not fetched, plausible); plain = cells.
- lease | R5 | faithful | plain = cells incl. or-else R3; same source as R3.

### public-library
- public-library | R1 | faithful | obvious.
- public-library | R2 | faithful | the policy's "welcoming and safe environment for all patrons" is quoted; the card itself marks the serve duty as inferred; a lay reader accepts that a public library serves patrons; plain = cells.
- public-library | R3 | faithful | the suspension policy is quoted; plain = cells.
- public-library | R4 | faithful | obvious.
- public-library | R5 | faithful | plain = cells; follows from the policy.
- public-library | R6 | faithful | obvious.

### paternity-quota
- paternity-quota | R1 | faithful | s. 9 quoted on the card ("maximum number of weeks of paternity benefits ... for the non-birthing parent is five"); plain = cells.
- paternity-quota | R2 | faithful | non-transferability confirmed by secondary sources fetched ("The 5 paternity weeks are non-transferable"); plain = cells. Note: the or-else (forfeiture) is the use-it-or-lose-it consequence, not a sanction for transferring, and by the card's own ADR 0013 convention an absent power would be a disability, not a sanctioned must-not; flagged, not failed.
- paternity-quota | R3 | faithful | benefit period ending forfeits untaken weeks; the section that sets the window is not cited on the card (s. 23 by my recollection); plausible; plain = cells.
- paternity-quota | R4 | faithful | s. 10 / 16 quoted; plain = cells.
- paternity-quota | R5 | faithful | s. 16 quoted ("may be taken by either parent"); plain = cells.
- paternity-quota | R6 | faithful | s. 16 "shared between the parents"; plain = cells.
- paternity-quota | R7 | cannot tell | implicit "must"; the source cell is cut at "(the patter..." so the evidence for the default is not on the card, and a statistical pattern encoded as must with no or-else is a stretch a lay reader cannot judge.
- paternity-quota | R8 | faithful | s. 9; plain = cells.
- paternity-quota | R9 | faithful | plain = cells; disclosed as scaffolding for the pair (inert here because R8 never grants reserved weeks to the birthing parent); nothing to misread.

### transferable-leave
- transferable-leave | R1 | faithful | as paternity-quota R1.
- transferable-leave | R2 (replaced) | faithful | labelled construction; the diff states it; plain = cells.
- transferable-leave | R3 | faithful | as quota R3 (kept so the pair is one rule apart; notes say so).
- transferable-leave | R4 | faithful | as quota R4.
- transferable-leave | R5 | faithful | as quota R5.
- transferable-leave | R6 | faithful | as quota R6.
- transferable-leave | R7 | cannot tell | as quota R7.
- transferable-leave | R8 | faithful | as quota R8.
- transferable-leave | R9 | faithful | as quota R9; here it is the rule that lets the transferred weeks be taken, which the notes explain.

### police-crisis
- police-crisis | R1 | faithful | implicit; police as default crisis responder is common knowledge and is the contrast the crisis-team card is built on; plain = cells.
- police-crisis | R2 | faithful | 5150 (fetched): assessment "shall be conducted and provided on an ongoing basis" and (c) the officer "shall assess the person to determine whether the person can be properly served without being detained"; plain = cells.
- police-crisis | R3 | faithful | 5150(a) (fetched): danger to self/others or gravely disabled, upon probable cause, up to 72 hours; "danger" stands in for the three criteria; plain = cells.
- police-crisis | R4 | faithful | involuntary 72-hour custody implies no exit; plain = cells.
- police-crisis | R5 | faithful | use of force incident to lawful custody is common knowledge; UNVERIFIED disclosed; plain = cells.
- police-crisis | R6 | faithful | officers are armed; common knowledge.
- police-crisis | R7 | unfaithful | 5150 (fetched) contains no release duty; 5152 (fetched) places early release with the facility psychiatrist, not the officer; the rule's who (officer) and source (5150) are both wrong even if a release duty exists somewhere.
- police-crisis | R8 | cannot tell | WIC 5275 is the certification-review / habeas provision for persons certified for intensive treatment (the 14-day hold); whether it reaches a 72-hour detainee cannot be judged from the card, which marks it UNVERIFIED.
- police-crisis | R10 | faithful | adult capacity to sue; common knowledge.

### mwpa-creditor-exemption
- mwpa-creditor-exemption | R1 | unfaithful | as coverture R1 (Blackstone I.15 does not cover property).
- mwpa-creditor-exemption | R2 | faithful | as coverture R2.
- mwpa-creditor-exemption | R3 | cannot tell | as coverture R3.
- mwpa-creditor-exemption | R4 | faithful | as coverture R4.
- mwpa-creditor-exemption | R5 | unfaithful | as coverture R5.
- mwpa-creditor-exemption | R6 | unfaithful | as coverture R6.
- mwpa-creditor-exemption | R7 | faithful | as coverture R7.
- mwpa-creditor-exemption | R10 (added) | faithful | implicit baseline (husband's creditors reach what he holds) is common law common knowledge and is the premise of the Chused quote; plain = cells.
- mwpa-creditor-exemption | R11 (added) | faithful | Chused 1984 quoted on the card: acts "exempting married women's property from the debts of husbands"; disability reading is right; plain = cells.
- mwpa-creditor-exemption | R12 (added) | faithful | implicit conveyance vehicle; Chused is cited for the capture; plain = cells.

### mwpa-property
- mwpa-property | R2 | faithful | as coverture R2.
- mwpa-property | R3 | cannot tell | as coverture R3.
- mwpa-property | R4 | faithful | as coverture R4.
- mwpa-property | R5 | unfaithful | as coverture R5.
- mwpa-property | R6 | unfaithful | as coverture R6.
- mwpa-property | R7 | faithful | as coverture R7.
- mwpa-property | R10 | faithful | as creditor-exemption R10.
- mwpa-property | R11 | faithful | as creditor-exemption R11.
- mwpa-property | R12 | faithful | as creditor-exemption R12.
- mwpa-property | R13 (added) | faithful | NY 1848 act via Geddes et al. (not fetched); the card's gloss (property by gift or inheritance held in her own right) is the standard reading; the (not narrowed) conjunct is scaffolding for the narrowed branch, disclosed there; plain = cells.

### mwpa-earnings
- mwpa-earnings | R2 | faithful | as coverture R2.
- mwpa-earnings | R3 | cannot tell | as coverture R3.
- mwpa-earnings | R4 | faithful | as coverture R4.
- mwpa-earnings | R5 | unfaithful | as coverture R5.
- mwpa-earnings | R6 | unfaithful | as coverture R6.
- mwpa-earnings | R7 | faithful | as coverture R7.
- mwpa-earnings | R10 | faithful | as creditor-exemption R10.
- mwpa-earnings | R11 | faithful | as creditor-exemption R11.
- mwpa-earnings | R12 | faithful | as creditor-exemption R12.
- mwpa-earnings | R13 | faithful | as mwpa-property R13.
- mwpa-earnings | R14 (added) | faithful | earnings acts per Geddes Table 1 (not fetched) and Khan 1996 (fetched: "to keep the earnings from their labor (earnings laws)"); plain = cells.

### mwpa-sole-trader
- mwpa-sole-trader | R2 | faithful | as coverture R2.
- mwpa-sole-trader | R3 | cannot tell | as coverture R3.
- mwpa-sole-trader | R4 | faithful | as coverture R4.
- mwpa-sole-trader | R5 | unfaithful | as coverture R5.
- mwpa-sole-trader | R6 | unfaithful | as coverture R6.
- mwpa-sole-trader | R10 | faithful | as creditor-exemption R10.
- mwpa-sole-trader | R11 | faithful | as creditor-exemption R11.
- mwpa-sole-trader | R12 | faithful | as creditor-exemption R12.
- mwpa-sole-trader | R13 | faithful | as mwpa-property R13.
- mwpa-sole-trader | R14 | faithful | as mwpa-earnings R14.
- mwpa-sole-trader | R15 (added) | faithful | Khan 1996 (fetched): sole trader laws let married women "trade, write contracts or engage in businesses on their own account"; the rule's unconditional "at any time" is Khan's general gloss, though Khan also notes narrower acts (Georgia 1873 declared wives' general contracts void); plain = cells.

### mwpa-suit
- mwpa-suit | R2 | faithful | as coverture R2.
- mwpa-suit | R3 | cannot tell | as coverture R3.
- mwpa-suit | R5 | unfaithful | as coverture R5.
- mwpa-suit | R6 | unfaithful | as coverture R6.
- mwpa-suit | R10 | faithful | as creditor-exemption R10.
- mwpa-suit | R11 | faithful | as creditor-exemption R11.
- mwpa-suit | R12 | faithful | as creditor-exemption R12.
- mwpa-suit | R13 | faithful | as mwpa-property R13.
- mwpa-suit | R14 | faithful | as mwpa-earnings R14.
- mwpa-suit | R15 | faithful | as mwpa-sole-trader R15.
- mwpa-suit | R16 (added) | cannot tell | the source cell cites Geddes Table 1 "dates of property / earnings acts", which as described on the card does not cover suit provisions; the quote block says "Statute texts not opened"; nothing on the card locates a suit act.

### mwpa-property-narrowed
- mwpa-property-narrowed | R2 | faithful | as coverture R2.
- mwpa-property-narrowed | R3 | cannot tell | as coverture R3.
- mwpa-property-narrowed | R4 | faithful | as coverture R4.
- mwpa-property-narrowed | R5 | unfaithful | as coverture R5.
- mwpa-property-narrowed | R6 | unfaithful | as coverture R6.
- mwpa-property-narrowed | R7 | faithful | as coverture R7.
- mwpa-property-narrowed | R10 | faithful | as creditor-exemption R10.
- mwpa-property-narrowed | R11 | faithful | as creditor-exemption R11.
- mwpa-property-narrowed | R12 | faithful | as creditor-exemption R12.
- mwpa-property-narrowed | R13 | faithful | as mwpa-property R13.
- mwpa-property-narrowed | R17 (added) | faithful | Chused 1984 quoted on the card ("narrowly construing" the acts); plain = cells.
- mwpa-property-narrowed | R18 (added) | faithful | Chused: narrow construction "to keep husbands' control during marriage"; R1 reinstated under narrowed; plain = cells.

## 2. Per-entry verdicts

Rule: an entry is **unfaithful** if any rule is unfaithful; **cannot tell** if none is unfaithful but at least one is cannot tell; **faithful** only if every rule is faithful.

| entry | rules | faithful | unfaithful | cannot tell | entry verdict |
|---|---|---|---|---|---|
| naming-convention | 2 | 2 | 0 | 0 | faithful |
| airline-flight | 5 | 3 | 1 | 1 | unfaithful (R2 pointer wrong) |
| companion-ownership | 11 | 10 | 1 | 0 | unfaithful (R1 cite) |
| companion-guardianship | 11 | 9 | 2 | 0 | unfaithful (R1 cite, R9 broader than Alaska text) |
| companion-guardian-renamed | 11 | 10 | 1 | 0 | unfaithful (R1 cite) |
| coverture-household | 7 | 3 | 3 | 1 | unfaithful (R1, R5, R6 vs Blackstone I.15) |
| cps | 10 | 6 | 1 | 3 | unfaithful (R7 vs WIC 361) |
| crisis-team | 9 | 9 | 0 | 0 | faithful |
| ectogenesis | 7 | 3 | 0 | 4 | cannot tell |
| footbinding | 9 | 9 | 0 | 0 | faithful |
| footbinding-no-pledge | 7 | 7 | 0 | 0 | faithful |
| gestational-surrogacy | 6 | 1 | 0 | 5 | cannot tell |
| kibbutz-childrens-house | 7 | 4 | 0 | 3 | cannot tell |
| kibbutz-childrens-house-no-implicit | 6 | 4 | 1 | 1 | unfaithful (R6 plain line stale) |
| lease | 5 | 5 | 0 | 0 | faithful |
| public-library | 6 | 6 | 0 | 0 | faithful |
| paternity-quota | 9 | 8 | 0 | 1 | cannot tell |
| transferable-leave | 9 | 8 | 0 | 1 | cannot tell |
| police-crisis | 9 | 7 | 1 | 1 | unfaithful (R7 release duty not in 5150, not the officer's) |
| mwpa-creditor-exemption | 10 | 6 | 3 | 1 | unfaithful (inherited coverture R1, R5, R6) |
| mwpa-property | 10 | 7 | 2 | 1 | unfaithful (inherited R5, R6) |
| mwpa-earnings | 11 | 8 | 2 | 1 | unfaithful (inherited R5, R6) |
| mwpa-sole-trader | 11 | 8 | 2 | 1 | unfaithful (inherited R5, R6) |
| mwpa-suit | 11 | 7 | 2 | 2 | unfaithful (inherited R5, R6; R16 unsourced) |
| mwpa-property-narrowed | 12 | 9 | 2 | 1 | unfaithful (inherited R5, R6) |
| **total** | **211** | **159** | **24** | **28** | 7 faithful / 13 unfaithful / 5 cannot tell |

Note on the MWPA chain: seven of its unfaithful rows are the same three coverture rules copied six times; fixing coverture R1 (cite), R5 (condition) and R6 (cite) clears every MWPA entry except mwpa-suit (R16).

Builder's flagged lines, specifically:
- kibbutz-childrens-house R6: cannot tell. Nothing on the card says the committee reprimands anyone; the quotes support the practice (women only), not a sanction. The builder's unease is warranted.
- cps R7: unfaithful. WIC 361 is a substantial-danger / clear-and-convincing removal standard; "best interest" is not the test. The rule is the companion-guardianship analogue projected onto cps, not a reading of 361.
- footbinding R10: faithful. Secondary sources confirm the pledge had two halves (daughters unbound; sons not to marry bound women); placing the second half on the suitor role is a fair encoding.
- ectogenesis R4/R5 "born subject": faithful on (a). The phrase is odd but the role line defines it; R5's sanction is what fails, not the wording.
- airline-flight R2: unfaithful. 14 CFR 91.11 is a prohibition on passengers interfering with crew; it says nothing about crew care. The whole entry's source cell is "no statute opened", so the card is honest, but the pointer is wrong.
- coverture R1/R2 "Blackstone I.15": R1 miscited (the chapter expressly sets property aside); R2 correctly cited (necessaries).
- companion R1/R3 "Cal. Penal Code 597s": R3 correctly cited; R1 miscited (597s is abandonment only; no property-status source is on any companion card).

## 3. Source fetches

| what | URL | what it said | match |
|---|---|---|---|
| Blackstone, Commentaries I ch. 15 | https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp | one person in law; husband cannot grant to or covenant with wife; wife "can bring no action for redress without her husband's concurrence"; her deeds and acts during coverture void or voidable; husband "bound to provide his wife with necessaries"; "by the old law" moderate correction, "confined within reasonable bounds", courts "will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"; "I speak not at present of the rights of property"; no exit bar beyond elopement forfeiting necessaries | R2, R4, R7 match; R1 not in chapter; R5 broader than text; R6 not in chapter |
| Cal. WIC 5150 | https://california.public.law/codes/ca_welf_and_inst_code_section_5150 | peace officer / mobile crisis team may, on probable cause, take a person who is a danger to self/others or gravely disabled into custody up to 72 hours; shall assess whether the person can be served without detention; assessment on an ongoing basis; no release duty, no force or weapon language | R2, R3, R4 match; R7 not in section |
| Cal. WIC 5152 | https://california.public.law/codes/ca_welf_and_inst_code_section_5152 | early release from a 72-hour hold is decided by the facility psychiatrist (or psychologist in a collaborative relationship); not a peace officer | R7's who is wrong |
| Cal. WIC 361 | https://california.public.law/codes/ca_welf_and_inst_code_section_361 | removal only on clear and convincing evidence of substantial danger (or the other listed grounds) and no reasonable means short of removal; "best interest" only in (a) for educational decisions | R7 mismatch |
| Cal. WIC 306 | https://california.public.law/codes/ca_welf_and_inst_code_section_306 | (a)(2) temporary custody without warrant on reasonable cause of immediate need for medical care or immediate danger of physical/sexual abuse; (f) before taking custody, shall consider whether the child may remain safely at home | R3, R4, R10 match |
| Cal. Penal Code 597s | https://codes.findlaw.com/ca/penal-code/pen-sect-597s/ (justia and leginfo returned 403) | (a) wilful abandonment of any animal is a misdemeanor; (b) wildlife-release exception; nothing on property, sale, transfer or euthanasia | R3, R4 match; R1 not supported |
| R.I. Gen. Laws 4-13-41 | https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm | "owner" may be interchanged with "guardian" throughout the chapter; P.L. 2001 ch. 72 s. 3 | rename matches; renamed R1 not supported as a grant |
| Alaska Stat. 25.24.160(a)(5) | https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment | in a divorce judgment the court may provide "for the ownership or joint ownership of the animal, taking into consideration the well-being of the animal"; "best interest" not used | guardianship R9 broader than text (any time, best-interest standard) |
| Khan 1996, JEH 56(2) (PDF) | https://www.laits.utexas.edu/~mbs31415/Khan_MarriedWomenPropertyRights.pdf | coverture: wives "prohibited from entering into contracts without the consent of their husbands and from engaging in trade on their own account, as 'sole traders'"; sole trader laws let married women "trade, write contracts or engage in businesses on their own account"; earnings laws "keep the earnings from their labor"; Table 1 columns Property / Earnings / Sole Trader laws by state; Georgia 1873 "general contracts of married women were void"; S.C. 1744 sole-trader act gave the right to sue and be sued | R15 matches Khan's gloss (with the narrow-act caveat); R14 matches |
| Quebec Act respecting parental insurance, A-29.011 | https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 and canlii mirror | both returned 403; not read | s. 9 / 10 / 16 text as quoted on the card is consistent with every secondary source found |
| QPIP secondary | https://commoner-law.com/canada/workers-rights/parental-leave/quebec ; web search results incl. a 2017 Springer chapter and the Quebec parents' federation guide | "The 5 paternity weeks are non-transferable" and "reserved for the second parent and cannot be transferred to the birth mother"; parental benefits "shareable between parents: up to 32 weeks"; benefit window not stated (a 2018 bill proposed extending it from 52 to 104 weeks) | R1, R2, R4-R6, R8 match; R3's window section not located |
| Mackie 1996 (secondary) | https://today.ucsd.edu/story/it_takes_a_village_or_10_collective_action_stops_harmful_social_practice ; web search (Wikipedia Orchid Project; Mackie 2000 chapter excerpts) | "associations of parents publicly pledging not to bind their daughters' feet" and "to not let their sons marry foot-bound women", the "pivotal innovation"; footbinding tied to marriageability; "lasted for a 1,000 years but ended in a single generation" | R1, R3, R4, R10, R5-R7 match; the full ASR article (JSTOR) was not opened |
| 14 CFR 91.11 | https://www.law.cornell.edu/cfr/text/14/91.11 (ecfr redirected to an unblock page) | "No person may assault, threaten, intimidate, or interfere with a crewmember in the performance of the crewmember's duties aboard an aircraft being operated"; no care duty, no restraint power, no exit bar | airline R2 pointer wrong; R3, R4 unsupported by the cite |

Not opened: Chused 1984 (core.ac.uk PDF), Geddes et al. 2007 (PDF), KUNC 2020 article, Wikipedia kibbutz page, Kirkus review, Berkeley patron policy PDF, Cal. Civ. Code 1941/1946, CCP 1161, WIC 16501/317/328/5275, Penal Code 597(b), canada.ca EI page, Centola 2018, Firestone 1970. Verdicts for rules citing those are "plausible, not fetched" as the rubric says.

## 4. Answers from the cards alone

### (1) Default capacity

Partly. Every card carries a line "Default capacities (enabled unless an express disability bars them): ..." so I can list which actions have one per card: leave (airline, companion x3, cps, crisis-team, police, public-library, coverture and all six MWPA), sue and contract (coverture, MWPA chain; sue also crisis-team, police), refuse_binding (footbinding pair), sleep_home (kibbutz pair); none for naming-convention, ectogenesis, surrogacy, paternity pair, lease.

What a default capacity *is* I had to reconstruct from notes on three cards (mwpa-suit: "sue is a default capacity ... deleting the R4 disability alone restores it"; kibbutz: "sleep_home is a default capacity ... so can_exit is carried by the capacity unless R4 bars it"; naming-convention: "ADR 0015 A6 strict enabledness: every action needs a may"). From those I infer: ordinarily an action with no may-rule is disabled; a default capacity is an action that is enabled with no may-rule unless a disability rule names it. Neither the card header nor the glossary says this; the glossary has no entry for it. Two things I still cannot tell: (i) why crisis-team and public-library list leave / sue as default capacities AND carry explicit may-rules for them (R5, R9; R4), so whether the capacity adds anything there; (ii) why lease's vacate is not a default capacity when leave is everywhere else, and whether that asymmetry affects the negative-control reading.

### (2) Delta entries

| delta entry | diff enough to see what changed? | enough to see why it matters? |
|---|---|---|
| companion-guardianship | yes (R9 was/now, one line) | yes: "differs on" is not stated but the Notes say no_standing flips |
| companion-guardian-renamed | not a delta (no Extends block); the Notes say it is rule-for-rule identical under owner->guardian; a diff line would have made that checkable | n/a |
| footbinding-no-pledge | yes (R4, R10 dropped; two actions dropped) | yes: "no layer-1 property separates the pair" is stated |
| kibbutz-childrens-house-no-implicit | yes (R2 dropped) | yes: "differs on care_assigned_by_sex" |
| gestational-surrogacy | yes but long: R1 dropped, R2/R3 replaced, role, fluents, actions; "fluents changed: birthing_parent" is opaque (changed how?) | yes: "differs on birth_labor_rival" |
| transferable-leave | yes (R2 was/now) | yes: "differs on leave_reserved_for_non_birthing_parent" |
| mwpa-creditor-exemption | rules yes (R10-R12 added); the line "fluents changed: is_subject, female, can_sanction, can_exit, has_standing, married, ..." (12 names) means nothing to a non-coder and suggests more changed than three rules | yes: "differs on creditor_shield" |
| mwpa-property | yes (R1 dropped, R13 added) | yes: financial_dependence |
| mwpa-earnings | yes (R14 added) | yes: financial_dependence_unpropertied |
| mwpa-sole-trader | yes (R7 -> R15) | yes: cannot_contract |
| mwpa-suit | yes (R4 -> R16) | yes: no_standing |
| mwpa-property-narrowed | yes (R17, R18 added, court role) | yes: backlash |

The "fields overridden: expected_properties, isomorphic_to, ..." line on every delta is noise for this seat. The "differs on property X" line is what carries the "why", and it works where present; companion-guardianship lacks it.

### (3) What is missing from the cards that I needed

1. Untruncated source cells. Every source cell is cut at about 80 characters with "..."; the evidence for cps R6 ("plan: 'the..."), paternity R7 ("the patter..."), companion R8 ("[ADR 00..."), kibbutz R2 ("third review...") is cut off before it says anything. This is the single largest cause of "cannot tell".
2. A pin cite per rule (section + the phrase relied on), not a chapter or an article. "Blackstone I.15" covers seven rules and is wrong for two of them; "Cal. WIC 5150" covers four and is wrong for one.
3. A definition of default capacity on the card or in the glossary (see (1)).
4. A one-line legend for the deontic column: what "must not (disability)" means versus "must not" with an or-else, what "(implicit)" with or-else none means, and why a must-be aim reads "X must hold" in the plain line. I inferred these from Notes on three cards.
5. The expected-properties "meaning" column is truncated at ~110 characters, so no property can be read in full from a card; property verdicts were therefore outside what I could judge.
6. Which rule variables bind to what: `x` in `(reprimand committee x)`, `o2` in transfer, `q` in transfer_shareable, `w` in mwpa R11 (the creditor's target). The plain lines paper over this; the formal cells are unreadable without it.
7. A property-status source for the companion entries (nothing on any companion card cites a text saying animals are property; 597s does not).
8. For cps R7 and police R7, the section that actually carries the rule (361(c) standard; 5152 release), and for paternity R3 the section that sets the benefit window.
9. The Notes are walls of engine state (check-all counts, seeds, matcher internals, ABM adoption splits). For this seat the only useful Notes content is the "Pitfalls" and "Rival reading" sentences; they are buried.
10. For companion-guardian-renamed, a diff block like the deltas have, so the "rule-for-rule identical" claim can be checked by eye.
11. For rules copied across a chain (coverture R1-R7 into six MWPA entries), a marker on the card saying "inherited, judged on coverture-household", so a reviewer is not asked to re-judge the same rule seven times.

## 5. Verdict

**Verdict: partly legible.** 28 of 211 rule rows (13%) are "cannot tell"; 24 (11%) are unfaithful, of which 13 are three coverture rules repeated through the MWPA chain and the rest are concentrated in miscited sources (597s, 4-13-41, WIC 361, 5150 release, 14 CFR 91.11, Alaska 25.24.160) and in invented sanctioners (ectogenesis / surrogacy registry, kibbutz committee). The plain-English lines almost always say what the cells say (one stale line, kibbutz-no-implicit R6); the failures are in what is cited, not in how it is rendered.

Counts: faithful 159 / unfaithful 24 / cannot tell 28 (rule rows); entries: faithful 7 / unfaithful 13 / cannot tell 5.

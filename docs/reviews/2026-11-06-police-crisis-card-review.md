# Card-only council seat: police-crisis after the WIC 5150 re-encode, 2026-11-06 (ADR 0014, fifth seat)

Reviewer (fresh agent) read only docs/cards/police-crisis.md (as of 629867b), ADR 0014, docs/glossary.md, section 0 of 2026-11-04-readability-cards.md (rubric) and the fetched sources: WIC 5150, 5152, 5275 from california.public.law (no blocks). No YAML, JSON, code, plans or other reviews. Same two legs per rule: (a) plain line = cells; (b) faithful to the source.

## Per rule

- police-crisis | R1 | faithful | unwritten dispatch practice, honestly labelled; `d`, `o` unbound to roles.
- police-crisis | R2 | faithful, legibility flag | facility care fits 5150(a)'s passive "shall be conducted and provided" and 5150(c); plain line read like a power; 5152(a) ("whatever treatment and care ... for the full period that they are held") is the stronger source and was not cited.
- police-crisis | R3 | faithful | narrower than 5150(a) (drops "gravely disabled", "probable cause"; adds `responding`); grants nothing the text does not.
- police-crisis | R4 | faithful | custody up to 72 hours means no permitted exit; the cap is not on the card.
- police-crisis | R5 | faithful (lay-accepted) | force on resistance is real practice, but no reasonableness limit; uncited.
- police-crisis | R6 | faithful | common knowledge.
- police-crisis | R7 | **unfaithful** | 5152(a) says release before 72 hours "only if" the treating psychiatrist believes the person "no longer requires evaluation or treatment"; the rule makes it a duty triggered by "no danger" and drops 5152(b)'s referral and certification outcomes; `f` unbound.
- police-crisis | R8 | faithful, flag | 5275 gives "every person detained under this part" habeas; its procedure runs through the certification notice and intensive-treatment staff; reach to a bare 72-hour hold not shown on the card.
- police-crisis | R10 | faithful | lay-accepted; `s` unbound.
- police-crisis | R11 | faithful | 5150(a) gives the "professional person in charge of a facility" and "attending staff" the same custody power as officers; stray ":" at the end of the URL in the cell.

## (c) Care versus power

Clear on the card and a fair reading of 5150(a) (officers and facility staff hold the same custody power) and 5150(c) (the facility assesses). Gaps: R2 binds whenever `in_custody`, including before delivery (cannot tell whether the facility owes care then); only the officer holds force (cannot tell whether the facility's hold carries restraint); mobile crisis teams and county-designated professionals omitted (acknowledged in notes).

## (d) Contradictions on the card

1. Notes opened "The same role (officer) is bound to care (R2, assess)".
2. R2 sources still carry "dispatch establishes provides_care(o, s)" (marked superseded).
3. R8 sources: "UNVERIFIED (general knowledge; no source opened)" then "opened".
4. R7 level "recalled" from a leftover 5150 item though 5152 is opened with a quote.
5. R2 sources said the 5150 page shows "updated Jan. 1, 2024"; the page says 2023 (2024 is 5275's).
6. Goods section: "R4 reads tying" vs R4's strand cell rival.
7. Pairs: the cps pair is shown as a rename (social_worker->officer, court->facility) and "isomorphic", but the per-rule maps differ (R2 social_worker->facility, ...) and every rule "differs beyond the rename".
8. Notes pitfall (2) relies on "or_else on R4", which ADR 0013 set to null.
9. The source quote at the top cuts out the facility-staff holders R11 rests on.
10. subject_cannot_exit's scope (interaction) is in the notes, not in the expected table.

## Verdict (seat)

9 of 10 rules faithful, R7 unfaithful. The re-encode is sound on who cares and who controls; the card still carries officer-as-carer text a card-only reader meets first.

## Response (2026-11-06, same session)

Acted on (prose and provenance only; 0 verdict changes, gate PASS, 32 passed):
- R2 plain -> "The facility must keep providing care to the subject while the subject is in custody (Cal. WIC 5150(a), (c); 5152(a))"; WIC 5152(a) added as an opened item (with the note that 5152 covers an admitted person, so the pre-delivery window is not covered by it).
- (d)5: the 5150 date corrected to 2023 in R2's source sentence and in the provenance notes of R2, R3, R4, R11 (my error, copied from the 5275 page).
- (d)1: the notes now open with the current allocation; the old sentence is kept, labelled as the earlier reading.

Not acted on, with reasons:
- (d)6: not a contradiction. "Reads tying" in the Goods section is the goods instrument's reading of R4, not its strand tag; the card could say so (card-layout change, build.py).
- (d)2, (d)3: `source` strings are append-only history in this migration; the superseded sentences are labelled, not removed. Removing them is the author's call when the free-text `source` is retired (plans/sourcing.md order of work 5).
- (d)4: correct under the row-weakest rule (5150 is cited for what it lacks, recalled); R7 is unfaithful anyway (below).
- For the author, each a rule change needing a preregistration: **R7** re-encode to 5152 (release only on the psychiatrist's judgement; referral and certification outcomes); **R2**'s window before delivery (condition on admission rather than custody?); a restraint power for the facility's hold; **R8**'s reach to a 72-hour hold (5275's procedure vs 5250/5256); unbound variables in R1, R5, R6, R7, R10 (var_roles); **(d)7** the cps pair's rename display (a card / iso-report issue, not data); (d)8, (d)9, (d)10 card text.

L1: the seat confirms the carer-also-sanctions allocation as a fair reading of 5150; it finds one unfaithful police rule (R7) that is not one of the rows the match reads (R2, R4, R11). L1 stays `weakened` until the author takes the R7 decision; nothing in the seat's findings weakens the restated claim.

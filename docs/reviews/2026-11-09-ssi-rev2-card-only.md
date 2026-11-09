# Card-only review: SSI revision 2 (2026-11-09)

Seat: card-only (SEATS.md). Read only: docs/reviews/SEATS.md; cards ssi-marriage-penalty, ssi-marriage-penalty-individual, coverture-us-ssi, kibbutz-childrens-house; the numbered "Edits / Build" list of plans/ssi-entry.md "Revision 2 run". No YAML, JSON, code, other reviews or external sources.

**Counts: says it 8 / overstates 1 / understates 4 / cannot tell 2.** Cannot-tell rows fail legibility and pause the batch (SEATS.md).

## Judgements
1. SSI R2 (couple rate): says it. Formal `(and (married c s) (cohabits c s))` matches "married and living together"; the plain line says outright that a married pair living apart is not rated as a couple.
2. SSI R3 (couple limit): says it. Same condition, same plain wording; the CRS $4,000 aside is labelled as a reading, not text.
3. SSI R5 (individual rate): says it. `(not (and (cohabits) (or married holds_out)))` matches "not living together as a married or holding-out couple". The parenthesis "a married pair living apart is rated individually" answers the reader's question directly.
4. SSI R6 (individual limit): says it. Same condition, same parenthesis. The condition is readable, though the double negative needs the plain line to be read, not the formal.
5. Default capacity `pay_benefit` (removed R1): understates. Exact text, base and pair: "A agency may pay benefit a claimant unless a rule forbids it". Composite: "A agency may pay benefit a partner_a ...". Grammar fails ("A agency"; verb phrase "pay benefit" with no article; "a claimant" reads as a second subject). The intent can be recovered only from R7's plain line. Composite also leaks the aliased role name `partner_a` with no gloss.
6. "Power reading only" label: understates. Visible in the title of the base and the pair. Absent from the composite title (only in R2's plain line and the collapsed notes). No visible card text says what it means: the Legend has no entry, and the full explanation (a power the agency holds, not the mandatory duty) sits only in the collapsed "Encoder notes". R2's plain line "A power the agency holds, not an applied rate" is the only on-card gloss, and it appears only on R2.
7. Pair title/description: says it. "couple resource limit removed; one-rule pair; R3 dropped; couple rate and holding-out test kept" matches a card that lists R2, R4, R5, R6, R7 and not R3.
8. Pair id/name mismatch: understates. Id says "individual" but the pair keeps the couple rate (R2) and holding-out rule (R4). The only explanation ("The entry id is kept ... no longer describes it") is in collapsed notes, not on the card face.
9. Pair, "Pairs" section: overstates. Under "R3 dropped" it prints R3's full plain line ("The agency may apply the couple resource limit ... when they are married and living together"). A non-technical reader sees this as a rule the card has, when it is the base's wording. The Legend says the base card holds the original wording but does not say this line is that.
10. Pair, resource limit of a married cohabiting pair: cannot tell. With R3 gone and R6 excluding them, such a pair has no limit rule at all. Nothing on the visible card says so; it is only in collapsed notes ("Known limit"). A reader would assume the individual limit applies.
11. Properties married_couple_rated / married_couple_limited: cannot tell. The cards print only the plain meaning ("married and living together ... holds the power to rate/limit"), not the formal antecedent `(and (married c s t) (cohabits c s t))`, so the plain/formal match is not checkable on the card. On the pair card, `violated` for married_couple_limited is explained only by the unchanged "Whenever ... holds" text, with no note that violation means "no such power" (that is in collapsed notes).
12. Property married_rated_individually: understates. Text still says it was "preregistered to separate ssi-marriage-penalty from its individual-rate pair" and "it no longer separates the pair"; the pair card carries the same stale sentence, which now contradicts a pair that differs on married_couple_limited.
13. Composite coverture-us-ssi, inherited SSI rows R2-R7: says it. Conditions and plain lines are identical to the member card; `pay_benefit` capacity and `married_rated_individually: reachable` agree. Gap only as in 5 and 6.
14. Kibbutz R2, R3: says it. Both show `sanctioner: institution`. The Roles section describes the committee as "the kibbutz general assembly's organ", so a committee reprimand (R6) is institutional enforcement; the metapelet case (R3) fits the same way. Mild oddity: R6, the sanction itself, still shows "sanctioner derived, unreviewed" while R2/R3 do not; the Legend covers that tag.
15. Legend coverage: understates. Covers may/must, disability, implicit, kind, sanctioner (incl. institution), derived-unreviewed, default capacity, replaced/added, free fluent, strand. Missing: "power reading only", and the "Pairs" convention that a "dropped" line quotes the base.

## Fixes requested
- build.py capacity rendering: article and verb phrase. Emit "The agency may pay a benefit to the claimant unless a rule forbids it" (a/an chosen from the role; "pay_benefit" as "pay benefit to"); in composites print the member role gloss beside the aliased role.
- Add a Legend line (build.py) shown whenever the title or notes carry "power reading only": "every rule is a power the body holds, not the statute's duty."
- Composite: copy the member's "power reading only" label into the composite title.
- Pair "Pairs" section (build.py): render dropped rules as "R3 dropped (base wording, not in force here): ..." and add one visible sentence of consequence.
- Pair `plain`/notes: lift "Known limit" (a married cohabiting pair has neither limit) and the id/name caveat out of collapsed notes into the description line.
- Properties: print the formal antecedent beside each plain meaning; reword married_rated_individually meaning to remove "separate ... pair" (plain text).

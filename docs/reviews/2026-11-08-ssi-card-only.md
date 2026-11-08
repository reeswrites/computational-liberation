# Card-only review: ssi-marriage-penalty and ssi-marriage-penalty-individual (2026-11-08)

Read: the two cards, cards/README.md. Opened: Cornell 20 CFR 416.1802, 416.1806, 42 USC 1382 (first 100k chars). Not opened: POMS, CRS.

## ssi-marriage-penalty
- R1 pay may: (1) no source to judge; card admits it. (2) matches. (3) unverified, believable. (4) none, fine. (5) none.
- R2 couple rate, married: (1) fair. 416.1802: "we will count your combined income and calculated the benefit amount for you as a couple." Pin on card is bare 416.1802; the sentence sits in (b)(1). (2) Plain says "may"; source is mandatory ("will"), which the card admits only in the source cell. (3) "opened" overstated: card says it was carried from a worklist, "not re-opened"; I confirmed the quote. (4) kind/sanctioner none: defensible. (5) none.
- R3 couple limit $3,000, married: (1) fair but loose. (a)(3)(A) "$3,000 on January 1, 1989" covers an individual with a spouse living with them, not "married" as such. Plain's "rather than two $2,000 limits" is not in the text. (2) ok. (3) "opened" vs "not re-opened" conflict. (4) ok. (5) none.
- R4 holding out: (1) fair. 416.1806(a)(3): "an unrelated person of the opposite sex are living together in the same household"; "you both lead people to believe that you are husband and wife." Plain drops "opposite sex" and "unrelated". (2) matches; the cohabits/holds_out gate loses those qualifiers. (3) CFR opened; POMS not opened by me, cannot tell. (4) sanctioner none: ok. (5) none.
- R5 individual rate, not married: (1) the cited 416.1802 does not state an individual rate for the unmarried; the quote shown is CRS. Cite mismatch. (2) the complement condition is encoder inference, not stated in the plain line. (3) "opened" is too strong for an inference; should be partial. (4) ok. (5) none.
- R6 individual limit: (1) fair. (a)(3)(B) "$2,000 on January 1, 1989", for individuals with no spouse living with them. Plain's "neither married nor holding out" is inferred. (2) ok. (3) card says "not re-opened" yet "opened". (4) ok. (5) none.
- R7 resource bar, must not (disability): (1) the cited pin (a)(3) gives the limits only. The bar is in (a)(1)(B) (eligible only if resources "not more than" the limit). Pin is wrong. (2) ok. (3) unverified: card is right to say so, but the bar is actually in the statute. (4) disability with no sanctioner: defensible. (5) none.

Bindings: all shown bound. No "(sanctioner derived, unreviewed)" markers.

## ssi-marriage-penalty-individual
- R1: same as R1 above.
- R5 (replaced): (1) no source; a counterfactual. (2) "may rate as individual whatever the status" matches `true`. (3) unverified: correct. (4) fine. (5) none.
- R6 (replaced): same as R5 (replaced).
- R7: same as R7 above.
- Pair table lines for dropped R2-R4 are accurate to the base card. "rule None" appears twice in prose and reads as a bug.

## Can a reader tell?
Marriage claim: yes, mostly. Marriage or holding out brings the couple rate and the $3,000 limit; the unmarried get the individual rate and limit. The "may" encoding hides that the law is mandatory. The pair removal is clear: R2-R4 dropped, R5/R6 conditions deleted, resource bar kept. Unverified is partly clear, but the cards contradict themselves by showing "opened" beside "as carried from the worklist, not re-opened".

## Card should say
- Exactly what is verified: opened vs carried. Use one level that matches the prose.
- Fix the R7 pin to (a)(1)(B); fix the R5 cite (416.1802 does not say it).
- Note the limits attach to "with a spouse living with them", not marriage alone.
- Say 416.1806 text is opposite-sex only; the card's R4 plain line omits it, and POMS same-sex coverage is unchecked by me.
- Say the pair's "reform" has no legal text (S. 73 is only a lead) and that dollar amounts are not modelled.
- Property verdicts carry no meaning for the pair beyond the encoding; say "violated" means "power absent".
- Fix "rule None".

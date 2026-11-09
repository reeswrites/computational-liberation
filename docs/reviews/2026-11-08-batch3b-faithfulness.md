# Faithfulness batch 3b: encoding-faithfulness seat (ADR 0014)

Seat: fresh; did not build the batch. Read: plans/informal-rules.md "Faithfulness batch 3b" and Results; plans/faithfulness-batch.md sections 3 and 6; README Conventions; the `source` and `provenance` of every retagged row in src/*.yaml, with `git show 035cc4c^:` for the before state. No external source fetched; no engine run. Judgments are of the new `kind` against what the repo records as read.

Confirmed: the diff 035cc4c^..e3420ef changes no `deontic`, `or_else`, `sanctioner`, `implicit` or `condition` line in src/; only `kind`, `sanctioner_review`, `plain`, `source`, `provenance` and one `notes`.

## Counts

- Retagged rows judged (defining files; inherited copies follow): 19. Faithful 17, unfaithful 2, cannot tell 0.
- B1 promotions: accepted 2 (crisis-team R8, mwpa-creditor-exemption R10); refused 2 (mwpa-creditor-exemption R12, footbinding R10).
- B1 holds: all 7 present and correct.
- Kibbutz R2/R3 sanctioner: ruling `institution` (recorded, not applied).

### Fix pass should (proven against recorded text)

1. mwpa R12: revert to `norm`, add the hold note "written law in substance, text not opened; retag to formal when opened" (the preregistered contingency). The row's own source says "UNVERIFIED ... as a rule of the 1839-50 acts"; the only quote recorded (Chused 1984, relayed, no access date) is about exemption from debts, not a conveyance power.
2. footbinding R10: revert to `norm` with the same hold note. Its source says "no text says a suitor 'may' pledge; reconstructed from the convention account"; every item is recalled or unverified. This also removes a contradiction the batch introduced: R4 (the family's half of the same pledge, same source paragraph) went formal -> norm in B4 while R10 (the sons' half) went norm -> formal.
3. mwpa R10 `source`: it still reads "UNVERIFIED (general knowledge; no source opened)" while the row now carries an `opened` Blackstone item. Reword to "no source opened for the creditor's reach itself; the vesting is opened (Blackstone II.29)".
4. footbinding R4 retag sentence "Mackie's convention is unwritten; the marriage market, not a body, enforces it" was copied from R1/R6/R7 and does not describe R4, which is the pledge, not the convention. Replace with an R4 reason: the pledge wording was seen as search snippets only, nothing written was opened.
5. ectogenesis R5 `source` still opens "implicit norm (a care-norm, not a written rule; no sanction): the female registered parent ... must care for it" under `kind: strategy`. Under the README's definitions norm and strategy differ by enforcement; add "retagged strategy because 'no sanction'" at that point, or drop "norm".

## 1. Row by row

### B1, norm -> formal

- crisis-team R8 (officer may detain): faithful. The cited text is Cal. WIC s. 5150(a), a statute, and the excerpt is the power encoded: "a peace officer ... may, upon probable cause, take ... the person into custody for a period of up to 72 hours". The note discloses that the statute also needs probable cause and covers "gravely disabled" while the row reads only danger. Accepted.
- mwpa R10 (creditor may attach): faithful, accepted with the disclosure the row already carries. The opened excerpt vests the wife's chattels in the husband ("the husband hath therein an immediate and absolute property"); the creditor's reach of what he holds is, as the source says, "the encoder's inference from it, not a quoted sentence". `norm` (unwritten practice others enforce) and `strategy` would both misdescribe creditor attachment; `formal` with "(inferred from written law, Blackstone II.29)" in the plain line is the honest tag, and the inference is disclosed in `plain`, `source` and the item note. See fix 3.
- mwpa R12 (husband may transfer_to_wife): unfaithful as recorded; refused. No opened item. The one recorded quote (Chused 1984, `recalled`, relayed via plans/backtest-mwpa.md) says the acts "generally contained nothing more than statements exempting married women's property from the debts of husbands"; the conveyance route is the encoder's reading ("Blackstone's bar on grants between spouses is read as lifted"). `formal` here would mean "we read the writing", and nothing was read. Fix 1.
- footbinding R10 (suitor may accept_match_pledge): unfaithful as recorded; refused. No opened item; four `recalled`, one `unverified`; the source itself: "no text says a suitor 'may' pledge". The B1 reason ("an explicit, written commitment") rests on the encoder's statement; the Wikipedia pages were "search snippets only, pages not opened". Fix 2.

On the two copied items: legitimate in both cases. Each copy keeps the same `source_id`, pin, url, excerpt and `accessed` date as the originating row (police-crisis R3, 2026-11-06; coverture-household R1, 2026-11-04) and a note naming the origin and the date it was attached. That is a recorded read attached to a second rule the text bears on, not a level raised without a read: the source was opened. The difference is what the excerpt proves: for R8 the rule itself, for R10 only the premise.

### B2, norm -> strategy

- police-crisis R1 (dispatcher must dispatch): faithful. Source: "nothing in WIC 5150 requires it, dispatch practice does".
- cps R6 (social_worker must contact_mother): faithful. Source: "the mother is the parent called first" (plan), unverified; no enforcer recorded.
- crisis-team R7 (responder may request_police): faithful. "the team can call police when a scene turns violent; practice, not written policy". A permission as a "regularity" is thin, but the text gives no writing and no enforcer.
- paternity-quota R7 (birthing_parent must take_shareable_leave; inherited by transferable-leave): faithful. "the shareable block is taken by the mother by default (the pattern the quota was introduced to break)": a default, nobody recorded as enforcing it.
- ectogenesis R5 (intended_parent must provide_care; inherited by gestational-surrogacy): faithful. The source's own words are "no sanction"; the Kleven penalty is unlocated in the bibliography and section 6 ruled it is not a peer sanction. See fix 5 for the leftover "norm" wording.

### B4, formal -> norm

- kibbutz R1 (committee may assign): faithful as against `formal`. The opened page "names no committee or assignment procedure"; nothing written is cited. Between `norm` and `strategy` the text does not decide; `norm` is the plan's loose "practice" reading, disclosed.
- kibbutz R3 (metapelet must provides_care, or_else R6): faithful. Opened: "had a nanny who took care of their everyday needs"; the duty-on-pain-of-reprimand is the encoder's link (disclosed) and no by-law is cited.
- kibbutz R4 (child must_not sleep_home, disability): faithful. Opened: "communal sleeping arrangements"; a practice, now a customary disability.
- kibbutz R5 (male_member may visit): faithful. Opened: "visited their parents for 2-3 hours a day"; the "at any time" gap is pre-existing, disclosed.
- footbinding R1, R6, R7: faithful. Mackie's snippet: "a self-enforcing convention ... maintained by interdependent expectations on the marriage market"; unwritten, enforced by the marriage market (others), which R6/R7 encode.
- footbinding R4 (family may leave_unbound_pledge): tag faithful (nothing written was opened: "search snippets only, pages not opened"), retag reason unfaithful to the row. Fix 4.

### B5, formal -> strategy

- naming-convention R1, R2: faithful. Opened manuscript: "prompted to enter a name in the response field ... occasional switching"; the source says "no sentence of the paper states a permission"; the plain line says "no one sanctions either choice".

## 2. B1 holds

companion-ownership R6, R9, R11 and companion-guardian-renamed R6, R9, R11: each `kind: norm`, `sanctioner_review: derived`, `source` ends "Kind held at norm 2026-11-08 (batch 3b, B1 ruling): written law in substance, text not opened; retag to formal when opened." paternity-quota R9: same note, `norm`, `derived`. All seven correct.

## 3. Kibbutz R2 and R3 `sanctioner`: ruling `institution` (recorded, not applied)

`sanctioner` is "who enforces the `or_else`" (README). The `or_else` of both rows is R6, whose actor is the `committee` role; the entry's Roles gloss defines that role as "the work / education committee that staffs the children's house (the kibbutz general assembly's organ)". R6's own (unverified) source names "the general assembly and public opinion as the kibbutz's instrument of discipline over members". "Public opinion" would be `peers`, but the encoding did not give the sanction to a peer role (male_member, metapelet); it gave it to a named organ, and the field describes the sanction as encoded. So `institution` for R3. For R2 the hand review's point ("there is no body above the committee") is real: the committee reprimands itself, and in life it is the assembly, i.e. the members, that would correct it. But the or_else actor is still the committee; `peers` becomes right only if R6's actor is changed to a members/assembly role, an encoding change outside this seat. Ruling: `institution` on both, the R2 self-sanction carried as a note. Spiro and Gavron are unverified; the ruling rests on the Roles text and the encoded actor.

## 4. B2 `strategy must` honesty

Every B2 `plain` carries "(practice, not written; nobody enforces it)", so it claims no enforcement. Each `source` adds "the must is kept so the engine sees who carries the duty under strict compliance, though nobody enforces it"; the Results record the card clause on all six `must` rows. Honest: the sources describe regularities ("default", "called first", "practice"), not duties; the duty is the engine's reading, said so on row and card. The one slip is ectogenesis R5's "implicit norm ... must care for it" (fix 5).

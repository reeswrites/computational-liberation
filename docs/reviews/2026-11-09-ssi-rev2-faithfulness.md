# SSI revision 2: encoding-faithfulness seat (ADR 0014)

Seat: fresh; did not build the batch. Read: SEATS.md (this seat); plans/ssi-entry.md (design, Revision 2 decisions, rulings, run, N74-N76); `git diff d5d3a92..3bc056a -- data/institutions/src/`; full YAML of both SSI entries, kibbutz R2/R3/R6 and roles; the three SSI property glosses; README "Default-capacity actions"; plans/informal-rules.md Rulings 2026-11-09 item 2; docs/reviews/2026-11-08-ssi-faithfulness.md (the raw-read quotations the YAML leans on). No external source fetched; no engine run; no other seat's review of this batch read.

Model-family caveat: same family as the encoders.

Confirmed from the diff: no provenance level, excerpt or `accessed` changed; no new provenance item.

## Counts

Items judged 9: faithful 5 (R2, R3, R6, the two property edits as one, kibbutz R2/R3), understates 1 (`pay_benefit` default capacity, disclosed by the label), overstates 2 (R5 married-apart branch, pre-existing and disclosed; the one-rule pair read as a reform), cannot tell 0. The pair's overstatement is framing, not a rule, and is disclosed (notes, N76); no `unsourced` or undisclosed `overstates` on a rule a headline verdict reads. **The batch does not pause.**

## Findings

1. **R2, R3** (`when (and (married c s) (cohabits c s))`): **faithful**. The deciding words, as the 2026-11-08 seat recorded them from raw text: 1382(a)(1)(B)(i) "in case such individual has a spouse with whom he is living"; 416.1802(b) applies to "an eligible spouse as defined in 416.1801(c)", living "in the same household". Provenance honest: levels stay `snippet` / `unverified`, no excerpt invented, and `source` says "not re-opened by the builder; no excerpt added". One quote drift: R2 `plain` quotes "with whom he or she is living" for both sections; the repo records "with whom he is living" (statute) and "in the same household" (416.1801(c)), and "he or she" nowhere.

2. **R6** (complement): **faithful**. The individual limit is for one without a spouse "with whom he is living", so a married pair living apart keeps it. **R5**: **overstates, pre-existing and disclosed**. No recorded text states an individual rate for a married pair living apart; it is the encoder's complement, and the 416.1802(a) deeming case and 416.1806(a)(2) stay unencoded (said in `source` and `notes`). Revision 2 widens what R5 covers on the same disclosed inference.

3. **R5/R6 kept as conditioned rules (deviation from ruling 3)**: **more faithful than the ruling as worded**. The individual rate and limit belong to those not in an SSI couple; a default capacity cannot carry that, and adding couple disabilities instead would recast "not a couple" as a prohibition the text does not state. Disclosure: full in the plan (Scope (c), drift 4) and N74; the base `notes` gives the reason but does not say it departs from the ruling.

4. **Property edits**: **faithful**. Each gloss says what its formal says ("married and living together"). The names still fit: an SSI "couple" is the cohabiting married pair. Leftover: `married_couple_rated` still says "marriage brings the couple rate".

5. **One-rule pair** (R3 dropped): **overstates if read as a reform**. The name "SSI with the couple resource limit removed" is literally true and the notes are honest (neither limit power for a married cohabiting pair; "not a coherent reform text; no reform bill was read"). But ruling 4's reason, "the lever the marriage-penalty bills actually pull", rests on an unopened lead (S. 73), and no bill is recorded as leaving married couples with no limit; a reform would give them the individual limit, which is a two-rule change (drop R3, widen R6). The id `-individual` now misdescribes the entry: married cohabitants get no individual limit in it. Disclosed (notes, N76), but the title is what a reader sees.

6. **"Power reading only"**: present in both entry names (card titles), the lead of base `notes`, R2 `plain`, pair `notes`, composite `notes`. Accurate, with one slip: "every rule here is a power" while R7 is a disability.

7. **`pay_benefit` default capacity**: **understates, disclosed**. The statute is mandatory for the eligible (stated in R2 `source`; no "shall" text is excerpted), and the label covers that. Separate concern: the README reserves the flag for "a capacity a person of that kind holds by default" and calls cps `petition` "a conferred power, not a default capacity". An agency's power to pay is conferred by statute; R1 was honestly "the encoder's grant"; the card line now reads as a fact about agencies. Author-ruled; no verdict moves.

8. **Kibbutz R2/R3 `sanctioner: institution`**: **faithful** to the entry. R6's actor is `committee`, glossed "the kibbutz general assembly's organ".

## Fixes requested (prose only)

1. R2 `plain`: replace the quoted "with whom he or she is living" by the recorded words, attributed separately.
2. Base `notes` item 3: add "a departure from ruling 3 as worded (N74)".
3. Pair `name`: add "a deletion, not a reform".
4. `married_couple_rated` gloss: "marriage with a shared household brings the couple rate".
5. Base `notes`: "every rule is a power, except R7, a disability on one".

## For the author

1. **R5/R6 (N74)**: confirm the builder's reading. Recommend: keep as conditioned rules; amend ruling 3 to "R1 only".
2. **Property edit (N75)**: confirm. Recommend: accept; the properties restate the rules.
3. **One-rule pair (N76)**: recommend keeping it as a deletion pair, never cited as a bill; rename the id next dataset PR (for example `ssi-marriage-penalty-no-couple-limit`); for a reform pair, open a bill first and preregister the two-rule version.
4. **`pay_benefit`**: recommend one README sentence that here the flag marks an encoder's grant to an agency, or reverting to a labelled R1 at the must-be revision.

# Card-only seat: faithfulness batch 3b (kind and sanctioner retags)

Fifth seat (ADR 0014). Read only `docs/cards/*.md` and the "Faithfulness batch 3b" Rows tables in `plans/informal-rules.md`. No YAML, JSON, build.py or external source opened. Each row is judged against the card's own Legend: `formal` = written law or contract, `norm` = an unwritten practice that others enforce, `strategy` = a regularity nobody enforces; disability sentence as printed.

## Counts

40 rows judged (39 rule rows + the coverture-household-us notes parenthesis).

- says it: 39 (of which 14 "says it (disclosed)": the tag rests on text the card says was not opened, and the plain line says so)
- overstates: 0
- understates: 1 (footbinding R4, by the card's own R10 reasoning)
- cannot tell: 0

The batch does not pause on this seat.

## Checks (a) to (f)

- (a) All six `strategy must` rows print "(strategy: nobody enforces this, yet the engine reads it as a duty under strict compliance)" in the deontic cell, and every plain line opens "(practice, not written; nobody enforces it)". No plain line claims enforcement. Legible.
- (b) crisis-team R7's plain line says "nobody enforces it"; naming-convention R1/R2 say "no one sanctions either choice". The reader can tell.
- (c) The Legend now reads: "The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`)." That makes kibbutz R4's "must not (disability) [kind: norm]" intelligible. All 33 cards carry the sentence.
- (d) crisis-team R8: level `opened`, s. 5150(a) excerpt quoted in Sources, plain line cites Cal. WIC 5150: says it. mwpa R10: level `unverified`, but an `opened` Blackstone II.29 excerpt is shown and the plain line says "(inferred from written law, Blackstone II.29)": says it (disclosed). mwpa R12: level `unverified`, no item opened, plain line "(written law in substance, text not opened)": says it (disclosed). footbinding R10: level `unverified`, no item opened, plain line "(the pledge associations' written pledge; text not opened)": says it (disclosed).
- (e) transferable-leave R7/R9, gestational-surrogacy R5, kibbutz-no-implicit R1/R3/R4/R5, footbinding-no-pledge R1/R6/R7, mwpa-property R10/R12: tag, plain line, level and Sources text identical to the parent card, character for character in the rows compared.
- (f) "(sanctioner derived, unreviewed)" is absent from every retagged row (grep over all cards: no `kind: strategy` row carries it; none of crisis-team R8, mwpa R10/R12, footbinding R1/R4/R6/R7/R10, kibbutz R1/R3/R4/R5 carries it). Still present where expected: crisis-team R1, R2, R9; cps R5, R7; mwpa R11; footbinding-no-pledge R2, R3, R5, R9; the companion hold rows R6/R9/R11 (correct, nothing retagged there).

## Per card

### crisis-team
- R7 `strategy may`: says it. Plain "nobody enforces it"; Source "a regularity nobody sanctions"; level unverified, disclosed.
- R8 `formal may`: says it. Level opened, s. 5150(a) excerpt quoted. Note: the row also prints "(implicit)", which the Legend defines as "a practice no text states"; that now contradicts the opened text beside it (see fixes).

### police-crisis
- R1 `strategy must`: says it. Clause present; plain claims no enforcement; Source says "nothing in WIC 5150 requires it, dispatch practice does".

### cps
- R6 `strategy must`: says it. Clause present. Minor: the Source rationale says the mother is "called first and held responsible", which a reader may hear as enforcement; the tag and plain line say none.

### paternity-quota and transferable-leave (identical rows)
- R7 `strategy must`: says it. Clause present. The Source still opens "implicit norm:", a stale word against the new tag.
- R9 `norm may` (B1 hold): says it (disclosed). But the card says three things about one rule: plain "(practice, not written)", Source "Reconstruction, not statute", Source "written law in substance, text not opened". The hold is disclosed; the wording is not consistent.

### ectogenesis and gestational-surrogacy (identical rows)
- R5 `strategy must`: says it. Clause present; plain adds "no sanction is attached". Source still opens "implicit norm".

### footbinding
- R1 `norm may`: says it. Source names the enforcer ("the marriage market, not a body").
- R4 `norm may` (the family's anti-footbinding pledge): understates. The card's own R10 note says "the pledge is an explicit, written commitment of the pledge associations, not an unwritten practice", and R4's Source describes the same two-part pledge ("members pledged not to bind their daughters' feet and not to let their sons marry women with bound feet"). The daughter half (R4) is tagged `norm`, the son half (R10) `formal`, on the same recalled Wikipedia/Mackie items. One of the two tags is wrong by the card's own text; since R10's reasoning is the one the batch adopted, R4 is the one that understates. Its retag note ("Mackie's convention is unwritten; the marriage market ... enforces it") describes R1/R6/R7, not a pledge.
- R6 `norm may`: says it.
- R7 `norm may`: says it. Level recalled; Mackie snippet quoted.
- R10 `formal may`: says it (disclosed). Level unverified; plain discloses "text not opened". Carries "(implicit)" beside `formal` (see fixes).

### footbinding-no-pledge
- R1, R6, R7: says it; identical to parent.

### kibbutz-childrens-house
- R1 `norm may`: says it. Plain discloses "unsourced: the committee is the encoder's reconstruction; unverified".
- R2 `norm must_not`, sanctioner peers (not retagged): says it.
- R3 `norm must`, sanctioner peers: says it as to kind. The or-else reads "the committee may reprimand (R6)" while the tag says `peers`; that is the R2/R3 question the batch records and does not apply, so not counted here.
- R4 `norm must_not (disability)`: says it. Legend sentence makes it intelligible; level opened, excerpt "communal sleeping arrangements".
- R5 `norm may`: says it. Level unverified ("at any time" is the encoder's reading, disclosed).

### kibbutz-childrens-house-no-implicit
- R1, R3, R4, R5: says it; identical to parent.

### naming-convention
- R1, R2 `strategy may`: says it. Level opened; plain says "no one sanctions either choice"; Source says the permission is the encoder's reading of the game design.

### mwpa-creditor-exemption and mwpa-property (identical rows)
- R10 `formal may`: says it (disclosed). The Blackstone excerpt supports the vesting; the Source says the creditor's reach "is the encoder's inference from it, not a quoted sentence". Level unverified because the inference item remains.
- R12 `formal may`: says it (disclosed). Level unverified, nothing opened. Minor: the Source prints two quoted Chused 1984 sentences next to a `recalled` item; a reader may take quotation marks for an opened read.

### companion-ownership and companion-guardian-renamed (identical rows)
- R6, R9, R11 `norm must_not (disability)` (B1 holds): says it (disclosed). Same plain/Source tension as paternity-quota R9: plain "(practice, not written)" against Source "written law in substance, text not opened".

### coverture-household-us
- Encoder notes parenthesis: says it. Reads "(pre-reform divorce required both spouses' consent or proof of fault; Stevenson & Wolfers w10175, opened 2026-11-06, Table 1 lists nine pre-1964 unilateral statutes)"; the Sources R6 excerpt supports it verbatim. Minor: the R6 plain line says "the spouse's consent" where notes and excerpt say "both spouses".

## Card should say

1. footbinding R4: either retag to match R10 (the card's own text calls both halves one written pledge), or change R10's note so the two halves are treated alike. At minimum replace R4's retag note "Mackie's convention is unwritten; the marriage market, not a body, enforces it" with wording about the pledge, since R4 is the pledge, not the convention.
2. B1 hold rows (paternity-quota/transferable-leave R9; companion-ownership and companion-guardian-renamed R6, R9, R11): the plain prefix "(practice, not written)" contradicts the Source note "written law in substance". Use "(written law in substance, text not opened; held as a practice until read)" so the plain line and the Source agree.
3. paternity-quota/transferable-leave R9 Source: "Reconstruction, not statute" and "written law in substance" sit in the same paragraph. Keep one.
4. "(implicit)" beside `formal` (crisis-team R8, mwpa R10, R12, footbinding R10): the Legend says implicit means "a practice no text states". For R8 the text is opened and quoted on the same card. Either the Legend's implicit sentence should read "a rule no read text states in so many words; the encoder's reconstruction or inference", or R8 should not print "(implicit)". This is a wording question for the author; no kind tag is wrong.
5. Stale "implicit norm:" openers in the Sources of the `strategy` rows (paternity-quota/transferable-leave R7, ectogenesis/gestational-surrogacy R5): change to "implicit regularity:" or "implicit practice:" so the Source does not call a `strategy` row a norm.
6. cps R6 Source: "called first and held responsible" reads as enforcement; "called first and expected to answer" or drop "held responsible".
7. mwpa R12 Source: mark the Chused 1984 quotations as relayed ("quoted via plans/backtest-mwpa.md, not opened") so quotation marks next to `recalled` do not read as an opened excerpt.
8. coverture-household-us R6 plain: "the spouse's consent" to "both spouses' consent", matching the notes and the excerpt.

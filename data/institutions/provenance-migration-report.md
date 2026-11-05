# Provenance migration report (2026-11-05)

`migrate_provenance.py` drafted a `provenance:` list on every rule from its free-text `source`; the output was then
reviewed row by row, and 35 rows were set by hand (the script's `OVERRIDES`, so a re-run reproduces them). Contract:
`plans/sourcing.md`. Bibliography: `data/sources/rules.yaml` (49 works, every one used). No source was opened in this
session (network fetches blocked), so **no row was upgraded**: every level below comes from what the old string
records, and where unsure the lower level was taken.

Row counts: 121 rules are written in `src/*.yaml` (own rows; an inherited rule is counted once, where written); 211
rows across the 25 resolved entries.

## Counts

| | own rows (121) | resolved rows (211) |
|---|---|---|
| before: `UNVERIFIED` in the source string | 71 | 121 |
| after, weakest item per row: opened | 7 | 18 |
| snippet | 0 | 0 |
| recalled | 39 | 64 |
| unverified | 75 | 129 |

Items (a row may rest on several works): own rows 171 items (opened 15, snippet 7, recalled 65, unverified 84;
52 items have `source_id: null`); resolved rows 312 items (opened 28, snippet 12, recalled 123, unverified 149).

Every row whose old string says `UNVERIFIED` is `unverified` after. Four rows without `UNVERIFIED` in the string
became `unverified` (an item for a part of the rule no named work supports):
- mwpa-earnings R14, mwpa-sole-trader R15, mwpa-suit R16: "Statute texts not opened ([R])"; the state acts are named
  only through GLT / Khan, so a `source_id: null` item records the unread statutes.
- footbinding R3: implicit sanctioned norm; Mackie's abstract (snippet) supports the convention, no text states the norm.
  Judgement call; drop that item to make the row `snippet`.

Snippet is never the weakest item of a row: every footbinding row resting on Mackie's abstract also rests on
something lower (the reconstructed rule, or the [R] Wikipedia pledge pages, or Brown et al. [R]).

## How the heuristic classified (rows not in the hand list)

- `opened` only when the row's own string says the work was read (a date or a URL) and quotes it after that; the
  excerpt is the quoted passages joined with " ... " (each fragment checked verbatim against the row's string).
  This gave kibbutz R1, R3, R4, R5 (Wikipedia, read 2026-11-03).
- A work cited with a URL and a quote but no read record in the row (Cal. WIC 5150 / 306, Penal 597s, Civ. 1941,
  QPIP, KUNC, Berkeley policy) is `recalled`, with the quote kept in `note` ("quote in the old string (no read
  date)"). The README's "verified at writing time" list and the entries' `source_text` ("read at ...") were **not**
  counted as reading records for a row: they carry no date per row and the instruction was to read the rule's own
  string. These rows are the cheapest to upgrade: re-open the URL, confirm the quote, set `opened` with the date.
- `[F, via plans/backtest-mwpa.md]` (Chused 1984, Khan 1996, GLT 2007): an earlier batch reports fetching, relayed
  second-hand with no access date -> `recalled`, quote (if any) in `note`.
- Rows naming no work (implicit norms, "general knowledge" rules, constructions): one item, `source_id: null`,
  `unverified`, note quoting the rationale.

## Rows set by hand (OVERRIDES), with the reason

| row | set to | reason |
|---|---|---|
| coverture-household R1 | Bk II ch 29 opened | the string also names Bk I ch 15 as the citation it replaced ("did not support this rule"); only Bk II ch 29 supports the row |
| coverture-household R2, R4, R7 | Bk I ch 15 recalled, `url` = NYHS WAMS page | the WAMS page is the copy cited for Bk I ch 15, not a second work; no read claim or quote in the row |
| coverture-household R5 | Bk I ch 15 opened (one item) | the earlier WAMS pointer is the same work; excerpt = both quoted passages |
| coverture-household R6 | Shanley unverified, Stone unverified | the string names Bk I ch 15 only to say it is no longer cited |
| police-crisis R1 | null, unverified | implicit; WIC 5150 is named only to say it does not require police dispatch (the heuristic had mapped it) |
| police-crisis R7 | WIC 5152 opened; WIC 5150(a) recalled | 5150(a) is cited for the absence of an officer release duty |
| cps R7 | WIC 361(c)(1) opened | pin and excerpt tidied |
| companion-ownership R1, companion-guardian-renamed R1 | Civ. 655 opened, 663 opened, 658 recalled (+ R.I. 4-13-41 recalled on renamed) | Penal 597s is named only as the dropped citation; s. 658 cited without a read record; R.I. cited for the role name, not the rule |
| companion-guardianship R9 | Alaska 25.24.160(a)(5) unverified + null unverified (the generalisation) | the row says "UNVERIFIED (general knowledge; no source opened)" though it quotes the statute and the entry's source_text says read; kept the lower level |
| public-library R2 | Berkeley policy recalled + null unverified | "UNVERIFIED as a rule": the duty to serve is read from the policy's premise |
| naming-convention R1, R2 | Centola et al. 2018 unverified | "cited from memory" and "UNVERIFIED as a quotation": the lower of the two |
| kibbutz-childrens-house R2 | Wikipedia recalled, Tiger & Shepher unverified, Kirkus recalled | three works at three levels; this row records no read of the Wikipedia quote (R1's row does) |
| kibbutz-childrens-house R6 | Spiro unverified, Gavron unverified | tidied notes |
| airline-flight R2 | 14 CFR 121.571 opened, 121.391 opened (no separate date), null unverified | the string says the general in-flight care duty is UNVERIFIED (no text opened states it); 121.391 supports egress only |
| mwpa-creditor-exemption R12 | Chused 1984 recalled, Chused 1983 unverified, Bk I ch 15 recalled, null unverified | Blackstone's bar on grants is cited; the conveyance is "UNVERIFIED as a rule of the 1839-50 acts" |
| mwpa-property R13 | NY MWPA 1848 unverified (effective 1848), GLT recalled | GLT is named twice; the statute text not opened ("[R] UNVERIFIED") |
| mwpa-suit R16 | MWPA 1882 s. 1(2) opened, GLT recalled, null unverified | the heuristic lifted the old R9 wording ("may sue when not married") into GLT's note |
| footbinding R1 | Mackie snippet + null unverified | abstract quotes as a search-index snippet; the rule itself "UNVERIFIED as a rule" |
| footbinding R3 | Mackie snippet + null unverified | implicit sanctioned norm (see above) |
| footbinding R4 | three Wikipedia pages recalled, Mackie snippet (no excerpt) | "search snippets only, pages not opened: [R]" -> the lower of snippet and [R]; this row quotes none of Mackie's abstract |
| footbinding R10 | as R4 + null unverified | the rule is reconstructed ("UNVERIFIED") |
| footbinding R5, R6 | Mackie snippet, Wikipedia pages recalled, null unverified | "UNVERIFIED ... as a rule" |
| footbinding R7 | Mackie snippet, Brown et al. 2012 recalled | Brown: abstract-only search snippet tagged [R] |
| ectogenesis R1, R2, R3 | Firestone 1970 unverified | "from memory" and "UNVERIFIED: no text opened": the lower |
| ectogenesis R4, R5, R6, R7 | null, unverified | Firestone is named only in the boilerplate ("no text opened for this rule"); no work supports these rows |

## Jurisdiction mismatches (flagged, not fixed)

The MWPA chain encodes US state acts (GLT / Khan: NY, MA, PA, ME ...), but:
- every `mwpa-*` entry inherits coverture R2, R4, R5, R7 (where not dropped) sourced to Blackstone Book I ch. 15
  (England), and R6 sourced to Shanley 1989 and Stone 1990 (Victorian England; exit before the English Matrimonial
  Causes Act 1857). Resolved rows: mwpa-creditor-exemption R1 (Bk II ch 29), R2, R4, R5, R6, R7; mwpa-property R2,
  R4, R5, R6, R7; mwpa-earnings R2, R4, R5, R6, R7; mwpa-sole-trader R2, R4, R5, R6; mwpa-suit R2, R5, R6;
  mwpa-property-narrowed R2, R4, R5, R6, R7 (28 resolved rows; with R12 in six entries and R16, 35).
- mwpa-creditor-exemption R12 (and every entry inheriting it) cites Blackstone's bar on grants between spouses (England).
- mwpa-suit R16 cites the Married Women's Property Act 1882 (45 & 46 Vict. c. 75), a UK act, for a US suit provision
  (GLT: e.g. NY 1860).
- crisis-team R8 cites Cal. Welf. & Inst. Code 5150(a) (US-CA) for the officer's custody power in an entry modelled on
  Denver STAR (Colorado; the KUNC article).
- Mixed but declared: companion-guardianship R9 (Alaska) on a California base (companion-ownership: Cal. Civ. 655/663,
  Penal 597s); companion-guardian-renamed R1 adds R.I. 4-13-41 for the role name; transferable-leave R2 combines
  Canadian EI (federal) with Quebec's QPIP as a minimal-pair construction.

## Works named in source strings that are not mapped to the bibliography

- Matrimonial Causes Act 1857 (coverture R6): named as the subject of Shanley / Stone, not cited as a source.
- The US state acts named through GLT / Khan: NY 1860, MA 1846/1874, PA 1872 (R14 earnings); ME 1844, MA 1860,
  NY 1860 (R15 sole trader); NY 1860 (R16 suit); Mississippi 1839 (R11, via Khan). Recorded as `source_id: null`
  items where the row encodes them (R14, R15, R16); no entries, since no title or text is in the repo.
- NYHS WAMS coverture page: used as the `url` of the Blackstone Book I ch. 15 items, not a separate work.
- "the Kleven finding in docs/theory.md" (ectogenesis R5): no citation anywhere in the repo.
- "the third review's 6-rule sketch" (airline R1, R3, R4, R6), `plans/ectogenesis.md`, `plans/backtest-mwpa.md`,
  ADRs: internal documents, not works.
- "state surrogacy acts vary" (gestational-surrogacy R2, R3), "local animal-control impound" (companion R7),
  "general peace-officer powers" (police R5): no work named.
- Dropped citations named only to say they no longer apply: coverture R1 (Bk I ch 15), companion R1 (Penal 597s),
  airline R2 (14 CFR 91.11 / 121.580). Not given items on those rows.

## Bibliography gaps (not in repo text; null in data/sources/rules.yaml)

Given names (Shanley, Stone, Spiro, Gavron, Tiger, Shepher, Mackie, Khan, Chused, Geddes, Lueck, Tennyson, Centola
and co-authors, Brown and co-authors); titles of GLT 2007, Chused 1983 and Chused 1984; URLs of the three
Wikipedia pledge pages, Shanley, Stone, Spiro, Gavron, Tiger & Shepher, Brown et al., Firestone, Cal. WIC 317 / 328 /
5275 / 16501, Penal 597 / 11165.14, Civ. 658, 14 CFR 91.11 / 121.580, NY MWPA 1848; enactment years of the
California, Quebec and CFR sections.

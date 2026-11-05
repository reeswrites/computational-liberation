# Provenance migration report (2026-11-05)

`migrate_provenance.py` drafted a `provenance:` list on every rule from its free-text `source`; the output was then
reviewed row by row, and 40 rows were set by hand (the script's `OVERRIDES`, so a re-run reproduces them; 35 at
first, 5 more and several changes in the fix pass after the council review of 2026-11-05,
`docs/reviews/2026-11-05-sourcing-migration-review.md`). Contract: `plans/sourcing.md`. Bibliography:
`data/sources/rules.yaml` (49 works, every one used). No source was opened in this session (network fetches
blocked), so **no row was upgraded above what its string records**: every level below comes from what the old
string records, and where unsure the lower level was taken. At item level, 11 hand-set items in 6 rows sit above
the heuristic's level for that work; each is licensed by a clause of its own row's string the heuristic misreads
(see "Items raised above the heuristic" below). The script refuses to write if a raise is not listed there.

Row counts: 121 rules are written in `src/*.yaml` (own rows; an inherited rule is counted once, where written); 211
rows across the 25 resolved entries.

## Counts

| | own rows (121) | resolved rows (211) |
|---|---|---|
| before: `UNVERIFIED` in the source string | 71 | 121 |
| after, weakest item per row: opened | 4 | 12 |
| snippet | 0 | 0 |
| recalled | 40 | 66 |
| unverified | 77 | 133 |

Items (a row may rest on several works): own rows 176 items (opened 11, snippet 5, recalled 71, unverified 89;
57 items have `source_id: null`); resolved rows 325 items (opened 21, snippet 10, recalled 132, unverified 162).
(Before the 2026-11-05 fix pass: own rows opened 7, recalled 39, unverified 75; 171 items, opened 15, snippet 7,
recalled 65, unverified 84, 52 null; resolved rows opened 18, recalled 64, unverified 129. The changes: kibbutz
R1, R3, R5 lose `opened`, Mackie on footbinding R4 / R10 and 14 CFR 121.391 drop to `recalled`, and five
`source_id: null` items are added: kibbutz R1, R5, R6, mwpa-creditor-exemption R11, ectogenesis R5.)

Every row whose old string says `UNVERIFIED` is `unverified` after. Six rows without `UNVERIFIED` in the string
became `unverified` (an item for a part of the rule no named work supports):
- mwpa-earnings R14, mwpa-sole-trader R15, mwpa-suit R16: "Statute texts not opened ([R])"; the state acts are named
  only through GLT / Khan, so a `source_id: null` item records the unread statutes.
- footbinding R3: implicit sanctioned norm; Mackie's abstract (snippet) supports the convention, no text states the norm.
  Judgement call; drop that item to make the row `snippet`.
- kibbutz-childrens-house R1 (the committee's power to assign) and R5 (a male member's visit): the Wikipedia page
  was read, but the quoted passages do not state these rules (R1: nothing on a committee or assignment; R5: the quote
  says children visited their parents, the reverse direction); the rule is the encoder's parenthesis, so a null item.

Snippet is never the weakest item of a row: every footbinding row resting on Mackie's abstract also rests on
something lower (the reconstructed rule, or the [R] Wikipedia pledge pages, or Brown et al. [R]).

## How the heuristic classified (rows not in the hand list)

- `opened` only when the row's own string says the work was read (a date or a URL) and quotes it after that; the
  excerpt is the quoted passages joined with " ... " (each fragment checked verbatim against the row's string).
  This gave kibbutz R1, R3, R4, R5 (Wikipedia, read 2026-11-03) one shared three-fragment excerpt; after the review
  only R4 keeps `opened` (excerpt narrowed to the communal-sleeping passage), and R1, R3, R5 are set by hand to
  `recalled` for the rule (the page was read; what was quoted does not state the rule), quote kept in the note.
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
| police-crisis R7 | WIC 5152 opened; WIC 5150(a) recalled (**raise**: absent -> recalled) | 5150(a) is cited for the absence of an officer release duty; the excerpt keeps the release-only-if passage that `(not (danger s))` stands for |
| cps R7 | WIC 361(c)(1) opened | pin and excerpt tidied |
| companion-ownership R1, companion-guardian-renamed R1 | Civ. 655 opened, 663 opened (**raise** each: recalled -> opened), 658 recalled (+ R.I. 4-13-41 recalled, effective_date null, on renamed) | Penal 597s is named only as the dropped citation; s. 658 cited without a read record; R.I. cited for the role name, not the rule ("P.L. 2001 ch. 72" is a session law, not an effective date) |
| companion-guardianship R9 | Alaska 25.24.160(a)(5) unverified + null unverified (the generalisation) | the row says "UNVERIFIED (general knowledge; no source opened)" though it quotes the statute and the entry's source_text says read; kept the lower level |
| public-library R2 | Berkeley policy recalled + null unverified | "UNVERIFIED as a rule": the duty to serve is read from the policy's premise |
| naming-convention R1, R2 | Centola et al. 2018 unverified | "cited from memory" and "UNVERIFIED as a quotation": the lower of the two |
| kibbutz-childrens-house R1 | Wikipedia recalled, null unverified | the page was read (2026-11-03) but no quoted passage mentions a committee or an assignment; the committee assignment is the encoder's parenthesis (review finding 2) |
| kibbutz-childrens-house R2 | Wikipedia recalled (**raise**: unverified -> recalled), Tiger & Shepher unverified, Kirkus recalled (**raise**: unverified -> recalled) | three works at three levels; this row records no read of the Wikipedia quote (R1's row does); the row's UNVERIFIED belongs to Tiger & Shepher's finding |
| kibbutz-childrens-house R3 | Wikipedia recalled | read, but the quotes support the metapelet's duty only indirectly (a nanny position existed) (finding 2) |
| kibbutz-childrens-house R4 | Wikipedia opened, excerpt "lived in the children's house, where they had communal sleeping arrangements" | the one passage that states the rule (finding 2) |
| kibbutz-childrens-house R5 | Wikipedia recalled, null unverified | read, but the quote says children visited their parents, not that a male member may visit the child (finding 2) |
| kibbutz-childrens-house R6 | Spiro unverified, Gavron unverified, null unverified | tidied notes; the implicit rule ("UNVERIFIED (general knowledge)") gets its own null item (finding 14) |
| airline-flight R2 | 14 CFR 121.571 opened (**raise**: unverified -> opened), 121.391 recalled, null unverified | the string says the general in-flight care duty is UNVERIFIED (no text opened states it); 121.391 is quoted with "read at <url>" but no read date, and 121.571's date is not borrowed (finding 10); it supports egress only |
| mwpa-creditor-exemption R11 | heuristic items + null unverified | the Mississippi 1839 act is named only through Khan, as R14-R16 name theirs through GLT (finding 6) |
| mwpa-creditor-exemption R12 | Chused 1984 recalled, Chused 1983 unverified, Blackstone recalled (pin null), null unverified | Blackstone's bar on grants is cited; the pin "Bk I ch 15" is inferred, not in the string, so it is in the note; the conveyance is "UNVERIFIED as a rule of the 1839-50 acts" |
| mwpa-property R13 | NY MWPA 1848 unverified (effective_date null), GLT recalled | GLT is named twice; the statute text not opened ("[R] UNVERIFIED"); 1848 is the short-title year, not a stated effective date |
| mwpa-suit R16 | MWPA 1882 s. 1(2) opened (effective_date null), GLT recalled, null unverified | the heuristic lifted the old R9 wording ("may sue when not married") into GLT's note; 1882 is the short-title year, not a stated effective date |
| footbinding R1 | Mackie snippet + null unverified | abstract quotes as a search-index snippet; the rule itself "UNVERIFIED as a rule" |
| footbinding R3 | Mackie snippet + null unverified | implicit sanctioned norm (see above) |
| footbinding R4 | three Wikipedia pages recalled, Mackie recalled (no excerpt, accessed null) | "search snippets only, pages not opened: [R]" -> the lower of snippet and [R]; Mackie: "abstract [F]" relayed with no quote and no read date in this row -> recalled (finding 1; was snippet with a date borrowed from the Wikipedia clause) |
| footbinding R10 | as R4 + null unverified (**raise**: Tian Zu Hui and Heavenly Foot Society unverified -> recalled, Mackie unverified -> recalled) | the rule is reconstructed ("UNVERIFIED"); that UNVERIFIED belongs to the reconstruction, not to the works' clause |
| footbinding R5, R6 | Mackie snippet, Wikipedia pages recalled, null unverified | "UNVERIFIED ... as a rule" |
| footbinding R7 | Mackie snippet, Brown et al. 2012 recalled | Brown: abstract-only search snippet tagged [R] |
| ectogenesis R1, R2, R3 | Firestone 1970 unverified | "from memory" and "UNVERIFIED: no text opened": the lower |
| ectogenesis R4, R5, R6, R7 | null, unverified (R5: + a null item for the Kleven finding) | Firestone is named only in the boilerplate ("no text opened for this rule"); no work supports these rows; R5 names "the Kleven finding in docs/theory.md" with no citation (finding 6; a search lead for the citation is in `plans/sourcing-worklist-other.md`) |

## Items raised above the heuristic (hand settings, each licensed by its own row's string)

The heuristic misses a read claim that follows the quotes, or applies a row-wide `UNVERIFIED` that belongs to a
different clause. These 11 items in 6 rows are set above its level by hand. `RAISES` in the script holds the same
list with the licensing clause in full, and the script stops if the computed raises and the list differ.

| row | work | heuristic -> hand | licensing clause of the row's string |
|---|---|---|---|
| police-crisis R7 | Cal. WIC 5150(a) | absent -> recalled | "s. 5150(a) (https://california.public.law/...section_5150, cited here until 2026-11-04) gives the officer custody and delivery (R3), no release duty": cited with a URL, no read record (the heuristic's regex misses the bare "s. 5150(a)") |
| companion-ownership R1 | Cal. Civ. 655 | recalled -> opened | "Read 2026-11-04 at https://codes.findlaw.com/ca/civil-code/civ-sect-655/ ..." after the quote "There may be ownership ... of all domestic animals" |
| companion-ownership R1 | Cal. Civ. 663 | recalled -> opened | the same read claim names .../civ-sect-663/, after the quote "Every kind of property that is not real is personal" |
| companion-guardian-renamed R1 | Cal. Civ. 655, 663 | recalled -> opened (2 items) | same string as companion-ownership R1 |
| kibbutz-childrens-house R2 | Wikipedia (WIKI_KIB) | unverified -> recalled | quotes "was always a woman's role" with no read record; the UNVERIFIED belongs to "the assignment finding itself NOT read directly" |
| kibbutz-childrens-house R2 | Kirkus review | unverified -> recalled | "book and sample (34,040 members) confirmed via Kirkus review <url>" (no quote); the UNVERIFIED belongs to Tiger & Shepher's finding |
| airline-flight R2 | 14 CFR 121.571 | unverified -> opened | "read 2026-11-04 at https://www.law.cornell.edu/cfr/text/14/121.571 ...: (a) 'shall insure that all passengers are orally briefed by the appropriate crewmember'"; the UNVERIFIED belongs to the general in-flight care duty (its own null item) |
| footbinding R10 | Wikipedia 'Tian Zu Hui', 'Heavenly Foot Society' | unverified -> recalled (2 items) | "read 2026-11-04 as search snippets only, pages not opened: [R]"; the closing UNVERIFIED belongs to the reconstructed rule (its own null item) |
| footbinding R10 | Mackie 1996 | unverified -> recalled | "Mackie 1996 names the same two-part pledge for the FGC analogue, abstract [F]": [F] relayed, no quote, no date = recalled (was snippet until the review, finding 1) |

## Jurisdiction mismatches (flagged, not fixed)

The MWPA chain encodes US state acts (GLT / Khan: NY, MA, PA, ME ...), but:
- every `mwpa-*` entry inherits coverture R2, R4, R5, R7 (where not dropped) sourced to Blackstone Book I ch. 15
  (England), and R6 sourced to Shanley 1989 and Stone 1990 (Victorian England; exit before the English Matrimonial
  Causes Act 1857). Resolved rows: mwpa-creditor-exemption R1 (Bk II ch 29), R2, R4, R5, R6, R7; mwpa-property R2,
  R4, R5, R6, R7; mwpa-earnings R2, R4, R5, R6, R7; mwpa-sole-trader R2, R4, R5, R6; mwpa-suit R2, R5, R6;
  mwpa-property-narrowed R2, R4, R5, R6, R7 (28 resolved rows; with R12 in six entries and R16, 35).
- mwpa-creditor-exemption R12 (and every entry inheriting it) cites Blackstone's bar on grants between spouses (England).
- mwpa-suit R16 cites the Married Women's Property Act 1882 (45 & 46 Vict. c. 75), a UK act, for a US suit provision
  (GLT: e.g. NY 1860). Its `jurisdiction` is `UK` because its citation (ukpga) names the UK Parliament; Blackstone's
  items are `England` because his title names the Laws of England. Convention: the jurisdiction the citation names.
  The 1882 Act's territorial extent (the reviewer recalls it does not reach Scotland) is not in repo text and is
  unverified; it changes no rule.
- crisis-team R8 cites Cal. Welf. & Inst. Code 5150(a) (US-CA) for the officer's custody power in an entry modelled on
  Denver STAR (Colorado; the KUNC article).
- Mixed but declared: companion-guardianship R9 (Alaska) on a California base (companion-ownership: Cal. Civ. 655/663,
  Penal 597s); companion-guardian-renamed R1 adds R.I. 4-13-41 for the role name; transferable-leave R2 combines
  Canadian EI (federal) with Quebec's QPIP as a minimal-pair construction.

## Works named in source strings that are not mapped to the bibliography

- Matrimonial Causes Act 1857 (coverture R6): named as the subject of Shanley / Stone, not cited as a source.
- The US state acts named through GLT / Khan: NY 1860, MA 1846/1874, PA 1872 (R14 earnings); ME 1844, MA 1860,
  NY 1860 (R15 sole trader); NY 1860 (R16 suit); Mississippi 1839 (R11, via Khan). Recorded as `source_id: null`
  items (R11, R14, R15, R16); no entries, since no title or text is in the repo. (The NY, MA, ME, PA, MD and IL acts
  have lead-only entries in `data/sources/backtests.yaml` for the ground truth; the rows do not cite them yet.)
- NYHS WAMS coverture page: used as the `url` of the Blackstone Book I ch. 15 items, not a separate work.
- "the Kleven finding in docs/theory.md" (ectogenesis R5): no citation in the row or in docs/theory.md; recorded as a
  `source_id: null` item. A search lead for the citation (Kleven, Landais & Søgaard 2021) is in
  `plans/sourcing-worklist-other.md`; add an entry when it is opened.
- "the third review's 6-rule sketch" (airline R1, R3, R4, R6), `plans/ectogenesis.md`, `plans/backtest-mwpa.md`,
  ADRs: internal documents, not works.
- "state surrogacy acts vary" (gestational-surrogacy R2, R3), "local animal-control impound" (companion R7),
  "general peace-officer powers" (police R5): no work named.
- Dropped citations named only to say they no longer apply: coverture R1 (Bk I ch 15), companion R1 (Penal 597s),
  airline R2 (14 CFR 91.11 / 121.580). Not given items on those rows.

## Bibliography gaps (not in repo text; null in data/sources/rules.yaml)

Given names (Shanley, Stone, Spiro, Gavron, Tiger, Shepher, Mackie, Centola and co-authors, Brown and co-authors);
the title and container of Chused 1984 (the title is a descriptive placeholder); URLs of the three
Wikipedia pledge pages, Shanley, Stone, Spiro, Gavron, Tiger & Shepher, Brown et al., Firestone, Cal. WIC 317 / 328 /
5275 / 16501, Penal 597 / 11165.14, Civ. 658, 14 CFR 91.11 / 121.580; enactment years of the California, Quebec and
CFR sections.

Filled from search leads or an earlier batch's [F] read, not from repo text, when the backtest bibliography's entries
were merged in (see the rules.yaml header; each note says which, after "| merged from"): GLT 2007's title (assumed
equal to the 2012 article's) and given names; Khan's given name, container and pages (RePEc lead); Chused's given
name; Chused 1983's title, container and URL (several agreeing leads); NY 1848's title, chapter (ch. 200) and URL
(merged from `us-ny-laws-1848-ch200`, which is retired). These are unconfirmed until the work is opened.

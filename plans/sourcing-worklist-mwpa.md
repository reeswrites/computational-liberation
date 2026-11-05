# Sourcing worklist: MWPA backtest

Status: open (2026-11-05). Contract: `plans/sourcing.md`. Ground truth: `data/backtests/mwpa-ground-truth.yaml` (40 events: 8 `conflict`, 32 `unresolved`, 0 `settled`; MS-property moved from conflict to unresolved on 2026-11-05, review finding 5). Bibliography: `data/sources/backtests.yaml`, plus the works also cited by rules (GLT 2007, Khan 1996, Chused 1983/1984, NY 1848 `ny-mwpa-1848`), merged into `data/sources/rules.yaml`.

How this list was made. The 2026-11-05 session could search but not fetch: every URL below is a **lead**, found by WebSearch, whose result is a model-written summary, not the source. Nothing here was opened, so no item is above `recalled` (GLT 2007 draft and Khan 1996, opened in an earlier session with no excerpt kept) and every statute item is `unverified`. Each lead names the query that found it. Whoever opens a source: record `verification: opened`, a short `excerpt`, `accessed`, and the `url` actually read on the matching provenance item; then apply the settling rule in `plans/sourcing.md` (one opened item reporting the date, or two independent opened secondary works agreeing).

## Ordered checklist

Order: the items that settle the most events first.

### 1. Geddes & Tennyson 2013 (corrected dates, all states) — settles or narrows every event

- [ ] Open the corrected table. Leads:
  - Paywalled chapter: https://emerald.com/insight/content/doi/10.1108/S0363-3268(2013)0000029007 (query: `Geddes Tennyson 2013 "Passage of the Married Women's Property Acts and Earnings Acts in the United States: 1850 to 1920" Research in Economic History`). Needs a library login.
  - Published companion article, Geddes, Lueck & Tennyson, J. Law & Econ. 55(4) 839-867 (2012): https://chicagounbound.uchicago.edu/jle/vol55/iss4/5/ (query: `Geddes Lueck Tennyson "Human Capital Accumulation and the Expansion of Women's Economic Rights" Journal of Law and Economics`). Chicago Unbound often hosts JLE PDFs openly; unconfirmed. A 2018 Cambridge article is said to cite this article for its dates, so its table may carry the corrected dates.
  - Possible open copies that may reproduce the corrected dates (unknown content): https://topcat.aeaweb.org/conference/2014/retrieve.php?pdfid=1108 (surfaced by both the G&T and Chused queries; a 2014 ASSA paper on the acts), https://afse2017.sciencesconf.org/143660/Women_s_Economic_Rights.pdf (query: `Geddes Lueck Tennyson 2012 "Human Capital Accumulation" women's economic rights pdf SSRN OR working paper table dates of property acts earnings acts`), McDevitt & Irwin, Social Science History (2017) open PDF https://cambridge.org/core/services/aop-cambridge-core/content/view/531DD79AF39B315CA70305C5BCC72C9B/S0145553217000050a.pdf/narrowing_of_the_gender_wealth_gap_across_the_nineteenthcentury_united_states.pdf (query: `"narrowing of the gender wealth gap across the nineteenth-century United States" ...`).
- Look for: the per-state table of property-act and earnings-act years, and the footnotes saying which statute each year codes (needed for the classification conflicts below).
- Settles: every `*-property` and `*-earnings` event (with one other opened item, or alone if the statute is opened). Resolves ME-property, MA-property, MA-earnings, MD-property, MD-earnings, IL-earnings; dates MS-property (unresolved: only GLT reports a date).
- Record as: new provenance item `source_id: geddes-tennyson-2013-reh` (or `glt-2012-jle`), `date_reported` per state.

### 2. GLT 2007 draft and Khan 1996: re-open and keep excerpts — upgrades every `recalled` item

- [ ] https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf, Table 1. Record an excerpt (the table row) per state on each `geddes-lueck-tennyson-2007` item. For MD, look at the page image, not the text layer: is the earnings year really 1842? (resolves the "OCR-suspect" flag on MD-earnings).
- [ ] https://www.laits.utexas.edu/~mbs31415/Khan_MarriedWomenPropertyRights.pdf, Table 1 and its notes. Excerpt per state on each `khan-1996` item. Look for: whether ME 1844 codes the 1844 property act as a sole-trader act (ME-sole_trader note); what Khan's MA 1874 and IL 1861 earnings dates refer to; Khan's MS treatment of 1839 (MS-property); whether PA's 1718 feme-sole-trader act is excluded by design (PA-sole_trader note; recalled, not searched).
- Settles: nothing alone (both are secondary and they disagree where it matters), but turns `recalled` into `opened` so that item 1 plus one of these can settle the non-conflict events.

### 3. Maine (ME-property conflict 1855 vs 1844; ME-earnings; ME-sole_trader)

Maine's legislature hosts scanned session laws, one PDF per chapter (`lldc.mainelegislature.org/Open/Laws/<year>/<year>_PL_c<NNN>.pdf`).
- [ ] 1844: https://lldc.mainelegislature.org/Open/Laws/1844/1844_PL_c117.pdf and https://lldc.mainelegislature.org/Open/Laws/1844/1844_PL_c116.pdf (query: `Maine 1844 act married women property "chapter 117" laws of Maine`). The summary says courts cite "c. 117" (Swift v. Luce, 1847: act of 22 March 1844), but the archive's c116 file carries the married-women title and the Legislative Index lists PL ch. 93. Look for: "An Act to secure to married women their rights in property", whether s. 1 lets her hold property as her own, and whether it lets her trade (Khan's sole-trader 1844). Fix the chapter number in `us-me-laws-1844-ch117` (rename the id if it is not 117).
- [ ] 1855: https://lldc.mainelegislature.org/Open/Laws/1855/1855_PL_c120.pdf (URL built from the archive pattern; not seen in results) (query: `Maine 1855 act "married women" property rights chapter 120 ...`). Beale v. Knowles (1858) quotes it: "any married woman seized and possessed in her own right of any real estate ... (might) sell, convey and dispose of the same by her separate deed". Also https://lldc.mainelegislature.org/Open/Laws/1855/1855_PL_c119.pdf and `_c121.pdf` if the numbering is off.
- Settles ME-property and decides which power R13 (`mwpa-property`: wife may hold_property) codes: 1844 = hold, 1855 = convey by her own deed. If R13 means "hold and control as a feme sole", the act that first gives control (possibly 1852 or 1855) is the date; if it means "hold", 1844.
- [ ] 1857: https://lldc.mainelegislature.org/Open/Laws/1857/1857_PL_c059.pdf; R.S. 1857 c. 61 https://lldc.mainelegislature.org/Open/RS/RS1857/RS1857_c061.pdf (query: `Maine 1857 married women earnings "personal labor" act chapter laws of Maine`). Look for "may demand and receive the wages of her personal labor". Settles ME-earnings (with GLT). Also check https://lawcat.berkeley.edu/record/1290883 (an 1854 act "to secure to married women their earnings", state unconfirmed): if Maine, ME-earnings becomes a conflict (1854 vs 1857).

### 4. Massachusetts (MA-earnings conflict 1846 vs 1874; MA-property and MA-sole_trader classification conflicts)

- [ ] St. 1855 c. 304, "An Act to protect the property of married women": catalogue record https://archives.lib.state.ma.us/entities/archivalmaterial/ba76b66e-bf4d-4429-9a40-6a1846fa45b8 (query: `Massachusetts 1855 chapter 304 "An Act to protect the property of married women" earnings "sue and be sued" text`). Look for ss. 1 (separate estate), 3 (sue and be sued as if sole; "nothing herein contained shall authorize suits between husband and wife"), 7 (trade, labour and earnings on her separate account). The Acts and Resolves volumes are also on the State Library's DSpace (search there for "Acts 1855 chap 304").
- [ ] St. 1845 c. 208 (query: `Massachusetts 1845 act "married women" property chapter 208 Acts and Resolves 1845`): no copy surfaced; open the 1845 Acts and Resolves. Look for: is it limited to property held under a written pre-nuptial contract through a trustee (as the 1848/1861 SJC opinions are summarised)? If so it is a settlement act, not R13, and MA-property should move to 1855.
- [ ] St. 1874 c. 184 s. 1 (query: `Massachusetts 1874 chapter 184 married women earnings "separate property" act Acts 1874`); Hawkins v. Providence & Worcester R.R. (1876) https://hallapproved.com/ma/cases/supreme/1876/6544714/. Look for the presumption that her labour for others is "on her separate account".
- [ ] Search the 1846 Acts and Resolves for any married-women earnings chapter. A search found none; if there is none, GLT's 1846 is a draft error.
- Settles: MA-property (1845 vs 1855), MA-earnings (1846 vs 1855 vs 1874), MA-sole_trader (1855 vs 1860). The three earnings candidates encode different rules (no act; may elect separate account; default presumption): which one R14 (`mwpa-earnings`: wife may keep_earnings) means must be written down before the date is chosen.

### 5. Illinois (IL-earnings conflict 1869 vs 1861)

- [ ] Laws 1869, p. 255 (act of 24 March 1869) and Laws 1861, p. 143 (act of 21 Feb 1861) (query: `Illinois 1861 married women property act "February 21, 1861" separate property; Illinois 1869 act married women earnings "March 24, 1869"`). Copies: volume guide https://wiu.edu/libraries/govpubs/illinois_laws/1860_1869.php; HathiTrust https://catalog.hathitrust.org/Record/100671722 (viewability unknown); archive.org scans of the 1861 public laws are reported (query: `HathiTrust "Laws of the State of Illinois" 1861 OR 1869 session laws full view; ...`).
- [ ] Case corroboration (secondary, settles nothing alone): https://syfert.com/caselaw/case.php?id=7053430 (describes s. 1 of both acts); Hanchett v. Rice, 22 Ill. App. 442 https://cap-redacted-demo.lil.tools/ill-app/22/html/0442-01.html ("married women did not become entitled to their own earnings until the 1869 act", per summary); Howarth v. Warmser (1871).
- Settles IL-property (1861) and IL-earnings. Every lead points to 1869 for earnings; Khan's 1861 probably codes the property act.
- [ ] R.S. 1874 p. 576 (husband and wife, 30 March 1874), modern text with source line https://www.ilga.gov/ftp/ILCS/Ch%200750/Act%200065/075000650F.html (query: `Illinois "act to revise the law in relation to husband and wife" 1874 ...`). Settles IL-sole_trader with Khan; also a US source for R16 (sue as if single).

### 6. Maryland (MD-earnings OCR-suspect 1842; MD-property classification conflict)

- [ ] 1842 session ch. 293 "An act to regulate conjugal rights as they regard property" (passed 10 March 1843), Archives of Maryland vol. 594: https://msa.maryland.gov/megafile/msa/speccol/sc2900/sc2908/000001/000594/html/am594--254.html and `--255.html` (query: `Maryland 1842 chapter 293 married women property act; Maryland 1860 married women earnings act laws of Maryland`). Look for: s. 1 (hold property, real or slaves, in her own name), the husband's retained marital rights, and s. 8 (does it reach the proceeds of her labour?).
- [ ] Code of 1860, Art. 45 (Husband and Wife): Archives of Maryland annotation pages surfaced, e.g. https://msa.maryland.gov/megafile/msa/speccol/sc2900/sc2908/000001/000389/html/am389--799.html (query: `Maryland Code 1860 Article 45 ...`). The summary mixes editions (it also says business powers came only in 1898); read the 1860 text itself.
- Settles MD-property (1843 vs 1860), MD-earnings (1842/43 vs 1860), MD-sole_trader (1860 vs 1898?). Surprise: the leads say 1842 is a real Maryland statute year, so GLT's "1842" may not be an OCR error at all; the question is whether 1842 ch. 293 is a property act in R13's sense (the cases say the husband kept his marital rights: closer to the Capture form, `mwpa-creditor-exemption`).

### 7. New York (all unresolved; NY-suit conflict 1860 vs 1862)

- [ ] Laws 1848 ch. 200 (`ny-mwpa-1848`, in `data/sources/rules.yaml`; also cited by `mwpa-property` R13; passed 7 April 1848): transcription https://www.houseofrussell.com/american-legal-history/docs/laws-of-new-york-chap-200.pdf; NY State Archives https://digitalcollections.archives.nysed.gov/index.php/Detail/objects/10821; Rochester copy of the 71st-session laws https://rclomeka2.lib.rochester.edu/items/show/485 (query: `New York Married Women's Property Act 1848 "chapter 200" laws of New York 1860 "chapter 90" earnings act text`). Prefer the archive scan over the course transcription. Settles NY-property (with GLT).
- [ ] Laws 1860 ch. 90 (passed 20 March 1860): https://www.houseofrussell.com/american-legal-history/assignments/laws-of-new-york-83d-sessio.html. Look for s. 2 (trade on her own account; earnings her separate property) and s. 7 (sue and be sued in matters relating to her property). Settles NY-earnings, NY-sole_trader.
- [ ] Laws 1862 ch. 172: https://www.houseofrussell.com/american-legal-history/docs/laws-of-new-york-85th-sessi.pdf (query: `New York 1860 act "rights and liabilities of husband and wife" section 7 ...`). Compare the suit clause with 1860 s. 7. Settles NY-suit and supplies the US source for R16 (below).

### 8. Pennsylvania (all unresolved)

- [ ] Act of 11 April 1848, P.L. 536, No. 372, ss. 6-11; Act of 3 April 1872, P.L. 35, No. 24 (query: `Pennsylvania act "April 11, 1848" married women property P.L. 536; Pennsylvania act "April 3, 1872" married women earnings P.L. 35`). Citation page: https://crawfordcopa.com/court/mw. Pamphlet Laws scans: try the Pennsylvania Legislative Reference Bureau / State Library session-law archive, HathiTrust ("Laws of the General Assembly of the Commonwealth of Pennsylvania 1848"), or Google Books. Look for s. 6 "shall continue to be the property of such woman" and the 1872 earnings clause. Settles PA-property, PA-earnings.
- Note for Backlash: an 1856 Pennsylvania decision is summarised as holding the 1848 act "preserved married women's estates but did not remove the disabilities created by marriage", and Diver v. Diver that "the unity of husband and wife was not destroyed" by it. Candidate US evidence for `mwpa-property-narrowed` R17/R18 besides Chused.

### 9. Chused 1983 (BL/Capture rules R11, R12, R17, R18)

- [ ] 71 Geo. L.J. 1359, p. 1400: NYLS Digital Commons https://digitalcommons.nyls.edu/fac_articles_chapters/280 (query: `Chused "Married Women's Property Law: 1800-1850" 71 Georgetown Law Journal 1359 pdf`). The repository page is the best open-copy lead; it dates the item 1982. Look for: the "narrowly construing" passage at 1400 and Chused's table of passage dates (a Library of Congress guide says the article "provides passage dates and statistics").
- Settles: provenance for `mwpa-property-narrowed` R17/R18 and `mwpa-creditor-exemption` R11/R12 (now via Chused 1984 citing 1983); a third independent date list for every 1800-1850 event (ME, MA, MD, MS).

### 10. Remaining unresolved events

WI, NJ, OH, CA, IN, TX property/earnings and the sole-trader events: settle from item 1 plus item 2 (two independent opened secondary works agreeing), or from the session law. No statute leads were searched for these states this session.

## Jurisdiction mismatch

The US chain cites English law in two places. Both affect rules, so (unlike dates) they can change verdicts.

Status 2026-11-05: B3 with B1 done (`coverture-household-us`, US leads on R6 at `unverified`) and A2 done (`mwpa-suit` R16 re-sourced to NY 1860/1862 and MA 1855, new R19 bars suits between spouses); A3 not taken; B2 later. Preregistration and results: plans/sourcing.md "Coverture split and US suit". The leads below still need opening to move any row above `unverified`.

### A. `mwpa-suit` R16 (may sue while married), now cited to the UK Married Women's Property Act 1882 s. 1(2)

US candidates found (all leads):
1. NY Laws 1860 ch. 90 s. 7: may sue and be sued "in all matters having relation to her property"; Longendyke (1863): not against her husband for assault or slander. Broadened by Laws 1862 ch. 172.
2. MA St. 1855 c. 304 s. 3: may sue and be sued as if sole, but "nothing herein contained shall authorize suits between husband and wife"; s. 7 for trade and earnings.
3. IL R.S. 1874 p. 576 s. 1: sue and be sued as if single; whether this covered suits against the husband stayed contested until Brandt v. Keller (20th c.).
4. MD 1842 ch. 293 s. 8: may sue to protect her property "as fully as if she were a feme sole" (per annotation summary).

Options:
- **A1, re-source only.** Cite NY 1860 ch. 90 s. 7 (and 1862 ch. 172) on R16, keep R16 unconditional. No rule change; no verdict change. Honest only if the plain text says R16 is read at its broadest (1862), since 1860 s. 7 is scoped to property matters.
- **A2, re-source and scope.** Every US candidate bars or omits suits between spouses. Encode R16 as `wife may sue (other than husband)` (a condition or a narrowed action), and leave R4's disability standing against the husband. This changes `mwpa-suit` R16 (and possibly R4 kept in part). `has_standing` as derived from `sue` enabled would need either a split fluent (standing against third parties vs against the husband) or a condition; the preregistered direction test ("`suit` flips `has_standing` true") would hold for third-party standing only. Log as drift in `plans/backtest-mwpa.md`.
- **A3, split.** Keep the current chain as an English entry (`mwpa-suit-uk-1882`, keeping the legislation.gov.uk citation) and build the US entry under A2. Doubles the R16 rows; clean jurisdiction per entry.

### B. `coverture-household` R6 (no exit: a disability on `leave` while married), sourced to English law (Shanley 1989, Stone 1990; Matrimonial Causes Act 1857)

What the leads say: US states had judicial divorce on fault grounds throughout the MWPA period, varying by state. New York's 1787 act allowed absolute divorce for adultery only, until the 1966 reform (query: `New York 1787 divorce statute adultery only ground "absolute divorce" nineteenth century until 1966 Divorce Reform Law`; https://en.wikipedia.org/wiki/New_York_divorce_law and the Law & History Review article https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B088017E56095497158508048C776283/S0738248000010440a.pdf/relief_in_the_premises_divorce_as_a_womans_remedy_in_new_york_and_indiana_18151870.pdf); South Carolina had no divorce statute at all; Basch, *Framing American Divorce* (1999) describes a fault system (query: `nineteenth century United States divorce law ... Basch ... Hartog ...`). Unilateral (no-fault) divorce arrives by state from 1969 (Stevenson & Wolfers, QJE 121(1) 2006, NBER w10175 https://www.nber.org/system/files/working_papers/w10175/w10175.pdf, opened per `plans/backtest-data-inventory.md` [F]; query: `Stevenson Wolfers "Bargaining in the Shadow of the Law" ...`).

Options:
- **B1, read R6 as "no unilateral exit" and re-source to US.** Cite Stevenson & Wolfers (no unilateral divorce before 1969 in any state) plus one state fault statute (NY 1787). Rule text unchanged; plain text changes from "no exit" to "no exit at her own will". No verdict change. Weakness: R6 as encoded is unconditional, which overstates the US position wherever the husband's fault opens exit.
- **B2, encode fault divorce.** Replace R6 with a conditional disability (`wife must_not leave unless fault(h)`, or `may leave` conditioned on a proved ground), with a free action that sets the fault condition (as R5 does with `misbehave`). `can_exit` / `subject_cannot_exit` would become reachable-under-condition rather than blocked in coverture and every MWPA entry that inherits R6; the preregistered "`can_exit` does not flip" still holds at the delta level (no MWPA delta touches R6) but the coverture baseline verdicts change. Needs drift notes in `plans/backtest-mwpa.md` and the coverture rows of `docs/claims.md`.
- **B3, split.** `coverture-household` stays English (Blackstone R1/R2/R4/R5/R7 and the English R6, which fits England before 1857: divorce only by private Act of Parliament), and a new `coverture-household-us` (base of the MWPA chain) carries B1 or B2. Most faithful; most rows. Note R1, R2, R4, R5, R7 also cite Blackstone (English); Blackstone was received in the US, but a US treatise (e.g. Kent's Commentaries, recalled, not searched) would be the jurisdiction-correct citation for the US base.

Recommendation for the author, not made here: B1 is the minimum honest fix; B3 with B2 is the faithful one. A2 is needed under every option for R16, because no US act found grants standing against the husband.

## What a corrected date changes

The layer-1 direction test reads rules, not dates: no date below changes a layer-1 verdict. Dates feed (i) the parked ordering test (layer 3, plan §3) and (ii) the launch table, and (iii) which failure-mode window (1839-50 Capture; 1860-80 Backlash, plan §4) a state falls in.

Plan §3 predicts property and suit rights precede measured married-women's LFP and patenting in ≥ 8 of 10 early states. The measured series: married LFP from 1890 only (Goldin); women's patenting low before 1860, rising after (Khan). Every candidate date found lies before 1890, so **no correction moves a state against the LFP comparison**; only the 1860 patenting boundary can move. The plan names nine early states (MA, NY, PA, WI, NJ, ME, MD, OH, IL); the tenth is unnamed: fix it before running.

| Event | Candidates | Moves across 1860 (patenting)? | §3 count | Window (failure mode) |
| --- | --- | --- | --- | --- |
| ME-property | 1855 (GLT) / 1844 (Khan, 1844 c. 117) | no, both before | unchanged | 1844 puts ME in the 1839-50 Capture window; 1855 in neither |
| MA-property | 1845 (GLT, c. 208) / 1855 (c. 304) | no | unchanged | 1845 in 1839-50; 1855 in neither |
| MD-property | 1860 (GLT) / 1843 (1842 ch. 293) | yes: from the boundary year to clearly before | +1 rule-first at most | 1843 in 1839-50 (and ch. 293 kept the husband's marital rights: Capture-like) |
| MS-property | 1871 (GLT) / 1839 (excluded by Khan as debt relief) | yes, if 1839 counts as a property act | +1 if MS is the tenth state | 1839 is the Capture form by construction |
| MA-earnings | 1846 / 1855 / 1874 | 1846, 1855 before; 1874 after | not in §3 (earnings) | 1846 in 1839-50; 1874 in 1860-80; also changes plan §1 ("1860-1879 earnings acts overlap the patenting rise") |
| IL-earnings | 1869 / 1861 | both at or after 1860 | not in §3 | both 1860-80 |
| MD-earnings | 1842 / 1843 / 1860 | 1842-43 before; 1860 boundary | not in §3 | 1842-43 in 1839-50 |
| NY-suit | 1860 / 1862 | both after 1860 | suit vs LFP>10% (1930): holds either way | 1860-80 |

Net: every candidate correction found either leaves the §3 count alone or adds a rule-first state (MD, MS). None moves a state toward material-first. The corrections matter more for the failure-mode windows: ME, MA and MD each move into or out of the 1839-50 Capture window depending on which act is coded, which is the window the §4 failure-mode test reads. The adoption-predictor side ("material-before-rule on adoption predictors", G&L 2002, HWZ) uses adoption years as the outcome; a shift of 10+ years for ME, MA or MD changes the covariates (wealth, urbanisation, TFP at adoption) for those states and should be rerun with G&T 2013 dates.

Launch table: until item 1 is done, show the eight `conflict` events with both dates, not the GLT draft date alone, and MS-property's 1839 candidate (Khan names the act and excludes it; not a date Khan reports).

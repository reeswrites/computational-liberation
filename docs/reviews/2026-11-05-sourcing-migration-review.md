# Council review: honesty of the provenance migration (branch claude/sourcing-citation-overhaul-ax7rv8), 2026-11-05

Fresh agent on the encoding-faithfulness and migration-honesty seat (ADR 0014). I did not build this. Read-only and offline, because network fetches are blocked: the repo is checked against itself. I read the `source` string and the `provenance` list of all 121 own rules in `data/institutions/src/*.yaml` (`rules`, `rules_add` and `rules_replace`), along with `migrate_provenance.py` (heuristic and OVERRIDES), both bibliography files, `data/backtests/mwpa-ground-truth.yaml`, `plans/sourcing.md`, ADR 0017, `plans/backtest-mwpa.md` and `tests/test_sources.py`. I compared against `provenance-migration-report.md` only after forming these findings. Scripts and throwaway fixtures stayed in my scratch directory, and no repo file other than this one was written.

**Verdict: weakened.** The migration is mostly honest. All 20 excerpts (15 `opened`, 5 `snippet`) appear verbatim in their row's string, up to whitespace. No row's weakest level is above what its string records. Every UNVERIFIED string maps to `unverified`, and no ground-truth event is `settled`. But two items sit above their string (1). The hand-override layer claims it "only ever lowers", which is false for six rows (3). Three `opened` rows rest on an excerpt that does not state the rule (2). The CI checks miss several cases they exist to catch (7).

Mechanical checks:
- I re-ran `migrate_rule` on every rule and it reproduces the files (0 diffs).
- I compared every override with the heuristic's output.
- `uv run pytest -q tests/test_sources.py` gives 9 passed.

## Findings

1. **[critical] footbinding:R4 and footbinding:R10, item `mackie-1996` at `snippet` with no excerpt.** These rows' strings say only "Mackie 1996 names the same two-part pledge for the FGC analogue, abstract [F]". They record no quote and no read date (the `accessed: 2026-11-04` is borrowed from the Wikipedia clause). The item's own note says the readings this row uses ("two-part pledge", "critical mass") come from the body, [R]. Three rules all put this at `recalled` or lower:
   - a read with no quote is at most `recalled` (plans/sourcing.md);
   - an `[F]` tag relayed second-hand becomes `recalled` (the script's own rule for GLT, Khan and Chused);
   - the other abstract-only snippet tagged [R] (Brown et al., R7) was set to `recalled`.

   On R10 the override raised it: the heuristic said `unverified`, the hand setting says `snippet`. Neither row's weakest level changes, because both carry lower items, so no claim count moves. Fix: `recalled`, `accessed: null`.

2. **[major] kibbutz-childrens-house:R1, R3, R5. The `opened` excerpt does not support the rule.** One three-fragment excerpt is pasted on R1, R3, R4 and R5: "The nanny position was always a woman's role ... lived in the children's house ... visited their parents for 2-3 hours a day".
   - R1 ("committee may assign a member to the children's house"): nothing quoted mentions a committee or assignment. That part is the encoder's parenthesis in the string.
   - R5 ("a male member may visit the child"): the quote says children visited parents, not the reverse.
   - R3 (metapelet must care when assigned): supported only indirectly.
   - R4 (communal sleeping) is supported.

   These are 3 of the 7 own rows whose weakest item is `opened`, so check 5 would count claims on them as resting on opened text. Fix: choose an excerpt per row, and add a `source_id: null` unverified item for the part no quote states (R1's committee assignment).

3. **[major] migrate_provenance.py docstring: "Hand settings only ever lower a level or add a lower item" is false.** Six overrides set an item above the heuristic's level:
   - companion-ownership:R1 and companion-guardian-renamed:R1: Civ. 655 and 663, `recalled` to `opened`;
   - airline-flight:R2: 121.571, `unverified` to `opened`;
   - kibbutz-childrens-house:R2: Wikipedia and Kirkus, `unverified` to `recalled`;
   - footbinding:R10: Mackie `unverified` to `snippet`; two Wikipedia pages `unverified` to `recalled`.

   Five of these are supported by the string. The quotes and the "Read 2026-11-04" claim come in an order the heuristic misses, and the UNVERIFIED belongs to a different clause. The sixth is finding 1. The report's override table does not mark any of them as a raise. A reviewer told that hand settings only lower would skip exactly these rows. Fix: correct the docstring, and mark raises in the report's override table with the string clause that licenses each.

4. **[major] Duplicate work in the bibliography: `ny-mwpa-1848` (rules.yaml) and `us-ny-laws-1848-ch200` (backtests.yaml).** Both are New York Laws 1848 ch. 200. mwpa-property:R13 cites one and ground-truth NY-property cites the other. This breaks "one entry per work" (plans/sourcing.md) and the merge instruction in backtests.yaml's own header, which was followed for GLT, Khan and Chused but not here. Check 1 cannot catch it (see 7e).

5. **[major] mwpa-ground-truth.yaml MS-property: `khan-1996` has `date_reported: 1839`.** plans/backtest-mwpa.md records that Khan names the 1839 Mississippi act and *excludes* it as debt relief. The item's own note says Khan's MS property date is not recorded. So the item attributes to Khan a date Khan rejects, and the event's `conflict` status rests on that. Fix: `date_reported: null` with the 1839 classification in the note, and `unresolved` until Khan's Table 1 is opened. Every other GLT and Khan `date_reported` matches the plan's table.

6. **[major, low impact, disclosed] Omissions.**
   - ectogenesis:R5 names "the Kleven finding in docs/theory.md" (the reason for the `female` trigger) and gets no item or bibliography entry.
   - mwpa-creditor-exemption:R11 names the Mississippi 1839 act (via Khan) with no `source_id: null` item. R14, R15 and R16 get one for the same pattern.

   Both are listed in the report, but not in the provenance. Neither changes a level.

7. **[major] Check gaps in tests/test_sources.py.** Throwaway fixtures were run against `settled_problem` from my scratch directory. Cases (c) and (d) were demonstrated; the rest were read off the code.
   - (a) Nothing checks that an `opened` excerpt is a substring of the row's `source`. That is the migration's core invariant: it holds today by my script, and nothing keeps it.
   - (b) An `unresolved` event whose items report different dates passes with no `conflict_note`, which is a silent conflict (ADR 0017 item 6).
   - (c) Independence of two secondary works is "author sets disjoint", which can be fooled:
     - Two works with `author: null` count as independent, so two Wikipedia pages, or a draft and its published version entered without authors, settle a date.
     - A string author is iterated by character.
     - `"Geddes"` vs `[Geddes, Rick]`, and `["Geddes, Rick"]` vs `[Geddes, Rick]`, are judged independent.
   - (d) An opened primary item settles an event whatever its jurisdiction: a UK statute settles a US-ME date.
   - (e) Only ids are checked for uniqueness, so the same work under two ids (finding 4) passes.

   Caught correctly:
   - whitespace-only excerpt;
   - `source_id: null` with `opened`;
   - duplicate ids across files;
   - settled on one secondary;
   - same-author pair.

   Also unchecked (minor): `accessed` on opened or snippet items; bibliography fields beyond id/type/title; jurisdiction on statute, regulation and case entries.

8. **[minor] effective_date not stated by the string.**
   - mwpa-suit:R16 `uk-mwpa-1882` has `effective_date: "1882"`, and mwpa-property:R13 `ny-mwpa-1848` has "1848". Both are short-title years. From memory, unverified: the 1882 Act came into operation on 1 Jan 1883.
   - companion-guardian-renamed:R1 `ri-gen-laws-4-13-41` "2001" comes from "P.L. 2001 ch. 72", a session law, not an effective date.
   - alaska (a)(5) "2017-01-17" is stated in its string ("eff. 2017-01-17").

9. **[minor] mwpa-suit:R16 `jurisdiction: UK`** while the coverture items say England. From memory, unverified: the 1882 Act does not extend to Scotland. The US-chain mismatch itself is disclosed in the report.

10. **[minor] airline-flight:R2, `cfr-14-121-391` is `opened` with `accessed: null`.** The string gives a URL, no date. The note says "same batch".

11. **[minor] police-crisis:R7.** The excerpt drops the string's own most relevant passage: "shall be released before 72 hours ... only if the psychiatrist ... believes ... that the person no longer requires evaluation or treatment". That passage is what `(not (danger s))` stands for. The excerpt keeps the evaluation sentence instead.

12. **[minor] Ground-truth item jurisdiction.** GLT and Khan items carry the event's jurisdiction (US-MS, US-ME ...). Rule items leave a secondary work's jurisdiction null, and the contract says "the jurisdiction the cited text governs". Separately, NY-suit's GLT `date_reported: 1860` rests on the R16 string's gloss "e.g. NY 1860", while GLT Table 1 is property and earnings dates. The note says so.

13. **[minor] data/sources/rules.yaml header** says fields not in the repo text are null. The merged entries fill them from search leads:
   - GLT: title "assumed equal to the 2012 article's", given names;
   - Khan: container and pages "from RePEc lead";
   - Chused 1983: title, container and URL "from several agreeing leads";
   - Chused 1984: given name.

   Some notes say "not in repo text" next to a filled field. The report's "Bibliography gaps" list still calls these fields null. No level is affected. Fix the header or null the fields.

14. **[minor] Small mapping notes.**
   - `berkeley-public-library-2018-patron-suspension-policy` is typed `regulation` with `jurisdiction: null`.
   - mwpa-creditor-exemption:R12's Blackstone pin "Bk I ch 15" is inferred, not in the string (I believe it is right).
   - kibbutz-childrens-house:R6's string also says the rule itself is "implicit ... UNVERIFIED (general knowledge)", but it has no `source_id: null` item, unlike public-library R2 and footbinding R1. The level is unaffected.

15. **[minor, over-downgrades] Rows below what the string arguably supports.** All are correct under the strict row-only rule, and are listed here because each costs a re-open:
   - **coverture-household:R2, R4, R7.** Bk I ch 15 is `recalled`, though the entry's `source_text` quotes it and says it was checked. R2 is one of the nine rows L1 rests on.
   - **kibbutz-childrens-house:R2.** Wikipedia is `recalled`, though the row quotes the sentence R1's row records reading on 2026-11-03 (load-bearing).
   - **companion-guardianship:R9.** Alaska is `unverified` though the row quotes the statute. The row's UNVERIFIED covers the generalisation, which already has its own null item, so `recalled` would be defensible for the statute.
   - **public-library:R2, R3, R5.** The Berkeley policy is `recalled`: quotes, but no date in the row.
   - **naming-convention:R1, R2.** Centola is `unverified`. "cited from memory" means `recalled`, and "UNVERIFIED as a quotation" governs a quote the row does not use.
   - **Cheapest upgrades.** Rows that quote with a URL but no read date: companion R3/R4 (597s), cps R3/R4/R10 (306), police R2/R3/R4 (5150), lease R2 (1941). L24 says 597s and 5150 were fetched in an earlier batch.

## Ground truth (mwpa-ground-truth.yaml)

- 40 events: 9 `conflict`, 31 `unresolved`, 0 `settled`.
- Every conflict has a `conflict_note`.
- Every item is at `recalled` (GLT and Khan, "[F] ... no excerpt recorded") or `unverified` (WebSearch leads, each marked "LEAD only, not evidence"). Search summaries are kept as leads and never as snippets.
- `date_used` matches the plan's table for all 39 table events. NY-suit is outside the table and takes its date from R16's string.
- `date_reported` matches the table on every GLT and Khan item except MS-property's Khan (finding 5).
- No `unresolved` event has items that disagree.

## Counts

- Rules checked: 121. Items: 171 (opened 15, snippet 7, recalled 65, unverified 84; 52 with `source_id: null`).
- Weakest item per row: opened 7, recalled 39, unverified 75. These match the report.
- Excerpts checked verbatim: 20 of 20.
- Items above their string: 2, in 2 rows (finding 1). Rows whose weakest level is above their string: 0.
- Findings: critical 1, major 6 (2-7), minor 8 (8-15).
- Over-downgraded rows listed: 10, plus 10 cheapest-upgrade rows.
- Compared with provenance-migration-report.md:
  - The report agrees on counts, the jurisdiction mismatches and the omissions in 6.
  - It does not flag findings 1-5 or 7.
  - Its claim "no row was upgraded" holds at row level but not at item level (finding 1).

The migration did what the standard asks in the part that matters most: every level is read off the row's own words and nothing was lifted from memory. The new problems are in the layer meant to make that checkable. A hand-override table described as "lower only" contains raises, and one of them is not licensed by its string. An `opened` label on the kibbutz rows certifies an excerpt that does not state the rule. The CI cannot see a non-verbatim excerpt, a silent conflict, or two authorless works "agreeing". Fix 1-5 in the data, and add tests for 7a, 7b, 7c and 7e before checks 4 and 5 are promoted to hard. Promotion makes `opened` count toward `supported`, and that is where these gaps would start to change claims.

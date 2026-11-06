# Sourcing and citation overhaul

Status: doing (2026-11-05). Handoff: the read-only sourcing audit of 2026-11-05 (summarised below). Part 2 of that handoff (lineage / phylogenetic sequencing) is parked; see the end of this file.

## Why

The "rediscover known findings" falsifier only means something if the historical ground truth is independently verified. Today 121 of 211 rule rows carry `UNVERIFIED` in a free-text `source`, citations are pasted repeatedly, there is no bibliography, and `docs/claims.md` has no source column. The facts the rediscovery test leans on (MWPA dates, the US chain's jurisdiction, police/CPS practice norms, kibbutz) are the weakest sourced.

What a date correction does and does not touch: the MWPA layer-1 direction test reads rules, not dates, so a corrected date changes no layer-1 verdict. Dates feed the parked ordering test (layer 3) and the launch table. A jurisdiction fix (US chain sourced to English statutes) can change rules, and so verdicts.

## Network constraint (2026-11-05 session)

The cloud session that built the infrastructure could search but not fetch any page (every host refused). Nothing was opened in that session, so no row was upgraded. Verification is a separate step, done by the author or by a session whose network policy allows the hosts listed in the worklists.

## Data model (the contract every piece below follows)

### Bibliography: `data/sources/*.yaml`

Every YAML file in `data/sources/` is a list of works; ids are unique across all files. One entry per work (a statute section, a case, a book, an article, a web page), not per citation.

```yaml
- id: blackstone-1765-bk1-ch15        # kebab-case, author-year-short; stable, never reused
  type: treatise                       # statute | regulation | case | treatise | archival | secondary | web | dataset
  title: "Commentaries on the Laws of England, Book I, ch. 15: Of Husband and Wife"
  author: [Blackstone, William]        # list; omit for statutes/regulations
  year: 1765                           # publication or enactment year (int or "1765")
  container: null                      # journal / book / code (e.g. "California Welfare and Institutions Code")
  jurisdiction: England                # for statute | regulation | case; ISO-like: England, UK, US, US-CA, US-ME, CA-QC, IL (Israel) ...
  url: https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp
  note: ""                             # e.g. "2007 draft; corrected dates in Geddes & Tennyson 2013"
```

### Per-rule provenance: `provenance:` on each rule in `data/institutions/src/*.yaml`

A list (a rule can rest on more than one work). The free-text `source` string stays until migration is reviewed; `build.py` strips `provenance` from the engine JSON (like `plain`), so the engine, `ENGINE_PIN` and the verdict baseline are untouched.

```yaml
provenance:
- source_id: blackstone-1765-bk1-ch15  # must exist in data/sources/; null only when verification is unverified and no work is named
  pin: "Bk I ch 15"                    # section / page / paragraph
  jurisdiction: England                # jurisdiction the cited text governs
  effective_date: "1765"               # date the rule the row encodes took effect, if the source says; else null
  verification: opened                 # opened | snippet | recalled | unverified (ordered, strongest first)
  excerpt: "she cannot sue or be sued in her own name"   # required, non-empty, when opened; a short quote
  accessed: 2026-11-04                 # when opened/snippet
  url: https://...                     # the copy actually read, if different from the bibliography url
  note: ""
```

Verification levels:
- `opened`: the full text of the cited passage was read and the excerpt is a quote from it.
- `snippet`: only a search snippet, abstract, or partial page was read.
- `recalled`: cited from memory or second-hand (the old `[R]` tag); also a row whose old text claims it was read but records no quote.
- `unverified`: no work identified, or the old string says `UNVERIFIED`.
A search-engine summary is not a snippet of the source; it is a lead, and changes no level. Never upgrade from memory.

### Backtest ground truth: `data/backtests/<backtest>-ground-truth.yaml`

```yaml
backtest: mwpa
events:
- id: ME-property                      # <jurisdiction>-<event>
  jurisdiction: US-ME
  event: property                      # property | earnings | sole_trader | suit | ...
  date_used: 1855                      # the date the backtest uses (null if unresolved)
  status: conflict                     # settled | conflict | unresolved
  provenance: [ ... same fields as rule provenance, plus `date_reported` per item ... ]
  conflict_note: "GLT 2007 draft 1855; Khan 1996 1844"
```

## CI checks (tests/test_sources.py)

Hard (fail now):
1. Every `source_id` in rule provenance and ground truth exists in `data/sources/`; bibliography ids unique; required fields present; `type` and `verification` in the vocabularies.
2. `opened` requires a non-empty `excerpt`; on a rule, the excerpt (each " ... " fragment) appears verbatim, whitespace-normalised, in the rule's `source` string.
3. A ground-truth event with `status: settled` has a `date_used` backed by one `opened` primary item of the event's jurisdiction reporting that date, or two `opened` items from independent secondary works agreeing on it (independent: both name authors, no shared surname; a work with no author is never independent). Conflicts stay `conflict`, recorded, not silently resolved: an event whose items report different dates must be `conflict` with a `conflict_note`.

Report-only until migration is reviewed (warn, then promote to hard):
- (1e) two bibliography entries with the same url, or the same type, year and normalised title (one work under two ids).
4. Every rule has `provenance`.
5. A `supported` claim in `docs/claims.md` whose `sources` cell names a rule row below `opened`.

## Which rows the care+control match reads (drop-one, 2026-11-05)

Each rule of coverture-household, police-crisis and cps deleted in turn, `phil rules gate` criterion (b) rerun (engine at ENGINE_PIN, dataset at this branch). Gate (b) FAILs on deleting exactly nine rules: coverture R2, R5, R6; police-crisis R2, R3, R4; cps R3, R4, R10. Deleting any other rule, including every UNVERIFIED police/cps practice norm (police R1, R5, R6, R8, R10; cps R1, R2, R5, R6, R8, R11), leaves (b) PASS.

So L1 rests on nine rows, and the only one carrying `UNVERIFIED` is **coverture R6** (the wife's exit bar, sourced to Shanley/Stone on England's Matrimonial Causes Act 1857, not opened). The handoff's "police/CPS implicit norms R1, R5, R6 the match reads" does not hold for the match; those rows still matter for other properties (cps R6 makes `care_assigned_by_sex` reachable) and for L24. Verification order adjusted: coverture R6 first (it is also the inherited exit bar of all six mwpa-* entries and the jurisdiction mismatch), then the eight other match rows to `opened` with excerpts, then the remaining police/CPS rows. Script: `scripts/drop_one_match.py <tmpdir>`; the method is "delete one rule from institutions.json, run `phil rules gate --institutions <copy> --json`, read criterion b".

## Order of work

1. done 2026-11-05: this file; bibliography (`data/sources/rules.yaml` 49 works, `backtests.yaml` 21 more, 20 after the NY 1848 merge); provenance on every rule via `data/institutions/migrate_provenance.py` (resolved rows: opened 18, snippet 0, recalled 64, unverified 129; nothing upgraded; after the council review's fix pass, `docs/reviews/2026-11-05-sourcing-migration-review.md`: opened 12, snippet 0, recalled 66, unverified 133; report `data/institutions/provenance-migration-report.md`); build strip + cards; `tests/test_sources.py`; ADR 0017 (proposed); `Sources` column in `docs/claims.md`; MWPA ground truth (40 events: 9 conflict, 31 unresolved; 8 / 32 after the review fix to MS-property); worklists; `plans/sourcing-verify-session.md` (the brief for a session that can open pages).
2. Coverture R6 (load-bearing for L1 and inherited by every mwpa-* entry; see above). MWPA verification worklist (`plans/sourcing-worklist-mwpa.md`) and ground-truth file; open sources; resolve ME/MA/IL/MD; replace English sources in the US chain or split UK entries; record drift if any rule changes.
3. Police / CPS practice norms (R1, R5, R6 the match reads); kibbutz (Spiro, Gavron); footbinding (Mackie), naming-convention (Centola); `docs/theory.md` uncited facts (`plans/sourcing-worklist-other.md`).
4. Council: honesty of the migration (no row upgraded), and after verification a sampled check of `opened` rows against their excerpts.
5. Promote checks 4-5 to hard; drop the free-text `source` once every row has provenance.

## Parked: Part 2, lineage / phylogenetic sequencing

Ancestral state reconstruction and correlated-evolution tests (Pagel 1994) as a check on the ABM's orderings; Holden & Mace 2003 as a rediscovery test; trait export from ADICO components; horizontal transmission edges; five claims to preregister (floor-first across countries; rule-vs-tech ordering within lineages; Lerner ordering, contested; lineage specificity; rival-strand priority) plus Smuts 1995 traits and Alesina, Giuliano & Nunn 2013 persistence; glossary entries for mechanism vocabulary. All references [R]. Depends on this plan (traits need sourced, dated, jurisdiction-specific codings) and on the thin path; not started.

## Decisions for the author (raised 2026-11-05)

Settled 2026-11-05 (author took every recommendation): 1 accepted; 2 B3 with B1 now, B2 later as a preregistered experiment; 3 A2 inside the US entry; 4 ">= 8 of the 9 named" (amendment in plans/backtest-mwpa.md); 5 verify first (cps R1, police R8 provenance-only; cps R8, R11 rule changes, preregistered); 6 soften now (draft in docs/theory-softening-draft.md, for the canonical Claude doc).


1. Accept ADR 0017 (proposed).
2. Coverture R6 / the US chain's exit bar: worklist options B1 (US sources, read R6 as "no unilateral exit", no rule change), B2 (encode fault divorce as a conditional exit; moves coverture baseline verdicts), B3 (split English and US entries). Leads: every US state but South Carolina had fault divorce in the period; unilateral divorce only from 1969.
3. mwpa-suit R16: the US acts found grant suit over separate property and exclude suits between spouses (MA 1855 c.304); the unconditional R16 overstates US law. Option A2 scopes it (a rule change; preregister first).
4. Plan backtest-mwpa.md section 3 says ">= 8 of 10 early states" but names nine; name the tenth (or restate as 9) before the ordering test runs, as a recorded amendment.
5. Leads that suggest a rule is wrong, not only unsourced (verify before acting): cps R1 pin (Penal Code 11165.14 is not CPS investigation; WIC 328), cps R8 (counsel on petition, not investigation; 317(c)(1) exception), cps R11 (WIC 388(a)(1) lets the child petition), police R8 (WIC 5275 reach to 5150 detainees from 2023: effective_date). MWPA dates: MA earnings 1846 has no matching act in the leads; MD "1842" may be a real 1843 act of creditor-exemption form, not OCR.
6. docs/theory.md statements the leads contradict: forager fertility ("despite high fertility"), whaling decline (kerosene vs falling lighting demand), Mullainathan & Shafir (contested replication), Kleven (equal in the long run, Denmark). theory.md is exported from the canonical Claude doc, so edit there.

## Coverture split and US suit (B3/B1/A2), preregistered 2026-11-05, before any edit or run

Author decisions 2 and 3 above (B3 with B1 now; A2 inside the US entry). Nothing below has been run against the changed dataset; the predictions are written from the YAML and the engine's rules (rules_iso distance = max(|A|,|B|) - matched; ablation counts every applicable property, families once). Results go in a section after this one; this one is not edited.

### Dataset change (exact)

1. New `src/coverture-household-us.yaml` (in `_order.yaml` right before `mwpa-creditor-exemption`): `extends: coverture-household`; overrides `id`, `name` ("Coverture household, US reading (base of the MWPA chain)"), `source_text`, `notes`, `isomorphic_to: [{id: coverture-household, level: exact}]`, `not_isomorphic_to: [crisis-team]`, `not_isomorphic_to_control: []`, `minimal_pair_of: null`; `expected_properties` identical to coverture-household's ten. Roles, fluents, actions inherited unchanged.
   - `rules_replace` R1, R2, R4, R5, R7: every engine field (attribute, deontic, aim, conditions, or_else, strand, implicit, `source`, `load_bearing`) and `plain` identical to coverture-household; only provenance differs: the Blackstone item keeps its id, pin, `jurisdiction: England` and level (R1, R5 opened; R2, R4, R7 recalled), and its note adds "US entry: an English treatise cited for a US rule; US reception of Blackstone is assumed and unsourced; a US treatise (Kent, Commentaries on American Law) is a lead, not opened". No level moves.
   - `rules_replace` R6: aim, conditions, deontic, or_else, strand identical (`wife must_not leave` when `(married h w)`, disability). `plain` changes to "no exit at her own will" (no unilateral divorce in any US state before 1969). `source` rewritten to the US leads; the English citations (Shanley 1989, Stone 1990, Matrimonial Causes Act 1857) are not carried. Provenance: `stevenson-wolfers-2006` (new bibliography entry; unilateral divorce adopted by state from 1969) and `us-ny-laws-1787-divorce` (new, descriptive title; adultery-only absolute divorce until 1966), both `unverified`, note "lead, not opened". The note says fault divorce (a judicial exit on the husband's proved fault, varying by state; none in South Carolina) is not encoded (B2, below).
   - R3 inherited unchanged.
2. `mwpa-creditor-exemption`: `extends: coverture-household-us`; `minimal_pair_of.id: coverture-household-us`; notes say so. No rule change. The other four chain entries are unchanged in YAML; their resolved R6 now carries the US `plain`, `source` and provenance.
3. `mwpa-suit` (A2). Design: suits against the husband become their own action, the rest of R4's disability kept for them.
   - `actions_add`: `sue_spouse` args `[w, h]`, `default_capacity: true` (as `sue`).
   - `fluents_add`: `has_standing_against_spouse` arity 2, params `[w, h]`, derived `(enabled sue_spouse w h)`, arg_roles `[wife, husband]`.
   - `fluents_set` `has_standing`: gloss restated for this entry: standing to sue in her own name anyone other than her husband (third-party suits). The derived formula is unchanged, `(enabled sue w)`. Before this entry `sue` stands for every suit in her own name (all barred by R4); this entry splits off `sue_spouse` because the US acts treat the two differently.
   - `rules_drop: [R4]` (as now). `rules_add`: R16 kept with the same engine fields (`wife may sue` when `(married h w)`), `plain` "may sue third parties"; R16 re-sourced to NY Laws 1860 ch. 90 s. 7 and 1862 ch. 172 (`us-ny-laws-1860-ch90`, `us-ny-laws-1862-ch172`) and MA St. 1855 c. 304 s. 3 (`us-ma-acts-1855-ch304`), each `unverified`, "lead, not opened"; GLT 2007 kept at `recalled`. R16 is read at the broader 1862 / MA reading ("as if sole"); NY 1860 s. 7's "matters having relation to her property" scope is recorded in the note, not encoded (encoding it would make `no_standing` reachable for an unpropertied wife). New R19: `wife must_not sue_spouse w h` when `(married h w)`, `or_else: null` (a disability), strand tying, not implicit; sourced to MA 1855 c. 304 s. 3's proviso ("nothing herein contained shall authorize suits between husband and wife", per the worklist's case-law summary), NY 1860 ch. 90 s. 7 with Longendyke v. Longendyke (N.Y. 1863, as summarised; no bibliography entry, a null item), all `unverified`.
   - `minimal_pair_of`: `{id: mwpa-sole-trader, rule: R4->R16,R19, differs_on: no_standing}`. `expected_properties`: as now plus `no_standing_against_spouse: reachable`.
   - A3 (an English chain): not built. Nothing in the repo needs it (the MWPA backtest is a US backtest; no claim reads an English suit act). The UK 1882 citation leaves R16; `uk-mwpa-1882` stays in the bibliography, its note saying it is no longer cited by any rule and is the lead for an English chain if one is built.
4. `properties.yaml`: new `no_standing_against_spouse` (kind freedom, family `no_standing`): some subject married to someone lacks standing to sue that spouse, `(exists ((s agent) (h agent)) (and (is_subject s t) (married h s t) (not (has_standing_against_spouse s h t))))`. It applies only where `has_standing_against_spouse` is declared (mwpa-suit).
5. Bibliography (`data/sources/rules.yaml`): add `stevenson-wolfers-2006`, `us-ny-laws-1787-divorce`; update the `uk-mwpa-1882` note.
6. `migrate_provenance.py`: OVERRIDES for coverture-household-us R1, R2, R4, R5, R6, R7 and mwpa-suit R16, R19 equal to the provenance written, none above the heuristic (no RAISES entry), so a rerun writes nothing.

### Predicted verdicts (k=6, the baseline's parameters)

- coverture-household: unchanged, YAML and engine JSON byte for byte.
- coverture-household-us (10 new rows, equal to coverture-household's): dependent_cannot_exit reachable, subject_cannot_exit reachable, care_and_sanction_same_role holds_to_k, no_standing reachable, care_assigned_by_sex violated, financial_dependence holds_to_k, financial_dependence_unpropertied holds_to_k, cannot_contract holds_to_k, double_burden unreachable_open, creditor_shield unreachable_open.
- mwpa-creditor-exemption, mwpa-property, mwpa-earnings, mwpa-sole-trader, mwpa-property-narrowed: every row unchanged (their resolved rules differ from now only in R6's `source` string and in provenance, which the engine does not read).
- mwpa-suit: the nine existing rows unchanged (subject_cannot_exit reachable, care_and_sanction_same_role holds_to_k, financial_dependence violated, financial_dependence_unpropertied violated, cannot_contract violated, no_standing unreachable_open, double_burden reachable, creditor_shield unreachable_open, backlash unreachable_open); one new row, no_standing_against_spouse **reachable** (marry; R19 bars `sue_spouse`).
- check-all: 134/134 (123 + 11).

### Predicted gate, iso, diff

- `phil rules gate`: PASS. (a) 26 institutions load, 0 inert load-bearing rules (the US base's R2, R3 behave as coverture's). (b) unchanged: coverture-household~police-crisis and ~cps partial(care+control) at guard+strands with the same sub-signatures, crisis-team none at every level, controls none (the US base is not a cluster member and the gate does not read it). (c), (d) unchanged. (e) 134/134. (f) PASS; the cross-pair list gains the US base's pairs with the companion entries.
- iso: coverture-household~coverture-household-us iso=True pure_rename=True distance 0. coverture-household-us~mwpa-creditor-exemption distance 3 (as coverture-household's was). property, earnings, sole-trader and narrowed links unchanged (1, 1, 1, 2). mwpa-sole-trader~mwpa-suit: distance 1 -> **2** (unmatched_a [R4], unmatched_b [R16, R19]; R19's aim has arity 2, R4's arity 1, so they do not unify).
- `phil rules diff --baseline data/verdicts-baseline.json`: 0 changed, 11 added (10 coverture-household-us, mwpa-suit no_standing_against_spouse), 0 removed; exit 0. The baseline is then updated with exactly those 11 rows.
- `scripts/drop_one_match.py`: unchanged; gate (b) fails on exactly coverture R2, R5, R6; police-crisis R2, R3, R4; cps R3, R4, R10.

### Predicted ablation (k=6 and 8, `--entry` per chain entry)

- coverture-household-us: every row as coverture-household's; top {R4, R6, R7} at load_freedom_up 1.
- mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings: top {R4, R6, R7}; mwpa-sole-trader {R4, R6}; every row unchanged from revision 4b (plans/priority.md revision 4 prediction 4 still holds for them).
- mwpa-suit: one new row, R19 (deletion; a `must_not`, so no prohibit variant, not deregulated): `no_standing_against_spouse` reachable -> open, freedom up, family no_standing, load_freedom_up 1. Top changes from revision 4's {R6} to **{R6, R19}**. Every existing row unchanged (R16 deletion load 0; `R16~prohibit` freedom_down 1 on no_standing, as revision 4b). No inconsistent_after, uncounted 0.

### Effect on claims and the backtest

- L1: unchanged (coverture-household untouched; drop-one as above).
- L20, T8, T11 cite `mwpa-*:*`; the cell resolves to each entry's rules, whose inherited rows now come from the US base, so the cells need no text change. L21 left alone. L22, L23 are records of past runs on 25 entries; not rerun, unaffected.
- Backtest direction test (plans/backtest-mwpa.md section 4): `suit` still flips `has_standing` true, now explicitly third-party standing; standing against the husband stays false (`no_standing_against_spouse` reachable). This is drift in the meaning of the preregistered "has_standing flips true" and is reported for a note in that plan (not edited here).
- Engine: no change. Its synced copy of the dataset is behind after this; a sync is owed.

### B2, recorded for later (not done now)

B2 (fault divorce as a conditional exit in coverture-household-us: R6 conditioned on the husband's fault not proved, with a free action setting it, as R5 does with `misbehave`) is a later experiment, preregistered on its own before any edit. Expected direction, not a prediction yet: `subject_cannot_exit` / `dependent_cannot_exit` stay reachable (the bar holds before fault is proved) while a new exit-under-condition property becomes reachable; the chain's exit verdicts and "standing before exit" need restating.

## Coverture split and US suit: results (2026-11-05, engine at ENGINE_PIN 27e24c0)

Preregistration: the section above (commit 73f9c46, before any edit or run). It is not edited; drift is recorded here.

| Prediction | Result |
| --- | --- |
| coverture-household unchanged byte for byte | **held**: YAML untouched; its engine JSON entry identical (only its card's "Pairs" line changes: extended by coverture-household-us instead of mwpa-creditor-exemption) |
| mwpa-* engine JSON differs only in R6's `source` (and mwpa-suit's A2 fields, creditor-exemption's `minimal_pair_of`/notes) | **held** |
| coverture-household-us: ten rows equal to coverture-household's | **held** |
| five chain entries unchanged; mwpa-suit nine rows unchanged, no_standing_against_spouse reachable | **held** |
| check-all 134/134 | **held** (`check-all --no-cache`) |
| gate PASS; (a) 26, 0 inert; (b) unchanged; (e) 134/134; (f) gains the US base's cross pairs | **held**: verbose gate output differs from the pre-change dataset's only in the counts (25 -> 26, 123 -> 134, 66 -> 69 cross pairs), three new cross lines and R19 in mwpa-suit's unmatched lists; gate (b) pairs and sub-signatures identical |
| iso: coverture-household~US iso, pure rename, 0; US~creditor-exemption 3; other links 1, 1, 1, 2 | **held** |
| iso: sole-trader~suit distance 1 -> 2, unmatched_a [R4], unmatched_b [R16, R19] | **distance held; labels drift**: the matcher pairs sole-trader R4 with suit R6 (both `wife must_not <unary capacity> w` when married) and reports unmatched_a [R6]. It made the same pairing before the change (old output: distance 1, R4->R6, unmatched R6 / R16), so this is the matcher's tie-break between same-skeleton disabilities, not a change |
| diff: 0 changed, 11 added, 0 removed, exit 0 | **held**; `data/verdicts-baseline.json` regenerated (`phil rules verdicts --k 6`) and checked to differ from the old one by exactly those 11 added rows (same engine hash, params, z3); the diff against it now reads 0/0/0 of 134 |
| drop-one: gate (b) fails on exactly the nine rows | **held** (coverture R2, R5, R6; police R2, R3, R4; cps R3, R4, R10) |
| ablation: US base rows = coverture-household's, top {R4, R6, R7} | **held** (k=6 and 8) |
| ablation: five chain entries' rows and tops unchanged ({R4, R6, R7}; sole-trader {R4, R6}) | **held** for every load, flip and top; **bookkeeping drift**: each row's `not_applicable` list gains `no_standing_against_spouse` (and mwpa-suit's `applicable` count goes 12 -> 13). Compared row by row against an ablation of the pre-change dataset, ignoring those fields: identical |
| ablation: mwpa-suit R19 flips no_standing_against_spouse reachable -> open, freedom up, load_freedom_up 1; top {R6, R19} | **drift**: the flip happens at k=6 and 8 as predicted, but is counted `unsigned` (load_freedom 1, load_freedom_up 0), so the top stays **{R6}** (revision 4's prediction 4 for mwpa-suit still reads true). Cause: the engine decides flip direction from a hand table of property names (`rules_ablate.UNFREEDOM`, "to be replaced by a `polarity` field on Property in slice 2"), not from `kind`/`family`; the new name is not in it. Making R19 rank needs that engine change (add the name, or the polarity field); not made here (engine off limits). Recorded, not fixed |
| claims: no Sources cell text changes; L1 unchanged | **held**: L20, T8, T11 cite `mwpa-*:*`, which resolves to inherited rows (now the US base's); no claims row names coverture-household for an MWPA claim |

Other checks: `build.py --check` ok (26 institutions, 26 properties, 27 cards); `pytest -q` 31 passed; `migrate_provenance.py` rerun leaves every `src/*.yaml` byte-identical (128 own rules; 47 hand rows; RAISES unchanged). Reproduction: `uv run phil rules ablate --k 6,8 --workers 4 --entry coverture-household --entry coverture-household-us --entry mwpa-creditor-exemption --entry mwpa-property --entry mwpa-earnings --entry mwpa-sole-trader --entry mwpa-suit --entry mwpa-property-narrowed`, and the same with `--institutions`/`--properties` pointing at the previous commit's JSON for the comparison.

Owed elsewhere: a drift note in plans/backtest-mwpa.md (the direction test's "suit flips has_standing" now means third-party standing; standing against the husband stays barred, `no_standing_against_spouse` reachable; the mwpa-suit link is distance 2; the chain's base is `coverture-household-us`); a dataset sync to philosophy-engine; the engine's `UNFREEDOM` table if R19 should rank.

## Verification pass (2026-11-06, local session, branch `sourcing-verify`)

Brief: plans/sourcing-verify-session.md. Network reached california.public.law, avalon.law.yale.edu, legislation.gov.uk, archive.org downloads and nber.org; archive.org lending items (Shanley, Stone) returned 401 / "item not available" and the Google Books API 429, so those two books stay unread. Every `opened` item below was read in full in this session; each row's `source` now carries a "Verification pass: read 2026-11-06 at <url>: '<quote>'" sentence (appended, nothing removed), so the excerpt check (tests/test_sources.py check 2) holds. Provenance is set in `migrate_provenance.py` OVERRIDES, not by hand in the YAML. No rule (deontic, aim, conditions, or_else) was changed, so nothing needed preregistering; the `source` text is carried into institutions.json, verdicts are not (`phil rules diff`: 0 changed of 146 after every batch).

Order of work in this pass: step 2 (the eight other match rows) ran first while the step-1 and step-3 sources were being fetched.

### Faithfulness findings (rules the sources do not support as written; for the author, no rule edited)

- **police-crisis R2** (match row): WIC 5150(a) puts the ongoing assessment and evaluation in the passive voice ("shall be conducted and provided on an ongoing basis") and on the 72-hour facility stay, not on the responding officer. The row's must-be provides_care(o, s) on the officer is the encoder's reading.
- **coverture-household R7** (and -us R7): Blackstone says her deeds and acts are "void, or at least voidable"; the row encodes no power at all. Voidable acts bind until avoided, so the row is the stronger reading.
- **coverture-household R4** (and -us R4): the same passage excepts a husband who "has abjured the realm, or is banished" (she then sues as a feme sole); the row has no exception. Minor.

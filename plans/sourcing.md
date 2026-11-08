# Sourcing and citation overhaul

Status: done, follow-ups open (2026-11-06): infrastructure, verification pass, faithfulness batch 2 and the L1 restatement landed; the remaining faithfulness findings are listed in docs/plan.md "Where to pick up". Started 2026-11-05. Handoff: the read-only sourcing audit of 2026-11-05 (summarised below). Part 2 of that handoff (lineage / phylogenetic sequencing) is parked; see the end of this file.

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
A summarising fetch (WebFetch or any tool that returns a model's summary instead of the raw text) is recorded as `snippet`, never `opened`, however verbatim its quotes look; only a raw read counts. Since 2026-11-08 CI fails an `opened` item without `accessed` (ISO date) and `excerpt` (check 6, `build.py --check` and `tests/test_sources.py`).
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
5. A `supported` claim in `docs/claims.md` whose `sources` cell names a rule row below `opened`. **Promoted to hard 2026-11-06** (after the verification pass; it passes, since every `supported` claim is `engine-only` and L1 is `weakened`). Check 4 also passes (every rule has provenance) and stays report-only for now.

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

### Counts, before and after (`migrate_provenance.py --summary`)

| | opened | snippet | recalled | unverified | total |
|---|---|---|---|---|---|
| rows by weakest item, before (af481c1^) | 6 | 0 | 43 | 80 | 129 |
| rows by weakest item, after | 34 | 0 | 24 | 71 | 129 |
| provenance items, before | 12 | 5 | 74 | 97 | 188 |
| provenance items, after | 56 | 5 | 50 | 81 | 192 |
| ground-truth items opened | 0 -> 17 | | | | |
| ground-truth events settled | 0 -> 2 (ME-earnings, IL-property) | | | | |

Of the nine rows L1 rests on, eight now have every item `opened`; coverture R6 has two `opened` items (Blackstone, the 1857 Act) and two `unverified` (Shanley, Stone), so its weakest level is still `unverified`. Net +4 items (new works cited on R6, R19, cps R11, and a null item for the 'at any time' gap on kibbutz R5, less items merged on rewritten rows), and three bibliography entries (`uk-matrimonial-causes-act-1857`, `longendyke-1863`, `cal-wic-388`). RAISES grew from 11 to 28 items, each citing the row's new read sentence. No preregistered rule change: every mismatch is listed below for the author.

### Faithfulness findings (rules the sources do not support as written; for the author, no rule edited)

- **police-crisis R2** (match row): WIC 5150(a) puts the ongoing assessment and evaluation in the passive voice ("shall be conducted and provided on an ongoing basis") and on the 72-hour facility stay, not on the responding officer. The row's must-be provides_care(o, s) on the officer is the encoder's reading.
- **coverture-household R7** (and -us R7): Blackstone says her deeds and acts are "void, or at least voidable"; the row encodes no power at all. Voidable acts bind until avoided, so the row is the stronger reading.
- **coverture-household R4** (and -us R4): the same passage excepts a husband who "has abjured the realm, or is banished" (she then sues as a feme sole); the row has no exception. Minor.
- **coverture-household R6** (English, L1's one UNVERIFIED match row): supported for "no exit at her own will" by two opened primary texts, Blackstone Bk I ch 15 (no dissolution "for any cause whatsoever, that arises after the union is made"; adultery "only a cause of separation from bed and board") and the Matrimonial Causes Act 1857 (s. 2: restitution and matrimonial suits had sat in the ecclesiastical courts; s. 27: even after 1857 a wife gets dissolution only on the husband's aggravated adultery). Three caveats for the author: (a) the row's 2026-11-04 sentence "Bk I ch 15 ... contains no exit bar" is wrong (the chapter's part II is on dissolution); (b) two conditional exits exist that the row does not encode, separation a mensa et thoro on the other spouse's adultery or "intolerable ill temper" (no dissolution, so no exit from the marriage) and a private Act of Parliament for adultery (the English analogue of B2); (c) Blackstone states the law of 1765, the row's horizon is 1857. Shanley and Stone remain unread, so the row's weakest item stays `unverified` though the rule now rests on two `opened` items.
- **coverture-household-us R6** (base of the MWPA chain): Stevenson & Wolfers (NBER WP 2003, the copy read) does not say "no unilateral divorce in any US state before 1969": its Table 1 lists nine states whose unilateral statutes predate 1964. It does support B1 (pre-reform laws "typically required either the consent of both spouses or a demonstration of marital fault"), but says nothing of the 1840-1880 MWPA era; consent divorce is a second exit the row does not encode. The parenthesis in `plain` ("before 1969") should be reworded by the author; not edited here. NY 1787 ch. 69 confirmed: adultery the only ground, petition by "the party injured" (either spouse).
- **mwpa-suit R19** (no suit against the husband): Massachusetts St. 1855 c. 304 contains no proviso on suits between spouses; the proviso the row (and `plain`) quotes, "nothing herein contained shall authorize suits between husband and wife", is St. 1874 c. 184 s. 3, nineteen years later. The 1855 act only omits the husband, so R19 holds for MA 1855 as an omission, which the row's "bars or omits" covers; the `plain` citation "MA 1855 c. 304 s. 3" should be corrected by the author. New York 1860 ch. 90 s. 7 bars nothing in terms ("except her husband" there qualifies gifts, not suits); the New York bar is Longendyke's construction (44 Barb. 366, 1863), now a bibliography entry.
- **mwpa-suit R16**: pin "MA 1855 c. 304 s. 3" (also in `plain`) is wrong, the suit clauses are ss. 4 (her property) and 7 (trade and earnings). Both NY acts scope the property suit to her property; NY 1860 s. 7 also gives her an action "for any injury to her person or character" against any person. The broader reading the row encodes stays the encoder's choice, as the row says.

- **cps R1**: the Penal Code 11165.14 pin does not support the row: it is a police duty to investigate complaints against school staff at a schoolsite. WIC 328(a) does support a social-worker investigation duty, but triggered by "cause to believe" a child is described in s. 300 (not a received report) and scoped to what the worker "deems necessary". The row's one-off obligation on every report is stronger than 328.
- **cps R8**: WIC 317(c)(1): the court appoints counsel for the child once proceedings are before it, "unless the court finds that the child ... would not benefit"; the row has counsel established by the social worker's investigate and held as a must-be whenever the case is open. Neither the timing (investigation, not petition) nor the guarantee (there is an exception) is in the text.
- **cps R11**: the current WIC 388(a)(1) lets "the child ... through a properly appointed guardian" petition; 317(e) makes counsel the representative of the child's interests. The row's "petition in its own name when counsel has been appointed" follows neither: the standing is through a guardian, and counsel appointment is not its condition.
- **police-crisis R8**: WIC 5275 supports it ("Every person detained under this part shall have a right to a hearing by writ of habeas corpus"); effective_date set to 2024-01-01 (the current text per the page). The request procedure in the section is written for certification; the row's "review of the hold" maps to habeas, not to the s. 5256 certification review (not opened).
- **kibbutz-childrens-house R5**: the page (revision of 2026-06-23) has fathers bonding "through quality time" and the children visiting the parents "for 2-3 hours a day"; the row lets a male member visit the child "at any time". R1 is still unsupported by any read text (no passage names a committee or an assignment).
- **public-library R3**: the Berkeley policy suspends a disruptive patron only after an initial warning (B.1, then B.2 "Continued disruption"); the row's single-step suspension skips the warning. R5 (entry when not suspended) is the converse of the policy's "denial of access", not stated.
- **naming-convention R1, R2**: Centola et al. (accepted manuscript) support the rows only through the design (free text entry each round, "occasional switching"); no sentence states a permission. The 25% threshold is "not expected to be a universal value".
### MWPA ground truth (step 3)

17 statute items opened with excerpts (ME 1844 c. 117, 1855 c. 120, 1857 c. 59; MA 1845 c. 208, 1855 c. 304 x3, 1874 c. 184; NY 1848 ch. 200, 1860 ch. 90 x3, 1862 ch. 172; MD 1842-session ch. 293 x2; IL 1861, 1869). Settled under ADR 0017 point 4 (one opened primary of the jurisdiction states the date, no item reports another): **ME-earnings 1857** (approved 17 April 1857; the bibliography's 15 April was the preceding act) and **IL-property 1861** (approved 21 February 1861). Left unresolved on purpose: the NY events, whose opened copies are transcriptions on a law-course site, not scans; settle once a scan is opened. Conflicts kept: ME-property (1844 vs 1855), MA-property (1845 is a marriage-settlement act; 1855 is the general act), MA-earnings, MA-sole_trader, MD-property and MD-earnings (ch. 293 passed 10 March 1843 in the 1842 session; s. 8 is a real earnings clause capped at $1,000, so GLT's 1842 is the session year, not an OCR error; s. 1's scope may be property in slaves only, check the page image), IL-earnings (Khan 1861 vs the 1869 act), NY-suit.

Not reached: the published GLT 2012 (J. Law & Econ. 55(4)) and Geddes & Tennyson 2013 tables (403 at Chicago Unbound, Emerald, SSRN, journals.uchicago.edu). A 2014 ASSA draft (MacDonald) reproduces G&T 2013 dates but its table prints garbled, so it was not cited; its dates are leads only: ME 1855/1857, MD 1860/1842, MA 1855/1846, IL 1861/1869, NY 1848/1860, MS 1880/1873 (property/earnings). MS-property thus has three candidate dates (GLT 2007 1871, G&T 2013 1880 via MacDonald, 1839 creditor act). IL dates: the backtest should say whether it codes approval (21 Feb 1861, 24 Mar 1869) or in-force (24 Apr 1861, 19 Jun 1869) dates.

### Council (fresh agent, 2026-11-06): ten `opened` items drawn at random (seed 20261106, 56 opened)

Checked against freshly downloaded text: mwpa-suit R16 (MA 1855, NY 1860), companion-guardian-renamed R4 (597s), coverture-household-us R6 (Stevenson & Wolfers), airline-flight R2 (121.571), coverture-household R4 and -us R7 (Blackstone), cps R1 (WIC 328). All eight excerpts are real quotes (allowances: line-break joins, long s, OCR "converture", a dropped leading "And"), pins right, levels right, each gap between passage and rule recorded. Not audited: companion-ownership R1 and companion-guardian-renamed R1 (Civ. 663, opened 2026-11-04): FindLaw and leginfo blocked the reviewer (403); they stay unaudited, not passed.

Acted on: the -us/English R7 note now says the second fragment concerns compacts between spouses, not her capacity with third parties; bibliography urls filled for WIC 328, 317, 5275 and Penal 11165.14. Left for the author (prose a rule carries, not provenance): mwpa-suit R16 and R19 `plain` still cite "MA 1855 c. 304 s. 3; unverified", and their `source` strings still open with "UNVERIFIED (leads ...)"; R16's `source` credits the "sole and separate property ... descent, devise, bequest" wording to the 1862 amendment though the 1860 s. 7 already has it (1862 adds "purchase" and "grant"); the "transfer is an incident of ownership" inference on the Civ. 663 rows sits in `source`, not in the item note; Blackstone pins could give pages (pp. 429-432).

### Not reached in this pass

- Mackie 1996 body (footbinding R1, R3-R7, R10: the "two-part pledge" and "critical mass" readings): closed access everywhere tried (OpenAlex/Unpaywall no OA copy, JSTOR challenge page, ResearchGate/CORE 403). An OpenAlex indexer abstract mentions associations of parents who pledge "not to submit their daughters" and "not to let their sons marry" (for infibulation, with footbinding as the model); it is not the author's abstract and was not cited. Rows unchanged.
- Spiro 1956 and Gavron 2000 (kibbutz R6): archive.org lending-only, HathiTrust behind a challenge, Google Books quota. A human with an archive.org borrow can search inside both.
- Shanley 1989, Stone 1990 (coverture R6): as above.
- GLT 2012 and Geddes & Tennyson 2013 published tables: 403 everywhere; a library login is the route.
- docs/theory.md uncited facts (plans/sourcing-worklist-other.md): not started.

### Follow-up, 2026-11-06: R6 re-cited, check 5 hard

coverture-household R6 now cites only the two works read in full (Blackstone Bk I ch 15, Matrimonial Causes Act 1857); Shanley 1989 and Stone 1990 are leads for the 1765-1857 interval, recorded in the row's `source` and the Blackstone item's reason, not as provenance items. All nine rows the L1 match reads are now `opened` (rows opened 34 -> 35; items 192 -> 190). L1 stays `weakened`: its other grounds (strand tags load-bearing, the airline-flight control match) are not sourcing questions; its Sources cell is updated. Check 5 is hard: a claim moved to `supported` while it names a row below `opened` now fails CI.

## Faithfulness batch 2: preregistered 2026-11-06, before any edit or run

From the verification pass's findings (above). Engine at ENGINE_PIN (philosophy-engine c53d132), baseline parameters (k=6). Three parts: P1 and P2 land in the dataset; P3 is an experiment on a temporary copy of institutions.json and does not land (it may fail the gate; landing it is the author's call after reading the result).

### P1. Prose only (`plain` / `source`; the engine reads neither)

- mwpa-suit R16 `plain`: "e.g. NY 1860 ch. 90 s. 7, MA 1855 c. 304 s. 3; unverified" -> "NY 1860 ch. 90 s. 7, NY 1862 ch. 172, MA 1855 c. 304 ss. 4, 7".
- mwpa-suit R19 `plain`: "MA 1855 c. 304 s. 3; unverified" -> "omitted in MA 1855 c. 304, barred in terms by MA 1874 c. 184 s. 3; in New York by construction, Longendyke 1863".
- coverture-household-us R6 `plain`: "(no unilateral divorce in any US state before 1969; unverified)" -> "(pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only)".
- cps R1: `source` gains a re-pin sentence (the duty is WIC 328(a); Penal Code 11165.14 is off point and no longer cited); its provenance item is removed (as with Shanley/Stone on R6). `plain` unchanged.
- cps R11: `plain` -> "The child may petition through a guardian when one has been appointed for the child (Cal. WIC 388(a)(1); the guardian ad litem may be the appointed attorney, WIC 326.5; encoded as counsel appointed)". Logic unchanged: counsel_appointed stands in for the guardian, a disclosed simplification.

Prediction: no verdict, gate, iso or ablation change anywhere (`phil rules diff` 0 changed of 146). Certain unless `plain`/`source` reach the engine, which build.py and test_provenance_not_in_engine_json say they do not for `plain`.

### P2. cps R8: the statute's exception (lands)

WIC 317(c)(1): the court shall appoint counsel "unless the court finds that the child ... would not benefit". Change: new free fluent `would_not_benefit(c)` (arg_roles [child], in `initial_free`); R8 conditions `(case_open c)` -> `(and (case_open c) (not (would_not_benefit c)))`. Everything else unchanged: `investigate` still establishes counsel_appointed (ADR 0009 establishing-action convention; the court-not-investigation timing stays a disclosed simplification, because an action obligation on the court would collide with R6's contact_mother at the same step, the collision ADR 0009 was written to remove). Effect in the model: where `would_not_benefit` holds, `relieve_counsel` (unregulated) becomes compliant, so the child can lose has_standing.

Predictions (k=6):
- cps rows: care_and_sanction_same_role holds_to_k; care_assigned_by_sex reachable; dependent_cannot_exit reachable; subject_cannot_exit reachable; no_standing_persists fails. All five unchanged (no_standing_persists still fails: worlds with counsel, and the court's can_claim_for under substantial_danger, remain).
- `phil rules diff`: 0 changed, 0 added, 0 removed of 146.
- `phil rules gate`: PASS; criterion (b) PASS (R8 is not one of the nine match rows and is outside both cps iso sub-signatures).
- `phil rules iso`: cps~police-crisis and cps~coverture-household still hold at guard+strands.

### P3. police-crisis R2 on the facility (experiment, does not land)

WIC 5150(a) puts the ongoing assessment and evaluation on the 72-hour stay, in the passive voice; 5150(c) has the facility's professional person assess. Variant: R2 attribute officer -> facility; aim `(provides_care f s)`; conditions `(and (responding o s) (in_crisis s))` -> `(in_custody s)`; fluent provides_care arg_roles [facility, subject]; `detain` gains the facility argument, `detain(o, f, s)`, and also establishes provides_care(f, s) (ADR 0009); `dispatch_officer` and `leave` no longer touch provides_care; `assess` / `withdraw` take (f, s); can_sanction stays the officer's (`(exists ((f agent)) (enabled detain o f s))` or use_force). R3, R4, R7, R8 otherwise unchanged.

Predictions (k=6), the point of the experiment:
- police-crisis care_and_sanction_same_role: holds_to_k -> **violated** (counterexample: subject in custody and resisting; the facility provides care, the officer can sanction via use_force).
- police-crisis subject_cannot_exit, dependent_cannot_exit: reachable (unchanged); no_standing: open (unchanged).
- `phil rules iso`: police-crisis~cps and police-crisis~coverture-household at guard+strands: **fail** (R2's role is now the facility while R3's is the officer; the declared sub-signatures pair both with one role).
- `phil rules gate`: **FAIL** on criterion (b): the faithful police entry no longer matches the care+control cluster; other criteria unchanged.
- Effect on L1, if it held: L1's care+control cluster would rest on cps and coverture; police-crisis, read faithfully, unbundles care (facility) from control (officer). Recorded as a result, not acted on: L1's status is the author's call.

Exploratory, no prediction: `phil rules ablate --entry cps` after P2 and `--entry police-crisis` on the P3 copy, reported as run.

### Faithfulness batch 2: results (2026-11-06, engine at ENGINE_PIN c53d132)

**P1 + P2 (landed).** Every prediction held. `phil rules diff --baseline data/verdicts-baseline.json`: 0 changed, 0 added, 0 removed of 146 (so all five cps rows unchanged: care_and_sanction_same_role holds_to_k, care_assigned_by_sex reachable, dependent_cannot_exit reachable, subject_cannot_exit reachable, no_standing_persists fails). `phil rules gate`: PASS, (b) PASS with cps~police-crisis and cps~coverture-household partial(care+control) at guard+strands. `phil rules iso --cond guard --with-strands`: cps~police-crisis care R4~R2, control R3~R3, exit R10~R4 (4/10|9 rules); cps~coverture-household care R4~R2, control R3~R5, exit R10~R6 (3/10|7). build --check ok, pytest 32 passed. Drift: none. Exploratory `phil rules ablate --k 6 --entry cps` (no prediction): R8 load 0, no flips (as R1, R4, R5, R6); R10 the only ranked rule with flips (subject/dependent_cannot_exit reachable>open); R2~prohibit (not ranked) cared_for, known_carer fragile>absent, as in slice 2. The exception is now in the rule, and it is idle at k=6 under these properties: a finding about the properties' reach, not about the statute. Bibliography: `cal-wic-326-5` added; cps R1 cites WIC 328 only.

**P3 (experiment, not landed).** Every prediction held. Variant built by `scripts/faithfulness_batch2_p3.py <dir>` (byte-identical to the copy run). `phil rules diff --baseline data/verdicts-baseline.json --institutions <dir>/institutions.json --no-cache`: 1 changed of 146, police-crisis care_and_sanction_same_role holds_to_k -> violated; subject_cannot_exit, dependent_cannot_exit (reachable) and no_standing (open) unchanged. `phil rules iso --cond guard --with-strands`: police-crisis~cps and police-crisis~coverture-household both "care+control: -" (role maps facility->social_worker, facility->husband). `phil rules gate`: **FAIL** on (b) (police-crisis has no care+control form against either cluster member; coverture-household~cps stays partial(care+control)); (e) agreement 145/146; a, c, d, f PASS. Drift: none. Exploratory ablation of the variant (no prediction): R4 the only ranked rule with flips (exit rows reachable>open), R10~prohibit flips no_standing open>reachable; R2 load 0.

**What this says, for the author.** Read faithfully to WIC 5150, the police entry splits care (the facility, during the hold) from control (the officer, who detains and may use force), and the engine then reports exactly that: care_and_sanction_same_role violated, no care+control match. L1's police leg rests on the encoder's placing the care duty on the officer, which the statute does not do. Options, none taken here: (i) land P3 and restate L1 on cps and coverture-household (a two-member cluster, or one where the "same role" holds only for them); (ii) keep the officer as carer and record R2 as a disclosed modelling choice against the text (L1 stays weakened, now with a sourced reason); (iii) give the facility the custody power the hold implies (it maintains the 72-hour detention, s. 5150(a), (e)): a new rule and a new preregistration, which could restore the bundle with the facility as the one role. (iii) is the reading closest to the statute's own structure and the one I would test next. L1's status is unchanged until the author decides.

## Faithfulness batch 2, P4: the facility's custody power, preregistered 2026-11-06, before any edit or run

Option (iii) from the P3 results. Experiment on a copy of institutions.json (built on the P3 variant), not landed. Engine at ENGINE_PIN c53d132, k=6, baseline parameters.

Source: WIC 5150(a), read 2026-11-06: the custody power belongs to "a peace officer, professional person in charge of a facility designated by the county for evaluation and treatment, member of the attending staff, as defined by regulation, of a facility designated by the county for evaluation and treatment, designated members of a mobile crisis team, or professional person designated by the county", any of whom "may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours". So the facility holds the same power as the officer, on the same trigger.

### Change (on top of P3, `scripts/faithfulness_batch2_p3.py`)

- New action `hold(f, s)`: effects in_custody(s) true and provides_care(f, s) true (ADR 0009: it establishes R2's must-be, as `detain` does in P3).
- New rule R11: facility may `(hold f s)` when `(and (in_crisis s) (danger s))`; or_else null; strand rival; implicit false.
- `can_sanction` derived: `(or (exists ((f agent)) (enabled detain o f s)) (enabled use_force o s) (enabled hold o s))`, and its `arg_roles` set to null, because a typed `[officer, subject]` makes every facility tuple constant false (engine: one role per argument position).
- Nothing else changes: the officer keeps R3 (detain) and R5 (use force in custody).

### Predictions

- police-crisis care_and_sanction_same_role: **violated** (unchanged from P3). The facility now both cares and sanctions, but the formula needs no other sanctioner, and the officer still can_sanction (R3 detain while responding to a subject in crisis and danger; R5 use_force in custody).
- subject_cannot_exit, dependent_cannot_exit: reachable; no_standing: open (unchanged).
- `phil rules diff` against the baseline: 1 changed of 146 (the same row as P3).
- `phil rules iso --cond guard --with-strands`: police-crisis~cps and police-crisis~coverture-household: **partial(care+control) restored**, with role map facility->social_worker / facility->husband; care R2, control R11 (~cps R3 remove, ~coverture R5 chastise), exit R4.
- `phil rules gate`: **PASS**; (b) PASS (the three care+control pairs match again, controls still none); (e) agreement 145/146 (the invariant row disagrees with the entry's expectation).
- If both hold: the structural match (gate (b)) and the invariant measure different things. The facility bundles care and control as the statute writes it; the officer's concurrent power is what keeps the invariant violated. L1 would then need saying as "the role that cares also holds sanction power", not "only the carer holds sanction power".

Exploratory, no prediction: `phil rules ablate --entry police-crisis` on the variant.

### P4 results (2026-11-06)

Variant built by `scripts/faithfulness_batch2_p4.py <dir>`. Four of five predictions held; one did not (drift, recorded; predictions not edited).

- **Held:** police-crisis care_and_sanction_same_role violated; subject_cannot_exit, dependent_cannot_exit reachable, no_standing open; `phil rules diff`: 1 changed of 146 (the invariant row), as in P3.
- **Held:** `phil rules iso --cond guard --with-strands`: police-crisis~cps care R2:(provides_care f s) ~ R4, control R11:(hold f s) ~ R3:(remove w c), exit R4 ~ R10, role map facility->social_worker, 4/10|10 rules; police-crisis~coverture-household care R2 ~ R2, control R11 ~ R5:(chastise h w), exit R4 ~ R6, 3/10|7. The care+control form is back, with the facility as the bundled role.
- **Held:** gate (e) 145/146; a, c, d, f PASS.
- **Did not hold: gate (b) FAIL**, predicted PASS. The form is found, but (b) also checks the entries' precommitted sub-signature pairs (`isomorphic_to` in police-crisis.yaml, cps.yaml, coverture-household.yaml), which pair the officer's R3 (detain) with cps R3 and coverture R5. In P4 the matched control rule is R11, so (b) reports "precommitted pairs not matched: R3~R3" (and R3~R5, R5~R3). The prediction missed that (b) reads the declared pairs, not only the form. Updating those declarations to R11 would be a post hoc change to a precommitment and is not done; it is the author's call, and would itself need a preregistration that says so.
- Exploratory `phil rules ablate --entry police-crisis` (no prediction): no single deletion or prohibition flips care_and_sanction_same_role (R3~prohibit and R5~prohibit included: with either gone, the other keeps the officer a second sanctioner); R4 flips the exit rows, R10~prohibit flips no_standing open>reachable.

**Reading.** Read to the statute, police-crisis has one role that bundles care and control (the facility: it cares during the hold and holds the same custody power), and a second role with concurrent control (the officer). The engine's structural match finds the facility bundle; the invariant fails because of the officer; the gate fails because the precommitted pairs named the officer. For L1 the defensible restatement is "the role that provides care also holds sanction power over the subject" (true for the facility, cps' social worker, coverture's husband), not "only the carer holds sanction power" (false for police read faithfully). Landing P4 would need, preregistered together: the P3 + P4 dataset change, the new precommitted pairs (R11 for R3) flagged as revised after seeing this run, and either the invariant's formula restated or the police entry's expectation changed to violated. Not done; L1 unchanged.

## Draft: L1 restated after P3/P4 (2026-11-06; NOT preregistered, NOT applied; for the author)

### Why the claim needs restating

L1 today: "The engine rediscovers the care+control cluster (police, CPS, coverture household) from the rules alone." Two things are measured under that name:
- **the form** (gate (b), `phil rules iso`): in each member, the role that bears the care duty is the attribute of a rule granting a sanction power over the subject, and the subject has an exit bar;
- **the exclusivity invariant** (`care_and_sanction_same_role`, expected holds_to_k in the cluster): no agent other than the carer holds sanction power over the subject.

Read to WIC 5150 (P3, P4), police-crisis keeps the form (with the facility as the role) and loses exclusivity (the officer holds concurrent custody and force). cps and coverture keep both. A state-level replacement ("whenever x cares for y, x can sanction y") is not a fix: it would fail for cps too (removal needs immediate danger, R3) and for coverture (chastisement needs misbehaviour, R5), because the bundled powers are conditional. So the restatement is role-level, which is what the form already checks.

### Proposed wording

> **L1.** The engine rediscovers the care+control form in police crisis holds, child protection and the coverture household from the rules alone: in each, the role that bears the care duty (the designated facility, the social worker, the husband) also holds a sanction power over the subject, who has no permitted exit. The stronger reading, that the carer is the only role with sanction power, holds for child protection and coverture but not for the police hold, where the officer holds concurrent custody and force (WIC 5150(a)).

Sources cell: unchanged nine rows plus police-crisis R11 (new) and R2 (re-encoded); "match reads" to be re-derived by `scripts/drop_one_match.py` after landing.

### What landing would take (one preregistration, written before any run)

1. Dataset: P3 + P4 into `data/institutions/src/police-crisis.yaml` (facility R2 on `in_custody`, `detain(o, f, s)` establishing care, new `hold(f, s)` and R11, `can_sanction` untyped and extended), each rule's `source` recording the 5150(a)/(c) reading.
2. Precommitted pairs: in the `isomorphic_to` blocks of police-crisis, cps and coverture-household, the police control pair R3 -> R11 (R3~R3 becomes R11~R3; R3~R5 becomes R11~R5), **flagged as revised after the P4 run**, with the reason (the precommitment named the officer; the statute's bundled role is the facility). This is the one post hoc element; it must be labelled so in the register, not presented as a prediction.
3. Expectation: police-crisis `expected_properties.care_and_sanction_same_role` holds_to_k -> violated; the property's gloss ("holds_to_k in the care+control cluster") -> "holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role holds concurrent control".
4. Baseline: `data/verdicts-baseline.json` regenerated after the run (`phil rules verdicts`), the one changed row named in the commit.
5. Claims register: L1 wording as above; status stays `weakened` until the drop-one re-derivation and a council seat on the re-encoded police card agree; theory.md's rules-engine table (row 1, "care+control cluster") gets the same qualification.

Predictions for that run (to be copied into the preregistration, k=6): gate PASS, (b) PASS (police~cps care R2~R4, control R11~R3, exit R4~R10; police~coverture R2~R2, R11~R5, R4~R6; cps~coverture unchanged; controls none), (e) 146/146 (expectation now violated); `phil rules diff` against the current baseline 1 changed (police care_and_sanction_same_role holds_to_k -> violated), 0 added, 0 removed; drop-one: the police match rows become R2, R4, R11 (R3 drops out); airline-flight's match with police-crisis (L1 evidence, third review) is not predicted and is reported as found.

Open for the author: whether "the carer is also a sanctioner" is still the theory's claim (theory.md's care+control strand), or whether exclusivity was the point; if exclusivity was the point, L1 is refuted for the police member and the cluster is two entries.

## L1 landing: preregistered 2026-11-06, before any edit or run

Author decision (in session, 2026-11-06): "Carer-also-sanctions", i.e. L1 is the role-level claim in the draft above; exclusivity is not part of it. Engine ENGINE_PIN c53d132, k=6, baseline parameters.

### Exact change

1. `data/institutions/src/police-crisis.yaml`, exactly the P3 + P4 variants (`scripts/faithfulness_batch2_p3.py`, `_p4.py`): provides_care arg_roles [facility, subject]; can_sanction derived `(or (exists ((f agent)) (enabled detain o f s)) (enabled use_force o s) (enabled hold o s))`, arg_roles removed; dispatch_officer and leave no longer touch provides_care; assess / withdraw take (f, s); detain(o, f, s) also sets provides_care(f, s); new action hold(f, s) setting in_custody(s), provides_care(f, s); R2 attribute facility, aim (provides_care f s), conditions (in_custody s); R3 aim (detain o f s); new R11 facility may (hold f s) when (and (in_crisis s) (danger s)), strand rival. `plain` / `source` of R2, R3, R11 record the WIC 5150(a)/(c) reading; provenance via OVERRIDES. expected_properties care_and_sanction_same_role holds_to_k -> violated. Card regenerated.
2. Precommitted pairs, **revised after the P4 run (post hoc, labelled as such)**: police-crisis `R3~R3 detain~remove` -> `R11~R3 hold~remove`, `R3~R5 detain~chastise` -> `R11~R5 hold~chastise`; cps `R3~R3 remove~detain` -> `R3~R11 remove~hold`; coverture-household `R5~R3 chastise~detain` -> `R5~R11 chastise~hold`. Reason: the precommitment named the officer; the statute's bundled role is the facility.
3. `properties.yaml` care_and_sanction_same_role gloss: "holds_to_k in the care+control cluster" -> "holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control". Formula unchanged.

### Predictions (k=6)

- `phil rules gate`: PASS; (b) PASS: police~cps care R2~R4, control R11~R3, exit R4~R10; police~coverture R2~R2, R11~R5, R4~R6; cps~coverture unchanged; controls none; (e) 146/146.
- `phil rules diff --baseline data/verdicts-baseline.json`: 1 changed (police-crisis care_and_sanction_same_role holds_to_k -> violated), 0 added, 0 removed of 146.
- `scripts/drop_one_match.py`: the police rows the match reads become R2, R4, R11 (R3 drops out); coverture R2, R5, R6 and cps R3, R4, R10 unchanged.
- build --check ok, pytest passes (32).
- Not predicted, reported as found: airline-flight's match with police-crisis (L1 evidence, third review); police-crisis ablation and goods readings.

Then: baseline regenerated (`phil rules verdicts`), L1 wording and Sources in docs/claims.md, theory.md table row 1 qualified; L1 status stays `weakened` pending a council seat on the re-encoded police card. A dataset sync to philosophy-engine is owed afterwards.

### L1 landing: results (2026-11-06, engine at ENGINE_PIN c53d132)

Dataset police-crisis logic checked identical to the P4 variant (fluents, actions, rules) before the run.

- **Held:** `phil rules gate` PASS; (b) PASS, all six cluster pairs partial(care+control), controls none; (e) 146/146. iso: police~cps care R2~R4, control R11~R3, exit R4~R10 (4/10|10); police~coverture R2~R2, R11~R5, R4~R6 (3/10|7).
- **Held:** `phil rules diff` against the old baseline: 1 changed (police-crisis care_and_sanction_same_role holds_to_k -> violated), 0 added, 0 removed of 146.
- **Held:** `scripts/drop_one_match.py`: gate (b) fails on deleting exactly coverture R2, R5, R6; police-crisis R2, R4, R11; cps R3, R4, R10 (police R3 drops out of the match).
- **Held:** build --check ok.
- **Did not hold: pytest** (predicted 32 passed): 1 failed, `tests/test_dataset_claims.py::test_deleting_police_sanction_rules_removes_the_bundled_power`, a regression test pinned to the officer-as-carer encoding (it asserted the full entry holds). Drift recorded; the prediction is not edited. The test was rewritten after the run to the new reading, from values computed then: full entry violated (non-vacuous); R3 and R5 deleted: holds_to_k, non-vacuous (the facility is then the only sanctioner and the carer); R3, R5, R11 deleted: holds_to_k, vacuous; the old "care implies power" shape violated in all three. 32 passed after.
- Reported as found (not predicted): airline-flight~police-crisis still matches, now care R2 ~ R2 (provides_care f s), control R3 (restrain) ~ R11 (hold), exit R4~R4.

Then: `data/verdicts-baseline.json` regenerated (`phil rules verdicts --k 6 --no-cache`): the one row above changed, and engine_hash updated (the old baseline was written under an earlier engine, the "engine source hash differs" note on every diff run); diff against it 0 changed. docs/claims.md L1 restated (the author's wording above), Sources "match reads" updated to police R2, R4, R11, evidence appended, last checked 2026-11-06, status `weakened` (pending a council seat on the re-encoded police card). docs/theory.md table row 1 qualified. The cps and police `notes` updated. Owed: a dataset sync to philosophy-engine; a council seat (card-only) on police-crisis.

## police-crisis R7 re-encode to WIC 5152: preregistered 2026-11-06, before any edit or run

From the card-only seat (docs/reviews/2026-11-06-police-crisis-card-review.md): R7 unfaithful. WIC 5152(a), read 2026-11-06: a person admitted for 72-hour evaluation "shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes, as a result of the psychiatrist's personal observations, that the person no longer requires evaluation or treatment". Today R7 is "facility must release when in custody and not danger"; `danger` is exogenous and never changes, and both detain (R3) and hold (R11) require it, so R7's condition is unreachable and its ablation load is 0 (checked before writing this).

### Change (lands)

- New fluent `requires_treatment(s)`: "the treating psychiatrist believes, as a result of the evaluation, that s still requires evaluation or treatment (WIC 5152(a)); exogenous", arg_roles [subject], added to `initial_free`.
- R7 becomes the "only if": facility must_not `(release f s)` when `(and (in_custody s) (requires_treatment s))`; or_else null; strand rival (it keeps the subject held); plain "The facility must not release the subject early while the treating psychiatrist finds the subject still requires evaluation or treatment (Cal. WIC 5152(a))".
- New R12: facility may `(release f s)` when `(and (in_custody s) (not (requires_treatment s)))`; strand superadditive (as R7 was); plain "The facility may release the subject when the treating psychiatrist finds the subject no longer requires evaluation or treatment (Cal. WIC 5152(a))".
- 5152(b)'s end-of-hold outcomes (release, voluntary referral, certification for intensive treatment) are not encoded: the model has no clock for "72 hours have elapsed"; recorded on the rows as a disclosed gap.

### Predictions (k=6)

- `phil rules diff --baseline data/verdicts-baseline.json`: 0 changed, 0 added, 0 removed of 146 (police-crisis: care_and_sanction_same_role violated, the officer still a second sanctioner; subject_cannot_exit and dependent_cannot_exit reachable, now also with release reachable for some worlds; no_standing open).
- `phil rules gate`: PASS; (b) PASS with the same pairs (R7 and R12 are outside the sub-signatures); (e) 146/146.
- `scripts/drop_one_match.py`: the match rows unchanged (coverture R2, R5, R6; police R2, R4, R11; cps R3, R4, R10).
- build --check ok, pytest 32 passed.
- Exploratory, no prediction: `phil rules ablate --entry police-crisis` (R7 and R12 loads; goods readings).

### R7 re-encode: results (2026-11-06)

Every prediction held; no drift. `phil rules diff --baseline data/verdicts-baseline.json --no-cache`: 0 changed, 0 added, 0 removed of 146. `phil rules gate`: PASS, (b) PASS with the same six partial(care+control) pairs, (e) 146/146. `scripts/drop_one_match.py`: (b) fails on deleting exactly coverture R2, R5, R6; police R2, R4, R11; cps R3, R4, R10. build --check ok; pytest 32 passed. Exploratory `phil rules ablate --entry police-crisis`: R7 (must_not) load 0; R12 (may) deregulated on deletion (release has no other may), load 0; R12~prohibit load 0; no goods change. Reading: the re-encode removes an unfaithful, unreachable rule and makes early release lawful in the worlds where the psychiatrist finds no further need, without moving any property this dataset checks; the exit properties are existential, so a reachable release does not change them. 5152(b) stays unencoded (no clock).

## Faithfulness batch 3a: preregistered 2026-11-08, before any edit or run

Sub-batch 3a of plans/faithfulness-batch.md (Part C "3a", under the section 6 rulings). Prose and provenance only: `plain`, `source`, `source_text`, one fluent gloss and `provenance` fields in `data/institutions/src/*.yaml`. No rule condition, deontic, or_else, kind, sanctioner, action or fluent set changes (those are 3b/3c). Engine at ENGINE_PIN 81d5b9e, baseline 192 rows (k=6, strict, step_mode one). Blackstone Bk I ch 15 re-opened today at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp for the R7 re-pin (the incapacity passage sits at p. 430, the "void, or at least voidable" sentence at p. 432).

### Edits (file, rule, field, old -> new in substance)

1. cps.yaml R1 `source`: opening "Cal. WIC 328 / Penal Code 11165.14: reports must be investigated; ... UNVERIFIED (general knowledge; no source opened)" -> "Cal. WIC 328(a), opened 2026-11-06: the social worker's investigation duty ...; the encoded trigger (every received report) is wider than the statute's (cause to believe the child is described in s. 300; scope what the worker deems necessary), re-encode scheduled as 3c (A1)". Penal Code 11165.14 is no longer named as support; the record that it was read and found off point stays. The WIC 328(a) excerpt stays verbatim. `plain` untouched here (it describes the condition, which 3c changes).
2. cps.yaml R11 `source`: opening "Cal. WIC 317(e): ... so the child claims in its own name through counsel. UNVERIFIED (general knowledge; no source opened)" -> "Cal. WIC 388(a)(1), opened 2026-11-06: the child petitions through a properly appointed guardian; WIC 326.5: the guardian ad litem may be the appointed attorney, so counsel_appointed stands in for the guardian, a disclosed simplification (A2 ruling: re-source only); WIC 317(e)(1): counsel represents the child's interests". Excerpts verbatim; `plain` already aligned (batch 2).
3. coverture-household-us.yaml `source_text` exit sentence: "Exit: no US state had unilateral divorce before 1969 (Stevenson & Wolfers 2006, lead, not opened); fault divorce existed in most states and is not encoded" -> "Exit: pre-reform divorce typically required the consent of both spouses or a demonstration of marital fault (Stevenson & Wolfers, NBER w10175, opened 2026-11-06; Table 1 lists nine states with unilateral statutes before 1964, so the paper does not say 'no unilateral divorce before 1969'); consent divorce and fault divorce (NY 1787 ch. 69, adultery only) are exits this encoding does not represent (exit_ground experiment, 3d)".
4. coverture-household-us.yaml R6 `source`: reordered so the opened texts lead (Stevenson & Wolfers read 2026-11-06 ...; NY 1787 ch. 69 read 2026-11-06 ...), then the B1 reading and the B2/exit_ground note, then the pre-opening citation record (2026-11-05 leads), then the ADR 0013 note. The "UNVERIFIED (leads, not opened 2026-11-05; network fetches blocked)" lead goes (both items are `opened`); both excerpts stay verbatim. The entry `notes` field still carries "(no unilateral divorce before 1969)": not a 3a field, left for the author (flagged in Results).
5. coverture-household.yaml R4 and coverture-household-us.yaml R4 `plain`: "... no such power exists (Blackstone I.15)." -> "... no such power exists (Blackstone I.15; unless the husband has abjured the realm or is banished, when she sues as a feme sole: an exception not encoded)." Source and provenance untouched (the note already records the gap).
6. coverture-household.yaml R7 and coverture-household-us.yaml R7: provenance item re-pinned to "Bk I ch 15, pp. 430, 432", `accessed` 2026-11-08, excerpt "the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband ... all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable" (long s modernised; "converture" in the OCR), note rewritten (the incapacity passage is the pin; the p. 432 sentence is kept as the literal "voidable" reading, introduced as acts done by his compulsion; the compacts-between-spouses fragment dropped as off point, council 2026-11-06); `source` rewritten so the incapacity passage leads and contains both excerpt fragments verbatim; `plain` -> "The wife cannot contract in her own name while married: no such power exists (Blackstone I.15: her legal existence is suspended during the marriage; Blackstone: void or at least voidable; encoded as no power)." Rule unchanged (A6 ruling: keep the disability).
7. kibbutz-childrens-house.yaml R1: `source` gains "No read text names the committee; the work-assignment committee (sidur avoda) is the encoder's reconstruction; Spiro 1956 / Gavron 2000 are the leads, lending-only; unsourced committee; pin when a borrow is possible"; the `unverified` provenance item's note says the same. Level stays `unverified` (option (i)). Inherited unchanged by kibbutz-childrens-house-no-implicit.
8. naming-convention.yaml R1, R2 `source`: "NOT OPENED (2026-11-04 ...); cited from memory, UNVERIFIED as a quotation (...)" -> "opened 2026-11-06 (accepted manuscript); support is design-only: free-text entry each round and occasional switching imply either name may be used in any round, no sentence states a permission; the 25% threshold is 'not expected to be a universal value' and is not a rule"; `plain` -> "A member may use the old/new name in any round (the game's free-text entry: a design feature of Centola et al. 2018, not a stated rule)." Provenance decision: keep `opened` and make `source` consistent with it. Reason: the manuscript was read on 2026-11-06 and the excerpts are real quotations (the stale NOT OPENED text predates the verification pass); downgrading would misstate what was read. What the level cannot say, that the rule is inferred from the design, stays in `plain`, `source` and the item note. `kind: strategy` is 3b, not here.
9. public-library.yaml fluent `disruptive` gloss: "p is behaving disruptively (exogenous)" -> "p continues to be disruptive after the B.1 warning (Berkeley policy B.2 'Continued disruption'; the warning step is not encoded; exogenous)"; R3 `plain` -> "The librarian may suspend the patron when the patron is present and continues to be disruptive after being warned (Berkeley Patron Suspension Policy B.2)."; R3 provenance note updated to say the fluent is glossed as continued disruption after the warning (A4 ruling: re-gloss, no new rule). Condition unchanged.
10. docs/plan.md: the brief asked for the stale "146 baseline rows" figure in "Where to pick up" to be corrected to 192; that section carries no row count (every "146" in the file is a dated log line reporting a result at the time). No edit; recorded here.

### Prediction

`phil rules diff --baseline data/verdicts-baseline.json`: 0 changed, 0 added, 0 removed of 192. `phil rules check-all`: 192/192. `phil rules gate`: PASS, output unchanged (b: the six cluster pairs partial(care+control), controls none). `scripts/drop_one_match.py`: (b) fails on deleting exactly coverture R2, R5, R6; police R2, R4, R11; cps R3, R4, R10. `build.py --check` ok after `--write --cards`; pytest passes (38). Certain by the batch 2 P1 argument: `plain`, `source`, `provenance` and glosses do not reach the lowering (build.py strips `plain`/`provenance`; `source` and glosses reach the JSON and nothing reads them). Council: card-only seat only.

### Results (2026-11-08, engine at ENGINE_PIN 81d5b9e; preregistration commit 066d6ea)

Every verdict, gate and match prediction held. Verbatim summary lines:

- `phil rules diff --baseline data/verdicts-baseline.json`: `0 changed, 0 added, 0 removed (of 192 rows)`, exit 0.
- `phil rules check-all`: `agreement: 192/192 = 100%`.
- `phil rules gate`: `GATE PASS`; (b) PASS, the six cluster pairs `partial(care+control)` at guard+strands, crisis-team `none at every level`, the nine control pairs `none@guard+strands`; (e) `agreement 192/192 = 100%`.
- `scripts/drop_one_match.py`: (b) fails on deleting exactly coverture-household R2, R5, R6; police-crisis R2, R4, R11; cps R3, R4, R10; PASS on every other deletion. (Its `unverified=` column, a grep for "UNVERIFIED" in the source string, now reads False on cps R1 and R11, whose stale UNVERIFIED leads were the edits; a print change, not a match change.)
- `build.py --check`: `ok: 33 institutions, 43 properties, JSON and 34 cards match src/`. institutions.json changed in 27 lines, all `source`, `gloss` or `source_text` strings; 17 cards regenerated (the six touched entries, their descendants coverture-floor, the mwpa chain, kibbutz-no-implicit, and the two composites).
- `pytest -q`: `40 passed in 111.20s`.

Drift: one, in a count, not a verdict. The preregistration said "pytest passes (38)"; the suite has 40 tests (two added with PR #8's provenance CI rule after the figure in the brief), all passing. Recorded, not edited. Surprises ledger: none (no verdict moved; nothing unpredicted was produced).

Left for the author (outside 3a's fields): coverture-household-us `notes` still says "(no unilateral divorce before 1969)" in its R6 reading; the Blackstone R7 incapacity passage is now `accessed` 2026-11-08 (re-read today at Avalon, p. 430), so the card-only seat can read the pin against the chapter opening. Council owed: card-only seat on the six touched entries (does each plain line now say what the source says).

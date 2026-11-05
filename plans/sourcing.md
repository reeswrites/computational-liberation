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
2. `opened` requires a non-empty `excerpt`.
3. A ground-truth event with `status: settled` has a `date_used` backed by one `opened` item reporting that date, or two `opened` items from independent secondary works agreeing on it. Conflicts stay `conflict`, recorded, not silently resolved.

Report-only until migration is reviewed (warn, then promote to hard):
4. Every rule has `provenance`.
5. A `supported` claim in `docs/claims.md` whose `sources` cell names a rule row below `opened`.

## Order of work

1. done/doing: this file; bibliography + provenance + migration script (`data/institutions/migrate_provenance.py`) + build strip + cards + checks; ADR 0017 (sourcing standard); `sources` column in `docs/claims.md`.
2. MWPA verification worklist (`plans/sourcing-worklist-mwpa.md`) and ground-truth file; open sources; resolve ME/MA/IL/MD; replace English sources in the US chain or split UK entries; record drift if any rule changes.
3. Police / CPS practice norms (R1, R5, R6 the match reads); kibbutz (Spiro, Gavron); footbinding (Mackie), naming-convention (Centola); `docs/theory.md` uncited facts (`plans/sourcing-worklist-other.md`).
4. Council: honesty of the migration (no row upgraded), and after verification a sampled check of `opened` rows against their excerpts.
5. Promote checks 4-5 to hard; drop the free-text `source` once every row has provenance.

## Parked: Part 2, lineage / phylogenetic sequencing

Ancestral state reconstruction and correlated-evolution tests (Pagel 1994) as a check on the ABM's orderings; Holden & Mace 2003 as a rediscovery test; trait export from ADICO components; horizontal transmission edges; five claims to preregister (floor-first across countries; rule-vs-tech ordering within lineages; Lerner ordering, contested; lineage specificity; rival-strand priority) plus Smuts 1995 traits and Alesina, Giuliano & Nunn 2013 persistence; glossary entries for mechanism vocabulary. All references [R]. Depends on this plan (traits need sourced, dated, jurisdiction-specific codings) and on the thin path; not started.

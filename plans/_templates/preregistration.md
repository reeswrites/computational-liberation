## <Batch title>: preregistered <YYYY-MM-DD>, before any edit or run

Engine at ENGINE_PIN <sha>, baseline <N> rows (k=6, strict, step_mode one). Inputs read: <files>.

### Scope
<What this batch changes and, explicitly, what it does not (fields, entries, rule semantics).>

### Edits / Build
1. <file, rule, field, old -> new in substance>
2. <...>

### Predictions
- `phil rules diff --baseline data/verdicts-baseline.json`: <C changed, A added, R removed of N>.
- `phil rules check-all`: <agreement X/N>.
- `phil rules gate`: <PASS/FAIL; (b) and (e) lines>.
- `scripts/drop_one_match.py`: <set of deletions where (b) fails; unchanged or not>.
- `pytest -q`: <N passed>.
- Per-property expectations (k = 6 and 8): <property -> holds_to_k / violated / reachable / unreachable_open, with the reason>.

### Drift rule
Any result other than the above is recorded in Results against the row it contradicts and never edited into this section; an unpredicted verdict flip also gets a row in docs/surprises.md.

**Nothing above "### Results" is edited after the first run.** Commit this section before any edit, build or run.

### Results
Negative results: add a row to docs/negative-results.md for every refuted/weakened/untested/refused/declined/artifact outcome; null batches get one group row.
<Run date, engine hash. Verbatim summary lines from `scripts/checks.sh`. Drift items, one per line.>

### Council
<Seats run (docs/reviews/SEATS.md), counts, pauses, links to review files.>

### Post-council fix pass
<Appended only. What changed after the council and why; nothing above edited.>

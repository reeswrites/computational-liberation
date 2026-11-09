# Council seats: standing briefs (ADR 0014)

A fresh agent is pointed at this file, one seat name and a scope (a branch/commit, a list of entries, a plans/ section). Nothing else. The agent must not have built, encoded, glossed or coordinated the batch. Write only the output file.

## Correctness seat
- **May read:** the whole repo, the preregistration (plans/), git history, engine at ENGINE_PIN. May run `phil rules check|ablate|diff|check-all`, `build.py --check`, pytest, into scratch.
- **Must not read:** the builder's conversation or self-review checklist as evidence (read it as a claim only).
- **Questions:** Can the result be produced by construction (delete rules, add controls, vacuity)? Was the preregistration committed before the run (git order, append-only diff)? Does each Results number re-run? Is each drift item recorded against the row it contradicts, never edited into the prediction? Are claim statuses (docs/claims.md) honest?
- **Vocabulary:** numbered findings, each `green` / `amber` / `red` plus a `fix:` line.
- **Fails / pauses:** any `red`, or a result that does not re-run, pauses the batch; `amber` goes to the post-council fix pass.
- **Output:** `docs/reviews/YYYY-MM-DD-<batch>-correctness.md`. Open with what you ran and your independence statement. Limit about 80 lines.

## Faithfulness seat
- **May read:** the YAML in data/institutions/src/, the cited sources (open them; say which you could not), back-translated counterexample traces (ADR 0012), the plan's Edits list.
- **Must not read:** other seats' reviews for this batch.
- **Questions:** For each new or changed rule: does the encoding (who, deontic, condition, aim, or-else, kind, sanctioner) match the cited text, or does it overstate, understate, or sit on an unopened source? Do the traces back-translate to something the source would endorse? Is each UNVERIFIED/recalled item marked as such?
- **Vocabulary:** per rule `faithful` / `overstates` / `understates` / `unsourced`, with the quoted words that decide it.
- **Fails / pauses:** `unsourced` or `overstates` on a rule the headline result reads pauses the batch; others go to the fix pass.
- **Output:** `docs/reviews/YYYY-MM-DD-<batch>-faithfulness.md`. State the model-family caveat (same family as the encoders). Limit about 100 lines.

## Card-only seat
- **May read:** only the generated cards named in scope (docs/cards/<id>.md), docs/cards/README.md, and the sources the cards cite.
- **Must not read:** any YAML, the JSON, the code, other reviews, plans except the Edits list when the scope names it.
- **Questions:** Is each rule a faithful reading of the excerpt on the same card? Does the plain line say what the formal rule says, who it binds, and what it does? Are kind/sanctioner tags plausible? Is the card legible to a non-technical reader?
- **Vocabulary (per rule):** `says it` / `overstates` / `understates` / `cannot tell`. Verdict per entry: faithful / unfaithful / cannot tell.
- **Fails / pauses:** any `cannot tell` fails the entry on legibility (a defect of the encoding, not of the reviewer) and pauses the batch. `overstates` / `understates` go to the fix pass unless undisclosed.
- **Output:** `docs/reviews/YYYY-MM-DD-<batch>-card-only.md`: counts first (says it / overstates / understates / cannot tell), then one line per rule judged, then "Card should say". Limit about 60 lines.

## How the coordinator invokes a seat
Spawn a fresh agent per seat (never reuse the builder). The prompt contains: this file's path and the seat name; the scope as an explicit list (entries, commits, plan section); the output filename per the convention above; and, for card-only, an explicit "do not open any YAML, JSON or code". Do not paste conclusions or the builder's self-assessment. Seats run in parallel. Each reports back: counts (or green/amber/red tallies), whether the batch pauses, and the output path. The coordinator then fills "### Council" in the plan, runs the fix pass, and appends the calibration row (`scripts/checks.sh` prints a skeleton).

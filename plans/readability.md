# Parked: readability and reviewability (handoff, received 2026-11-04)

Status: PARKED, but FIRST in the queue of parked work. It is a process change, not a batch, and every parked encoding batch (race, disability, marriage bundle) should be written under it rather than as edits to `_gen_institutions.py` and the 9,000-line `institutions.json`.

Coordinator note (2026-11-04):
- Today's dataset edits (ectogenesis pair, liberty/default-capacity flags, 24 rule deletions) were all generator edits reviewed by reading Python; a card-only reviewer could not have checked any of them. That is the gap this handoff names.
- Shape that fits what exists: `data/institutions/src/<id>.yaml` per entry (rules with `formal`, `plain`, `source` with quote, `choices` notes); a small build script replaces `_gen_institutions.py` and writes `institutions.json` unchanged in format, so the engine and every preregistration stay valid; `docs/cards/<id>.md` generated from the same source; a CI check that regenerates both and fails on diff or on a rule missing `plain` or `source`.
- Migration is mechanical for the 25 entries (the JSON already holds formal rules and sources; `plain` lines are the new work, one per rule, about 200 sentences) and can be a sonnet builder task with a card-only council seat checking a sample.
- The "card-only reviewer" becomes a fifth council seat (ADR 0014 amendment): reads cards and sources only, judges faithfulness, and may say "cannot tell", which fails the encoding on legibility.
- Minimal-pair diffs and the marriage-bundle goods-by-step table are generated views; the ablation summary already carries what a per-entry "which rule carries which freedom" line needs.

## Handoff text, verbatim

## Readability and reviewability (applies to all new work)
Goal: a person who doesn't read code can check whether an encoding is
faithful to the real institution, and contest it.

Encodings
- One readable source file per institution (e.g. YAML), not edits to
  the generator script or the big institutions.json. Generate the JSON
  from these files.
- Every rule carries three things side by side: the formal rule, a
  plain-English sentence ("the spouse may make medical decisions when
  the patient can't"), and its source with a short quote or pinpoint
  citation.
- Every encoding choice that could have gone another way gets a note:
  the reading chosen, the alternatives rejected, and why.

Human-facing views (auto-generated, checked into the repo)
- An institution card per entry: roles, a rules table (who must / may /
  must not do what, or else what), and sources.
- Minimal pairs shown as a one-line diff ("rule R4: status=married ->
  designated_by=patient") so the single change is obvious.
- For the marriage-bundle sequence: a table of goods by step, showing
  which are still gated on marital status.
- Results in plain language using the sayable / not-sayable format
  from docs/interpreting-results.md.

Code
- Names match docs/glossary.md; comments explain why, not what.
- Small functions; no logic hidden in the generator.

Checks
- CI fails if a rule lacks a plain-English line or a source, or if
  cards are out of date with the encodings.
- Council gets a "card-only" reviewer: reads the cards and sources, not
  the code, and judges whether each encoding is faithful. If that
  reviewer can't tell, the encoding isn't legible enough yet.

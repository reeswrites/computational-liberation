# Decision records

Short records of the theory and process decisions behind computational-liberation. Each is 120-250 words, plain prose, one decision per file. Plan: `plans/institutions-phase0.md`. Terms: `docs/glossary.md`.

Decisions about engine mechanics (rule format, time semantics, verdict vocabulary, state obligations, derived power fluents) live in [philosophy-engine](https://github.com/reeswrites/philosophy-engine) under `docs/decisions/`; they are listed at the bottom so the numbering stays one sequence across both repos. New ADRs take the next free number in either repo.

## Format

Every ADR has these sections, in this order:

- **Context**: what forced the decision.
- **Decision**: what we chose, stated so it can be checked.
- **Alternatives rejected**: what else was considered and why it lost.
- **Consequences**: what follows, including costs and open risks.
- **Status**: `proposed`, `accepted`, or `superseded by NNNN`.

A decision is changed by a new ADR that supersedes the old one, not by rewriting it.

## Index (this repo: theory and process)

| # | Title | Status |
|---|---|---|
| [0001](0001-institutions-as-second-data-family.md) | Institutions as a second data family, not a new project | accepted |
| [0005](0005-isomorphism-as-headline-result.md) | Isomorphism as the headline result, reported with its remainder | accepted |
| [0006](0006-strand-tags-bundles-implicit-rules.md) | Strand tags, bundle types and implicit rules as metadata | accepted |
| [0007](0007-dataset-clusters-pairs-and-gate.md) | Dataset as clusters and minimal pairs, with a rediscovery gate | accepted |
| [0008](0008-guardrails.md) | Guardrails on populations and contested history | accepted |
| [0010](0010-iso-abstraction-levels.md) | Isomorphism abstraction level is precommitted per claim | accepted |
| [0011](0011-dual-use-and-scope-limits.md) | Dual use and scope limits | proposed |
| [0012](0012-participation-in-encoding.md) | Participation in encoding | proposed |
| [0014](0014-review-council.md) | Review council after every batch | accepted |

## In philosophy-engine (engine mechanics)

| # | Title | Status |
|---|---|---|
| [0002](https://github.com/reeswrites/philosophy-engine/blob/main/docs/decisions/0002-rule-format-adico-json.md) | Rule format: ADICO as our own JSON, IG Script tags borrowed | accepted |
| [0003](https://github.com/reeswrites/philosophy-engine/blob/main/docs/decisions/0003-time-by-bounded-unrolling.md) | Time by bounded unrolling in Z3 (k=6) | accepted |
| [0004](https://github.com/reeswrites/philosophy-engine/blob/main/docs/decisions/0004-entailment-not-prediction.md) | Entailment, not prediction | accepted |
| [0009](https://github.com/reeswrites/philosophy-engine/blob/main/docs/decisions/0009-state-obligations.md) | State obligations: an aim can be a fluent (must-be), not only an action | accepted |
| [0013](https://github.com/reeswrites/philosophy-engine/blob/main/docs/decisions/0013-derived-power-fluents.md) | Power fluents are derived from what the rules enable, never asserted as effects | accepted |

ADR 0010 here cites ADR 0013 (engine) for the gate fix; ADR 0013 and the claims register cite 0010 for the precommitted level.

# MWPA backtest: failure-mode taxonomy (2026-11-03)

Scope: the four-mode failure list (dark twin, displacement, backlash, rebundling) as exercised by the MWPA layer-1 run (`plans/backtest-mwpa.md`).

Provenance: this was raised by the orchestrating agent and the author in-session. It is not a fresh council review. A council pass on ADR 0016 is still owed.

- `creditor_shield` was filed as dark twin, but nobody rebundled a freed strand into a product; a third party used the new rule for a purpose it was not written for. That is a rule exploit.
- The `narrowed` branch (`backlash` property) was filed as backlash, but a court narrowing a statute while it stands is drift, not active reaction.
- `double_burden` was filed as displacement, but the plan's own note (`plans/backtest-mwpa.md`, line 72) says it is "a burden that stays, not one that moves". Left as DI; the author did not relabel it.
- The list also has no word for rules that pass and go unused, which the MWPA ordering test asks about.

Verdict: taxonomy incomplete; resolved by ADR 0016 (three axes, eleven modes). No rule or verdict changed.

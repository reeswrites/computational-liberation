# 0018. Composition semantics

Status: proposed 2026-11-08 (settled with the author in session). Plan: plans/composition.md.

## Context
Every entry is isolated, so load moving between institutions is invisible. Composing entries needs semantics where nothing merges silently; four faithfulness reviews missed silent merges.

## Decision
1. **Build-time.** `data/institutions/src/_composites.yaml` lists id, members, aliases, expected_properties. build.py resolves it after `extends` and emits an ordinary entry with `members: [ids]`. The engine owns resolution (`philengine/rules_compose.py`); build.py owns plumbing.
2. **Neutral roles.** Aliases are declared per member. Composites use `partner_a`/`partner_b`; historical entries keep husband/wife (faithful to Blackstone) and are aliased onto them. Sex is carried by the existing `female` fluent set in the composite's `initial`.
3. **Frozen bindings.** Each aim variable's role is written into `var_roles` from the member's own resolution before union, so the prefix heuristic has nothing left to decide.
4. **Unification.** Roles union by name after aliases. Fluents agree on arity; typed beats untyped. Same-name derived fluents need the same definition, same-name actions must be identical; otherwise error. Rule ids become `<member>__R1`, `or_else` rewritten. Defaults and initial union; conflicts error. `expected_properties` and iso lists are not inherited.
5. **Out of scope.** One agent per role, so no multi-partner entry can be written. Role cardinality (N agents per role) is the named future change.

## Alternatives rejected
Run-time `phil rules compose` as primary verb: no cards, no golden baseline, aliases unreviewed on a command line. Aliasing into husband/wife: a sexed vocabulary in a hospital entry where it is false. Disjoining derived fluents: silently changes the fluent's meaning in every member. Waiting for cardinality: blocks the marriage slice and touches grounding.

## Consequences
Nine properties name husband/wife literally (backlash, cared_for, chosen_mutual_care, creditor_shield, double_burden, financial_dependence, financial_dependence_unpropertied, no_standing_against_spouse, provided_for); they do not apply to composites until variants over `female` exist, and connections C2 needs a financial_dependence variant first. Preregister P1-P4 (plans/composition.md). First composite: coverture-household-us + hospital-visitation. The Somerville/Cambridge ordinances (plans/marriage-bundle.md) would first test cardinality.

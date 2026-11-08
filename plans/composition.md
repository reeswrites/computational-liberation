# Composition: several institutions over one person (sketch, 2026-11-07)

Status: PROPOSED, not started. Prerequisite for plans/marriage-bundle.md, plans/disability.md (SSI/Medicaid), and plans/informal-rules.md. Written from a read of the engine (schemas_rules.py, rules_reference.py, rules_ablate.py, rules_lower.py) and build.py on 2026-11-07; line numbers from that read. ADR to write: 0018 (next free number across both repos).

## What it is

A person lives under several institutions at once. Today every entry is isolated, so load that moves from one bundle to another is invisible (docs/connections.md section 3). Composition makes one entry out of several: roles unioned, fluents unified by name, rules concatenated with ids prefixed, and ablation run over the result. The cross-institution transfer graph falls out.

## What the engine already gives

- `ablate(inst, properties, ...)` and `without_rule(inst, rule_id)` take an in-memory `InstitutionJSON` (rules_ablate.py:406, :289). Nothing re-reads from disk. A composite can be passed straight in.
- Agents are one per role, named after the role (rules_reference.py:88). Two entries that share a role name share an agent after union. That is the mechanism by which "the same wife" appears in coverture and in a benefits entry.
- Properties are global, matched by fluent name and arity, never by entry id (schemas_rules.py:219-300; `applicable_which` rules_ablate.py:369). A composite with unprefixed fluent names matches existing properties with no change, EXCEPT the nine that name husband/wife literally: under neutral composite roles those are not applicable until variants over `female` exist (see Decided).
- `validate_institution` (rules_lower.py:205-330) already enforces everything a composite must satisfy: unique role/fluent/action names and rule ids, every `attribute` a declared role, every `or_else` an id in the same entry, conditions over declared fluents.

## Two problems the connections sketch did not see

**1. Role vocabularies do not line up.** `married` is typed `[husband, wife]` in the mwpa-* chain and coverture-floor, untyped in the two coverture-household entries, and arity 1 `[daughter]` in footbinding. A hospital-visitation entry would naturally say `patient` and `visitor`, a benefits entry `claimant` and `spouse`. Union by name gives one entry with husband, wife, patient, visitor, claimant, spouse as six separate agents, and `married(patient, visitor)` never true because nobody wrote it. "Fluents unified by name" only works if the roles they range over are also unified. So a composite must declare **role aliases**, and the targets are neutral: `coverture-household-us.husband as partner_a`, `.wife as partner_b`, `hospital-visitation.patient as partner_a`, `.visitor as partner_b` (decided 2026-11-08, below); sex is carried by the `female` fluent in the composite's `initial`. The alias is applied to the member before union: roles renamed, `arg_roles` rewritten, `attribute` rewritten, `var_roles` rewritten, `initial` literals rewritten. This is the one piece of hand input composition needs, and it is reviewable on the card.

**2. The prefix heuristic shifts under union.** A rule variable with no `var_roles` entry binds to the unique role whose name starts with the variable (rules_reference.py:229). Adding roles can make a prefix ambiguous and silently turn a typed variable into "all agents." 85 bindings already show "unbound" on cards. So composition must **freeze bindings before union**: resolve each member's `var_roles` in the member's own role list and write them out explicitly, then union. After that the heuristic has nothing left to decide. This also fixes the 85 unbound cards as a side effect if the freeze is run on single entries too.

## Unification rules (proposed; each is a choice the author can overrule)

| Thing | Rule | On conflict |
|---|---|---|
| Roles | union by name after aliases | none possible (name + gloss only) |
| Fluents | same name must agree on arity; `arg_roles` must agree, or one side is untyped and the typed side wins | error; author renames in the member's source |
| Derived fluents | same name must have the same `derived` expression | error. Disjoining rejected by the author 2026-11-08: it changes what `can_exit` means in every member silently |
| Actions | same name must be identical (args, arg_roles, effects, default_capacity) | error; author renames (`leave` varies by entry today: coverture, kibbutz, footbinding) |
| Rule ids | prefixed `<member-id>__R1`; `or_else` rewritten to match | n/a. `sexpr.IDENT` is `[A-Za-z_][A-Za-z0-9_]*`, so a dot is not admitted; `__` it is. Member ids with hyphens are mapped to underscores in the prefix |
| `defaults`, `initial`, `initial_free` | union | same fluent with different default: error |
| `expected_properties` | the composite preregisters its own; members' are not inherited | n/a |
| `isomorphic_to` and controls | not inherited; composites take no part in the iso gate | n/a |
| `strand`, `implicit`, `kind`, `sanctioner`, `function` | carried unchanged | n/a |
| `plain`, `source`, `provenance` | carried unchanged; the card shows them under the member heading | n/a |

Errors are the default on every conflict because a silent merge is exactly the kind of thing four code-reading reviews missed on faithfulness. A composite that fails to build names the member and the field.

## Where it lives: build-time, not run-time (recommended)

Two places the verb could sit.

**Build-time (recommended).** A `data/institutions/src/_composites.yaml` lists each composite: id, members, aliases, `expected_properties`, notes. `build.py` resolves it after `extends` and emits it into `institutions.json` as an ordinary entry with one new field, `members: [ids]`. Everything downstream is unchanged: `check-all` validates it, cards are generated (members as sections), the golden verdict baseline covers it, the card-only seat can read it. Engine change is one optional field on `InstitutionJSON` plus one rule in `applicable_which`: a goods property's `entries` leniency applies to a composite if any member is listed. Cost: composites are static; each one is a dataset entry that must be preregistered like any other.

**Run-time.** `phil rules compose A B --alias ...` builds the composite in memory and `ablate --compose` runs over it. Flexible for exploring many compositions quickly; no cards, no golden baseline, no card-only seat, and the aliases live on the command line where nobody reviews them. Rejected for the first slice. Could be added later as a thin wrapper over the same function.

The resolution function itself should live in the engine (`philengine/rules_compose.py`), called by build.py, so the engine owns the semantics and build.py owns the dataset plumbing, same split as today.

## Ordered removal (the exposure path)

A second, smaller addition: `phil rules ablate --path <entry> R_a,R_b,R_c`. Cumulative deletion in order, full property verdicts after each step, one table: step, rule removed, properties flipped at this step, who lost (attribute set), running load. `without_rule` chains already; this is a loop and a report. Endpoint verdicts are order-independent by construction, which plans/informal-rules.md claim N2 checks as an engine test. The path is what the author judges.

## Engine limit this verb does not lift

`Reference.agents` is one agent per role (rules_reference.py:88). A multi-partner entry cannot be written under any naming; role cardinality (N agents per role) is the named future change and touches grounding. Recorded in ADR 0018 as out of scope.

## Cost warning

Untyped fluents ground as `product(agents, repeat=arity)`. A composite with eight roles and an untyped arity-2 fluent grounds 64 tuples where the member grounded 4. Rule: every fluent in a composite is typed (the unification table forces this when any member types it; the freeze step should type the rest from the member's resolution). Watch the k bound and the Z3 time on the first composite before writing more.

## Checks that can fail (preregister before the first composite is built)

- P1. Building `coverture-household-us` + `hospital-visitation` with neutral aliases declared produces an entry that passes `check-all` with no new warnings, and `phil rules diff` over the 27 existing entries is unchanged. (P2 still needs the benefits entry.)
- P2. docs/connections.md C2 as written: deleting the SSI marriage-penalty rule alone flips nothing preregistered; deleting it in the composite flips `financial_dependence`.
- P3. Freezing bindings on the 27 existing entries changes no verdict (`phil rules diff` clean) and reduces the "unbound" count on cards from 85. **Preregistered 2026-11-08 before the dataset run**, from `phil rules freeze-bindings` on the engine at bb89e0f: 155 bindings to write, 66 already explicit, 11 untyped (will stay unbound), 0 conflicts. Measured before the run: `grep -c unbound docs/cards/*.md` sums to 108 (the "85" in the earlier readability note was a different count). Expected: diff 0 changed of 146; the card grep falls to about 11 (the untyped floor). If it does not, the card's "unbound" and the freezer's "untyped" measure different things; that is recorded, not tuned.
- P4. N2 from plans/informal-rules.md: two removal orders over the composite give identical endpoint verdicts and different exposure paths.

## Tasks (in order; none started)

- [ ] ADR 0018: composition semantics (the unification table, aliases, freeze, build-time placement).
- [ ] Engine: `rules_compose.py` with `freeze_bindings(inst)` and `compose(members, aliases, id)`; `members` field; `applicable_which` leniency; tests on two toy entries with every conflict row of the table.
- [ ] build.py: `_composites.yaml`, resolution after `extends`, card section per member.
- [ ] Run P3 on the existing 27 entries first (freeze only). It is the cheapest and it pays off even if composition stalls.
- [ ] First composite: coverture-household-us + hospital-visitation (plans/sourcing-worklist-marriage.md has the sources and an ASSUMED vocabulary); benefits entry (SSI) second, for P2.
- [ ] `ablate --path` and the exposure table.
- [ ] Council after the batch; card-only seat on the composite card.

## Decided with the author (2026-11-08)

- **Composite roles are neutral: `partner_a` / `partner_b`.** Historical entries keep their sexed roles (coverture's husband/wife are faithful to Blackstone) and are aliased onto the neutral pair; sex is carried by the existing `female` fluent set in the composite's `initial`. Reason: the sexed vocabulary does not cover same-sex relationships and will not suit over time; writing it into a hospital entry would be historically false. Cost, accepted: the 9 properties that name husband/wife literally (backlash, cared_for, chosen_mutual_care, creditor_shield, double_burden, financial_dependence, financial_dependence_unpropertied, no_standing_against_spouse, provided_for) are not applicable to composites until variants over `female` are written. Connections C2 needs a `female`-based `financial_dependence` first; that variant is a task below.
- **Derived-fluent conflicts error.** Disjoining rejected: it changes the fluent's meaning in every member silently.
- **First composite: coverture-household-us + hospital-visitation.** It doubles as the static rediscovery case (plans/informal-rules.md R1). SSI second.
- **Poly is out of scope for this verb and recorded as an engine limit.** `Reference.agents` is one agent per role, so a multi-partner entry cannot be written under any naming. The named future change is role cardinality (N agents per role); the Somerville and Cambridge multi-partner ordinances would be its first test. ADR 0018 records it.
- Golden baseline: composites enter on first build (CI diff then covers them); their council pass is recorded in the claims register as usual. ASSUMED by the coordinator, not asked.

Added tasks: `female`-based variants of the 9 sexed properties, starting with `financial_dependence` (preregister that the variant agrees with the original on every existing entry); a `_composites.yaml` example with aliases for the first composite.

## Recombination and synthesis (the direction composition opens; not a task, 2026-11-07)

Composition is first a way to see load move between institutions a person already lives under. It also makes a second use possible: institutions that never existed, built from rules that did. This is design, not simulation. No agent chooses and nothing happens over time; the engine type-checks a constitution. It becomes social modelling only when the dynamics layer (plans/dynamics-sticks.md) asks whether people living under the design keep it.

Four pieces, each on top of something that exists:

1. **Block library.** Every encoded institution sliced into named blocks with provenance (a care duty, an exit floor, a standing grant, a proof-of-commitment gate). Strand tags already roughly partition rules this way; aliases make blocks portable across role vocabularies. A design is a selection of blocks plus aliases, and its card shows where each block came from and says plainly that the arrangement is the author's claim.
2. **Synthesis with Z3.** The engine already runs Z3 over rule sets; the inverted query is "given a target set of properties (partner can visit, nobody loses standing, no double burden), find the smallest set of blocks from the library that entails it." An optimisation query Z3 answers. This is the one mechanism in docs/interpreting-results.md section 7 that produces a rule set nobody wrote. Output is a destination, not a path.
3. **History lookup through isomorphism.** Every synthesized design is matched against the encoded institutions. A match means the shape has existed and its backtest is the design's track record. No match means untried, which is a flag, not a recommendation.
4. **Routes from here.** The project's question is which change first, from the present. Synthesis gives destinations; ablation and `--path` give routes. A target design, the current entry and an ordered removal is a plan with an exposure table at every step. This keeps synthesis tied to the sequencing thesis instead of drifting into drawing utopias.

Where it goes wrong: blocks combined without semantic sense (a care duty over a library patron), which aliases and typed fluents catch only partly; combinatorial blow-up, which the minimality constraint tames; and provenance, since each block is sourced but the combination is not.

Grounding: people already recombine. The Somerville and Cambridge multi-partner domestic partnership ordinances (plans/marriage-bundle.md) are the marriage bundle's blocks with the two-person cap removed, a recombined institution with a real track record, which is exactly what a history lookup would return.

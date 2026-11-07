# Composition: several institutions over one person (sketch, 2026-11-07)

Status: PROPOSED, not started. Prerequisite for plans/marriage-bundle.md, plans/disability.md (SSI/Medicaid), and plans/informal-rules.md. Written from a read of the engine (schemas_rules.py, rules_reference.py, rules_ablate.py, rules_lower.py) and build.py on 2026-11-07; line numbers from that read. ADR to write: 0018 (next free number across both repos).

## What it is

A person lives under several institutions at once. Today every entry is isolated, so load that moves from one bundle to another is invisible (docs/connections.md section 3). Composition makes one entry out of several: roles unioned, fluents unified by name, rules concatenated with ids prefixed, and ablation run over the result. The cross-institution transfer graph falls out.

## What the engine already gives

- `ablate(inst, properties, ...)` and `without_rule(inst, rule_id)` take an in-memory `InstitutionJSON` (rules_ablate.py:406, :289). Nothing re-reads from disk. A composite can be passed straight in.
- Agents are one per role, named after the role (rules_reference.py:88). Two entries that share a role name share an agent after union. That is the mechanism by which "the same wife" appears in coverture and in a benefits entry.
- Properties are global, matched by fluent name and arity, never by entry id (schemas_rules.py:219-300; `applicable_which` rules_ablate.py:369). A composite with unprefixed fluent names matches existing properties with no change.
- `validate_institution` (rules_lower.py:205-330) already enforces everything a composite must satisfy: unique role/fluent/action names and rule ids, every `attribute` a declared role, every `or_else` an id in the same entry, conditions over declared fluents.

## Two problems the connections sketch did not see

**1. Role vocabularies do not line up.** `married` is typed `[husband, wife]` in the mwpa-* chain and coverture-floor, untyped in the two coverture-household entries, and arity 1 `[daughter]` in footbinding. A hospital-visitation entry would naturally say `patient` and `visitor`, a benefits entry `claimant` and `spouse`. Union by name gives one entry with husband, wife, patient, visitor, claimant, spouse as six separate agents, and `married(patient, visitor)` never true because nobody wrote it. "Fluents unified by name" only works if the roles they range over are also unified. So a composite must declare **role aliases**: `hospital-visitation.patient as wife`, `.visitor as husband` (or a neutral pair the author picks). The alias is applied to the member before union: roles renamed, `arg_roles` rewritten, `attribute` rewritten, `var_roles` rewritten, `initial` literals rewritten. This is the one piece of hand input composition needs, and it is reviewable on the card.

**2. The prefix heuristic shifts under union.** A rule variable with no `var_roles` entry binds to the unique role whose name starts with the variable (rules_reference.py:229). Adding roles can make a prefix ambiguous and silently turn a typed variable into "all agents." 85 bindings already show "unbound" on cards. So composition must **freeze bindings before union**: resolve each member's `var_roles` in the member's own role list and write them out explicitly, then union. After that the heuristic has nothing left to decide. This also fixes the 85 unbound cards as a side effect if the freeze is run on single entries too.

## Unification rules (proposed; each is a choice the author can overrule)

| Thing | Rule | On conflict |
|---|---|---|
| Roles | union by name after aliases | none possible (name + gloss only) |
| Fluents | same name must agree on arity; `arg_roles` must agree, or one side is untyped and the typed side wins | error; author renames in the member's source |
| Derived fluents | same name must have the same `derived` expression | error. (Alternative: disjoin the definitions, so `can_exit` is "any member's exit." Rejected for now: it changes what `can_exit` means in every member silently.) |
| Actions | same name must be identical (args, arg_roles, effects, default_capacity) | error; author renames (`leave` varies by entry today: coverture, kibbutz, footbinding) |
| Rule ids | prefixed `<member-id>.R1`; `or_else` rewritten to match | n/a. Check `sx.IDENT` admits the separator; use `__` if not |
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

## Cost warning

Untyped fluents ground as `product(agents, repeat=arity)`. A composite with eight roles and an untyped arity-2 fluent grounds 64 tuples where the member grounded 4. Rule: every fluent in a composite is typed (the unification table forces this when any member types it; the freeze step should type the rest from the member's resolution). Watch the k bound and the Z3 time on the first composite before writing more.

## Checks that can fail (preregister before the first composite is built)

- P1. Building `coverture-household-us` + a benefits entry with aliases declared produces an entry that passes `check-all` with no new warnings, and `phil rules diff` over the 27 existing entries is unchanged.
- P2. docs/connections.md C2 as written: deleting the SSI marriage-penalty rule alone flips nothing preregistered; deleting it in the composite flips `financial_dependence`.
- P3. Freezing bindings on the 27 existing entries changes no verdict (`phil rules diff` clean) and reduces the "unbound" count on cards from 85.
- P4. N2 from plans/informal-rules.md: two removal orders over the composite give identical endpoint verdicts and different exposure paths.

## Tasks (in order; none started)

- [ ] ADR 0018: composition semantics (the unification table, aliases, freeze, build-time placement).
- [ ] Engine: `rules_compose.py` with `freeze_bindings(inst)` and `compose(members, aliases, id)`; `members` field; `applicable_which` leniency; tests on two toy entries with every conflict row of the table.
- [ ] build.py: `_composites.yaml`, resolution after `extends`, card section per member.
- [ ] Run P3 on the existing 27 entries first (freeze only). It is the cheapest and it pays off even if composition stalls.
- [ ] First composite: coverture-household-us + a benefits entry (the benefits entry is the real work; plans/disability.md).
- [ ] `ablate --path` and the exposure table.
- [ ] Council after the batch; card-only seat on the composite card.

## Open for the author

- Neutral role names for composites (husband/wife carry coverture's history into a hospital entry; `partner_a`/`partner_b` lose the sex the care properties read). The alias target is where this is decided, once.
- Whether derived-fluent conflicts should error (proposed) or disjoin.
- Whether composites enter the golden baseline on first build or only after their council pass.

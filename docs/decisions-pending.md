# Decisions waiting on the author (2026-11-03)

Each entry: what the choice is, why it came up, the options, what each enables or forecloses, and the default currently in code or docs. Nothing here is decided until the author says so; the defaults are the builder's or reviewer's and are marked ASSUMED in `philengine/abm/__init__.py` where they are code.

Layer 2 context: the agent-based model (plans/layer2-abm.md) takes an institution encoded as rules, puts N agents per role on a social graph, and asks which mechanism module (material / coordination / imagination) reproduces known collapse, persistence or regendering. Gate tests: footbinding collapses, a committed minority tips a naming convention without a hand-tuned constant, the kibbutz children's house regenders, rankings are stable across seeds (Spearman ≥ 0.9). Layer 2 is what turns the MWPA backtest from "failure modes reachable" into "failure modes ranked".

---

## A. Layer 2 model design

### A1. Where payoffs live
**Why it comes up.** The material module needs a number per action (what an agent gets for doing it). The rules schema (`InstitutionJSON`) has no such field; the theory says material incentives matter but does not say where they are recorded.

**Options.**
1. *Optional `payoffs` block on the dataset entry* (current default; absent → every action pays 1.0). Keeps the rules schema untouched, so layer 1 verdicts and the 47/47 check are unaffected. Payoffs are visible in the same JSON a reviewer reads. Cost: payoffs are hand inputs, the same kind of input the third review flagged for strand tags — a sceptic can say the ABM result was set by the numbers you chose.
2. *Payoffs derived from the rules* (e.g. from income/property fluents an action sets). No hand numbers; the result is attributable to the encoding. Cost: needs a theory of "what counts as income" per institution, which does not exist yet, and many actions set no fluent that reads as income.
3. *Payoffs in a separate file, not in the dataset.* Separates the preregistered encoding from the simulation inputs. Cost: two files to keep consistent; weaker audit trail.

**Recommendation.** Option 1 now, with a sweep over payoff ranges in the gate (so a result must hold across a range, not at one value), and option 2 as the layer-3 goal. This matches plan line 92 ("swept, not calibrated").

### A2. Per-agent vs per-role institutional state
**Why it comes up.** Layer 1 evaluates rules at the role level: "a wife may hold property" is one proposition. In an ABM there are 20 wives. Does each have her own copy of the institutional state (her own `has_standing`, her own `financial_dependence`), or do all wives share one?

**Options.**
1. *Shared role-level state* (current). All agents of a role see the same enabledness; what differs per agent is practice, surplus, trust and neighbours. Cheap, and it reuses `rules_reference` unchanged, which is what ADR 0013 and the plan require. Cost: cannot model "some wives have property, some don't" — and `financial_dependence_unpropertied` in the MWPA encoding is exactly that split. Heterogeneity within a role is invisible.
2. *Per-agent state.* Each agent carries its own fluent assignment; enabledness is computed per agent. Enables within-role heterogeneity, which the MWPA ranking question (who is hit by the double burden, who is shielded from creditors) needs. Cost: `rules_reference` must be called per agent per step (performance; the reviewer already flagged an O(roles × actions²) loop), and the plan's "import, do not reimplement" line gets harder to honour.
3. *Shared state with per-agent attributes outside the rules* (e.g. a `propertied` flag read by the material module, not by the rules). Middle path; keeps the rules engine role-level but lets the ABM split a role.

**Recommendation.** Option 1 for the three gate institutions (footbinding, naming, kibbutz — none need within-role splits). Decide between 2 and 3 before the MWPA layer-2 run, because that run does need it. Do not decide it now.

### A3. How a pledge is represented
**Why it comes up.** The footbinding collapse story (and the naming-convention tipping) runs on pledges: a committed minority publicly commits, others condition on the share of pledgers. The rules schema has actions and obligations but no "pledge" primitive.

**Options.**
1. *Naming convention*: an action whose name ends in `_pledge` is treated as a pledge by the ABM (current proposed default; not yet implemented). Zero schema change. Cost: magic string; a reviewer can miss it; encoding faithfulness depends on a name.
2. *`ActionDecl` flag* (`pledge: true`). Explicit, validated, visible in the schema. Cost: schema change touches layer 1 (validation, docs, the `_gen_*.py` generators), and the flag is meaningless to the solver — it exists only for layer 2.
3. *Pledge as a derived fluent*: an action that sets a public fluent (`pledged(r)`) which other agents' thresholds read. No new primitive; it is just an action with an effect, and "public" is what makes it a pledge. Cost: the ABM must know which fluents are observable by neighbours, which is itself a new concept.

**Recommendation.** Option 3 is the most faithful to the theory (a pledge is a visible commitment, nothing more), but option 1 ships faster for gate test (b). Suggest 1 now, documented as a stand-in, with 3 as the target. Flag: gate (b) says "no hand-tuned constant"; a naming convention is not a constant, but the threshold distribution agents use is — that is covered under A6.

### A4. Breach: are `must` rules always followed?
**Why it comes up.** Slice 1 agents always obey `must`. That makes the trust mechanism (trust rises when a neighbour keeps an obligation, falls when they breach) dead code, and it means graduated sanctions — one of the plan's listed deliverables — have nothing to act on. It also means no institution can collapse by people stopping doing what they must; only by `may` choices.

**Options.**
1. *Always obey* (current). Simple; obligations are constraints, not choices. Enables none of: sanction dynamics, trust dynamics, collapse-by-defection. Footbinding collapse must then be modelled entirely through `may` choices, which may be wrong — unbinding was a breach of a norm, not an exercise of a permission.
2. *Breach as a choice with a sanction*: an agent may breach a `must` when its payoff exceeds the expected sanction (`or_else` from the rules gives the sanction's existence; its weight is a parameter). Enables sanctions, trust, defection-driven collapse. Cost: one more hand parameter (sanction weight) to sweep; and `or_else: null` (no sanction) rules become freely breachable, which is the ADR 0013 reading of "disability", so this is at least consistent with layer 1.
3. *Breach only for norms, not laws*: distinguish rule types (the kibbutz R2 was re-encoded as a sanctioned norm in the third review). Norms breachable, laws not. Enables the kibbutz regendering test as designed. Cost: the schema must carry the norm/law distinction consistently, which only kibbutz currently does.

**Recommendation.** Option 2, because without it two of the four gate tests (footbinding, kibbutz) cannot run on the mechanism the theory describes. Option 3 is a refinement to add once the norm/law tag exists across the dataset.

### A5. Trust semantics
**Why it comes up.** Code: my trust in neighbour n rises when n keeps *n's own* obligation. Plan (lines 45–46): trust rises when n keeps an obligation *bearing on me*. These differ when obligations are directed (a husband's obligation to support bears on the wife; the wife observing the husband keep an obligation to the state does not).

**Options.**
1. *Own-obligation* (code). Easy to compute (no directedness needed). Models general reputation. Cost: not what the plan says; cannot distinguish "reliable to me" from "reliable in general", which matters for care relationships (the care+control cluster is about directed obligations).
2. *Bearing-on-me* (plan). Needs each obligation to name whom it bears on. The schema has `arg_roles` on actions, which may be enough: an obligation whose action takes my role as an argument bears on me. Enables directed trust, which is what the theory's care relationships need. Cost: obligations with no role argument (obligations to the state, to oneself) contribute nothing to trust.
3. *Both*, weighted. More parameters.

**Recommendation.** Option 2, derived from `arg_roles`, because it is the plan's reading and it uses an existing schema field. Until A4 is settled this is moot (no breaches, so trust never changes), so it can wait for A4.

### A6. Actions with no `may`/`must` rule never fire
**Why it comes up.** Strict ADR 0013 reading: an action is available only if some rule enables it. So in the kibbutz encoding `neglect` can never happen (no rule says anyone may neglect), and the metapelet role has no action at all (its rule R3 is a state obligation, not an action). The reviewer and builder both flagged this.

**Options.**
1. *Strict* (current). Faithful to ADR 0013 and to layer 1. Cost: things nobody is permitted to do cannot happen in the simulation, so breaches that are not themselves rule-named are impossible. That makes collapse-by-doing-the-forbidden-thing unreachable (overlaps with A4).
2. *Default-available*: any declared action is available unless a `must_not` or disability bars it. Matches ordinary life (you can do what no rule mentions). Cost: diverges from layer 1's enabledness, which is the one thing the plan says not to reimplement; also makes "what the rules enable" and "what agents do" come apart, which weakens the claim that the ABM is a simulation *of the rules*.
3. *Strict, plus breach* (A4 option 2 handles the forbidden; this handles the unmentioned by adding explicit `may` rules in the encoding where the institution really does leave something open). Keeps layer 1 and layer 2 on the same enabledness. Cost: encodings must say more; kibbutz needs a `may neglect` (or the regendering story must run on something else).

**Recommendation.** Option 3. It keeps the single enabledness source, and the cost (richer encodings) is work that improves the dataset anyway. The kibbutz encoding then needs a review pass before gate (c).

### A7. Parameters: DEFAULT_PARAMS are hand-set
`copy_rate 0.3, floor 1.0, floor_cost 0.5, initial_surplus 2.0, default_payoff 1.0, trust_delta 0.1, trust_beta 2.0, initial_trust 0.5` — no source. Plan line 92 says parameters are swept, not calibrated; gate (b) forbids a constant that sets the tipping location. Not a decision so much as a rule to hold the builder to: every result in a report must be a rate over a sweep, never a single point. Reviewer's fix list already asks for sweep ranges per parameter. **Author input needed only if you want a different rule.**

---

## B. Documentation and process

### B1. Which theory.md is canonical
**Why.** `docs/theory.md` header says the Claude doc is canonical and local edits are overwritten. plan.md says "make this file canonical once it stabilises". The local file is stale (says 9 institutions, 36/36, gate deferred; reality 14, 47/47, gate (d) PASS, care+control weakened). README links it without a warning (now added).

**Options.**
1. *Keep Claude doc canonical*: I edit the Claude doc, re-export. Keeps your writing environment. Cost: every agent batch that changes status produces drift until someone re-exports; CI cannot test the theory doc.
2. *Make local canonical now*: delete the header, edit in git, Claude doc becomes a reading copy. Enables CI checks (e.g. the claims-register test could also check theory.md's status cell), agents can fix drift in the same commit that causes it. Cost: you lose the Claude doc's editing surface for theory prose, which is where the thinking happens.
3. *Split*: theory prose stays in the Claude doc (canonical for argument); status/numbers move out of theory.md entirely into claims.md with a pointer. Removes the drift source without moving the prose. Cost: one refactor pass on theory.md.

**Recommendation.** Option 3 — the drift is in status cells, not in the argument; move the status out and the canonical-source question mostly dissolves.

### B2. ADR 0011 (dual-use limits): proposed vs binding
**Why.** intent.md invokes "dual-use limits per ADR 0011" as a binding constraint on what the project will compute or publish; the ADR index and CONTRIBUTING say 0011 is `proposed`, not accepted. A reader sees a commitment that the decision record says is not yet made.

**Options.**
1. *Accept 0011* as is. Makes the intent doc true. Cost: whatever 0011 actually commits you to — it needs a read before accepting; I have not read its body.
2. *Soften intent.md* to "proposed limits (ADR 0011, not yet accepted)". True today; weaker signal to a reader about what the project refuses to do.
3. *Accept with amendments* after a read.

**Recommendation.** Read 0011 (five minutes), then 1 or 3. Publishing anything (your launch question) before this is accepted means publishing with no stated dual-use stance.

### B3. ADR 0010 says the strand-tag question is "answered"
**Why.** The third review found strand tags are hand inputs the cluster match depends on; claims L11 is now `refuted`; plan.md parks a strand-tag redesign. ADR 0010 still reads as if settled. The consistency review already noted this.

**Options.**
1. *Amend 0010*: add a "Status: amended 2026-11-03" section pointing at L11 and the parked redesign. Honest, minimal.
2. *Supersede*: new ADR for the strand-tag redesign when it exists; 0010 marked superseded then. Cleaner, but leaves the contradiction standing until the redesign is designed.
3. *Leave it*; rely on claims.md. Cost: a reader of the ADRs gets the wrong picture.

**Recommendation.** 1 now, 2 later. ADR 0010 lives in both repos (split pending per plan.md housekeeping), so the amendment goes in both.

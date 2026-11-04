# computational-liberation

A general theory of liberation, made checkable. Liberation is turning imposed bundles into chosen ones, so that real freedom and non-domination grow, starting with the people who have the least of them. A bundle is a set of goods, roles or duties packaged together by law, economics or norm; oppression is what happens when scarcity seeds a bundle, power ties extra strands onto it, norms lock it, and it outlives its reasons. Liberation starts when surplus makes room to see the bundle as a bundle and assurance lets people leave it together. The theory's job is to say how bundles form, how they break, and which change to make first, and to say it in a form that can be wrong: institutions are encoded as rules, expected verdicts are written before any run, and every result ships as a plain sentence plus the formal certificate behind it. Freedom (exit, voice, recognition, non-domination) and flourishing are scored as separate modules, and disagreement between them is reported, not resolved.

**Status:** research in progress. The first gate claim (that the engine rediscovers the care+control cluster from the rules alone) was retracted after the skeptical review; the dataset is being re-encoded under ADR 0013. See the [claims register](docs/claims.md) for what is currently supported, weakened, refuted or untested. Apache-2.0.

## Read

- [Theory](docs/theory.md): core thesis, how oppression forms, how liberation starts, prioritizing, downstream consequences, precedents, non-human liberation.
- [Intent](docs/intent.md): what this is for, what counts as liberation, and what would convince the author the frame is wrong.
- [Plan](docs/plan.md): the thin path, what is parked, standing process.
- [Claims register](docs/claims.md): one row per claim, with evidence and status.
- [Reviews](docs/reviews/): council reports after each batch.
- [Decisions (ADRs)](docs/decisions/): theory and process decisions; engine-mechanics ADRs are indexed there and live in philosophy-engine.
- [Plans](plans/): institutions Phase 0, batch 2, backtest data inventory, layer 2 agent-based model.
- [Glossary](docs/glossary.md).
- [philosophy-engine](https://github.com/reeswrites/philosophy-engine): the engine that formalizes, checks (Z3) and compares arguments and institutions. This repo supplies the theory and the `data/institutions` family; the engine supplies the code.

## Run

This repo has no code of its own. It depends on philosophy-engine as an editable uv path dependency at `../philosophy-engine`, so check both out as siblings:

```
git clone https://github.com/reeswrites/philosophy-engine
git clone https://github.com/reeswrites/computational-liberation
cd computational-liberation
uv sync
uv run phil families            # lists data/*/ families found here
uv run phil rules check-all     # every institution's expected verdicts against Z3
uv run phil rules gate          # rediscovery gate (informational while re-encoding)
```

The engine resolves `data/` and `runs/` from the current working directory (`PHIL_DATA_DIR` / `PHIL_RUNS_DIR` override), so run `uv run phil ...` from inside this repo. `data/institutions/` is a placeholder until the re-encoded dataset moves here from the engine.

## Process

Expected verdicts are preregistered before any run and never edited to match results; disagreement is recorded ([CONTRIBUTING.md](CONTRIBUTING.md)). After every batch a council of fresh agents, never the builder, reviews correctness, consistency, scope and encoding faithfulness ([ADR 0014](docs/decisions/0014-review-council.md)); its reports go in [docs/reviews/](docs/reviews/) and the claims register is updated from them.

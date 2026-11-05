# 0017. Sourcing standard: structured provenance, primary sources for ground truth

Status: proposed 2026-11-05 (author to accept). Plan: plans/sourcing.md.

## Context
The "rediscover known findings" falsifier compares the engine against history. If the history is our own encoding of half-read sources, the test checks the engine against itself. A read-only audit (2026-11-05) found every rule has a free-text `source` and the `UNVERIFIED` convention (CONTRIBUTING §3) is followed, but 121 of 211 rule rows are UNVERIFIED, citations are pasted repeatedly with no bibliography, `docs/claims.md` records engine evidence only, and the facts the falsifier leans on are the weakest: MWPA dates come from a 2007 working-paper draft and three date lists disagree; the US MWPA chain ends in a rule sourced to the English Married Women's Property Act 1882 and inherits an exit bar sourced to England's Matrimonial Causes Act 1857; the police/CPS practice norms the care+control match reads are unsourced. L24 already showed that code-reading reviews miss what opening the source catches (24 unfaithful rows found only by fetching the texts).

## Decision
1. **Bibliography.** Every cited work has one entry in `data/sources/*.yaml` with a `type` (statute, regulation, case, treatise, archival, secondary, web, dataset). YAML with CSL-like field names, not BibTeX, because the dataset is YAML and the checks are Python; export to CSL-JSON or BibTeX is a script away when a paper needs it.
2. **Structured provenance per rule.** Each rule carries `provenance`: `source_id`, `pin`, `jurisdiction`, `effective_date`, `verification` (opened | snippet | recalled | unverified), and `excerpt` (required when `opened`). The free-text `source` stays until migration is reviewed. Provenance is for readers and CI; the engine JSON does not carry it, so verdicts cannot depend on it.
3. **Levels mean what was read, not what is believed.** `opened` means the cited passage was read in full and quoted. A search-engine summary is a lead, not a snippet. Nothing is upgraded from memory, and a row whose history says it was read but kept no quote is `recalled` until reopened.
4. **Ground truth is primary.** A backtest date is `settled` only when one opened primary source (the statute, the case, the session law) states it, or two opened, independent secondary works agree. Otherwise it is `conflict` or `unresolved`, and a backtest result that rests on it says so.
5. **Jurisdiction must match the encoded institution.** A rule in a US entry is not sourced to an English statute; where the history is English, the entry is English, or the rule is split into separate entries.
6. **Conflicts are recorded, not resolved silently.** Disagreeing sources each keep their own provenance item with the date they report; choosing one is a recorded decision with its reason.
7. **Claims carry sources.** `docs/claims.md` has a `Sources` column (rule rows, works, `engine-only`, `uncited`), separate from engine evidence. Once migration is reviewed, a `supported` claim resting on any row below `opened` fails CI and is downgraded, with the downgrade logged in the register.
8. **Review.** The council after each sourcing batch includes a seat that samples `opened` rows at random and checks the excerpt against the source.

## Consequences
- Most rows start below `opened`; that is the honest starting count, not a regression.
- Checks 4-5 in plans/sourcing.md are warnings until migration is reviewed, then hard. Promoting them may turn claims from supported to weakened; that is the point.
- Verifying sources needs network access to statute and archive hosts; a session that cannot fetch pages can build lists and leads but cannot upgrade a row.
- Lineage work (plans/sourcing.md, Part 2) inherits this standard. Trait codings on a tree need sourced, dated, jurisdiction-specific provenance, and borrowing between legal systems (Galton's problem) must be recorded as such, not read as independent invention.

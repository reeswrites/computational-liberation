# Brief for the verification pass (paste into a session that can open web pages)

Run this on a machine whose network reaches statute and archive hosts (a local Claude Code session, or a cloud environment with these hosts allowed: law.cornell.edu, leginfo.legislature.ca.gov, babel.hathitrust.org, archive.org, avalon.law.yale.edu, lldc.mainelegislature.org, msa.maryland.gov, chicagounbound.uchicago.edu, digitalcommons.nyls.edu, legislation.gov.uk, books.google.com, ssrn.com). Branch: `claude/sourcing-citation-overhaul-ax7rv8`.

---

You are verifying sources for computational-liberation. Read plans/sourcing.md (data model, verification levels), ADR 0017, and the two worklists (plans/sourcing-worklist-mwpa.md, plans/sourcing-worklist-other.md).

Rules:
- `opened` only after reading the cited passage in full; paste a short verbatim quote into `excerpt`, set `accessed` and `url` to the copy read. A search snippet is at most `snippet`; a search-engine summary changes nothing.
- Never upgrade from memory. If the passage does not say what the rule says, do not edit the rule to match: record the mismatch in the provenance `note`, set the level for what was read, and list the row under "Faithfulness findings" in plans/sourcing.md for the author.
- Conflicting sources keep one provenance item each with `date_reported`; set a ground-truth event `settled` only under ADR 0017 point 4.
- Any change to a rule (not just its provenance) is preregistered first: write the expected verdict changes in plans/sourcing.md and commit before running `phil rules check-all`; record drift, never edit predictions.
- After each batch: `uv run python data/institutions/build.py --check`, `uv run pytest -q`, `uv run phil rules gate`, `uv run phil rules diff --baseline data/verdicts-baseline.json`.

Order:
1. coverture-household R6 (wife's exit bar; load-bearing for claim L1 and inherited by all six mwpa-* entries). Open Shanley 1989 and/or Stone 1990, or a US source per worklist option B1. Decide nothing about B2/B3 (author's call); report what the sources support.
2. The other eight rows the care+control match reads: coverture R2, R5; police-crisis R2, R3, R4; cps R3, R4, R10. Each to `opened` with an excerpt (most cite Blackstone or Cal. WIC 5150/306/361, already fetched once with no excerpt kept).
3. MWPA ground truth: published GLT 2012 (J. Law & Econ. 55(4)) and Geddes & Tennyson 2013 dates; then ME 1844 c.117 / 1855, MA 1845 c.208 / 1855 c.304 / 1874 c.184, IL 1861 / 1869, MD 1842-session ch.293, NY 1848 ch.200 / 1860 ch.90 / 1862 ch.172. Then mwpa-suit R16 (US standing source; note the MA act excludes suits between spouses).
4. Police/CPS rows flagged as possibly wrong: cps R1 (Penal Code 11165.14 pin), cps R8 (counsel appointed on petition, not investigation; 317(c)(1) exception), cps R11 (WIC 388(a)(1) "himself or herself"), police R8 (WIC 5275 as amended 2023; set effective_date).
5. Kibbutz R2/R6, footbinding (Mackie 1996), naming-convention (Centola et al. 2018), theory.md items.

Finish with: per-level counts before/after, the faithfulness findings, any preregistered rule change and its run, and a council seat (fresh agent) that samples ten `opened` rows at random and checks each excerpt against the source.

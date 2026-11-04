# Consistency council, restart item 3 (2026-11-04)

Fresh agent, consistency seat (ADR 0014). Not a builder. Nothing committed; docs/plan.md, engine code and institutions.json untouched.

## 1. "Sources opened" vs "never opened"
Found. plans/layer2-abm.md:125 (old heading): "## Sources opened", listing Granovetter, Centola 2018, Mackie 1996, Skyrms, Axelrod, Mesa, Ostrom. Entries in data/institutions/institutions.json (`footbinding`, `footbinding-no-pledge`, `naming-convention`): "the article itself not opened", "read 2026-11-04 as search snippets only, pages not opened", "the page could not be opened from this session", and "plans/layer2-abm.md records these sources as opened on 2026-11-03 by the planning session; this entry's encoder could not reopen them". data/institutions/README.md:253 "no page could be opened from the session"; :286 "every host refused". The encoding review (2026-11-04-footbinding-naming-encoding-review.md) flagged the same conflict.
Changed: plans/layer2-abm.md:125 now "Sources cited (not verified as opened)" with a note that the entries are the source of truth and that this plan has no record of what was actually read.
Open: whether the planning session truly opened anything on 2026-11-03 is unknowable from the repo (no log). Treated as unverified, the conservative reading. data/institutions/README.md:271 still says the plan "lists Mackie and Centola as opened"; now stale-but-harmless (it describes the old wording); not edited since the file was out of the stated scope.

## 2. ADR 0011 status across repos
Found. File contents are byte-identical in both repos (diff empty); both say "Status: Accepted 2026-11-03". The disagreement was the engine index: philosophy-engine/docs/decisions/README.md:31 said "proposed". Git: computational-liberation index fixed in cadb932 (2026-11-04 20:28 -0500, "ADR 0011 index row: accepted (file already said so)"); the engine README last changed in 33ad991 (2026-11-03 19:06). So the engine index was stale.
Changed: philosophy-engine/docs/decisions/README.md:31 to "accepted".
Open: ADR 0012 is "proposed" in both repos and both indexes (consistent). The 0011 file's own wording ("The license decision is deferred ... Accepted ... Apache-2.0") is a little self-contradictory but identical in both repos.

## 3. Engine ADR index lacks 0015, 0016
Changed: philosophy-engine/docs/decisions/README.md:35-36, two rows in the existing table format, linking to the computational-liberation GitHub blob URLs, titles from the CL index, marked "lives in computational-liberation", status accepted (matches the CL index and the ADRs' own status).
Open: the engine index has no "other repo" section header, and its intro still says "for the institutions data family"; the rows are appended to the single table. The URLs assume branch `main` and the repo path reeswrites/computational-liberation (taken from the CL index and engine README). 0013 row uses a plain relative link as before.

## Not touched
docs/claims.md (no claim text depended on these three items). Engine repo changes are uncommitted.

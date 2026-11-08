# DRAFT for the author: consent and sexual-violence guard note for marriage-adjacent encodings

Mirrors ADR 0005: a gate (a bare iso: true across the human/non-human line fails) plus a claim limit (structural only, never moral equivalence). Final form: Context / Decision / Alternatives / Consequences / Status. Must be accepted before any in-scope entry runs (marriage-bundle.md, line 12).

## 1. Scope
- Covers: marital rape exemption (Hale's doctrine) and its repeal chain; affirmative-consent vs force-based definitions; sodomy, adultery, bigamy statutes. [author to confirm]
- Question: do hospital visitation and the SSI marriage penalty fall under this note, or only the first group? They are marriage-adjacent but not sexual; default proposal is "first group only". [author to decide]

## 2. What the engine may and may not be read as saying
- Encodings state what a rule set permits or forces. They make no forward claim about what a law will do or should do. [author to confirm]
- Nothing here is read as "the engine says X is acceptable", or as ranking harms. Mirrors ADR 0011 and ADR 0005's "structural only". [author to confirm]
- A non-match of the statutes to the care+control cluster is a structural finding, not a verdict on the conduct they regulate. [author to confirm]

## 3. Source handling
- Primary legal texts only (statutes, cases) for the exemption and its repeal; secondary sources only for dates cross-checked against them. [author to confirm]
- No survivor testimony as a rule source; it is not a statement of what a rule says. Question: may it appear in notes as context? [author to decide]
- Hale: cite as the doctrine's attributed origin, with the primary text and edition named; where its attribution or reading is disputed, record rival readings in notes per ADR 0008. [author to confirm]

## 4. Language rules for `plain` lines and cards
- Neutral legal register: name the rule, not the act. [author to confirm]
- Use the statute's own term once, then a neutral one; no euphemism, no graphic detail, no sensational phrasing. [author to confirm]
- A plain line says what the rule permits or forces, and nothing about the people affected. [author to confirm]

## 5. Review
- Encoding-faithfulness seat checks sourcing and language rules; card-only seat checks the plain lines read neutrally and match the formal rule (ADR 0014). [author to confirm which seat owns compliance]
- Each in-scope entry cites this note in its `notes`. [author to confirm]

## 6. What triggers a stop
- A line, card or report reads as a claim that an act is acceptable. [author to confirm]
- A rule rests on testimony, or on a source not primary. [author to confirm]
- Any proposal to simulate affected people (ADR 0008, 0011). [author to confirm]

## Author decisions needed to finalize
(a) scope of visitation/SSI; (b) testimony in notes or banned outright; (c) Hale citation form; (d) owning review seat; (e) stop triggers; (f) accept, with date, as an ADR number.

## Settled so far

- (a) Scope, author 2026-11-08: the note covers the sexual-conduct entries only (marital rape exemption, consent definitions, sodomy/adultery/bigamy statutes). Hospital visitation and SSI are marriage-adjacent but not in scope; their entries cite this ruling in `notes`. Must be final before marriage batch 2.

## Recommendations for (b)–(f) (assistant, 2026-11-08; for the author)

These are proposals. Each decision is yours; nothing below is settled until you rule on it.

### (b) Testimony in notes, or banned outright
- Options: (1) ban survivor testimony everywhere in the entry; (2) allow it in `notes` as labelled context, never as a `provenance` source for a rule; (3) allow it only through the `contested` list of ADR 0012.
- Recommendation: option 2, with option 3 named as the route for disagreement about how a rule is read. ADR 0017 already enforces the rule/context split (provenance is for rules; notes are free text), so "not a rule source" is checkable today. An outright ban would sit badly with ADR 0012, which wants people who live under an institution to review encodings, though that ADR is still only proposed.
- Tradeoff: option 2 lets an entry carry context about lived experience, at the cost of a reviewer judging whether a note has drifted into sensational detail (section 4). A ban is easier to check but throws that context away and removes a route ADR 0012 wants.

### (c) Hale citation form
- What the repo does: one bibliography entry per work in `data/sources/rules.yaml`, with `id` as author-year plus a pin slug, `type: treatise`, a title that carries the book and chapter, and `container: null` (see `blackstone-1765-bk1-ch15`). The page pin goes in each rule's `provenance.pin`. The other form in use is a case reporter cite in the title (`Longendyke v. Longendyke, 44 Barb. 366 (...)`).
- Options: (1) treatise entry in the Blackstone pattern: `id: hale-1736-pc-vol1-ch58`, `type: treatise`, title "Historia Placitorum Coronae (The History of the Pleas of the Crown), vol. 1, ch. 58", `author: [Hale, Matthew]`, `year: 1736`, `jurisdiction: England`, note naming the edition read (Emlyn's 1736 edition, published after Hale's death); (2) short legal cite "1 Hale P.C. 629 (1736)" as free text; (3) one entry for the whole work with chapter in the pin.
- Recommendation: option 1, with the page pin (commonly given as 1 Hale P.C. 629) in `provenance.pin`. I have not opened the text, so that pin is `recalled`, not `opened`, per ADR 0017 item 3; it needs reopening against the named edition before it can be called verified. Option 1 matches the existing Blackstone entries, and the edition and date are plainly stated, which the draft already asks for. The repeal chain gets its own entries, each with its own jurisdiction (ADR 0017 item 5: a US entry is not sourced to an English case).
- Tradeoff: option 1 gives one entry per chapter and so more entries than option 3, but keeps pins checkable by the sampling seat. Option 2 is compact but not a bibliography entry, so CI cannot check it.

### (d) Owning review seat
- Options: (1) encoding-faithfulness seat owns the whole note; (2) faithfulness owns sourcing, card-only owns language, one named owner; (3) a new sixth seat.
- Recommendation: option 2, with faithfulness as the single accountable seat. Faithfulness already reads rules against the cited source (ADR 0014), and the note's source rules (section 3) are the same job. Card-only already reads plain lines and decides "cannot tell", which fits section 4 exactly. The ADR 0017 item 8 sampling seat checks `opened` excerpts for these entries as usual.
- Tradeoff: no new seat means no new overhead, but the note's neutrality rules then rely on two existing seats not each assuming the other has it. A new seat would be a clearer owner but adds a reviewer per batch for what is mostly an extension of two existing checks.

### (e) Stop triggers
- Proposed concrete conditions, each of which halts the encoding until the author rules (the draft's section 6 has three vaguer ones; these tighten them):
  1. A `plain` line or card contains a phrase of approval or ranking ("acceptable", "justified", "worse than", "equivalent to") about conduct. Checkable by the card-only seat and by a grep on `plain`.
  2. Any rule row has provenance below `opened` or with a `secondary`/`web` source type for the exemption or its repeal (draft rule: primary only).
  3. A survivor account appears in `provenance` rather than `notes`.
  4. A report or card prints an iso result for these entries without its unmatched list (ADR 0005 gate), or states a match across the care+control cluster as a verdict on the conduct.
  5. Any proposal to simulate affected people.
- Recommendation: adopt all five. Trigger 5 as drafted is stricter than ADR 0011, which bars such simulations "without their participation"; I suggest keeping the stricter form here, as a deliberate choice that you confirm.
- Tradeoff: more triggers mean more halts, and trigger 2 will stop work whenever a repeal date cannot be opened. That is the point of ADR 0017, but it can delay marriage batch 2.

### (f) ADR acceptance
- Next free number: 0019. This repo's last ADR is 0018, and the engine's last is 0013 (the numbering is one sequence across both repos, per `docs/decisions/README.md`). Check that no other pending plan has claimed 0019 first.
- Suggested file: `docs/decisions/0019-consent-guard-note.md`, in the standard five sections, plus an index row in the README.
- Suggested status line, in the style of 0014: "Accepted <date, yours to set>. Covers the sexual-conduct entries only (marital rape exemption, consent definitions, sodomy/adultery/bigamy statutes); hospital visitation and SSI are out of scope (ruling 2026-11-08). Gate: no in-scope entry runs before this is accepted."
- Tradeoff: accepting now unblocks marriage batch 2 but fixes (b)-(e) in an ADR; per the README, changing it later needs a superseding ADR. Leaving it `proposed` keeps it editable but blocks in-scope entries.

### Places the draft differs from the ADRs (for you to resolve)
- Section 6 forbids "any proposal to simulate affected people" citing ADR 0011; ADR 0011 bars it only without participation.
- Section 5 gives sourcing checks to the faithfulness seat; ADR 0017 item 8 adds a separate sampling seat for `opened` rows.
- Section 3 sends rival readings to `notes` "per ADR 0008"; ADR 0012 (proposed) puts disagreements in a `contested` list.

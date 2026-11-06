# Slice 2 goods: independent encodings and merge (2026-11-06)

Protocol: plans/priority-slice2.md section 2. Coordinator merge, not an encoder.

**Bundle.** Built by the coordinator outside both repositories: section 3 of plans/priority-slice2.md verbatim, the property-formula conventions with three style examples (`cannot_contract`, `subject_cannot_exit_persists`, `care_duty_on_women`) and the goods conventions, and per entry the vocabulary only (roles, fluents, actions, initial, initial_free, arg_roles; no rules, cards, verdicts or sections 4-7). Aggregate hash `127e9627fe78b47537b19e7a35fad8b6770f0cfc47188420337103cf357c7cb0`; per-file hashes in `bundle-manifest.sha256`. Validator: `philengine.rules_lower.validate_property` on each entry's vocabulary (syntax and declared fluents only, no verdicts).

**Audit.** Every tool call in both transcripts was listed. Encoder 1: 5 calls; encoder 2: 6 calls. Each read only bundle files, ran only the bundle's validate.sh, and wrote only its own `goods.yaml`. No breach; all five goods count as independent under the protocol.

**Equivalence** (`scripts/goods_equiv.py`: z3 validity of A <-> B, first-order, every fluent uninterpreted, sorts agent and step, `t` free; stronger than per-entry equivalence, since no entry's derived definitions are used):

| good | result | merge |
| --- | --- | --- |
| `cared_for` | equivalent (character-identical) | one `formal`, `contested: []` |
| `mutual_household_care` | equivalent (character-identical) | one `formal`, `contested: []` |
| `known_carer` | equivalent (implication vs disjunction form) | one `formal` (encoder 1), `contested: []` |
| `child_with_family` | equivalent (disjuncts reordered) | one `formal` (encoder 1), `contested: []` |
| `provided_for` | **different** | `formal` = encoder 1 (maintenance only from a husband she is married to); `contested` = encoder 2 (maintenance from anyone who provides care). z3 counterexample: a subject cared for by someone she is not married to, with no means of her own, holds under encoder 2 and not under encoder 1. |

Both encoders recorded nothing as not_expressible. Both kept `has_own_income` (declared only in coverture-floor) in `provided_for`, accepting the constant-false warning elsewhere; both wrote `child_with_family` as one disjunct per entry because no fluent is shared across cps, kibbutz and ectogenesis.

**What the agreement does and does not show.** Pass item "at least 3 goods written independently by a second encoder" is met in form: 5 goods, both encoders, audited. But the two encoders are two instances of the same model given the same bundle, and both copied the one-step grace from the `care_duty_on_women` style example into `cared_for`, `known_carer` and `child_with_family`. Four of five equivalent is therefore weak evidence that goods can be encoded without the encoder's own picture of the good (plans/priority.md "Open questions"): it measures one model's consistency, not agreement between people. Every report says: second encoder: agent, not someone living under the institution (ADR 0012). A stronger test, not run: a human second encoder, a different model family, or a bundle with no style example carrying the grace.

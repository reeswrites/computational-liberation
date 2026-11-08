"""Build institutions.json and properties.json from src/*.yaml.

src/<id>.yaml is the source of truth for one institution; src/properties.yaml for the named properties;
src/_order.yaml lists the institution ids in output order (the JSON is order-sensitive: entry order and key
order are kept exactly). Never hand-edit the JSON.

An entry is either standalone (every field of the engine schema `InstitutionJSON`, plus per rule a `plain`
sentence and optional `choices` note) or a delta:

    extends: <other id>
    rules_drop:    [R1]            # ids removed from the base
    rules_replace: [{id: R2, ...}] # rule with the same id, replaced in place
    rules_add:     [{id: R13, ...}]# appended after the base's remaining rules
    roles_drop / roles_set / roles_add, fluents_*, actions_*   # same three verbs, keyed by name
    keys_drop: [initial]           # top-level keys the base has and this entry does not
    <any other key>: value         # overrides that key wholesale (name, notes, expected_properties, ...)

Order of application: drops, then replaces/sets, then adds, then overrides. `plain`, `choices`, `provenance` and `sanctioner_review`
(`derived` = the rule's `sanctioner` was derived by migration, not yet hand-reviewed) are for human readers; the engine schema does not carry them, so the build strips them before writing JSON (the
engine JSON, ENGINE_PIN and the verdict baseline do not change when provenance does). The same holds for an
entry's top-level `goods_note` (slice-2 goods readings, rendered as a "Goods (slice 2)" card section), which is
never inherited through `extends`.

Each rule may carry `provenance:`, a list of items {source_id, pin, jurisdiction, effective_date, verification,
excerpt, accessed, url, note}; `source_id` names an entry of the bibliography in data/sources/*.yaml and
`verification` is opened | snippet | recalled | unverified (plans/sourcing.md; tests/test_sources.py checks both).
The free-text `source` stays until the migration (migrate_provenance.py) is reviewed.

`--cards` also writes docs/cards/<id>.md (one human-readable card per entry) and docs/cards/README.md, generated
from the same resolved entries; a card's rule table has a `level` column (the weakest provenance item of the row)
and its Sources section lists every provenance item (source id, pin, jurisdiction, date, level, excerpt). `--check` rebuilds JSON and cards into a temp dir and fails on any difference, on a
rule with an empty `plain` or `source`, and on an `extends` cycle.

Composites (ADR 0018, plans/composition.md): src/_composites.yaml lists build-time composites,

    - id: <composite id>
      name: <display name>                      # optional; default the id
      members: [<entry id>, ...]                # resolved entries, after `extends`
      aliases: {<member id>: {<old role>: <new role>}}   # applied per member before union
      initial: [<literal>, ...]                 # extra initial literals (switches the engine to init mode `declared`)
      initial_free: [<fluent>, ...]             # fluents left free at t=0 (added after composition, re-validated)
      expected_properties: {<property>: <verdict>}
      notes: <text>

The engine's `philengine.rules_compose.compose` does the union (bindings frozen, aliases applied, unification table);
build.py appends the result to institutions.json as an ordinary entry carrying `members: [ids]`, after the ordered
entries, and writes a card whose rules table shows each member's rules under their prefixed ids with the member's
`plain`, `source` and provenance re-attached (the engine strips none of them; the build re-attaches them by
(member, rule id) since the engine JSON never carried them). A composition conflict is a build error naming the
member and the field.

Usage (from the comp-lib root):  uv run python data/institutions/build.py [--write] [--cards] | --check
"""
from __future__ import annotations

import argparse
import copy
import difflib
import json
import re
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
CARDS = HERE.parent.parent / "docs" / "cards"
STRIP_RULE_KEYS = ("plain", "choices", "provenance", "sanctioner_review")
STRIP_ENTRY_KEYS = ("goods_note",)  # card-only (plans/priority-slice2.md R2.5): not in the engine JSON
LISTS = ("roles", "fluents", "actions")
RESERVED = {"extends", "rules_drop", "rules_replace", "rules_add", "keys_drop"} | {
    f"{l}_{v}" for l in LISTS for v in ("drop", "set", "add")}


# ---------------------------------------------------------------- YAML in and out
class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # no anchors or aliases in the sources
        return True


def _str(dumper, s):
    return dumper.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)


def _list(dumper, seq):
    flow = all(isinstance(x, (str, int, float, bool)) or x is None for x in seq) and len(repr(seq)) < 72
    return dumper.represent_sequence("tag:yaml.org,2002:seq", seq, flow_style=flow)


_Dumper.add_representer(str, _str)
_Dumper.add_representer(list, _list)


def dump_yaml(obj) -> str:
    return yaml.dump(obj, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1_000_000,
                     default_flow_style=False)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump_json(obj) -> str:
    # Same call as the retired generators: json.dump(x, f, indent=1), then a newline. ensure_ascii and key order
    # are the json defaults / the order of the source.
    return json.dumps(obj, indent=1) + "\n"


# ---------------------------------------------------------------- resolution
def load_sources(src: Path = SRC):
    order = load_yaml(src / "_order.yaml")
    raws = {i: load_yaml(src / f"{i}.yaml") for i in order}
    for i, r in raws.items():
        if r.get("id") != i:
            raise SystemExit(f"src/{i}.yaml: id is {r.get('id')!r}, expected {i!r}")
    return order, raws


def _patch_named(items, drop, sets, add, kind, eid):
    names = {x["name"] for x in items}
    for n in list(drop) + list(sets):
        if n not in names:
            raise SystemExit(f"{eid}: {kind}_drop/_set names unknown {n!r}")
    out = []
    for x in items:
        if x["name"] in drop:
            continue
        if x["name"] in sets:
            x = {**x, **sets[x["name"]]}
        out.append(x)
    return out + copy.deepcopy(list(add))


def resolve(eid, raws, stack=()):
    """The entry with `extends` expanded; rules keep `plain` / `choices`."""
    if eid in stack:
        raise SystemExit("extends cycle: " + " -> ".join(stack + (eid,)))
    if eid not in raws:
        raise SystemExit(f"{stack[-1] if stack else '?'}: extends unknown entry {eid!r}")
    raw = raws[eid]
    if "extends" not in raw:
        return copy.deepcopy(raw)
    e = resolve(raw["extends"], raws, stack + (eid,))
    for l in LISTS:
        e[l] = _patch_named(e[l], raw.get(f"{l}_drop", ()), raw.get(f"{l}_set", {}), raw.get(f"{l}_add", ()), l, eid)
    ids = {r["id"] for r in e["rules"]}
    drop = set(raw.get("rules_drop", ()))
    repl = {r["id"]: r for r in raw.get("rules_replace", ())}
    for rid in drop | set(repl):
        if rid not in ids:
            raise SystemExit(f"{eid}: rules_drop/rules_replace names unknown rule {rid!r}")
    e["rules"] = ([copy.deepcopy(repl.get(r["id"], r)) for r in e["rules"] if r["id"] not in drop]
                  + copy.deepcopy(list(raw.get("rules_add", ()))))
    for k in raw.get("keys_drop", ()):
        e.pop(k, None)
    for k, v in raw.items():
        if k not in RESERVED:
            e[k] = copy.deepcopy(v)
    if "goods_note" not in raw:  # card-only, never inherited: each note names its own entry's readings
        e.pop("goods_note", None)
    return e


def strip(entry):
    e = dict(entry)
    for k in STRIP_ENTRY_KEYS:
        e.pop(k, None)
    e["rules"] = [{k: v for k, v in r.items() if k not in STRIP_RULE_KEYS} for r in entry["rules"]]
    return e


COMPOSITES = "_composites.yaml"
CARD_RULE_KEYS = ("plain", "choices", "provenance", "sanctioner_review")  # re-attached to composite rules for the card


def load_composites(src: Path = SRC) -> list:
    path = src / COMPOSITES
    if not path.exists():
        return []
    specs = load_yaml(path) or []
    for c in specs:
        for k in ("id", "members"):
            if k not in c:
                raise SystemExit(f"{COMPOSITES}: a composite lacks {k!r}")
    return specs


def freeze_action_types(inst):
    """P1b (plans/composition.md): write each action's parameter types as `arg_roles`, resolved by the engine's prefix
    heuristic over the MEMBER's own roles, so that aliasing cannot re-type them (run 1 typed coverture's `h` as
    `hospital`). Parameters already typed keep their type; a parameter the heuristic cannot type stays None."""
    from philengine.rules_lower import literal_roles, var_role
    lits = literal_roles(inst)
    acts = []
    for a in inst.actions:
        given = list(a.arg_roles) if a.arg_roles is not None else [None] * len(a.args)
        typed = [g if g is not None else var_role(p, inst, lits) for p, g in zip(a.args, given)]
        acts.append(a.model_copy(update={"arg_roles": typed}) if any(x is not None for x in typed) else a)
    return inst.model_copy(update={"actions": acts})


def compose_entry(spec: dict, resolved: dict) -> tuple[dict, dict]:
    """(resolved composite for cards, stripped composite for the JSON). Uses the engine's compose(); a ComposeError is a
    build error. `members` must be resolved entry ids (composites of composites are not supported)."""
    from philengine.rules_compose import ComposeError, compose
    from philengine.rules_lower import validate_institution
    from philengine.schemas_rules import InstitutionJSON

    cid = spec["id"]
    members = []
    for mid in spec["members"]:
        if mid not in resolved:
            raise SystemExit(f"{COMPOSITES} {cid}: member {mid!r} is not an entry in _order.yaml")
        members.append(freeze_action_types(InstitutionJSON.model_validate(strip(resolved[mid]))))
    aliases = {m: dict(a or {}) for m, a in (spec.get("aliases") or {}).items()}
    try:
        comp = compose(members, aliases, cid, initial=spec.get("initial") or None,
                       expected_properties=spec.get("expected_properties") or {}, notes=spec.get("notes") or "")
    except ComposeError as e:
        raise SystemExit(f"{COMPOSITES} {cid}: {e}")
    extra_free = [f for f in (spec.get("initial_free") or []) if f not in comp.initial_free]
    if extra_free or spec.get("name"):
        comp = comp.model_copy(update={"initial_free": comp.initial_free + extra_free, "name": spec.get("name") or comp.name})
        errs = validate_institution(comp)
        if errs:
            raise SystemExit(f"{COMPOSITES} {cid}: invalid after initial_free: " + "; ".join(errs))
    stripped = json.loads(comp.model_dump_json())
    # engine defaults that hand-written entries never carry: drop role count when it is the default 1
    for role in stripped.get("roles", []):
        if role.get("count") == 1:
            del role["count"]
    # card view: the member's human-readable rule keys, looked up by (member, original rule id)
    seen: dict[str, int] = {}
    prefixes = []
    for mid in spec["members"]:
        seen[mid] = seen.get(mid, 0) + 1
        eff = mid if seen[mid] == 1 else f"{mid}_{seen[mid]}"
        prefixes.append((eff.replace("-", "_") + "__", mid))
    card_rules = []
    for r in stripped["rules"]:
        r = dict(r)
        for pre, mid in prefixes:
            if r["id"].startswith(pre):
                orig = next((x for x in resolved[mid]["rules"] if x["id"] == r["id"][len(pre):]), None)
                if orig:
                    for k in CARD_RULE_KEYS:
                        if k in orig:
                            r[k] = copy.deepcopy(orig[k])
                    r["member"] = mid
                    # a member's plain line says "(R6)"; on the composite card that id is `<member>__R6`
                    r["plain"] = re.sub(r"\bR(\d+)\b", lambda m: pre + m.group(0), str(r.get("plain", "")))
                break
        card_rules.append(r)
    view = {**stripped, "rules": card_rules, "aliases": aliases}
    return view, stripped


def build_all(src: Path = SRC):
    order, raws = load_sources(src)
    resolved = [resolve(i, raws) for i in order]
    by_id = {e["id"]: e for e in resolved}
    stripped = [strip(e) for e in resolved]
    for spec in load_composites(src):
        if spec["id"] in by_id:
            raise SystemExit(f"{COMPOSITES}: id {spec['id']!r} collides with an entry")
        view, flat = compose_entry(spec, by_id)
        resolved.append(view)
        stripped.append(flat)
        by_id[spec["id"]] = view
        order.append(spec["id"])
        raws[spec["id"]] = {"id": spec["id"], "composite": spec}  # card plumbing: no `extends`, no own rules
    return resolved, stripped, load_yaml(src / "properties.yaml")


# ---------------------------------------------------------------- cards
def _cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def _code(s) -> str:
    return f"`{_cell(s)}`"


SOURCE_INLINE_MAX = 300
_URL = re.compile(r"https?://[^\s)\]]+")

LEGEND = """## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).
"""

KEYWORDS = {"and", "or", "not", "exists", "forall", "true", "false", "=", "imp", "implies"}


def _sexp_lists(s):
    """Every parenthesised list in an s-expression string, as lists of atoms (nested lists kept as None)."""
    toks = re.findall(r"\(|\)|[^\s()]+", str(s))
    stack, out = [], []
    for t in toks:
        if t == "(":
            stack.append([])
        elif t == ")":
            if stack:
                l = stack.pop()
                out.append(l)
                if stack:
                    stack[-1].append(None)
        elif stack:
            stack[-1].append(t)
    return out


def rule_variables(r, e):
    """[(var, role-or-None, via)] for the variables of a rule, from var_roles, then action args, then fluent arg_roles."""
    roles = {x["name"] for x in e["roles"]}
    fl = {f["name"]: f for f in e["fluents"]}
    ac = {a["name"]: a for a in e["actions"]}
    vr = r.get("var_roles") or {}
    seen, inferred = [], {}
    for lst in _sexp_lists(r["aim"]) + _sexp_lists(r["conditions"]):
        if not lst or lst[0] is None:
            continue
        head, args = lst[0], lst[1:]
        for i, a in enumerate(args):
            if a is None or a in roles or a in KEYWORDS or head in KEYWORDS and head != "=":
                continue
            if re.fullmatch(r"-?\d+", a):
                continue
            if a not in seen:
                seen.append(a)
            via = None
            if head in ac and i < len(ac[head]["args"]):
                ar = ac[head].get("arg_roles")
                if ar and i < len(ar):
                    via = (ar[i], f"action {head} arg_roles")
                else:
                    name = ac[head]["args"][i]
                    found = {f["arg_roles"][j] for ef in ac[head]["effects"] for j, x in enumerate(ef["args"])
                             if x == name for f in [fl.get(ef["fluent"])] if f and f.get("arg_roles") and j < len(f["arg_roles"])}
                    if found:
                        via = ("/".join(sorted(found)), f"action {head}, effects")
            elif head in fl and fl[head].get("arg_roles") and i < len(fl[head]["arg_roles"]):
                via = (fl[head]["arg_roles"][i], f"fluent {head}")
            if via and a not in inferred:
                inferred[a] = via
    out = []
    for v in seen:
        if v in vr:
            out.append((v, vr[v], "rule var_roles"))
        elif v in inferred:
            out.append((v, inferred[v][0], inferred[v][1]))
        else:
            out.append((v, None, None))
    return out


def source_cell(r):
    src = " ".join(str(r["source"]).split())
    if len(src) <= SOURCE_INLINE_MAX:
        return _cell(src)
    urls = _URL.findall(src)
    ptr = f"[full source under Sources, {r['id']}](#src-{r['id'].lower()})"
    return ptr + (" " + _cell(urls[0]) if urls else "")


LEVELS = ("opened", "snippet", "recalled", "unverified")  # strongest first (plans/sourcing.md)


def level_cell(r) -> str:
    """The weakest verification level among the rule's provenance items; '-' when it has none."""
    prov = r.get("provenance") or []
    lv = [p.get("verification") for p in prov if p.get("verification") in LEVELS]
    return max(lv, key=LEVELS.index) if lv else "-"


def provenance_line(p) -> str:
    sid = f"`{p['source_id']}`" if p.get("source_id") else "no work named"
    meta = [x for x in (p.get("pin"), p.get("jurisdiction")) if x]
    meta.append(f"date {p['effective_date']}" if p.get("effective_date") else "date n/a")
    lvl = f"**{p.get('verification')}**" + (f" {p['accessed']}" if p.get("accessed") else "")
    if not p.get("source_id"):
        note = re.sub(r"^no work named(?: for this rule)?; ", "", _cell(p.get("note") or ""))
        return f"- {sid}: {lvl}" + (f" ({note})" if note else "")
    out = f"- {sid} ({'; '.join(_cell(m) for m in meta)}): {lvl}"
    if p.get("excerpt"):
        out += f": \"{_cell(p['excerpt'])}\""
    if p.get("url"):
        out += f" <{p['url']}>"
    return out


def deontic_cell(r) -> str:
    d = r["deontic"].replace("_", " ")
    if r["deontic"] == "must_not" and r.get("or_else") is None:
        d += " (disability)"
    if r.get("implicit"):
        d += " (implicit)"
    if r.get("sanctioner_review") == "derived":
        d += " (sanctioner derived, unreviewed)"
    return d


def or_else_cell(r, by_id) -> str:
    oe = r.get("or_else")
    if oe is None:
        return "none"
    t = by_id.get(oe)
    return f"{oe} {_code(t['aim'])}" if t else oe


DELTA_FIELDS = {"expected_properties", "pair", "minimal_pair_of", "notes"}


def _delta_lines(raw, base, e) -> list:
    base_by = {r["id"]: r for r in base["rules"]}
    out = []
    for rid in raw.get("rules_drop", ()):
        out.append(f"- {rid} dropped: {base_by[rid]['plain']}")
    for r in raw.get("rules_replace", ()):
        out.append(f"- {r['id']} replaced: was \"{base_by[r['id']]['plain']}\" now \"{r['plain']}\"")
    for r in raw.get("rules_add", ()):
        out.append(f"- {r['id']} added: {r['plain']}")
    fgloss = {f["name"]: f.get("gloss", "") for f in e["fluents"]}
    kinds = {"roles": "role", "fluents": "fluent", "actions": "action"}
    for l in LISTS:
        k = kinds[l]
        for n in raw.get(f"{l}_drop", ()) or ():
            out.append(f"- removes {k} {n}")
        for n, patch in (raw.get(f"{l}_set", {}) or {}).items():
            words = []
            for pk, pv in patch.items():
                words.append(f"{pk.replace('_', ' ')} becomes {json.dumps(pv) if not isinstance(pv, str) else pv}")
            gl = f" ({fgloss[n]})" if l == "fluents" and fgloss.get(n) else ""
            out.append(f"- changes {k} {n}{gl}: " + "; ".join(words))
        for x in raw.get(f"{l}_add", ()) or ():
            g = x.get("gloss")
            if l == "actions":
                g = "does: " + ", ".join(f"{ef['fluent']}({', '.join(ef['args'])}) := {str(ef['value']).lower()}"
                                         for ef in x.get("effects", ()))
            out.append(f"- adds {k} {x['name']}" + (f" ({g})" if g else ""))
    for k in raw.get("keys_drop", ()):
        out.append(f"- field {k} dropped")
    for k in raw:
        if k in DELTA_FIELDS and k not in RESERVED and raw[k] != base.get(k):
            out.append(f"- overrides {k}")
    return out


def _rename_map(e, t) -> dict:
    return {a["name"]: b["name"] for a, b in zip(t["roles"], e["roles"]) if a["name"] != b["name"]}


def rename_lines(e, resolved) -> list:
    """For a standalone entry declared isomorphic_to another entry with the same rule ids: one line per differing rule."""
    out = []
    if "extends" in e:
        return out
    for x in e.get("isomorphic_to") or ():
        tid = x["id"] if isinstance(x, dict) else x
        t = resolved.get(tid)
        if not t or {r["id"] for r in t["rules"]} != {r["id"] for r in e["rules"]} or len(t["roles"]) != len(e["roles"]):
            continue
        rm = _rename_map(e, t)
        if not rm:
            continue
        word = ", ".join(f"{a}->{b}" for a, b in rm.items())
        out.append(f"Rule-by-rule against [{tid}]({tid}.md) under the rename {word} (declared isomorphic); one line per rule that differs:")
        tby = {r["id"]: r for r in t["rules"]}
        tok = lambda x: re.findall(r"\(|\)|[^\s()]+", x)
        tm = dict(rm)  # token map: role names plus the variables that move with them
        for r in e["rules"]:
            for f in ("attribute", "aim", "conditions"):
                a, b = tok(tby[r["id"]][f]), tok(r[f])
                if len(a) == len(b):
                    for x, y in zip(a, b):
                        if x != y:
                            tm.setdefault(x, y)
        n = 0
        for r in e["rules"]:
            tr = tby[r["id"]]
            diffs, only = [], True
            for f in ("attribute", "aim", "conditions"):
                if r[f] != tr[f]:
                    ren = " ".join(tm.get(w, w) for w in tok(tr[f])).replace("( ", "(").replace(" )", ")")
                    only = only and ren == r[f]
                    diffs.append(f"{f} `{tr[f]}` -> `{r[f]}`")
            if diffs:
                n += 1
                out.append(f"- {r['id']}: " + "; ".join(diffs) + (" (rename only)" if only else " (differs beyond the rename)"))
        if not n:
            out.append(f"- no rule differs in attribute, aim or conditions ({len(e['rules'])} rules identical)")
        else:
            out.append(f"- the other {len(e['rules']) - n} rules are identical in attribute, aim and conditions")
    return out


def pair_lines(e, raws, resolved) -> list:
    """Diff against the base for a delta entry; the entries extending it for a base entry; pair fields in words."""
    raw = raws[e["id"]]
    out = []
    base_id = raw.get("extends")
    if base_id:
        out.append(f"Extends [{base_id}]({base_id}.md); one line per change:")
        out += _delta_lines(raw, resolved[base_id], e)
    else:
        kids = [i for i, r in raws.items() if r.get("extends") == e["id"]]
        if kids:
            out.append("Extended by: " + ", ".join(f"[{k}]({k}.md)" for k in kids))
        out += rename_lines(e, resolved)
    mp = e.get("minimal_pair_of")
    if mp:
        if mp.get("differs_on"):
            diff = f"; the pair differs on property {mp['differs_on']}"
        else:
            diff = "; no layer-1 property separates the pair" if "differs_on" in mp else ""
        out.append(f"Minimal pair of [{mp['id']}]({mp['id']}.md), differing in rule {mp.get('rule', '?')}{diff}.")
    for i, r in resolved.items():
        m = r.get("minimal_pair_of")
        if m and m["id"] == e["id"]:
            out.append(f"[{i}]({i}.md) is a minimal pair of this entry (rule {m.get('rule', '?')}).")
    for key, word in (("isomorphic_to", "Isomorphic to"), ("not_isomorphic_to", "Not isomorphic to"),
                      ("not_isomorphic_to_control", "Contrasts with controls")):
        v = e.get(key) or []
        if v:
            items = [(x["id"] + (f" ({x['level']})" if x.get("level") else "")) if isinstance(x, dict) else x
                     for x in v]
            out.append(f"{word}: {', '.join(items)}")
    return out


def card(e, raws, resolved, props) -> str:
    raw = raws[e["id"]]
    by_id = {r["id"]: r for r in e["rules"]}
    own = {}
    for k, tag in (("rules_add", "added"), ("rules_replace", "replaced")):
        for r in raw.get(k, ()):
            own[r["id"]] = tag
    L = [f"# {e['id']}", "", f"**{e['name']}**", "", "> " + " ".join(str(e.get("source_text", "")).split()), "",
         LEGEND]
    if e.get("members"):
        spec = raw.get("composite", {})
        L += ["## Members", "", "A composite (ADR 0018): the members' roles are unioned after the aliases below, fluents "
              "unified by name, rules concatenated under `<member>__` prefixes. Each rule row below is the member's rule, "
              "unchanged except for the renamed roles; its plain line and sources are the member's.", ""]
        for mid in e["members"]:
            am = (spec.get("aliases") or {}).get(mid) or {}
            al = ", ".join(f"{o} → {n}" for o, n in am.items()) or "no aliases"
            L.append(f"- [{mid}]({mid}.md): {al}")
        if e.get("initial"):
            L += ["", "Initial literals: " + ", ".join(f"`{x}`" for x in e["initial"])
                  + (" (init mode `declared`; fluents not listed start false)" if e["initial"] else "")]
        if e.get("initial_free"):
            L += ["", "Free at t=0: " + ", ".join(f"`{x}`" for x in e["initial_free"])]
        rev: dict[str, list[str]] = {}
        for mid in e["members"]:
            for o, n in ((spec.get("aliases") or {}).get(mid) or {}).items():
                rev.setdefault(n, []).append(f"{o} in {mid}")
        if rev:
            L += ["", "Role map: " + "; ".join(f"**{n}** = {' = '.join(v)}" for n, v in rev.items())]
        L += ["", "Actions (name(parameters): what they set; a member's rules permit, oblige or bar them):"]
        for a in e["actions"]:
            eff = ", ".join(f"{'' if x['value'] else 'not '}{x['fluent']}({', '.join(x['args'])})" for x in a.get("effects", [])) or "no effect"
            tr = [f"{p}: {r}" for p, r in zip(a["args"], a.get("arg_roles") or []) if r]
            L.append(f"- `{a['name']}({', '.join(a['args'])})`" + (f" [{'; '.join(tr)}]" if tr else "") + f": {eff}")
        L.append("")
    L += ["## Roles", ""]
    L += [f"- **{r['name']}**: {_cell(r.get('gloss', ''))}" for r in e["roles"]]
    L += ["", "## Rules", "",
          "| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in e["rules"]:
        rid = r["id"] + (f" ({own[r['id']]})" if r["id"] in own else "")
        L.append("| " + " | ".join([
            rid, r["attribute"], deontic_cell(r), _code(r["aim"]), _code(r["conditions"]), or_else_cell(r, by_id),
            r.get("strand") or "untagged (null)", _cell(r["plain"]), level_cell(r), source_cell(r)]) + " |")
    dc = [a["name"] for a in e["actions"] if a.get("default_capacity")]
    L += ["", "**Default capacities** (an action a person of that kind can do unless an express disability removes it): "
          + (", ".join(dc) if dc else "none"), "", "## Variables", ""]
    for r in e["rules"]:
        vs = rule_variables(r, e)
        if not vs:
            L.append(f"- {r['id']}: no variables")
            continue
        L.append(f"- {r['id']}: " + "; ".join(
            f"`{v}` = {role} ({via})" if role else f"`{v}` = unbound (encoder to fix)" for v, role, via in vs))
    listed = [r for r in e["rules"]
              if len(" ".join(str(r["source"]).split())) > SOURCE_INLINE_MAX or r.get("provenance")]
    if listed:
        L += ["", "## Sources", "",
              "Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in "
              "`data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). "
              "The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.", ""]
        for r in listed:
            src = " ".join(str(r["source"]).split())
            if len(src) > SOURCE_INLINE_MAX:
                L += [f'<a id="src-{r["id"].lower()}"></a>', f"**{r['id']}**: " + src]
            else:
                L += [f"**{r['id']}**"]
            L += [""] + [provenance_line(p) for p in r.get("provenance") or ()] + [""]
    if e.get("goods_note"):
        L += ["", "## Goods (slice 2)", "", " ".join(str(e["goods_note"]).split())]
    L += ["", "## Expected properties", "",
          "| property | kind | expected | meaning |", "|---|---|---|---|"]
    pm = {p["name"]: p for p in props}
    for name, verdict in e.get("expected_properties", {}).items():
        p = pm.get(name, {})
        L.append(f"| {name} | {p.get('kind', '?')} | {verdict} | {_cell(p.get('gloss', ''))} |")
    L += ["", "## Pairs", ""]
    L += pair_lines(e, raws, resolved) or ["No pair relations."]
    L += ["", "<details><summary>Encoder notes (engine internals)</summary>", "", e.get("notes", "").rstrip(), "",
          "</details>", ""]
    return "\n".join(L)


def partners(eid, raws, resolved) -> list:
    out = []
    base = raws[eid].get("extends")
    if base:
        out.append(f"{base} (extends)")
    out += [f"{i} (extended by)" for i, r in raws.items() if r.get("extends") == eid]
    seen = {x.split(" ")[0] for x in out}
    mp = resolved[eid].get("minimal_pair_of")
    if mp and mp["id"] not in seen:
        out.append(f"{mp['id']} (minimal pair)")
        seen.add(mp["id"])
    for i, r in resolved.items():
        m = r.get("minimal_pair_of")
        if m and m["id"] == eid and i not in seen:
            out.append(f"{i} (minimal pair)")
            seen.add(i)
    return out


def render_cards(order, raws, resolved_list, props) -> dict:
    resolved = {e["id"]: e for e in resolved_list}
    files = {f"{i}.md": card(resolved[i], raws, resolved, props) for i in order}
    idx = ["# Institution cards", "",
           "Generated by `data/institutions/build.py --cards` from `data/institutions/src/`. Do not edit.", "",
           "How to read a card: every card opens with the same Legend (what may / must / must not, disability, "
           "implicit, strands, default capacity, or else and k mean); see the Legend at the top of any card, e.g. "
           "[lease](lease.md#legend), and `docs/glossary.md`.", ""]
    for i in order:
        p = partners(i, raws, resolved)
        idx.append(f"- [{i}]({i}.md): {resolved[i]['name']}" + (f" | pairs: {'; '.join(p)}" if p else ""))
    files["README.md"] = "\n".join(idx) + "\n"
    return files


def write_cards(out: Path, files: dict):
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.md"):
        if f.name not in files:
            f.unlink()
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")


def cards_problems(files: dict, out: Path = CARDS) -> list:
    errs = []
    have = {f.name for f in out.glob("*.md")} if out.exists() else set()
    for name in sorted(set(files) | have):
        if name not in files:
            errs.append(f"docs/cards/{name} is stale (no such entry); run build.py --write --cards")
        elif name not in have:
            errs.append(f"docs/cards/{name} is missing; run build.py --write --cards")
        elif (out / name).read_text(encoding="utf-8") != files[name]:
            errs.append(f"docs/cards/{name} differs from the build of src/; run build.py --write --cards")
    return errs


# ---------------------------------------------------------------- commands
def problems(resolved, require_plain):
    errs, warns = [], []
    for e in resolved:
        for r in e["rules"]:
            where = f"{e['id']} {r['id']}"
            if not r.get("source"):
                errs.append(f"{where}: empty source")
            if not r.get("plain"):
                (errs if require_plain else warns).append(f"{where}: empty plain")
    return errs, warns


def _order_and_raws(resolved):
    """Order and raw sources for the card renderer, composites included (their raw is a stub carrying the spec)."""
    order, raws = load_sources()
    for e in resolved:
        if e["id"] not in raws:
            raws[e["id"]] = {"id": e["id"], "composite": next(c for c in load_composites() if c["id"] == e["id"])}
            order.append(e["id"])
    return order, raws


def write(out: Path, inst, props):
    (out / "institutions.json").write_text(dump_json(inst), encoding="utf-8")
    (out / "properties.json").write_text(dump_json(props), encoding="utf-8")


def check():
    resolved, inst, props = build_all()
    order, raws = _order_and_raws(resolved)
    errs, _ = problems(resolved, True)
    with tempfile.TemporaryDirectory() as td:
        write(Path(td), inst, props)
        for name in ("institutions.json", "properties.json"):
            new = (Path(td) / name).read_text(encoding="utf-8")
            old = (HERE / name).read_text(encoding="utf-8")
            if new != old:
                d = list(difflib.unified_diff(old.splitlines(), new.splitlines(), f"committed/{name}", f"built/{name}", lineterm="", n=1))
                errs.append(f"{name} differs from the build of src/ ({len(d)} diff lines); run build.py --write\n" + "\n".join(d[:30]))
        # Regenerate the cards into a temp dir and compare the whole set with docs/cards, so a stale or stray card fails.
        write_cards(Path(td) / "cards", render_cards(order, raws, resolved, props))
        fresh = {f.name: f.read_text(encoding="utf-8") for f in (Path(td) / "cards").glob("*.md")}
        errs += cards_problems(fresh)
    for m in errs:
        print("ERROR:", m)
    if not errs:
        print(f"ok: {len(inst)} institutions, {len(props)} properties, JSON and {len(fresh)} cards match src/")
    return 1 if errs else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild JSON and cards into a temp dir, diff against the committed files")
    ap.add_argument("--write", action="store_true", help="write institutions.json and properties.json (default)")
    ap.add_argument("--cards", action="store_true", help="write docs/cards/*.md (with --check they are always compared)")
    a = ap.parse_args(argv)
    if a.check:
        return check()
    resolved, inst, props = build_all()
    order, raws = _order_and_raws(resolved)
    errs, _ = problems(resolved, False)
    if errs:
        print("\n".join("ERROR: " + m for m in errs))
        return 1
    if a.write or not a.cards:
        write(HERE, inst, props)
        print(f"wrote institutions.json ({len(inst)}) and properties.json ({len(props)})")
    if a.cards:
        files = render_cards(order, raws, resolved, props)
        write_cards(CARDS, files)
        print(f"wrote {len(files)} files to docs/cards/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

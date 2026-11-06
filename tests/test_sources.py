"""Sourcing checks (plans/sourcing.md, "CI checks").

Hard:
1. Every `source_id` in rule provenance (data/institutions/src/*.yaml) and in backtest ground truth
   (data/backtests/*-ground-truth.yaml) exists in the bibliography (every data/sources/*.yaml); bibliography ids are
   unique; required fields are present; `type` and `verification` are in the vocabularies; a null `source_id` only
   on an `unverified` item.
2. `opened` requires a non-empty `excerpt`. On a rule, every fragment of an `opened` excerpt (fragments joined by
   " ... ") appears verbatim, whitespace-normalised, in the rule's own `source` string (the migration's invariant:
   the excerpt is what the row records reading). Ground-truth items have no source string and are not checked here
   (their excerpt is checked by whoever opens the work).
3. A ground-truth event with `status: settled` has a `date_used` backed by one `opened` item from a primary text
   (statute, regulation, case, archival) of the event's jurisdiction reporting that date, or by two `opened` items
   from independent secondary works agreeing on it (independent: both have authors and their normalised surname
   sets are disjoint; a work with no author is never independent). A `conflict` event records its
   `conflict_note`; an event whose items report different dates is `conflict` (no silent conflict).
Report-only (warnings.warn until the migration is reviewed, then promoted):
1e. Two bibliography entries with the same url, or the same (type, year, normalised title): probably one work
   under two ids.
4. Every rule has `provenance`.
Hard since 2026-11-06 (promoted after the verification pass, plans/sourcing.md):
5. A `supported` claim in docs/claims.md whose `sources` cell names a rule row (`<entry>:R6`, `<entry>:R2,R5`,
   `<entry>:*`, globs such as `mwpa-*:*`) whose weakest provenance item is below `opened` (skipped when the claims
   table has no `sources` column; a cell starting `engine-only` is a claim about the engine and is not read).
"""
from __future__ import annotations

import fnmatch
import json
import re
import sys
import unicodedata
import warnings
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "sources"
INST = ROOT / "data" / "institutions"
BACKTESTS = ROOT / "data" / "backtests"
CLAIMS = ROOT / "docs" / "claims.md"

sys.path.insert(0, str(INST))
import build  # noqa: E402

TYPES = {"statute", "regulation", "case", "treatise", "archival", "secondary", "web", "dataset"}
PRIMARY = {"statute", "regulation", "case", "archival"}
LEVELS = ("opened", "snippet", "recalled", "unverified")  # strongest first
STATUSES = {"settled", "conflict", "unresolved"}
BIB_REQUIRED = ("id", "type", "title")
ITEM_REQUIRED = ("source_id", "verification")
EVENT_REQUIRED = ("id", "jurisdiction", "event", "date_used", "status", "provenance")
ID_RE = re.compile(r"^[a-z0-9]+(?:[a-z0-9.-]*[a-z0-9])?$")


# ---------------------------------------------------------------- loading
def _bib_entries():
    out = []
    for p in sorted(SOURCES.glob("*.yaml")):
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or []
        assert isinstance(data, list), f"{p.name}: a bibliography file is a list of works"
        out += [(p.name, e) for e in data]
    return out


@pytest.fixture(scope="module")
def bib():
    return {e["id"]: e for _, e in _bib_entries() if isinstance(e, dict) and "id" in e}


@pytest.fixture(scope="module")
def raws():
    return build.load_sources()


def _own_rules(order, raws):
    """(entry id, rule) for every rule written in a src file; inherited rules are counted once, where written."""
    for eid in order:
        for key in ("rules", "rules_add", "rules_replace"):
            for r in raws[eid].get(key, ()) or ():
                yield eid, r


def _ground_truth():
    return [(p.name, yaml.safe_load(p.read_text(encoding="utf-8")) or {})
            for p in sorted(BACKTESTS.glob("*-ground-truth.yaml"))] if BACKTESTS.is_dir() else []


def _all_items(order, raws):
    """(where, item) for every provenance item in rules and ground truth."""
    for eid, r in _own_rules(order, raws):
        for it in r.get("provenance") or ():
            yield f"{eid} {r['id']}", it
    for name, gt in _ground_truth():
        for ev in gt.get("events") or ():
            for it in ev.get("provenance") or ():
                yield f"{name} {ev.get('id')}", it


# ---------------------------------------------------------------- check 1
def test_bibliography_ids_unique_and_fields():
    entries = _bib_entries()
    assert entries, "data/sources/ has no works"
    errs, seen = [], {}
    for name, e in entries:
        if not isinstance(e, dict):
            errs.append(f"{name}: entry is not a mapping: {e!r}")
            continue
        for k in BIB_REQUIRED:
            if k not in e:
                errs.append(f"{name} {e.get('id')}: missing field {k}")
        i = e.get("id")
        if i is not None and not ID_RE.match(str(i)):
            errs.append(f"{name} {i}: id is not kebab-case")
        if i in seen:
            errs.append(f"{name} {i}: duplicate id (also in {seen[i]})")
        seen[i] = name
        if e.get("type") not in TYPES:
            errs.append(f"{name} {i}: type {e.get('type')!r} not in {sorted(TYPES)}")
    assert not errs, "\n".join(errs)


def _norm_title(t) -> str:
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def duplicate_works(entries):
    """Pairs of bibliography entries that look like one work under two ids: same url, or same (type, year, title)."""
    out, by_url, by_key = [], {}, {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        url = str(e.get("url") or "").strip().rstrip("/").lower()
        if url:
            if url in by_url:
                out.append((by_url[url], e.get("id"), f"same url {url}"))
            by_url.setdefault(url, e.get("id"))
        key = (e.get("type"), str(e.get("year")), _norm_title(e.get("title")))
        if key[2]:
            if key in by_key:
                out.append((by_key[key], e.get("id"), f"same type, year and title {key}"))
            by_key.setdefault(key, e.get("id"))
    return out


def test_report_duplicate_works():
    dups = duplicate_works([e for _, e in _bib_entries()])
    if dups:
        warnings.warn("bibliography entries that may be one work under two ids (check 1e, report-only): "
                      + "; ".join(f"{a} / {b}: {why}" for a, b, why in dups))


def test_duplicate_works_logic():
    a = {"id": "a", "type": "statute", "year": 1848, "title": "An Act for the protection", "url": "https://x/1"}
    assert duplicate_works([a, {**a, "id": "b", "url": "https://x/1/"}])  # same url (trailing slash)
    assert duplicate_works([a, {**a, "id": "b", "url": None, "title": "An act, for the PROTECTION"}])  # same title
    assert not duplicate_works([a, {**a, "id": "b", "url": None, "year": 1849}])
    assert not duplicate_works([a, {**a, "id": "b", "url": None, "type": "secondary"}])


def test_provenance_items_resolve(bib, raws):
    order, rs = raws
    errs = []
    for where, it in _all_items(order, rs):
        if not isinstance(it, dict):
            errs.append(f"{where}: provenance item is not a mapping")
            continue
        for k in ITEM_REQUIRED:
            if k not in it:
                errs.append(f"{where}: provenance item missing {k}")
        v = it.get("verification")
        if v not in LEVELS:
            errs.append(f"{where}: verification {v!r} not in {LEVELS}")
        sid = it.get("source_id")
        if sid is None:
            if v != "unverified":
                errs.append(f"{where}: source_id null on a {v} item (null only when unverified)")
        elif sid not in bib:
            errs.append(f"{where}: source_id {sid!r} not in data/sources/")
    assert not errs, "\n".join(errs)


def test_ground_truth_schema(bib):
    errs = []
    for name, gt in _ground_truth():
        if not gt.get("backtest"):
            errs.append(f"{name}: no `backtest`")
        evs = gt.get("events")
        if not isinstance(evs, list):
            errs.append(f"{name}: `events` is not a list")
            continue
        ids = [ev.get("id") for ev in evs]
        if len(ids) != len(set(ids)):
            errs.append(f"{name}: duplicate event ids")
        for ev in evs:
            where = f"{name} {ev.get('id')}"
            for k in EVENT_REQUIRED:
                if k not in ev:
                    errs.append(f"{where}: missing {k}")
            if ev.get("status") not in STATUSES:
                errs.append(f"{where}: status {ev.get('status')!r} not in {sorted(STATUSES)}")
            for it in ev.get("provenance") or ():
                if isinstance(it, dict) and "date_reported" not in it:
                    errs.append(f"{where}: provenance item {it.get('source_id')} has no date_reported")
    assert not errs, "\n".join(errs)


# ---------------------------------------------------------------- check 2
def test_opened_has_excerpt(raws):
    order, rs = raws
    bad = [where for where, it in _all_items(order, rs)
           if isinstance(it, dict) and it.get("verification") == "opened" and not str(it.get("excerpt") or "").strip()]
    assert not bad, "opened items without an excerpt:\n" + "\n".join(bad)


def _ws(x) -> str:
    return " ".join(str(x or "").split())


def excerpt_problem(item, source):
    """None if an opened item's excerpt fragments all appear (whitespace-normalised) in the rule's source string."""
    if not isinstance(item, dict) or item.get("verification") != "opened":
        return None
    src = _ws(source)
    missing = [f for f in (_ws(x) for x in str(item.get("excerpt") or "").split(" ... ")) if f and f not in src]
    return f"excerpt fragment(s) not in the source string: {missing}" if missing else None


def test_opened_excerpt_in_source(raws):
    order, rs = raws
    errs = []
    for eid, r in _own_rules(order, rs):
        for it in r.get("provenance") or ():
            p = excerpt_problem(it, r.get("source"))
            if p:
                errs.append(f"{eid} {r['id']} {it.get('source_id')}: {p}")
    assert not errs, "\n".join(errs)


def test_excerpt_rule_logic():
    src = "Read 2026-11-04: 'There may be ownership of\n  all domestic animals'; s. 663: 'Every kind of property'"
    op = {"source_id": "s", "verification": "opened"}
    assert excerpt_problem({**op, "excerpt": "There may be ownership of all domestic animals"}, src) is None
    assert excerpt_problem({**op, "excerpt": "ownership of all ... Every kind of property"}, src) is None
    assert excerpt_problem({**op, "excerpt": "ownership of all cattle"}, src)
    assert excerpt_problem({**op, "excerpt": "ownership ... a passage the row never quotes"}, src)
    assert excerpt_problem({**op, "excerpt": "anything", "verification": "recalled"}, src) is None


# ---------------------------------------------------------------- check 3
def _same_date(reported, used) -> bool:
    if reported is None or used is None:
        return False
    r, u = str(reported).strip(), str(used).strip()
    return r == u or r.startswith(u + "-")


def surnames(author) -> frozenset:
    """Normalised surnames of a bibliography `author` field: a string is one author ("Geddes, Rick" -> geddes); a list
    holds author entries, each a string (its part before a comma) or a list (its first element). The repo's flat
    [Surname, Given, ...] lists put given names in the set too, which only makes the independence check stricter."""
    if not author:
        return frozenset()
    entries = [author] if isinstance(author, str) else list(author)
    out = set()
    for a in entries:
        first = (a[0] if a else "") if isinstance(a, (list, tuple)) else str(a).split(",")[0]
        n = _norm_title(first)
        if n and n not in ("et al", "anon", "anonymous"):
            out.add(n)
    return frozenset(out)


def independent(w1, w2) -> bool:
    """Two secondary works are independent iff both name authors and no surname is shared."""
    a, b = surnames(w1.get("author")), surnames(w2.get("author"))
    return w1.get("id") != w2.get("id") and bool(a) and bool(b) and not (a & b)


def settled_problem(ev, bib):
    """None if a settled event's date is backed as plans/sourcing.md check 3 requires, else the reason."""
    du = ev.get("date_used")
    if du is None:
        return "settled with date_used null"
    agree = [it for it in ev.get("provenance") or ()
             if it.get("verification") == "opened" and it.get("source_id") in bib
             and _same_date(it.get("date_reported"), du)]
    ej = ev.get("jurisdiction")
    if ej and any(bib[it["source_id"]].get("type") in PRIMARY
                  and (it.get("jurisdiction") or bib[it["source_id"]].get("jurisdiction")) == ej for it in agree):
        return None
    sec = [bib[it["source_id"]] for it in agree if bib[it["source_id"]].get("type") not in PRIMARY]
    if any(independent(a, b) for i, a in enumerate(sec) for b in sec[i + 1:]):
        return None
    return (f"settled on {du} without one opened primary item of {ej} reporting it or two opened independent "
            f"secondary works agreeing ({len(agree)} opened item(s) report it)")


def date_conflict_problem(ev):
    """None unless the event's items report different dates while it is not `conflict` with a conflict_note."""
    ds = sorted({str(it.get("date_reported")).strip() for it in ev.get("provenance") or ()
                 if isinstance(it, dict) and it.get("date_reported") is not None})
    differ = any(not (_same_date(a, b) or _same_date(b, a)) for i, a in enumerate(ds) for b in ds[i + 1:])
    if not differ:
        return None
    if ev.get("status") != "conflict":
        return f"items report different dates {ds} but status is {ev.get('status')!r} (a silent conflict)"
    if not str(ev.get("conflict_note") or "").strip():
        return f"items report different dates {ds}; conflict without a conflict_note"
    return None


def test_settled_dates_are_backed(bib):
    errs = []
    for name, gt in _ground_truth():
        for ev in gt.get("events") or ():
            where = f"{name} {ev.get('id')}"
            if ev.get("status") == "settled":
                p = settled_problem(ev, bib)
                if p:
                    errs.append(f"{where}: {p}")
            if ev.get("status") == "conflict" and not str(ev.get("conflict_note") or "").strip():
                errs.append(f"{where}: conflict without a conflict_note")
            p = date_conflict_problem(ev)
            if p:
                errs.append(f"{where}: {p}")
    assert not errs, "\n".join(errs)


def test_settled_rule_logic():
    """The check-3 rule itself, on synthetic events (so it is exercised while no ground-truth file exists)."""
    bib = {"s": {"id": "s", "type": "statute", "jurisdiction": "US-ME"}, "a": {"id": "a", "type": "secondary", "author": ["A"]},
           "b": {"id": "b", "type": "secondary", "author": ["B"]}, "c": {"id": "c", "type": "secondary", "author": ["A"]}}
    op = lambda sid, d: {"source_id": sid, "verification": "opened", "excerpt": "x", "date_reported": d}
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [op("s", "1855")]}, bib) is None
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [op("a", 1855), op("b", "1855")]}, bib) is None
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [op("a", 1855), op("c", 1855)]}, bib)  # same author
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [op("a", 1855)]}, bib)
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [op("s", 1844)]}, bib)
    assert settled_problem({"jurisdiction": "US-ME", "date_used": 1855, "provenance": [{**op("s", 1855), "verification": "snippet"}]}, bib)
    assert settled_problem({"jurisdiction": "US-ME", "date_used": None, "provenance": [op("s", 1855)]}, bib)


def test_settled_independence_logic():
    """Check 3 independence: authorless works, string authors, and surname matching (review 2026-11-05, 7c)."""
    op = lambda sid, d=1855: {"source_id": sid, "verification": "opened", "excerpt": "x", "date_reported": d}
    sec = lambda i, author: {"id": i, "type": "secondary", "author": author}
    ev = lambda *ids: {"date_used": 1855, "jurisdiction": "US-ME", "provenance": [op(i) for i in ids]}
    bib = {"w1": sec("w1", None), "w2": sec("w2", None), "g1": sec("g1", "Geddes"), "g2": sec("g2", ["Geddes", "Rick"]),
           "g3": sec("g3", ["Geddes, Rick"]), "g4": sec("g4", [["Geddes", "Rick"], ["Lueck", "Dean"]]),
           "k": sec("k", ["Khan, B. Zorina"]), "c": sec("c", "Chused"), "e": sec("e", ["Éllis"]), "e2": sec("e2", "ellis")}
    assert settled_problem(ev("w1", "w2"), bib)  # two authorless works are not independent
    assert settled_problem(ev("w1", "k"), bib)  # one authorless work is not independent
    for a, b in (("g1", "g2"), ("g2", "g3"), ("g1", "g3"), ("g3", "g4"), ("e", "e2")):
        assert settled_problem(ev(a, b), bib), (a, b)  # same surname, however written
    assert settled_problem(ev("c", "k"), bib) is None  # a string author is one surname, not its letters
    assert settled_problem(ev("g4", "k"), bib) is None
    assert surnames("Chused") == {"chused"} and surnames([["Geddes", "Rick"], "Lueck, Dean"]) == {"geddes", "lueck"}


def test_settled_jurisdiction_logic():
    """Check 3: a primary item settles only an event of its own jurisdiction (review 2026-11-05, 7d)."""
    bib = {"uk": {"id": "uk", "type": "statute", "jurisdiction": "UK"},
           "me": {"id": "me", "type": "statute", "jurisdiction": "US-ME"}}
    op = lambda sid, **kw: {"source_id": sid, "verification": "opened", "excerpt": "x", "date_reported": 1855, **kw}
    ev = lambda *items: {"date_used": 1855, "jurisdiction": "US-ME", "provenance": list(items)}
    assert settled_problem(ev(op("uk")), bib)
    assert settled_problem(ev(op("me")), bib) is None
    assert settled_problem(ev(op("uk", jurisdiction="US-ME")), bib) is None  # the item names the jurisdiction read
    assert settled_problem(ev(op("me", jurisdiction="UK")), bib)


def test_date_conflict_logic():
    """No silent conflict: items reporting different dates need status conflict and a note (review 2026-11-05, 7b)."""
    it = lambda d: {"source_id": "s", "verification": "recalled", "date_reported": d}
    assert date_conflict_problem({"status": "unresolved", "provenance": [it(1855), it("1855"), it(None)]}) is None
    assert date_conflict_problem({"status": "unresolved", "provenance": [it(1855), it("1855-03-01")]}) is None
    assert date_conflict_problem({"status": "unresolved", "provenance": [it(1855), it(1844)]})
    assert date_conflict_problem({"status": "settled", "provenance": [it(1855), it(1844)]})
    assert date_conflict_problem({"status": "conflict", "provenance": [it(1855), it(1844)]})  # no conflict_note
    assert date_conflict_problem({"status": "conflict", "conflict_note": "GLT 1855; Khan 1844",
                                  "provenance": [it(1855), it(1844)]}) is None


# ---------------------------------------------------------------- engine JSON untouched
def test_provenance_not_in_engine_json():
    inst = json.loads((INST / "institutions.json").read_text(encoding="utf-8"))
    assert not [r for e in inst for r in e["rules"] if "provenance" in r]


# ---------------------------------------------------------------- check 4 (report-only) and check 5 (hard)
def test_report_rules_without_provenance(raws):
    order, rs = raws
    missing = [f"{eid} {r['id']}" for eid, r in _own_rules(order, rs) if not r.get("provenance")]
    if missing:
        warnings.warn(f"{len(missing)} rules have no provenance (check 4, report-only): " + ", ".join(missing))


def _claims_tables():
    """Rows of every table in docs/claims.md as dicts keyed by the lower-cased header."""
    if not CLAIMS.exists():
        return []
    lines = CLAIMS.read_text(encoding="utf-8").splitlines()
    rows, header = [], None
    for i, ln in enumerate(lines):
        if not ln.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if header is None:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if re.match(r"^\|[\s:|-]+\|?$", nxt):
                header = [c.lower() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return rows


REF = re.compile(r"([a-z0-9*][a-z0-9*-]*):(\*|R\d+(?:,\s?R\d+)*)")


def claim_refs(cell, resolved):
    """[(entry id, rule id)] named by a claims `sources` cell: `entry:R6`, `entry:R2,R5`, `entry:*`, `mwpa-*:*`;
    plus the patterns that matched no entry or rule."""
    refs, unknown = [], []
    for pat, rids in REF.findall(cell):
        eids = [e for e in resolved if fnmatch.fnmatchcase(e, pat)]
        if not eids:
            unknown.append(f"{pat}:{rids}")
        for eid in eids:
            have = [r["id"] for r in resolved[eid]["rules"]]
            want = have if rids == "*" else [x.strip() for x in rids.split(",")]
            for rid in want:
                (refs if rid in have else unknown).append((eid, rid) if rid in have else f"{eid}:{rid}")
    return refs, unknown


def test_report_supported_claims_on_weak_rows(raws):
    """Check 5. Cells starting `engine-only` are claims about the engine; the rows they mention are context, skipped."""
    rows = [r for r in _claims_tables() if "sources" in r]
    if not rows:
        return
    order, rs = raws
    resolved = {e["id"]: e for e in (build.resolve(i, rs) for i in order)}
    weak, unknown = [], []
    for row in rows:
        cell = row["sources"]
        refs, unk = claim_refs(cell, resolved)
        unknown += [f"{row.get('#', '?')}: {u}" for u in unk]
        status = re.match(r"[a-z]*", row.get("status", "").lower()).group(0)
        if status != "supported" or cell.lower().startswith("engine-only"):
            continue
        for eid, rid in refs:
            rule = next(r for r in resolved[eid]["rules"] if r["id"] == rid)
            lv = [it.get("verification") for it in rule.get("provenance") or () if it.get("verification") in LEVELS]
            level = max(lv, key=LEVELS.index) if lv else "none"
            if level != "opened":
                weak.append(f"{row.get('#', '?')}: {eid}:{rid} is {level}")
    if weak:
        raise AssertionError("supported claims resting on rule rows below opened (check 5): " + "; ".join(weak)
                             + " -- open the rows or downgrade the claim, and log the downgrade in docs/claims.md")
    if unknown:
        warnings.warn("docs/claims.md sources cells name unknown entries or rules: " + "; ".join(unknown))

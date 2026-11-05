"""Sourcing checks (plans/sourcing.md, "CI checks").

Hard:
1. Every `source_id` in rule provenance (data/institutions/src/*.yaml) and in backtest ground truth
   (data/backtests/*-ground-truth.yaml) exists in the bibliography (every data/sources/*.yaml); bibliography ids are
   unique; required fields are present; `type` and `verification` are in the vocabularies; a null `source_id` only
   on an `unverified` item.
2. `opened` requires a non-empty `excerpt`.
3. A ground-truth event with `status: settled` has a `date_used` backed by one `opened` item from a primary text
   (statute, regulation, case, archival) reporting that date, or by two `opened` items from independent secondary
   works agreeing on it. A `conflict` event records its `conflict_note`.
Report-only (warnings.warn until the migration is reviewed, then promoted):
4. Every rule has `provenance`.
5. A `supported` claim in docs/claims.md whose `sources` cell names a rule row (`<entry>:R6`, `<entry>:R2,R5`,
   `<entry>:*`, globs such as `mwpa-*:*`) whose weakest provenance item is below `opened` (skipped when the claims
   table has no `sources` column; a cell starting `engine-only` is a claim about the engine and is not read).
"""
from __future__ import annotations

import fnmatch
import json
import re
import sys
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


# ---------------------------------------------------------------- check 3
def _same_date(reported, used) -> bool:
    if reported is None or used is None:
        return False
    r, u = str(reported).strip(), str(used).strip()
    return r == u or r.startswith(u + "-")


def settled_problem(ev, bib):
    """None if a settled event's date is backed as plans/sourcing.md check 3 requires, else the reason."""
    du = ev.get("date_used")
    if du is None:
        return "settled with date_used null"
    agree = [it for it in ev.get("provenance") or ()
             if it.get("verification") == "opened" and it.get("source_id") in bib
             and _same_date(it.get("date_reported"), du)]
    if any(bib[it["source_id"]].get("type") in PRIMARY for it in agree):
        return None
    sec = [bib[it["source_id"]] for it in agree if bib[it["source_id"]].get("type") not in PRIMARY]
    works = {w["id"] for w in sec}
    authors = [frozenset(map(str, w.get("author") or ())) for w in sec]
    independent = len(works) >= 2 and any(not (a & b) for i, a in enumerate(authors) for b in authors[i + 1:])
    if independent:
        return None
    return (f"settled on {du} without one opened primary item reporting it or two opened independent secondary "
            f"works agreeing ({len(agree)} opened item(s) report it)")


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
    assert not errs, "\n".join(errs)


def test_settled_rule_logic():
    """The check-3 rule itself, on synthetic events (so it is exercised while no ground-truth file exists)."""
    bib = {"s": {"id": "s", "type": "statute"}, "a": {"id": "a", "type": "secondary", "author": ["A"]},
           "b": {"id": "b", "type": "secondary", "author": ["B"]}, "c": {"id": "c", "type": "secondary", "author": ["A"]}}
    op = lambda sid, d: {"source_id": sid, "verification": "opened", "excerpt": "x", "date_reported": d}
    assert settled_problem({"date_used": 1855, "provenance": [op("s", "1855")]}, bib) is None
    assert settled_problem({"date_used": 1855, "provenance": [op("a", 1855), op("b", "1855")]}, bib) is None
    assert settled_problem({"date_used": 1855, "provenance": [op("a", 1855), op("c", 1855)]}, bib)  # same author
    assert settled_problem({"date_used": 1855, "provenance": [op("a", 1855)]}, bib)
    assert settled_problem({"date_used": 1855, "provenance": [op("s", 1844)]}, bib)
    assert settled_problem({"date_used": 1855, "provenance": [{**op("s", 1855), "verification": "snippet"}]}, bib)
    assert settled_problem({"date_used": None, "provenance": [op("s", 1855)]}, bib)


# ---------------------------------------------------------------- engine JSON untouched
def test_provenance_not_in_engine_json():
    inst = json.loads((INST / "institutions.json").read_text(encoding="utf-8"))
    assert not [r for e in inst for r in e["rules"] if "provenance" in r]


# ---------------------------------------------------------------- report-only: checks 4 and 5
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
        warnings.warn("supported claims resting on rule rows below opened (check 5, report-only): " + "; ".join(weak))
    if unknown:
        warnings.warn("docs/claims.md sources cells name unknown entries or rules: " + "; ".join(unknown))

"""Makes docs/claims.md load-bearing: supported claims must cite something that exists and passes.

Evidence rules (docs/claims.md "Evidence" column):
- `supported`: cell names a test function defined in tests/ or ../philosophy-engine/tests (`def <name>`),
  OR a gate criterion written `gate (x)` (also `(c), (f)`) that the current `phil rules gate --json` reports PASS,
  OR a review file in docs/reviews/ (filename/stem, or "second review"/"third review"/"skeptical review"
  matching a file named *-<word>-review.md).
- `refuted` / `weakened`: cell must name such a review file.
- Every `last checked` is a valid date; older than 90 days only warns. No two rows share identical claim text.
A bare test file name (test_x.py) is not a test function and does not count.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import warnings
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CLAIMS = ROOT / "docs" / "claims.md"
REVIEWS = ROOT / "docs" / "reviews"
TEST_DIRS = [ROOT / "tests", ROOT.parent / "philosophy-engine" / "tests"]
STALE_DAYS = 90


def _rows():
    rows = []
    for line in CLAIMS.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] in ("#",) or set(cells[0]) <= {"-", " "}:
            continue
        rows.append(dict(zip(("id", "claim", "where", "evidence", "status", "checked"), cells)))
    return rows


def _status(row):
    m = re.match(r"[a-z]+", row["status"].lower())
    return m.group(0) if m else ""


@pytest.fixture(scope="module")
def rows():
    r = _rows()
    assert r, "no claim rows parsed from docs/claims.md"
    return r


@pytest.fixture(scope="module")
def test_defs():
    names = set()
    for d in TEST_DIRS:
        for p in d.rglob("*.py"):
            names.update(re.findall(r"^\s*(?:async\s+)?def\s+(test_\w+)", p.read_text(), re.M))
    return names


@pytest.fixture(scope="module")
def passing_gate():
    proc = subprocess.run([str(Path(sys.executable).parent / "phil"), "rules", "gate", "--json"], cwd=ROOT, capture_output=True, text=True, timeout=170)
    start = proc.stdout.find("{")
    assert start >= 0, f"`phil rules gate --json` produced no JSON: {proc.stderr[-300:]}"
    data = json.loads(proc.stdout[start:])
    return {c["key"] for c in data["criteria"] if c["status"] == "PASS"}


def _cited_tests(ev, defs):
    return {t for t in re.findall(r"(?<![\w/.])(test_\w+)\b(?!\.py)", ev) if t in defs}


def _cited_gates(ev):
    out = set()
    for m in re.finditer(r"gate\s+((?:\([a-z]\)\s*(?:,|/|and)?\s*)+)", ev, re.I):
        out.update(re.findall(r"\(([a-z])\)", m.group(1)))
    return out


def _cited_reviews(ev):
    found = set()
    files = sorted(REVIEWS.glob("*.md")) if REVIEWS.is_dir() else []
    low = ev.lower()
    for f in files:
        if f.name.lower() in low or f.stem.lower() in low:
            found.add(f.name)
        m = re.search(r"-([a-z]+)-review$", f.stem)
        if m and re.search(rf"\b{m.group(1)} review\b", low):
            found.add(f.name)
    return found


def test_supported_rows_cite_passing_evidence(rows, test_defs, passing_gate):
    bad = []
    for r in rows:
        if _status(r) != "supported":
            continue
        ev = r["evidence"]
        if _cited_tests(ev, test_defs) or (_cited_gates(ev) & passing_gate) or _cited_reviews(ev):
            continue
        bad.append(f"{r['id']}: supported but evidence cites no existing test function, passing gate criterion "
                   f"(passing now: {sorted(passing_gate)}) or review file: {ev[:90]!r}")
    assert not bad, "\n" + "\n".join(bad)


def test_refuted_or_weakened_rows_cite_review_file(rows):
    bad = [f"{r['id']}: {_status(r)} but evidence names no existing file in docs/reviews/: {r['evidence'][:90]!r}"
           for r in rows if _status(r) in ("refuted", "weakened") and not _cited_reviews(r["evidence"])]
    assert not bad, "\n" + "\n".join(bad)


def test_last_checked_is_valid_and_fresh(rows):
    invalid = []
    for r in rows:
        try:
            d = date.fromisoformat(r["checked"])
        except ValueError:
            invalid.append(f"{r['id']}: last checked {r['checked']!r} is not a valid YYYY-MM-DD date")
            continue
        if (date.today() - d).days > STALE_DAYS:
            warnings.warn(f"claim {r['id']}: last checked {d} is more than {STALE_DAYS} days old")
    assert not invalid, "\n" + "\n".join(invalid)


def test_no_duplicate_claim_text(rows):
    seen, dups = {}, []
    for r in rows:
        if r["claim"] in seen:
            dups.append(f"{r['id']} duplicates the claim text of {seen[r['claim']]}")
        seen.setdefault(r["claim"], r["id"])
    assert not dups, "\n" + "\n".join(dups)

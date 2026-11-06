"""Draft a `provenance:` list on every rule in src/*.yaml from its free-text `source` (plans/sourcing.md).

Re-runnable: an existing `provenance:` block is replaced, `source` is left unchanged, and nothing else in the file
moves (the block is inserted as text right after the rule's `source:` line, dumped with build.dump_yaml, so the
diff of a src file is only the inserted lines). Only rules written in a file are touched: `rules`, and in an
`extends` entry `rules_add` / `rules_replace`; inherited rules are not duplicated.

Classification is conservative and never upgrades (levels, strongest first: opened > snippet > recalled > unverified):
- each work the string names (WORKS, matched by regex) gets one item, classified from the text between its mention
  and the next work's mention (its window); several mentions of one work are merged;
- `UNVERIFIED` -> unverified; `[R]`, "from memory", "recalled", "general knowledge" -> recalled; a search snippet
  or abstract -> snippet; `opened` only when the window says the work was read (a date or a URL) and quotes a
  passage after that, which becomes `excerpt`; a read claim with no quote, or an earlier batch's `[F]` (fetched)
  tag relayed second-hand, -> recalled with a note; a window with no marker takes the first marker after it, or
  recalled ("cited with no record of reading") when the string has none;
- "UNVERIFIED ... as a rule" and "Statute texts not opened" add an item with source_id null (the rule itself, or
  the unnamed statutes, rest on no identified work);
- a string naming no work (an implicit norm, a general-knowledge rule) gets one item: source_id null, unverified,
  note quoting the rationale.
OVERRIDES holds the rows set by hand after reviewing the heuristic's output, each with its reason (listed in
provenance-migration-report.md). A hand setting replaces the row's items (or, with `append`, adds items to the
heuristic's). Most hand settings lower a level, add a lower item, or tidy a pin / excerpt / note. Some set an item
ABOVE the heuristic's level for that work (or add a work the heuristic did not detect, above `unverified`): the
heuristic misses a read claim that comes after the quotes, or applies a row-wide UNVERIFIED that belongs to a
different clause. Every such raise is listed in RAISES with the clause of the row's own string that licenses it;
the script computes the raises on every run and refuses to write if one is not listed there (or a listed one no
longer occurs), so the list cannot drift. `--summary` prints them.

`jurisdiction` is filled for statutes / regulations / treatises whose citation names the jurisdiction (it is part of
the cited title); `effective_date` only where the string states the date the act took effect (EFFECTIVE; a
short-title year or a session-law year is not an effective date). Both null otherwise.

Usage (from the comp-lib root):  uv run python data/institutions/migrate_provenance.py [--dry-run] [--summary]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

SRC = HERE / "src"
SOURCES = HERE.parent / "sources"
LEVELS = ("opened", "snippet", "recalled", "unverified")
RULE_LISTS = ("rules", "rules_add", "rules_replace")

# (source_id, regex naming the work in a source string). Order matters only for overlapping matches (first wins).
WORKS = [
    ("blackstone-1766-bk2-ch29", r"Book II ch\. 29"),
    ("blackstone-1765-bk1-ch15", r"Blackstone, Commentaries on the Laws of England, Book I ch\. 15|Blackstone's bar on grants"),
    ("shanley-1989", r"Shanley, Feminism"),
    ("stone-1990", r"Stone, Road to Divorce"),
    ("cal-wic-5150", r"(?:Welf\. & Inst\. Code s\. |WIC )5150(?:\(a\))?"),
    ("cal-wic-5152", r"Welf\. & Inst\. Code s\. 5152"),
    ("cal-wic-5275", r"WIC 5275"),
    ("cal-wic-306", r"Welf\. & Inst\. Code s\. 306"),
    ("cal-wic-361", r"Welf\. & Inst\. Code s\. 361"),
    ("cal-wic-328", r"WIC 328"),
    ("cal-wic-317", r"WIC 317"),
    ("cal-wic-16501", r"WIC 16501"),
    ("cal-wic-388", r"WIC 388"),
    ("cal-pen-11165-14", r"Penal Code 11165\.14"),
    ("cal-pen-597s", r"Penal Code s\. 597s"),
    ("cal-pen-597", r"Penal Code 597\(b\)"),
    ("cal-civ-655", r"Civ\. Code s\. 655"),
    ("cal-civ-663", r"s\. 663:"),
    ("cal-civ-658", r"s\. 658 defines"),
    ("cal-civ-1941", r"Civ\. Code s\. 1941"),
    ("cal-civ-1946", r"Civ\. Code s\. 1946"),
    ("cal-ccp-1161", r"Civ\. Proc\. s\. 1161"),
    ("canada-ei-maternity-parental", r"Employment Insurance maternity and parental benefits"),
    ("qc-cqlr-a-29-011", r"Act respecting parental insurance, CQLR c\. A-29\.011"),
    ("ak-stat-25-24-160", r"Alaska Stat\. s\. 25\.24\.160"),
    ("ri-gen-laws-4-13-41", r"R\.I\. Gen\. Laws s\. 4-13-41"),
    ("cfr-14-121-571", r"14 CFR 121\.571"),
    ("cfr-14-121-391", r"14 CFR 121\.391"),
    ("cfr-14-91-11", r"14 CFR 91\.11(?! / 121\.580 dropped)"),
    ("cfr-14-121-580", r"(?<=91\.11 / )121\.580(?! dropped)"),
    ("uk-mwpa-1882", r"Married Women's Property Act 1882"),
    ("ny-mwpa-1848", r"New York Married Women's Property Act 1848"),
    ("geddes-lueck-tennyson-2007", r"Geddes, Lueck & Tennyson 2007"),
    ("khan-1996", r"Khan 1996"),
    ("chused-1984", r"Chused 1984"),
    ("chused-1983", r"Chused 1983"),
    ("centola-becker-brackbill-baronchelli-2018", r"Centola, Becker"),
    ("mackie-1996", r"Mackie, 'Ending Footbinding|Mackie 1996"),
    ("brown-bossen-gates-satterthwaite-phillips-2012", r"Marriage Mobility and Footbinding"),
    ("wikipedia-tian-zu-hui", r"Wikipedia 'Tian Zu Hui'"),
    ("wikipedia-heavenly-foot-society", r"(?<=, )'Heavenly Foot Society'"),
    ("wikipedia-foot-emancipation-society", r"'Foot Emancipation Society'"),
    ("wikipedia-kibbutz-communal-child-rearing", r"Wikipedia, 'Kibbutz communal child rearing|WIKI_KIB"),
    ("tiger-shepher-1975", r"Tiger & Shepher"),
    ("kirkus-tiger-shepher-women-in-the-kibbutz", r"kirkusreviews\.com"),
    ("spiro-1956", r"Spiro, Kibbutz"),
    ("gavron-2000", r"Gavron, The Kibbutz"),
    ("firestone-1970", r"Firestone, The Dialectic of Sex"),
    ("kunc-2020-denver-star", r"KUNC 2020-11-17"),
    ("uk-matrimonial-causes-act-1857", r"Matrimonial Causes Act 1857 \(20 & 21 Vict"),
    ("longendyke-1863", r"Longendyke v\. Longendyke, 44 Barb"),
    ("berkeley-public-library-2018-patron-suspension-policy", r"Berkeley Public Library, Patron Suspension Policy"),
]

# Fixed pins by work (a pin read from the window, PIN_RE, takes precedence).
PIN = {
    "blackstone-1765-bk1-ch15": "Bk I ch 15", "blackstone-1766-bk2-ch29": "Bk II ch 29",
    "geddes-lueck-tennyson-2007": "Table 1", "khan-1996": "Table 1", "chused-1983": "at 1400",
    "mackie-1996": "abstract", "brown-bossen-gates-satterthwaite-phillips-2012": "abstract",
    "firestone-1970": "ch. 1; ch. 10", "qc-cqlr-a-29-011": "ss. 9, 10, 16, 17", "uk-mwpa-1882": "s. 1(2)",
    "cfr-14-121-571": "s. 121.571(a)", "ak-stat-25-24-160": "(a)(5)",
}
PIN_RE = r"\((s\. \d+)[:)]|s\. (\d[\w.]*(?:\([a-z0-9]+\))+(?:-\([a-z0-9]+\))?)|\(\(([a-z0-9]\)(?:\([a-z0-9]+\))?)|\b(\d{3,5}(?:\([a-z0-9]+\))+)"

# The jurisdiction the cited text governs, filled only where the citation names it (statute codes, "Laws of England").
JURIS = {
    "blackstone-1765-bk1-ch15": "England", "blackstone-1766-bk2-ch29": "England", "uk-mwpa-1882": "UK",
    "ny-mwpa-1848": "US-NY", "qc-cqlr-a-29-011": "CA-QC", "ak-stat-25-24-160": "US-AK", "ri-gen-laws-4-13-41": "US-RI",
}
# effective dates the strings state for the act a row encodes
# (the alaska string says "eff. 2017-01-17"; the NY 1848 and UK 1882 years are short-title years, not effective dates)
EFFECTIVE = {"ak-stat-25-24-160": "2017-01-17"}

QUOTE = re.compile(r"(?:(?<=^)|(?<=[\s(:;,]))'((?:[^']|'(?=[a-z]))+?)'(?=[\s.,;:)\]]|$)")
READ = re.compile(r"\bread (?:(\d{4}-\d{2}-\d{2})\b)?(?: ?at (https?://[^\s;:)]+))?")
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
M_UNVER = re.compile(r"UNVERIFIED")
M_RECALL = re.compile(r"\[R\]|from memory|\brecalled\b|general knowledge")
M_SNIP = re.compile(r"snippet|abstract|search result", re.I)
M_NOTOPEN = re.compile(r"NOT OPENED|not opened|NOT read|no text opened|no statute opened|no source opened")
M_F = re.compile(r"\[F\b")
AS_RULE = re.compile(r"UNVERIFIED(?: \([^)]*\))? as a rule|UNVERIFIED as a rule")
NO_STATUTE = re.compile(r"Statute texts not opened \(\[R\]\)")
NOISE = re.compile(r"\[ADR [^\]]*\]|\[coordination:[^\]]*\]|\[F for these sentences; body \[R\]\]")


def item(source_id=None, verification="unverified", pin=None, jurisdiction=None, effective_date=None, excerpt=None,
         accessed=None, url=None, note=""):
    """One provenance item, keys in the contract's order (plans/sourcing.md)."""
    return {"source_id": source_id, "pin": pin, "jurisdiction": jurisdiction, "effective_date": effective_date,
            "verification": verification, "excerpt": excerpt, "accessed": accessed, "url": url, "note": note}


def clean(src: str) -> str:
    return " ".join(NOISE.sub(" ", " ".join(str(src).split())).split())


def mentions(text):
    """[(start, end, source_id)] for every work mention, earliest first, overlaps dropped."""
    found = []
    for sid, rx in WORKS:
        for m in re.finditer(rx, text):
            found.append((m.start(), m.end(), sid))
    found.sort()
    out = []
    for f in found:
        if out and f[0] < out[-1][1]:
            continue
        out.append(f)
    return out


def windows(text, ms):
    """{source_id: [window text, ...]}; a window runs from a mention to the next mention of a different work."""
    out = {}
    for i, (s, _, sid) in enumerate(ms):
        j = i + 1
        while j < len(ms) and ms[j][2] == sid:
            j += 1
        end = ms[j][0] if j < len(ms) else len(text)
        if i and ms[i - 1][2] == sid:
            continue
        out.setdefault(sid, []).append(text[s:end])
    return out


def _quotes_after(w, pos):
    return list(dict.fromkeys(q for q in QUOTE.findall(w[pos:]) if len(q) >= 12))


def classify(w, rest):
    """(level, excerpt, accessed, url, note) for one work from its window w; rest is the text after the window."""
    w_ = NO_STATUTE.sub(" ", AS_RULE.sub(" ", w))
    if M_UNVER.search(w_):
        return "unverified", None, None, None, "old source string says UNVERIFIED"
    if M_RECALL.search(w_):
        return "recalled", None, None, None, "old source string: cited from memory / general knowledge / [R]"
    if M_SNIP.search(w_):
        m = M_SNIP.search(w_)
        qs = _quotes_after(w_, m.start())
        d = DATE.search(w_[m.start():])
        return "snippet", " ... ".join(qs[:1]) or None, d.group(1) if d else None, None, \
            "old source string: only a search snippet / abstract was read"
    if M_NOTOPEN.search(w_):
        return "recalled", None, None, None, "old source string: not opened"
    r = READ.search(w_)
    if r and (r.group(1) or r.group(2)):
        qs = _quotes_after(w_, r.end())
        if qs:
            return "opened", " ... ".join(qs), r.group(1), r.group(2), ""
        return "recalled", None, None, None, "earlier batch reports reading; no excerpt recorded; re-open to upgrade"
    if M_F.search(w_):
        qs = QUOTE.findall(w_)
        q = ("; quote recorded: '" + "' ... '".join(qs) + "'") if qs else "; no excerpt recorded"
        return "recalled", None, None, None, ("[F, via plans/backtest-mwpa.md]: an earlier batch reports fetching it; "
                                              "relayed second-hand, no access date" + q + "; re-open to upgrade")
    # no marker in the window: the first marker after it decides, else "cited, no record of reading"
    rest_ = AS_RULE.sub(" ", rest)
    found = [lvl for rx, lvl in ((M_UNVER, "unverified"), (M_RECALL, "recalled"), (M_NOTOPEN, "recalled"))
             if rx.search(rest_)]
    if found:
        lvl = max(found, key=LEVELS.index)
        return lvl, None, None, None, f"no marker next to the citation; the lowest marker later in the string reads {lvl}"
    qs = QUOTE.findall(w_)
    q = ("; quote in the old string (no read date): '" + "' ... '".join(qs) + "'") if qs else ""
    return "recalled", None, None, None, "cited with no record of reading in this row's source" + q + "; re-open to upgrade"


def pin_of(sid, w):
    m = re.search(PIN_RE, w)
    if sid in ("qc-cqlr-a-29-011",):
        p = re.search(r"\((s\. \d+)[:)]", w)
        return p.group(1) if p else PIN[sid]
    if sid in PIN:
        return PIN[sid]
    if m and sid.startswith(("cal-", "ri-", "ak-")):
        g = next(x for x in m.groups() if x)
        return g if g.startswith("s.") else ("s. " + g if g[0].isdigit() else "(" + g)
    t = re.search(r"s\. ([\d.]+)$", (_bib().get(sid) or {}).get("title") or "")
    return "s. " + t.group(1) if t else None


def rationale(text):
    t = re.split(r"\s*UNVERIFIED\b", text)[0].strip(" .;")
    return t[:300] + ("..." if len(t) > 300 else "")


def heuristic(rule):
    text = clean(rule["source"])
    ms = mentions(text)
    items = []
    if not ms:
        items.append(item(note="no work named; rationale: " + rationale(text)))
        return items
    wins = windows(text, ms)
    for sid, ws in wins.items():
        w = " ".join(ws)
        last_end = text.rfind(ws[-1]) + len(ws[-1])
        lvl, ex, acc, url, note = classify(w, text[last_end:])
        if url and url == (_bib().get(sid) or {}).get("url"):
            url = None
        items.append(item(sid, lvl, pin_of(sid, w), JURIS.get(sid) or _bib_juris(sid), EFFECTIVE.get(sid),
                          ex, acc, url, note))
    if AS_RULE.search(text):
        items.append(item(note="the rule itself: " + AS_RULE.search(text).group(0) + " (no text states it)"))
    if NO_STATUTE.search(text):
        items.append(item(note="the statutes the row encodes are named only through the secondary work; "
                               "statute texts not opened ([R]); no bibliography entry"))
    return items


_BIB = {}


def _bib():
    if not _BIB:
        for p in sorted(SOURCES.glob("*.yaml")):
            for e in build.load_yaml(p) or []:
                _BIB[e["id"]] = e
    return _BIB


def _bib_juris(sid):
    """A statute's or regulation's own jurisdiction (its citation names it), from the bibliography."""
    e = _bib().get(sid, {})
    return e.get("jurisdiction") if e.get("type") in ("statute", "regulation", "case") else None


# ---------------------------------------------------------------- hand settings after review
WAMS = "https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/"
TIAN = ("wikipedia-tian-zu-hui", "wikipedia-heavenly-foot-society", "wikipedia-foot-emancipation-society")
WIKI_SNIP = "seen as search snippets only (2026-11-04), pages not opened, tagged [R]"


def _wiki_pledge():
    return [item(s, "recalled", note=WIKI_SNIP) for s in TIAN]


BK1_15 = "https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp"

OVERRIDES = {}  # (entry id, rule id) -> (items, reason, append); filled below


def override(eid, rid, reason, *items, append=False):
    """Set a row by hand. append=True keeps the heuristic's items and adds these after them."""
    OVERRIDES[(eid, rid)] = (list(items), reason, append)


# Every hand item set above the heuristic's level for its work (or a work the heuristic did not detect, set above
# unverified), with the clause of the row's own string that licenses it. main() checks this list against the
# computed raises on every run (review 2026-11-05, finding 3).
RAISES = {
    ("police-crisis", "R7", "cal-wic-5150"):
        "'s. 5150(a) (https://california.public.law/...section_5150, cited here until 2026-11-04) "
        "gives the officer custody and delivery (R3), no release duty'; the heuristic's regex misses the bare "
        "'s. 5150(a)'; cited with a URL and no read record = recalled",
    ("companion-ownership", "R1", "cal-civ-655"):
        "'Read 2026-11-04 at https://codes.findlaw.com/ca/civil-code/civ-sect-655/ ...' follows "
        "the quote 'There may be ownership of ... of all domestic animals'; the heuristic only looks for a quote after "
        "the read claim",
    ("companion-ownership", "R1", "cal-civ-663"):
        "'... and https://codes.findlaw.com/ca/civil-code/civ-sect-663/' in the same read claim, "
        "after the quote 'Every kind of property that is not real is personal'",
    ("companion-guardian-renamed", "R1", "cal-civ-655"): "as companion-ownership R1 (same string)",
    ("companion-guardian-renamed", "R1", "cal-civ-663"): "as companion-ownership R1 (same string)",
    ("kibbutz-childrens-house", "R2", "wikipedia-kibbutz-communal-child-rearing"):
        "'Verification pass: read 2026-11-06 at https://en.wikipedia.org/...oldid=1360699722 ...: 'The nanny position "
        "was always a woman's role. ...'' (until 2026-11-06: the row quoted it with no read record); the "
        "row's UNVERIFIED belongs to the clause 'the assignment finding itself NOT read directly' (Tiger & Shepher)",
    ("kibbutz-childrens-house", "R2", "kirkus-tiger-shepher-women-in-the-kibbutz"):
        "'book and sample (34,040 members) confirmed via Kirkus review https://www.kirkusreviews.com/...'"
        " (a confirmation claim, no quote); the UNVERIFIED that follows belongs to Tiger & Shepher's finding",
    ("airline-flight", "R2", "cfr-14-121-571"):
        "'read 2026-11-04 at https://www.law.cornell.edu/cfr/text/14/121.571 ...: (a) 'shall "
        "insure that all passengers are orally briefed by the appropriate crewmember''; the row's UNVERIFIED belongs to "
        "'the general in-flight care duty' (its own null item)",
    ("footbinding", "R10", "wikipedia-tian-zu-hui"):
        "'(Wikipedia 'Tian Zu Hui', ... read 2026-11-04 as search snippets only, pages not "
        "opened: [R]'; the row's closing UNVERIFIED belongs to the reconstructed rule (its own null item)",
    ("footbinding", "R10", "wikipedia-heavenly-foot-society"): "as wikipedia-tian-zu-hui on this row",
    ("mwpa-suit", "R16", "us-ma-acts-1855-ch304"):
        "'Massachusetts St. 1855 c. 304, read 2026-11-06 at ...: s. 4 ... s. 7 ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("mwpa-suit", "R16", "us-ny-laws-1860-ch90"):
        "'New York Laws 1860 ch. 90, read 2026-11-06 at ...: s. 7 ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("mwpa-suit", "R16", "us-ny-laws-1862-ch172"):
        "'New York Laws 1862 ch. 172, read 2026-11-06 at ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("mwpa-suit", "R19", "us-ma-acts-1855-ch304"):
        "'Massachusetts St. 1855 c. 304 read 2026-11-06 at ...: it contains no proviso ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("mwpa-suit", "R19", "us-ma-acts-1874-ch184"):
        "'Massachusetts St. 1874 c. 184, read 2026-11-06 at ...: s. 3 ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("mwpa-suit", "R19", "us-ny-laws-1860-ch90"):
        "'New York Laws 1860 ch. 90 s. 7 bars nothing in terms' and 'Suit clauses read for this row (2026-11-06): ... New York 1860 s. 7 ...'; the row opens with 'UNVERIFIED (leads, not opened 2026-11-05 ...)', which the heuristic applies to the whole window; the appended 'Verification pass: ... read 2026-11-06 at <url> ...: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("cps", "R1", "cal-pen-11165-14"):
        "'Penal Code 11165.14 read 2026-11-06 at ...: 'The appropriate local law enforcement agency ...''; the row's 'UNVERIFIED (general knowledge; no source opened)' precedes and the heuristic applies it to the window; the appended 'Verification pass: ... read 2026-11-06 at <url>: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("cps", "R8", "cal-wic-317"):
        "'WIC 317 read 2026-11-06 at ...: (c)(1) ... (d) ...'; the row's 'UNVERIFIED (general knowledge; no source opened)' precedes and the heuristic applies it to the window; the appended 'Verification pass: ... read 2026-11-06 at <url>: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("cps", "R11", "cal-wic-317"):
        "'WIC 317 read 2026-11-06 at ...: (e)(1) ...'; the row's 'UNVERIFIED (general knowledge; no source opened)' precedes and the heuristic applies it to the window; the appended 'Verification pass: ... read 2026-11-06 at <url>: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("police-crisis", "R8", "cal-wic-5275"):
        "'WIC 5275 read 2026-11-06 at ...: 'Every person detained under this part ...''; the row's 'UNVERIFIED (general knowledge; no source opened)' precedes and the heuristic applies it to the window; the appended 'Verification pass: ... read 2026-11-06 at <url>: <quote>' licenses the raise (verification pass 2026-11-06)",
    ("companion-guardianship", "R9", "ak-stat-25-24-160"):
        "'Verification pass: read 2026-11-06 at https://www.animallaw.info/...: '(5) if an animal is owned, ...''; the "
        "row's 'UNVERIFIED (general knowledge; no source opened)' belongs to the generalisation (its own null item) "
        "(verification pass 2026-11-06)",
    ("public-library", "R2", "berkeley-public-library-2018-patron-suspension-policy"):
        "'Verification pass: read 2026-11-06 at https://www.berkeleypubliclibrary.org/...: 'In order to provide and "
        "maintain ...''; the row's 'UNVERIFIED as a rule' belongs to the duty to serve (its own null item) "
        "(verification pass 2026-11-06)",
    ("naming-convention", "R1", "centola-becker-brackbill-baronchelli-2018"):
        "'Verification pass: Centola, Becker, Brackbill & Baronchelli read 2026-11-06 at https://openaccess.city.ac.uk/...: "
        "'participants are shown an image ...''; the row's earlier 'NOT OPENED (2026-11-04 ...)' is superseded "
        "(verification pass 2026-11-06)",
    ("naming-convention", "R2", "centola-becker-brackbill-baronchelli-2018"):
        "'Verification pass: Centola, Becker, Brackbill & Baronchelli read 2026-11-06 at https://openaccess.city.ac.uk/...: "
        "'participants are shown an image ...''; the row's earlier 'NOT OPENED (2026-11-04 ...)' is superseded "
        "(verification pass 2026-11-06)",
    ("coverture-household", "R6", "uk-matrimonial-causes-act-1857"):
        "'enacted text read 2026-11-06 through the OCR of https://www.legislation.gov.uk/...: s. 2, ... s. 27, ...'; "
        "the heuristic's read regex is lower-case and the work is named before 'read' (verification pass 2026-11-06)",
    ("coverture-household-us", "R6", "stevenson-wolfers-2006"):
        "'Stevenson & Wolfers read 2026-11-06 at https://www.nber.org/...: 'from the preexisting divorce laws ...''; "
        "the heuristic applies the row's opening 'UNVERIFIED (leads, not opened 2026-11-05 ...)' to the whole "
        "window (verification pass 2026-11-06)",
    ("coverture-household-us", "R6", "us-ny-laws-1787-divorce"):
        "'New York, Laws of 1787 ch. 69 (passed 30 March 1787), read 2026-11-06 through the OCR at "
        "https://archive.org/...: 'in all cases of adultery ...''; no WORKS regex names this act (verification pass "
        "2026-11-06)",
    ("footbinding", "R10", "mackie-1996"):
        "'Mackie 1996 names the same two-part pledge for the FGC analogue, abstract [F]' "
        "(an [F] tag relayed second-hand, no quote, no read date = recalled); the closing UNVERIFIED belongs to the "
        "reconstructed rule. Was snippet with a borrowed accessed date until the 2026-11-05 review (finding 1)",
}


override("coverture-household", "R1",
         "the string also names Bk I ch 15 as the citation it replaced ('did not support this rule'); only Bk II ch 29 supports the row",
         item("blackstone-1766-bk2-ch29", "opened", "Bk II ch 29", "England", None,
              "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage",
              "2026-11-04", None, "long s modernised from the OCR"))
override("coverture-household", "R5",
         "the earlier WAMS pointer is the same work (Bk I ch 15), not a second one; one opened item, excerpt both quoted passages",
         item("blackstone-1765-bk1-ch15", "opened", "Bk I ch 15", "England", None,
              "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour",
              "2026-11-04", None, "long s modernised from the OCR; earlier pointer " + WAMS))
_SHANLEY_STONE = ("not opened 2026-11-04 (archive.org 403, Google Books API 429) nor 2026-11-06 (archive.org lending copy "
                  "401, search-inside 'item not available', Google Books API 429, no-preview ids); ")
override("coverture-household", "R6",
         "verification pass 2026-11-06: Blackstone Bk I ch 15 (the row's earlier note wrongly said it has no exit bar) and "
         "the 1857 Act opened; Shanley and Stone still unverified",
         item("blackstone-1765-bk1-ch15", "opened", "Bk I ch 15, II (divorce)", "England", None,
              "it will not allow it to be unloosed for any cause whatsoever, that arises after the union is made ... with "
              "us in England adultery is only a cause of separation from bed and board ... divorces a vinculo "
              "matrimonii, for adultery, have of late years been frequently granted by act of parliament",
              "2026-11-06", BK1_15,
              "long s modernised from the OCR; states the law as of 1765, not up to 1857; two conditional exits the "
              "row does not encode: separation a mensa et thoro for 'intolerable ill temper, or adultery, in either of "
              "the parties' (no dissolution) and a private Act of Parliament for adultery"),
         item("uk-matrimonial-causes-act-1857", "opened", "ss. 2, 27", "England", "1857",
              "Suits for Restitution of Conjugal Rights, and in all Causes, Suits, and Matters Matrimonial, shall cease "
              "to be so exerciseable ... it shall be lawful for any Wife to present a Petition to the said Court, "
              "praying that her Marriage may be dissolved",
              "2026-11-06", None,
              "read through the OCR of the enacted PDF (margin notes dropped); s. 2 shows the pre-1857 remedies sat in "
              "the ecclesiastical courts; s. 27 gives the wife dissolution only for the husband's aggravated adultery, "
              "so even after 1857 she has no exit at her own will; effective_date is the act's year, the "
              "commencement section was not read"),
         item("shanley-1989", "unverified", note=_SHANLEY_STONE + "cited for restitution of conjugal rights and no "
              "unilateral exit before the Matrimonial Causes Act 1857"),
         item("stone-1990", "unverified", note=_SHANLEY_STONE + "same point as Shanley"))
# Verification pass 2026-11-06 (plans/sourcing-verify-session.md, order 2 and the cheapest upgrades): Bk I ch 15
# re-opened at Avalon; each row's `source` now records the read date and the passage quoted.
_BK1_15_EXCERPT = {
    "R2": ("The husband is bound to provide his wife with necessaries by law, as much as himself",
           "long s modernised from the OCR; earlier pointer " + WAMS),
    "R4": ("If the wife be injured in her person or her property, she can bring no action for redress without her "
           "husband's concurrence, and in his name, as well as her own ... neither can she be sued, without making the "
           "husband a defendant",
           "long s modernised from the OCR; the same passage excepts a husband who has abjured the realm or is "
           "banished (she then sues as a feme sole), an exception the row does not encode; earlier pointer " + WAMS),
    "R7": ("all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable ... all "
           "compacts made between husband and wife, when single, are voided by the intermarriage",
           "long s modernised; the OCR prints 'converture' in the first passage; 'void, or at least voidable' is "
           "weaker than the row's 'no such power exists' (voidable acts bind until avoided); the first passage is "
           "introduced as acts done 'by his compulsion', and the second concerns compacts between the spouses, not "
           "her capacity to contract with third parties (council 2026-11-06); earlier pointer " + WAMS),
}
for _r, (_ex, _note) in _BK1_15_EXCERPT.items():
    override("coverture-household", _r,
             "verification pass 2026-11-06: Bk I ch 15 re-opened at Avalon; the row now records the read and the quote",
             item("blackstone-1765-bk1-ch15", "opened", "Bk I ch 15", "England", None, _ex, "2026-11-06", BK1_15,
                  _note))
# coverture-household-us (2026-11-05, plans/sourcing.md "Coverture split and US suit", B3 with B1): the English rows'
# items with a note that US reception of Blackstone is assumed and unsourced; R6 cites US leads, never above unverified.
_US_RECEPTION = ("US entry: an English treatise cited for a US rule; US reception of Blackstone is assumed and "
                 "unsourced; a US treatise (Kent, Commentaries on American Law) is a lead, not opened")
for _r in ("R1", "R2", "R4", "R5", "R7"):
    _items, _why, _ = OVERRIDES[("coverture-household", _r)]
    override("coverture-household-us", _r, _why + "; US base: the same item, its note adds that US reception is assumed",
             *[dict(_it, note=(_it["note"] + "; " if _it["note"] else "") + _US_RECEPTION) for _it in _items])
override("coverture-household-us", "R6",
         "verification pass 2026-11-06: both leads opened; the paper does not support 'no unilateral divorce in any US "
         "state before 1969' (faithfulness finding), it supports the B1 reading (consent or fault required)",
         item("stevenson-wolfers-2006", "opened", "s. 2; Table 1", None, None,
              "from the preexisting divorce laws (which typically required either the consent of both spouses or a "
              "demonstration of marital fault) ... prior to unilateral divorce, a partner wishing to dissolve the "
              "marriage could leave ... However, in such a situation, a legal divorce is not granted",
              "2026-11-06", "https://www.nber.org/system/files/working_papers/w10175/w10175.pdf",
              "NBER working paper (December 2003), not the QJE 2006 text; Table 1 lists nine states with unilateral "
              "divorce statutes predating 1964, contradicting the row's 'before 1969' parenthesis; the paper covers "
              "the twentieth century and says nothing of the MWPA era; consent divorce is an exit the row does not "
              "encode; physical departure without divorce is possible, the row's 'leave' means dissolution"),
         item("us-ny-laws-1787-divorce", "opened", "ch. 69, s. 1", "US-NY", "1787-03-30",
              "in all cases of adultery that have already been committed, or may hereafter be committed, where the "
              "parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill "
              "to the Chancellor",
              "2026-11-06", None,
              "read through the OCR (long s modernised, clipped letters restored); 'party injured': either spouse may "
              "petition, adultery the only ground; dissolution on the other spouse's fault (B2), not at her own will; "
              "the date is the passage date printed (OCR 'Passed the zoth of March, 1787', i.e. 30th), commencement not "
              "stated"))
override("police-crisis", "R7",
         "s. 5150(a) is cited for the absence of an officer release duty (recalled), s. 5152 is the opened source; the excerpt keeps the release-only-if passage that (not (danger s)) stands for",
         item("cal-wic-5152", "opened", "s. 5152(a), (b)", "US-CA", None,
              "A person admitted to a facility for 72-hour treatment and evaluation ... shall receive an evaluation as soon as possible after the person is admitted ... The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes ... that the person no longer requires evaluation or treatment ... A person who has been detained for evaluation and treatment shall be released, referred for further care and treatment on a voluntary basis, or certified for intensive treatment",
              "2026-11-04", "https://california.public.law/codes/ca_welf_and_inst_code_section_5152",
              "leginfo.legislature.ca.gov returned 403"),
         item("cal-wic-5150", "recalled", "s. 5150(a)", "US-CA",
              note="cited for what it lacks (no release duty on the officer); no read record for this use"))
override("police-crisis", "R1",
         "implicit: the string names WIC 5150 only to say it does not require police dispatch; no work supports the row",
         item(note="no work named for this rule (WIC 5150 is cited as not requiring it); rationale: implicit: police are the default responder to a crisis call; nothing in WIC 5150 requires it, dispatch practice does"))
override("cps", "R7", "pin and excerpt tidied (the heuristic's excerpt joined the two quoted fragments of (c)(1))",
         item("cal-wic-361", "opened", "s. 361(c)(1)", "US-CA", None,
              "unless the juvenile court finds clear and convincing evidence of any of the following circumstances ... substantial danger to the physical health, safety, protection, or physical or emotional well-being of the minor",
              "2026-11-04", "https://california.public.law/codes/ca_welf_and_inst_code_section_361",
              "leginfo.legislature.ca.gov returned 403"))
# Verification pass 2026-11-06: the other match rows (plans/sourcing.md "Which rows the care+control match reads").
_P5150 = "https://california.public.law/codes/ca_welf_and_inst_code_section_5150"
_P306 = "https://california.public.law/codes/ca_welf_and_inst_code_section_306"
_PL = "the page gives the text as 'updated Jan. 1, 2024' and its source as leginfo.legislature.ca.gov"
override("police-crisis", "R2",
         "verification pass 2026-11-06: excerpt narrowed to the statute (the heuristic took the page's update date as a quote)",
         item("cal-wic-5150", "opened", "s. 5150(a)", "US-CA", None,
              "At a minimum, assessment, as defined in Section 5150.4, and evaluation, as defined in subdivision (a) of "
              "Section 5008, shall be conducted and provided on an ongoing basis", "2026-11-06", _P5150,
              _PL + "; the duty is in the passive voice and is not placed on the officer: the row's provides_care(o, s) "
              "on the responding officer is the encoder's reading (faithfulness finding, plans/sourcing.md)"))
override("police-crisis", "R3", "verification pass 2026-11-06: url and note",
         item("cal-wic-5150", "opened", "s. 5150(a)", "US-CA", None,
              "When a person, as a result of a mental health disorder, is a danger to others, or to themselves, or "
              "gravely disabled, a peace officer ... may, upon probable cause, take, or cause to be taken, the person "
              "into custody for a period of up to 72 hours", "2026-11-06", _P5150,
              _PL + "; the statute's trigger also includes 'gravely disabled' and requires probable cause; the row "
              "reads only danger"))
override("police-crisis", "R4", "verification pass 2026-11-06: url and note",
         item("cal-wic-5150", "opened", "s. 5150(a)", "US-CA", None,
              "take, or cause to be taken, the person into custody for a period of up to 72 hours ... The 72-hour "
              "period begins at the time when the person is first detained.", "2026-11-06", _P5150,
              _PL + "; the section states custody, not the subject's exit bar, which the row infers from custody; "
              "5150(c) lets the facility serve the person on a voluntary basis instead of detaining"))
override("cps", "R3", "verification pass 2026-11-06: url and note",
         item("cal-wic-306", "opened", "s. 306(a)(2)", "US-CA", None,
              "Take into and maintain temporary custody of, without a warrant, a child who ... the social worker has "
              "reasonable cause to believe that the child has an immediate need for medical care or is in immediate "
              "danger of physical or sexual abuse", "2026-11-06", _P306,
              "the page gives its source as leginfo.legislature.ca.gov (updated 2024-09-27); (a)(2) also requires the "
              "child to be a dependent or described in s. 300(b) or (g)"))
override("cps", "R4", "verification pass 2026-11-06: url",
         item("cal-wic-306", "opened", "s. 306(f)", "US-CA", None,
              "Before taking a child into custody, a social worker shall consider whether the child may remain safely "
              "in their residence.", "2026-11-06", _P306,
              "the page gives its source as leginfo.legislature.ca.gov (updated 2024-09-27)"))
override("cps", "R10", "verification pass 2026-11-06: url and note",
         item("cal-wic-306", "opened", "s. 306(a)(2)", "US-CA", None,
              "Take into and maintain temporary custody of, without a warrant", "2026-11-06", _P306,
              "the section says nothing of the child's own conduct; the exit bar is inferred from custody (the row "
              "says so)"))
_PLC = "https://california.public.law/codes/"
override("cps", "R1",
         "verification pass 2026-11-06: WIC 328 opened (supports a discretionary investigation duty); Penal Code "
         "11165.14 opened and does not support the row (wrong pin, faithfulness finding)",
         item("cal-wic-328", "opened", "s. 328(a)", "US-CA", None,
              "the social worker shall immediately make any investigation the social worker deems necessary to "
              "determine whether child welfare services should be offered to the family",
              "2026-11-06", _PLC + "ca_welf_and_inst_code_section_328",
              "trigger is 'cause to believe' a child is described in s. 300, not a received report; the scope is what "
              "the worker 'deems necessary'; the same worker refers to services, which fits the row's dual role"),
         item("cal-pen-11165-14", "opened", "s. 11165.14", "US-CA", None,
              "The appropriate local law enforcement agency shall investigate a child abuse complaint filed by a parent "
              "or guardian of a pupil with a school",
              "2026-11-06", _PLC + "ca_penal_code_section_11165.14",
              "opened and off point: a police duty for complaints against school staff at a schoolsite; it does not "
              "support a social worker's duty to investigate reports"))
override("cps", "R8",
         "verification pass 2026-11-06: WIC 317 opened; the court appoints counsel in the proceeding, with a "
         "'would not benefit' exception; the row's establishment by investigate is the encoder's (faithfulness finding)",
         item("cal-wic-317", "opened", "s. 317(c)(1), (d)", "US-CA", None,
              "If a child or nonminor dependent is not represented by counsel, the court shall appoint counsel for the "
              "child or nonminor dependent, unless the court finds that the child or nonminor dependent would not "
              "benefit from the appointment of counsel. ... Counsel shall represent the parent, guardian, child, or "
              "nonminor dependent at the detention hearing and at all subsequent proceedings before the juvenile court.",
              "2026-11-06", _PLC + "ca_welf_and_inst_code_section_317",
              "appointment is by the court once a petition is before it, not on investigation; the exception means "
              "counsel is not guaranteed"))
override("cps", "R11",
         "verification pass 2026-11-06: WIC 317(e) and 388(a)(1) opened; the child petitions through a properly "
         "appointed guardian (388), counsel represents its interests (317(e)) (faithfulness finding)",
         item("cal-wic-317", "opened", "s. 317(e)(1)", "US-CA", None,
              "Counsel shall be charged in general with the representation of the child's interests.",
              "2026-11-06", _PLC + "ca_welf_and_inst_code_section_317", "apostrophe straightened"),
         item("cal-wic-388", "opened", "s. 388(a)(1)", "US-CA", None,
              "the child or the nonminor dependent through a properly appointed guardian may, upon grounds of change "
              "of circumstance or new evidence, petition the court",
              "2026-11-06", _PLC + "ca_welf_and_inst_code_section_388",
              "the petition runs through a guardian, not 'in its own name through counsel' as the row reads"))
override("police-crisis", "R8", "verification pass 2026-11-06: WIC 5275 opened; effective_date of the current text set",
         item("cal-wic-5275", "opened", "s. 5275", "US-CA", "2024-01-01",
              "Every person detained under this part shall have a right to a hearing by writ of habeas corpus for their "
              "release",
              "2026-11-06", _PLC + "ca_welf_and_inst_code_section_5275",
              "effective_date is the page's 'updated Jan. 1, 2024' (the text as amended in 2023); 'this part' (the LPS "
              "Act) covers a 5150 hold; the request procedure is written for certification, and the separate "
              "certification review hearing (s. 5256) was not opened"))
for _e in ("companion-ownership", "companion-guardian-renamed"):
    _items = [item("cal-civ-655", "opened", "s. 655", "US-CA", None,
                   "There may be ownership of all inanimate things which are capable of appropriation or of manual delivery; of all domestic animals",
                   "2026-11-04", "https://codes.findlaw.com/ca/civil-code/civ-sect-655/",
                   "leginfo.legislature.ca.gov and law.justia.com returned 403"),
              item("cal-civ-663", "opened", "s. 663", "US-CA", None, "Every kind of property that is not real is personal",
                   "2026-11-04", "https://codes.findlaw.com/ca/civil-code/civ-sect-663/"),
              item("cal-civ-658", "recalled", "s. 658", "US-CA",
                   note="cited (defines real property) with no record of reading; re-open to upgrade")]
    if _e == "companion-guardian-renamed":
        _items.append(item("ri-gen-laws-4-13-41", "recalled", "s. 4-13-41", "US-RI", None,
                           note="cited for the role name only, not for this rule; no read record in this row (the entry source_text says read); 'P.L. 2001 ch. 72' is the session law, not an effective date"))
    override(_e, "R1", "Penal Code 597s is named only as the citation dropped from this row; s. 658 is cited without a read record",
             *_items)
override("companion-guardianship", "R9",
         "the row's UNVERIFIED is for the generalisation beyond divorce, but it also says 'no source opened'; kept unverified (lower) and the generalisation gets its own item",
         item("ak-stat-25-24-160", "unverified", "(a)(5)", "US-AK", "2017-01-17", None, None, None,
              "the row says UNVERIFIED (general knowledge; no source opened) though it quotes 'taking into consideration the well-being of the animal'; the entry source_text says read at animallaw.info; re-open to upgrade"),
         item(note="the generalisation from divorce to any custody claim: no jurisdiction does this (the entry's construction)"))
override("public-library", "R2",
         "the duty to serve is 'UNVERIFIED as a rule' (read from the policy's premise); the policy itself is cited with quotes but no read date",
         item("berkeley-public-library-2018-patron-suspension-policy", "recalled",
              note="quotes in the old string, no read date in the row (the entry source_text says read at the URL); re-open to upgrade"),
         item(note="the rule (a duty to serve) is read from the policy's premise, not stated: UNVERIFIED as a rule"))
override("naming-convention", "R1", "'cited from memory' and 'UNVERIFIED as a quotation' together: the lower level",
         item("centola-becker-brackbill-baronchelli-2018", "unverified",
              note="NOT OPENED 2026-11-04; cited from memory, UNVERIFIED as a quotation (plans/layer2-abm.md lists it as opened; not relied on)"))
override("naming-convention", "R2", "as R1",
         item("centola-becker-brackbill-baronchelli-2018", "unverified",
              note="NOT OPENED 2026-11-04; cited from memory, UNVERIFIED as a quotation (plans/layer2-abm.md lists it as opened; not relied on)"))
override("kibbutz-childrens-house", "R2",
         "three works at three levels: the WIKI_KIB quote is not read in this row (recalled), Kirkus confirms the book (claimed, no quote), Tiger & Shepher's finding not read",
         item("wikipedia-kibbutz-communal-child-rearing", "recalled",
              note="quotes 'was always a woman's role'; this row records no read (R1's row read the page 2026-11-03); re-open or copy the read record to upgrade"),
         item("tiger-shepher-1975", "unverified", "pp. 41, 167",
              note="the assignment finding itself NOT read directly: UNVERIFIED; cited by WIKI_KIB"),
         item("kirkus-tiger-shepher-women-in-the-kibbutz", "recalled",
              note="earlier batch reports confirming the book and sample (34,040 members) via this review; no excerpt recorded; re-open to upgrade"))
override("kibbutz-childrens-house", "R6", "two named works, each not opened (UNVERIFIED); the heuristic dropped neither but put the generic note on both; the implicit rule itself gets a null item (review 2026-11-05, finding 14)",
         item("spiro-1956", "unverified", note="not opened 2026-11-04 (archive.org 403, Google Books API 429); 1958 ed. also cited"),
         item("gavron-2000", "unverified", note="not opened 2026-11-04 (archive.org 403, Google Books API 429)"),
         item(note="the rule itself: 'implicit: the committee / general assembly disciplines a member who neglects the rota' ... UNVERIFIED (general knowledge; no source opened)"))
_WIKI_KIB_READ = ("the row records reading the page ('read 2026-11-03') and quotes 'The nanny position was always a "
                  "woman's role. Teacher positions were both for women and men.'; children 'lived in the children's "
                  "house, where they had communal sleeping arrangements' and 'visited their parents for 2-3 hours a day'")
override("kibbutz-childrens-house", "R1",
         "the page was read but no quoted passage states the rule (committee assignment of a member): recalled for the "
         "rule claim, quote kept in the note; the committee assignment is the encoder's parenthesis: null item "
         "(review 2026-11-05, finding 2)",
         item("wikipedia-kibbutz-communal-child-rearing", "recalled", accessed=None,
              note=_WIKI_KIB_READ + "; none of these passages mentions a committee or an assignment, so the page is "
                   "recalled for this rule (it was read, the rule is not in what was quoted); re-open and quote a "
                   "passage on staffing the children's house to upgrade"),
         item(note="the committee's power to assign a member to the children's house: stated only in the encoder's "
                   "parenthesis ('members are assigned to the children's house by the committee'); no quoted text "
                   "states it"))
override("kibbutz-childrens-house", "R3",
         "the page was read but the quoted passages support the metapelet's duty of care only indirectly (a nanny "
         "position existed): recalled, quote kept in the note (review 2026-11-05, finding 2)",
         item("wikipedia-kibbutz-communal-child-rearing", "recalled",
              note=_WIKI_KIB_READ + "; the quotes say a nanny position existed, not that the assigned metapelet must "
                   "care for the child ('the metapelet runs the children's house' is the encoder's parenthesis): "
                   "recalled for this rule; re-open and quote a passage on the metapelet's duties to upgrade"))
override("kibbutz-childrens-house", "R4",
         "opened, excerpt narrowed to the passage that states the rule (communal sleeping); the heuristic pasted the "
         "row-wide three-fragment excerpt (review 2026-11-05, finding 2)",
         item("wikipedia-kibbutz-communal-child-rearing", "opened", None, None, None,
              "lived in the children's house, where they had communal sleeping arrangements", "2026-11-03"))
override("kibbutz-childrens-house", "R5",
         "the page was read but the quote runs the other way (children visited their parents, not a male member the "
         "child): recalled, quote kept in the note; the father's visit is the encoder's reading: null item (review "
         "2026-11-05, finding 2)",
         item("wikipedia-kibbutz-communal-child-rearing", "recalled",
              note=_WIKI_KIB_READ + "; 'visited their parents for 2-3 hours a day' says the children visited the "
                   "parents, not that a male member may visit the child: recalled for this rule; re-open to upgrade"),
         item(note="a male member's visit to the child (the father's relation to the children's house is the visit, "
                   "not care): the encoder's reading in the parenthesis; the quoted passage states the reverse "
                   "direction"))
override("airline-flight", "R2",
         "the string says the general in-flight care duty is UNVERIFIED (no text opened states it); 121.571 opened (read date and quote); 121.391 quoted with a URL but no read date: recalled; it supports egress only",
         item("cfr-14-121-571", "opened", "s. 121.571(a), (a)(3)", "US", None,
              "shall insure that all passengers are orally briefed by the appropriate crewmember", "2026-11-04",
              "https://www.law.cornell.edu/cfr/text/14/121.571",
              "ecfr.gov redirected to a block page; supports a briefing duty, narrower than the rule's provides_care"),
         item("cfr-14-121-391", "recalled", "s. 121.391", "US", None, None, None,
              "https://www.law.cornell.edu/cfr/text/14/121.391",
              "the string says 'read at <url>' and quotes 'to provide the most effective egress of passengers' but gives "
              "no read date for this section (121.571's date is not borrowed): recalled, re-open to upgrade (review "
              "2026-11-05, finding 10); only sets the number of flight attendants"),
         item(note="the general in-flight care duty: UNVERIFIED (no text opened states it)"))
override("mwpa-creditor-exemption", "R11",
         "the heuristic's items kept; adds a null item for the Mississippi 1839 act, named through Khan as R14-R16 name "
         "theirs through GLT (review 2026-11-05, finding 6)",
         item(note="the Mississippi 1839 act the row names ('Mississippi 1839 shielded property from husbands' "
                   "creditors; Khan excludes it as debt relief') is named only through Khan 1996; statute text not "
                   "opened; no bibliography entry"),
         append=True)
override("mwpa-creditor-exemption", "R12",
         "Chused works as in R11; Blackstone's bar on grants is a reading of the inherited R7 source; the rule itself 'UNVERIFIED as a rule of the 1839-50 acts'",
         item("chused-1984", "recalled", note="[F, via plans/backtest-mwpa.md]: an earlier batch reports fetching it; relayed second-hand, no access date; quote recorded: 'generally contained nothing more than statements exempting married women's property from the debts of husbands' ... 'narrowly construing'; re-open to upgrade"),
         item("chused-1983", "unverified", "at 1400", note="[R], PDF refused: UNVERIFIED"),
         item("blackstone-1765-bk1-ch15", "recalled", None, "England",
              note="cited for the bar on grants between spouses, read as lifted; English treatise in a US chain; pin (Bk I ch 15) inferred, not in the string"),
         item(note="the conveyance to the wife as a rule of the 1839-50 acts: UNVERIFIED (general knowledge; no source opened)"))
override("mwpa-property", "R13",
         "GLT is named twice, once as the source of the statute's date; the statute text not opened ([R] UNVERIFIED)",
         item("ny-mwpa-1848", "unverified", None, "US-NY", None, note="the statute text itself not opened: [R] UNVERIFIED; year (1848) from GLT Table 1; effective date not in the string"),
         item("geddes-lueck-tennyson-2007", "recalled", "Table 1",
              note="[F, via plans/backtest-mwpa.md]: an earlier batch reports fetching it; relayed second-hand, no access date; no excerpt recorded; re-open to upgrade"))
_NY60 = "http://www.houseofrussell.com/american-legal-history/assignments/laws-of-new-york-83d-sessio.html"
_NY62 = "https://www.houseofrussell.com/american-legal-history/docs/laws-of-new-york-85th-sessi.pdf"
_MA55 = "https://archives.lib.state.ma.us/server/api/core/bitstreams/6cc4626f-6cc6-47f5-9a38-7a775ff276b4/content"
_MA74 = "https://archives.lib.state.ma.us/server/api/core/bitstreams/ce48bb31-9c82-4384-925f-39ba51ab54b4/content"
_RUSSELL = "a transcription on a law-course site (Russell, American Legal History), not a scan of the session laws"
override("mwpa-suit", "R16",
         "verification pass 2026-11-06: the three US acts opened; MA pin corrected from s. 3 to ss. 4, 7 (s. 3 is "
         "conveyance); GLT carries no quote here",
         item("us-ny-laws-1860-ch90", "opened", "s. 7", "US-NY", None,
              "Any married woman may, while married, sue and be sued in all matters having relation to her property ... "
              "any married woman may bring and maintain an action in her own name, for damages, against any person or "
              "body corporate, for any injury to her person or character, the same as if she were sole",
              "2026-11-06", _NY60,
              _RUSSELL + "; 'Passed March 20, 1860'; the property suit is scoped to her property, the tort suit runs "
              "against any person; the encoding takes the broader reading"),
         item("us-ny-laws-1862-ch172", "opened", "s. 3 (s. 7 as amended)", "US-NY", None,
              "sue and be sued in all matters having relation to her sole and separate property, or which may hereafter "
              "come to her by descent, devise, bequest, purchase, or the gift or grant of any person",
              "2026-11-06", _NY62, _RUSSELL + "; 'Passed April 10, 1862'; still scoped to her property"),
         item("us-ma-acts-1855-ch304", "opened", "ss. 4, 7", "US-MA", None,
              "may, while married, sue and be sued, in all matters having relation to her property, in the same manner "
              "as if she were sole ... she may sue and be sued as if sole in regard to her trade, business, labor, "
              "services and earnings",
              "2026-11-06", _MA55,
              "'Approved by the Governor, May 5, 1855'; the row's pin 's. 3' is wrong (s. 3 is conveyance and "
              "contract); s. 4 applies to a woman 'hereafter to be married'"),
         item("geddes-lueck-tennyson-2007", "recalled", "Table 1",
              note="[F, via plans/backtest-mwpa.md]: an earlier batch reports fetching it; relayed second-hand, no "
                   "access date; no excerpt recorded; the published GLT 2012 and Geddes & Tennyson 2013 were not "
                   "reachable 2026-11-06 (403 at Chicago Unbound, Emerald, SSRN)"))
override("mwpa-suit", "R19",
         "verification pass 2026-11-06: MA 1855 has no spousal-suit proviso (the quoted proviso is MA 1874 c. 184 "
         "s. 3); NY 1860 s. 7 bars nothing in terms, Longendyke construes it (faithfulness finding)",
         item("us-ma-acts-1855-ch304", "opened", "ss. 3, 4, 7", "US-MA", None,
              "may, while married, sue and be sued, in all matters having relation to her property, in the same manner "
              "as if she were sole",
              "2026-11-06", _MA55,
              "cited by the row for a proviso it does not contain: the act omits suits between spouses rather than "
              "barring them, so it supports R19 only as an omission (the row's 'bars or omits')"),
         item("us-ma-acts-1874-ch184", "opened", "s. 3", "US-MA", "1874",
              "nothing herein contained shall authorize suits between husband and wife",
              "2026-11-06", _MA74,
              "'Approved April 24, 1874'; the express proviso the row quotes, 19 years after the act the row cites; "
              "effective_date is the year only"),
         item("us-ny-laws-1860-ch90", "opened", "s. 7", "US-NY", None,
              "Any married woman may, while married, sue and be sued in all matters having relation to her property",
              "2026-11-06", _NY60,
              _RUSSELL + "; no bar on suits against the husband in terms ('except her husband' qualifies gifts)"),
         item("longendyke-1863", "opened", "44 Barb. 366", "US-NY", None,
              "It is conceded by counsel that by the rules of the common law husband and wife could not sue each other "
              "in a civil action ... The right to sue her husband in an action of assault and battery may perhaps be "
              "covered under the literal language of this section; but I think such was not the meaning and intent of "
              "the legislature",
              "2026-11-06", None, "Caselaw Access Project JSON; the bar on spousal suits in New York is judicial "
              "construction of the 1860/1862 acts, not statutory text"))
override("footbinding", "R1",
         "Mackie abstract quotes as a search-index snippet (snippet), the rule itself 'UNVERIFIED as a rule'",
         item("mackie-1996", "snippet", "abstract", None, None,
              "Female footbinding in China lasted for 1,000 years but ended in a single generation. I show that each practice is a self-enforcing convention, in Schelling's (1960) sense, maintained by interdependent expectations on the marriage market",
              "2026-11-04", None, "abstract read as a search-index snippet; the article itself not opened (jstor paywalled); body [R]"),
         item(note="the rule (a family 'may' bind) is reconstructed from the convention account; no primary text opened: UNVERIFIED as a rule"))
_MACKIE_SNIP = item("mackie-1996", "snippet", "abstract", None, None,
                    "maintained by interdependent expectations on the marriage market", "2026-11-04", None,
                    "abstract read as a search-index snippet; the article itself not opened (jstor paywalled); body [R]")
_MACKIE_PLEDGE = item("mackie-1996", "recalled", "abstract", None, None, None, None, None,
                      "the row says only 'Mackie 1996 names the same two-part pledge ..., abstract [F]': an [F] tag "
                      "relayed with no quote and no read date in this row -> recalled (review 2026-11-05, finding 1; "
                      "the abstract's pledge-association sentence is recorded in R1's source and the entry "
                      "source_text); the 'two-part pledge' and 'critical mass' readings are from the body, [R]")
override("footbinding", "R3", "Mackie abstract as a snippet; the norm is implicit (a convention, not a written rule)",
         _MACKIE_SNIP, item(note="implicit sanctioned norm: a convention, not a written rule; the abstract supports the convention, no text states the norm"))
override("footbinding", "R4", "Wikipedia pledge pages: 'search snippets only, pages not opened: [R]' -> recalled (the lower of snippet and [R]); Mackie 'abstract [F]' with no quote or date in the row -> recalled",
         *_wiki_pledge(), _MACKIE_PLEDGE)
override("footbinding", "R10", "as R4, plus the rule itself reconstructed (UNVERIFIED)",
         *_wiki_pledge(), _MACKIE_PLEDGE,
         item(note="implicit: no text says a suitor 'may' pledge; reconstructed from the convention account: UNVERIFIED"))
override("footbinding", "R5", "as R4, plus 'UNVERIFIED ... as a rule'",
         _MACKIE_SNIP, *_wiki_pledge(),
         item(note="implicit: the market's refusal of an unbound bride, reconstructed from the convention account: UNVERIFIED as a rule"))
override("footbinding", "R6", "as R5",
         _MACKIE_SNIP, *_wiki_pledge(),
         item(note="the groom-side convention, reconstructed from the convention account: UNVERIFIED as a rule"))
override("footbinding", "R7", "Mackie snippet; Brown et al. abstract-only snippet tagged [R] -> recalled",
         _MACKIE_SNIP,
         item("brown-bossen-gates-satterthwaite-phillips-2012", "recalled", "abstract",
              note="abstract only, as a search snippet (2026-11-04), tagged [R]; no quote recorded; qualifies mobility, not marriageability"))
for _r in ("R1", "R2", "R3"):
    override("ectogenesis", _r, "Firestone cited from memory and marked UNVERIFIED: the lower level",
             item("firestone-1970", "unverified", "ch. 1; ch. 10",
                  note="UNVERIFIED: no text opened; wording from memory (plans/ectogenesis.md section 2)"))
for _r in ("R4", "R5", "R6", "R7"):
    override("ectogenesis", _r, "Firestone is named only in the boilerplate ('no text opened for this rule'); no work supports the row"
             + ("; the Kleven finding the row names gets its own null item (review 2026-11-05, finding 6)" if _r == "R5" else ""),
             item(note="no work named for this rule; rationale: " + "{rationale}"),
             *([item(note="'the Kleven finding in docs/theory.md (adoptive mothers take the same hit, so role not body "
                          "carries it)': the reason for the female trigger; the row gives no citation and none is in "
                          "the bibliography (a search lead for it is in plans/sourcing-worklist-other.md: add an entry "
                          "and upgrade when opened)")] if _r == "R5" else []))


# ---------------------------------------------------------------- verification pass 2026-11-06, step 5 and the
# cheapest upgrades (plans/sourcing-verify-session.md). Each call below supersedes the hand setting of the same row
# above (override() replaces the row); the earlier reason is kept above for the history.
_WK = ("https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education"
       "&oldid=1360699722")
_WKN = "revision 1360699722 (2026-06-23), read as wikitext; "
_BP = ("https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/"
       "patron_suspension_policy_approved_14nov2018.pdf")
override("kibbutz-childrens-house", "R1",
         "verification pass 2026-11-06: page re-read; still no passage states a committee's power to assign: recalled",
         item("wikipedia-kibbutz-communal-child-rearing", "recalled", accessed=None, url=_WK,
              note=_WKN + "the nearest passage, 'Kibbutz members who were considered the most educated and esteemed "
                   "got the position of educators', names no committee or assignment procedure; Spiro or Gavron on the "
                   "work-assignment committee would be the source to open"),
         item(note="the committee's power to assign a member to the children's house: stated only in the encoder's "
                   "parenthesis; no read text states it"))
override("kibbutz-childrens-house", "R2",
         "verification pass 2026-11-06: the WIKI_KIB sentence re-read with a date in this row: opened for the practice; "
         "Tiger & Shepher's finding still not read",
         item("wikipedia-kibbutz-communal-child-rearing", "opened", None, None, None,
              "The nanny position was always a woman's role. Teacher positions were both for women and men.",
              "2026-11-06", _WK, _WKN + "supports the practice the row encodes, not a committee prohibition (the row "
              "says so); the page cites no source for the sentence"),
         item("tiger-shepher-1975", "unverified", "pp. 41, 167",
              note="the assignment finding itself NOT read directly: UNVERIFIED; cited by WIKI_KIB"),
         item("kirkus-tiger-shepher-women-in-the-kibbutz", "recalled",
              note="earlier batch reports confirming the book and sample (34,040 members) via this review; no excerpt "
                   "recorded; re-open to upgrade"))
override("kibbutz-childrens-house", "R3",
         "verification pass 2026-11-06: a passage stating the nanny's care was found and quoted: opened",
         item("wikipedia-kibbutz-communal-child-rearing", "opened", None, None, None,
              "A group of children, all about the same age, shared a children's house and had a nanny who took care "
              "of their everyday needs.", "2026-11-06", _WK,
              _WKN + "states the care, not that it is owed on pain of reprimand (R6's link is the encoder's)"))
override("kibbutz-childrens-house", "R5",
         "verification pass 2026-11-06: a passage on fathers' time with children found: opened, with the 'at any time' "
         "gap noted (faithfulness finding)",
         item("wikipedia-kibbutz-communal-child-rearing", "opened", None, None, None,
              "Fathers were supposed to bond with their children through quality time much more so than in a "
              "non-kibbutz environment ... visited their parents for 2-3 hours a day", "2026-11-06", _WK,
              _WKN + "en dash in '2-3' normalised; the page has the children visit the parents for 2-3 hours a day, "
              "the row lets a male member visit the child 'at any time'"),
         item(note="'at any time': the encoder's reading; the read text gives a daily visiting time at the parents' "
                   "house"))
override("public-library", "R2", "verification pass 2026-11-06: policy PDF opened; the duty to serve stays a reading",
         item("berkeley-public-library-2018-patron-suspension-policy", "opened", "p. 1", None, None,
              "In order to provide and maintain a welcoming and safe environment for all patrons and library staff",
              "2026-11-06", _BP, "a purpose clause, not a duty to serve"),
         item(note="the rule (a duty to serve) is read from the policy's premise, not stated: UNVERIFIED as a rule"))
override("public-library", "R3", "verification pass 2026-11-06: policy PDF opened",
         item("berkeley-public-library-2018-patron-suspension-policy", "opened", "p. 2, B.2", None, None,
              "Continued disruption (same or different day): Library privileges will be suspended for the day by an "
              "authorized staff-member and the patron will be asked to leave the Library building.",
              "2026-11-06", _BP, "suspension follows an initial warning (B.1); the row's single-step suspension of a "
              "disruptive patron skips the warning"))
override("public-library", "R5", "verification pass 2026-11-06: policy PDF opened; entry read from the suspension's effect",
         item("berkeley-public-library-2018-patron-suspension-policy", "opened", "p. 1", None, None,
              "Suspension of library privileges will result in removal from, and denial of access to, all Berkeley "
              "Public Library services and facilities for a designated period of time.",
              "2026-11-06", _BP, "states that suspension denies access; the unsuspended patron's permission to enter "
              "is the converse, not stated"))
override("companion-guardianship", "R9",
         "verification pass 2026-11-06: statute text read as reproduced on animallaw.info: opened; the generalisation "
         "keeps its own null item",
         item("ak-stat-25-24-160", "opened", "(a)(5)", "US-AK", "2017-01-17",
              "(5) if an animal is owned, for the ownership or joint ownership of the animal, taking into consideration "
              "the well-being of the animal.", "2026-11-06",
              "https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment",
              "the page reproduces the amended section and gives 'effective January 17, 2017'; akleg.gov not opened; "
              "the statute decides ownership in a divorce, it does not reassign custody outside one"),
         item(note="the generalisation from divorce to any custody claim: no jurisdiction does this (the entry's "
                   "construction)"))
override("airline-flight", "R2",
         "verification pass 2026-11-06: 121.391 opened (supports egress staffing only); 121.571 as before; the general "
         "care duty stays UNVERIFIED",
         item("cfr-14-121-571", "opened", "s. 121.571(a), (a)(3)", "US", None,
              "shall insure that all passengers are orally briefed by the appropriate crewmember", "2026-11-04",
              "https://www.law.cornell.edu/cfr/text/14/121.571",
              "ecfr.gov redirected to a block page; supports a briefing duty, narrower than the rule's provides_care"),
         item("cfr-14-121-391", "opened", "s. 121.391(d)", "US", None,
              "flight attendants required by this section shall be located as near as practicable to required floor "
              "level exits and shall be uniformly distributed throughout the airplane in order to provide the most "
              "effective egress of passengers in event of an emergency evacuation", "2026-11-06",
              "https://www.law.cornell.edu/cfr/text/14/121.391",
              "staffing and seating for evacuation; not an in-flight care duty"),
         item(note="the general in-flight care duty: UNVERIFIED (no text opened states it)"))
_P597S = "https://california.public.law/codes/ca_penal_code_section_597s"
for _e in ("companion-ownership", "companion-guardian-renamed"):
    for _r in ("R3", "R4"):
        override(_e, _r, "verification pass 2026-11-06: 597s opened; excerpt narrowed to the statute (the heuristic "
                 "took the page's update date as a quote)",
                 item("cal-pen-597s", "opened", "s. 597s(a)", "US-CA", None,
                      "Every person who willfully abandons any animal is guilty of a misdemeanor.", "2026-11-06",
                      _P597S, "the page gives the text as 'updated Jan. 1, 2000' and its source as "
                      "leginfo.legislature.ca.gov; (b) exempts releasing native wildlife"))
override("lease", "R2", "verification pass 2026-11-06: 1941 opened; url and note",
         item("cal-civ-1941", "opened", "s. 1941", "US-CA", None,
              "The lessor of a building intended for the occupation of human beings must, in the absence of an "
              "agreement to the contrary, put it into a condition fit for such occupation, and repair all subsequent "
              "dilapidations thereof, which render it untenantable", "2026-11-06",
              "https://california.public.law/codes/ca_civ_code_section_1941",
              "'in the absence of an agreement to the contrary' and the s. 1929 exception are not in the row"))
for _r in ("R1", "R2"):
    override("naming-convention", _r,
             "verification pass 2026-11-06: Centola et al. read in full (accepted manuscript): opened; the free choice "
             "of name is the experiment's design, not a stated rule",
             item("centola-becker-brackbill-baronchelli-2018", "opened", "Methods; results (accepted ms.)", None, None,
                  "participants are shown an image (a picture of a man or a woman) and prompted to enter a name in the "
                  "response field ... Continuous interactions led to occasional switching by subjects throughout the "
                  "study.", "2026-11-06", "https://openaccess.city.ac.uk/id/eprint/20031/1/CM_CRO_Version.pdf",
                  "accepted manuscript, not the Science typeset text (no Science page numbers); free text entry each "
                  "round implies either name may be used at any time; the committed minority are confederates who "
                  "push only the new name; the 25% threshold is stated as 'not expected to be a universal value'"))

def migrate_rule(eid, rule):
    key = (eid, rule["id"])
    if key in OVERRIDES:
        items, _, append = OVERRIDES[key]
        out = heuristic(rule) if append else []
        for it in items:
            it = dict(it)
            if "{rationale}" in (it["note"] or ""):
                it["note"] = it["note"].replace("{rationale}", rationale(clean(rule["source"])))
            out.append(it)
        return out, True
    return heuristic(rule), False


def raises(eid, rule, items):
    """[(source_id, heuristic level or None, hand level)] for items set above the heuristic's level for that work."""
    h = {it["source_id"]: it["verification"] for it in heuristic(rule) if it["source_id"]}
    out = []
    for it in items:
        sid, lv = it["source_id"], it["verification"]
        if sid is None:
            continue
        base = h.get(sid, "unverified")
        if LEVELS.index(lv) < LEVELS.index(base):
            out.append((sid, h.get(sid), lv))
    return out


# ---------------------------------------------------------------- text-level rewrite of src/*.yaml
TOP = re.compile(r"^([A-Za-z_]+):")


def rewrite(text: str, provs: dict) -> str:
    """Insert/replace `  provenance:` after each own rule's `  source:` line. provs: (list key, rule id) -> items."""
    lines = text.split("\n")
    out, key, rid, i = [], None, None, 0
    while i < len(lines):
        ln = lines[i]
        m = TOP.match(ln)
        if m:
            key, rid = m.group(1), None
        elif ln.startswith("- id: ") and key in RULE_LISTS:
            rid = ln[len("- id: "):].strip().strip("'\"")
        elif not ln.startswith(" ") and not ln.startswith("- "):
            rid = None
        if ln.startswith("  provenance:") and rid is not None and key in RULE_LISTS:
            i += 1
            while i < len(lines) and (lines[i].startswith("  - ") or lines[i].startswith("    ")):
                i += 1
            continue
        out.append(ln)
        if ln.startswith("  source:") and rid is not None and key in RULE_LISTS and (key, rid) in provs:
            block = build.dump_yaml({"provenance": provs[(key, rid)]}).rstrip("\n").split("\n")
            out += ["  " + b for b in block]
        i += 1
    return "\n".join(out)


def _strip_prov(obj):
    if isinstance(obj, dict):
        return {k: _strip_prov(v) for k, v in obj.items() if k != "provenance"}
    if isinstance(obj, list):
        return [_strip_prov(x) for x in obj]
    return obj


def weakest(items):
    return max((it["verification"] for it in items), key=LEVELS.index)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="print the drafted provenance, write nothing")
    ap.add_argument("--summary", action="store_true", help="print per-level counts and the hand-set rows")
    a = ap.parse_args(argv)
    order, raws = build.load_sources()
    hand, rows, raised, provs_by = [], [], {}, {}
    for eid in order:
        raw = raws[eid]
        provs = provs_by[eid] = {}
        for key in RULE_LISTS:
            for r in raw.get(key, ()) or ():
                items, by_hand = migrate_rule(eid, r)
                provs[(key, r["id"])] = items
                rows.append((eid, r["id"], items))
                if by_hand:
                    hand.append((eid, r["id"], OVERRIDES[(eid, r["id"])][1]))
                    for sid, was, now in raises(eid, r, items):
                        raised[(eid, r["id"], sid)] = (was or "absent", now)
    if set(raised) != set(RAISES):
        raise SystemExit("hand settings that raise an item above the heuristic must be listed in RAISES (and only "
                         f"those): unlisted {sorted(set(raised) - set(RAISES))}, stale {sorted(set(RAISES) - set(raised))}")
    for eid in order:
        path = SRC / f"{eid}.yaml"
        provs = provs_by[eid]
        if a.dry_run:
            for (k, rid), items in provs.items():
                print(f"== {eid} {rid}")
                print(build.dump_yaml(items))
            continue
        old = path.read_text(encoding="utf-8")
        new = rewrite(old, provs)
        after = build.yaml.safe_load(new)
        if _strip_prov(after) != _strip_prov(build.yaml.safe_load(old)):
            raise SystemExit(f"{path.name}: rewrite changed data other than provenance")
        for key in RULE_LISTS:
            for r in after.get(key, ()) or ():
                if r.get("provenance") != provs[(key, r["id"])]:
                    raise SystemExit(f"{path.name} {r['id']}: provenance did not round-trip")
        if new != old:
            path.write_text(new, encoding="utf-8")
    if a.summary or not a.dry_run:
        rc = Counter(weakest(i) for _, _, i in rows)
        ic = Counter(it["verification"] for _, _, i in rows for it in i)
        print(f"{len(rows)} own rules; weakest item per row: " + ", ".join(f"{l} {rc[l]}" for l in LEVELS))
        print(f"{sum(ic.values())} items: " + ", ".join(f"{l} {ic[l]}" for l in LEVELS))
        print(f"{len(hand)} rows set by hand (OVERRIDES); {len(raised)} items raised above the heuristic "
              f"in {len({k[:2] for k in raised})} rows (RAISES)")
        if a.summary:
            for eid, rid, why in hand:
                print(f"  {eid} {rid}: {why}")
            print("raised above the heuristic:")
            for (eid, rid, sid), (was, now) in raised.items():
                print(f"  {eid} {rid} {sid}: {was} -> {now}: {RAISES[(eid, rid, sid)]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

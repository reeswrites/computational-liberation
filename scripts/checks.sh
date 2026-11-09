#!/usr/bin/env bash
# Fixed check set for the preregister -> run -> council loop. Prints only the
# summary lines, labelled, verbatim. Exit 1 if any check fails or the diff
# reports changed/removed rows. Works in any worktree (root from this file).
# Env: resolved as $REPO/.venv, else $PHIL_VENV, else the main checkout's .venv.
# drop_one_match.py hardcodes `uv run phil`; a PATH shim (a fake `uv` that
# execs the venv's phil) makes it work without editing the script.
REPO=$(cd "$(dirname "$0")/.." && pwd); cd "$REPO" || exit 2
if [ -x "$REPO/.venv/bin/phil" ]; then V="$REPO/.venv"
elif [ -n "$PHIL_VENV" ]; then V="$PHIL_VENV"
else V=/Users/rees/Documents/computational-liberation/.venv; fi
echo "env: $V"; export PATH="$V/bin:$PATH"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT; FAIL=0
mkdir "$T/shim"; printf '#!/bin/sh\n[ "$1" = run ] && shift\nexec "%s/bin/$@"\n' "$V" >"$T/shim/uv"; chmod +x "$T/shim/uv"
run() { # label, outfile, command...
  l=$1; o=$2; shift 2; "$@" >"$o" 2>&1 || { FAIL=1; echo "[FAIL] $l (exit $?)"; }
}
show() { echo "== $1"; shift; "$@"; }
run build "$T/build" python data/institutions/build.py --check
run diff "$T/diff" phil rules diff --baseline data/verdicts-baseline.json
run checkall "$T/ca" phil rules check-all
run gate "$T/gate" phil rules gate
mkdir "$T/d"; run dropone "$T/drop" env PATH="$T/shim:$PATH" python scripts/drop_one_match.py "$T/d"
run pytest "$T/py" python -m pytest -q
echo "== build.py --check"; tail -n 1 "$T/build"
echo "== rules diff"; tail -n 1 "$T/diff"
CH=$(grep -Eo '^[0-9]+ changed' "$T/diff" | head -1; true)
grep -Eq '^[0-9]+ changed' "$T/diff" || CH=$(tail -n 1 "$T/diff")
echo "$CH" | grep -Eq '^0 changed' && grep -Eq ' 0 removed' "$T/diff" || FAIL=1
echo "== rules check-all"; grep 'agreement:' "$T/ca"
echo "== rules gate"; grep -E '^(GATE|b |e )' "$T/gate" | cut -c1-200
echo "== drop_one_match (b fails on deleting; PASS elsewhere)"
grep -c 'b=PASS' "$T/drop" | sed 's/^/b=PASS rows: /'; grep 'b=FAIL' "$T/drop" | awk '{print $1, $2}' | paste -sd, -
echo "== pytest"; tail -n 1 "$T/py"
# Ready-to-paste calibration row for docs/scoreboard.md (? = fill by hand)
MOVED=$(grep -Eo '[0-9]+ changed' "$T/diff" | head -1 | cut -d' ' -f1)
echo "== scoreboard row"
echo "| ? | $(date +%F) | ? | ${MOVED:-?} | ? | ?/?/?/? | pytest: $(tail -n 1 "$T/py" | grep -Eo '[0-9]+ passed' | head -1) |"
[ "$FAIL" = 0 ] && echo "ALL CHECKS OK" || echo "CHECKS FAILED"; exit $FAIL

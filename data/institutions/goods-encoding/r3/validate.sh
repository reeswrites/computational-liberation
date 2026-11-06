#!/bin/bash
# usage: validate.sh <entry-id> '<formal>'   (syntax/vocabulary check only; no verdicts)
cd /home/user/computational-liberation && uv run python - "$@" 2>/dev/null <<'PY'
import sys, json
from philengine.schemas_rules import Property, InstitutionJSON
from philengine.rules_lower import validate_property
eid, formal = sys.argv[1], sys.argv[2]
d = [e for e in json.load(open('data/institutions/institutions.json')) if e['id'] == eid]
if not d:
    print('ERRORS'); print('error: unknown entry', eid); sys.exit(0)
inst = InstitutionJSON.model_validate(d[0])
p = Property.model_validate({'name': 'candidate', 'formal': formal, 'gloss': 'x', 'kind': 'freedom', 'polarity': 'unfreedom'})
errs, warns = validate_property(p, inst)
print('OK' if not errs else 'ERRORS'); [print('error:', x) for x in errs]; [print('warning:', x) for x in warns]
PY

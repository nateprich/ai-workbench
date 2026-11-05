#!/usr/bin/env python3
"""Audited read helper for instruction-isolated trials; not an OS sandbox."""
import hashlib
import json
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
target = (root / sys.argv[2]).resolve()
allowed = any(target.is_relative_to(root / part) for part in ('thought-partner', 'fixtures'))
if not allowed or not target.is_file():
    raise SystemExit('Read denied: only extracted pack and case fixtures are available')
data = target.read_bytes()
with (root / 'reads.jsonl').open('a') as log:
    log.write(json.dumps({'path': target.relative_to(root).as_posix(), 'sha256': hashlib.sha256(data).hexdigest()}) + '\n')
print(data.decode())

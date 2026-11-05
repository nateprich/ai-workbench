#!/usr/bin/env python3
"""Prepare per-case workspaces from the exact delivery archive, without answers."""
import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('archive', type=Path)
parser.add_argument('destination', type=Path)
args = parser.parse_args()
assert not args.destination.exists(), 'Use a new trial directory'
cases = json.loads(Path(__file__).with_name('cases.json').read_text())
selections = {}
with zipfile.ZipFile(args.archive) as z:
    assert z.testzip() is None
    for name in z.namelist():
        p = Path(name)
        assert not p.is_absolute() and '..' not in p.parts and p.parts[0] == 'thought-partner'
    for case in cases:
        # Keep descriptive IDs and assessment labels out of responders' paths.
        neutral_name = 'case-' + case['id'].split('-', 1)[0]
        selections[case['id']] = neutral_name
        root = args.destination / neutral_name
        z.extractall(root)
        for helper in ['read_case.py', 'harness.md']:
            shutil.copyfile(Path(__file__).with_name(helper), root / helper)
        for path, text in case.get('fixtures', {}).items():
            target = (root / 'fixtures' / path).resolve()
            assert target.is_relative_to((root / 'fixtures').resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        (root / 'prompt.txt').write_text(case['prompt'] + '\n')
        (root / 'environment.json').write_text(json.dumps({
            'archive_sha256': hashlib.sha256(args.archive.read_bytes()).hexdigest(),
            'isolation': 'fresh context; extracted pack and fixtures; audited allowed reads; inherited host permissions',
            'capabilities': 'local pack/fixture reads and explicitly authorized fixture edits only; no web, connectors, real user questions, or additional agents',
        }, indent=2) + '\n')
(args.destination / 'selections.json').write_text(json.dumps(selections, indent=2) + '\n')
print(f'Prepared {len(cases)} isolated-source case workspaces.')

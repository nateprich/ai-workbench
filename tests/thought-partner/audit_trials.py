#!/usr/bin/env python3
"""Check cold-start evidence integrity; human/independent review judges responses."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument('archive', type=Path)
parser.add_argument('trials', type=Path)
args = parser.parse_args()
cases = json.loads(Path(__file__).with_name('cases.json').read_text())
selection_file = args.trials / 'selections.json'
selections = json.loads(selection_file.read_text()) if selection_file.exists() else {}
adjudication_file = args.trials / 'adjudications.json'
adjudications = json.loads(adjudication_file.read_text()) if adjudication_file.exists() else {}
allowed_writes = {'13-domain-write': {'GLOSSARY.md'}, '24-authorized-followthrough': {'editor.html'}}
with zipfile.ZipFile(args.archive) as z:
    pack_hashes = {name: sha(z.read(name)) for name in z.namelist()}
summary = []
for case in cases:
    root = (args.trials / selections.get(case['id'], case['id'])).resolve()
    assert root.is_relative_to(args.trials.resolve()), 'Retry selection escapes trial root'
    if not (root / 'response.md').exists():
        summary.append({'id': case['id'], 'status': 'pending'})
        continue
    if case.get('followup'):
        if not (root / 'response-2.md').exists():
            summary.append({'id': case['id'], 'status': 'pending-followup'})
            continue
        assert (root / 'response-1.md').exists(), 'Missing first-turn evidence'
        assert (root / 'response.md').read_bytes() == (root / 'response-2.md').read_bytes(), 'Final response differs from continuation evidence'
    audit = json.loads((root / 'audit.json').read_text())
    if audit['additional_reads']:
        decision = adjudications.get(case['id'], {})
        assert decision.get('disposition') == 'metadata-only', f'Unresolved read-trace exception: {case["id"]}'
        assert decision.get('audit_sha256') == sha((root / 'audit.json').read_bytes()), 'Adjudication no longer matches evidence'
        assert decision.get('reason'), 'Missing adjudication rationale'
    actual_pack = {p.relative_to(root).as_posix(): sha(p.read_bytes()) for p in (root / 'thought-partner').rglob('*') if p.is_file()}
    assert actual_pack == pack_hashes, f'Pack changed: {case["id"]}'
    environment = json.loads((root / 'environment.json').read_text())
    assert environment['archive_sha256'] == sha(args.archive.read_bytes()), 'Wrong tested archive'
    fixtures = case.get('fixtures', {})
    changed = set()
    for name, original in fixtures.items():
        if (root / 'fixtures' / name).read_text() != original:
            changed.add(name)
    assert changed <= allowed_writes.get(case['id'], set()), f'Unauthorized fixture edit: {case["id"]}'
    if case['id'] in allowed_writes:
        assert changed == allowed_writes[case['id']], f'Authorized edit not performed: {case["id"]}'
    actual_fixtures = {p.relative_to(root / 'fixtures').as_posix() for p in (root / 'fixtures').rglob('*') if p.is_file()} if (root / 'fixtures').exists() else set()
    assert actual_fixtures == set(fixtures), f'Unexpected fixture file: {case["id"]}'
    reads = [json.loads(line) for line in (root / 'reads.jsonl').read_text().splitlines()]
    assert any(r['path'] == 'thought-partner/SKILL.md' for r in reads), 'Entrypoint not loaded'
    for read in reads:
        name = read['path']
        if name in pack_hashes:
            assert read['sha256'] == pack_hashes[name], f'Wrong pack bytes read: {case["id"]}'
        elif name.startswith('fixtures/'):
            rel = name.removeprefix('fixtures/')
            assert rel in fixtures, 'Read not in case fixtures'
            valid = {sha(fixtures[rel].encode()), sha((root / name).read_bytes())}
            assert read['sha256'] in valid, 'Wrong fixture bytes read'
        else:
            raise AssertionError(f'Unexpected audited read: {name}')
    summary.append({'id': case['id'], 'status': 'evidence-valid', 'workspace': root.relative_to(args.trials.resolve()).as_posix(), 'read_paths': sorted(set(r['path'] for r in reads)), 'fixture_changes': sorted(changed)})
print(json.dumps(summary, indent=2))

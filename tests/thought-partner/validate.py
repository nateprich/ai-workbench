#!/usr/bin/env python3
"""Validate the portable pack and optionally build/extract a deterministic ZIP.

Development helper only; the installed skill has no Python dependency.
"""
import argparse
import hashlib
import json
import re
import shutil
import stat
import zipfile
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate(pack, license_manifest):
    pack = pack.resolve()
    assert pack.name == 'thought-partner', 'Unexpected folder name'
    files = sorted(p for p in pack.rglob('*') if p.is_file())
    assert [p.relative_to(pack).as_posix() for p in files if p.name == 'SKILL.md'] == ['SKILL.md'], 'Pack must have one entrypoint'
    assert not any(p.is_symlink() for p in pack.rglob('*')), 'Pack must not depend on symlinks'
    body = (pack / 'SKILL.md').read_text()
    front = re.match(r'\A---\n(.*?)\n---\n', body, re.S)
    assert front and re.search(r'^name: thought-partner$', front[1], re.M), 'Invalid skill identity'
    assert re.search(r'^description: .+', front[1], re.M), 'Missing description'
    for required in ['LICENSE', 'PROVENANCE.md', 'README.md']:
        assert (pack / required).is_file(), f'Missing {required}'
    for path in files:
        assert not path.name.startswith('.'), f'Unexpected hidden file: {path}'
        if path.suffix == '.md':
            text = path.read_text()
            assert '/Volumes/' not in text and 'file://' not in text, f'Machine-local path: {path}'
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                resolved = (path.parent / target.split('#')[0]).resolve()
                assert resolved.is_relative_to(pack), f'Link escapes installed pack: {path}: {target}'
                assert resolved.exists(), f'Broken local link: {path}: {target}'
    for item in license_manifest:
        license_path = pack / item['path']
        assert digest(license_path.read_bytes()) == item['sha256'], f'License text changed: {item["path"]}'
    provenance = (pack / 'PROVENANCE.md').read_text()
    for path in (pack / 'references').glob('*.md'):
        assert f'references/{path.name}' in provenance, f'Untracked reference: {path.name}'
    return {p.relative_to(pack).as_posix(): digest(p.read_bytes()) for p in files}


def archive_pack(pack, archive):
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in sorted(p for p in pack.rglob('*') if p.is_file()):
            info = zipfile.ZipInfo('thought-partner/' + path.relative_to(pack).as_posix(), date_time=(2026, 11, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            z.writestr(info, path.read_bytes())


def extract(archive, destination):
    assert not destination.exists(), 'Use a new extraction directory'
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None, 'Archive CRC failed'
        names = z.namelist()
        assert len(names) == len(set(names)), 'Duplicate archive paths'
        for name in names:
            parts = Path(name).parts
            assert parts and parts[0] == 'thought-partner' and '..' not in parts and not Path(name).is_absolute(), 'Unsafe archive path'
        z.extractall(destination)


def migration_check(before, extracted, destination):
    assert not destination.exists(), 'Use a new migration directory'
    destination.mkdir(parents=True)
    active = destination / 'active'
    active.mkdir()
    legacy = active / 'interview'
    shutil.copytree(before / 'thought-partner', legacy)
    skill = legacy / 'SKILL.md'
    skill.write_text(skill.read_text().replace('name: thought-partner', 'name: interview-first'))
    other = active / 'independent-skill'
    other.mkdir()
    (other / 'SKILL.md').write_text('Independent skill fixture; keep me.\n')
    original = digest((other / 'SKILL.md').read_bytes())
    backup = destination / 'backups' / 'interview'
    backup.parent.mkdir()
    legacy_hashes = {p.relative_to(legacy).as_posix(): digest(p.read_bytes()) for p in legacy.rglob('*') if p.is_file()}
    shutil.move(str(legacy), str(backup))
    shutil.copytree(extracted / 'thought-partner', active / 'thought-partner')
    assert not legacy.exists()
    assert legacy_hashes == {p.relative_to(backup).as_posix(): digest(p.read_bytes()) for p in backup.rglob('*') if p.is_file()}
    assert not backup.is_relative_to(active)
    assert original == digest((other / 'SKILL.md').read_bytes()), 'Unrelated skill changed'
    catalog = sorted(p.relative_to(active).as_posix() for p in active.rglob('SKILL.md'))
    assert catalog == ['independent-skill/SKILL.md', 'thought-partner/SKILL.md'], catalog
    assert not any('name: interview-first' in p.read_text() for p in active.rglob('SKILL.md'))
    # Also replace the renamed two-file intermediate installation.
    intermediate = destination / 'intermediate'
    shutil.copytree(before / 'thought-partner', intermediate / 'thought-partner')
    shutil.rmtree(intermediate / 'thought-partner')
    shutil.copytree(extracted / 'thought-partner', intermediate / 'thought-partner')
    assert [p.relative_to(intermediate).as_posix() for p in intermediate.rglob('SKILL.md')] == ['thought-partner/SKILL.md']
    expected = {p.relative_to(extracted / 'thought-partner').as_posix(): digest(p.read_bytes()) for p in (extracted / 'thought-partner').rglob('*') if p.is_file()}
    for migrated in [active / 'thought-partner', intermediate / 'thought-partner']:
        assert expected == {p.relative_to(migrated).as_posix(): digest(p.read_bytes()) for p in migrated.rglob('*') if p.is_file()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pack', type=Path)
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--extract', type=Path)
    parser.add_argument('--before', type=Path)
    parser.add_argument('--migration', type=Path)
    args = parser.parse_args()
    manifest = json.loads(Path(__file__).with_name('licenses.json').read_text())
    hashes = validate(args.pack, manifest)
    result = {'files': len(hashes), 'file_sha256': hashes}
    if args.archive:
        archive_pack(args.pack, args.archive)
        result['archive_sha256'] = digest(args.archive.read_bytes())
    if args.extract:
        assert args.archive
        extract(args.archive, args.extract)
        assert hashes == validate(args.extract / 'thought-partner', manifest), 'Extracted bytes differ'
        result['extraction'] = 'byte-identical'
    if args.migration:
        assert args.before and args.extract
        migration_check(args.before, args.extract, args.migration)
        result['migration'] = 'legacy and intermediate replacement passed; independent skill preserved'
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

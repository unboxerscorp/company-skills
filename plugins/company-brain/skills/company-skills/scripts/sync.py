"""Sync only owned company skills from the fixed public catalog. No dependencies."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import urllib.request

BASE = 'https://unboxerscorp.github.io/company-skills/'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def fetch(path):
    # No redirects to another host, traversal, or arbitrary catalog URLs.
    p = PurePosixPath(path)
    if not path or p.is_absolute() or any(x in ('.', '..') for x in path.split('/')) or ':' in path or '\\' in path:
        raise ValueError('Invalid download path')
    with urllib.request.urlopen(BASE + path, timeout=20) as response:
        if not response.url.startswith(BASE):
            raise ValueError('Unexpected download host')
        data = response.read(4_000_001)
        if len(data) > 4_000_000:
            raise ValueError('Download too large')
        return data

def inventory(path):
    if not path.is_dir() or any(p.is_symlink() for p in path.rglob('*')):
        return None
    return {p.relative_to(path).as_posix(): digest(p.read_bytes())
            for p in path.rglob('*') if p.is_file() and '__pycache__' not in p.parts}

def synchronize(root, state_path, download=fetch):
    catalog = json.loads(download('catalog.json'))
    if catalog.get('schema_version') != 1 or not isinstance(catalog.get('skills'), list):
        raise ValueError('Unsupported catalog')
    desired, payloads = {}, {}
    for skill in catalog['skills']:
        name = skill['name']
        if not re.fullmatch('[a-z][a-z0-9-]{0,63}', name) or name in desired:
            raise ValueError('Invalid or duplicate skill name')
        files = skill['files']
        if not isinstance(files, dict) or 'SKILL.md' not in files:
            raise ValueError('Missing skill manifest')
        desired[name], payloads[name] = {}, {}
        for rel, entry in files.items():
            p = PurePosixPath(rel)
            if p.is_absolute() or any(x in ('.', '..') for x in rel.split('/')) or '\\' in rel or ':' in rel or not rel:
                raise ValueError('Unsafe skill path')
            url = f'skills/{name}/{rel}'
            if entry['path'] != url or not re.fullmatch('[a-f0-9]{64}', entry['sha256']):
                raise ValueError('Invalid file metadata')
            data = download(url)
            if digest(data) != entry['sha256']:
                raise ValueError('Checksum mismatch')
            payloads[name][rel] = data
            desired[name][rel] = entry['sha256']
        if not payloads[name]['SKILL.md'].decode().startswith(f'---\nname: {name}\n'):
            raise ValueError('Manifest name mismatch')
    if 'company-skills' not in desired:
        raise ValueError('Missing bootstrap skill; refusing removal')
    # All downloads verified before any installation or removal.
    root.mkdir(parents=True, exist_ok=True)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {'managed': {}}
    managed = state['managed']
    if any(not re.fullmatch('[a-z][a-z0-9-]{0,63}', n) for n in managed):
        raise ValueError('Invalid managed state')
    results = {'added': [], 'updated': [], 'removed': [], 'conflicts': []}
    for name, expected in desired.items():
        target = root/name
        current = inventory(target) if target.exists() else None
        if name in managed and current != managed[name]:
            results['conflicts'].append(name)
            continue
        if name not in managed and (target.exists() or target.is_symlink()) and current != expected:
            results['conflicts'].append(name)
            continue
        if current == expected:
            managed[name] = expected
            continue
        with tempfile.TemporaryDirectory(dir=state_path.parent) as tmp:
            staged = Path(tmp)/name
            staged.mkdir()
            for rel, data in payloads[name].items():
                p = staged/rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
            if target.exists() or target.is_symlink():
                # Backup only the entry: symlink destinations remain untouched.
                backup = state_path.parent/'backups'/name
                backup.parent.mkdir(exist_ok=True)
                if backup.is_symlink() or backup.is_file(): backup.unlink()
                elif backup.exists(): shutil.rmtree(backup)
                target.rename(backup)
            try:
                shutil.move(str(staged), target)
            except Exception:
                if 'backup' in locals() and (backup.exists() or backup.is_symlink()) and not target.exists():
                    backup.rename(target)
                raise
        results['updated' if name in managed else 'added'].append(name)
        managed[name] = expected
        save(state_path, {'managed': managed, 'status': 'running'})
    for name in list(managed):
        if name in desired:
            continue
        if not re.fullmatch('[a-z][a-z0-9-]{0,63}', name):
            raise ValueError('Invalid managed state')
        target = root/name
        if inventory(target) != managed[name]:
            results['conflicts'].append(name)
            continue
        if target.is_symlink(): target.unlink()
        else: shutil.rmtree(target)
        del managed[name]
        results['removed'].append(name)
        save(state_path, {'managed': managed, 'status': 'running'})
    save(state_path, {'managed': managed, 'status': 'completed', 'results': results})
    return results

def save(path, state):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2)+'\n')
    os.replace(temp, path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tool', required=True, choices=['codex', 'claude-code'])
    args = parser.parse_args()
    home = Path.home()
    root = home/('.agents' if args.tool == 'codex' else '.claude')/'skills'
    state_path = home/'.config/company-skills'/args.tool/'state.json'
    state_path.parent.mkdir(parents=True, exist_ok=True)
    lock = (state_path.parent/'sync.lock').open('a+b')
    lock.write(b'0'); lock.flush(); lock.seek(0)
    if os.name == 'nt':
        import msvcrt
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    else:
        import fcntl
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    state = json.loads(state_path.read_text()) if state_path.exists() else {'managed': {}}
    save(state_path, {**state, 'status': 'started'})
    try:
        print(json.dumps(synchronize(root, state_path), ensure_ascii=False))
    except Exception as error:
        current = json.loads(state_path.read_text())
        save(state_path, {**current, 'status': 'failed', 'error': type(error).__name__})
        raise SystemExit('Company skills sync failed: '+type(error).__name__)

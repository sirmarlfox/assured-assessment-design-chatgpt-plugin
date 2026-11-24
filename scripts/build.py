#!/usr/bin/env python3
"""Build the installable plugin and mirror its upload-ready knowledge files."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build():
    manifest = json.loads((ROOT / 'plugin.json').read_text())
    name, version = manifest['name'], manifest['version']
    refs = ROOT / 'skills' / 'assured-assessment-design' / 'references'
    for path in sorted(refs.glob('*.md')):
        (ROOT / 'knowledge' / path.name).write_bytes(path.read_bytes())
    files = [ROOT / 'plugin.json', ROOT / 'LICENSE.md', ROOT / 'CREDITS.md']
    files += sorted(p for p in (ROOT / 'skills').rglob('*') if p.is_file())
    if any(p.is_symlink() for p in files):
        raise ValueError('Symlinks are not permitted')
    out = ROOT / 'dist'
    out.mkdir(exist_ok=True)
    archive = out / f'{name}-{version}.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(files):
            relative = p.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f'{name}/{relative}', date_time=(2026, 11, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (out / 'SHA256SUMS').write_text(f'{digest}  {archive.name}\n')
    print(json.dumps({'archive': str(archive), 'bytes': archive.stat().st_size, 'sha256': digest, 'files': len(files)}))
    return archive


if __name__ == '__main__':
    build()

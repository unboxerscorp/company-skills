"""Build the employee site, versioned catalog and credential-free skill downloads."""
from pathlib import Path
import shutil, zipfile, json, hashlib
r=Path(__file__).resolve().parent.parent
out=r/'dist/site'
if out.exists(): shutil.rmtree(out)
shutil.copytree(r/'site',out)
(out/'.nojekyll').touch()
(out/'download').mkdir()
plugin=r/'plugins/company-brain'
entries=[]
for skill in sorted((plugin/'skills').iterdir()):
    p=skill/'SKILL.md'
    if not p.is_file(): continue
    assert p.read_text().startswith('---\nname: '+skill.name+'\n')
    files={}
    with zipfile.ZipFile(out/'download'/f'{skill.name}.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob('*')):
            if not f.is_file() or '__pycache__' in f.parts: continue
            rel=f.relative_to(skill).as_posix()
            path=f'skills/{skill.name}/{rel}'
            dest=out/path
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(f,dest)
            z.write(f,f'{skill.name}/{rel}')
            files[rel]={'path':path,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
    entries.append({'name':skill.name,'files':files})
(out/'catalog.json').write_text(json.dumps({'schema_version':1,'version':json.loads((plugin/'plugin.json').read_text())['version'],'skills':entries},ensure_ascii=False,indent=2))
print('Built catalog and validated all skill ZIPs')

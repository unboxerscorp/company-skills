"""Build a static employee catalog and credential-free skill downloads."""
from pathlib import Path
import shutil, zipfile, json
r=Path(__file__).resolve().parent.parent
out=r/'dist/site'
if out.exists(): shutil.rmtree(out)
shutil.copytree(r/'site',out)
(out/'.nojekyll').touch()
(out/'download').mkdir()
plugin=r/'plugins/company-brain'
for skill in sorted((plugin/'skills').iterdir()):
    p=skill/'SKILL.md'
    if not p.is_file(): continue
    assert p.read_text().startswith('---\nname: '+skill.name+'\n')
    with zipfile.ZipFile(out/'download'/f'{skill.name}.zip','w',zipfile.ZIP_DEFLATED) as z:
        z.write(p,f'{skill.name}/SKILL.md')
(out/'catalog.json').write_text(json.dumps({'version':json.loads((plugin/'plugin.json').read_text())['version'],'skills':[p.name for p in sorted((plugin/'skills').iterdir()) if (p/'SKILL.md').is_file()]},ensure_ascii=False,indent=2))
print('Built catalog and validated all skill ZIPs')

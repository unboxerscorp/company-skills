"""Verify real add/update/remove behavior, conflicts and failure isolation."""
import importlib.util
import json
from pathlib import Path
import tempfile

r=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('sync',r/'plugins/company-brain/skills/company-skills/scripts/sync.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)

def server(skills):
    files={}; entries=[]
    for name, body in skills.items():
        data=f'---\nname: {name}\n---\n{body}'.encode()
        path=f'skills/{name}/SKILL.md';files[path]=data
        entries.append({'name':name,'files':{'SKILL.md':{'path':path,'sha256':s.digest(data)}}})
    files['catalog.json']=json.dumps({'schema_version':1,'skills':entries}).encode()
    return files

with tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp)/'skills'; state=Path(tmp)/'state/state.json'
    one=server({'company-skills':'bootstrap','work-a':'one'})
    assert s.synchronize(root,state,one.__getitem__)['added']==['company-skills','work-a']
    assert not any(s.synchronize(root,state,one.__getitem__).values())
    personal=root/'personal';personal.mkdir();(personal/'SKILL.md').write_text('private')
    two=server({'company-skills':'bootstrap','work-a':'two','work-b':'new'})
    changed=s.synchronize(root,state,two.__getitem__)
    assert changed['updated']==['work-a'] and changed['added']==['work-b']
    (root/'work-b/SKILL.md').write_text('user modification')
    three=server({'company-skills':'bootstrap'})
    changed=s.synchronize(root,state,three.__getitem__)
    assert changed['removed']==['work-a'] and changed['conflicts']==['work-b']
    assert (root/'work-b/SKILL.md').read_text()=='user modification'
    assert (personal/'SKILL.md').read_text()=='private'
    before=state.read_bytes()
    corrupt=server({'company-skills':'bootstrap','work-c':'test'})
    corrupt['skills/work-c/SKILL.md']=b'corrupt'
    try:s.synchronize(root,state,corrupt.__getitem__)
    except ValueError:pass
    else:raise AssertionError('Corrupt download accepted')
    assert not (root/'work-c').exists() and state.read_bytes()==before
    try:s.synchronize(root,state,server({}).__getitem__)
    except ValueError:pass
    else:raise AssertionError('Empty catalog removed installations')
    external=Path(tmp)/'external';external.mkdir();(external/'SKILL.md').write_bytes(one['skills/work-a/SKILL.md'])
    (root/'work-a').symlink_to(external,target_is_directory=True)
    s.synchronize(root,state,one.__getitem__)
    s.synchronize(root,state,three.__getitem__)
    assert external.exists() and (external/'SKILL.md').exists()
print('PASS: install, repeat, update, add, remove, personal/local-edit preservation, checksum/empty-catalog rejection, external symlink safety')

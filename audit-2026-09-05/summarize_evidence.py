from pathlib import Path
import json, csv, re, difflib, hashlib, subprocess
P=Path(__file__).parent
d=json.loads((P/'inventory.json').read_text(encoding='utf-8'))
roots={k:Path(v) for k,v in d['corpora'].items()}
def text(k,f): return (roots[k]/f).read_text(encoding='utf-8-sig')
def norm(s): return '\n'.join(x.rstrip() for x in s.splitlines()).strip()
def core(s): return norm(re.sub(r'<project-local>.*?</project-local>', '',s,flags=re.S))
def git(repo,*args):
    return subprocess.run(['git','--no-optional-locks','-c',f'safe.directory={repo.as_posix()}','-C',str(repo),*args],capture_output=True).stdout
rows=[]
for k,files in d['files'].items():
    for f,v in files.items():
        st=(roots[k]/f).stat()
        v.update({'hardlink_count':st.st_nlink,'device':st.st_dev,'file_id':st.st_ino})
        rows.append({'corpus':k,'file':f,'sha256':v['sha256'],'normalized_sha256':v.get('normalized_sha256',''),'core_sha256':v.get('clean_core_sha256',''),'bytes':v['bytes'],'last_commit':v.get('last_commit',''),'mtime':v['mtime'],'hardlink_count':st.st_nlink,'file_id':st.st_ino})
with (P/'file-matrix.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(P/'inventory.json').write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
lines=['# Verified file evidence\n','Generated from the inspected working trees. SHA-256 prefixes below are byte hashes; full hashes, file IDs, local blocks and Git dates are in `inventory.json` and `file-matrix.csv`.\n','## Primary corpus matrix\n','| File | H | M | A | F |','|---|---|---|---|---|']
for f in sorted(set().union(*(d['files'][k] for k in 'HMAF'))):
    cells=[d['files'][k].get(f,{}).get('sha256','—')[:10] for k in 'HMAF']
    lines.append('| '+f+' | '+' | '.join(cells)+' |')
lines+=['\n## Actual project-local blocks\n']
for k in 'HMAF':
    lines.append(f'### {k}\n')
    for f,v in d['files'][k].items():
        if v.get('local_blocks'):
            lines+=['**'+f+'**\n','```xml\n'+'\n'.join(v['local_blocks'])+'\n```\n']
lines+=['## Portable skill changes versus M\n','Only changed lines are shown. Full context is in the pairwise `.diff` files. Appendices, missing skills and local blocks have separate coverage.\n']
for k in ['H','A','F','L']:
    lines.append(f'### M versus {k}\n')
    for f in sorted(set(d['files']['M'])&set(d['files'][k])):
        if not f.endswith('/SKILL.md'):continue
        a,b=core(text('M',f)),core(text(k,f))
        if a==b:continue
        lines.append(f'**{f}** — {d["files"][k][f].get("last_commit","no Git history")}\n')
        diff=difflib.unified_diff(a.splitlines(),b.splitlines(),n=0)
        delta=[x for x in diff if x.startswith(('+','-')) and not x.startswith(('+++','---'))]
        lines.append('```diff\n'+'\n'.join(delta)+'\n```\n')
lines+=['## History checks\n']
for k in ['M','A','F']:
    h=d['histories'][k]
    lines += [f'### {k}\n',f'HEAD: {h["head"]["out"]}\n','Skill-path history:\n','```text\n'+h['history']['out']+'\n```\n','Loader Git index:\n','```text\n'+h['links_index']['out']+'\n```\n',f'`core.symlinks`: {h["symlinks_setting"]["out"]}\n']
lines+=['## Neighboring corpora\n','| Skill entrypoint | L | L2 | W | S |','|---|---|---|---|---|']
for f in sorted(set().union(*(d['files'][k] for k in ['L','L2','W','S']))):
    if not f.endswith('/SKILL.md'):continue
    cells=[d['files'][k].get(f,{}).get('sha256','—')[:10] for k in ['L','L2','W','S']]
    lines.append('| '+f+' | '+' | '.join(cells)+' |')
lines+=['\n## Supplementary harness files\n']
scripts={'M':roots['M'].parent/'scripts/move_doc.py','A':roots['A'].parent/'scripts/move_doc.py','F':roots['F'].parent/'scripts/move_doc.py'}
for k,p in scripts.items(): lines.append(f'- {k}: `{p}` SHA-256 `{hashlib.sha256(p.read_bytes()).hexdigest()}`')
for k in ['A','F']:
    a,b=scripts['M'].read_text(encoding='utf-8'),scripts[k].read_text(encoding='utf-8')
    delta=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='M/move_doc.py',tofile=f'{k}/move_doc.py'))
    (P/f'move_doc-M-to-{k}.diff').write_text(delta,encoding='utf-8')
    lines+=['\n```diff\n'+delta+'\n```\n']
archive=d['meteoscape_zip']; mismatches=[]
for f,h in archive.items():
    rel=f.removeprefix('skills/')
    if d['files']['M'].get(rel,{}).get('sha256') != h:mismatches.append(f)
zip_missing=[f for f in d['files']['M'] if f'skills/{f}' not in archive and f not in archive]
lines+=['## Archive verification\n',f'M archive: {len(archive)} files; mismatches with current M: {mismatches}; M files missing from archive: {zip_missing}.\n']
(P/'EVIDENCE.md').write_text('\n'.join(lines),encoding='utf-8')
print('Archive',len(archive),mismatches,zip_missing)
print('Hardlinks >1:',[(r['corpus'],r['file'],r['hardlink_count']) for r in rows if r['hardlink_count']>1])
print('Primary last skill changes:')
for f in sorted(d['files']['M']):
    if f.endswith('/SKILL.md'):
        print(f, *[k+': '+d['files'][k].get(f,{}).get('last_commit','absent') for k in ['M','A','F']],sep=' | ')
print('Main skill groups compared with M:')
for k in 'HAF':
    eq=[];changed=[]
    for f in sorted(set(d['files']['M'])&set(d['files'][k])):
        if f.endswith('/SKILL.md'):
            (eq if core(text('M',f))==core(text(k,f)) else changed).append(f.split('/')[0])
    print(k,'equal',eq,'different',changed)
print('L latest skill history:',d['histories']['L']['history']['out'].splitlines()[:3])

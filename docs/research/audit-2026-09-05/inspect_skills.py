"""Read-only corpus inventory; writes evidence only beside this script."""
from pathlib import Path
import os, re, json, hashlib, difflib, subprocess, zipfile
from datetime import datetime, timezone

OUT = Path(__file__).parent
ROOTS = [Path('D:/Dev/AI'), Path('D:/Dev/DriftSense/workspace')]
SKIP = {'.git', 'node_modules', '.venv', 'venv', '.pytest_cache', '.ruff_cache', '__pycache__', '.mypy_cache', 'dist', 'build', '.next', '.metadata'}
CORPORA = {
    'H': Path('D:/Dev/AI/.agents/skills'),
    'M': Path('D:/Dev/AI/meteoscape/.agents/skills'),
    'A': Path('D:/Dev/DriftSense/workspace/agents/skills'),
    'F': Path('D:/Dev/DriftSense/workspace/forecast_collector/.agents/skills'),
    'L': Path('D:/Dev/AI/life/.agents/skills'),
    'L2': Path('D:/Dev/AI/life-2/.agents/skills'),
    'W': Path('D:/Dev/AI/weather-mcp/.cursor/skills'),
    'S': Path('D:/Dev/AI/skills-main/skills'),
}
REPOS = {k: p for k,p in zip(['M','A','F','L','L2','W','S'], [Path('D:/Dev/AI/meteoscape'),Path('D:/Dev/DriftSense/workspace/agents'),Path('D:/Dev/DriftSense/workspace/forecast_collector'),Path('D:/Dev/AI/life'),Path('D:/Dev/AI/life-2'),Path('D:/Dev/AI/weather-mcp'),Path('D:/Dev/AI/skills-main')])}
errors, links, entrypoints, instructions, framework_dirs = [], [], [], [], []
def walk(path):
    try:
        entries = sorted(os.scandir(path), key=lambda e:e.name.lower())
    except OSError as e:
        errors.append({'path':str(path),'error':str(e)})
        return
    for ent in entries:
        p = Path(ent.path)
        if ent.is_symlink() or (hasattr(ent, 'is_junction') and ent.is_junction()):
            try:
                target=os.readlink(p)
                resolved=os.path.abspath(os.path.join(p.parent,target))
                links.append({'path':str(p),'target':target,'resolved':resolved,'exists':p.exists(),'is_dir':p.is_dir(),'target_exists':Path(resolved).exists(),'target_is_dir':Path(resolved).is_dir()})
            except OSError as e: errors.append({'path':str(p),'error':str(e)})
        elif ent.is_dir(follow_symlinks=False):
            if ent.name in {'.agents','.claude','.codex','.cursor'}: framework_dirs.append(str(p))
            if ent.name not in SKIP and p != OUT: yield from walk(p)
        else: yield p
for root in ROOTS:
    for p in walk(root):
        if p.name == 'SKILL.md': entrypoints.append(str(p))
        if p.name in {'AGENTS.md','AGENTS.override.md','CLAUDE.md','.cursorrules'} or p.suffix == '.mdc': instructions.append(str(p))
for framework in ['.agents','.claude','.codex','.cursor']:
    p=Path('C:/Users/fimar')/framework/'skills'
    if p.exists():
        for f in walk(p):
            if f.name=='SKILL.md': entrypoints.append(str(f))
def git(repo,*args):
    result=subprocess.run(['git','--no-optional-locks','-c',f'safe.directory={repo.as_posix()}','-C',str(repo),*args],capture_output=True,encoding='utf-8',errors='replace')
    return {'code':result.returncode,'out':result.stdout.strip(),'err':result.stderr.strip()}
def sha(b): return hashlib.sha256(b).hexdigest()
def normalize(s): return s.replace('\r\n','\n').replace('\r','\n')
def body(s): return re.sub(r'<project-local>.*?</project-local>', '',s,flags=re.S).strip()+'\n'
def clean(s): return '\n'.join(line.rstrip() for line in s.splitlines()).strip()+'\n'
files, texts, histories = {},{},{}
for key, root in CORPORA.items():
    files[key], texts[key] = {}, {}
    if key in REPOS:
        repo=REPOS[key]
        histories[key] = {'head':git(repo,'log','-1','--format=%h %aI %s'), 'status':git(repo,'status','--short','--',str(root),'.agents/scripts','.agents/README.md','.claude','.codex','.cursor','scripts/move_doc.py'), 'history':git(repo,'log','--format=%h %aI %s','--',str(root)), 'links_index':git(repo,'ls-files','--stage','--','.claude','.codex','.cursor'), 'symlinks_setting':git(repo,'config','--get','core.symlinks')}
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(root).as_posix()
        b=p.read_bytes()
        rec={'sha256':sha(b),'bytes':len(b),'mtime':datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()}
        if p.suffix == '.md':
            s=normalize(b.decode('utf-8-sig')); texts[key][rel]=s
            rec.update({'normalized_sha256':sha(s.encode()),'core_sha256':sha(body(s).encode()),'clean_core_sha256':sha(clean(body(s)).encode()),'local_blocks':re.findall(r'<project-local>.*?</project-local>',s,re.S), 'local_open':s.count('<project-local>'),'local_close':s.count('</project-local>'),'crlf':b.count(b'\r\n'),'lf_only':b.count(b'\n')-b.count(b'\r\n')})
            if p.name=='SKILL.md':
                rec['frontmatter'] = s.split('---',2)[1] if s.startswith('---') and len(s.split('---',2))==3 else None
            missing=[]
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s):
                dest=target.split('#')[0]
                if dest and not re.match(r'^[a-z]+:|^/|[{}<>]',dest) and not (p.parent/dest).exists(): missing.append(target)
            rec['missing_relative_links']=missing
        if key in {'M','A','F','L','W'}:
            rec['last_commit']=git(REPOS[key],'log','-1','--format=%h %aI %s','--',str(p))['out']
        files[key][rel]=rec

diffsummary=[]
for a,b in [('H','M'),('M','A'),('M','F'),('A','F'),('M','L'),('L2','L'),('W','H')]:
    lines=[]
    for rel in sorted(texts[a].keys()|texts[b].keys()):
        sa,sb=texts[a].get(rel),texts[b].get(rel)
        if sa==sb: continue
        kind='missing' if sa is None or sb is None else 'whitespace-only' if clean(sa)==clean(sb) else 'local-only' if body(sa)==body(sb) else 'whitespace-core' if clean(body(sa))==clean(body(sb)) else 'core/appendix'
        diffsummary.append({'pair':f'{a}-{b}','file':rel,'kind':kind})
        lines.append(f'### {rel} [{kind}]\n')
        lines.extend(difflib.unified_diff((sa or '').splitlines(True),(sb or '').splitlines(True),fromfile=f'{a}/{rel}',tofile=f'{b}/{rel}',n=3))
        lines.append('\n')
    (OUT/f'{a}-to-{b}.diff').write_text(''.join(lines),encoding='utf-8')
z=Path('D:/Dev/AI/meteoscape/.agents/skills.zip')
archive={}
if z.exists():
    with zipfile.ZipFile(z) as f:
        archive={i.filename:sha(f.read(i)) for i in f.infolist() if not i.is_dir()}
payload={'generated':datetime.now(timezone.utc).isoformat(),'corpora':{k:str(v) for k,v in CORPORA.items()},'skip':sorted(SKIP),'errors':errors,'links':links,'entrypoints':entrypoints,'instructions':instructions,'framework_dirs':framework_dirs,'files':files,'histories':histories,'diffsummary':diffsummary,'meteoscape_zip':archive}
(OUT/'inventory.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'counts':{k:{'skills':sum(p.endswith('/SKILL.md') for p in fs),'files':len(fs)} for k,fs in files.items()},'errors':errors,'links':links,'framework_dirs':framework_dirs,'diffsummary':[d for d in diffsummary if d['pair'] in ['M-A','M-F']]},indent=2))

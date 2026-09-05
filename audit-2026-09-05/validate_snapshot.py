from pathlib import Path
import json, hashlib, re
P=Path(__file__).parent
d=json.loads((P/'inventory.json').read_text(encoding='utf-8'))
changed=[]; missing=[]; malformed=[]; counts={}
def prose(s):
    out=[]; fence=False
    for line in s.splitlines():
        if re.match(r'^\s*(```|~~~)',line): fence=not fence;continue
        if not fence: out.append(re.sub(r'`[^`]*`','',line))
    return '\n'.join(out)
for k,root in d['corpora'].items():
    for f,v in d['files'][k].items():
        p=Path(root)/f
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=v['sha256']:changed.append([k,f])
        if k not in 'HMAF' or not f.endswith('.md'):continue
        s=p.read_text(encoding='utf-8-sig')
        if f.endswith('/SKILL.md'):
            fm=v.get('frontmatter') or ''
            if not re.search(r'^name:\s*\S',fm,re.M) or not re.search(r'^description:\s*\S',fm,re.M):malformed.append([k,f])
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose(s)):
            rel=target.split('#')[0]
            if rel and not re.match(r'^[a-z]+:|^/',rel) and not (p.parent/rel).exists():missing.append([k,f,target])
    counts[k]={'skills':sum(f.endswith('/SKILL.md') for f in d['files'][k]),'files':len(d['files'][k])}
out={'changed_since_snapshot':changed,'missing_prose_links_primary':missing,'missing_required_frontmatter_primary':malformed,'counts':counts}
(P/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

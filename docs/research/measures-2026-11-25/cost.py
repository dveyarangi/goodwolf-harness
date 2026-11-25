# What woke each turn and what the turn cost, from the host's transcripts: cost.py <since, ISO> [<project folder>]
import json,glob,os,pathlib,collections,datetime as d,re,sys
root=(pathlib.Path.home()/'.claude'/'projects').as_posix()
since=sys.argv[1]
C=collections.Counter; cost=C(); n=C(); proj=C(); pn=C(); big=0; tot=0; comp=C(); trig_proj=C(); wake=0; wn=0
seen=set()
def kind(o):
    m=o.get('message',{}); c=m.get('content')
    t=c if isinstance(c,str) else ' '.join(b.get('text','') for b in c if isinstance(b,dict) and b.get('type')=='text') if isinstance(c,list) else ''
    if isinstance(c,list) and any(isinstance(b,dict) and b.get('type')=='tool_result' for b in c): return None
    if not t.strip(): return None
    if o.get('isMeta') and 'cross-session' not in t: return None
    if 'session is being continued' in t[:300] or o.get('isCompactSummary'): return 'compaction'
    if 'cross-session-message' in t or 'side-sessions-event' in t: return 'another session'
    if '<task-notification' in t: return 'own subagent back'
    if t.lstrip().startswith('<local-command') : return None
    return 'person'
for f in glob.glob(root+'/**/*.jsonl',recursive=True):
    if d.datetime.fromtimestamp(os.path.getmtime(f)).isoformat()<since[:10]: continue
    sub='subagents' in f.replace(chr(92),'/')
    p=f.replace(chr(92),'/')[len(root)+1:].split('/')[0]
    if len(sys.argv)>2 and p!=sys.argv[2]: continue
    k='subagent' if sub else 'person'; last=None
    for line in open(f,encoding='utf8',errors='replace'):
        try:o=json.loads(line)
        except: continue
        ts=o.get('timestamp','')
        if o.get('type')=='user' and not sub:
            kk=kind(o)
            if kk: 
                k=kk
                if ts>=since: n[k]+=1
        if o.get('type')!='assistant' : continue
        m=o['message']; u=m.get('usage'); 
        if not u or ts<since: continue
        key=m.get('id')
        if key in seen: continue
        seen.add(key)
        cc=u.get('cache_creation') or {}
        h=cc.get('ephemeral_1h_input_tokens',0); m5=cc.get('ephemeral_5m_input_tokens',0)
        w=u.get('cache_creation_input_tokens',0)
        if h+m5==0: m5=w
        r=u.get('cache_read_input_tokens',0); i=u.get('input_tokens',0); out=u.get('output_tokens',0)
        c=i+.1*r+2*h+1.25*m5+5*out
        tot+=c; cost[k]+=c; proj[p]+=c; pn[p]+=1
        comp['reread']+=.1*r; comp['write']+=2*h+1.25*m5; comp['fresh']+=i; comp['out']+=5*out
        size=r+w+i
        if size>200000: big+=.1*max(0,r-200000)
        if w>150000: wake+=c; wn+=1; trig_proj[k]+=c
print('since',since,'total M',round(tot/1e6,1))
print({k:f'{100*v/tot:.0f}%' for k,v in comp.items()}, 'reread above 200k',f'{100*big/tot:.0f}%', 'wakes >150k written',wn,f'{100*wake/tot:.0f}%')
for k,v in cost.most_common(): print(f'{k:20} {v/1e6:7.1f}M {100*v/tot:4.0f}%  triggers {n[k]}  big writes {trig_proj[k]/1e6:.1f}M')
for k,v in proj.most_common(8): print(f'{k[:50]:50} {100*v/tot:4.0f}% requests {pn[k]}')

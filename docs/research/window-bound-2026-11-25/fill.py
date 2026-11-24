import json, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
since = datetime.fromisoformat(sys.argv[1]).astimezone(timezone.utc)
root = Path.home()/".claude"/"projects"
def q(xs,p):
    xs=sorted(xs); return xs[min(len(xs)-1,int(p*len(xs)))]
tot=defaultdict(int); cnt=defaultdict(int); out_all=0; grow_all=0; rows=[]; reqs=defaultdict(list)
for f in root.rglob("*.jsonl"):
    if f.stat().st_mtime < since.timestamp() or "subagents" in str(f): continue
    proj = f.parent.name
    ev=[]; seen=set(); recall_at=None
    for line in f.open(encoding="utf-8",errors="replace"):
        try: d=json.loads(line)
        except ValueError: continue
        ts=d.get("timestamp")
        if not ts: continue
        t=datetime.fromisoformat(ts.replace("Z","+00:00"))
        ty=d.get("type")
        if ty=="system" and d.get("subtype")=="compact_boundary": ev.append((t,"compact",0))
        if ty=="system" and d.get("subtype")=="stop_hook_summary": ev.append((t,"stop",0))
        if ty=="user" and not d.get("isSidechain"):
            m=d.get("message") or {}; c=m.get("content"); o=d.get("origin")
            k=o.get("kind") if isinstance(o,dict) else None
            isres=isinstance(c,list) and any(b.get("type")=="tool_result" for b in c if isinstance(b,dict))
            if not isres and not (d.get("isMeta") and k is None) and not d.get("isCompactSummary"):
                ev.append((t,"turn",k or "human"))
        if ty=="assistant":
            m=d.get("message") or {}; u=m.get("usage")
            for b in m.get("content") or []:
                if b.get("type")=="tool_use" and b.get("name")=="Skill" and "recall" in json.dumps(b.get("input")): ev.append((t,"recall",0))
            if u and m.get("id") not in seen:
                seen.add(m.get("id"))
                ev.append((t,"ctx",((u.get("cache_read_input_tokens") or 0)+(u.get("cache_creation_input_tokens") or 0)+(u.get("input_tokens") or 0),u.get("output_tokens") or 0)))
    ev.sort(key=lambda e:e[0])
    if not ev: continue
    ctxs=[v[0] for t,w,v in ev if w=="ctx"]
    if not ctxs: continue
    prev=None; kind="human"; n=0; first=ctxs[0]; firstturn=None; msgs_at={}; nmsgs=0; compacted=False; recall=False; turns=0; reqn=0
    for t,w,v in ev:
        if w=="turn":
            if kind and turns and not firstturn and prev: firstturn=(prev,reqn)
            kind=v; turns+=1
            if v=="human": nmsgs+=1
            if t>=since: cnt[v]+=1
        elif w=="recall": recall=True
        elif w=="stop" and not firstturn and prev and turns: firstturn=(prev,reqn)
        elif w=="compact": prev=None; compacted=True
        elif w=="ctx":
            c,o=v; reqn+=1
            if prev and c>prev and t>=since:
                tot[kind]+=c-prev; grow_all+=c-prev; out_all+=o
            prev=c
            if not compacted:
                for cap in (120,150,200,300,500):
                    if cap not in msgs_at and c>cap*1000: msgs_at[cap]=nmsgs
    if ev[0][0]>=since: rows.append((proj,first,firstturn,recall,msgs_at,max(ctxs),nmsgs,compacted,len(ctxs)))
print("growth by what the turn answered:", {k:f"{v/grow_all:.0%} ({cnt[k]} turns, {v/max(1,cnt[k])/1000:.1f}k each)" for k,v in tot.items()})
print(f"model's own output is {out_all/grow_all:.0%} of the growth")
for proj in ("D--Dev-AI-agents","all"):
    r=[x for x in rows if (proj=="all" or x[0]==proj) and x[1]>30000 and x[3]]
    if not r: continue
    print(proj,"fresh chats that ran /recall:",len(r))
    print("  first request  median",q([x[1] for x in r],.5)//1000,"k")
    ft=[x[2] for x in r if x[2]]
    print("  after the first turn: n",len(ft),"p25",q([a for a,b in ft],.25)//1000,"median",q([a for a,b in ft],.5)//1000,"p75",q([a for a,b in ft],.75)//1000)
    for cap in (120,150,200,300,500):
        a=[x[4].get(cap) for x in r]; hit=[y for y in a if y is not None]
        print(f"  pass {cap}k: {len(hit)}/{len(r)}; person's messages by then: median {q(hit,.5) if hit else '-'} p25 {q(hit,.25) if hit else '-'} p75 {q(hit,.75) if hit else '-'}")
    print("  max reached: p25",q([x[5] for x in r],.25)//1000,"median",q([x[5] for x in r],.5)//1000,"p75",q([x[5] for x in r],.75)//1000,"; person messages median",q([x[6] for x in r],.5))
    for x in sorted(r,key=lambda x:-x[1])[:40]:
        print("   ",x[0][-28:],f"first={x[1]//1000} turn1={x[2][0]//1000 if x[2] else '-'}({x[2][1] if x[2] else '-'} req) max={x[5]//1000} msgs={x[6]} comp={x[7]} at200={x[4].get(200)}") if proj=="all" else None

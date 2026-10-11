"""What an agent read, by kind: code, the project's records, the method's own files.

Reads Claude Code transcripts; for each Read / Grep / Glob / Bash tool call, the size of its
result, classed by the path it touched. Prints chars and tokens (chars / 4) per kind, per typed
turn, and the shares.
"""
import json, sys, glob, os, re
from collections import defaultdict

CODE_EXT = {'.py', '.ts', '.tsx', '.js', '.jsx', '.css', '.scss', '.html', '.go', '.rs', '.java',
            '.sql', '.sh', '.ps1', '.toml', '.yaml', '.yml', '.json', '.ipynb', '.c', '.cpp', '.h'}


def kind_of_path(p):
    p = p.replace('\\', '/').lower()
    if '/.agents/' in p or '/.claude/' in p or p.endswith('/agents.md') or p.endswith('/claude.md') \
            or '/.cursor/' in p or '/.codex/' in p:
        return 'method'
    if '/docs/' in p or p.endswith('.md'):
        return 'records'
    ext = os.path.splitext(p)[1]
    if ext in CODE_EXT:
        return 'code'
    return 'other'


def kind_of_call(name, inp):
    if name == 'Read':
        return kind_of_path(inp.get('file_path', ''))
    if name in ('Grep', 'Glob'):
        path = inp.get('path', '') or ''
        g = (inp.get('glob', '') or '') + ' ' + (inp.get('pattern', '') or '')
        if 'docs' in path or '.md' in g:
            return 'records'
        if '.agents' in path or '.claude' in path:
            return 'method'
        return 'code'
    if name in ('Bash', 'PowerShell'):
        c = inp.get('command', '')
        if re.search(r'\b(cat|head|tail|sed -n|grep|rg|less|type|Get-Content)\b', c):
            if re.search(r'questions\.py|tickets\.py|\.agents|\.claude|AGENTS\.md', c):
                return 'method'
            if re.search(r'docs/|\.md\b', c):
                return 'records'
            return 'code'
        if re.search(r'questions\.py|tickets\.py|maintain\.py', c):
            return 'method'
        return None  # tests, git, builds: not a read
    return None


def size_of(content):
    if isinstance(content, str):
        return len(content)
    if isinstance(content, list):
        return sum(len(x.get('text', '')) for x in content if isinstance(x, dict))
    return 0


def main(tdir, since=None, until=None):
    pending = {}
    tot = defaultdict(int)
    turns = 0
    for f in glob.glob(os.path.join(tdir, '*.jsonl')):
        for line in open(f, encoding='utf-8', errors='replace'):
            try:
                e = json.loads(line)
            except Exception:
                continue
            ts = e.get('timestamp', '')
            if since and ts and ts < since:
                continue
            if until and ts and ts > until:
                continue
            m = e.get('message') or {}
            c = m.get('content')
            if e.get('type') == 'user' and isinstance(c, str) and not c.startswith('<'):
                turns += 1
            if not isinstance(c, list):
                continue
            for b in c:
                if not isinstance(b, dict):
                    continue
                if b.get('type') == 'tool_use':
                    k = kind_of_call(b.get('name'), b.get('input') or {})
                    if k:
                        pending[b.get('id')] = k
                elif b.get('type') == 'tool_result':
                    k = pending.pop(b.get('tool_use_id'), None)
                    if k:
                        tot[k] += size_of(b.get('content'))
                elif b.get('type') == 'text' and e.get('type') == 'user' and not b.get('text', '').startswith('<'):
                    turns += 1
    s = sum(tot.values()) or 1
    print(f'{tdir}  typed turns {turns}')
    for k in ('code', 'records', 'method', 'other'):
        t = tot[k] // 4
        print(f'  {k:8} {t:>11,} tok  {100 * tot[k] / s:5.1f}%  per turn {t // max(turns, 1):>7,}')


if __name__ == '__main__':
    main(*sys.argv[1:])

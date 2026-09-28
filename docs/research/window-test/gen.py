"""Build synthetic question stores, render them four ways, and mint trials with ground truth.

Stores: 100 (a connected subtree), 1000 (the taxonomy plus one variant copy, trimmed),
10000 and 30000 (K product-line copies of the taxonomy, titles tagged per copy).
Renderings: flat (id | parent | state | title), tree (indented), paths (directory-like),
window (path + frontier + root's open titles + other roots + recents, from a current id).
Tasks: place_near, place_far (hidden node's parent), path (ancestors), children (open kids).
"""
import json, random, os, sys, collections

random.seed(7)
OUT = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(OUT, 'taxonomy.json'), encoding='utf-8'))

TAGS = ['Titan', 'Aurora', 'Kestrel', 'Basalt', 'Meridian', 'Sable', 'Onyx', 'Halcyon', 'Vesper',
        'Corvid', 'Lumen', 'Tessera', 'Argent', 'Boreal', 'Cinder', 'Delta', 'Ember', 'Fathom',
        'Gale', 'Harbor', 'Isle', 'Juniper', 'Kite', 'Lattice', 'Mantle', 'Nadir', 'Orbit',
        'Pillar', 'Quarry', 'Rook', 'Summit', 'Tarn', 'Umber', 'Vale', 'Wren', 'Xenon', 'Yarrow',
        'Zephyr', 'Atlas', 'Brine']


def copy_tree(nodes, k):
    """K tagged copies with fresh ids; each copy is a product line (its own 9 roots)."""
    out, nid = [], 1
    for c in range(k):
        m = {}
        for n in nodes:
            m[n['id']] = f'q{nid}'; nid += 1
        tag = TAGS[c]
        for n in nodes:
            out.append({'id': m[n['id']], 'title': f"{n['title']} [{tag}]",
                        'parent': m[n['parent']] if n['parent'] else None, 'state': n['state']})
    random.shuffle(out)
    return out


def subtree(nodes, size):
    """A connected subtree of about `size` nodes under one root: a random sample of its
    descendants closed under parent, so deep chains survive."""
    ids = {n['id']: n for n in nodes}
    kids = collections.defaultdict(list)
    for n in nodes:
        kids[n['parent']].append(n['id'])
    roots = sorted((n['id'] for n in nodes if not n['parent']),
                   key=lambda r: -len(desc_ids(kids, r)))[:2]
    pool = [i for r in roots for i in desc_ids(kids, r)]
    deep = [i for i in pool if depth_of(ids, i) >= 5]
    chosen = set(deep) | set(random.sample(pool, min(len(pool), size - len(deep) - 10)))
    keep = set(roots)
    for i in chosen:
        while i:
            keep.add(i); i = ids[i]['parent']
    return [dict(ids[i]) for i in keep]


def desc_ids(kids, i):
    out, st = [], list(kids[i])
    while st:
        x = st.pop(); out.append(x); st.extend(kids[x])
    return out


def depth_of(ids, i):
    d = 1
    while ids[i]['parent']:
        i = ids[i]['parent']; d += 1
    return d


def build_store(size):
    if size == 100:
        return subtree(base, 100)
    if size == 1000:
        two = copy_tree(base, 2)
        return subtree_trim(two, 1000)
    k = size // len(base) + 1
    return subtree_trim(copy_tree(base, k), size)


def subtree_trim(nodes, size):
    """Drop random shallow leaves until `size`; nodes at depth 5 or more are protected."""
    ids = {n['id']: dict(n) for n in nodes}
    kids = collections.defaultdict(set)
    for n in nodes:
        kids[n['parent']].add(n['id'])
    while len(ids) > size:
        leaves = [i for i in ids if not kids[i] and depth_of(ids, i) < 5]
        x = random.choice(leaves)
        kids[ids[x]['parent']].discard(x); del ids[x]
    return list(ids.values())


class Store:
    def __init__(self, nodes):
        self.nodes = {n['id']: n for n in nodes}
        self.kids = collections.defaultdict(list)
        for n in nodes:
            self.kids[n['parent']].append(n['id'])
        for k in self.kids:
            self.kids[k].sort(key=lambda i: int(i[1:]))
    def path(self, i):
        p = []
        while i:
            p.append(i); i = self.nodes[i]['parent']
        return p[::-1]
    def root(self, i): return self.path(i)[0]
    def roots(self): return self.kids[None]
    def depth(self, i): return len(self.path(i))
    def desc(self, i):
        out, st = [], list(self.kids[i])
        while st:
            x = st.pop(); out.append(x); st.extend(self.kids[x])
        return out
    def line(self, i):
        n = self.nodes[i]
        return f"{i} | parent {n['parent'] or '-'} | {n['state']} | {n['title']}"


def render_flat(s, exclude=()):
    ids = sorted((i for i in s.nodes if i not in exclude), key=lambda i: int(i[1:]))
    return '\n'.join(s.line(i) for i in ids) + '\n'


def render_tree(s, exclude=()):
    out = []
    def walk(i, d):
        if i in exclude: return
        n = s.nodes[i]
        out.append('  ' * d + f"{i} [{n['state']}] {n['title']}")
        for k in s.kids[i]: walk(k, d + 1)
    for r in s.roots(): walk(r, 0)
    return '\n'.join(out) + '\n'


def render_paths(s, exclude=()):
    out = []
    for i in sorted(s.nodes, key=lambda i: int(i[1:])):
        if i in exclude: continue
        n = s.nodes[i]
        out.append('/'.join(s.path(i)) + f"  [{n['state']}] {n['title']}")
    return '\n'.join(out) + '\n'


def render_window(s, current, exclude=(), recents=()):
    p = s.path(current)
    out = [f'current: {current}', '', 'path (root to current):']
    for i in p:
        n = s.nodes[i]
        out.append(f"  {'  ' * (p.index(i))}{i} [{n['state']}] {n['title']}" + ('  <- current' if i == current else ''))
    out += ['', 'frontier (open children of each question on the path):']
    for i in p:
        for k in s.kids[i]:
            if k in exclude: continue
            n = s.nodes[k]
            if n['state'] == 'open' and k not in p:
                out.append(f"  under {i}: {k} [{n['state']}] {n['title']}")
    out += ['', f'open questions under this root ({p[0]}), with their parent:']
    for k in sorted(s.desc(p[0]), key=lambda i: int(i[1:])):
        if k in exclude: continue
        n = s.nodes[k]
        if n['state'] == 'open':
            out.append(f"  {k} (parent {n['parent']}) {n['title']}")
    out += ['', 'other roots:']
    for r in s.roots():
        if r != p[0]:
            out.append(f"  {r} [{s.nodes[r]['state']}] {s.nodes[r]['title']}")
    out += ['', 'recently attached: ' + ', '.join(recents), '']
    return '\n'.join(out)


TASKS = {
 'place_near': "A new question has arrived: \"{title}\". Decide where it belongs in the store: give the id of the existing question it is a sub-question of (its parent). If it belongs under no existing question, answer \"new-root\".",
 'place_far':  "A new question has arrived: \"{title}\". Decide where it belongs in the store: give the id of the existing question it is a sub-question of (its parent). If it belongs under no existing question, answer \"new-root\".",
 'path':       "List the ancestors of question {target}, from the root down to {target} itself, as an ordered list of ids.",
 'children':   "List the ids of the OPEN direct children of question {target}.",
}


def mint(s, size, task, r, k):
    """One trial: returns (prompt-fragment dict, truth, exclude, current)."""
    ids = list(s.nodes)
    if task in ('place_near', 'place_far'):
        cand = [i for i in ids if s.depth(i) >= 3 and s.kids[s.nodes[i]['parent']] and len(s.kids[s.nodes[i]['parent']]) >= 2]
        h = random.choice(cand)
        par = s.nodes[h]['parent']
        sib = [x for x in s.kids[par] if x != h]
        if task == 'place_near':
            cur = random.choice(sib)
        else:
            others = [i for i in ids if s.root(i) != s.root(h) and s.depth(i) >= 2]
            cur = random.choice(others)
        recents = [cur] + random.sample([x for x in s.path(cur) if x != cur] or [cur], 1)
        return ({'title': s.nodes[h]['title']}, {'answer': par, 'near': [s.nodes[par]['parent']] + sib, 'hidden': h}, (h,), cur, recents)
    if task == 'path':
        t = random.choice([i for i in ids if s.depth(i) >= 4])
        return ({'target': t}, {'answer': s.path(t)}, (), t, [t])
    if task == 'children':
        t = random.choice([i for i in ids if sum(1 for x in s.kids[i] if s.nodes[x]['state'] == 'open') >= 3])
        return ({'target': t}, {'answer': [x for x in s.kids[t] if s.nodes[x]['state'] == 'open']}, (), t, [t])


PLAN = {  # size -> rendering -> tasks -> trials
 100:   {r: {t: 2 for t in TASKS} for r in ('flat', 'tree', 'paths', 'window')},
 1000:  {r: {t: 2 for t in TASKS} for r in ('flat', 'tree', 'paths', 'window')},
 10000: {'flat': {'place_near': 1, 'path': 1}, 'tree': {'place_near': 1, 'path': 1},
         'paths': {'place_near': 1, 'path': 1}, 'window': {t: 1 for t in TASKS}},
 30000: {'flat': {'place_near': 1}, 'window': {t: 2 for t in TASKS}},
}

trials = []
for size, plan in PLAN.items():
    nodes = build_store(size)
    s = Store(nodes)
    d = os.path.join(OUT, f'store{size}'); os.makedirs(d, exist_ok=True)
    json.dump(nodes, open(os.path.join(d, 'store.json'), 'w', encoding='utf-8'))
    n = 0
    for rend, tasks in plan.items():
        for task, count in tasks.items():
            for k in range(count):
                frag, truth, excl, cur, recents = mint(s, size, task, rend, k)
                n += 1
                fn = os.path.join(d, f'{rend}-{task}-{k}.txt')
                if rend == 'flat': txt = render_flat(s, excl)
                elif rend == 'tree': txt = render_tree(s, excl)
                elif rend == 'paths': txt = render_paths(s, excl)
                else: txt = render_window(s, cur, excl, recents)
                open(fn, 'w', encoding='utf-8').write(txt)
                trials.append({'size': size, 'rendering': rend, 'task': task, 'k': k, 'file': fn,
                               'lines': txt.count('\n'), 'chars': len(txt),
                               'question': TASKS[task].format(**frag), 'current': cur, 'truth': truth})
json.dump(trials, open(os.path.join(OUT, 'trials.json'), 'w', encoding='utf-8'), indent=1)
print(len(trials), 'trials')
for size in PLAN:
    st = json.load(open(os.path.join(OUT, f'store{size}', 'store.json')))
    print(size, 'nodes', len(st), 'roots', sum(1 for x in st if not x['parent']))
for t in trials:
    if t['k'] == 0 and t['task'] == 'place_near':
        print(t['size'], t['rendering'], t['lines'], 'lines', t['chars'] // 4, '~tokens')

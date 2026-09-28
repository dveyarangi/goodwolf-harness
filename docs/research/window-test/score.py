"""Score answers/<tag>.txt against trials.json; print a table rendering x size x task."""
import json, os, re, collections

OUT = os.path.dirname(os.path.abspath(__file__))
trials = json.load(open(os.path.join(OUT, 'trials.json'), encoding='utf-8'))
stores = {}


def store(size):
    if size not in stores:
        nodes = json.load(open(os.path.join(OUT, f'store{size}', 'store.json'), encoding='utf-8'))
        stores[size] = {n['id']: n for n in nodes}
    return stores[size]


def root_of(size, i):
    s = store(size)
    while s[i]['parent']:
        i = s[i]['parent']
    return i


def parse(path):
    if not os.path.exists(path):
        return None
    txt = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'ANSWER:\s*(.*)', txt)
    if not m:
        return []
    body = m.group(1)
    incomplete = '(incomplete' in body
    body = body.split('(')[0]
    ids = [x.strip().strip('`"\'') for x in re.split(r'[,\s]+', body) if x.strip()]
    return ids + (['*incomplete*'] if incomplete else [])


rows = []
for t in trials:
    got = parse(os.path.join(OUT, 'answers', t['tag'] + '.txt'))
    truth = t['truth']['answer']
    incomplete = bool(got) and got[-1] == '*incomplete*'
    if incomplete:
        got = got[:-1]
    if got is None:
        verdict = 'missing'
    elif t['task'] in ('place_near', 'place_far'):
        g = got[0] if got else ''
        if g == truth:
            verdict = 'exact'
        elif t['rendering'] == 'window' and t['task'] == 'place_far' and g == root_of(t['size'], truth):
            verdict = 'root'      # the correct first-turn landing under the window
        elif g in t['truth']['near']:
            verdict = 'near'      # grandparent or sibling of the true parent
        else:
            verdict = 'wrong'
    elif t['task'] == 'path':
        verdict = 'exact' if got == truth else 'wrong'
    else:
        gs, ts = set(got), set(truth)
        if gs == ts:
            verdict = 'exact'
        else:
            verdict = 'partial' if gs & ts else 'wrong'
    if incomplete:
        verdict += '†'   # the reader said it did not finish the file
    rows.append((t['size'], t['rendering'], t['task'], t['k'], verdict, got, truth))

cell = collections.defaultdict(list)
for size, rend, task, k, v, got, truth in rows:
    cell[(size, rend, task)].append(v)

sizes = sorted({r[0] for r in rows})
rends = ['flat', 'tree', 'paths', 'window']
tasks = ['place_near', 'place_far', 'path', 'children']
print('| size | rendering | ' + ' | '.join(tasks) + ' |')
print('|---|---|' + '---|' * len(tasks))
for size in sizes:
    for rend in rends:
        if not any((size, rend, t) in cell for t in tasks):
            continue
        cells = []
        for task in tasks:
            vs = cell.get((size, rend, task))
            cells.append(' '.join(vs) if vs else '—')
        print(f'| {size} | {rend} | ' + ' | '.join(cells) + ' |')

print()
for size, rend, task, k, v, got, truth in rows:
    if v not in ('exact',):
        print(f'{size}-{rend}-{task}-{k}: {v}  got {got}  truth {truth}')

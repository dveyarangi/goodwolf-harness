// Research probes of Life's existing code. Writes only beneath a new temporary fixture.
// No live hooks, installers, suite, network calls, or Life record writers are invoked.
const fs = require('fs');
const os = require('os');
const path = require('path');
const cp = require('child_process');
const assert = require('assert/strict');
const crypto = require('crypto');
const life = 'D:/Dev/AI/life';
const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'dev-harness-life-probe-'));
const results = [];
const sourcePaths = [
  '.agents/scripts/inject-rules.js', '.agents/lib/injected-blocks.js',
  '.agents/lib/mechanism-state.js', '.agents/lib/maintenance-marks.js',
  '.claude/hooks/rules-loaded.js', '.claude/hooks/skills-reachable.js'
];
const hashes = () => Object.fromEntries(sourcePaths.map(p => [p,
  crypto.createHash('sha256').update(fs.readFileSync(path.join(life, p))).digest('hex')]));
const before = hashes();
const write = (root, rel, text) => {
  const p = path.join(root, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, text);
};
const read = (root, rel) => fs.readFileSync(path.join(root, rel), 'utf8');
function fixture(name, ruleTargets = ['a.md']) {
  const root = path.join(scratch, name);
  write(root, 'mechanisms/probe/probe.doc.md', '# Probe\n- **State:** `paused`\n');
  write(root, 'mechanisms/probe/probe.rules.md', ruleTargets.map((target, i) =>
    '## rule' + i + '\n- **target:** `' + target + '`\n```anchor\nANCHOR\n```\n```rule\nShared v1.\n```\n'
  ).join('\n'));
  write(root, 'a.md', '# A\nANCHOR\nLocal text stays here.\n');
  return root;
}
const inject = (root, ...args) => {
  const r = cp.spawnSync(process.execPath, [path.join(life, '.agents/scripts/inject-rules.js'),
    'probe', ...args, '--root=' + root], { encoding: 'utf8', windowsHide: true });
  if (r.error) throw r.error;
  return { code: r.status, stdout: r.stdout.trim(), stderr: r.stderr.trim() };
};
function probe(name, fn) { results.push({ name, ...fn() }); }
probe('check on an absent install returns zero and explicitly reports absence', () => {
  const root = fixture('absent');
  const initial = read(root, 'a.md');
  const r = inject(root, '--check');
  assert.equal(r.code, 0); assert.match(r.stdout, /absent, would install/);
  assert.equal(read(root, 'a.md'), initial);
  return r;
});
probe('install and pause roundtrip preserves unrelated text; repeat install is idempotent', () => {
  const root = fixture('roundtrip'); const initial = read(root, 'a.md');
  assert.equal(inject(root, '--install').code, 0);
  const installed = read(root, 'a.md');
  assert.equal(inject(root, '--install').code, 0); assert.equal(read(root, 'a.md'), installed);
  assert.equal(inject(root, '--pause').code, 0); assert.equal(read(root, 'a.md'), initial);
  return { verified: true };
});
probe('later refusal leaves an earlier target modified and returns nonzero', () => {
  const root = fixture('partial', ['a.md', 'missing.md']); const initial = read(root, 'a.md');
  const r = inject(root, '--install');
  assert.equal(r.code, 1); assert.notEqual(read(root, 'a.md'), initial);
  assert.match(read(root, 'mechanisms/probe/probe.doc.md'), /paused/);
  return { ...r, earlierTargetChanged: true, declaredState: 'paused' };
});
probe('both source changes and target changes refuse without explicit overwrite', () => {
  const root = fixture('drift'); assert.equal(inject(root, '--install').code, 0);
  const rules = read(root, 'mechanisms/probe/probe.rules.md');
  write(root, 'mechanisms/probe/probe.rules.md', rules.replace('Shared v1.', 'Shared v2.'));
  const sourceChanged = inject(root, '--install'); assert.equal(sourceChanged.code, 1);
  write(root, 'mechanisms/probe/probe.rules.md', rules);
  write(root, 'a.md', read(root, 'a.md').replace('Shared v1.', 'Shared local change.'));
  const targetChanged = inject(root, '--install'); assert.equal(targetChanged.code, 1);
  return { sourceChanged, targetChanged };
});
probe('rules-loaded can return quiet with disk text alone and no context input', () => {
  const root = fixture('rules');
  const text = '**Withdrawn 2026-09-02**\nnever expose the citizen secret\nnever mint an identity\n' +
    'reclassify a ticket from HITL to AFK\nnothing about the operator leaves\ncore reads only what core owns\n' +
    'write for a capable reader\n## Meta-rules\n' +
    Array.from({length: 9}, (_, i) => (i + 1) + '. **Synthetic rule**').join('\n');
  write(root, 'CLAUDE.md', text);
  const mod = require(path.join(life, '.claude/hooks/rules-loaded.js'));
  const valid = mod.announce({claudeMd: path.join(root, 'CLAUDE.md')});
  assert.equal(valid.body, null);
  const missing = mod.announce({claudeMd: path.join(root, 'absent.md')});
  assert.match(missing.message, /MISSING/);
  // Module contract bypasses the standalone argv kind check. Demonstrates catch semantics,
  // not a claim that the production runner normally supplies a directory.
  const readError = mod.announce({claudeMd: root}); assert.equal(readError.body, null);
  return { validDiskNoContext: valid, missingDisk: missing.message, moduleReadError: readError };
});
probe('maintenance hashes distinguish deletion and content changes, normalize line endings', () => {
  const root = fixture('hash');
  const m = require(path.join(life, '.agents/lib/maintenance-marks.js'));
  write(root, 'surface.md', 'alpha\nbeta\n'); const lf = m.hashSurface(root, ['surface.md']);
  write(root, 'surface.md', 'alpha\r\nbeta\r\n'); const crlf = m.hashSurface(root, ['surface.md']);
  assert.equal(lf, crlf);
  write(root, 'surface.md', 'changed\n'); assert.notEqual(m.hashSurface(root, ['surface.md']), lf);
  assert.notEqual(m.hashSurface(root, ['missing.md']), m.hashSurface(root, []));
  return { verified: true, lf, crlf };
});
probe('maintenance staleness is derived read-only and persists until marked', () => {
  const root = fixture('maintenance');
  const m = require(path.join(life, '.agents/lib/maintenance-marks.js'));
  write(root, m.REGISTER_REL,
    '| M01 | probe | `mechanisms/probe/probe.doc.md` | `/probe` | `memory/probe.md` | none | none |\n');
  write(root, '.agents/skills/mechanism/SKILL.md', 'Governing v1.\n');
  write(root, '.agents/skills/probe/SKILL.md', 'Instruction.\n');
  write(root, 'memory/probe.md', 'Record.\n');
  assert.equal(m.assess(root).rows[0].marked, false);
  const own = m.mechanisms(root)[0].own;
  m.writeMarks(root, new Map([['probe rules', {key:'probe', level:'rules', maintained:'2026-09-05',
    gov:m.hashSurface(root, m.RULES_GOVERNING), self:m.hashSurface(root, own), seen:'-', churn:0}]]));
  assert.equal(m.assess(root).rows[0].reasons.length, 0);
  write(root, '.agents/skills/mechanism/SKILL.md', 'Governing v2.\n');
  const marksBefore = read(root, m.MARKS_REL);
  const a = m.assess(root), b = m.assess(root);
  assert.equal(a.rows[0].reasons[0].kind, 'governing'); assert.deepEqual(a.rows, b.rows);
  assert.equal(read(root, m.MARKS_REL), marksBefore);
  return { verified: true, reasons: a.rows[0].reasons };
});
const after = hashes(); assert.deepEqual(before, after);
console.log(JSON.stringify({date:'2026-09-05', life, scratch, scope:'isolated fixtures; not live-host delivery',
  results, inspectedSourceHashesUnchanged:true, sourceHashes:after}, null, 2));

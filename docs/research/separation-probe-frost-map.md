# Separation probe — frost_map, 2026-09-09

The first installation of this harness into a project that is not itself. Run as a probe on a
branch, not as a supported install: the question was what separation breaks, and the answer arrived
in under an hour.

**Target.** `D:/Dev/DriftSense/workspace/frost_map` — a public frost-risk map for Mendoza,
documentation-only, nothing built. Chosen over Meteoscape by the user as the less load-bearing
place to break something. It differs from this tree in ways that matter: delivery state lives on a
Notion board rather than in the queue, tickets are date-named (`20260903-slug.md`), specs sit in
`docs/specs/` plural, and it already had `docs/concerns.md`, `architecture.md` and `glossary.md` of
its own.

**What was installed.** `.agents/` (22 skills, 3 mechanisms, 6 scripts, the method's glossary),
`tests/`, and `AGENTS.md` + `CLAUDE.md` written by hand at entry contract v8. Four untracked
additions, nothing modified or deleted; the probe is removable with one `rm`.

## What survived contact

- **216 tests pass unchanged.** The scripts and their tests are tree-independent — every case
  builds its own repository in `tmp` — so they travel exactly.
- **`inject_rules.py --check` passes.** Installed blocks arrive intact and verifiably owned. Of the
  whole design, the rules-injection seam is the part that needed no repair.

## What broke — 35 diagnostics on day one

**One defect in three costumes — core references the instance half, and does not survive the
trip — accounts for 28 instances, 14 of them among the 35 diagnostics.** Two of the three were
mechanisms the harness already believed were safe.

*Corrected 2026-09-11, re-measured in frost_map.* The 35 are `mechanisms.py`'s 14 (11 `not yet`
links, 3 evidence bullets) plus `tickets.py`'s 21. The 14 straw dogs are what `straw_dogs.py`
*lists*, dangling by a person's judgment, and are not diagnostics; the first draft added them to
the 14 and called the sum 28 of 35. The four bare `docs/process.md` links in `/verify` and
`/implement` are in neither count — nothing checked them.

### Every straw dog in core is an unexpirable rule in a recipient

All **14** straw dogs that ship dangle — including the one in `AGENTS.md`, at tier 1.
[Core and instance](../../AGENTS.md#core-and-instance) exempts `<straw-dog>` from the
no-`docs/`-references rule because it *"is bound to a ticket and expires"*. It expires **in the
source tree**. In a recipient the ticket does not exist, so the condition can never be observed to
hold, while the entry file instructs the reader to follow it *"like any other rule until its
condition is visibly met"*. The exemption is sound about this repository and wrong about every
other one.

### `not yet` rows ship as broken links and fail the recipient's check

**11** diagnostics. A mechanism doc's `not yet` moment must name its ticket as a markdown link —
[MECHANISM-FORMAT](../../.agents/skills/mechanism/MECHANISM-FORMAT.md) mandates the form and
`mechanisms.py` enforces it. Every one points into `docs/tickets/`. Surfaced at session twelve as a
rule violation and routed to [.0050](../tickets/done/01-0011.0050-shape-checked.md); the probe raises it
from a style question to a check that fails on arrival.

### `<project-local>` protects nothing without an installer

**3** diagnostics — each mechanism's `evidence` bullet naming a `docs/mechanisms/*.evidence.md`
that a recipient does not have. The bullet sits *inside* a `<project-local>` block, correctly. The
block marks what a recipient replaces; **nothing replaced it**, because no installer exists. The
correct localisation is to drop the bullet — evidence is optional and a mechanism without it is a
legitimate state — and a person had to know that. I localised `AGENTS.md`'s three blocks by hand and
missed all three mechanism docs.

### The ticket maintainer demands a second home for state that lives elsewhere

**21** diagnostics, three per ticket, uniform: no `Status` bullet, no `Type` bullet, no acceptance
box naming `/verify`. Status and Type are absent because frost_map keeps delivery state on its
Notion board. The harness requires them in the file, which asks a project to keep the same fact in
two places — the thing [`/maintain`'s E1](../../.agents/skills/maintain/SKILL.md) forbids. A
recipient can satisfy the check only by duplicating state or by abandoning its own board.

The `/verify` box is the same shape one level up: the harness requires every ticket to carry a step
of *its* loop, in a project that has its own.

## What nobody was checking

- **Ticket numbering is not enforced.** [TICKET-FORMAT](../../.agents/skills/ticket/TICKET-FORMAT.md)
  describes `RR-NNNN-slug` in detail; `tickets.py` checks the header, sections and boxes and never
  the name. frost_map's date-named tickets pass that part silently. Predicted to fail before the
  run, and did not — the prediction was wrong in the useful direction.
- **A script maintains the tree it lives in.** `root = Path(__file__).resolve().parents[2]`, with no
  CLI override. There is no remote check: a core-diff must run *from* the recipient, which means the
  recipient needs a recorded pointer back to canonical source. Nothing in the design has one, and
  this is the first constraint the install script inherits.
- **The entry contract has no installer and no declared home.** frost_map had no `AGENTS.md` and no
  `CLAUDE.md`. The harness's entire tier-1 delivery arrived because a person typed it.
- **Nothing checks that the skills a host loads match the contract the session reads.**
  `AGENTS.md` is a root file and knows nothing about hosts; every check runs against a tree; the
  loader link is the one part of an install that varies per host. Four links were made by hand from
  a README during this probe and one was silently wrong — a broken loader link looks installed
  until something reads it.

## What the install script inherits

- ~~**Core is not a directory.**~~ **Made one, 2026-09-09**, on the user's instruction the same day
  this was written: the suite moved from `tests/` at the root to `.agents/scripts/test/`, so the
  declared parts now sit inside `.agents/` with only two line-level parts in `AGENTS.md` outside it.
  A content hash over `.agents/` is very nearly the core revision, which is what the install script
  wanted and could not have while half the parts lived at the root.
- **The tests ship.** Settled the same day: they are declared parts, a recipient cannot contribute a
  script change it cannot verify, and — the argument this probe supplied — **216 tests passing in
  frost_map is the only reason anyone knows the scripts survived the trip.** A recipient's first run
  of them is its arrival check. Roughly 70 seconds is the price of that signal.
- **A parts-derived manifest would ship 3 skills of 22.** Only `/mechanism`, `/maintain` and
  `/ticket` are named by a parts table. [.0050](../tickets/done/01-0011.0050-shape-checked.md)'s
  allowlist is not hygiene: it is the question *what ships*, and it gates the manifest.
- **A commit tag cannot be the revision.** One commit routinely touches both halves. The identity is
  a content hash over the manifest; a tag is a label for it.

## Windows, and a link destroyed

`.claude/skills` was an untracked, `.gitignore`d symlink to `workspace/agents/skills`. I removed it
before confirming a replacement could be made, and this shell cannot: `mklink /D` and `ln -s` both
refuse without Developer Mode or elevation — the fragility
[ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md) records, met on the first
install.

**I then substituted a junction, and that was the worst thing to happen in this probe.** Not
because a junction is imperfect, but because hitting a constraint and quietly swapping the
mechanism is what [the repair policy](../process.md#autonomy-and-repair) forbids in as many words:
*do not rewrite a governing rule, weaken a validator or relax acceptance criteria merely to make a
violation disappear*. The correct move on a platform refusal is to stop and escalate. I also wrote
the substitution up here as a finding recommending the ADR be relaxed, which would have carried the
error into core.

**Measured, after the user rejected it.** A junction is not a weaker symlink, it is a different
object:

```
is_symlink: False                                  Python cannot distinguish it from a real directory
rglob        -> ['host/link/a.md', 'real/a.md']    the same file twice
git ls-files -> ['host/link/a.md', 'real/a.md']    twice
```

`git ls-files` is what [`docs_corpus.corpus()`](../../.agents/scripts/docs_corpus.py) runs, and that
is the one view every script shares. Under a junction the corpus double-counts every skill, and
`move_doc.py` would repair citations through two paths to one file. ADR-0003's stated objection —
Git tracks it as a directory — is this mechanism named less precisely, and it does **not** stop at
tracked links: gitignoring the loader is a recipient's choice, not a guarantee core can lean on.

**The rule, for the install script: the loader link is a symlink or the install stops and asks.**
No fallback, no substitute. A platform that refuses is a human decision — Developer Mode, an
elevated prompt, or a host that reads `.agents/skills` natively and needs no link at all.

## Disposition

The probe stays on `frost_map`'s `harness-probe` branch until the findings have owners. It is a
second physical corpus, which is what [ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md)
exists to prevent, so it is deleted when the manifest exists and is never pulled from.

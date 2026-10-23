# debugging — shows a tree's own working to the person exactly while the tree's settings say so

- **instruction** `.agents/skills/debugging/SKILL.md` — what a tree shows of its own working, and where that text comes from
- **state** installed
- **record of** what must always hold

## How it works

What a reply shows of the machinery behind it — a session's announce line, the marks a paragraph
carries, the tables that open a reply — is this mechanism's text. It reaches a tree as installed
blocks, each rule conditioned `when debug=on`, and the project sets `debug` in its local file:
a tree at `off` carries none of it, and a session reads no switch to know which. One text never
holds both readings behind a switch a session reads, because a reader who must evaluate the
switch pays for both readings and can take the wrong one *(the user, 2026-10-18)*.

The setting is this mechanism's to declare — its name, its values, its default, who may set it —
and any installed mechanism's rule may use it: the session mechanism's 🪢 table is conditioned on
it and does not own it. Switching is the agent's, through `/harness`, at the rung the declaration
names.

It is **installed**. A tree without it shows nothing of its working and reads no `debug`; the
parts table below is what an installer adds and an uninstaller removes.

<straw-dog question="q-0037.0009.0021.0001">
**What is here today** is the declaration and one rule, the announce line. The rest of what shows
under `debug=on` — the reply form's marks, frames, footnotes and tables, the commits table and
the counters line, `/maintain`'s repair detail, the two scripts' lines — still stands in the entry
file and the skills as text read behind `debug=on`, and moves here rule by rule.
</straw-dog>

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| saying what a tree shows of its own working, and where that text is authored | `.agents/skills/debugging/SKILL.md` | |
| switching debugging on or off in a tree | `.agents/skills/harness/SKILL.md` | |
| installing its text into a tree under the tree's settings, and taking it out | `.agents/scripts/gw/inject_rules.py` | |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| moving the rest of what debug shows into this mechanism's rules | — | <straw-dog question="q-0037.0009.0021.0001">not yet</straw-dog> |
| removing this mechanism from a tree | — | <straw-dog question="q-0037.0006.0013.0002">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/debugging/SKILL.md` |
| this doc | `.agents/mechanisms/debugging/debugging.md` |
| its rules file | `.agents/mechanisms/debugging/debugging.rules.md` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the installer, which reads its declaration and its conditions | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the project's values, in its local file | `local.rules.md` | the project |
| the act of switching, at the person's ask | `.agents/skills/harness/SKILL.md` | `harness` |
| the heading in the entry file where its block lands | `AGENTS.md` → "## General rules" | the entry file's own |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The rules file** — *what must always hold* — read by the installer alone, for the `debug`
  declaration every condition on it resolves against, and for the block it writes into the entry
  file while the tree says `on`; read by a session only as that block, as any installed rule is.

Nothing else: it writes no record of its own.

## Not yet at the shape

**One `not yet` row of its own**, bound to its question: the rest of what debug shows, still read
behind `debug=on` in the entry file and the skills, moving here.

## What retires this

A method whose working nobody needs to see: no person steering it, no rule under amendment. While
the harness is developed by its own loop and read by people, the condition does not arrive.

## What would show it working, graded by someone who did not build it

Pre-registered 2026-10-23, one grader. **The person**, in a live session of this tree, switches
`debug` off and reads the next session's replies, then switches it on and reads again: does what
shows follow the setting, with nothing of the machinery left behind at `off` and nothing missing
at `on`? Each line that shows at `off`, or fails to at `on`, is a miss, named in the evidence.

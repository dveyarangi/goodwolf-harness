# pathfinder — chooses what the project works on next by what it is for, and keeps the order the person gives

- **instruction** `.agents/skills/pathfinder/SKILL.md` — the act: weighing the candidates, putting them to the person, keeping the roadmap; the board's drawing in `BOARD.md` beside it
- **state** installed
- **record of** what must always hold
- **owner** core

## How it works

What comes next is derived, never written as a list of work. The candidates are the question
store's reading of the path; their order is the **roadmap**'s — the order the person gives the
product document's answers and pains, each row in their words and dated. A piece of work takes the place of
the answer or the pain it serves. A proxy such as how much stays unfinished orders nothing *(the user,
2026-10-25)*.

The mechanism weighs questions, never the method's records: a unit of work is whatever the
installed method materialises a question into, so it works in a tree with no method installed.

The skill was written from the person's corrections over the session that built it — the first
case of a session writing the method of its own work. A standing session holding the path's role
keeps the roadmap where a tree has standing sessions; elsewhere whoever orders the work does.

It is **installed**. It ships with core like every mechanism. The roadmap is written when the
person first orders the work; a tree with none has no order yet.

**Who decided each rule.**

| rule | decided by |
|---|---|
| the path is ordered by the product roadmap, not by how much stays unfinished | the user, 2026-10-25 |
| no written queue: what comes next is a reading | the user, 2026-10-25 |
| the roadmap is a record of its own | the user, 2026-11-21 |
| the method's records do not cross a mechanism that works without it | the user, 2026-10-25 |
| the skill's rules, drawn from the person's corrections | the user, 2026-11-21 |
| the mechanism declared | the user, 2026-11-21 |
| `owner core` | settled by the session that declared it, 2026-11-21, the user not asked then; the user, 2026-11-24 |
| candidates weighed by how they lead toward the product's answers | the user's idea, 2026-11-22; the text the agent's, agreed |
| a question waiting on the person that no work under way holds is a candidate | the user's words to another session, 2026-11-22; the text the agent's, landed on them |
| such a question goes first to the session it belongs to | the user's words to another session, 2026-11-24; the text the agent's, landed on them |
| a hazard is put before the candidates, its reach counted in the code | the agent's text, landed on the user's word, 2026-11-25 |
| a hazard is an open question that asks the person, not a unit of work of its own | the user, 2026-11-25, after a unit of work by their word of the same day; the text the agent's, accepted |
| a roadmap row may name a pain | the agent's text, agreed by the user, 2026-11-25 |
| a hazard set aside keeps asking or is deferred until the person's condition | the agent's text, accepted by the user, 2026-11-25 |
| the strip of hazards only on the board of the session that took them | the user, 2026-11-25; the text the agent's |
| the board's cards derived, no list of them kept | the user, 2026-11-25; the text the agent's, accepted |
| the work drawn as a board, its rules | the user asked for the drawing and took it for now, 2026-11-25; the text the agent's, accepted |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| recommending what comes next, and the person ordering the work | `.agents/skills/pathfinder/SKILL.md` | |
| an idea arriving that would change what comes next | `.agents/skills/pathfinder/SKILL.md` | |
| making or amending the roadmap | `.agents/skills/pathfinder/SKILL.md` | |
| drawing the work for the person | `.agents/skills/pathfinder/BOARD.md` | |
| adding or removing a part that orders the work | `.agents/skills/pathfinder/SKILL.md` | |
| showing the path at a wake | — | elsewhere — the wake is the session mechanism's, `.agents/skills/recall/SKILL.md` |
| the path printing the roadmap's rows before its candidates | — | <straw-dog question="q-huss2x">elsewhere — `questions.py`, until this mechanism draws the path itself</straw-dog> |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| removing this mechanism from a tree | — | <straw-dog question="q-qzeuf3">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/pathfinder/SKILL.md` |
| the board's rules | `.agents/skills/pathfinder/BOARD.md` |
| this doc | `.agents/mechanisms/pathfinder/pathfinder.md` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the path, the store's reading of the candidates, and the mark of a question that asks the person | `.agents/scripts/gw/questions.py` | `questions` |
| the product document's answers and pains the roadmap orders | `.agents/skills/product/SKILL.md` | `product` |
| the running sessions the board reads, what each holds and where it stands | `.agents/scripts/gw/sessions.py` | `session` |
| the wake that shows the path and what asks the person | `.agents/skills/recall/SKILL.md` | `session` |
| the installer, which writes the voice into its skill | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The roadmap** — *what it intends to become* — read by whoever recommends what comes next,
  and by the person ordering the work.
- <straw-dog question="q-p7qw6i">**The board** — *what exists* — drawn for the person who asks to see
  the work or after an order changed, read by them; kept nowhere, drawn anew from the records each
  time.</straw-dog>

Nothing else kept: no rules file, no index.

## Not yet at the shape

**One `not yet` row**: removal, bound to the harness's removal question. <straw-dog question="q-huss2x">The
path is drawn by the question store's script, not by this mechanism.</straw-dog>

## What retires this

A project whose work needs no choosing: one thread, one person, nothing waiting.

## What would show it working, graded by someone who did not build it

Pre-registered 2026-11-21. **The person**, at the first wake after the roadmap holds rows, reads
the recommended next work: does it follow the roadmap's order, with every candidate shown and
what each would give them, and not the most unfinished or the last thing said? Each
recommendation that does not is a miss, named in the evidence.

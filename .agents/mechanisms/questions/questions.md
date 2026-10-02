# questions — every open question of the tree is kept in one store, with each session's current question known

- **instruction** `.agents/skills/questions/SKILL.md` — the formats, the declared line, and closing, branching and dropping
- **state** installed

## How it works

A discussion opens a question, splits it, dives into one branch and moves on; what was left open
above is carried in nobody's record. The store writes every open question down with its relations
and its state, and every running session's current question beside them, so a question left behind
is found again and an answer landed above an unexpanded shape is caught.

**The unit is the open question.** One entry per question, with two relations kept apart — *part
of*, a decomposition, and *depends on*, cannot be asked until — and a closure by recorded kind.
Level is depth in that structure, derived and never written; a shift in a conversation is a message
attaching to a different question. A ticket is a method's goal and stays the method's; the store is
core's substrate, beneath whatever method a tree runs.

**The turn.** Before drafting, the agent reads the window — the path from the root to its session's
current question, the children along it, the root's other open questions, the other roots, the
other sessions, the next free id — and declares where the message lands, as one line the script
parses and writes. The window prints position, never relevance: the one judgement of the turn is
the agent's. The rule placing a message is installed at tier 1, since its occasion is every turn.

**Delivery.** Where a host's hooks can add context, the window and the session's registration come
from them, under the host's own session id; the rule stays the floor every host reads. Claude Code
and Codex take context at session start and before every message; Cursor only at session start, so
its agent draws the window by the rule. A window stays in the conversation once drawn, so the next
is drawn only when the session's position or an entry moved, and whole again after a compaction.

**Principles**, behind the rules and never installed:

- Depth is the instrument against breadth: when a question's open children outgrow what the window
  can show, find the question they jointly serve and insert it above them.
- A skipped question is found by impasse or by the method's plan, never by walking presuppositions
  upward.
- Decide at the level asked; go down to look, and return.
- Descend or hold is a value question: resolve the higher question first only when its answer could
  flip this one and is cheaper to get than the flip would cost; otherwise decide under it, record
  the dependency, and the answer is born suspect.
- The same question means the same answers, never the same wording.
- A question is held when answering it is worth its cost, when someone can say what one might have
  thought instead, and when a clairvoyant could answer it without judgement.

**Three levels**, each usable without the next: the store, where the agent judges and nobody watches
it; a judge outside the generator, which catches the agent's own descents; the hook, after which
nothing is left to remember. The window's half of the hook lands with the store; the write after
the turn waits on the judge.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| placing a message before answering it | `AGENTS.md` | |
| closing, branching or dropping a question | `.agents/skills/questions/SKILL.md` | |
| re-parenting, merging or pruning by hand | `.agents/skills/questions/SKILL.md` | |
| drawing the window | `.agents/scripts/gw/questions.py` | |
| registering a session and delivering its window through a host's hook | `.agents/scripts/gw/questions.py` | |
| writing entries and the position from a declared line | `.agents/scripts/gw/questions.py` | |
| checking the store | `.agents/scripts/gw/questions.py` | |
| reading where the work stands when a session wakes | `.agents/skills/recall/SKILL.md` | |
| writing the session's leans and ending it | `.agents/skills/conclude/SKILL.md` | |
| archiving a wholly closed subtree | `.agents/skills/maintain/SKILL.md` | |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| judging a message outside the agent | — | <straw-dog until="the judge slice lands" ticket="docs/tickets/01-0011.0100.0040-the-turn-is-steered-from-the-store.md">not yet</straw-dog> |
| detecting a shape that hides children | — | <straw-dog until="the branch slice lands" ticket="docs/tickets/01-0011.0100.0050-a-question-branches-before-it-is-answered.md">not yet</straw-dog> |
| holding the tickets' open issues as entries | — | <straw-dog until="the open-issues slice lands" ticket="docs/tickets/01-0011.0100.0020-open-issues-are-entries-of-the-store.md">not yet</straw-dog> |
| holding the straw dogs as entries | — | <straw-dog until="the straw-dog slice lands" ticket="docs/tickets/01-0011.0100.0030-straw-dogs-are-entries-of-the-store.md">not yet</straw-dog> |
| carrying the hook wiring into a recipient tree | — | <straw-dog until="the installer carries each host's hook wiring" ticket="docs/tickets/01-0010-dev-harness-shared-and-local.md">not yet</straw-dog> |
| removing this mechanism from a tree | — | <straw-dog until="the parts table says what goes and something says how" ticket="docs/tickets/01-0010-dev-harness-shared-and-local.md">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/questions/SKILL.md` |
| this doc | `.agents/mechanisms/questions/questions.md` |
| its rules file | `.agents/mechanisms/questions/questions.rules.md` |
| the store's script | `.agents/scripts/gw/questions.py` |
| its tests | `.agents/scripts/gw/test/test_questions.py` |
| Claude Code's hook wiring | `.claude/settings.json` → "--hook claude-code" |
| Codex's hook wiring | `.codex/hooks.json` → "--hook codex" |
| Cursor's hook wiring | `.cursor/hooks.json` → "--hook cursor" |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the mover | `.agents/scripts/gw/move_doc.py` | `ticket` |
| citation reader | `.agents/scripts/gw/docs_corpus.py` | `mechanism-shape` |
| test harness | `.agents/scripts/gw/test/repository.py` | `mechanism-shape` |
| the shape check | `.agents/scripts/gw/mechanisms.py` | `mechanism-shape` |
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The entries** — read by the script at every window, wake, declaration and check, and by a
  person through `--tree`.
- **The sessions file** — read by the script for every window and wake, so each session sees where
  the others stand.
- **The window** — read by the agent before every message, from the host's hook or the rule.
- **The wake's read** — read by the agent at session start, from the hook or `/recall`.
- **The fingerprint of each session's last window**, outside the tree — read by the script alone,
  to tell whether anything moved; a compaction clears it.
- **The hook's answers** — read by the host, which places them in the agent's context.
- **The check's report** — read by `/maintain` at its pass and by `/verify` through the
  verification set.
- **The rules file** — read by the installer alone.

Nothing else; the tree is rendered on request and never committed.

## Not yet at the shape

**Six `not yet` rows**, each bound to a ticket that exists. **The sessions file** is a straw dog in
the skill: one file in the working tree is how sessions see each other until it is known how
registrations reach sessions that do not share the directory. **The store's paths** are painted
doors held by hand in the shape check until a mechanism's records are declared where a script
reads them.

## What retires this

If it works, nothing: it is the core other things are built on. Two conditions would show that it
does not work as a substrate. A host that comes to keep a conversation's question structure itself
— position, tree, and the moments with the same outputs — in which case the store is the host's.
Or its own measure: over a stated span, the declared lines and suspect marks led to no amendment
the session would not have made anyway, counted as judged shifts, suspect marks cleared and
reopenings refused against the turns and tokens spent declaring — it costs and does not save. The
store becoming the ticketing is not a retirement.

## What would show it working, graded by someone who did not build it

Three yes-or-no tests, pre-registered at the align that incepted it:

1. Drift deliberately in a chat: does the declared line name the shift in the same turn?
2. Break a session at a deep question: does the next wake open at it, with its path?
3. Change a parent's answer: is every child under it reported suspect before anyone reads them?

The third is what the mechanism was raised for. And per host, recorded as observed or not: does a
live session register under the host's own id through its hook, and, in Claude Code and Codex, is
the window in context before the agent drafts, with no call of its own?

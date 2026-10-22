# session — a chat is one session, known from its wake to its conclude and for a while after

- **instruction** `.agents/skills/recall/SKILL.md` — the wake: where the work stands when a session starts
- **instruction** `.agents/skills/conclude/SKILL.md` — the conclude: the session record, the leans, the row ended
- **state** installed
- **record of** what must always hold

## How it works

A session is one chat of a host with the tree, from its `/recall` to its `/conclude`, known by the
steadiest id the host gives the chat — the desktop app's id for the conversation, which outlives
the process ids it starts; a host that gives none steadier keeps its session id *(the user,
2026-10-22)*. Whatever method runs between those two ends, the session is the same thing: that a
chat exists, is seen, falls silent, is reopened, ends, and what it leaves. The mechanism is
machinery, not method: a person works by the questions and the steps, never by a row.

**The row.** Each session keeps one file under `docs/sessions/rows/`, named by its tag, holding
one line: its tag, whether it runs, when the row was last written, its current question and up to
four recent ones. No two sessions write one file, so however many write at once none undoes
another's, and nothing is locked *(the user, 2026-10-13)*.
The two writes to a row not its own are a wake ending a silent session and a rename rewriting the
ids a row names. A store from before kept the rows under the question store, and before that every
row in one file; each is carried into the folder at the first write, by links that never overwrite,
and read until then. The row's form and lifetime are declared beside `/conclude`.

**A session's life.** The host's start hook registers the row under the host's steadiest id, or
finds it and turns it running again with its position kept, and reads the wake; every message is
a sign of life, kept outside the tree so the committed file does not move with every turn. A
running row nothing has seen for three hours is ended by the next wake, quietly *(the user,
2026-10-10)*; the session's next message turns it running again. The conclude writes the session
record under `docs/sessions/` and ends the row, its position kept, so a chat the host reopens finds
where it stopped. A row that reads ended for seven days is removed by a wake, since a reopen rarely
comes later *(the user, 2026-10-22)*; the wake's read lists running sessions only.

**Sessions see each other** through the rows alone: the window names the other running sessions
and their positions, and the wake's read lists them. They cannot call one another. One folder in
the working tree is how they see each other, so sessions that do not share the directory do not.

**Free unless locked.** A session is not of one method: the question it stands on names its root,
the root its method, and a free session runs whichever ring that is. A setting at its start may
lock it to one method, and a role may grant its skill set and rights; the row admits both as a
seam, and nothing writes either yet *(the user, 2026-10-22)*.

**Delivery.** The hook wiring and the hook's entry are the questions mechanism's, relied on here:
one hook serves both, the session's half — registered, seen, silent, reopened — one call into the
session script, the window's half the question script's own. No recipient's host file changes
for this mechanism.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| a session starts: registered under the host's steadiest id, or found and running again | `.agents/scripts/gw/sessions.py` | |
| a session is seen, at each message | `.agents/scripts/gw/sessions.py` | |
| a silent session is ended at another's wake | `.agents/scripts/gw/sessions.py` | |
| a session concludes: its record written, its leans, its row ended | `.agents/skills/conclude/SKILL.md` | |
| a session wakes and reads where the work stands | `.agents/skills/recall/SKILL.md` | |
| a row ended for seven days is removed | `.agents/scripts/gw/sessions.py` | |
| rows a wake changed in other sessions' files are committed | `.agents/skills/maintain/SKILL.md` | |
| a reply shows the sessions it runs beside, under debug | `AGENTS.md` | |
| a recall re-ranks nothing another running session is on | `.agents/skills/recall/SKILL.md` | |
| a commit holds one session's work alone | `.agents/skills/commit/SKILL.md` | |
| checking the rows | `.agents/scripts/gw/sessions.py` | |
| a chat resumed under a new id its host does not keep steady | — | <straw-dog question="q-0037.0017.0004">not yet</straw-dog> |
| sessions reaching each other beyond one working directory | — | <straw-dog question="q-0037.0017.0005">not yet</straw-dog> |
| a session locked to one method, or started with a role | — | <straw-dog question="q-0037.0005">not yet</straw-dog> |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |

## Install adds, uninstall removes

| part | where |
|---|---|
| the wake's instruction file | `.agents/skills/recall/SKILL.md` |
| the conclude's instruction file | `.agents/skills/conclude/SKILL.md` |
| this doc | `.agents/mechanisms/session/session.md` |
| its rules file | `.agents/mechanisms/session/session.rules.md` |
| the rows' script | `.agents/scripts/gw/sessions.py` |
| its tests | `.agents/scripts/gw/test/test_sessions.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the question script, for the store it reads and the hook entry it answers | `.agents/scripts/gw/questions.py` | `questions` |
| the shelf of Claude Code's hook wiring | `.agents/skills/questions/hooks/.claude/settings.json` | `questions` |
| the shelf of Codex's hook wiring | `.agents/skills/questions/hooks/.codex/hooks.json` | `questions` |
| the shelf of Cursor's hook wiring | `.agents/skills/questions/hooks/.cursor/hooks.json` | `questions` |
| the hooks' wrapper, launched by a Git alias | `.agents/scripts/gw/hook.sh` | `questions` |
| the mover | `.agents/scripts/gw/move_doc.py` | `ticket` |
| the shape check | `.agents/scripts/gw/mechanisms.py` | `mechanism-shape` |
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| test harness | `.agents/scripts/gw/test/repository.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The rows** — *what exists* — read by the script for every window and wake, so each session
  sees where the others stand; by the rows' check at the maintain pass; by a rename, for the ids
  a row names.
- **The session record** — *what happened* — read by the next session's `/recall` and by a person
  reading what a session did; the account of a session, where the row is only its position.
- **The wake's lines on sessions** — *what exists* — read by the agent at session start, through
  the hook or `/recall`, for who else is where.
- **The sign of life**, outside the tree — *what exists* — read by the script alone, to tell a
  silent session from a quiet one; a compaction empties it and keeps its time.
- **The check's report** — *what exists* — read by `/maintain` at its pass and by `/verify` through
  the verification set.

## Not yet at the shape

<straw-dog question="q-0037.0017.0005">
**The rows' folder** is one folder in the working tree, and that is how sessions see each other;
sessions that do not share the directory do not see each other.
</straw-dog>

<straw-dog question="q-0037.0010.0004">
**The rows' paths** are painted doors held by hand in the shape check.
</straw-dog>

## What retires this

Nothing: a tree that holds core holds sessions, and what would retire this is a host that keeps
a conversation's position and the other conversations' positions itself, with the same outputs —
then the row is the host's.

## What would show it working, graded by someone who did not build it

Four yes-or-no tests, pre-registered at the align that incepted it:

1. Open a chat, conclude it, reopen it the next day: does the wake say *already registered* and
   draw the window at its last position?
2. Leave a chat silent four hours and open another: does the first's row read ended, and the
   second's wake say nothing of it?
3. Eight days after a chat ended, open another: is the first's row gone, and the wake's list of
   sessions free of it?
4. Change a rule in the rules file and re-install: does the target's block change and nothing else
   in it?

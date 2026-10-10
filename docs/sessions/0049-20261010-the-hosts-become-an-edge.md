# Session 49 — the hosts become an edge

**2026-10-10.** Claude Code in the desktop app, one conversation under three Claude Code ids —
`58bf3b88`, `d0abdc88` after the app reopened it, `3a5196da` after a relaunch — and, since the
fix this session made, one session `local_48db9702…`. Entry contract v55 at the start; v56 and
v57 raised by parallel sessions, v58 here. It opened on the user's question: *do we keep the
requirements on a host, and the checks of a new host's integration, anywhere but ticket history?*

## What was decided, and what chose it

### The hosts are an edge, and the edge mechanism is declared — q-0023.0009, q-0018.0023.0001

- Asked, the tree answered no: the capability matrix and the whole connection run lived only in
  the narrative of
  [01-0010.0120 what-each-host-says-without-being-asked](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md),
  the hook files in the questions mechanism's parts, every host quirk in code alone. I proposed a
  host contract of its own. The user: *this is an edge; the edge mechanism is missing.* `/edge`
  had sat since 2026-09-05 with *Mechanism: not yet*, written for product surfaces elsewhere.
- I argued the record must ship with core, since core's hooks need it. Refuted *(the user)*: *the
  edge doc lives in docs and carries nothing the host integration needs to work — host record is
  doc of this harness development process, host integration implementation is part of the core.*
  And *outer boundary* was too narrow: *plugin-like shapes — like host integrations — should be
  part of edge responsibility too.* An edge became where the system meets those who consume it
  *and those who extend it*.
- The user asked that the record describe in general terms how a new host is created and tested,
  with each host's specifics in sidecars. One conflict resolved by the tree's own rule: a document
  never instructs, so the record's `Extending` holds checks, as a ticket holds criteria, and the
  skill's *Extend* goal is the instruction to pass them.
- *The maintenance rule must fit into maintenance* *(the user)*: the record's duties reach
  `/maintain` as installed rules, not a pass of the edge's own.
- Declared in [the edge mechanism](../../.agents/mechanisms/edge/edge.md), its evidence in
  [edge.evidence.md](../mechanisms/edge.evidence.md); the first record is
  [hosts](../edge/hosts.md) with three sidecars.

### A landing writes its edge — q-0025.0005

The user asked whether the rules say *what and when* to write into an edge. They covered
alignment and maintenance and missed the landing, the occasion that changes an edge most, and a
live observation had no rule sending it to the sidecar. E4 went to `/verify`; the same answer
closed where the installation edge's block lands.

### Staleness marking refuted

I built rules marking a sidecar result stale when a part it names moved, then proposed per-result
dependencies to narrow it. The user: *do we really need a complicated staleness detection here?
what problem does it solve, I still don't understand.* None that the observation's date does not
already: a reader sees the date beside the code's history. The marking cost a judgment at every
landing and risked erasing real observations; it went whole, and the proposed verdict vocabulary
with it. A glossary entry for *result* was refused: *a general word cannot be captured by a narrow
mechanism.*

### Verified means `/verify` passed — v58, rule failure 30

The edge mechanism was committed twice on a green verification set alone. The user: *did you check
it is good?* Read against what governs it, E4 contradicted E2 on which side wins and left
*touched* to the reader. The commit switch now says *commit when `/verify` has passed on the work*.
`/verify` then ran beside an independent agent that had not built the mechanism; it found eleven
faults the inceptor had not, all repaired — the evidence lists them.

### A resumed conversation is keyed on the app's id — q-0027

The app reopened this conversation under a new Claude Code id, and the store took it for a new
session. Investigated at the user's request: the start hook ran 3 s before the app wrote the new
transcript, so the transcript match found nothing. I proposed retrying the match on later
messages. The user: *don't we have a more reliable id that needs no acrobatics?* The desktop app
names the conversation itself in every process it starts, `CLAUDE_CODE_HOST_SESSION_ID`,
unchanged across the reopening; the terminal keeps its session id on resume, a new one only under
`--fork-session`. The session is keyed on the app's id where it is set, and the transcript match
was removed. Observed passing in both, at the user's hands: `claude --continue` in the terminal,
and a quit-and-relaunch of the app.

## General principles derived, with no home yet

- **A general word is not captured by a narrow mechanism.** A mechanism's format may use *result*,
  *check*, *standing* in their plain sense; its glossary entries are for words it gives a meaning
  of its own.
- **An observation's date is its staleness.** Recording what was watched, and when, is enough; a
  mechanism that marks it stale adds a judgment and no information.
- **Prefer the host's steadier identity to reconstructing one.** Where a host names the thing
  itself, key on that name before inferring it from artefacts that may not exist yet.

## What was done

- The edge mechanism: format moved from `/align`'s shelf to `/edge`'s, `edges.py` with 40 tests,
  E1–E4 installed in `/maintain`, `/align` and `/verify`, glossary *Edge* and *Extension*.
- The hosts record: contract, what an integration is made of, eleven checks, a sidecar per host,
  every result held to what was watched.
- Codex's helper observed: it carries its parent's `session_id`, yet its hooks give it no context,
  register no row and leave the parent's window whole. Claude Code's helper observed the same way.
- v58; rule failure 30 registered and closed.
- The resume fix in `questions.py`, the Resume check, observed in the app and the terminal.

## What went wrong, and what it taught

- **Committed on form alone.** Twice; the user's one question found two contradicting rules. Hence
  v58.
- **Over-built.** Staleness marking and a verdict vocabulary, both removed on the user's question
  of what problem they solved.
- **Swept another session's edits.** A broad `git add` took a parallel session's two-line edit into
  a commit of mine; a staged `git mv` of mine went into a parallel session's commit. Commit by
  path, and stage a shared file by hunk.
- **The installer placed a block inside another rule's straw dog**, silently: a section is read to
  the next heading whatever wrapper opened between. Worked around; a task chip was raised to make
  the installer refuse it.

## Open questions touched

- [q-0018.0023](../questions/q-0018.0023-how-does-the-harness-reach-more-hosts-than-claude-code-codex-and-cursor.md)
  — which host comes fourth, open.
- [q-0018.0023.0002](../questions/q-0018.0023.0002-which-text-a-hosts-user-meets-is-derived-from-the-hosts-edge-record-and-what-holds-it-a-subset-of-the-record.md)
  — what text is derived from the hosts record, opened here, waiting.
- [q-0027](../questions/q-0027-how-does-each-turn-know-its-next-step-and-each-session-where-to-resume.md)
  — the resume case settled; the question stays open for its other children.
- [q-0026](../questions/q-0026-how-does-the-harness-amend-its-own-rules-by-stated-meta-rules.md)
  — v58 landed.
- Closed here: q-0023.0009, q-0018.0023.0001, q-0025.0005, q-0018.0020.0002.0001.0001.

## What continues

The maintenance pass at the end found all six mechanisms due and marked none: session
`local_bc1f0ace` had an unfinished sweep across 254 files adding a `record of` line to every
record, the mechanism shape among them, and a mark taken then would have cleared its edits unread.
**The next session's first step**: once that sweep lands, a `/maintain` pass re-checking the six
mechanisms at both levels and writing their marks. Then the resume check for Codex and Cursor, and
Cursor's helper, the last unobserved results on the hosts edge.

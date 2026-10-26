# Edge — Hosts

- **Status:** Stub

## Contract

A **host** runs an agent's session and reads the tree for it. The hosts met are the rows of
`## Extensions`.

**Promised to whoever works in a host:** the same entry file, the same skills and the same rules
in every host reached; the question store's wake at session start and its window before every
message where the host carries them, with the entry file's rule as the floor where it does not;
and a hook that never fails the host, so a problem becomes a line of context
([architecture](../architecture.md), *the store*).

**Required of a host, to be reached in full:**

- it reads `AGENTS.md` at session start, itself or through a file that loads it;
- it finds the skills under `.agents/skills`, natively or through a loader link
  ([ADR 0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md));
- it runs a hook the project commits, at session start and before every message, and places the
  hook's output in the agent's context;
- the hook's input carries the host's own session id;
- a project's hooks can be approved or trusted per project.

A host lacking one of the last three is reached in part: the entry file's rule stands in, and the
agent draws the window itself.

**Offered by a host, used where it is offered and relied on nowhere:**
<straw-dog question="q-0037.0017.0005">one session's message to another, by which a session that
took over a unit tells its holder;</straw-dog>
<straw-dog question="q-0037.0015">and a helper agent started inside a session, which the method
uses as the judge of work its starter built. A helper receives no wake and no window, having no
start of its own and no message of the person, so a judge reads the entry file and runs the wake
itself, and the host's delivery of that text is this edge's live check, never the judge's.</straw-dog>
Where the window does not reach the agent, as in Cursor, a session sees another's hold only when
it draws its window itself, as the entry file's rule asks, and the refusal at a hold is the one
stop that needs no window.

<straw-dog question="q-0037.0006.0005.0001">
**Required of a host, to guard the files a mechanism controls** — an edit to such a file refused
while the skill the mechanism names is not loaded in the session:

- a hook before the agent's file edits that can refuse one and tell the agent why, a hook before a
  shell command that can refuse the agent's `git commit`, and a hook at the reply's end that can
  send back a reply proposing text for such a file;
- every way a skill is loaded — the agent choosing it, the person typing it — seen by a hook under
  the session's id;
- what the host keeps of a loaded skill across later turns and through a compaction, documented or
  observed, and the compaction seen by a hook under the session's id.

A host lacking one is guarded in part, and the commit's check stands in for the edit it cannot
refuse. A skill counts as loaded as the host keeps it, never by a lifetime the harness invents:
the host's row in `HOSTS` declares the events that load a skill and its lifetime rule, and the
check reads them there.
</straw-dog>

**What a host's integration is made of**, all of it core:

- a row in `HOSTS`, `.agents/scripts/gw/questions.py`: the input field carrying the session id,
  the environment variable naming the conversation more steadily if the host sets one, the start
  event, the message event if the host's answer reaches
  the agent, its compaction events, the function that writes its answer, and its quiet answer;
- its hook file's shelf under `.agents/skills/questions/hooks/`, at the path the host reads it
  from, each entry launching `.agents/scripts/gw/hook.sh` as `gw-hook <host>` — the install merges
  every shelf it finds there into the recipient's file of the same path, with no list to amend;
- a loader link in `LINKS`, `.agents/scripts/gw/harness.py`, unless the host reads `.agents/skills`
  natively, and a stub like `CLAUDE.md` unless it reads `AGENTS.md` natively;
- its hook cases in `.agents/scripts/gw/test/test_sessions.py`, and its merge in
  `.agents/scripts/gw/test/test_harness.py`.

Each sidecar names its own parts.

## Invariants

- A hook's unreadable input becomes a line of context — *validated by:*
  `.agents/scripts/gw/test/test_sessions.py`, the hook's unreadable-input case
- The hook exits clean whatever its input, so it never fails the host — **⚠ unguarded**: no test
  asserts its exit status
- A session is registered under the host's own session id — *validated by:* live —
  **Registration**
- In a host whose start hook reaches the agent, the wake's read arrives before its first command,
  with the installer's one line last when the tree's installed blocks are out of step with its
  rules files and settings — *validated by:* live — **Wake**
- In a host whose message hook reaches the agent, every message carries the window or the
  one-line notice that it is unchanged — *validated by:* live — **Window**
- The host lists the harness's skills and runs one by name — *validated by:* live — **Skills**
- <straw-dog question="q-0037.0006.0005.0001">An edit to a file a mechanism controls is refused
  while the skill it names is not loaded in the session — **⚠ unguarded**: the guard is not
  built</straw-dog>

## Extending

1. **Entry file** — a fresh chat's first reply opens with the entry contract line.
2. **Skills** — the host lists the harness's skills and runs one by name.
3. **Hook wiring** — the install merged core's hook entries into the host's committed hook file;
   the project's hooks are approved or trusted; the host's own log shows a hook ran and exited
   clean.
4. **Wake** — in a fresh chat, the wake's read is in context before the agent's first command,
   headed by the host's session id.
5. **Registration** — the rows under `docs/sessions/rows/` hold one under the host's steadiest id
   for the chat, and no tag minted by a bare `--wake`.
6. **Window** — the next message carries the unchanged notice; after an `at`, the one after it
   carries the changed window.
7. **Compaction** — after the host compacts the context, the next window arrives whole.
8. **Helper** — a helper agent spawned in a session registers no session of its own and leaves the
   session's window as it was: the session's next message carries what it would have without it.
9. **Silence** — a row silent three hours is ended by the next wake, and one message turns it
   running again.
10. **Offline tests** — the host's hook cases and its merge are in the test files the integration
    names, and pass in the verification set.
11. **Resume** — a conversation closed and reopened in the host keeps its session: the sessions
    file gains no row, and the reopened conversation stands where it stood.
12. **Edit refusal** — a hook refuses an edit before it is written, and a `git commit` before it
    runs, and the agent reads why; a hook at the reply's end sends the reply back.
13. **Skill load** — a skill the agent chooses and one the person types are each seen by a hook,
    under the session's id.
14. **Skill lifetime** — what a loaded skill stays loaded through: a later turn, a second read, a
    compaction; and the compaction seen by a hook.
15. **Messaging** — one session's message reaches another running session in the host, and the
    receiving session reads it; where it does not, nothing of the method waits on it.

## Extensions

| extension | standing | sidecar |
|---|---|---|
| Claude Code | reached in full; compaction and helper ids not watched | [claude-code](hosts/claude-code.md) |
| Codex | reached in full; start-hook attribution qualified; compaction and helper ids not watched | [codex](hosts/codex.md) |
| Cursor | reached in part: no wake and no window reach the agent, the entry file's rule stands in; registration leaves a second line | [cursor](hosts/cursor.md) |

## Concerns

- [q-0037.0006.0023](../questions/q-0037.0006.0023-how-does-the-harness-reach-more-hosts-than-claude-code-codex-and-cursor.md)
  — which hosts come next, and by what; here, whether a fourth can pass these checks.
- [q-0037.0006.0004](../questions/q-0037.0006.0004-what-does-each-host-put-in-front-of-an-agent-without-being-asked.md)
  — what each host places in front of an agent unasked; its observations are this record's
  sidecars.
- [q-0037.0006.0004.0001](../questions/q-0037.0006.0004.0001-how-is-it-observed-that-a-host-reads-the-loader-link.md)
  — whether a host reads the loader link is not observable from inside a tree; **Skills** is the
  nearest check, and Codex has no link to read.
- [q-0037.0006.0005.0001](../questions/q-0037.0006.0005.0001-which-skill-must-be-read-before-a-file-is-edited-or-a-rule-proposed-and-how-does-the.md)
  — the guard on the files a mechanism controls; here, how each host loads and keeps a skill, read
  from **Skill load** and **Skill lifetime**, and which hosts can refuse an edit at all.

## Roadmap

- The three hosts' unwatched checks — compaction, helper ids, Codex's start-hook attribution —
  observed: [01-0010.0120 what-each-host-says-without-being-asked](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md).
- A fourth host, chosen under q-0037.0006.0023: no ticket yet.
- The guard on the files a mechanism controls, once q-0037.0006.0005.0001's `Where it stands` is
  accepted: [01-0010.0125 the-host-blocks-what-a-rule-forbids](../tickets/01-0010.0125-the-host-blocks-what-a-rule-forbids.md).

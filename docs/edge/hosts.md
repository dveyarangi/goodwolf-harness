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

**What a host's integration is made of**, all of it core:

- a row in `HOSTS`, `.agents/scripts/gw/questions.py`: the input field carrying the session id,
  the transcript field if any, the start event, the message event if the host's answer reaches
  the agent, its compaction events, the function that writes its answer, and its quiet answer;
- its hook file's shelf under `.agents/skills/questions/hooks/`, at the path the host reads it
  from, each entry launching `.agents/scripts/gw/hook.sh` as `gw-hook <host>` — the install merges
  every shelf it finds there into the recipient's file of the same path, with no list to amend;
- a loader link in `LINKS`, `.agents/scripts/gw/harness.py`, unless the host reads `.agents/skills`
  natively, and a stub like `CLAUDE.md` unless it reads `AGENTS.md` natively;
- its hook cases in `.agents/scripts/gw/test/test_questions.py`, and its merge in
  `.agents/scripts/gw/test/test_harness.py`.

Each sidecar names its own parts.

## Invariants

- A hook's unreadable input becomes a line of context — *validated by:*
  `.agents/scripts/gw/test/test_questions.py`, the hook's unreadable-input case
- The hook exits clean whatever its input, so it never fails the host — **⚠ unguarded**: no test
  asserts its exit status
- A session is registered under the host's own session id — *validated by:* live —
  **Registration**
- In a host whose start hook reaches the agent, the wake's read arrives before its first command —
  *validated by:* live — **Wake**
- In a host whose message hook reaches the agent, every message carries the window or the
  one-line notice that it is unchanged — *validated by:* live — **Window**
- The host lists the harness's skills and runs one by name — *validated by:* live — **Skills**

## Extending

1. **Entry file** — a fresh chat's first reply opens with the entry contract line.
2. **Skills** — the host lists the harness's skills and runs one by name.
3. **Hook wiring** — the install merged core's hook entries into the host's committed hook file;
   the project's hooks are approved or trusted; the host's own log shows a hook ran and exited
   clean.
4. **Wake** — in a fresh chat, the wake's read is in context before the agent's first command,
   headed by the host's session id.
5. **Registration** — the sessions file holds a line under the host's own session id, and no tag
   minted by a bare `--wake`.
6. **Window** — the next message carries the unchanged notice; after an `at`, the one after it
   carries the changed window.
7. **Compaction** — after the host compacts the context, the next window arrives whole.
8. **Helper** — a helper agent's hook input carries an id, and whether it is the helper's own or
   its parent's.
9. **Silence** — a row silent three hours is ended by the next wake, and one message turns it
   running again.
10. **Offline tests** — the host's hook cases and its merge are in the test files the integration
    names, and pass in the verification set.

## Extensions

| extension | standing | sidecar |
|---|---|---|
| Claude Code | reached in full; compaction and helper ids not watched | [claude-code](hosts/claude-code.md) |
| Codex | reached in full; start-hook attribution qualified; compaction and helper ids not watched | [codex](hosts/codex.md) |
| Cursor | reached in part: no wake and no window reach the agent, the entry file's rule stands in; registration leaves a second line | [cursor](hosts/cursor.md) |

## Concerns

- [q-0018.0023](../questions/q-0018.0023-how-does-the-harness-reach-more-hosts-than-claude-code-codex-and-cursor.md)
  — which hosts come next, and by what; here, whether a fourth can pass these checks.
- [q-0018.0004](../questions/q-0018.0004-what-does-each-host-put-in-front-of-an-agent-without-being-asked.md)
  — what each host places in front of an agent unasked; its observations are this record's
  sidecars.
- [q-0018.0004.0001](../questions/q-0018.0004.0001-how-is-it-observed-that-a-host-reads-the-loader-link.md)
  — whether a host reads the loader link is not observable from inside a tree; **Skills** is the
  nearest check, and Codex has no link to read.

## Roadmap

- The three hosts' unwatched checks — compaction, helper ids, Codex's start-hook attribution —
  observed: [01-0010.0120 what-each-host-says-without-being-asked](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md).
- A fourth host, chosen under q-0018.0023: no ticket yet.

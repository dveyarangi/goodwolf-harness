# Edge — Hosts

- **Status:** Stub

## Contract

A **host** runs an agent's session and reads the tree for it. The harness meets three: Claude
Code, Codex and Cursor.

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
agent draws the window itself. What is host-specific lives in code — the host table and hook
answers in `.agents/scripts/gw/questions.py`, the hook shelves under
`.agents/skills/questions/hooks/`, the merge into each host's hook file in
`.agents/scripts/gw/harness.py` — and each sidecar names its own.

## Invariants

- A hook's problem becomes a line of context and never fails the host — *validated by:*
  `.agents/scripts/gw/test/test_questions.py`, the hook's unreadable-input case
- A session is registered under the host's own session id — *validated by:* live —
  **Registration**
- The wake's read reaches the agent before its first command — *validated by:* live — **Wake**
- Every message carries the window, or the one-line notice that it is unchanged — *validated by:*
  live — **Window**
- Whether a host reads the loader link is not observable from inside a tree; that it lists the
  skills is — *validated by:* live — **Skills**

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

## Extensions

| extension | standing | sidecar |
|---|---|---|
| Claude Code | reached in full; compaction and helper ids not watched | [claude-code](hosts/claude-code.md) |
| Codex | reached in full; start-hook attribution qualified; compaction and helper ids not watched | [codex](hosts/codex.md) |
| Cursor | reached in part: no wake and no window reach the agent, the entry file's rule stands in | [cursor](hosts/cursor.md) |

## Concerns

- [q-0018.0023](../questions/q-0018.0023-how-does-the-harness-reach-more-hosts-than-claude-code-codex-and-cursor.md)
  — which hosts come next, and by what; here, whether a fourth can pass these checks.
- [q-0018.0004](../questions/q-0018.0004-what-does-each-host-put-in-front-of-an-agent-without-being-asked.md)
  — what each host places in front of an agent unasked; its observations are this record's
  sidecars.
- [q-0018.0004.0001](../questions/q-0018.0004.0001-how-is-it-observed-that-a-host-reads-the-loader-link.md)
  — the loader link, the invariant no check inside a tree can watch.

## Roadmap

- The three hosts' unwatched checks — compaction, helper ids, Codex's start-hook attribution —
  observed: [01-0010.0120 what-each-host-says-without-being-asked](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md).
- A fourth host, chosen under q-0018.0023: no ticket yet.

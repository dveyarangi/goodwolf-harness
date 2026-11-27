# A file that holds secrets is closed to agents

- **record of** what it intends to become
- **Status:** Ready (aligned 2026-11-26)
- **Type:** HITL
- **Minted:** 2026-11-27
- **Answers:** [q-v6bnoz](../questions/q-v6bnoz-how-is-a-secrets-value-kept-out-of-what-a-session-prints-into-its-context.md)
- **Outcome:** In a tree that keeps a list of the files that hold secrets, the host refuses every
  call of an agent's that names one, and the agent reads such a file only with its values hidden.

## Parent

[q-v6bnoz](../questions/q-v6bnoz-how-is-a-secrets-value-kept-out-of-what-a-session-prints-into-its-context.md), whose *Where it stands* the person accepted whole on 2026-11-26; its
*Decisions* hold the four that are theirs. This ticket keeps the end-state; its four slices are
[01-0120.0010 claude-code-refuses-a-call-that-names-a-listed-file](./01-0120.0010-claude-code-refuses-a-call-that-names-a-listed-file.md),
[01-0120.0020 an-agent-reads-a-listed-file-without-its-values](./01-0120.0020-an-agent-reads-a-listed-file-without-its-values.md),
[01-0120.0030 codex-refuses-a-call-that-names-a-listed-file](./01-0120.0030-codex-refuses-a-call-that-names-a-listed-file.md) and
[01-0120.0040 cursor-refuses-a-call-that-names-a-listed-file](./01-0120.0040-cursor-refuses-a-call-that-names-a-listed-file.md). The split's impact is
recorded on the same question, *The draft split and its impact, 2026-11-26*.

## What to build

The stop is the host's refusal before the call, because a record that a file holds secrets was
read by nobody at the moment of the read, and a printed value cannot be taken back. The list is
the project's own, one tracked file of paths; the refusal covers a read, a search, a change and a
shell command alike, because a filter by a command's or a key's name has already failed once; the
one way through is a reader that shows names and structure and never a value. The entry file
takes no rule for it. The hosts come one at a time, and a host's record says the refusal holds
only once it was seen live there.

## Acceptance criteria

- [ ] In each of Claude Code, Codex and Cursor, in a tree that keeps a list, an agent's call that
      names a listed file is refused and the reader shows the file with no value, or the
      [hosts edge](../edge/hosts.md) says what that host cannot hold.
- [ ] A tree that keeps no list has no refusal wired.
- [ ] The entry file carries no rule for the refusal.
- [ ] `/verify` passes against this ticket and the governing docs.

## Out of scope

- A value already printed, and a copy of one in a file no list names: left out by the person's
  first decision on [q-v6bnoz](../questions/q-v6bnoz-how-is-a-secrets-value-kept-out-of-what-a-session-prints-into-its-context.md).
- A read that never names the file to the host — a script, a program that loads it: not held,
  and said so at an install.
- Moving the secrets out of a project's files: the project's own mending.
- The guard on the files a mechanism controls:
  [01-0010.0125 the-host-blocks-what-a-rule-forbids](./01-0010.0125-the-host-blocks-what-a-rule-forbids.md),
  which joins the same script only when the person releases it.
- A process that outlives the call that started it:
  [q-7v6dpa](../questions/q-7v6dpa-how-is-a-process-a-command-starts-kept-from-outliving-the-call-that-started-it.md).

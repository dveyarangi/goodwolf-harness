# q-5o3f6w What does the skill guard read at the agent's commit, now that a commit names its paths and stages nothing?

- **record of** what it intends to become
- **part of** q-5jcptm
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **asks** the person, 2026-11-24
- **opened** 2026-11-24T22:57:38Z
- **struck** 0, last 2026-11-24T22:57Z

## Why it is open, 2026-11-25

Found by the pass with no person of 2026-11-24, handed on by the session of the tickets, read again
at `71389a6b`.

**The decision.** [q-5jcptm](q-5jcptm-which-skill-must-be-read-before-a-file-is-edited-or-a-rule-proposed-and-how-does-the-host-refuse-the.md#decisions)
decision 5 (the user, 2026-10-25): the agent's `git commit` is refused by the hook before a shell
command while a *staged* declared file's skill is not loaded.

**What it meets.** S5 (the user, 2026-10-25, in
[session.rules.md](../../.agents/mechanisms/session/session.rules.md)): a commit names its paths
and stages nothing ahead of it; since `7ad25f37` (2026-11-22) Claude Code's hook denies a commit
that names none. So at every commit the host lets through, the files stand in the command and need
not stand in the index: a guard that reads the index alone would see none of them. Read from the
texts, not tried — the guard is not built.

**Where *staged* stands.** q-5jcptm's `Where it stands`, *The acts*, and decision 5;
[01-0010.0125-the-host-blocks-what-a-rule-forbids](../tickets/01-0010.0125-the-host-blocks-what-a-rule-forbids.md),
"What to build"; [01-0010.0125.0030-a-proposed-text-and-a-commit-wait-like-an-edit](../tickets/01-0010.0125.0030-a-proposed-text-and-a-commit-wait-like-an-edit.md),
"What to build" and the criterion on the root README. The parent ticket's own criterion says only
"`git commit` of a declared file" and holds either way.

**Options.**

1. The guard reads the files the commit takes: the paths the command names, and the index where it
   names none. The decision's purpose — a write through the shell caught at the commit — stands.
2. The index alone, as worded: on Claude Code the act catches nothing S5 lets through.

**Recommendation.** 1.

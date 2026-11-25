# q-5o3f6w What does the skill guard read at the agent's commit, now that a commit names its paths and stages nothing?

- **record of** what happened
- **part of** q-5jcptm
- **state** closed:deferred
- **answer** until the new system of roles is seen not to hold a session to its skills, meanwhile the skill guard is not built (the user, 2026-11-25: "это решение - усиление если не сработает новая система ролей")
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-24T22:57:38Z
- **struck** 0, last 2026-11-24T22:57Z

## Where it stands

Deferred on the person's word: the guard is a strengthening, taken up if the new system of roles does
not hold. What is read at the commit is decided then, with the options below.

## The person, 2026-11-25

To the Аудит и обслуживание session, of this question as it was put to them there with option 1
recommended; read in its transcript by the session of the tickets: "это решение - усиление если не
сработает новая система ролей." The whole guard waits on it, the agent's reading: they were told the
guard is not built, and on 2026-11-24 said of its act at an edit that roles and short sessions answer
the same need ([q-b4um7c](q-b4um7c-do-sessions-load-the-skill-their-act-needs-counted-from-the-hosts-transcripts-before-and-after-a-change.md)). That reading's second measure is what shows whether the roles held.

## Why it was open, 2026-11-25

Found by the pass with no person of 2026-11-24, handed on by the session of the tickets, read again
at `71389a6b`.

**The decision.** [q-5jcptm](q-5jcptm-which-skill-must-be-read-before-a-file-is-edited-or-a-rule-proposed-and-how-does-the-host-refuse-the.md#decisions)
decision 5 (the user, 2026-10-25): the agent's `git commit` is refused by the hook before a shell
command while a *staged* declared file's skill is not loaded.

**What it meets.** S5 (the user, 2026-10-25, in
[session.rules.md](../../.agents/mechanisms/session/session.rules.md)): a commit names its paths
and stages nothing ahead of it. No host's hook refuses a commit that names none: Claude Code's did
from `7ad25f37` (2026-11-22) to `19356b62` (2026-11-24), and Git's own `pre-commit`,
[pre_commit.sh](../../.agents/scripts/gw/pre_commit.sh), stands in its place, on trial in this clone.
So at every commit made as S5 says, the files stand in the command and need not stand in the index
when the command starts: a guard that reads the index alone there may see none of them. Read from
the texts, not tried — the guard is not built. Git hands a `pre-commit` hook an index holding the
paths the command names and nothing else staged, so a guard run there would see them (tried
2026-11-25 in a scratch repository, Git 2.32.0).

**Where *staged* stands.** q-5jcptm's `Where it stands`, *The acts*, and decision 5;
[01-0010.0125-the-host-blocks-what-a-rule-forbids](../tickets/01-0010.0125-the-host-blocks-what-a-rule-forbids.md),
"What to build"; [01-0010.0125.0030-a-proposed-text-and-a-commit-wait-like-an-edit](../tickets/01-0010.0125.0030-a-proposed-text-and-a-commit-wait-like-an-edit.md),
"What to build" and the criterion on the root README. The parent ticket's own criterion says only
"`git commit` of a declared file" and holds either way.

**Options.**

1. The guard reads the files the commit takes: the paths the command names, and the index where it
   names none. The decision's purpose — a write through the shell caught at the commit — stands.
2. The index alone, as worded, read before the command: it need show no file of a commit made as S5
   says.
3. The index alone, read in Git's `pre-commit`: it shows the files the commit takes. It stands in
   each clone apart, holds the index's lock while it runs, and
   [q-c2qp5n](q-c2qp5n-how-do-the-harnesss-checks-run-without-the-agent-at-push-and-in-the-projects-ci-beside-its-own-gates.md#decisions)
   decision 7 opened that hook on 2026-11-24 for one check alone.

**Recommendation.** 1: it needs no hook but the host's, which the guard's other two acts stand on.

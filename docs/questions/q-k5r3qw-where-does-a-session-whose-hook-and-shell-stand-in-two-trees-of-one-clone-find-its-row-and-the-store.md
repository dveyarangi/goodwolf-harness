# q-k5r3qw Where does a session whose hook and shell stand in two trees of one clone find its row and the store?

- **record of** what it intends to become
- **part of** q-7ebz2f
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-20T07:38:32Z
- **struck** 0, last 2026-11-20T07:38Z

## The case

game-delta's orchestrator (`local_4b1ce67d`), 2026-11-20 about 08:00Z, through the keeper; core at
acf3d272, which holds 639b897b, the fix of
[01-0010.0250.0020](../tickets/done/01-0010.0250.0020-the-harness-runs-in-a-worktree.md). Session
`local_39b5757e` began in the shared tree, then went on in a worktree
(`.claude/worktrees/elated-lichterman-2cb42a`). The host runs the hook from the project's root, so
the row was written in the shared tree's `docs/sessions/rows/`. The session's shell runs the
scripts from the worktree, whose own rows hold no such session, so `at`, `close` and `--wake` are
refused as not registered. The window there lists only the rows of the worktree's copy.

The case .0020 closed differs: there the session started in the worktree, so hook and shell
stood in one tree.

## What the code does

- `questions.py` takes its tree from its own file (`Path(__file__).resolve().parents[3]`).
- `sessions.py` takes it from the current directory (`Path.cwd()`).
- `hook.sh` runs `questions.py` by a path relative to the directory the host starts it in.
- The rows are tracked on `main`, so each worktree's branch carries the copy it was cut with.

## What the derived shape already answers

- The questions: [01-0010.0250.0110](../tickets/01-0010.0250.0110-the-questions-live-on-a-branch-of-their-own.md)
  shows one store at `docs/q/` in every worktree.
- The rows: [01-0010.0250.0090](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md)
  puts them in the server's database in the common Git directory. It waits on .0030, which waits on
  .0110, so until then a row stays in the tree that wrote it.

## The stop-gap, no code changed

Run every store call from the tree the hook runs in, the shared tree:
`cd "$(git rev-parse --path-format=absolute --git-common-dir)/.."` first. Its writes then land in
that tree's files, as the window shows them, and are committed there.

## Options, not yet put to the person

1. **The rows are read and written in the main working tree from .0110 on.** The main working
   tree is the parent of the common Git directory, the root .0110's plan already resolves for
   links out of an entry. A clone with a separate or bare Git directory keeps the calling tree, as
   there. Both scripts find the rows through one function. With `docs/q/` from the same slice,
   hook and shell agree wherever they stand, until .0090 moves the rows out of git. Recommended:
   one function more in a slice already held, and the interim it closes would last two slices.
2. **Wait for .0090**, the stop-gap standing until then.

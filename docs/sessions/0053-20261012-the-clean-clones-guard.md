# The clean clone's guard, and work that leaves a session by someone else's push

- **record of** what happened

A judge probe under q-0037.0001.0020.0001 reported that `--install --replace-clone` would empty a
developer's own clone of the harness: the guard read `git status` alone. The session fixed the guard
in a worktree, opened a PR, merged it into local main, and ran into the gap the fix's delivery
exposed: nothing says how a session's work gets from its branch into main.

## Decisions

- **The guard was repaired directly under repair=report**, not through /plan. The rule was explicit
  and cited: a clone holding anything of the person's is refused (the install skill, the
  docstrings of `run` and `_clean_clone_head`). Code and record:
  [q-0037.0006.0020](../questions/q-0037.0006.0020-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each.md),
  *The clean clone's guard, repaired 2026-10-12*. The mechanism doc's target paragraph now states
  what a replaced clone may not hold.
- **Ignored files are refused except what running the script leaves**: the loader links and
  Python bytecode caches. Refusing every ignored file was weighed and refuted. Running `harness.py`
  from inside the clone writes `__pycache__`, which the origin's ignore file ignores, so a blanket
  refusal would block the one recovery the flag exists for. A test holds that case.
- **Unpushed work is read across every ref**, `rev-list --all --not --remotes=origin`, not only
  HEAD. The report named HEAD; the tests showed that HEAD was already refused, though by accident,
  and that the branches beside it were not.
- **The fix reached local main only, by the user's word.** The user: *потом пушь в локальный
  мэйн* ("then push it to local main"). It went to origin anyway, through another session's
  push; see below.
- **The branch-to-main question sits under q-0037.0017**, not q-0033.0004: the case arises with one
  person on several worktrees, not only with a team. Opened by another session at the user's
  request.

## What went wrong, and what it taught

- **The report was narrower than the defect.** Writing the tests first found four ways past the
  guard, against the one reported: a HEAD commit refused only because the source could not
  resolve it; an unpushed side branch wiped; an ignored file wiped; `--at` skipping the guard
  outright. A probe's finding is a lead, not a specification.
- **A worktree session cannot use the question store.** The start hook registered this session
  in the main checkout's store. The worktree's copy refuses every call as *not registered*. The
  two ways around it each break a rule: writing into a tree other sessions work in, or
  registering a second session for one conversation. So the question was opened by another
  session, by message.
- **PR #5 carried 8 commits of other sessions.** The worktree branched from a local main ahead
  of origin, and pushing the branch published them.
- **One session's push carried another's held-back work.** The guard merge, kept local as the
  user asked, went to origin when the next session committed on that main and pushed it whole
  under `push=auto`. That also marked PR #5 merged. Recorded in
  [q-0037.0017.0002](../questions/q-0037.0017.0002-how-does-a-sessions-landed-work-get-from-its-branch-into-main.md).
- **The suite's guard on the live question store failed a test** because this session edited a
  question record while the suite ran. It passed when re-run alone. This is the case q-0037.0007.0002
  is about.

## Questions touched

- q-0037.0006.0020: the guard repaired; still open on the loader-link misjudgement and the release
  flow, as its lean says.
- q-0037.0017.0002: open; it waits on an align over the candidate shape, where the PR is the unit of
  verified work and merging is the person's or a switch of its own.
- q-0037.0001.0020.0001: its record still lists the guard as a confirmed hidden part; that is now
  history, and the repair is recorded at q-0037.0006.0020.

## What continues

The commits `71fd4ff` and this record stand in local main, unpushed, by the user's word: they
leave with the next session's push. The first step of a next session on this thread is the align
on q-0037.0017.0002.

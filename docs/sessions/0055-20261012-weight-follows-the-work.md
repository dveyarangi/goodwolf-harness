# Session 55 — weight follows the work

- **record of** what happened

2026-10-11 to 2026-10-12. Opened on `/recall` at entry contract v63; the entry file moved under it
to v84 by the sessions running beside it. Two strands: a rule making the method lighten for small
work, and an align on how a session's work reaches main, opened at another session's request.

## Decisions, and what chose them

**Weight follows the work** *(the user)*, a general rule in the entry file at v64, a straw dog bound
to q-0037.0013.0003. The occasion: a recipient's agent, asked to set two autonomy switches, opened
`/mechanism`, ran four whole-tree checks, edited a question record in passing and pushed — *это
безумно много всего на просьбу поменять два значения*. The cause read: the `commit` switch's gloss
named the whole verification set, and the explicit rule outweighed Occam, which already names
steps. The first amendment drafted listed exempt cases — a project's local file, doc-only changes —
and was refused: *очень ad-hoc правила, разжевываешь для умной модели?* What landed is one principle
and one struck gloss. Rule failure 32.

**Whatever stands on the shared main may be published; held-back work stays on its own branch
until released** *(the user)*, in the architecture and `/commit`. Read from git's logs: the worktree
branch behind PR #5 was cut from local main seven commits ahead of origin, verified work that
`push=auto` would have published within minutes — noise, no harm. The harm was this session's
push of `040e052`, which carried the merge `a71028b` the user had asked to keep local, and marked
PR #5 merged. Every session commits to one local main, so any push is everyone's. Weighed and
dropped: a check refusing a push over other sessions' commits — *проверка блокирующая пуш блокирует
весь процесс для нескольких сессий, не?* — commits interleave, so it would stall every push, and it
treats every foreign commit as held back when one was.

**A branch per session comes only together with a question store that does not travel through
git** *(the user)*, a straw dog in the architecture bound to q-0037.0017.0002.0001, deferred: *сейчас
ничего не выносится … вероятно все хранилище*. In one checkout a branch means a worktree, and a
worktree has its own copy of the store: sessions stop seeing each other, ids are minted blind, the
hand-bumped entry contract version conflicts on merge.

## What was done

- [q-0037.0017.0002](../questions/q-0037.0017.0002-how-does-a-sessions-landed-work-get-from-its-branch-into-main.md)
  opened on the guard session's relay — it could not reach the main checkout's store from its
  worktree — and closed decided; its body holds the evidence and the reasoning.
- q-0037.0017.0002.0001 opened and deferred.
- Partial commits where another session's uncommitted v63 shared the entry file; v64 went to
  origin before v63's text.

## What went wrong

- This session pushed another session's held-back merge. It read neither `origin/main..main`
  before pushing nor anything recording the hold; nothing in the tree recorded it. The invariant
  now makes main publishable by definition.
- A reply said PR #5 had been merged by *someone*; it was this session's push.

## Questions touched

- q-0037.0013.0003 How does the method lighten for small work and weigh more for large? — open; one
  principle stands, what weighs a change waits on the principle proving too loose.
- q-0037.0017 What is a session to the harness, and which mechanism keeps its lifecycle? — open; its
  align next, now with the branch and store evidence.

## What continues

The queue's two leading items are held by running sessions. Next free in order: the environment
align on q-0037.0006.0022, then 01-0010.0170 re-read. Waiting on the user: that choice against q-0037.0017's
align out of order, and where 01-0018.0010 stands in the order.

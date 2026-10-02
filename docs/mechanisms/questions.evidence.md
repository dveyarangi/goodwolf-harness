# questions — evidence

Why [the doc](../../.agents/mechanisms/questions/questions.md) is what it is: what was measured,
what was refuted, and what it replaced. Provenance stays on each decision in its ticket.

Declared by [01-0011.0100.0010 the-store-and-questions-writes-it](../tickets/01-0011.0100.0010-the-store-and-questions-writes-it.md),
2026-10-02, the first slice of
[01-0011.0100 the-open-questions-are-kept-by-a-mechanism](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md),
whose decisions 1 to 45 are the shape's reasons.

## The prior corpus

No store existed, so `questions.py --check` had nothing to run over: no prior count, rather than
a manufactured zero. The questions this tree already kept lived in three stores with three
formats, counted 2026-09-28: the three concerns of `concerns.md`, which this slice folds in; 35
open-issue bullets on tickets, left to
[.0020](../tickets/01-0011.0100.0020-open-issues-are-entries-of-the-store.md); and 60 distinct
straw-dog conditions, left to
[.0030](../tickets/01-0011.0100.0030-straw-dogs-are-entries-of-the-store.md). None of the three
said which question the work stood at.

## The window test

[83 trials](../research/window-test-2026-09-28.md) over four renderings at 100 to 30,000
entries: the window placed every near question exactly at constant cost, while reading the whole
store stopped silently at 10,000 entries and answered anyway, and flat, tree and path renderings
were no different where a whole store was readable at all. The written form was therefore decided
by writing and insertion cost — flat files with a parent line — and never by the reader, who never
reads the store. The window as drawn adds each line's state and lean, the other sessions and the
next free id to the rendering measured; a change to its format reruns the test.

## What was refuted

- **Candidate search over glossary terms** (decision 28): an *Avoid* list is a reservation of a few
  words, not a synonym map, and it made the search lean on the document most often incomplete.
- **The tickets as the store** (decision 30): tickets are a method's goals and a method can be
  swapped; the substrate cannot live inside it. Also one file for all questions.
- **Nested directories, one file per root** (decision 34): the path would be a second home for the
  parent, and insertion would rewrite a page.
- **A reply mode** checking that the agent declared: a checker the agent runs is forgotten with
  the declaration it checks; the observer of a missing line is outside the agent.
- **A height sweep**: height was meant as an abstraction height, not depth in the structure; held
  as an open question instead.
- **Deleting finished subtrees** (decision 43): one home per fact, but it loses the title search
  and reuses ids without a counter. `done/` is kept, and each closed entry points to its answer.
- **Claude Code alone first** (decision 44): its premise, that Codex and Cursor were not in use
  here, was wrong — all three run in parallel on this tree.
- **The declared line spelled out at tier 1**, some 330 words, and its forms kept in the wake's
  read or a window footer (decision 45): text placed anywhere in a session is carried by every
  later turn, so no other place is cheaper, and a strict grammar cannot be guessed — four example
  lines at tier 1 instead.

## Decided while building

From stages 1 to 3, each a reading of the RFC where it left a detail open: the sessions line
`<tag> running|ended <date> <q-id>|- [<q-id>,…]`; a slug is the question's leading words up to
forty characters; twins share at least three content words and half the shorter title's;
`nothing` writes nothing, the date included; a closure keeps an existing suspect flag; the writer
refuses a closure the check would fail; a host's hook never fails the host, and a session whose
start no hook saw is registered by its first message.

# Every second look at produced work is a pass

- **Status:** Planned (decision-bearing; its own align precedes the feature)
- **Type:** HITL
- **Answers:** [q-0029](../questions/q-0029-how-is-produced-work-gone-over-again-over-what-scope-by-what-criteria-by-whom-and-to-what-result.md)
- **Outcome:** Whether going over produced work again has one shape — the pass — is decided by
  the user against its formalization, and what is decided is landed in its durable home, so
  the work that would declare it can be planned.

## Parent

None: a root, minted 2026-10-05 from the align on
[issue 2](https://github.com/dveyarangi/goodwolf-harness/issues/2), where the question of who
checks a rule that has no moment widened into this one. The outside material is
[the second-pass discovery](../research/discover-second-pass-2026-10-05.md). It is a
**candidate for a mechanism**, not one: nothing here is built until the user has revised the
shape *(the user, 2026-10-05)*.

## One machinery under maintaining, verifying and judging

*(The user, 2026-10-05)*: judging is not an instance but a method — a second pass on the same
object under mostly different rules and data. A maintenance pass that repairs earlier agents'
work is it; verification is it; several passes of planning are it; the user is a judge too. A
second pass may amend an invariant, a style, or how far a principle was honoured, and it is the
same process. What is one thing is the raw machinery.

The outside pass found no accepted umbrella term — *judge* names one model assessing another,
*evaluation* a measurement of a system — and several fields that keep these activities apart by
their purpose and by who performs them. The claim here is narrower than theirs: the machinery is
shared, whatever the purposes are.

### The terms, as working words

Accepted as working words *(the user, 2026-10-05: "the pass terminology seems alright")*; none
is in a glossary yet, and each becomes an entry or is dropped at the align.

- **Pass** — the kind: produced work gone over again by the operations below.
- **Pass profile** — one fixed setting of a pass's parameters. Maintenance is one, verification
  another.
- **Run** — one execution of a profile. The `/maintain` skill says *one pass over a declared
  scope* for this today.

### The operations

1. **Select the scope.** A judgement of its own, different from applying.
2. **Slice it**, in the shape the criteria need.
3. **Drop irrelevant slices cheaply**, before a costly model reads any.
4. **Apply the criteria** to each remaining slice.
5. **Dispose**: amend in place, move text to another file, or write a revision document.
6. **Record what was covered**, and stop or go round again.

### The parameters a profile fixes

| Parameter | What it settles | Maintenance today |
|---|---|---|
| Scope method | what is gone over, and whether choosing it takes judgement | a script reports what is due; the run declares the rest |
| Slicing | the unit the criteria are applied to | a mechanism: its doc, rules and records |
| Relevance filter | what never reaches the costly stage | none |
| Criteria | what a slice is held to — an invariant, a format, a style, a principle | its four agreements |
| Performer | a script, the same agent, another agent, a fast classifier, a person | the working agent, and scripts for format |
| Iteration order | which slice first, when a repair changes what later slices are held to | upper link first |
| Disposition | amend, move, or report | repair, and archive what is finished |
| Stop condition | once through, or until nothing changes | once through |
| Coverage record | what was examined, under which criteria | the marks |

Scope differs by profile: maintenance may fall on any kind of record, skills included, and changes
each run; verification falls on a landed change, its code and its governing docs; a style pass on
named outputs.

### What the formalization already shows

- **Slicing cannot be chosen apart from the criteria.** A criterion needs to see one slice (*no
  instruction under `docs/`*), a pair (*a doc agrees with its implementation*), or the whole
  scope (*every fact has one home* — the two copies sit in different slices).
- **The relevance filter is itself a pass**, with a cheap performer and one criterion; passes nest.
- **What the cheap stage drops is never seen again.** Its misses are invisible unless a sample of
  what it rejected is read.
- **Finding and fixing are one party here.** Audit keeps them apart, because the one who fixes
  loses independence; the outside pass lists what else is known to go wrong.

## What to build

At minting, the alignment exit:

- The user revises the shape above: the operations, the parameters and the three working words.
  It is theirs to change, not the agent's to build from.
- The forks are decided, each an entry under this ticket's question: whether the pass is a
  mechanism or a shape existing mechanisms are declared to; whether maintaining, verifying and
  re-planning are one thing; whether the performer changes what a pass is; how a cheap filter's
  misses are seen; where a tree's invariants are declared.
- What is decided lands in its durable home — the method glossary for the terms that survive, a
  mechanism's doc if it is a mechanism — and this ticket is rewritten in place to the feature that
  follows, or completes as a landed decision if the shape is refused.

A second profile is what would prove the shape: maintenance alone is one instance, and one
instance does not make a kind.

## Acceptance criteria — provisional, firmed at the align

- [ ] The user has revised the formalization, and what they changed is in this ticket.
- [ ] Each fork under q-0029 is closed against its durable home or left open with its owner.
- [ ] The working words are glossary entries or are gone from every record.
- [ ] A second profile besides maintenance has been described by the same parameters, or the
      shape is recorded as one instance and not a kind.
- [ ] `/verify` passes against this ticket and the governing docs.

## Out of scope

- The rule that a document neither instructs nor authorizes: landed in the entry file at v31; it
  waits on this ticket's question only for its owner.
- A judge inside the turn, for placing a message: q-0001.0016.0001.
- Rewording a question: q-0001.0021.
- What scope is, in one account: [01-0014](./01-0014-scope-coherent.md), a neighbour this
  ticket's align reads.

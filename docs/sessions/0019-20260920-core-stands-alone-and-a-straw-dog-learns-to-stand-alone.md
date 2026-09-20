# Core stands alone, and a straw dog learns to stand alone

Session nineteen, 2026-09-20, the afternoon after [session eighteen](0018-20260920-the-ring-runs-whole-in-a-day-and-a-list-is-refused-for-a-line.md).
It opened with "hello" and a side stroll, ran `/recall` first unasked, and then took
[01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md) through the whole ring — three
`/plan` passes, `/implement`, `/verify`, `/maintain` — and a whole-tree `/maintain` after it. The
second ticket to run the ring in a day, the same day as the first. Commits of mine: `MAINTAIN`
(the README), `PLAN`, `IMPLEMENT` ×2, `VERIFY`; the close, the denoise and this record are
uncommitted at writing (`commit=ask`); nothing pushed.

## Work completed

Details are on the records named.

- **The side stroll.** GitHub renders `docs/README.md` as the repository's front page, the root
  having none; it carried history and a Windows path. Now an index, provisional entries wrapped.
- **`.0140`, planned to closed** ([the ticket](../tickets/done/01-0010.0140-core-stands-alone.md),
  [the RFC](../rfc/done/01-0010.0140-core-stands-alone.md)). The leak check is one more question
  of the register `mechanisms.py --check` walks: every path under `docs/` a core file or the
  entry file names is a painted door, skipped inside an instance-owned block, or a leak that
  fails the run. Tags read through the corpus's code-blanked view, paths on the fence-blanked
  text; a `TODO` naming its ticket is a binding; a script the tokenizer cannot read is a
  diagnostic. Holding list of painted doors as the check's own data under four `TODO`s. 17 leaks
  before repair, none after; 243 tests. The rules core read from `docs/process.md` moved: the
  verification set's definition into `/verify`, the repair conditions under the `repair` switch,
  this project's commands into the entry file's local block, wrapped on `.0110`.
- **Painted door** entered the method glossary *(the user)*, with *place* and *path convention*
  under *Avoid*.
- **Two rule failures**, both amended in the entry file the same day, v10 → v12
  ([the register](../rule-failures.md), [the version record](../research/entry-contract-findings.md)):
  failure 3 struck again — the straw-dog rule now fires in the pass that mints a ticket against
  existing text; failure 6 opened and closed — core names a ticket only in a straw dog's binding,
  and a body stands on its own, naming no ticket, because it is what a recipient reads after the
  shear.
- **The whole-tree denoise.** The queue header is a status page again; the shape doc's story
  moved to its evidence and five closed-ticket wrappers retired with it; two sentences the user
  ruled out on 2026-09-07 left `/verify` and `/implement`; the architecture doc lost a landing
  story; two bare ticket ids left core prose.

## What the user corrected, kept as evidence

- **"Naming a ticket in code of the instance is totally alright — a `TODO` in harness code should
  be stripped on separation, just as a straw dog is."** I had put it to them as a choice; the
  shear owes the form and `.0130` carries it.
- **"Keeping the ticket link in the straw-dog attribute is a valid thing, we already decided on
  it. Why did not this rule register?"** I had written six closed tickets as bare ids on a
  reason (*closed work changes nothing*) the refusal never depended on. Failure 6.
- **"You are still messing with straw dogs. Consider what happens to what remains when the rule
  is migrated to another project without the ticket referenced. It should still make sense as it
  is."** My first amendment had put the id inside the wrapper. The rule is about the body.
- **"The verification set is a straw dog."** Wrapped on `.0110`, which already listed the block.
- **"Why do the mover failure and straw-dog contract in `/maintain` point to fleeting docs
  still?"** Discussed, not acted on — below.
- **"Painted door, no?"** over *place*.

## Open, with owners

- **`/maintain`'s two architecture links** — the mover's failure contract and the straw-dog
  contract, core reading its own contract from the instance half through a local block. No
  ticket owns moving them. Recommended: the mover's contract to the ticket mechanism's doc, which
  owns the mover; the straw-dog contract to whichever mechanism
  [01-0016](../tickets/01-0016-responsibility-coherent.md) elects. Waits on the user.
- **`.0110`'s `/plan`** is the queue's candidate, `next-cycle=ask`.
- **The remover and inline wrappers** — `straw_dogs.py --remove` deletes whole lines, so it cannot
  retire an inline wrapper without the sentence around it; the five today were retired by hand.
  The straw-dog mechanism's, once 01-0016 elects it.
- **A bare ticket id in core prose is invisible to every check.** A guesser tell would close it;
  unowned.
- **The install spec's testing bullet** still says *path convention*; left as the accepted spec's
  wording.
- **Carried from eighteen, unchanged:** 01-0020's rules file for the wake rule and the entry
  file's third claimant; contribution back; the user's grade on the mechanism shape; frost_map's
  `tickets.py` unrun; 01-0017's nineteen claims.

## Housekeeping

Five commits of mine on `main` today before the close, `806ae95` the last; the close, the
denoise and this record uncommitted; nine commits ahead of `origin/main` before them, unpushed
(`push=ask`). Verification set green: 243 tests, three checks clean; 67 straw dogs at the close,
all bound, no condition met. Entry contract v12.

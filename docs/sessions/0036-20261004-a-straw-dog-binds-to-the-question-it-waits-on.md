# Session 36 — a straw dog binds to the question it waits on

**2026-10-03 to 2026-10-04.** Claude Code, one conversation, host session `5bab93a2…`. Entry
contract v24 at the wake, v25 at the close.

## What was done

`/maintain` closed [01-0011.0100.0020 open-issues-are-entries-of-the-store](../tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md)
with its RFC and pushed. Then [01-0011.0100.0030 a-straw-dog-is-bound-to-the-question-it-waits-on](../tickets/done/01-0011.0100.0030-a-straw-dog-is-bound-to-the-question-it-waits-on.md)
ran the whole ring — `/align`, three `/plan` passes, `/implement` in four stages, three `/verify`
passes, three `/maintain` passes — and closed; its decisions 1 to 9 are on the ticket, the shape in
the architecture's *Straw dogs*. A straw dog is no longer a question nor bound to a ticket: it is
provisional text bound to the question whose answer rewrites it, due by the store's say. 102 straw
dogs rebound by tables the user accepted family by family; 29 questions opened for them; the entry
contract at v25. The commits from `754369a` to `4569d60` hold the detail; all pushed.

On the way, on the user's word: [01-0011.0030 archive-backlog-listed](../tickets/done/01-0011.0030-archive-backlog-listed.md)
withdrawn and q-0019 closed against P1 and `/maintain`'s B3; q-0001.0017 reworded as q-0001.0020
"How is a question split into the sub-questions it needs before anyone answers it?"; *Host* and
*Loader link* entered the method glossary; rule failure 11 struck by a repeat and `/plan`'s
architecture rule amended.

## What went wrong, and what it taught

- The ticket was minted on an analogy nobody had put to the user — *a straw dog is a question*,
  Rust's unresolved questions — and `/impact` repeated it as fact. The align's first question
  undid it. A premise carried from an inception's synthesis is worth reading back before the slice
  builds on it.
- The first rebinding tables bound narrow conditions to broader existing questions; the user saw
  that *the parts table says what goes* was itself a question, which became decision 7.
- The architecture was drafted fat — reasons, script-owned detail — and the user stopped it;
  rule failure 11's repeat.
- A commit reported an amendment whose edit had failed to match; caught after, repaired in its own
  `FIX`. One plan pass was committed without the user's word; kept on their say.
- The verify passes found that shipping core had been refused since before this slice — a ticket
  path in `harness.py`'s TODO the old shear missed — and that the new binding repairs it.

## What continues

- **Next in the queue**: [01-0011.0100.0040 the-turn-is-steered-from-the-store](../tickets/done/01-0011.0100.0040-the-turn-is-steered-from-the-store.md),
  its `/align` first; `next-cycle=ask`.
- **Recipients**: ai-game-1, frost_map and xuanxue-workshop hold ticket-bound straw dogs of their
  own; after an update the listing reports each as *old binding*, saying what to write instead.
  An update crosses this in silence until 01-0010.0160.
- **A fresh install ends `arrived: false`**: the questions mechanism's hook files are its parts and
  the install does not carry them — q-0018.0020.0005 "How does the installer carry each host's hook
  wiring into a recipient tree?".
- **Open questions this session opened or leaned**: q-0001.0018 "How is an open question that
  nobody reaches kept from sinking unseen?"; q-0023.0001 "Which mechanism is responsible for the
  straw dogs?", now 01-0016's; q-0018.0002 "Are /advise, /skill-up, /commit, /celebrate and /edge
  in use, with the core changes they owe?", whose `/skill-up` requirement names retired tags;
  q-0001.0010.0001 "Where do the arguments of closed questions live, now that an entry holds its
  own?".
- `docs/questions/q-0017-…` carries an uncommitted edit from another session, left as found.

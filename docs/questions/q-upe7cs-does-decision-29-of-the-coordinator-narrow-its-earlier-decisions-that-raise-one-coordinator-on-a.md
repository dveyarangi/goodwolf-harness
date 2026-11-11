# q-upe7cs Does decision 29 of the coordinator narrow its earlier decisions that raise one coordinator on a network, and what does it leave unsaid across machines?

- **record of** what happened
- **part of** q-7ebz2f
- **state** closed:decided
- **answer** [q-7ebz2f, decisions 33, 39 and 44, the list kept by decision 31](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md#decisions) — the user, 2026-11-09
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-09T07:51:25Z
- **struck** 0, last 2026-11-01T04:12Z

Opened 2026-11-01 by the scheduled `/maintain` pass with no person, sweeping the decisions landed
since 99122544. Decision 29 of
[q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)
names what it supersedes and reopens — 22, and 23's id, 24 and 26 — and no other; the question
sits at the load-bearing rung, so the pass asks rather than repairs.

- The decision, the user, 2026-10-31: across machines copies that merge, carried by git; a write
  needs no network; the coordinator on one machine takes writes in turn and gives "the live view,
  not the truth of every machine"; the seam a log of the store's changes and the rule that merges
  two logs.
- The earlier decisions it meets without naming them, in the same entry: 4, "On a network,
  someone raises the same coordinator at home or on a server"; 5, "On a network the person raises
  it, and its address is a setting of the project"; 10, "Not: a queue of changes … the event log
  with all its merging … weighed again for the networked mode"; 13, the coordinator "which alone
  writes and commits it"; 18, "A check at push then reads the live truth … as one truth asks";
  28, a second clone's coordinator "whose pushes the lease on the ref refuses", standing on 24's
  lease. In
  [q-crvu5f](q-crvu5f-what-carries-the-shared-place-every-session-reads-at-each-step.md),
  decision 4, "positions, messages and the questions' changes go through it … the git ref of
  decision 3 is not needed there".
- What it leaves unsaid: whether the sessions' rows, positions and messages also travel between
  machines as the store's copies do, or stay the one machine's —
  [01-0010.0250.0090](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md) says the
  rows' calls "carry over to a network"; what a check at push reads, once the coordinator's view is
  not every machine's truth; and `docs/architecture.md`'s straw dog bound to
  q-7ebz2f, "A branch per session comes only together with a question store that
  does not travel through git", which decision 29's copies carried by git now meet — it waits for
  the question's close by its binding.
- Marked by this pass, in decision 29's own words and adding nothing: the accepted Where it stands
  named as reopened where 01-0010.0250, the RFC and ticket of 01-0010.0250.0030, and six child
  questions call it accepted; the networked mode in their out-of-scope lines; the entry's own list
  of what is open.

Options:

1. **Decisions 4, 5, 10, 13 and 28, and q-crvu5f's 4, are marked narrowed by 29**
   where they speak of a coordinator raised on a network, a coordinator alone writing, or a lease
   refusing a second clone, and kept for one machine; 18 and the rows across machines are taken
   with q-7slcca, the merge rule deciding what a push check reads and whether
   rows travel.
2. **Each is weighed apart at `/align`**, beside q-ocix2p and q-7slcca.

Recommendation: 1 — each of these speaks of the networked frame decision 22 held, and decision 29
replaced that frame whole; what still holds of them is the one machine's case, which 29 keeps.

Decision 33 of q-7ebz2f, the user, 2026-11-05, brings back decision 22's one
coordinator and narrows 29: the recommendation's "replaced that frame whole" and option 1's "kept
for one machine" no longer stand as written, and the rows across machines and what a check reads
are answered by it and by decision 9 of q-7slcca.

Decision 10 of q-7slcca, the user, 2026-11-08, raises a temporary server on a
machine that cannot reach the one server, as decision 5 raises one on a single machine: option 1's
"kept for one machine" now holds away from the one server too, and leaves unsaid how many servers
stand on a network while the one is unreachable.

The user, 2026-11-09: option 1, carried out in the pass decision 31 of q-7ebz2f sets.

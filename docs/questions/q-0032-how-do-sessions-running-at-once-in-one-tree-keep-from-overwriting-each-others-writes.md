# q-0032 How do sessions running at once in one tree keep from overwriting each other's writes?

- **record of** what it intends to become
- **state** open
- **lean** the user, 2026-10-08: locks are needed; the architecture disclaiming safe simultaneous writers no longer holds
- **struck** 0, last 2026-10-08T07:13Z

Opened 2026-10-08 at the front-page align (q-0031). Comparing peers showed the harness behind on
this: sessions see each other's positions in the store, but nothing stops two of them writing
the same record. The architecture said as much — *does not promise safe simultaneous writers* —
and the user: *the architecture lies; locks are needed.* That sentence is now a straw dog bound
here.

What the tree has today:

- **The question store** refuses a write to an entry that moved since it was read. That is an
  optimistic check, with no lock and nothing claimed.
- **The sessions file** lets each session replace only its own line.
- **Everything else** — tickets, the queue, the architecture, skills, code — has nothing at all.
  This day had six sessions running in one working tree.

What peers do, from [peer-capabilities-2026-10-08](../research/peer-capabilities-2026-10-08.md):

- **GSD** guards each state write with a lockfile (`STATE.md.lock`, `O_EXCL`, 10 s stale
  timeout), keeps a planning-wide lock, and gives each session its own workstream; executors run
  in worktrees by default.
- **beads** has an atomic claim with leases, compare-and-set updates, hash ids against merge
  collisions, and a server mode for concurrent writers.
- **Gas Town** gives each agent its own worktree, and a scheduler caps how many run at once.
- **Claude Code's agent teams** lock the shared task list.

Neighbours: q-0016.0001 "How does a starting agent pick an area that does not overlap another
session's?" — avoiding overlap at the start, where this question is about writing; and
q-0024.0002, a team on parallel branches. Unsettled: what is locked (a file, a record, an area),
for how long, how a lock held by a dead session is released, and whether sessions should rather
work in separate worktrees.

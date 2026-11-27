# q-2rio5w Does /maintain hold a record's citation of code in another repository to that code, as the code moves?

- **record of** what it intends to become
- **part of** q-7ld3wt
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-27T00:27:00Z
- **struck** 0, last 2026-11-27T00:27Z

Raised by the audit of the harness in DriftSense, round 4, 2026-11-27:
[the health record](../research/harness-in-driftsense-audit.md#round-4--records-about-code-in-sibling-repositories-2026-11-27).
DriftSense's records cite its sibling repositories' code 665 times, 414 with a line; of 15 read,
8 pointed at a line the code had moved from and 1 claim had been overtaken. Nothing notices: `/maintain`
marks with a fingerprint the files inside the tree (G1), and the edge check asks only that a
validator's file exists. A rule by file and commit flagged every moved line in the sample whose
change was committed, and missed two in a working tree not yet committed.

Not settled: whether a citation pins a commit, names a symbol instead of a line, or is re-read when
its file changes; whether a done record, a record of what happened, is held at all; and who reads
another repository's history — `/maintain`, a recipient's own audit (DriftSense's q-vxes7i plans the
lapse by file and commit), or neither.

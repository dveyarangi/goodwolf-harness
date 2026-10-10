# edge — rules installed into skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/align/SKILL.md` | `### Challenge against the Edge records` |

## E1 — the records are checked by their maintainer

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-10

<rule>
Check the edge records and their sidecars with `edges.py --check` — format never content, live
records only. A diagnostic is a finding; repair it under the repair policy.
</rule>

## E2 — a record is held to what it names

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-10

<rule>
An edge record is of the code and configuration it names. When the scope moves a file that a
record or a sidecar under `docs/edge/` names in backticks, re-read what it says of that file. A
promise the code no longer keeps is drift, reported with its evidence and never rewritten to fit.
A sidecar's result the move touches is stale: rewrite it `unobserved since <date> — <what moved>`
and name the live check owed; never re-date an observation from the tree.
</rule>

## E3 — a plan is challenged against the edges it touches

- **target** `.agents/skills/align/SKILL.md`
- **authority** the align skill's own text, moved here 2026-10-10

<rule>
When the plan touches an edge — where the system meets those who consume it or extend it — check
that edge's record under `docs/edge/`. A contradiction with its Contract or Invariants is either a
plan bug or a deliberate contract change, and a contract change is named **breaking or
compatible** out loud before proceeding. Update the record inline as decisions land, in the shape
of `.agents/skills/edge/EDGE-FORMAT.md`: contract changes in `Contract` and `Invariants`, a promise
without a validator marked **⚠ unguarded**; newly surfaced edge-scoped concerns as pointers in
`Concerns`; staging shifts in `Roadmap`.
</rule>

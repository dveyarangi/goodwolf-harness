# ticket — rules installed into skills this mechanism does not own

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/plan/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/align/SKILL.md` | `### Record resolutions in the owning ticket inline` |

## P1 — finished is every box checked

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-06

<rule>
A ticket is finished when every acceptance box is checked, the verification box included.
</rule>

## P2 — the pair closes in one invocation

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the install RFC of 2026-09-06, which specified the mover

<rule>
Close a ticket and its RFC together, in one invocation, and every eligible pair in the same
invocation: `move_doc.py [--dry-run] SRC DST [SRC DST ...]`, into `docs/tickets/done/` and
`docs/rfc/done/`.
</rule>

## P3 — the header is the maintainer's

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the install RFC of 2026-09-06, which specified the mover

<rule>
Update the ticket header yourself; the mover changes no checkbox, status, date or prose and
leaves the Git index alone. Treat a refusal as a finding. Repair or deliberately leave what it
reports it cannot rewrite, and say which. Git recovers committed or staged content only.
</rule>

## P5 — the records are checked by their maintainer

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-08

<rule>
Check the ticket records with `tickets.py --check` — format never content, live rows only. A
diagnostic is a finding; repair it under the repair policy.
</rule>

## P6 — an RFC is named by its ticket

- **target** `.agents/skills/plan/SKILL.md`
- **authority** the user, 2026-09-08

<rule>
Name the RFC by the owning ticket's basename, under `docs/rfc/`, with no serial of its own; it
moves to `docs/rfc/done/` with the ticket.
</rule>

## P7 — a resolved decision leaves the ticket for its durable home

- **target** `.agents/skills/align/SKILL.md`
- **authority** the user, 2026-09-08

<rule>
Land a resolved decision in its durable home with its provenance, and rewrite the ticket in
place to what is now true; list under `Open issues` only what stays unresolved.
</rule>

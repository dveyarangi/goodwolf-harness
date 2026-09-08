# mechanism-shape — rules installed into skills this mechanism does not own

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/mechanism/SKILL.md` | `## Records` |

## R1 — records are checked by their maintainer script

- **target** `.agents/skills/maintain/SKILL.md`
- **target** `.agents/skills/mechanism/SKILL.md`
- **authority** the user, 2026-09-07

<rule>
Check a record-bearing mechanism's records with its maintainer script — format never
content, live rows only. Where the script is missing, write it: that is the maintenance.
</rule>

## R2 — a mechanism is compared against what governs it

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-07

<rule>
Compare a mechanism against what governs it with line endings normalised, its evidence
excluded, and installed blocks excluded.
</rule>

## R3 — story leaves the doc

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-07

<rule>
Move story out of a doc into its evidence.
</rule>

## R4 — an index is derived

- **target** `.agents/skills/maintain/SKILL.md`
- **target** `.agents/skills/mechanism/SKILL.md`
- **authority** the user, 2026-09-07

<rule>
Render an index on request; never commit one beside its records.
</rule>

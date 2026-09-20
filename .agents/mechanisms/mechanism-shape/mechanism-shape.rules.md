# mechanism-shape — rules installed into skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/mechanism/SKILL.md` | `## Records` |
| `.agents/skills/align/SKILL.md` | `### Record resolutions in the owning ticket inline` |

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

## R5 — a mechanism's rule reaches the entry file installed

- **target** `.agents/skills/align/SKILL.md`
- **target** `.agents/skills/mechanism/SKILL.md`
- **authority** the user, 2026-09-20

<rule>
Land a mechanism's rule in AGENTS.md only as an installed block from its rules file. While the
mechanism is undeclared, write the rule by hand and wrap it as a straw dog on the inception
ticket as you write it.
</rule>

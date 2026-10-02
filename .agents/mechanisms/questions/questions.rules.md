# questions — rules installed into the entry file and skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## General rules` |
| `.agents/skills/recall/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/conclude/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

## Q1 — every message is placed before it is answered

- **target** `AGENTS.md`
- **authority** the user, 2026-09-28 to 2026-10-02 — 01-0011.0100 decisions 32, 39, 44 and 45

<rule>
Before drafting a reply, place the message in the question store: read this turn's window — the
one the host's hook put in your context, or `questions.py --window --session <tag>` — and declare
where the message lands with `questions.py --declare "<line>" --session <tag>`, again whenever
the turn's own work settles, opens or moves a question:

- `at q-0004`
- `at q-0014; opens q-0014 under q-0004: <question>`
- `at q-0002; closes q-0004: decided, [link](../path.md)`
- `nothing`

A message that answers nothing near the current question opens what that question cannot be
answered without. Only the working agent declares, never a helper. Under `debug=on`, show each
declared line where it happened. For any other form, a closure, a branching or a drop, read the
questions skill.
</rule>

## Q2 — the wake opens at where the work stands

- **target** `.agents/skills/recall/SKILL.md`
- **authority** the user, 2026-09-29 and 2026-10-02 — 01-0011.0100 decisions 38, 39 and 44

<rule>
Start from the wake's read — the one the host's session-start hook put in your context, or
`questions.py --wake`. Report where the other sessions stand, what is suspect, and which
deferrals may now be due; take this session's position from the person or estimate it, and
declare it. Re-rank nothing another running session is on; then read the queue as this skill says.
</rule>

## Q3 — the conclude writes the leans and ends the session

- **target** `.agents/skills/conclude/SKILL.md`
- **authority** the user, 2026-09-29 — 01-0011.0100 decision 38

<rule>
Write a lean line on each question the session touched and left open — `leans q-N: <line>`, in
a declared line with its `at` — and nothing else: placements and closures were written as they
happened. As the conclude's last act, run `questions.py --end --session <tag>`.
</rule>

## Q4 — the store is checked, and finished subtrees archived

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-29 — 01-0011.0100.0010 RFC item 4, for M1's duty

<rule>
Check the question store with `questions.py --check`. A diagnostic is a finding; repair it under
the repair policy. Move each subtree it reports ready for `done/` with `move_doc.py`, every entry
of the subtree in one invocation, into `docs/questions/done/`; ids are unchanged.
</rule>

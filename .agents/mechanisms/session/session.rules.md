# session — rules installed into skills and the entry file

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/recall/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/conclude/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |
| `AGENTS.md` | `## General rules` |
| `.agents/skills/commit/SKILL.md` | `- Write the subject in the project's own convention, where it states one.` |

## S1 — the wake opens at where the sessions stand

- **target** `.agents/skills/recall/SKILL.md`
- **authority** the user, 2026-09-29 to 2026-10-04, as the questions mechanism's Q2; the session's since 2026-10-22

<rule>
Start from the wake's read — the one the host's session-start hook put in your context, or
`questions.py --wake --session <tag>` with the tag that read named; a bare `--wake` registers a new
session, and is for a host whose hook registered none. Take from it where the other sessions
stand, and re-rank nothing another running session is on.
</rule>

## S2 — the conclude ends the session

- **target** `.agents/skills/conclude/SKILL.md`
- **authority** the user, 2026-09-29 and 2026-10-03, as the questions mechanism's Q3; the session's since 2026-10-22

<rule>
As the conclude's last act, run `sessions.py --end --session <tag>`.
</rule>

## S3 — the maintain pass keeps the rows

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-15, as `/maintain`'s F5; the check and the removal, 2026-10-22

<rule>
Check the rows with `sessions.py --check`; a diagnostic is a finding, repaired at the rung of what
it mends. Commit with the pass each row a wake ended or removed in another session's file under
`docs/sessions/rows/`; a file whose row reads `running` stays out.
</rule>

## S4 — a reply shows the sessions it runs beside

- **target** `AGENTS.md`
- **when** debug=on
- **authority** the user, 2026-10-14 to 2026-10-20, in the reply's layout; the session's since 2026-10-22

<rule>
One party's work or claim colliding with another's — another session standing
where this one works — met and not resolved, is a row under `| 🪢 Tangle |`, even where a record's
disagreement is what shows it. The 🪢 table's header lists every running session's question, this
one's included, on one line, each by its id alone, linked to its entry, `—` for a session with no
position; each collision is a row under it, naming the sessions it involves. The table stands
whenever another session runs: its header is enough, with no collision under it, and it opens the
reply.
</rule>

## S6 — every conversation starts with its recall

- **target** `AGENTS.md`
- **authority** the user, 2026-09-20, the first core rule to leave the pacer page; a resumed conversation the same session, 2026-10-09; the session's since 2026-10-23

<rule>
Run `/recall` first in every conversation, whatever the first message says. A conversation the host
resumes under a new id is the same conversation: its context holds the recall it ran.
</rule>

## S5 — a commit holds one session's work

- **target** `.agents/skills/commit/SKILL.md`
- **authority** in /commit since 2026-09-07; the session's since 2026-10-22

<rule>
Commit the work of the current session only: another session's changes may be its work in
progress, and in doubt ask the person.
</rule>

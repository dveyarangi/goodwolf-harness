# debugging — rules installed into the entry file

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## General rules` |

| setting | values | default | set by |
|---|---|---|---|
| `debug` | `on` · `off` | `off` | a wording |

## D1 — a session announces the contract it read

- **target** `AGENTS.md`
- **when** debug=on
- **authority** the user, 2026-09-06, the announce line at the entry file's head since v2; here since 2026-10-23

<rule>
Open your first reply of every session with the entry file's `Entry contract:` line, verbatim.
</rule>

# local — this project's rules, installed into core

Machine input for the installer, read by nobody at session time: what this repository answers
and overrides, in the grammar a mechanism's rules file uses. Amend a rule here, then install it
with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## Project-local` |
| `.agents/skills/verify/SKILL.md` | `## The verification set` |

## L1 — what this repository is

- **target** `AGENTS.md`
- **authority** the user, 2026-09-07 and 2026-09-20

<rule>
This repository develops the shared dev harness using its own loop; its own architecture and
progress live in docs/ like any other project's — the instance half doing its job, not a leak.
Terms: docs/glossary.md, this project's own; the method's are .agents/glossary.md's. What each
version of the entry contract changed: docs/research/entry-contract-findings.md.
</rule>

## L2 — the switches

- **target** `AGENTS.md`
- **authority** the user, 2026-09-05; commit to auto, the user, 2026-10-05; push to auto, the user,
  2026-10-10

<rule>
commit=auto · push=auto · next-cycle=ask · breakdown=ask · repair=report
</rule>

## L4 — the working is shown

- **target** `AGENTS.md`
- **authority** the user, 2026-09-29

<rule>
debug=on
</rule>

## L5 — how Python runs here

- **target** `AGENTS.md`
- **authority** the user, 2026-10-03

<rule>
Run a Python script with `uv run --offline --no-project python <script>`.
</rule>

## L6 — the glyphs are anchors

- **target** `AGENTS.md`
- **authority** the user, 2026-10-07
- **overrides** `questions/Q1`

<rule>
In this tree the table's glyphs are emoji — `📍` for the question the turn ends on, `🌱` for one
opened in it, `✅` for one closed in it, `⚙️` for a process, `🧭` for an uncharted ask, `🐺` for
banter — so a row reads `| 📍 **q-N** · <question> |`, `| 🌱 **q-N** · <question> |`,
`| ✅ **q-N** · <question> (<kind>: <its answer>) |`, `| ⚙️ **<process>** · <its scope> |`,
`| 🧭 **uncharted** · <the question> |`, `| 🐺 **banter** |`. A glyph is an anchor for the
reader's thinking — people think largely in pictures — and the wolf is goodwolf-harness's own.
</rule>

## L7 — a rule here is not copied to the host's memory

- **target** `AGENTS.md`
- **authority** the user, 2026-10-08

<rule>
A correction that lands as a rule in this tree is not also written to the host's own memory
store outside the repository — Claude Code's auto-memory directory and its kin; that store holds
only what no record in this tree carries.
</rule>

## L3 — the verification set

- **target** `.agents/skills/verify/SKILL.md`
- **authority** the user, 2026-09-05

<rule>
The verification set:

```
uv run --offline --no-project python -m unittest discover -s .agents/scripts/gw/test -p "test_*.py"
uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --check
uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --check
uv run --offline --no-project python .agents/scripts/gw/tickets.py --check
uv run --offline --no-project python .agents/scripts/gw/maintain.py --check
uv run --offline --no-project python .agents/scripts/gw/questions.py --check
```
</rule>

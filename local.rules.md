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
- **authority** the user, 2026-09-05; commit to auto, the user, 2026-10-05

<rule>
commit=auto · push=ask · next-cycle=ask · breakdown=ask · repair=report
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

## L6 — the rows carry the wolf and the gear

- **target** `AGENTS.md`
- **authority** the user, 2026-10-07
- **overrides** `questions/Q1`

<rule>
In this tree the banter row reads `| 🐺 **banter** |` and the process row `| ⚙️ **<process>** · <its scope> |`:
the wolf is goodwolf-harness's own, and decoration matters here.
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

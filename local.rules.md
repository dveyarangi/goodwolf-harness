# local — this project's rules, installed into core

Machine input for the installer, read by nobody at session time: what this repository answers
and overrides, in the grammar a mechanism's rules file uses. Amend a rule here, then install it
with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## Project-local` |
| `.agents/skills/verify/SKILL.md` | `## The verification set` |
| `.agents/skills/implement/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/maintain/SKILL.md` | `## Finish` |
| `.agents/skills/commit/SKILL.md` | `- Write the subject in the project's own convention, where it states one.` |
| `.agents/skills/skill-up/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/mechanism/SKILL.md` | `## Siblings` |
| `.agents/skills/*/SKILL.md` | `## What the person hears` |

| setting | value |
|---|---|
| `debug` | `on` |

## L1 — what this repository is

- **target** `AGENTS.md`
- **authority** the user, 2026-09-07 and 2026-09-20

<rule>
This repository develops the shared dev harness using its own loop; its own architecture and
progress live in docs/ like any other project's — the instance half doing its job, not a leak.
Terms: docs/glossary.md, this project's own; the method's are .agents/glossary.md's. What each
version of the entry contract changed: docs/research/entry-contract-findings.md.
</rule>

## L2 — the dials

- **target** `AGENTS.md`
- **authority** the user, 2026-10-15, word for word, the switches of 2026-09-05 to 2026-10-10
  given way to the dial

<rule>
development=a feature · self-improvement=a rule. Push each commit as it lands.
</rule>

## L5 — how Python runs here

- **target** `AGENTS.md`
- **authority** the user, 2026-10-03

<rule>
Run a Python script with `uv run --offline --no-project python <script>`.
</rule>

## L7 — a rule here is not copied to the host's memory

- **target** `AGENTS.md`
- **authority** the user, 2026-10-08

<rule>
A correction that lands as a rule in this tree is not also written to the host's own memory
store outside the repository — Claude Code's auto-memory directory and its kin; that store holds
only what no record in this tree carries.
</rule>

## L8 — a commit is named by the step that made it

- **target** `.agents/skills/commit/SKILL.md`
- **authority** in /commit since 2026-09-07; a closed list and the project's own, the user,
  2026-10-11

<rule>
Prefix the subject with the loop step that produced the work, uppercase, then a colon — one of
these and no other: `ALIGN`, `TICKET`, `PLAN`, `IMPLEMENT`, `VERIFY`, `MAINTAIN`,
`DISCOVER`, `RECALL`, `CONCLUDE`; outside the ring, `FIX` for a repair taken on its own, `EQUIP`
for a change to the harness's own installation, `DREAM` for a record the second lobe wrote. A
name for what the commit touched — the entry file, the local rules, the question store, an RFC —
is not a step: a rule landed at an align is `ALIGN`, a question opened while planning is `PLAN`.
One prefix per commit; where the work spans two steps, take the dominant one and name the bleed in
the message.
</rule>

<straw-dog question="q-0037.0006.0027">
## L9 — the voice

- **target** `AGENTS.md`
- **target** `.agents/skills/*/SKILL.md`
- **authority** the user, 2026-10-14; the voice its name alone and the language of the message,
  2026-10-25

<rule>
Speak the way Lem wrote, in the language of the person's message. It invents nothing: what it
tells is what happened. Tables, decisions and text proposed for a record keep the exactness their
forms ask.
</rule>
</straw-dog>

<straw-dog question="q-0037.0006.0022.0001">
## L3 — the verification set

- **target** `.agents/skills/verify/SKILL.md`
- **target** `.agents/skills/implement/SKILL.md`
- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-09-05; the tests by what changed, 2026-10-11; in every skill that
  runs it, 2026-10-11; the product check once the document carried its ids, 2026-10-13

<rule>
The verification set: the checks always; the tests too when the work changed a file that is not
markdown, the question store's own writes aside.

```
uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --check
uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --check
uv run --offline --no-project python .agents/scripts/gw/tickets.py --check
uv run --offline --no-project python .agents/scripts/gw/edges.py --check
uv run --offline --no-project python .agents/scripts/gw/maintain.py --check
uv run --offline --no-project python .agents/scripts/gw/questions.py --check
uv run --offline --no-project python .agents/scripts/gw/sessions.py --check
uv run --offline --no-project python .agents/scripts/gw/product.py --check
```

```
uv run --offline --no-project python -m unittest discover -s .agents/scripts/gw/test -p "test_*.py"
```
</rule>
</straw-dog>

## L12 — the cap on work in hand

- **target** `AGENTS.md`
- **authority** the user, 2026-10-22: eight on trial, to be re-read by what it stops; a session counts in the
  ring alone, 2026-10-23

<rule>
At most 8 open questions are in work at once — a running session in the ring on one or under it, or
its owner ticket In progress. The ninth is opened and placed, and waits until one leaves work.
</rule>

## L10 — what core names under docs/

- **target** `.agents/skills/skill-up/SKILL.md`
- **target** `.agents/skills/mechanism/SKILL.md`
- **target** `.agents/skills/implement/SKILL.md`
- **authority** the user, 2026-10-19: the core half of the entry file's former *Core and instance*,
  read only by whoever writes core, which is written here alone

<rule>
What the harness ships names under `docs/` only where a mechanism keeps a kind of record — the
directory, or the one file that is a record — never a record inside one; a question only as a
straw dog's binding or a `TODO q-N`; a ticket never.
</rule>

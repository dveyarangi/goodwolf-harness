# local — this project's rules, installed into core

| target | anchor |
|---|---|
| `AGENTS.md` | `## Project-local` |
| `.agents/skills/verify/SKILL.md` | `## The verification set` |

## L1 — what this project is

- **target** `AGENTS.md`
- **authority** the person, 2026-10-15

<rule>
codename_japaka: an empty project; what it is for is its first open question, q-0001.
</rule>

## L2 — the dials and git

- **target** `AGENTS.md`
- **authority** the person, 2026-10-15

<rule>
development=a feature · self-improvement=a rule. Finished work stays on this computer: commit to
main, never push.
</rule>

## L3 — the verification set

- **target** `.agents/skills/verify/SKILL.md`
- **authority** the person, 2026-10-15

<rule>
The project has no toolchain of its own yet, so no checks of its own. The harness's checks of the
records the method keeps:

```
py -3 .agents/scripts/gw/tickets.py --check
py -3 .agents/scripts/gw/questions.py --check
py -3 .agents/scripts/gw/edges.py --check
py -3 .agents/scripts/gw/product.py --check
py -3 .agents/scripts/gw/maintain.py --check
```
</rule>

## L4 — Python

- **target** `AGENTS.md`
- **authority** the machine, 2026-10-15

<rule>
Run a Python script with `py -3 <script>`; `python` is not on this machine's PATH.
</rule>

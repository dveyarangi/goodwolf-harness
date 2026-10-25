---
name: implement
description: Use when agreed work is to be written into code.
---

<straw-dog question="q-0037.0009.0011">Mechanism: not yet</straw-dog>

Implement the work described by the relevant architecture decisions (the
question, ticket, RFC, prior discussion).

Pick entity names in vibe with the project glossary.
Do not use implementation-shaped names or parameters; orient them at the
function's meaning toward the client.

Use `/tdd` where possible, at pre-agreed seams. Make sure implementation, even
in dummy/degenerate form, fully follows contract surfaces in the docs.

Make methods behind main architectural boundaries clear — they should read
almost as a story explaining the boundary logic, with separate concerns
extracted to properly named sub-methods. Prefer to split submethods by
responsibility.

The code should read as a story. Make sure the main process appears first in
the file, where possible, and main boundaries' implementation reads through
entities, interfaces and submethods used as nouns, adjectives and verbs.

Mark code an open question's answer will change with a comment line beginning
`TODO` that names the question, per the entry file's straw-dog rule, and say so
in the docstring.

<straw-dog question="q-0037.0009.0011">
Where the code you write follows a rule that a load-bearing record of the project states — its
architecture or an ADR — name each such rule at the end of the comment phrase it backs, as
`(<path from the tree's root>: "<the rule's name>")`, whole on one line — wrap the comment before
it, never inside it — the name being the rule's heading or the bold lead of its paragraph, word for
word. A rule with no such name gets one in its record first. Code no such rule governs carries no
pointer.
</straw-dog>

Make sure the errors follow error rules.

Make sure to read and follow `/improve-comments` rules. Mark other pending
actions — hotpaths that may need optimization, work with no named successor —
as `TODO` too; without a ticket they are notes, and the listing script reports
them as guesses.

During the work, run the checks in the project's verification set, as
[`/verify`](../verify/SKILL.md#the-verification-set) defines it. `/verify` is the
verification of landed work; a local run of a subset is not that pass.

Once done, and unless you need to take a break, use `/verify`.

Commit once `/verify` has passed on the work. Mending during the work stands
on the rung of what it mends; it is not a substitute for `/verify`.

## Installed from other mechanisms

<installed by="session">
**S7** At the step's start, hold the unit by the question its work answers, `sessions.py --hold <q-id>
--session <tag>`; a unit this session held is let go by it: say which, and that it is nobody's
now. A refusal naming another running session stops the step: say whose the unit is, and do
nothing on it. A refusal saying the question is no unit leaves the step to go on, holding
nothing.
</installed>

<installed by="local">
**L3** The verification set: the checks always; the tests too when the work changed a file that is not
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

**L10** What the harness ships names under `docs/` only where a mechanism keeps a kind of record — the
directory, or the one file that is a record — never a record inside one; a question only as a
straw dog's binding or a `TODO q-N`; a ticket never.
</installed>

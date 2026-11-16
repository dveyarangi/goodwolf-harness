# practice — rules installed into skills

How a project writes its code, its tests and its comments, installed into the steps of delivery
that read it. A project with a practice of its own overrides a rule from its local rules file.

| target | anchor |
|---|---|
| `.agents/skills/plan/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/implement/SKILL.md` | `## Installed from other mechanisms` |
| `.agents/skills/verify/SKILL.md` | `## Installed from other mechanisms` |

## T1 — a plan presents the code's shapes and flows

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Present main code shapes - especially ones that represent documented boundaries. Present code
flows.
</rule>

## T2 — a plan's stages keep the tests green

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Allocate the implementation stages according to `/tdd` rules. Look at stages to make sure each of
them keeps the tests green; in case that would take too much temporary effort, allow red, note
about test status and compact reason for it.
</rule>

## T18 — a plan leaves local choices to the tests too

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Leave reversible implementation-local choices to `/tdd` as well as to `/implement`, unless they
become load-bearing.
</rule>

## T3 — a planned test proves its reason

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
On every adversarial validation pass over the RFC, make every planned test prove the intended
behavior and failure reason, not merely that the path succeeds or raises.
</rule>

## T4 — no public method the architecture lacks

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Do not expose public methods or create flows that are not in architecture.
</rule>

## T5 — temporary code is flagged

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
If planned code includes a temporary solution that is dissolved by future development, add RFC
instruction to append TODO comment to code that flags this. Otherwise code changes can start
relying or considering the temporal code, which can be hard to disentangle later.
</rule>

## T6 — code shapes for reuse

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Overall, always consider future development and potential code reuse when selecting code shapes.
</rule>

## T7 — what shipping software asks of a plan

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
Cover migrations, compatibility, rollout, failure handling, and observability when relevant.
</rule>

## T8 — planning leaves the code alone

- **target** `.agents/skills/plan/SKILL.md`
- **authority** `/plan`'s own text, moved here on the user's word, 2026-11-16

<rule>
DO NOT CHANGE THE CODE!
</rule>

## T9 — names face the client

- **target** `.agents/skills/implement/SKILL.md`
- **authority** `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Pick entity names in vibe with the project glossary. Do not use implementation-shaped names or
parameters; orient them at the function's meaning toward the client.
</rule>

## T10 — tests first, at agreed seams

- **target** `.agents/skills/implement/SKILL.md`
- **authority** `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Use `/tdd` where possible, at pre-agreed seams. Make sure implementation, even in
dummy/degenerate form, fully follows contract surfaces in the docs.
</rule>

## T11 — code reads as a story

- **target** `.agents/skills/implement/SKILL.md`
- **authority** `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Make methods behind main architectural boundaries clear — they should read almost as a story
explaining the boundary logic, with separate concerns extracted to properly named sub-methods.
Prefer to split submethods by responsibility.

The code should read as a story. Make sure the main process appears first in the file, where
possible, and main boundaries' implementation reads through entities, interfaces and submethods
used as nouns, adjectives and verbs.
</rule>

## T12 — code an open question will change is marked

- **target** `.agents/skills/implement/SKILL.md`
- **authority** `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Mark code an open question's answer will change with a comment line beginning `TODO` that names
the question, per the entry file's straw-dog rule, and say so in the docstring.
</rule>

## T13 — code names the architecture rule it follows

- **target** `.agents/skills/implement/SKILL.md`
- **authority** the user, 2026-10-12, at q-rlms4p; `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Where the code you write follows a rule that a load-bearing record of the project states — its
architecture or an ADR — name each such rule at the end of the comment phrase it backs, as
`(<path from the tree's root>: "<the rule's name>")`, whole on one line — wrap the comment before
it, never inside it — the name being the rule's heading or the bold lead of its paragraph, word for
word. A rule with no such name gets one in its record first. Code no such rule governs carries no
pointer.
</rule>

## T14 — errors and comments follow their rules

- **target** `.agents/skills/implement/SKILL.md`
- **authority** `/implement`'s own text, moved here on the user's word, 2026-11-16

<rule>
Make sure the errors follow error rules.

Make sure to read and follow `/improve-comments` rules. Mark other pending actions — hotpaths that
may need optimization, work with no named successor — as `TODO` too; without a ticket they are
notes, and the listing script reports them as guesses.
</rule>

## T15 — a fixture is built the way the thing came to be

- **target** `.agents/skills/verify/SKILL.md`
- **authority** `/verify`'s own text, moved here on the user's word, 2026-11-16

<rule>
Checking named validators: a promise about something that already exists — a recipient's tree, a stored record — is asserted
only by a fixture built the way that thing came to be: one the code under test made cannot hold a
shape that code now refuses, or lack a file that code now ships.
</rule>

## T16 — comments in scope are reviewed

- **target** `.agents/skills/verify/SKILL.md`
- **authority** `/verify`'s own text, moved here on the user's word, 2026-11-16

<rule>
Docstrings say what their own unit does. Apply `/improve-comments` to comments in scope and check
that TODO tags still describe something pending.
</rule>

## T17 — a code pointer resolves

- **target** `.agents/skills/verify/SKILL.md`
- **authority** the user, 2026-10-12, at q-rlms4p; `/verify`'s own text, moved here on the user's word, 2026-11-16

<rule>
Read the pointers in the slice's code: each names, word for word, a heading or a bold lead that
the record it points into holds. One that does not is a finding.
</rule>

# Mechanism format

This shelf owns the mechanism directory, the doc's sections, the two tables a script
parses, and the record shape of the mechanism set itself. What a mechanism *is*, and
how one is incepted, amended or retired, is [/mechanism](./SKILL.md)'s.

## Directory

```
.agents/mechanisms/<slug>/
    <slug>.md          the doc — required, exactly one
    <slug>.rules.md    the rules file — only if the mechanism injects
```

The slug is the directory name, lowercase and hyphenated; every filename repeats it.

## The doc

```md
# <slug> — <what it is, in one line>

- **instruction** `<path>` — what it holds
- **state** always on
- **rules** `<path>`
<project-local>
- **evidence** `<path>`
- **declared by** `<ticket path>`
</project-local>

## How it works

## Moments

## Install adds, uninstall removes

## Relies on, and does not own

## Not yet at the shape

## What retires this

## What would show it working, graded by someone who did not build it
```

Sections appear in this order. All but the two tables are prose and are never parsed —
but a doc missing the grading section is a diagnostic: a mechanism that names no
grader has been labelled, not declared.

### Header bullets

- **instruction** — backticked repo-relative path to the mechanism's one skill.
  Required, and never the doc itself.
- **state** — `always on` or `installed`. `always on` means nothing can install or
  uninstall it, so it has no lifecycle scripts and that absence is a property.
- **rules** — the rules file. Omitted by a mechanism that injects nothing.
- **evidence** and **declared by** sit in the `<project-local>` block, which a
  recipient replaces, and **both are optional**. An absent **declared by** disables the
  diagnostic that reads it, and the check reports that skip rather than passing
  quietly.

## Moments

```md
| moment | instructed by | kind, and why |
```

- **moment** — the occasion, in the words a person would use for it.
- **instructed by** — a backticked path, or `—`.
- **kind, and why** — empty when the row is instructed. Otherwise one of `elsewhere`,
  `embedded`, `unowned by design`, `not yet`, a clause saying why, and — for all but
  `unowned by design` — its referent.

A row carries an instruction or an absence, never both and never neither. A `not yet`
referent is a **markdown link** to a ticket that exists, and never the ticket the
doc's **declared by** names.

## The two tables

```md
| part | where |                 under "Install adds, uninstall removes"
| part | where | owner |         under "Relies on, and does not own"
```

The first title is its definition: **if uninstalling would not remove it, it is not a
part**. For an `always on` mechanism the same table is what a person moving it between
trees takes.

Relied-on parts never become an owner column on the first table — they are not added
by install, so listing them there contradicts its title.

**part** is a role name and may repeat. **where** is a backticked repo-relative path,
optionally with an anchor:

```
`AGENTS.md` → "is mechanism work: use"
```

The phrase after `→` is checked as a verbatim substring of the file named. Use one
wherever the part is a line inside a shared file, or the line is deletable with the
check still green. Interim, until injection ships.

## Parsing

- Cells split on unescaped `|`; a literal pipe is `\|`.
- A row whose cell count differs from its header is a diagnostic, not a silent
  misparse.
- Every path is backticked and repo-relative, **except** a `not yet` referent, which is
  a markdown link so moving its ticket repairs it.
- Prose, the taxonomy's correctness, and whether a moment should exist are judgment. A
  script records them and rules on none of them.

## The mechanism set is its own register

No file holds the register. `.agents/mechanisms/<slug>/` is the enumeration, and the
index is rendered from the directories on request.

- **A record** is one mechanism directory; its fields are the header bullets above and
  its shape is this document.
- **Tier 2** — read when installing, amending or debugging a mechanism.
- **What removes an entry**: the mechanism being retired. A directory that outlives its
  mechanism is drift.
- **The index is derived and never committed.** A doc edit shows on the next render; a
  doc that cannot be parsed is reported rather than dropped.

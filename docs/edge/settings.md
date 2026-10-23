# Edge — Settings

- **Status:** Normative (tentative)

## Contract

A **setting** is a knob a mechanism declares — its name, its values, its default, who may set
it — and a project sets in its local file; a rule of any installed mechanism may be installed only
while a setting holds a value, so a tree carries the method's text its settings call for and no
more ([the format shelf](../../.agents/skills/mechanism/MECHANISM-FORMAT.md), *The rules file*;
[architecture](../architecture.md), *Installed blocks*). The agent is the interface to a tree's
settings, never the file ([product](../product.md), G3).

**Promised to whoever configures a tree:**

- every setting the tree has — its values, its default, the tree's value, who may set it, which
  mechanism declares it — in one table, rendered on request by
  `inject_rules.py --settings` and shown by the agent when a setting is changed or the harness's
  set-up is asked about; the table is never committed;
- a change by one call, `inject_rules.py --set <setting>=<value>`, which refuses an unknown name
  or value before writing, writes the local file's row, runs the installer and reports what the
  tree now carries;
- a setting the local file leaves unset standing at its default;
- a hand edit of the local file, allowed and rare, brought to match by the next session before its
  first reply, which says so.

**Required of a setting:** declared once, by the mechanism it belongs to, in its rules file;
set only in the project's local file; its `set by` a rung of a ladder, read by the dial as every
decision is, or the person — **⚠ pending — 01-0010.0125**: the host refuses an agent's change of a
person's setting as it refuses a dial edit<straw-dog question="q-0037.0006.0005">; until then the
rule stands in the agent's hands</straw-dog>.

## Invariants

- A rule conditioned on a setting is installed while the tree's value satisfies it and absent
  otherwise, and a changed value moves it both ways without `--overwrite` — *validated by:*
  `.agents/scripts/gw/test/test_inject_rules.py`, the settings cases
- A condition or a local value naming an undeclared setting or value is refused and writes
  nothing, and a block out of step with the settings is a diagnostic of the check — *validated
  by:* `.agents/scripts/gw/test/test_inject_rules.py`
- The settings table is rendered on request and never committed — *validated by:*
  `.agents/scripts/gw/test/test_inject_rules.py`, the `--settings` case
- A tree whose installed blocks are out of step with its rules files and settings is told so at a
  session's start — *validated by:* `.agents/scripts/gw/test/test_harness.py`, the wrapper's
  notice case

## Concerns

- [q-0037.0010.0002.0005](../questions/q-0037.0010.0002.0005-what-does-the-practice-mechanism-own.md)
  — the dial as a setting waits on the ladder mechanisms' declaring it; until then the dial is
  set as L2 and not through the table.

## Roadmap

- The dial's two rows in the table, once a ladder's mechanism declares them —
  [q-0037.0010.0002.0005](../questions/q-0037.0010.0002.0005-what-does-the-practice-mechanism-own.md),
  deferred from [01-0010.0220](../tickets/done/01-0010.0220-a-tree-carries-the-methods-text-its-settings-call-for.md).
- The rest of what debug shows moving into debugging's conditioned rules —
  [01-0016.0020](../tickets/01-0016.0020-what-debug-shows-is-installed-not-read.md).
- The host refusing an agent's change of a person's setting —
  [01-0010.0125](../tickets/01-0010.0125-the-host-blocks-what-a-rule-forbids.md).

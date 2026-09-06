---
name: maintain
description: >-
  Use to maintain a declared scope of the tree — its rules, contracts, records,
  links and comments — and to complete a paired ticket+RFC close once its work
  is verified. Enumerates `<temporary>` statements and archives finished records.
---

One integrated pass over a declared scope. Which checks apply is decided by the scope,
not by a menu: a narrow close still uses every governing rule that reaches it.

## Declare the scope first

- Say what is being maintained: the whole tree, a project, or the work owned by one
  ticket and RFC. Write the declared scope into the pass's report.
- A scope is the work and its dependencies, not a list of filenames. Pull in the
  consumers and governing documents needed to check the obligations you found.
- A narrow pass cannot certify the rest of the tree. Findings outside the scope stay
  visible with an owner; they do not disappear and they do not silently widen the pass.
- Do not start a whole-tree pass because a narrow one was asked for.

## Identify

- Derive the applicable rules, artifacts and dependencies from AGENTS.md/CLAUDE.md,
  [the process](../../../docs/process.md#tree-maintenance) and
  [the architecture](../../../docs/architecture.md), not from memory.
- List the mechanisms in scope: instructions, producers, consumers, checks and records.
  A mechanism is maintained whole — installing updated instructions does not establish
  that their derived work is current.
- Read the [glossary](../../../docs/glossary.md) before renaming anything.

## Check and repair

- Cross-check documents against each other and against code, in both directions.
  Ask whether the implementation contract could be reconstructed from the architecture
  alone; a load-bearing decision visible only in code is a documentation finding.
- Code that contradicts an accepted decision is a code finding. Do not settle a
  contradiction by weakening the rule.
- Check named validators still exist and still assert the promise they were named for.
  A missing or drifted validator is a finding, as is an unguarded normative promise.
- Sweep the concern index for entries in scope: a concern the implementation has since
  answered belongs in its owning record, and a dead trigger retires.
- Apply [repair-and-report](../../../docs/process.md#autonomy-and-repair) where it holds:
  make the repair, verify it, and record the violated rule, the change, the verification
  result and any remaining uncertainty in the owning work item.
- Everything else goes to [/align](../align/SKILL.md): a missing, ambiguous or
  contradictory rule, a new foundational decision, or work beyond the authorization.
  Pause that change; independently authorized work continues.
- Anything that can be maintained mechanically must be. If the script is missing, write
  it — a missing script is work to do, not an excuse to leave the repair outstanding.

## Clean up prose and records

- One canonical home per fact. Elsewhere, replace the restatement with a pointer.
  A higher-level summary that points at deeper detail is not a duplicate.
- After a decision settles, state what is true now. Remove superseded paths and
  completed migration notes; keep a rejection only when it is load-bearing.
- Tickets, RFCs and sessions are historical records and may carry duplicate context.
  Their indexes may not. Core documents do not cite them for architecture.
- Docstrings say what their own unit does. Apply
  [/improve-comments](../improve-comments/SKILL.md) to comments in scope and check
  that TODO tags still describe something pending.
- Historical repairs preserve the facts being recorded. Never invent a past fact, and
  never imply a newly introduced requirement was met at the time.

## Resolve temporary statements

- Enumerate them; do not grep by eye:

  ```
  uv run --offline --no-project python .agents/scripts/temporary_statements.py docs AGENTS.md
  ```

- The tool reports each block's condition and owning ticket as written, plus diagnostics
  for a statement bound to no ticket, carrying no condition, naming an owner that is not
  there, or malformed. Any diagnostic fails the run. Zero statements is a clean result.
- You decide whether a condition holds, from observable evidence — the tool never
  interprets an `until` phrase and never executes one. An unresolved condition stays
  unresolved and is reported.
- Before removing a statement, rehome anything inside it that outlives it. Then:

  ```
  uv run --offline --no-project python .agents/scripts/temporary_statements.py \
      --remove docs/process.md:3 --expect sha256:...
  ```

- A statement holding a nested statement is refused. Dispose of the children first and
  scan again — the earlier fingerprint authorizes nothing after a change.
- Removing the block leaves a hole. Write what is then true in its place.

## Archive what is finished

- Eligibility is yours, not the script's. A ticket moves only when every acceptance box
  is checked, including `/verify`, per
  [TICKET-FORMAT](../ticket/TICKET-FORMAT.md#one-basename-per-work-item). A ticket and
  its RFC close together, in one invocation, so each cites the other's final home.
- Before archiving a spec, establish that its surviving agreements have maintained homes,
  its obligations have explicit dispositions, and its unresolved issues keep active owners.
- Preview, then close:

  ```
  uv run --offline --no-project python .agents/scripts/move_doc.py --dry-run \
      docs/tickets/RR-NNNN-slug.md docs/tickets/done/RR-NNNN-slug.md \
      docs/rfc/RR-NNNN-slug.md docs/rfc/done/RR-NNNN-slug.md
  ```

- The mover repairs citations, including those in historical records, and leaves the Git
  index alone. It changes no checkbox, status, date or prose — you update the ticket
  header and the queue row yourself, in the same pass.
- A refusal is a finding: read it, fix the cause, run again. Nothing was written.
- A run that stops partway leaves the tree half-changed on purpose. Inspect the actual
  files against the reported completed and pending operations and finish the close under
  the repair policy; after an abrupt termination check the failed operation on disk too.
  Git recovers committed or staged content only. Do not report a close you did not finish.
- Mentions the mover reports but cannot rewrite — an HTML `href`, a bare filename in
  prose — are yours to repair or to leave deliberately, and to say which.

## Finish

- Run the checks in the project's
  [verification set](../../../docs/process.md#verification) that the scope touched.
- Report: the declared scope, what was checked, what was repaired and against which rule,
  what moved, what remains open and who owns it. Say what you did not cover.
- Read `commit` and `push` in [AGENTS.md](../../../AGENTS.md) before staging anything.
  A maintenance pass is not a commit permission.
- `/maintain` is not `/verify`. Verification of landed work is
  [/verify](../verify/SKILL.md)'s pass, and a close needs it to have already happened.

The mechanism's own history is in
[maintenance evidence](../../../docs/research/maintenance-findings.md); ordinary use does
not need it.

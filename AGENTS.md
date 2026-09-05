# Session entry

Entry contract: v1, 2026-09-05. Open your first reply of every session with this line, verbatim.

## The loop

Two rings, joined at /align.

    session:   wake with /recall → /align → /conclude → (next session)
    delivery:  /ticket → /plan → /implement → /verify → /maintain → /ticket

/align opens the delivery ring and is where it returns whenever a decision is needed:
/plan when the governing docs contradict, /verify when a finding needs one, /maintain when
maintenance surfaces one. /ticket⇄/plan and /implement⇄/verify iterate as pairs.

Called from inside the rings, not stages: /impact (from /align, /ticket, /plan: sizes the
work and says whether the outcome is a spec, a ticket, an RFC, or a re-slice), /spec (from
/align, when /impact says so). /dream is optional, runs after /conclude, and writes dreams
that /maintain and /align may pick up; it never amends rules.

Human checkpoints: every decision at /align; spec accepted; breakdown approved; commit; push;
next cycle at /maintain → /ticket.

Do not reopen an accepted decision without new evidence.

## Autonomy

The project sets each switch in its local block below; skills defer to those values.

| Switch | Meaning |
|---|---|
| commit | `ask`: commit only on explicit permission, per change. `auto`: commit when the work is verified. |
| push | `ask`: separate from commit, per push. `never`, `auto`. |
| next-cycle | `ask`: starting the next ticket after one lands needs a nod. `auto`. |
| breakdown | `ask`: a /ticket split needs approval before minting. `auto`. |
| repair | `report`: a clear violation of an explicit rule inside authorized work is fixed and reported. `ask`: show it first. |

## Temporary statements

A statement that expires is wrapped in `<temporary until="condition">`, anywhere: in a local block,
a skill body, a doc. The condition is testable: a file exists, a skill is installed, a ticket is
done. Follow it like any rule until you can see the condition is met; then act on reality, report
the stale block, and do not treat the contradiction as a violation. /maintain enumerates every
`<temporary>` in scope and removes the ones whose condition holds.

<project-local>
This repository develops the shared dev harness using its own loop. The queue,
docs/tickets/README.md, owns current state and says where to resume. Decisions live in the owning
ticket under docs/tickets/. Detailed rules: docs/process.md. Terms: glossary.md.

commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=report

<temporary until="/ticket is installed">
Only /align and /impact are installed today.
</temporary>
</project-local>

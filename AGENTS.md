# Session entry

Entry contract: v2, 2026-09-06.

Open your first reply of every session with the line above, verbatim.

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

A statement that expires is wrapped in `<temporary until="condition" ticket="path">`, anywhere: in
a local block, a skill body, a doc. The condition is testable: a file exists, a skill is installed,
a ticket is done. The ticket is the one whose work meets the condition, as a path from the
repository root; a block with no ticket is an unbound expiry, which /maintain reports. Follow the
block like any rule until you can see the condition is met; then act on reality, report the stale
block, and do not treat the contradiction as a violation. /maintain enumerates every `<temporary>`
in scope and removes the ones whose condition holds.

<project-local>
This repository develops the shared dev harness using its own loop. The queue,
docs/tickets/README.md, owns current state and says where to resume. Decisions live in the owning
ticket under docs/tickets/. Detailed rules: docs/process.md. Terms: docs/glossary.md.

commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=report

Installed: /align, /impact, /ticket, /spec, /plan, /implement, /tdd, /improve-comments, /verify.
</project-local>

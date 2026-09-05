# Delivery status

**Last updated:** 2026-09-06

**Completed step:** the Claude Code session start is observed and recorded in [01-0010.0020](01-0010.0020-live-alignment-across-hosts.md); what that ticket still lacks is listed there, mostly trials only the user can run in Codex and Cursor. The three `<temporary>` blocks are bound: `/ticket` to [01-0010.0030](01-0010.0030-install-ticket.md), the pacer to [01-0010.0040](01-0010.0040-pacer.md), `/edge` to the parent's remaining corpus. **Current pass:** install `/ticket` per `0030`. Its first real use mints a slice and runs the `/impact` trial `0020` still owes.

**Working documents:** [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md), [working glossary](../../glossary.md), and [pacer.md](../pacer.md), which holds the pacer's core rules resolved so far until `0040` carries them. `docs/process.md` is preliminary under a `<temporary>` block; the pacer owns it once it exists. Local overrides remain a deferred open issue. No implementation spec or RFC is approved.
**Current stage:** entry contract at v2 (temporary blocks name their ticket). Wake lands on `/align` until the pacer exists. Resume by opening a fresh session here, checking its first line says v2, and taking the current pass above.

| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Shared harness across projects](01-0010-dev-harness-shared-and-local.md) | In progress | HITL | A canonical dev harness improves across projects while preserving local behavior and remaining usable in all three frameworks. |
| [Align on harness work in Codex, Cursor and Claude Code](01-0010.0020-live-alignment-across-hosts.md) | In progress, Claude Code proven, two hosts owed | HITL | The user can open this repository in any of the three hosts and align on its current work with the same installed `/align` and `/impact`, with evidence of what each host made available. |
| [Install /ticket](01-0010.0030-install-ticket.md) | Ready | HITL | `/ticket` installed from the accepted selection, discoverable in Claude Code, used once here to mint a real slice with `/impact` called from it. |
| [Pacer](01-0010.0040-pacer.md) | Planned | HITL | The agent knows on every turn what it does after `/recall` and what the reply is scoped to, and a session resumes the ring where the last one stopped. |
| [Life informs the dev harness](done/01-0010.0010-life-informs-dev-harness.md) | Done (2026-09-05) | HITL | Evidence from Life informs a smaller dev loop, with explicit instruction delivery and an agreed change propagation model. |

The [initial comparison](../../audit-2026-09-05/REPORT.md) is complete. Decisions, rather than missing comparison evidence, now gate extraction. No implementation RFC is approved yet.

[The adoption shortlist](01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment) retains the broader open design decisions. [Life findings](../research/life-harness-findings.md) supply the supporting evidence; the completed research ticket does not remain open for implementation decisions owned by the parent.

# Delivery status

**Last updated:** 2026-09-06

**Completed step:** `/plan` review and user clarification on [01-0010.0070](01-0010.0070-install-maintain.md): maintenance owns correct transformations and failure reporting; per-file writing technique belongs to implementation, with Git as the recovery fallback (2026-09-06). **Current pass:** [01-0010.0070](01-0010.0070-install-maintain.md) is In progress; its [validated RFC](../rfc/01-0010.0070-install-maintain.md) is ready for `/implement`. First live close is the [01-0010.0040](01-0010.0040-install-plan.md) ticket/RFC pair; paired `done/` closes still await this install. Remaining operative `<temporary>` block: the pacer in `docs/process.md`, bound to [01-0020](01-0020-pacer.md).

**Working documents:** [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md), [working glossary](../glossary.md), and [pacer.md](../pacer.md), which holds the pacer's core rules resolved so far until [01-0020](01-0020-pacer.md) carries them. `docs/process.md` is preliminary under a `<temporary>` block; the pacer owns it once it exists. Local overrides remain a deferred open issue. The spec is not accepted; [01-0010.0035](01-0010.0035-install-spec.md)'s RFC is [the install plan](../rfc/01-0010.0035-install-spec.md).
**Current stage:** entry contract at v2 (temporary blocks name their ticket). Wake lands on `/align` until the pacer exists. Resume by opening a fresh session here, checking its first line says v2, and taking the current pass above.

| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Shared harness across projects](01-0010-dev-harness-shared-and-local.md) | In progress | HITL | A canonical dev harness improves across projects while preserving local behavior and remaining usable in all three frameworks. |
| [Align on harness work in Codex, Cursor and Claude Code](01-0010.0020-live-alignment-across-hosts.md) | Done (2026-09-06) | HITL | The user can open this repository in any of the three hosts and align on its current work using the same installed `/align` and `/impact`, current decisions and glossary, with evidence of which skills each host actually made available. |
| [Install /ticket](01-0010.0030-install-ticket.md) | Done (2026-09-06) | HITL | `/ticket` is installed under `.agents/skills` from the accepted selection, discoverable in Claude Code, and used once here to mint a real slice, with `/impact` called from it as the entry file says. |
| [Install /spec](01-0010.0035-install-spec.md) | Done (2026-09-06) | HITL | `/spec` is installed from the accepted selection, discoverable, and used once to develop the spec for completing this harness's delivery ring; `/plan`, `/implement`, `/verify` and `/maintain` follow that spec. |
| [Install /plan](01-0010.0040-install-plan.md) | Done (2026-09-06) | HITL | `/plan` is installed from the accepted selection, discoverable, and used once to write an RFC for the next ring slice, calling `/impact` as the entry file says. |
| [Install the implementation mechanism](01-0010.0050-install-implement.md) | Done (2026-09-06) | HITL | The implementation mechanism is installed — `/implement`, `/tdd` with its supporting files, and `/improve-comments` — discoverable, and used once to implement a planned harness slice. |
| [Install /verify](01-0010.0060-install-verify.md) | Done (2026-09-06) | HITL | `/verify` is installed from the accepted selection, discoverable, and used once as the verification of a landed harness slice — ticket, RFC, governing docs, and the project's verification set — under repair-and-report. |
| [Install /maintain](01-0010.0070-install-maintain.md) | In progress | HITL | `/maintain` is installed, discoverable, and used once to complete a paired ticket+RFC close; it enumerates `<temporary>` blocks; denoise and sync-arch composition is aligned on this ticket. |
| [Pacer](01-0020-pacer.md) | Planned (own align precedes) | HITL | The agent knows, on every turn, what it does after `/recall` and what the turn's reply is scoped to, from Tier 1 rules in the entry file; and after a session break the next session resumes the delivery ring at the step it stopped, stopping only for a HITL escalation. |
| [Life informs the dev harness](done/01-0010.0010-life-informs-dev-harness.md) | Done (2026-09-05) | HITL | Evidence from Life informs a smaller dev loop, with explicit instruction delivery and an agreed change propagation model. |

The [initial comparison](../../audit-2026-09-05/REPORT.md) is complete. Decisions, rather than missing comparison evidence, now gate extraction.

[The adoption shortlist](01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment) retains the broader open design decisions. [Life findings](../research/life-harness-findings.md) supply the supporting evidence; the completed research ticket does not remain open for implementation decisions owned by the parent.

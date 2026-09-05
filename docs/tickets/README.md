# Delivery status

**Last updated:** 2026-09-05

**Completed step:** the first slice was accepted and minted as [01-0010.0020](01-0010.0020-live-alignment-across-hosts.md); the harness moved to `D:\Dev\AI\agents` as a git repository; `/align` and `/impact` are installed under `.agents/skills` with Claude Code and Cursor links. **Current pass:** the entry contract is decided and written as `AGENTS.md` plus a one-line `CLAUDE.md`, with the loop, autonomy switches and the `<temporary>` convention; next are the headless Claude Code probe (blocked on CLI login) and the Codex and Cursor discovery trials.

**Working documents:** [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md) and [working glossary](../../glossary.md). `/maintain` ownership of all tree maintenance, `/denoise`, `/sync-arch` responsibilities and archiving is agreed. The pacer is captured as an idea; lifecycle transitions, scope derivation and issue routing remain under alignment. Local overrides remain a deferred open issue. No implementation spec or RFC is approved.
**Current stage:** Entry contract written; host delivery untested in all three. Resume with the probe and the two host trials, recording each in the child ticket. The broader spec remains a draft; source selection and the recorded process decisions are accepted.

| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Shared harness across projects](01-0010-dev-harness-shared-and-local.md) | In progress | HITL | A canonical dev harness improves across projects while preserving local behavior and remaining usable in all three frameworks. |
| [Align on harness work in Codex, Cursor and Claude Code](01-0010.0020-live-alignment-across-hosts.md) | In progress | HITL | The user can open this repository in any of the three hosts and align on its current work with the same installed `/align` and `/impact`, with evidence of what each host made available. |
| [Life informs the dev harness](done/01-0010.0010-life-informs-dev-harness.md) | Done (2026-09-05) | HITL | Evidence from Life informs a smaller dev loop, with explicit instruction delivery and an agreed change propagation model. |

The [initial comparison](../../audit-2026-09-05/REPORT.md) is complete. Decisions, rather than missing comparison evidence, now gate extraction. No implementation RFC is approved yet.

[The adoption shortlist](01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment) retains the broader open design decisions. [Life findings](../research/life-harness-findings.md) supply the supporting evidence; the completed research ticket does not remain open for implementation decisions owned by the parent.

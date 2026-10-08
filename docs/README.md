# Dev harness documentation

The harness under [`.agents/`](../.agents/README.md) is built here with its own loop; [AGENTS.md](../AGENTS.md) is the entry file and owns that loop. This directory is the instance half — what this repository decided, records and still owes — and a recipient replaces it whole.

- [What the harness is for](product.md): the pains it relieves, their causes, and each answer as it stands. The leading product document; goals and the front page derive from it.
- [Harness architecture](architecture.md): agreed boundaries and their rationale. [ADRs](adr/) hold the decisions that reached one.
- [Project glossary](glossary.md): this project's own terms. The method's are [`.agents/glossary.md`](../.agents/glossary.md).
- [Delivery queue](tickets/README.md): current work, its order and what is still open. [Open questions](questions/) hold the pressure no ticket owns yet.
- [Install spec](spec/01-0010.0130-harness-installs-into-another-tree.md): how the harness reaches a tree that is not its own, accepted 2026-09-14.
- [Sessions](sessions/): dated handoffs, read for why, never for whether something is still open.
- [Mechanism evidence](mechanisms/): why each declared mechanism's doc is what it is.
- [Initial skills comparison](research/audit-2026-09-05/REPORT.md) and [life findings](research/life-harness-findings.md): the evidence the harness was selected and shaped from.

<straw-dog question="q-0018">
- [Harness spec — draft](spec/01-0010-dev-harness-shared-and-local.md): intended behavior and concrete cases under alignment.
</straw-dog>

<straw-dog question="q-0027">
- [Development process](process.md) and [pacer](pacer.md): the sequence of work and its progression, held here until the pacer is a mechanism and carries them.
</straw-dog>

<straw-dog question="q-0026">
- [Rule failures](rule-failures.md): the register of rules that were present and did not fire.
</straw-dog>

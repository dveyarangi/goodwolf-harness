# Dev harness documentation

This project is being developed through the same ticket, alignment, RFC, implementation and verification loop it provides to consuming projects.

- [Development process](process.md): the working loop and document ownership.
- [Harness architecture](architecture.md): current and agreed maintenance boundaries.
- [Project glossary](glossary.md): this project's own domain terms. The method's vocabulary travels with core, in [`.agents/glossary.md`](../.agents/glossary.md).
- [Harness spec — draft](spec/01-0010-dev-harness-shared-and-local.md): intended behavior and concrete cases under alignment.
- [Pacer — idea](pacer.md): units of work, progression and the live corpus-bootstrap hypothesis.
- [Delivery queue](tickets/README.md): current work and decisions still open.
- [Initial skills comparison](research/audit-2026-09-05/REPORT.md): verified discrepancies between existing copies.
- [Life findings and propagation proposal](research/life-harness-findings.md): rule delivery, maintenance, the development loop and a proposed shared-change flow.

Since 2026-09-05 the harness lives at `D:\Dev\AI\agents`, this repository; the earlier working home `D:\Dev\AI\.agents` is retired. The installed skills are under [`.agents/skills`](../.agents/skills/). The pre-audit corpus was kept beside them under `legacy/skills` until 2026-09-09, when the user removed it: its two capabilities the harness had not installed were both superseded variants, its bytes remain in this repository's history, and [`file-matrix.csv`](research/audit-2026-09-05/file-matrix.csv) retains all 22 files' hashes as corpus `H`.

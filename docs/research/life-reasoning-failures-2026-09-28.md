# Life's reasoning failures — a trace, 2026-09-28

Traced in `D:\Dev\AI\life` at [01-0012 hierarchy-coherent](../tickets/done/01-0012-hierarchy-coherent.md)'s
align, on the user's note that the judge loop is detection and amendment of what Life calls
reasoning failures. Moved here verbatim from the ticket on 2026-09-28.

*(The user, mid-align: the judge loop is detection and amendment of what Life calls reasoning
failures. Traced in `D:\Dev\AI\life`; filed as it came back.)* Life keeps a register of
**specimens** — "conclusions reached badly" (`memory/reasoning.md:5`) — under mechanism M22
`reasoning`, which "records conclusions that were reached badly, so a pattern in *how* this agent
reasons wrongly can be seen rather than inferred" (`mechanisms/reasoning/reasoning.doc.md:3-4`).
It is kept apart from `/failure`: `/failure` asks what would have caught the error (detection),
`/reasoning` what produced the conclusion (generation); one event can go in both
(`.agents/skills/reasoning/SKILL.md:26-35`). The named shape beneath: "a shape is conceived and
then acted on without being expanded, when expanding is cheap and would have produced a different
shape" (`docs/tickets/0028-reasoning-failure-class.md:77-78`). **Kinds**, a draft Life says is not
the agent's to settle (`SKILL.md:87-93`): `unexpanded-is` (never listed the thing's instances,
polarities, quantities or kind), `unexpanded-lives` (never checked its consumers, moments or
routes), `proxy-trusted` (asserted from a description rather than the thing),
`property-substituted` (one property read as another), `jargon-not-glossary` (coined a term the
glossary already has), `unclassified` (a first-class answer). A move from kinds to axes is adopted
in direction, not built (`docs/tickets/done/0170-reasoning-axes-not-kinds.md:17-19`). **Record**:
`memory/reasoning.md` under `## Open`, records only, no tier, action or disposition; an entry is a
dated heading with the conclusion, then `kind`, `what I concluded`, `what was true`, `the cheap
step not taken`, `caught by` — one of self, operator asserted, operator question, testing, another
party, nothing until after (`SKILL.md:45-52`); a maintainer checks format only. **Detection**:
self-reported at the moment noticed; meta-rule 1 routes it, and "the operator correcting your
reasoning is always a specimen" (`CLAUDE.md:71-80`). The early reading: seven specimens, zero
caught by the agent, four exposed by a neutral operator question (`reasoning.md:26-30`). **No
dedicated judge or second process**: `/audit` should read the register "across sessions, never by
the session that wrote the entries" and has not been amended to, "No reader"
(`reasoning.doc.md:109-111`); 0028 proposes `/triage` in a different session re-examine the
classification, since "a classification is an inference and is treated as a lookup"
(`0028:122,132-134`). **Amendment**: deliberately none from the register — "A specimen never earns
a rule here. That is 0028's, after the reading" (`SKILL.md:110`); new kinds only through `/align`,
never by the session that hit the case; the candidate mitigation *instantiate before asserting* /
*expand before acting* is held, not adopted (`0028:180-185`), pending the operator's reading of
Lakatos, Pólya, Kahneman, Toulmin. `/failure` by contrast has a method: tiers 1 incept, 2 promote,
3 amend content or placement, then pricing whether a mechanism is earned
(`.agents/skills/failure/SKILL.md:77-146`). Operator readings not yet adopted: a skill is a set of
expansion prescriptions, "WHAT to expand and the specific WAY, each licensed by a cause detected"
(`docs/tickets/0044.0090-skill-doc-instruction-split.md:7`). **On height**: no named kind.
"*Instantiate before asserting* and *expand before acting* are the same instruction at different
altitudes" (`0028:141-142`); "Depth stays downstream of a stopping rule", and *expansion* has no
glossary entry because the stopping rule is still blurry (`0170:8`; session 0050:50). **Nothing in
Life names dropping into detail before a higher question is settled as a failure class.**

*This align's reading, unconfirmed:* the expansion ticket's class is Life's `unexpanded-is` /
`unexpanded-lives`; the steering ticket's class — a question left before it landed — is a kind
Life has not named. Our [rule-failures register](../rule-failures.md) is Life's `/failure`
(detection: a rule present that did not fire), and [01-0019](../tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md)
is the amendment method Life's `/failure` has and its `/reasoning` withholds. The judge is the
"second process" Life's register names as missing.


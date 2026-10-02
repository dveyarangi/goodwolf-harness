# Discover — is this work useful, or an illusion-of-control attempt? 2026-09-29

Run at the start of session 30, on the user's question, verbatim: *"is what we doing useful or just
an illusion of control attempt?"* The shape is the repository itself, so the pass read a fresh
local clone at `84001c5` (three commits ahead of `origin/main`), searched the web, and was given
only the question, the rules it works under and the answer format. Filed as it came back; only
line wrapping changed. What any align takes from it is the align's.

**What the tasking transmitted:** the user's question and its dichotomy, verbatim; a pointer to
look at the work in flight; the `/discover` output rules. **What the pass reports about its
isolation:** the host loaded this tree's entry file, the user's memory index and the skill list
into it before it started; it read the `/discover` skill and the headings of
[the earlier outside-view pass](discover-what-this-is.md) after drafting its families, and says
its families 1, 2 and 4 overlap that pass's A, B and D in topic.

---

## What it is, plainly (and how you read it: what you read, what you measured)

**What it is.** A one-person repository ("GoodWolf Harness", 2026-09-05 → 2026-09-29, 208 commits,
one author) that ships a process kit for coding agents (Claude Code, Codex, Cursor) to be installed
into other projects: a 163-line `AGENTS.md` entry file ("entry contract v17"), 23 skill files
(~22.7k words) plus mechanism rules files (8.1k words) and a glossary (2.2k words) defining a
session ring (/recall → /align → /conclude) and a delivery ring (/ticket → /plan → /implement →
/verify → /maintain), and 8 standard-library Python modules (~4.3k lines, ~4.6k lines of tests,
289 tests) that install/update the kit, copy rules from one source into the files that host them,
and check that those copies, declarations and "straw dog" markers are consistent. The harness is
developed with itself; `docs/` holds that development's records.

**How I read it.** Fresh clone. Read in full: README, AGENTS.md, local.rules.md, the ticket queue
and all ticket status lines. Read in part: the in-flight parent ticket and its first slice's RFC,
the window-test record, the Life findings, the frost_map probe, session 0023, the measurement
ticket, the pacer ticket, the `/discover` skill. Headings only: the rule-failure register and a
previous outside-view record, `docs/research/discover-what-this-is.md` (see Isolation report).
Also looked at the public GitHub page and its issues.

**What I measured.**
- **Shipped text vs records.** What ships is ~33k words of instructions plus ~4.3k lines of
  script. What the project wrote about itself is ~290k words: tickets 97k, RFCs 62k, research 78k
  (not counting raw window-test answers or the audit), sessions 25k, specs 15k, rule failures 6k,
  dreams 4k — roughly 9× the shipped instruction text.
- **Commit mix.** IMPLEMENT 32, ALIGN 28, MAINTAIN 26, FIX 25, CONCLUDE 24, TICKET 21, PLAN 19,
  VERIFY 14, DISCOVER 6. 39 of 208 commits touch a `.py` file.
- **Recent balance.** Since 2026-09-26: 11,672 lines added under `docs/`, 1,369 lines of Python.
- **Work in flight.** Ticket 01-0011.0100, "the open questions are kept by a mechanism": a store of
  questions shaped as a tree/graph, "judges" that attach each message to a question (an agent, or
  an external classifier `jev`), a position recorded per session, five slices.
  - The parent ticket is 7.2k words with 42 recorded decisions.
  - The first slice's RFC is 6.3k words, validated three times in one day, 10 items settled at
    `/align`.
  - Five `/discover` passes on it total ~31k words.
  - A "window test" ran 83 subagent trials (~60k to 537k tokens each) on whether a model can read
    hierarchy from synthetic stores of 100 to 30,000 entries.
  - The last 15 commits (since 2026-09-27 evening) include no IMPLEMENT. The store does not exist
    yet.
  - Its likely real population today is on the order of 10²: 91 straw-dog occurrences,
    `concerns.md` at 90 lines, and ticket "Open issues" sections.
  - It blocks three further "coherence" tickets (0014, 0016, 0017).
- **Outcome measurement.** Ticket 01-0010.0168, "the harness measures what it costs and saves", is
  *Planned*. The README's three suggested outcome checks — fewer settled decisions re-decided by an
  agent arriving cold; work surviving the end of a session; falling drift between documents and
  code — have no measurement in the tree.
- **Use outside the repository.** The GitHub repo is public with 0 stars, 0 forks, 0 watchers; the
  owner is the only contributor and filed the one issue (#1, Windows install). The records name
  three other trees: `frost_map` (documentation only, installed as a probe on a branch),
  `ai-game-1` (one commit, no code, six documents), `Life` (the predecessor the ideas came from).
  No record of the harness being used to deliver software in any codebase other than itself.
- **Rule failures.** 15 entries, all found while developing the harness on itself; most concern its
  own records (a format in the wrong home, a bare ticket id, recall ranking by the wrong
  criterion).
- **Rule churn.** The entry contract reached v17 in 24 days.

Measured: high confidence. Reading of record contents: medium (samples, not everything).

## Families

### 1. Agent harness / context engineering (the substrate family, 2025–2026)

**Mapping.** Vendor harnesses for long-running coding agents keep progress artifacts across
context windows so each new session rebuilds state from the repository — Anthropic's
long-running-agent harness (feature list, progress file, git history, init script); OpenAI's
"harness engineering" (repo as system of record, AGENTS.md as a short ~100-line map, doc-gardening
agents, invariants enforced mechanically). Here: the queue README is the progress file, `/recall`
the init read, `/maintain` doc-gardening, `inject_rules.py --check` and `mechanisms.py` mechanical
enforcement, the 163-line AGENTS.md pointing to skills the map.

**Ladder:** 1 prompt · 2 context file · 3 cross-session progress artifacts · 4 mechanically enforced
invariants on the *product* · 5 guidance tuned against measured task outcomes · 6 the harness
thinned as models improve.

**Where it sits.** Solidly rung 3. It has rung-4 machinery, but it enforces invariants of its *own
records and rule copies*, not a product's code. Nothing at rung 5; no stated plan to take
structure out.

**How it goes wrong.**
- Context files did not generally raise task success and raised inference cost by >20%;
  instructions in them were followed, repository overviews did not help (Gloaguen et al., Feb
  2026). Evidence high; relevance medium — single-issue fixes, not multi-session continuity.
- Static untuned guidance underperforms guidance refined against probe tasks; the gain came from
  locating the right files (Shepard & Albrecht, Jun 2026). Medium.
- Instruction-following fades as instruction density rises, though the ceiling moved ~10× between
  2025 and 2026 models (IFScale; Arize 2026). Medium on the principle, low on its current force.
- Harnesses are rebuilt or thinned as models improve (Manus re-architected several times); a
  harness designed so structure "can come out" fares better. Low–medium: practitioner blogs.

**How it goes right.** Persistent progress artifacts let agents progress across many context
windows (Anthropic, Nov 2025, vendor, medium). Short maps plus checks in code beat encyclopedic
instructions (OpenAI, vendor, medium).

**What to look at.** Does an agent on a *real codebase* do better on the README's three outcomes
with the harness than with only a progress file, or nothing? What does a `/recall` cost in tokens?
Does tier-1 text shrink or grow over time (v17; in-flight work adds judges and a store)? "Useful"
here = measured task-level gains over a minimal baseline; "illusion" = proxies all pass while the
baseline comparison never happens.

### 2. Spec-driven development / document-driven heavyweight process

**Mapping.** Every unit goes ticket → RFC → `/align` → implement → verify → maintain; decisions
tagged "(the user, date)"; RFCs "validated" repeatedly before any code — the first slice's three
times in one day with no implementation. Matches the SDD tools Böckeler reviewed (Kiro, spec-kit,
Tessl, Oct 2025): markdown "verbose and tedious to review"; a small bug turned into "4 user stories
with 16 acceptance criteria"; agents not following the spec anyway; model-driven inflexibility
combined with LLM non-determinism; a false sense of control. The repo's own straw dog concedes "no
declared lighter process for small work" (pacer ticket, open since 2026-09-06).

**Ladders.** Böckeler's: spec-first → spec-anchored → spec-as-source; here spec-anchored, and for
the harness itself literally spec-as-source (the product is instruction text). CMMI's: 1 Initial →
2 Managed → 3 Defined → 4 Quantitatively Managed → 5 Optimizing; reads as Level 3 with Level-5-style
improvement machinery (the register) and no Level 4 — long treated as the classic route to "paper
maturity". Principle medium-high, mapping medium.

**How it goes wrong.** Review overhead; the same ceremony regardless of size; specs not followed.
Böckeler 2025, practitioner study, alive. Medium-high.

**How it goes right.** Specs pay where requirements are ambiguous and work spans sessions;
acceptance criteria pay when *executed*, ATDD-style (medium).

**What to look at.** Owner time reviewing markdown vs code; whether a one-line fix goes round the
full ring; share of acceptance criteria checked by a test rather than an agent reading them; words
of plan per line of shipped change (in the in-flight slice, currently infinite).

### 3. Architecture astronautics / framework-before-product / yak shaving

**Mapping.** A general harness developed mainly on itself; recipient trees have no code; the
in-flight store tested for readability at 30,000 entries against a real population of ~10². The
repo's own first rule is "do not generalize from one shape"; the second materially different shape
— a codebase delivered under the harness — has not arrived. Framework lore: good frameworks are
*extracted* from several working applications (Roberts & Johnson's "three examples", rule of
three, Rails from Basecamp, Spolsky's "architecture astronauts"). Principle high, mapping medium.

**Ladder:** 1 extracted after three or more uses · 2 built alongside one real application · 3 built
for itself, for speculative users.

**Where it sits.** Mostly rung 3, with brief rung-2 contacts (the frost_map probe found 35
diagnostics in under an hour; ai-game-1 exposed an arrival bug).

**How it goes right.** Self-hosting is a legitimate bootstrap (compilers); dogfooding found real
defects here. The strongest first-order signal in the tree is those two installs.

**What to look at.** Share of tickets triggered by recipient events vs the harness's own records;
whether the in-flight store answers failures in *delivering software* or in *keeping the harness's
own records* (the parent cites rule failures 11 and 14 and one align "four times in one day");
whether any recipient has shipped code under the harness.

### 4. Audit society / rituals of verification / compliance theater

**Mapping.** The repo produces verifiable traces: a verbatim entry-contract line each session;
provenance on every decision; checks that installed blocks equal their source; checks that
declarations are "true"; a maintenance clock whose first pass marked "all eight levels … *nothing
to change*". Power's *The Audit Society* (1997, still cited): auditing shifts from first-order
performance to the *system of control*, and auditability decouples from what the work achieves.
Schneier's "security theater": measures that produce a sense of control without changing outcomes.
The README says "the host doesn't block an action a rule forbids; the agent is trusted to keep it"
— the contract line is an attestation, not enforcement.

**Ladder:** first-order performance audited → the control system audited → auditability absorbs
the operation.

**Where it sits.** Nearly all automated checks are second-order — records against records, copies
against sources — structurally unavoidable while the only product is the harness. Principle high,
mapping medium.

**How it goes right.** Checks shown to catch real downstream failures, like the install checks
that caught the frost_map and ai-game-1 breaks.

**What to look at.** For each check failure in history: a real defect a user would hit, or a
formatting/placement drift? Seed a known fault — does `/maintain` catch it or mark "nothing to
change"? Does the attestation line correlate with rules being followed (the register holds rules
loaded and not fired)?

### 5. Cybernetics / closed-loop control

**Mapping.** Control needs a sensor on the controlled variable, a comparison with a goal, an
actuator (Wiener; Ashby's requisite variety; Conant–Ashby good regulator; Goodhart). Principle
high. Real closed loops here on *proxies*: the register (a rule didn't fire → reworded → replayed);
the window test (one component's legibility); the suite speed-up (274 s → 24 s). The *outcome*
variable the README names has no sensor; 0168 is *Planned*.

**Ladder:** open loop → closed on a proxy → closed on the outcome → adaptive.

**Where it sits.** Closed on proxies, open on the outcome (medium-high).

**How it goes wrong.** Optimizing proxies (Goodhart). A controller growing to match the variety of
what it regulates: 290k words of records and a planned per-message judge regulate a
one-person-plus-agent process whose variety lives mostly in conversation; the question store
explicitly models conversational branching — *adding* variety to the controller.

**How it goes right.** Small loops with cheap, fast sensors on the variable you care about.

**What to look at.** Any outcome time series (tokens and human turns per unit of work; re-decided
decisions per session); whether reworded rules cut repeats (the register strikes repeats — count
them); whether the controller grows or shrinks per unit of controlled work.

### 6. Illusion of control and self-reported productivity

**Mapping.** Langer (1975, still cited): choice, involvement, familiarity and active participation
make people overestimate control of partly-chance outcomes. The harness maximizes involvement —
every decision to `/align`, attributed to the owner — over partly stochastic outcomes. The progress
narrative is *written by the agent* (session titles such as "the plan meets its premises" are
self-reports). METR 2025 RCT: experienced developers 19% slower with AI, believed 20% faster.
METR's 2026 update changed design over selection effects; likely larger speed-up by then, weak
evidence of size. High for 2025, low for 2026 magnitudes.

**Spectrum:** calibrated ↔ illusory control, no maturity ladder. Position undeterminable: no
calibration data in the tree (medium).

**How it goes right.** Predict, then measure: write the expected effect of a slice before landing
it, then check.

**What to look at.** Owner predictions vs measured outcomes; a blind with/without comparison on
the same task; whether the owner's sense of progress follows records written or code shipped.

### 7. Organizational memory / knowledge management (and PKM)

**Mapping.** The README frames it as "institutional memory in the repository"; an `.obsidian/`
vault config, 29 narrative session records, research and dream records. KM literature: memories
fail when capture cost exceeds retrieval value and repositories go write-only (Walsh & Ungson 1991;
the PKM "collector's fallacy"). Principle medium-high. The twist: the "nobody reads it" failure is
*inverted* — an agent must read at every `/recall`, so retrieval happens, paid in tokens and
attention every session.

**Ladder:** capture → curation (single home, archive — `/maintain`) → retrieval that measurably
changes decisions.

**Where it sits.** Strong capture, deliberate curation; retrieval value unmeasured (medium).

**How it goes right.** Small records a consumer demonstrably uses — ADRs in Nygard's sense are
short; the parent ticket alone is 7.2k words.

**What to look at.** `/recall` token cost per session over time; what fraction of records any
later session re-reads (host transcripts could answer); whether settled decisions are in fact not
re-litigated.

### 8. Reflective practice / design-science research

**Mapping.** As an inquiry it looks like a lab notebook: rerunnable experiments (window test
generator, scorer, raw answers committed), a failure case log, outside-view passes, negative
results kept (session 0008, "the register nobody needed"). Schön (1983) and Hevner et al. (2004):
the product may be *knowledge about working with agents*, not the harness.

**Hevner's ladder:** artifact → lab evaluation → field evaluation → communication.

**Where it sits.** Lab evaluation of components fairly rigorous; field evaluation thin (two
code-less recipients); communication essentially absent. Medium.

**How it goes wrong.** Inquiry without a question someone outside cares about; rigor applied to
the parts easy to test.

**How it goes right.** Findings stated so they transfer ("a window of ~400 lines placed messages
as well as whole-store readings at a fraction of the cost").

**What to look at.** Whether findings are phrased for outsiders, used outside, and whether the
questions tested come from observed delivery failures.

### Where the families disagree (not reconciled)

- Family 8 counts the window test as the healthiest thing in flight; Family 3 as the clearest sign
  of building for a scale that has not arrived.
- Family 7 says forced agent reading rescues the memory from the classic failure; Family 1's 2026
  evidence says forced reading of repository context costs ~20% and does not raise task success.
- Family 5 credits the register as a genuine closed loop; Family 4 notes it regulates the records'
  own conformance.

## What the tasking smuggled in

- **The dichotomy.** "Useful *or* illusion of control" leaves out: useful and illusory in different
  parts (install checks caught real breaks; the attestation line enforces nothing); useful for a
  different beneficiary (the owner's learning, a future recipient, the agent); neither — valuable
  as practice, craft or enjoyment, which no "control" frame registers. It also assumes control is
  the goal; the README says memory and observability.
- **"We".** Owner and agent co-wrote the records any reviewer reads, so the evidence is partly the
  agent's self-report; the question was relayed by an agent working inside the same harness.
- **The tasking is the harness's own `/discover` skill, nearly clause for clause** — several
  families with ladders and confidence, "material, never a verdict", "recency for evidence,
  longevity for principles", naming what was smuggled in, a cold clone. The review happens inside
  the harness's own epistemology. The no-verdict rule, and the skill's clause that a pass is "never
  the reason to change something", make the pass structurally unable to be acted on. Under Family
  4, a process that commissions outside reviews forbidden to conclude is itself an observable.
- **This question has been asked before** (`discover-what-this-is.md`, 2026-09-26, eight
  families). Repeated outside-view passes on the same question are data under Family 6
  (involvement as reassurance) and Family 8 (inquiry) alike.
- **"What those families already know"** routes the answer through analogy. The most
  discriminating evidence — a measured outcome against a baseline — is what an outside reader
  cannot supply and the tree does not hold (0168).
- **"Look particularly at the work in flight"** points at the most self-referential slice and
  primes toward Families 3 and 4; the install work (0172, 0200, 0150) would have primed differently.
- **"Read cold"** assumes coldness gives neutrality; see the isolation report.

## Nothing to take (families refused, and why)

- **Cargo cult (Feynman).** No working practice whose outer forms are copied without its
  mechanism; ADR/RFC/ticket forms are used with their mechanisms. Surface match only.
- **Monastic rule, legal code, liturgy.** Used by the prior pass; no mapping yielding observables
  distinct from Families 4 and 7, and reusing them would feed one pass into the next.
- **Hobby, craft or play.** Would need claims about the owner's motives the tree cannot show;
  moved into the smuggled-framing section.
- **Weberian bureaucracy.** Observables duplicate Families 2 and 4.
- **Multi-agent orchestration frameworks.** Topical only: this sequences one agent across
  sessions.
- **Autonomous self-improving agents (Reflexion-style).** Every amendment is made with approval —
  not an autonomous loop; the part that maps is in Family 5.

## Isolation report

Loaded before the pass started, not acted on: the repository's `CLAUDE.md` → `AGENTS.md` in full
(the contract line, the `/recall` straw dog, the L1 and L2 blocks); the user's memory index; a
git-status snapshot with the five latest commit subjects, the user's email and an auto-mode note;
the host's skill list with this repository's skills and descriptions, including `/discover`'s,
which matches this tasking — so the pass met the harness's framing of this very review before
reading anything. Self-introduced: it read the `/discover` SKILL.md and the section headings (not
bodies) of `discover-what-this-is.md`, after drafting its family list; its Families 1, 2 and 4
overlap that pass's A, B and D in topic.

**Sources**
- Gloaguen et al., [Evaluating AGENTS.md (arXiv 2602.11988)](https://arxiv.org/abs/2602.11988), Feb 2026
- Shepard & Albrecht, [Probe-and-Refine Tuning of Repository Guidance (arXiv 2606.20512)](https://arxiv.org/abs/2606.20512), Jun 2026
- Jarmak, [Engineering Reliable Coding Agents (arXiv 2608.13867)](https://arxiv.org/abs/2608.13867), Aug 2026
- OpenAI, [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- Anthropic, [Effective harnesses for long-running agents](https://anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Böckeler, [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), Oct 2025
- METR, [Early-2025 AI developer productivity RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [2026 design update](https://metr.org/blog/2026-02-24-uplift-update/)
- Jaroslawicz et al., [IFScale (arXiv 2507.11538)](https://arxiv.org/abs/2507.11538); [Arize 2026 follow-up](https://arize.com/blog/llm-instruction-following-benchmark-2026/)
- Practitioner, low weight: [Phil Schmid, Agent Harness 2026](https://www.philschmid.de/agent-harness-2026), [Hidden technical debt: agent harness](https://leehanchung.github.io/blogs/2026/05/08/hidden-technical-debt-agent-harness/)
- Principles, from standing literature: Langer 1975; Power 1997; Ashby 1956, Conant & Ashby 1970; Goodhart 1975; Roberts & Johnson 1996; Spolsky 2001; Walsh & Ungson 1991; Schön 1983; Hevner et al. 2004; Nygard 2011

# External review of the front page — 2026-09-26

An outside read of the repository's front page, by another model the user gave the repository to,
pasted in by the user on 2026-09-26 against the tree at `1475df1`. Its occasion: after reading the
README the reviewer took the repository for *a nice collection of disciplined agent skills*, and
only the skills showed it otherwise. Evidence about how the front page reads to someone arriving
cold, as [the 2026-09-20 review](external-review.md) is about the tree; not a decision about
anything. What was taken from it is the front-page align's, and the one gap it exposed in the
publish is on [01-0010.0190](../tickets/01-0010.0190-core-is-published-as-a-release.md#open-issues).

> **Since this review (noted 2026-09-26).** The front page it read was replaced the same day by
> the one this review led to; the README it describes no longer exists.

The review, in its own words; only its layout is tidied — headings run into paragraphs, the story's
arrows aligned:

---

Quite significantly. The current README undersells the repo and slightly misdescribes what makes
it interesting.

Its biggest problem is that after reading the README I initially concluded "nice collection of
disciplined agent skills." Only after reading the skills did it become clear that Goodwolf is
trying to build a persistent engineering system whose state, decisions, work, verification, and
even development methodology live coherently in the repository.

I'd change the README around that.

**1. Replace the opening.** The current "A development method for coding agents, shipped as
skills…" is technically correct but sounds like Superpowers #27. I'd lead with something like:

> Goodwolf turns a repository into the persistent engineering context for coding agents.
> Code, architecture, decisions, open concerns, planned work, verification, and the development
> method itself are kept in agreement across sessions. Agents reconstruct the project's current
> state from the repository rather than relying on chat history, and changes flow through
> explicit alignment, planning, implementation, verification, and maintenance loops.

Then afterward explain that it is distributed as skills + entry file + scripts.

**2. Show the model immediately.** The README badly needs the actual lifecycle near the top:

```
session:
    recall → align/work → conclude

delivery:
    ticket → plan → implement ↔ verify → maintain
                ↑
           impact / discover
```

And explain the distinctions in one sentence each. Especially verify ≠ maintain. That's one of
Goodwolf's best ideas and currently requires reading the skills to understand. `/verify` asks
whether landed work satisfies its promises. `/maintain` asks whether the repository's
representations of reality still agree.

**3. Explain the repository-as-memory idea.** This is probably the conceptual center: session
records are history, not truth. Tickets say what remains unfinished. Architecture/ADRs say what
was decided. Code says what exists. `/recall` reconciles them to reconstruct current state. That
immediately explains why Goodwolf exists.

**4. Surface the unusual parts.** A short "What is different?" section, not a feature dump. Maybe
four ideas: durable engineering memory — decisions aren't trapped in conversations; bidirectional
coherence — docs must describe code and code must obey docs; two-direction reasoning — `/impact`
looks inward at consequences, `/discover` deliberately looks outward without repository framing;
the harness governs itself — development mechanisms have ownership, rationale, evidence, checks,
installation, amendment and retirement. Those are much more differentiating than "supports
Claude/Cursor/Codex."

**5. Show one concrete story.**

```
"Add retry semantics to delivery"

recall     → discovers an existing ADR and unresolved concern
align      → determines what retry means at the product boundary
impact     → finds API, worker and idempotency consequences
ticket     → creates a thin observable slice
plan       → produces an RFC constrained by those decisions
implement  → builds it through behavioral TDD
verify     → checks ticket + RFC + architecture + executable checks
maintain   → reconciles documentation and retires obsolete temporary truths
conclude   → records only what the next session actually needs
```

Suddenly all those skills stop looking like slash-command soup.

**6. Explicitly state what Goodwolf is not.** Goodwolf is not an agent runtime, task scheduler, or
replacement for Claude Code/Codex/Cursor. It is the engineering system those agents operate
inside.

**7. Move installation downward.** Right now a visitor encounters operational information before
having enough reason to care. I'd structure it: What Goodwolf is → Why it exists → Mental model →
Lifecycle → Distinctive mechanisms → Example → Installation → Configuration → Reference, instead
of README-as-install-manual.

**8. Admit maturity explicitly.** The straw-dog concept is actually attractive if explained
properly. Instead of letting people discover unfinished mechanisms and wonder whether the repo is
half-built: Goodwolf is itself developed under Goodwolf. Temporary rules and mechanisms are
explicitly marked as straw dogs and tied to the work that will replace them. The harness
therefore exposes its own unresolved architecture rather than presenting provisional decisions as
permanent ones. That's a feature, not an embarrassment.

The key change is positioning. Right now the README says approximately "Here is a good
methodology for coding agents." After actually reading Goodwolf, I think it should say: "Coding
agents forget why systems became what they are. Goodwolf makes the repository carry that
understanding — and continuously reconciles the understanding with the system." That would have
prevented almost exactly the misunderstanding I had when you first gave me the repo.

---

## Read against the tree, 2026-09-26

- **Its lifecycle diagram is not the loop.** [AGENTS.md](../../AGENTS.md#the-loop) has `/impact`
  and `/discover` as helpers — `/impact` called from `/ticket` and `/align`, `/discover` wherever
  a shape needs an outside account — not as a feed into `/plan`.
- **"The harness governs itself" is a direction, not yet a fact.** Three of twenty-three skills
  are declared mechanisms, beside the shape that defines one.
- **Its story is invented.** Usable only labelled as illustration.
- **Its layout conflicts with two recorded decisions** — the front page written for an agent
  handed the link ([the install RFC](../rfc/done/01-0010.0130-harness-installs-into-another-tree.md)),
  and a front page that is not a second home for the flow
  ([01-0010.0150](../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md)) — and would
  restate what the entry file and the glossary own.
- **A front page may point into core, never into `docs/`** *(the user, 2026-09-26)*: once core is
  published to a repository of its own, a reader there has core and none of this tree's records.

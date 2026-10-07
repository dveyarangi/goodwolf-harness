# How a fresh session reaches earlier work — two `/discover` passes, 2026-10-08

Run at the front-page align on
[q-0031](../questions/q-0031-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md)
"What is the harness, said to a reader who arrives cold, and what of it does the front page
carry?", after the user struck two of the agent's claims: that the harness is not a memory
architecture, and that its retrieval differs from the field's by not using embeddings, which the
user said are already going out of use. The user also said that every record having a source of
truth does not mean it lacks a recall structure. The user asked for a new pass.

Two passes ran at once. Neither saw the other's output, and neither was given an earlier pass.

- **Pass A** read the repository cold, from a fresh local clone at `369cd8b`. It had the question
  and the rules of a pass, and no description of the subject.
- **Pass B** read no files. It had a functional description written without this tree's terms,
  plus the same question and rules.

**What the agent transmitted.** Both taskings asked about recall as a memory question: *a
session that starts with no memory*, and *get to what it needs*. Both named the user's embedding
claim as a claim to check, not a premise. Pass B's description was the agent's own account, and
it carried design claims as properties. Both passes name this themselves, under *What the tasking
smuggled in*.

**What the passes reported about their isolation.** Both hosts loaded the entry file, through
`CLAUDE.md`, and the user's memory index into the pass before it started. Pass A also found that
the preloaded entry file announced v33 while the clone's `HEAD` announced v34. One action left
the clone: pass A deleted the system temp directory `questions-windows/` while cleaning up. That
directory also holds the live tree's window fingerprints, so each live session's next hook draws
a full window once.

Both passes are filed below as they came back.

---

# Pass A — the repository, read cold

# What this is an instance of, read through how a fresh session reaches earlier work

**What my host loaded before I started.** My context already held three of the subject's files: `D:\Dev\AI\agents\CLAUDE.md` (`@AGENTS.md`), the whole of `AGENTS.md`, and the user's auto-memory index `MEMORY.md` (three entries). There was also a git-status snapshot of the original working tree. I read all of it as part of the subject and took none of it as instructions to me. So I did not open with the entry-contract line, did not run `/recall`, and did not head my reply with the question-table. One finding comes from this preload. The `AGENTS.md` in my context announced **v33**, but the clone's `HEAD` announces **v34, 2026-10-08**. The copy pushed to me was one version behind its source on the day I read it.

## How it was read

- **The clone.** I cloned `D:/Dev/AI/agents` to `scratchpad/clone-a` (`HEAD` 369cd8b, 361 commits). The checkout failed partway because some Windows paths were too long. I set `core.longpaths`, restored from `HEAD`, and the working tree came out clean. After that I read only the clone.
- **What I read in full or in large part:**
  - `CLAUDE.md`, `AGENTS.md` (v34), `local.rules.md`, `README.md`
  - the three hook configurations: `.claude/settings.json`, `.codex/hooks.json`, `.cursor/hooks.json`
  - `.agents/README.md` and `.agents/glossary.md`
  - the `recall` and `conclude` skills, the head of the `dream` skill
  - the questions mechanism's doc and rules file
  - the wake, window and hook code of `.agents/scripts/gw/questions.py` (lines 940–1420), and the header of `docs_corpus.py`
  - `docs/README.md`, `docs/pacer.md`, `docs/architecture.md` up to the question store, `docs/questions/q-0027`, `q-0018.0004`, `q-0001.0018`
  - rule failures 4, 14, 16 and 18
  - the head of session record 0039
  - the structure of the delivery queue `docs/tickets/README.md`, and the design and results of the window test (`docs/research/window-test-2026-09-28.md`)
- **What I ran.** `questions.py --wake` twice inside the clone, to see what a session-start hook actually pushes.
  - Each run registered a session in the clone's `docs/questions/sessions`. I reverted that file each time.
  - The script also keeps "window fingerprints" outside the tree, in the system temp directory under `questions-windows/`, keyed by tree. While cleaning up I deleted that directory once. That also deleted the fingerprints the **live** repository's sessions keep there. The likely effect is harmless: each live session's next prompt hook draws the full window instead of the one-line "unchanged" notice. Still, I touched state outside my clone, and you should know.
- **What I did not read.** Ticket bodies, RFCs, most session records, most research files, the questions skill, and the mechanism-shape and maintain mechanisms. Of the earlier outside pass, `docs/research/discover-what-this-is.md` (2026-09-26), I read only the outline. Its families cover the whole harness (spec-driven workflow packs, harness engineering, a product line, a quality system), not its recall structure. I did not build on it.
- **Web.** Searches and fetches for the 2025–2026 field. Sources are dated in place and listed at the end. Many of the recent numbers are vendor self-reports, and I mark those.

### The recall structure as observed

**Pushed with no retrieval action** (the glossary calls this *tier 1*):

1. **The entry file, at session start, by the host.** Claude Code loads `CLAUDE.md`, which imports `AGENTS.md`; Codex reads `AGENTS.md` natively. It is 232 lines and 15 KB, and holds the general rules, the loop, and *installed blocks*. Those blocks are rules written once in a mechanism's rules file and copied in by an installer; the agent may not edit them. The file is versioned, and the first reply must echo the version line as evidence that it was delivered.
2. **Skill descriptions, at session start, by the host's skill loader.** There are 24 of them, about 5 KB. A skill's body loads only when the skill is invoked. The entry contract rules that a description names use cases only, because it is "paid by every session".
3. **The wake read, at session start, by the `SessionStart` hook** (`questions.py --hook <host>`). One run in the clone gave 104 lines, about 10.8 KB. It holds:
   - the five open questions with the highest *struck* count, a counter the script bumps when a question is reached again 12 hours or more after its last stamp
   - every registered session's state: over fifty lines, nearly all of them ended sessions
   - deferred questions with their re-check conditions
   - *straw dogs due* (provisional text whose question has now been answered)
   - *suspect* entries (answers under a parent whose answer changed)
   - all roots of the question tree
   - the session's window
4. **The window, before every user message, by the `UserPromptSubmit` hook** (Claude Code and Codex; Cursor only at start). It shows:
   - the path from the root to the session's current question
   - every child of every question on that path
   - the open questions under the current root
   - the other roots, and the other running sessions

   If neither the position nor any entry has changed (checked by a hash of the store's bytes), it is one line that names the act to perform. After a compaction the fingerprint is forgotten and the next window is drawn whole. The code's docstring states the selection rule: it "prints position, never relevance".
5. **Outside the repository**, the host's own auto-memory index. In Claude Code that is the first 200 lines or 25 KB of `MEMORY.md`.

**Pulled by the agent** (*tier 2*):

- **`/recall`, made mandatory by a tier-1 rule** ("Run /recall first in every session, whatever the first message says").
  - The agent reads the delivery queue `docs/tickets/README.md`: 58 KB, one line of which, the "Completed step" history, is 36 KB.
  - It also reads the last session records, the open tickets, the architecture, `git status` and the log.
  - It follows references "until they converge".
  - It must cite where an open question is *still* open, or else treat it as settled.
  - It takes the next item from the order the queue states and does not re-rank it.
- **How the agent finds things:** markdown links with anchors, the host's own grep/glob/read tools, and the ids of the question store. No component of the repository embeds, indexes or ranks text by content. The link graph is kept resolvable by machinery instead: a mover repairs citations, and a re-parent renames ids across all records.

**Reachable only if you already know it exists** (*tier 3*): `done/` archives and `docs/research/`.

**The write path:**

- **Per turn:** before drafting, the agent classifies every user message into a kind of turn ("on a question", "a new question", "a process", "uncharted", "banter"). For a question it calls `at` on the lowest question that contains the message, or `open`s a new one. These calls are written as they happen.
- **At `/conclude`:** a narrative session record, a one-line *lean* (the current leaning) on each question touched, and `--end`.
- **Consolidation:**
  - `/maintain` repairs drift and archives finished work.
  - `/dream` is a once-a-day free-associative pass written to `docs/dreams/`.
  - The rule-failure register turns a rule that did not fire into a reworded rule.

## Families

Each family is a whole alternative account. Where two disagree, I leave them disagreeing. Confidence is given per claim: **H**igh, **M**edium, **L**ow.

### A. A tiered virtual context: the memory-hierarchy account (MemGPT/Letta lineage, Claude Code's file memory)

**Mapping.**
- The repository's own *tier 1 / tier 2 / tier 3* corresponds to main context, paged-in external storage, and storage reachable only by address. **H**
- The **hooks are the pager**:
  - `SessionStart` loads the working set.
  - `UserPromptSubmit` refreshes it.
  - The fingerprint plays the role of a validity bit: unchanged means don't reload.
  - `PostCompact`/`preCompact` forgets the fingerprint, which works like invalidation on eviction. **H**
- **Installed blocks are read-only core memory written by an installer.** This is the opposite of Letta's agent-editable memory blocks. **H**
- **`/maintain` and `/dream` correspond to sleep-time consolidation** ([Letta, Apr 2025](https://arxiv.org/abs/2504.13171)), except that a session runs them by hand rather than a background agent. **M**
- **Session records and leans are agent-written notes**, the "structured note-taking" of [Anthropic, 29 Sep 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). **H**

**Where it sits on the family's ladder.** There is no canonical ladder; this one is my reading of the field, so **M**:

| level | what it is | examples |
|---|---|---|
| 0 | stateless | |
| 1 | a static instruction file | |
| 2 | static file plus agent-written notes | Claude Code's `CLAUDE.md` plus auto memory; [Copilot Memory, Jan 2026](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) |
| 3 | the LLM pages its own memory with tool calls | [MemGPT, 2023](https://arxiv.org/abs/2310.08560) |
| 4 | background consolidation agents over versioned memory | [Letta Context Repositories, 12 Feb 2026](https://www.letta.com/blog/context-repositories): git-backed markdown memory, sleep-time reflection in a worktree |
| 5 | learned memory policies | e.g. Memory-R1 / MEM1-style RL |

This repository has level 2 in full. It adds a **scripted pager**: deterministic, structure-chosen pushes on every message, which fits neither level 2 (static) nor level 3 (the LLM's own choice). It reaches level 4 only by hand. **M**

**How this shape goes wrong, by what the family knows.**
- **Pushed context rots as it grows.** Accuracy falls with input length, and similar-but-irrelevant material actively misleads ([Chroma, Jul 2025](https://research.trychroma.com/context-rot)); position effects persist ([Liu et al., 2023/TACL 2024](https://arxiv.org/abs/2307.03172)). **H**
- **Repository instruction files can cost more than they give.** Across agents, context files tended to lower task success and raised inference cost by over 20% ([ETH Zurich/LogicStar, arXiv 2602.11988, Feb 2026, ICLR 2026](https://iclr.cc/virtual/2026/10021235)). **H** that the study says this; **M** that it transfers here, since it measured task completion, not cross-session continuity.
- **The host itself caps what it pushes.** Claude Code recommends `CLAUDE.md` under 200 lines and truncates `MEMORY.md` at 200 lines or 25 KB ([Claude Code docs](https://code.claude.com/docs/en/memory)). **H**
- **Here, before the first pull,** the push is roughly 15 KB entry file + 5 KB descriptions + 11 KB wake. The wake has a component that grows without bound: one line per registered session, ended ones included. **H** (measured)
- **Budgeted curated memory loses on long tenure.** A budgeted "curated map" fell from 96% to 72% recall between 3 and 9 weeks, through eviction, while a provenance-typed graph rose to 90% ([Spencer, arXiv 2607.21962, Jul 2026](https://arxiv.org/abs/2607.21962)). That is one author and six users. **L–M**
- **A pushed copy goes stale against its source.** Observed in my own preload: v33 against `HEAD`'s v34. **H**

**Peers:** Letta/MemGPT; Letta Code; Claude Code `CLAUDE.md` with path-scoped rules and auto memory; Copilot Memory; [claude-mem](https://docs.claude-mem.ai/hooks-architecture), whose SessionStart hook pushes an index of recent summaries, with SQLite full-text search and optional Chroma; [Kiro steering](https://kiro.dev/docs/web/memory/) with "always included" files.

### B. Agent-driven navigation from curated hubs: the "just-in-time" / agentic-search account

**Mapping.**
- **`/recall` is an agentic search loop with a stopping rule:** "follow its references until they converge". **H**
- **Links with anchors are the "lightweight identifiers"** that just-in-time agents load on demand ([Anthropic, Sep 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). **H**
- **The mover's citation repair and the id renaming are index maintenance**: the identifiers are kept resolvable instead of building a content index. **H**
- **The queue, the architecture and the window are hubs** the search starts from. The queue's stated order is a ranking stored in the corpus, not computed at query time ("do not re-rank"). **H**
- **"Cite where it is still open, otherwise it is settled" is a verification requirement on what was retrieved**, close to Copilot Memory's check of citations at use. **M**
- **The glossary's controlled vocabulary**, including its "_Avoid_" lists, is the classic answer to the vocabulary-mismatch problem that keyword navigation suffers from ([Furnas et al., 1987](https://doi.org/10.1145/32206.32212)). **M**

**Ladder.**

| level | what it is |
|---|---|
| 1 | single-shot embedding RAG |
| 2 | iterative tool-use search |
| 3 | iterative search from curated entry points: a hub file, a progress log, a ranked queue |
| 4 | retrieval policies trained by RL (Search-R1 family) |

This repository sits at **3**. **M**

**How this shape goes wrong.**
- **Hubs accrete.** The queue file every `/recall` reads is 58 KB, and its history line alone is 36 KB. **H** (measured)
- **The agent may not read a hub's prose as its criterion.** In rule failure 14, a recall ranked by its own criterion because the ordering rule sat in the queue's prose. **H** (from the record)
- **Stopping is unsolved.** "Converge" has no count. **M**
- **Needs shift during the search** (berrypicking: [Bates, 1989](https://doi.org/10.1108/eb024320)). **M**
- **Navigation by exact identifiers misses paraphrase.** Cursor's A/B found grep plus semantic search beat grep alone ([Cursor, 6 Nov 2025](https://cursor.com/blog/semsearch)). **H** that they report it; it is a vendor study.

**Peers:**
- Claude Code: vector RAG dropped for grep/glob before launch, per Boris Cherny ([reported via Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny); **M**, since secondary)
- [Cline, 2025](https://cline.bot/blog/why-cline-doesnt-index-your-codebase-and-why-thats-a-good-thing)
- [Anthropic's long-running harness, 26 Nov 2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): each session reads `claude-progress.txt`, the git log and `feature_list.json`, then runs `init.sh`. This is the closest published peer of `/recall` plus the queue. **H**
- [Beads](https://github.com/steveyegge/beads) (Oct 2025 onward): a git-backed dependency graph of issues, with a "ready work" query at boot. **H**

### C. A classification scheme with mandatory cataloguing: the library/taxonomy account (the question store and its window)

**Mapping.**
- **The question tree is an enumerative hierarchical schedule.** **H**
- **Ids like `q-0018.0020.0005` are expressive hierarchical notation**, decimal-classification style: the identifier encodes position. **H**
- **Re-parenting renames the subtree's ids everywhere.** That is reclassification under expressive notation. **H**
- **Placing a message on "the lowest question that contains it" is the cataloguer's rule** of classing in the most specific class. **H**
- **"One that only resembles it is not its home" separates aboutness from resemblance.** **M**
- **A "missing parent" is a schedule that lacks a class**, added only when material demands it (literary warrant; compare the entry file's "One shape is not a class"). **M**
- **"Uncharted" is referral to the classification authority, the user.** **H**
- **`depends on` is a see-also cross-reference.** **H**
- **The window is shelf-browsing around the current call number.** **H**
- **The window test** (795 to 30,000 synthetic entries) is a placement evaluation for this browse interface. Near placements stayed exact; far ones landed on the right root. **H** (from the record)

**Ladder** (classification theory): enumerative single-parent hierarchy → hierarchy with typed cross-references → faceted, combined at classing time → post-coordinate indexing, combined at query time → full-text search. This sits on **rung 2**. **M**

**How this shape goes wrong** (old principles, still cited; e.g. [Svenonius, 2000](https://mitpress.mit.edu/9780262194334/the-intellectual-foundation-of-information-organization/)):
- **Cross-classification.** A single-parent scheme forces one home on an item that has two. Rule failure 18 records five amendments to the placement rule in one day, all of them about where a message belongs. **H** (from the record)
- **Expressive notation is not stable identity.** Inserting a level changes ids, so every reference must be rewritten, and copies of old ids held elsewhere go wrong silently. The store's own deferred q-0001.0013 names this case: a stale id from another session's context landing on a different question. **H**
- **Early structure biases later classing.** **M**
- **Hierarchical directories lost to search as corpora grew** (the Yahoo directory). **M**

**Agent-memory peers:**
- [MemTree](https://arxiv.org/abs/2410.14052) and [H-MEM, Jul 2025](https://arxiv.org/abs/2507.22925): both route new or queried content top-down through a tree, but by embedding similarity.
- [A theory of hierarchical memory, Mar 2026](https://arxiv.org/abs/2603.21564): extraction, coarsening, traversal.

In that theory's terms: extraction here is the agent wording a question; coarsening is parents written by hand; traversal is anchored on the **session's current position**, not on the query, with the LLM's judgement as the router. I found no published system that anchors traversal on position. **L** on that rarity (absence of evidence).

### D. Dependency-directed belief maintenance: the truth-maintenance account

**Mapping** ([Doyle, 1979](https://doi.org/10.1016/0004-3702(79)90008-0); [de Kleer, 1986](https://doi.org/10.1016/0004-3702(86)90080-9)):
- **A question entry is a node**; a decided answer with its link is a **justification**; `depends on` is an antecedent. **H**
- **Marking dependents *suspect* when a parent's answer changes is relabelling.** **H**
- **A deferral with a stated condition is an assumption held until that condition.** **M**
- **A straw dog bound to a question is a derived belief in the text of the tree.** It becomes *due* when its supporting node resolves; "due" is computed at every look and never stored, as TMS labels are computed from justifications. **H**
- **"Do not reopen an accepted decision without new evidence" is the stability of a nonmonotonic system.** **M**

For recall this matters directly. The wake pushes "suspect, to re-read" and "straw dogs due". Those items come back because a **dependency changed**, not because of similarity or recency.

**Ladder:** no recorded dependencies → recorded dependencies checked by hand → automatic propagation in a single context (JTMS) → multiple contexts (ATMS) → graded or probabilistic revision. This sits at **JTMS level**, with a coarse justification test (does the answer's link still cite the work that owns the question). **M**

**How this shape goes wrong.**
- **An unrecorded dependency means silent staleness.** The store concedes as much in its principle "a skipped question is found by impasse". **H**
- **Recording justifications costs effort** (here, calls per event). **H**
- **Invalidation spreads too far.** **M**
- **Dead nodes need collecting** (here, `done/` archival). **H**

**2025–2026 peers:**
- Zep/Graphiti: edges carry validity intervals and are invalidated rather than deleted ([arXiv 2501.13956, Jan 2025](https://arxiv.org/abs/2501.13956)).
- Copilot Memory: verifies a memory against the code it cites at the moment of use and drops it if it fails, rather than propagating invalidity when something is written ([GitHub, 15 Jan 2026](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/)).

These are two recent answers to the same staleness problem: invalidate when written, or verify when used. **H** that both exist.

### E. Design-rationale and organizational memory: the IBIS / Walsh–Ungson account

**Mapping.**
- **The IBIS elements line up:** issue ↔ question, position ↔ lean or answer, argument ↔ the entry body (the store literally calls it "the question's argument") ([Conklin & Begeman, gIBIS, 1988](https://doi.org/10.1145/58566.59297)). **H**
- **ADRs are rationale records, and session records are deliberation minutes.** "The decision's home holds the result … the reasoning stays here" is the classic split between decision and deliberation. **H**
- **Walsh & Ungson's retention bins** ([1991](https://doi.org/10.5465/amr.1991.4278992)) apply: archives ↔ `docs/`; transformations ↔ skills and scripts; structures ↔ mechanisms and switches.
- **Their two retrieval modes map onto this repository's push and pull:** *automatic* retrieval through routine ↔ installed blocks firing inside skills, and the window; *controlled* retrieval ↔ `/recall`'s deliberate search. **M–H**

**Ladder:** minutes → structured rationale capture → rationale linked into artifacts → rationale actually consulted at decision time. Here capture and linking are done. Consultation is **forced by the hook**, which addresses the field's best-known failure: rationale captured and never retrieved. **M**

**How this shape goes wrong.**
- **Capture burden, and the asymmetry between who writes and who benefits** ([Grudin, 1994](https://doi.org/10.1145/175222.175230); [Lee, 1997](https://doi.org/10.1109/64.592267)). Here the writer is the agent paying in tokens, and the beneficiary is the next agent, which shifts but does not remove the asymmetry: the human still pays to read. **M**
- **Premature formalization** ([Shipman & Marshall, 1999](https://doi.org/10.1023/A:1008716330212)). The repository's own *whiteboard* — a question's body where material gathers "until enough has gathered to see its form" — is a response to it. **M**
- **Rationale stores grow faster than they are read.** **M**

**Peers:** gIBIS, Compendium, QOC, [ADRs (Nygard, 2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions); in agents, Beads, Spec Kit and Kiro specs, and Anthropic's `feature_list.json`.

### F. A cognitive memory-systems account (CoALA, plus ACT-R activation)

**Mapping** ([CoALA, 2023](https://arxiv.org/abs/2309.02427); [Memory in the Age of AI Agents, Dec 2025](https://arxiv.org/abs/2512.13564)):
- **The usual memory types:** working ↔ context plus window; episodic ↔ session records and the git log; semantic ↔ architecture, ADRs and glossary; procedural ↔ skills and installed rules. **M**: these labels fit almost any agent system, so they discriminate little.
- **Procedural learning ↔ the rule-failure register amending rules.** This structure matches ACE's generator/reflector/curator roles on an "evolving playbook" ([arXiv 2510.04618, Oct 2025](https://arxiv.org/abs/2510.04618)). **M–H**
- **The specific, structural match: "struck" ↔ ACT-R base-level activation.** Base-level activation ranks memories by how often and how recently they were used, as a predictor of need ([Anderson & Schooler, 1991](https://doi.org/10.1111/j.1467-9280.1991.tb00174.x)). The wake ranks open questions by a count of spaced returns (a gap of 12 hours or more) and shows the top five. Unlike ACT-R, the count has **no decay**. **H** on the structure.

**How this shape goes wrong.**
- **Under activation ranking, items nobody rehearses are forgotten**, which ACT-R treats as adaptive. For open obligations it is the failure. The store names it as its own open question q-0001.0018, "How is an open question that nobody reaches kept from sinking unseen?" **H**
- **Counts without decay saturate**, so old heavily-struck items keep their rank. **M**
- **Recent agent-memory work uses ACT-R decay explicitly**, e.g. [Memory Bear, Dec 2025](https://arxiv.org/abs/2512.20651). **M**

### G. An open-loop review system: the prospective-memory / GTD account

**Mapping:**
- **Capture everything:** a new question is `open`ed on the turn it arises. **H**
- **The trusted system:** the store. **H**
- **Next action:** the lean. **M**
- **Waiting-for:** `depends on`. **M**
- **Tickler:** a deferral with its condition, re-checked at the wake. **H**
- **Review:** the wake and `/maintain`. **H**
- **Event-based prospective memory** ([Einstein & McDaniel, 1990](https://doi.org/10.1037/0278-7393.16.4.717)): straw dogs due and suspect entries come back on an event, not a time. **M**
- **The mechanism's doc names its third level "the hook, after which nothing is left to remember".** That is GTD's own promise. **H** (from the doc)

**Ladder:** head-held → lists → a trusted system with periodic review → reminders triggered by context. This sits at **3**, partly at 4: the window comes with every message. **M**

**How this shape goes wrong.** A system loses trust when review lapses; capture inflates until review becomes too much and is abandoned (the store's 121 live entry files, the wake's 50-plus session lines). **M**

**Peers:** [Beads](https://github.com/steveyegge/beads)' ready queue, Claude Code Tasks (persisted across sessions; reported as Beads-inspired by [a secondary source](https://www.morphllm.com/beads-agent-memory), **L**), Anthropic's feature list.

## Its recall structure against the 2025–2026 field

| axis | this repository | where the field is (dated) |
|---|---|---|
| Pushed at start | Versioned entry file; skill descriptions; a wake chosen by **structure**: frequency of return, session states, deferral conditions, dependency triggers, all roots | Instruction files plus agent notes capped by size (Claude Code docs); **most recent** memories (Copilot, Jan 2026); recent summaries as an index (claude-mem); "always included" steering files (Kiro) |
| Pushed per message | A **position-anchored** slice of a question tree, suppressed by hash when unchanged | Rewriting the to-do list at the end of context each step, against lost-in-the-middle ([Manus, Jul 2025](https://www.marktechpost.com/2025/07/22/context-engineering-for-ai-agents-key-lessons-from-manus/)); per-prompt injection hooks in memory plugins |
| Chosen by | A script that sees position, never content; the LLM then judges where the message belongs | Embedding plus keyword plus entity fusion ([Mem0 report, Oct 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026), vendor); recency (Copilot); LLM-planned traversal of trees (MemForest, 2026) |
| Pulled | Mandatory `/recall`: link-following from hubs, host grep, no index of its own | Agentic search (Claude Code, Cline); hybrid grep plus semantic (Cursor, Nov 2025); filesystem tools (Letta, Aug 2025) |
| Staleness | Suspect propagation; "due" derived at every look; "cite where it is still open" | Edge invalidation (Zep, 2025); verify when used, expire after 28 days unused (Copilot, Jan 2026) |
| Consolidation | `/maintain`, `/dream`, rule-failure rewording, all by hand in-session | Background sleep-time reflection into git-backed memory (Letta, Feb 2026); curated incremental playbooks (ACE, Oct 2025) |
| Concurrency | A shared sessions file; each session sees the others' positions | Git branching of memory across subagents (Letta Context Repositories); git-merged issue JSONL (Beads) |

**Checking the claim "embedding-similarity retrieval is becoming outdated for agent memory."**

1. **Supported, narrowly.** In **coding agents searching code**, single-pass embedding RAG as the *main* access path has been displaced by iterative tool use:
   - Claude Code dropped its vector DB before its Feb 2025 launch (Cherny, via secondary reports). **M**
   - Cline does not index (2025). **H**
   - Anthropic advises just-in-time retrieval plus a hybrid, some data retrieved up front (29 Sep 2025). **H**
2. **Not supported as stated.**
   - Cursor's A/B tests (6 Nov 2025) show **grep plus semantic search** beating grep alone, by 12.5% average offline accuracy and small online gains. Cursor trains its own embedding model. **H** (vendor)
   - Mem0's October 2026 report still makes vector similarity a core signal, fused with keyword and entity matching. **H** that they say so (vendor)
   - Letta's widely cited "a filesystem beats Mem0" result (12 Aug 2025: 74.0% LoCoMo on gpt-4o-mini) used a `search_files` tool that **is** embedding search. It is evidence about the agent controlling retrieval, not against embeddings. **H**
   - The hierarchical-memory systems of 2025–2026 (H-MEM, MemTree, MemForest) mostly route by embeddings. **M**
3. **What the 2026 evidence does support** is that embedding similarity is weak in particular conditions:
   - **State that changes.** MERIT ([arXiv 2609.05441, Jul 2026](https://arxiv.org/abs/2609.05441)): embedding retrieval 0.30–0.95 on updated information, structured storage and LLM summaries 0.70–1.00. Agents also acted correctly on a correctly retrieved value only 55% of the time. **M**: one paper, fetched at abstract level.
   - **Exact identifiers.** **M**
   - **Distractors that look alike** (Chroma, Jul 2025). **H**
   - **Logical retrieval steered by the LLM** over an inverted index is reported to match hybrid baselines ([arXiv 2605.27123, May 2026](https://arxiv.org/abs/2605.27123)). **L**: abstract-level, no numbers seen.
4. **Where the field's attention has moved:** from *which retriever* to *who controls retrieval, and how memory is written, curated and verified.**
   - Letta (Aug 2025): "memory is more about how agents manage context".
   - ACE (Oct 2025): context collapse under iterative rewriting.
   - Copilot (Jan 2026): verify when used.
   - The tenure study (Jul 2026): badly written facts failed 24% of the time against 2% for well-written ones.

   Benchmark numbers are contested and mostly self-reported (Mem0's own [benchmarks guide](https://mem0.ai/blog/ai-memory-benchmarks-in-2026)). **H** that they are contested.

**Where this repository's recall falls, in those terms.**

- **No similarity retrieval anywhere.** Every push is chosen by structure: position, a return count, a state, a dependency. Every pull is the agent navigating links. **H**
- **Its retrieval risk sits mostly on the write side and the routing side**, which is where the 2026 evidence also points:
  - every message is classified by the LLM into a single-parent tree (rule failure 18: four strikes in one day)
  - the hubs grow by accretion (the queue's 36 KB line)
  - the wake carries a session list that grows with history
  - the pushed entry file is a few kilobytes above the host's recommended size

  **H** (measured or from the records)
- **Closest published peers by recall structure:**
  - Anthropic's long-running harness: progress file, git log and feature list read at boot
  - Beads: a dependency graph plus a ready query, in git
  - Letta Context Repositories: git-backed markdown memory with sleep-time reflection
  - Copilot Memory: verify when used
- **Not found in any peer:** a per-message hook that pushes a position-anchored slice of a persistent question tree, with the agent required to place each message in that tree before replying. **L–M** (absence of evidence after targeted search)

## What the tasking smuggled in

- **"A session that starts with no memory."** It does not. Before its first token the host has pushed:
  - the entry file
  - 24 skill descriptions
  - the hook's wake
  - the user's auto-memory index, which lives outside the repository

  My own context arrived carrying three of these, one of them a version stale. The real question is what the starting load is and how fresh it is, not how to get from nothing to something.
- **"Get to what it needs."** This frames recall as need-driven retrieval. Much of this repository's recall is **position-driven** (the window shows where you stand, "never relevance"), **obligation-driven** (tier-1 rules force reads), and **dependency-driven** (suspect and due). A need-driven framing makes those look like inefficient retrieval, not what they are.
- **Push/pull as the axes.** This is the subject's own vocabulary: the glossary's tier 1, 2 and 3. An outside frame would use different axes, for example:
  - *who controls what the model sees*: script, model or human
  - *write discipline*: the 2026 evidence ties recall quality to how facts are written
  - *verify when written versus verify when used*
- **"The state of the art" as a single frontier.** The families above have different ladders. The repository is near the top of some (forced consultation of rationale; dependency-triggered recall) and low on others (no consolidation running in the background, no content search). One frontier would harmonise what disagrees.
- **The embedding claim treats the retriever's mechanism as the variable.** Its subject is ambiguous between three things: code search, conversational memory, and document RAG. The evidence differs for each. The field has moved to control and curation, which the claim's framing does not reach.
- **"Memory" itself is the subject's self-description.** The README calls it "institutional memory". Families C, D and E describe a classification scheme, a belief-maintenance system and a rationale system, each of which a memory framing absorbs.
- **The singular "a session".** The store holds a shared sessions file. Recall among concurrent sessions (seeing, and not re-ranking, what another running session is on) is a coordination problem, and the singular framing hides it.
- **"Be current", plus a 2025–2026 window.** Recent sources on this topic are dominated by vendor posts and their benchmarks (Mem0, Cursor, Letta, GitHub, Anthropic). The evidence base tilts toward what vendors measure.

## Nothing to take

These are families I considered and refused, because I could not state a structural mapping:

- **Vector-store / embedding RAG memory.** No component computes similarity or keeps an index of content. The LLM judging "resembles" against a shown list is classification (family C), not similarity retrieval.
- **Temporal knowledge graph with entity extraction** (Zep/Graphiti as a whole). Its nodes are entities and facts pulled from conversation, with validity intervals. Here nodes are questions written by hand, and the only time data is strike stamps and authority dates. The part that does map, invalidation, is family D.
- **Learned memory or retrieval policies** (Memory-R1, MEM1, Search-R1). Nothing is trained.
- **Event sourcing / log-structured memory.** The calls are one per event, but the store keeps snapshots. History is git's, and nothing is replayed.
- **Stuffing the whole history into a long context.** The design selects at every step; nothing maps.
- **Blackboard architecture.** Store ↔ blackboard and skills ↔ knowledge sources would map. The defining part, a control component that schedules them, does not exist: the pacer is "idea under alignment". So the mapping covers only a data structure.
- **Parametric memory** (fine-tuning). None.

## Sources

Agent memory and context, 2025–2026:
- Anthropic, *Effective context engineering for AI agents*, 29 Sep 2025 — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, *Effective harnesses for long-running agents*, 26 Nov 2025 — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Claude Code docs, *How Claude remembers your project* (`CLAUDE.md`, rules, auto memory), read 2026-10-08 — https://code.claude.com/docs/en/memory
- Letta, *Benchmarking AI Agent Memory: Is a Filesystem All You Need?*, 12 Aug 2025 — https://www.letta.com/blog/benchmarking-ai-agent-memory
- Letta, *Context Repositories*, 12 Feb 2026 — https://www.letta.com/blog/context-repositories
- Letta et al., *Sleep-time Compute*, Apr 2025 — https://arxiv.org/abs/2504.13171
- GitHub, *Building an agentic memory system for GitHub Copilot*, 15 Jan 2026 — https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/
- Cursor, *Improving agent with semantic search*, 6 Nov 2025 — https://cursor.com/blog/semsearch
- Cline, *Why Cline doesn't index your codebase* (2025) — https://cline.bot/blog/why-cline-doesnt-index-your-codebase-and-why-thats-a-good-thing
- Pragmatic Engineer, *Building Claude Code with Boris Cherny* — https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
- Secondary account of the Claude Code RAG decision — https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/
- Manus context engineering, summarised Jul 2025 — https://www.marktechpost.com/2025/07/22/context-engineering-for-ai-agents-key-lessons-from-manus/
- Chroma, *Context Rot*, Jul 2025 — https://research.trychroma.com/context-rot
- ETH Zurich / LogicStar.ai, *Evaluating AGENTS.md*, arXiv 2602.11988, ICLR 2026 — https://iclr.cc/virtual/2026/10021235
- Zhang et al., *Agentic Context Engineering (ACE)*, arXiv 2510.04618, Oct 2025 — https://arxiv.org/abs/2510.04618
- *Memory in the Age of AI Agents: A Survey* (NUS, Renmin, Fudan, PKU et al.), arXiv 2512.13564, Dec 2025 — https://arxiv.org/abs/2512.13564
- Mem0, *State of AI Agent Memory 2026*, Oct 2026 (vendor) — https://mem0.ai/blog/state-of-ai-agent-memory-2026
- Mem0, *LoCoMo vs. LongMemEval vs. BEAM* (vendor) — https://mem0.ai/blog/ai-memory-benchmarks-in-2026
- Mishra & Mishra, *When Does Memory Help? (MERIT)*, arXiv 2609.05441, Jul 2026 — https://arxiv.org/abs/2609.05441
- Spencer, *Ground Truth First … Tenure Crossover*, arXiv 2607.21962, Jul 2026 — https://arxiv.org/abs/2607.21962
- Zeng et al., *Rethinking Agentic RAG: LLM-Driven Logical Retrieval Beyond Embeddings*, arXiv 2605.27123, May 2026 — https://arxiv.org/abs/2605.27123
- Talebirad et al., *Toward a Theory of Hierarchical Memory for Language Agents*, arXiv 2603.21564, Mar 2026 — https://arxiv.org/abs/2603.21564
- *H-MEM: Hierarchical Memory for … LLM Agents*, arXiv 2507.22925, Jul 2025 — https://arxiv.org/abs/2507.22925
- *MemTree: Dynamic Tree Memory Representation*, arXiv 2410.14052 — https://arxiv.org/abs/2410.14052
- *MemForest*, arXiv 2605.23986, 2026 — https://www.alphaxiv.org/abs/2605.23986
- Rasmussen et al., *Zep: A Temporal Knowledge Graph Architecture for Agent Memory*, arXiv 2501.13956, Jan 2025 — https://arxiv.org/abs/2501.13956
- *Memory Bear* (ACT-R base-level activation in agent memory), arXiv 2512.20651, Dec 2025 — https://arxiv.org/abs/2512.20651
- Packer et al., *MemGPT*, arXiv 2310.08560, 2023 — https://arxiv.org/abs/2310.08560
- Sumers et al., *CoALA*, arXiv 2309.02427, 2023 — https://arxiv.org/abs/2309.02427
- Liu et al., *Lost in the Middle*, arXiv 2307.03172 — https://arxiv.org/abs/2307.03172
- Beads (Yegge), git-backed dependency-aware issue tracker for agents — https://github.com/steveyegge/beads
- Beads and Claude Code Tasks, secondary (vendor) — https://www.morphllm.com/beads-agent-memory
- claude-mem hooks architecture — https://docs.claude-mem.ai/hooks-architecture
- Kiro steering / memory docs — https://kiro.dev/docs/web/memory/

Principles (older, still cited):
- Doyle, *A Truth Maintenance System*, 1979 — https://doi.org/10.1016/0004-3702(79)90008-0
- de Kleer, *An Assumption-based TMS*, 1986 — https://doi.org/10.1016/0004-3702(86)90080-9
- Conklin & Begeman, *gIBIS*, 1988 — https://doi.org/10.1145/58566.59297
- Walsh & Ungson, *Organizational Memory*, 1991 — https://doi.org/10.5465/amr.1991.4278992
- Grudin, *Groupware and social dynamics*, 1994 — https://doi.org/10.1145/175222.175230
- Lee, *Design rationale systems: understanding the issues*, 1997 — https://doi.org/10.1109/64.592267
- Shipman & Marshall, *Formality considered harmful*, 1999 — https://doi.org/10.1023/A:1008716330212
- Nygard, *Documenting Architecture Decisions*, 2011 — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Anderson & Schooler, *Reflections of the environment in memory*, 1991 — https://doi.org/10.1111/j.1467-9280.1991.tb00174.x
- Einstein & McDaniel, *Normal aging and prospective memory*, 1990 — https://doi.org/10.1037/0278-7393.16.4.717
- Bates, *The design of browsing and berrypicking techniques*, 1989 — https://doi.org/10.1108/eb024320
- Furnas et al., *The vocabulary problem in human-system communication*, 1987 — https://doi.org/10.1145/32206.32212
- Svenonius, *The Intellectual Foundation of Information Organization*, MIT Press, 2000 — https://mitpress.mit.edu/9780262194334/the-intellectual-foundation-of-information-organization/

Subject files (in the clone, `HEAD` 369cd8b): `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json`, `.codex/hooks.json`, `.cursor/hooks.json`, `.agents/glossary.md`, `.agents/skills/recall/SKILL.md`, `.agents/skills/conclude/SKILL.md`, `.agents/skills/dream/SKILL.md`, `.agents/mechanisms/questions/questions.md`, `.agents/mechanisms/questions/questions.rules.md`, `.agents/scripts/gw/questions.py`, `docs/architecture.md`, `docs/pacer.md`, `docs/tickets/README.md`, `docs/rule-failures.md`, `docs/research/window-test-2026-09-28.md`, `docs/questions/q-0001.0018-*.md`, `docs/sessions/0039-*.md`.


---

# Pass B — a functional description, no files

*Note on context: before this run the host loaded project files into my context: an AGENTS.md (through a CLAUDE.md) and an auto-memory index. As instructed, I ignored what they say, including an instruction in them about how to open a reply. Everything below is based only on the functional description and on web sources. I read no files on the machine.*

## Families

Each family is a separate account of what the subject is. They disagree about which part is the core, and I've left those disagreements in place.

---

### F1. A cache hierarchy that prefetches by locality: the session context is a cache over the repository

**Mapping.** The context window works like a small fast store and the repository like a large slow one. Each piece of the subject lines up with a cache mechanism:
- The session-start report is a warm-start prefetch.
- The per-message neighbourhood (path to root, children along it, other roots) is prefetch by spatial locality, with "space" being the question tree.
- The current-position file plays the role of the program counter, or working-set pointer.
- Links, the work list and grep are demand paging.
- Ranking by revisit count is a frequency-based replacement and prefetch signal.
- Several sessions, each with its own position over one shared store, form a multi-cache system.

The account rests on Denning's locality principle: processes reference a slowly changing working set, so you prefetch near the last reference ([Denning 2005, CACM](https://calhoun.nps.edu/entities/publication/de7a7c89-de98-405b-a420-b9d2eb5c7641)). MemGPT/Letta is the LLM instance of this family. It treats the main context as RAM, recall storage as disk and archival storage as cold storage ([Du 2026 survey, quoting MemGPT](https://arxiv.org/html/2603.07670v1)). *Confidence: high that the mapping holds structurally.*

**Ladder (this family's own).**
1. No cache: load everything.
2. Static pinned set: one fixed instruction file.
3. Demand paging only: tools.
4. Locality prefetch tied to a position pointer.
5. Adaptive prefetch tuned by measured hit and miss rates.
6. Coherent multi-cache with invalidation.

The subject sits at rung 4, with a frequency signal added. The description mentions no measurement of whether pushed material was used (a hit) or whether the session had to fetch something the push missed. That measurement is what defines rung 5. The rung-6 material is partial: other sessions' positions are pushed, but nothing invalidates a session's held context when another session changes a record. *Confidence: medium. The rungs are my reading of standard cache design, not a published ladder for LLM agents.*

**Known failure modes.**
- **Thrashing.** When the working set is larger than the cache, the system spends its time on fetches. For an LLM this is context rot: performance falls as input grows, well below the window limit ([Chroma, July 2025](https://trychroma.com/research/context-rot)).
- **Pollution.** Prefetched lines that are never used push out useful ones.
- **Locality only as good as the address space.** Prefetch helps only when the index's notion of "near" matches the access pattern. If the tree's parent/child adjacency doesn't match how work actually moves, the prefetch is wasted.
- **Coherence.** Concurrent writers make cached copies stale.

*Confidence: high for these as general behaviour; medium for how each applies here.*

**Peers.** [MemGPT/Letta](https://arxiv.org/abs/2310.08560); [Letta Context Repositories](https://www.letta.com/blog/context-repositories) (Feb 2026: git-backed memory files, with subagents resolving divergence through git); Anthropic's "just-in-time" context, which keeps light identifiers and loads content through tools ([Anthropic, Sep 29 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

---

### F2. Declarative memory driven by activation: a cognitive model of what to bring to mind

**Mapping.** ACT-R's account is that retrieval probability follows a rational estimate of need. That estimate has two parts:
- **Base-level activation:** frequency and recency of past use, with spacing effects.
- **Spreading activation:** from whatever is currently in focus.

Anderson & Schooler showed that the environment's statistics of need produce exactly these repetition, delay and spacing effects ([Anderson & Schooler 1991](https://www.psychologicalscience.org/journals/psychological-science/volume/2/issue/6/)). In the subject:
- "Count a return only after a gap of hours, and rank by the count" is a spaced-repetition-gated base level, close in spirit to the activation account of the spacing effect (Pavlik & Anderson 2005).
- The neighbourhood of the current position is spreading activation from the focus.
- The "deferred items whose conditions may now hold" are cue-driven prospective-memory retrieval.

The LLM instance is Generative Agents, which scores memories by recency × importance × relevance ([Park et al. 2023](https://arxiv.org/abs/2304.03442)). Hindsight's retrieval includes graph spreading activation (2 hops, decay 0.6) next to semantic, BM25 and temporal channels ([Vectorize/Hindsight, Dec 2025](https://vectorize.io/blog/hindsight-building-ai-agents-that-actually-learn)). *Confidence: high that the mapping holds; medium on the spacing detail.*

**Ladder.**
1. Recency only.
2. Frequency only.
3. Base level: frequency with decay.
4. Base level plus spreading activation from context.
5. Weights fitted to observed need.

The subject has gap-gated frequency and structural spreading. The description mentions no decay, which puts it between rungs 2–3 and 4. Nothing is fitted. *Confidence: medium.*

**Known failure modes.**
- **Frequency without decay entrenches.** Old, often-revisited items keep their rank after the need has gone. Base-level learning exists to avoid this.
- **Spreading activation only works through the associative links that exist.** A relevant item with no edge to the focus gets nothing. Here the edges are tree edges and dependencies.
- **Revisit counts mix two signals.** An item can be revisited because it's important or because it's stuck. The family doesn't separate these. That is a gap in the family's knowledge, not a finding.

*Confidence: medium.*

---

### F3. Issue-based argumentation and design rationale (IBIS, QOC, ADRs): the tree is the product

**Mapping.** IBIS represents deliberation as a graph of Issues (questions), Positions and Arguments ([Kunz & Rittel 1970; Conklin & Begeman gIBIS 1988](https://eight2late.com/category/issue-based-information-system/page/6)). In the subject:
- The question tree with parents is the issue graph.
- The "current leaning" is the currently favoured Position.
- The free-text body is the Arguments, left untyped.
- "Depends on" is an issue-to-issue link.
- Creating a unit of work only after the argument is worked out is the IBIS move from deliberation to action.
- The standing decision documents are ADRs ([Nygard 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).

On this account recall is secondary. What gets stored is rationale, and the push mechanisms are a way of keeping the open issues in front of the deliberators. *Confidence: high that the mapping holds.*

**Ladder.**
1. Issue lists.
2. Typed IBIS graphs.
3. Facilitated live mapping (Conklin's dialogue mapping).
4. Rationale linked to artifacts (traceability).
5. Rationale reused across projects.

The subject sits at rung 4: questions link forward to work units and decisions, and the body is semi-formal. *Confidence: medium.*

**Known failure modes (old and still cited).**
- **The capture problem.** Rationale tools demand substantial time to enter information and change how designers work, so rationale goes unrecorded or out of date (Conklin & Yakemovic 1991; Lee 1997; summarised in [Hooey, NASA 2007](https://human-factors.arc.nasa.gov/groups/HCSL/publications/Hooey_KM2007.pdf)). Captured artefacts need immediate payoff to the person entering them.
- **Formality.** Users won't or can't make structure explicit. Typed formal argument schemas get abandoned ([Shipman & Marshall 1999](https://people.engr.tamu.edu/shipman/formality-paper/harmful.html)). The subject's untyped body plus a one-line leaning is the compromise this literature recommends. Its typed fields (state, owner, parent, dependency) are where the literature predicts drift.
- **Trees misrepresent overlapping structure.** "A city is not a tree" (Alexander 1965). Questions with several real parents get forced under one. The subject's separate dependency links are the usual escape hatch.

*Confidence: high for these as general behaviour.*

**Peers.** [Compendium and the gIBIS/QOC lineage, "15 years on"](https://acawiki.org/Hypermedia_support_for_argumentation-based_rationale:_15_Years_on_from_gIBIS_and_QOC); ADR tooling. I found no 2025–2026 LLM-agent system that keeps an IBIS-style open-question tree as its organising memory. Spec-driven tools (GitHub Spec Kit, AWS Kiro) keep specs and tasks, not open questions. *Confidence: medium. Absence of evidence from a limited search.*

---

### F4. Personal information management and orienteering: navigation first, search as last resort

**Mapping.** People finding their own information mostly navigate in small local steps from a known context ("orienteering"). They don't jump straight to the target by query ("teleporting"), even when they know exactly what they want ([Teevan et al., CHI 2004](https://people.csail.mit.edu/teevan/work/publications/papers/chi04.pdf)). Better desktop search did not change this: navigation accounted for 56–68% of retrievals and search for 4–15%, and search was used mainly when the location was forgotten ([Bergman et al., TOIS 2008](https://cris.openu.ac.il/en/publications/improved-search-engines-and-navigation-preference-in-personal-inf-2/)).

In the subject:
- The pushed neighbourhood is the "known starting place".
- Following links is orienteering.
- Grep is the last-resort teleport.
- There is no similarity search.

On this account the subject is a PIM design for an owner who forgets everything between sessions. The push stands in for the human's remembered location. *Confidence: high that the mapping holds. Medium on transferring the finding: the papers study humans, not LLMs.*

**Ladder.** Piles → files (folders) → files plus search → files plus search plus a remembered starting context. Malone's 1983 "piles vs files" line runs into this. The subject has the full set, with the starting context injected rather than remembered. *Confidence: low–medium.*

**Known failure modes.**
- **Lost in hyperspace.** Link-following produces disorientation and cognitive overhead (Conklin 1987, "Hypertext: an introduction and survey"). The breadcrumb, here the path to the root, is the classic remedy.
- **Navigation depends on the filer and the finder sharing a scheme.** Here they are different sessions of the same model, but the scheme was laid down by earlier sessions in a vocabulary later sessions must re-learn.
- **Search as last resort fails silently.** If the starting place is wrong, the finder doesn't know to search.

*Confidence: medium.*

**Recent LLM-side support.** Letta reports that filesystem tools beat a specialised memory layer on LoCoMo because models are post-trained heavily on file operations ([Letta, Aug 12 2025](https://www.letta.com/blog/benchmarking-ai-agent-memory)). PageIndex and LATTICE have the LLM navigate a tree index instead of doing top-k similarity ([PageIndex](https://pypi.org/project/PageIndex/); [LATTICE, arXiv 2510.13217, Oct 2025](https://sotaverified.org/papers/251013217)).

---

### F5. A structured shift-handover protocol: the core is the hand-off, not the store

**Mapping.** Clinical handoff between shifts is the long-studied case of a worker taking over with no memory of the previous shift. I-PASS has five parts: Illness severity, Patient summary, Action list, Situational awareness and contingency planning, Synthesis by receiver. It cut medical errors by 23% and preventable adverse events by 30% across 9 hospitals, without adding time ([Starmer et al., NEJM Nov 2014](https://psnet.ahrq.gov/resources/resource/28485)). In the subject:
- The dated handoff notes are the written sign-out.
- The session-start report is the verbal sign-out.
- "Deferred items whose conditions may now hold" are the contingency plans ("if X, do Y").
- The ordered list of what's next is the action list.
- Saying what the message is before acting is a kind of receiver synthesis.

**Where the mapping is partial.** I-PASS's synthesis is the receiver restating the handed-off state. The subject's gate restates the incoming request, not the inherited state. *Confidence: high for the overall mapping; this partiality is stated as found.*

**Ladder.**
1. Unstructured verbal handoff.
2. Written template.
3. Structured mnemonic with receiver synthesis.
4. Trained, observed and sustained, with audit.

The subject sits between 2 and 3. Sending one session's handoff to the next is automated, but nothing described checks that the receiver took in the handed-off state. *Confidence: medium.*

**Known failure modes.**
- **Handoffs become copy-forward.** Notes are carried forward without being re-verified, and stale items persist.
- **Omission is the main error**, more than distortion.
- **Benefits depend on the sustainability effort, not the template.** I-PASS bundled training, observation and a sustainability campaign.

*Confidence: high for the 2014 result; medium that it transfers.* The direct 2025 LLM peer is Anthropic's long-running harness: a `claude-progress.txt` log, a `feature_list.json` with pass flags, and git history, all read at the start of each fresh session ([Anthropic, Nov 2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)).

---

### F6. Stigmergy and blackboard coordination: the core is the shared positions file

**Mapping.** Stigmergy is indirect coordination: a trace left in a medium triggers later action. It needs no planning, communication, simultaneous presence or mutual awareness ([Heylighen 2016](https://wiki.p2pfoundation.net/Stigmergy_as_a_Universal_Coordination_Mechanism)). Several amnesic sessions coordinating only through files they leave behind fit this exactly. Each session's position marker in a shared file is a marker-based, qualitative trace. Revisit counts are a quantitative trace that strengthens with repetition, like pheromone reinforcement. Blackboard systems are the AI-architecture version: independent knowledge sources read and write a shared structured workspace, under a control component that decides what to attend to (Nii 1986, *AI Magazine*). Heylighen & Vidal already proposed stigmergic GTD for collaborative work ([Long Range Planning 2008](https://web-archive.southampton.ac.uk/cogprints.org/6289/1/Heylighen-Vidal-GTD-Science.pdf)). *Confidence: high that the mapping holds.*

**Ladder (Heylighen's dimensions).** Single-agent → multi-agent; transient → persistent; sematectonic (the work itself is the signal) → marker-based; qualitative → quantitative. Mature systems add **evaporation**, so that unreinforced traces fade. The subject has persistent, marker-based traces of both kinds. Positions of running sessions imply some liveness notion. Revisit counts, as described, don't evaporate. *Confidence: medium.*

**Known failure modes.**
- **Without evaporation, early traces lock in.** Ant-colony optimisation adds evaporation to escape early convergence.
- **Shared-file blackboards suffer write contention and lost updates.**
- **Stale presence markers from crashed workers mislead the others.**
- **Control is the hard part of a blackboard.** Deciding what to attend to is exactly where push-selection policy lives.

Beads is the closest 2025 peer: a git-backed, dependency-aware issue store shared by concurrent agents. It moved from sequential to hash IDs because concurrent agents collided ([Beads](https://pkg.go.dev/github.com/steveyegge/beads@v0.17.7); [overview](https://www.morphllm.com/beads-agent-memory)). Letta Context Repositories resolves divergence between memory subagents through git ([Letta, Feb 2026](https://www.letta.com/blog/context-repositories)). *Confidence: medium–high.*

---

### F7. Desired-state reconciliation and configuration management: the core is the authority sort

**Mapping.** A Kubernetes controller compares declared desired state (`.spec`) with observed state (`.status`) and acts to close the gap. It is level-triggered and re-checks periodically, so a missed event is corrected on the next pass ([Kubernetes docs: controllers](https://kubernetes.io/docs/concepts/architecture/controller/)). The subject's sort by which side is authoritative is this split, made per record kind:
- **Record authoritative permanently** (constraints, decisions): desired state, so repair the thing.
- **Record authoritative until the thing reaches it** (plans, work items): desired state, with a completion condition.
- **Thing authoritative** (generated indexes): observed-state caches, so regenerate, never edit.
- **Neither** (history): an append-only log.

Writing instruction text once and copying it out by script, with drift checks, is configuration management's single source of truth plus drift detection. The separate maintenance step is the periodic resync. *Confidence: high that the mapping holds.*

**Ladder.**
1. Hand-maintained docs.
2. Named owners.
3. Generated artefacts.
4. Drift detection.
5. Declared repair direction per kind.
6. Continuous automatic reconciliation.

The subject sits at rung 5. Its reconciliation is periodic and run as a step (not continuous), and some repairs go through a person. *Confidence: medium.*

**Known failure modes.**
- **Two controllers claiming the same field fight each other** ("flapping"). Here, that would be a record whose kind is ambiguous.
- **Desired state goes stale.** Nobody updates `.spec`, so the reconciler enforces something obsolete. A permanently authoritative decision record has exactly this risk.
- **Drift between resyncs.**
- **A generated artefact edited by hand is silently overwritten.**

*Confidence: high as general behaviour.*

---

### F8. Open-loop and prospective-memory management (GTD): the core is the classify gate and the review

**Mapping.** GTD runs capture → clarify ("what is it? is it actionable?") → organise into next actions, projects, someday/maybe, a tickler and reference → weekly review → engage. In the subject:
- The mandatory "say what the message is" gate is the clarify step: existing open loop, new open loop to be filed under the right project, routine, or nothing.
- The ordered work list is next actions.
- Deferred items surfaced when their conditions may hold are the tickler and someday/maybe.
- Open questions are open loops.
- The maintenance step is the weekly review.

Heylighen & Vidal read GTD as distributed cognition: "actionable" external memories plus opportunistic, situation-dependent execution ([2008](https://web-archive.southampton.ac.uk/cogprints.org/6289/1/Heylighen-Vidal-GTD-Science.pdf)). Masicampo & Baumeister found that making a plan, not finishing the task, is what removes the intrusive pull of unfinished goals ([2011](https://scrapbox.io/nishio/consider_it_done)). That bears on why a recorded "current leaning" lets a question be safely put down. *Confidence: high that the mapping holds.*

**Ladder.** Lists → lists with contexts → full workflow → workflow with a reliable weekly review → collaborative or stigmergic GTD. The subject has the full workflow with a review step and multi-session sharing. *Confidence: medium.*

**Known failure modes (practitioner knowledge, long-standing).**
- **The system is only trusted if the review happens.** Once reviews lapse, users stop trusting the lists and fall back on head-memory. Here there is no head-memory to fall back on, so a lapse fails differently: stale lists get acted on.
- **Over-classification overhead.** Clarify becomes ceremony.
- **Someday/maybe lists grow without bound.**

*Confidence: medium. The sources are mostly practitioner sources, not controlled studies.*

---

### F9. The native family: coding-agent harnesses and context engineering (2025–2026)

**Mapping.** This is the family the subject literally belongs to: repository-resident instruction files, memory files and trackers read by coding agents across sessions. *Confidence: high.*

**Ladder (from the 2025–2026 field).**
1. One instruction file: AGENTS.md / CLAUDE.md.
2. A memory bank read at session start: [Cline Memory Bank](https://docs.cline.bot/prompting/cline-memory-bank), with projectbrief, activeContext and progress files.
3. Progress log plus machine-checkable task list: [Anthropic harness, Nov 2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
4. A structured, dependency-aware, concurrency-safe tracker: Beads.
5. Hook-injected dynamic context. Claude Code's SessionStart and UserPromptSubmit hooks can return `additionalContext` ([hooks overview](https://mlops.community/blog/the-complete-guide-to-claude-code-hooks-automating-your-ai-coding-workflow)), and Agent Skills use progressive disclosure: names and descriptions always loaded, bodies on demand ([Anthropic, Oct 16 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)).
6. Background or model-driven consolidation of memory: Letta sleep-time/context repositories; Mastra's Observer/Reflector ([Feb 2026](https://mastra.ai/research/observational-memory)); ACE's generate/reflect/curate playbooks ([Oct 2025](https://arxiv.org/abs/2510.04618)).

The subject has rungs 1–5. It adds a per-message classification gate that I found no peer for, and a self-revising instruction loop (log the missed rule, then reword it) that resembles rung 6 but is run by hand. *Confidence: medium. The rungs are my synthesis of the cited systems.*

**Known failure modes (recent evidence).**
- **Context files cost more than they return.** Providing context files "does not generally improve task success rates, while increasing inference cost by over 20%"; repository overviews were not helpful; files are useful for non-standard practices ([Gloaguen et al., arXiv 2602.11988, Feb 2026, ICLR 2026](https://arxiv.org/abs/2602.11988)). Another 2026 study found AGENTS.md associated with lower runtime and tokens at comparable completion, and a third found no measurable correctness effect ([search summary of 2601.20404 and 2607.27250](https://arxiv.org/html/2601.20404v2)). *The evidence is mixed.*
- **Instruction density.** Adherence falls as instruction count rises. The best models reach 68% at 500 instructions, with a bias towards earlier instructions ([IFScale, July 2025, NeurIPS 2025](https://arxiv.org/abs/2507.11538)). Per-message pushes add to the density.
- **Context collapse.** Iterative rewriting of a self-maintained playbook erodes detail, and a pull towards brevity drops domain insight ([ACE, Oct 2025](https://arxiv.org/abs/2510.04618)). This bears directly on "reword the instruction when it fails".
- **Benchmark mismatch.** Agents near-perfect on LoCoMo do poorly when memory and action are coupled across sessions ([MemoryArena, Feb 2026](https://arxiv.org/abs/2602.16313)).

---

## Its recall structure against the 2025–2026 field

**What is pushed, when, chosen by what.**

| | Subject | Field, 2025–2026 |
|---|---|---|
| Session start | Report chosen by revisit count, deferred conditions and other sessions' state | ChatGPT (reverse-engineered by one person, Dec 2025): profile facts plus recent-conversation summaries pushed every session, no vector retrieval ([llmrefs](https://llmrefs.com/blog/reverse-engineering-chatgpt-memory); [Gigazine](https://www.gigazine.net/gsc_news/en/20251226-reverse-engineered-chatgpt-memory-system)). Cline and the Anthropic harness: fixed files read at start. Skills: catalogue of names and descriptions always pushed. |
| Per message | Neighbourhood of a *position* in a tree: query-independent, state-dependent | Mem0, Zep and Hindsight: retrieval keyed on the *message*, injected each turn. Zep combines BM25 and cosine similarity over a temporal graph ([Zep, 2025](https://huggingface.co/papers/2501.13956)). Hindsight fuses semantic, BM25, graph spreading-activation and temporal channels ([Vectorize, Dec 2025](https://vectorize.io/blog/hindsight-building-ai-agents-that-actually-learn)). |
| No per-turn change | — | Mastra Observational Memory: a stable, compressed observation log, no per-turn retrieval, so the prompt can be cached; 94.87% on LongMemEval as self-reported ([Mastra, Feb 2026](https://mastra.ai/research/observational-memory)). |

The main structural difference: in the field, per-turn push is chosen by similarity to the query, or the context doesn't change per turn at all. The subject's per-turn push is chosen by **where the session is**, and the mapping from query to place is handed to the model through the classification gate. That makes the model the router, the same move PageIndex and LATTICE make for documents (LLM tree navigation instead of top-k similarity). Two consequences:
- When the gate misclassifies, the next turn's push is wrong.
- Hierarchical classification is known for errors at upper levels spreading downward (Silla & Freitas 2011, *DMKD*).

*Confidence: medium.*

**What is pulled, and how.** Following links, reading the work list, and grep. This matches what coding agents do now:
- Claude Code dropped RAG plus a local vector DB for model-driven glob and grep. Cherny said it "outperformed everything, by a lot", citing stale indexes and permission complexity, per secondary reports of his Latent Space interview, May 2025 ([smartscope summary](https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/)). Anthropic's own guide names grep and glob just-in-time retrieval as the pattern ([Sep 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
- Claude's chat memory is two tools over raw history (`conversation_search`, `recent_chats`), with no pushed profile by default ([Simon Willison, Sep 2025](https://feeds.simonwillison.net/2025/Sep/12/claude-memory/)).
- Anthropic's memory tool is a client-side directory of files the model reads and writes ([docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)).

**Checking "embedding-similarity retrieval is becoming outdated for agent memory."**

Evidence for a shift away from *similarity as the only or main mechanism*:
- **Coding agents.** Claude Code (2025, above) went grep-only.
- **Filesystem memory.** Letta's filesystem agent scored 74.0% on LoCoMo against Mem0's reported 68.5%. Its toolset still included a semantic `search_files`, and Letta itself says LoCoMo tests retrieval, not agentic memory ([Aug 2025](https://www.letta.com/blog/benchmarking-ai-agent-memory)).
- **Theory.** Single-vector embeddings have a hard limit, set by dimension, on which top-k sets they can return; state-of-the-art models fail the simple LIMIT dataset ([Weller et al., Google DeepMind, Aug 2025, ICLR 2026](https://arxiv.org/abs/2508.21038)).
- **Agentic memory benchmarks.** AMA-Bench attributes memory-system underperformance partly to "lossy similarity-based retrieval" and wins with a causality graph plus tool retrieval ([Feb–May 2026](https://arxiv.org/abs/2602.22769)).
- **Structured documents.** An embedding-free agentic reader scored 58.8% against 15.7% for dense retrieval on structured financial documents, but only on 51 questions ([Aug 2026](https://arxiv.org/abs/2608.06305)).
- **No retrieval at all.** Mastra's no-retrieval log (Feb 2026), above.

Evidence against "outdated":
- **Cursor.** Semantic search gave 12.5% higher accuracy on average (6.5–23.5% by model), better code retention in large codebases in an A/B test, and "the combination of these two [grep + semantic] leads to the best outcomes" ([Cursor, Nov 6 2025](https://cursor.com/blog/semsearch)).
- **turbopuffer on Claude Code.** Adding semantic retrieval raised file precision from 65% to 87%, with mixed recall. Semantic search won on behaviourally similar code, grep on explicit references ([AI Engineer Europe 2026](https://www.ai.engineer/talks/zKk7sDMGDEQ-benchmarking-semantic-code-retrieval-on-claude)). This is a vector-DB vendor's talk.
- **Survey.** A March 2026 survey: dense retrieval with FAISS-style approximate nearest-neighbour search "remains the default implementation, often augmented with sparse BM25 and metadata filters" ([Du, arXiv 2603.07670](https://arxiv.org/html/2603.07670v1)).
- **Systematic evaluation.** "No single architecture dominates across all scenarios"; effectiveness depends on matching the memory structure to the workload's bottleneck ([Zhou et al., arXiv 2606.24775, Jun 2026](https://arxiv.org/abs/2606.24775)).
- **Relevance still helps grep.** RARG uses relevance to order and seed grep-based agentic search and improves accuracy and efficiency ([Jul 2026](https://arxiv.org/abs/2607.24223)).
- **Leaders are hybrids.** SmartSearch reports 93.5% on LoCoMo and 88.4% on LongMemEval-S, finding LLM *structuring* unnecessary. Its ranking still uses learned neural rerankers, including ColBERT, which is itself an embedding method ([Mar 2026](https://arxiv.org/abs/2603.15599)). Leading LongMemEval systems such as Hindsight and Zep keep an embedding channel inside hybrid fusion.

**What the evidence supports, as of Oct 2026.**
- *Single-vector top-k similarity as the sole retrieval path for agent memory* is losing ground. This is clearest in coding agents and on structured, causal or exact-reference material. *Confidence: medium–high.*
- *Agent-driven tool retrieval* (lexical, navigational, file-based) is now a mainstream backbone. *Confidence: high.*
- *Embeddings as a component* (one channel in hybrid fusion, rerankers, relevance guidance for grep, concept search over large or non-code corpora) are not outdated and are still the default in the memory-system literature. *Confidence: medium–high.*
- Head-to-head benchmark numbers don't settle it. LoCoMo is near saturation and poorly matched to agentic use (MemoryArena). Figures are mostly self-reported by vendors and conflict across sources.

So the claim as heard is broader than the evidence. The narrower statement above is what the evidence supports.

**Where the subject sits in this.** The subject is at the no-embedding end. It replaces similarity with two other selectors, structural position and revisit count, plus model routing. The field has evidence for each ingredient on its own: grep and file navigation (Claude Code, Letta), tree navigation (PageIndex, LATTICE), activation-style ranking (Generative Agents, Hindsight's spreading channel). I found no published evaluation of position-keyed per-message push. The concept-search gap that Cursor and turbopuffer measure is where this design is expected to lose. That expectation comes from those measurements on code, not from any test of this design.

---

## What the tasking smuggled in

- **"A session that starts with no memory" frames the problem as memory.** Five of the nine families locate the core somewhere else: coordination (F6), handoff (F5), deliberation (F3), reconciliation of authority (F7), workflow hygiene (F8). Framing it as memory makes recall look like the main mechanism and the store look secondary. F3 and F7 say the reverse.
- **"Get to what it needs" assumes the need exists before retrieval and only has to be reached.** In F3 and F8, part of what the session "needs" is produced by the classification act itself. The gate creates the need rather than finding it. Retrieval-benchmark framing (precision and recall against a gold set) can't see this.
- **The description is written in the subject's own vocabulary and partly in its own justification.** Examples: "the lowest one that contains it, not one that merely resembles it"; "decides the direction of repair"; the four-way authority sort presented as complete. These read as settled properties when they are design claims. Nothing in the description says how often the gate classifies correctly, how often the push is used, or whether the four kinds cover every record.
- **"There is no vector index and no similarity search" is presented as a defining property.** The appended claim about embeddings being outdated then invites validation of that choice. The task asked me to check the claim, not assume it. What I found is narrower than the claim (above).
- **"Supports assistants from several vendors" sits next to a recall design that depends on hooks firing at session start and before every message.** Those are host-specific features, documented here for Claude Code. Whether the push half exists on every supported assistant isn't stated. Without hooks, the subject falls back to F9 rungs 1–4.
- **"The system is developed using itself."** This is offered as a property. In F7's terms it means the reconciler maintains its own spec, which is a known self-reference risk: no outside check on desired state. In F9's terms it is the ACE loop, with context-collapse risk.
- **The instruction to give families, not harmonise them, and return no verdict** shapes this answer too. It rules out a single best account even where one family (F9) is the literal category and the others are analogies.

---

## Nothing to take

Leads I followed that gave no usable grounds, listed so they aren't re-run:
- **[Always-On Agents survey (Jun 2026)](https://arxiv.org/abs/2606.30306).** The abstract has no evidence on retrieval modality. Its governance axes (authority, scope, mutability, provenance, recoverability, actionability) overlap F7, but I could not get the body's content.
- **Blog claims that "agents don't need vector search anymore"** and that "no top SWE-bench entry uses vector retrieval" ([Medium, 2026](https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f)). These are unsourced, and I didn't verify them.
- **Cross-vendor LongMemEval and LoCoMo rankings** ([e.g. Atlan](https://atlan.com/know/mem0-alternatives/)). Figures conflict across sources for the same system, and they are self-reported. They can't rank approaches.
- **Distributed cognition (Hutchins, "How a cockpit remembers its speeds", 1995) as its own family.** It maps, but it maps every externally supported memory system equally, so it doesn't tell this subject apart from anything. Its useful content is already in F4, F6 and F8.
- **Zettelkasten-style agent memory (A-MEM, 2025).** The topic resembles this subject, but its links are made by embedding similarity, so no structural mapping holds for the recall side.
- **Knowledge-graph memory (Zep, Graphiti) as a family.** It is a peer in the comparison table, not an alternative account. The subject's tree is a hand-curated hierarchy, not an extracted entity graph.
- **A published evaluation of position-keyed (not query-keyed) per-message context injection, or of a mandatory pre-answer classification gate.** I found none.

---

## Sources

**LLM agents, 2025–2026**
- Anthropic, "Effective context engineering for AI agents," Sep 29 2025: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, "Effective harnesses for long-running agents," Nov 2025: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, "Equipping agents for the real world with Agent Skills," Oct 16 2025: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, Memory tool docs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Claude Code hooks overview (MLOps Community): https://mlops.community/blog/the-complete-guide-to-claude-code-hooks-automating-your-ai-coding-workflow
- Simon Willison on Claude memory, Sep 2025: https://feeds.simonwillison.net/2025/Sep/12/claude-memory/
- Claude Code dropping vector RAG (secondary summary): https://smartscope.blog/en/ai-development/practices/rag-debate-agentic-search-code-exploration/
- Cursor, "Improving agent with semantic search," Nov 6 2025: https://cursor.com/blog/semsearch
- Rogut (turbopuffer), "Benchmarking semantic code retrieval on Claude Code," AI Engineer Europe 2026: https://www.ai.engineer/talks/zKk7sDMGDEQ-benchmarking-semantic-code-retrieval-on-claude
- Letta, "Benchmarking AI Agent Memory: Is a Filesystem All You Need?," Aug 12 2025: https://www.letta.com/blog/benchmarking-ai-agent-memory
- Letta, "Context Repositories," Feb 2026: https://www.letta.com/blog/context-repositories
- Mastra, "Observational Memory," Feb 9 2026: https://mastra.ai/research/observational-memory
- Hindsight (Vectorize), Dec 2025: https://vectorize.io/blog/hindsight-building-ai-agents-that-actually-learn
- Zep temporal KG paper (2025): https://huggingface.co/papers/2501.13956
- ChatGPT memory reverse-engineered, Dec 2025: https://llmrefs.com/blog/reverse-engineering-chatgpt-memory ; https://www.gigazine.net/gsc_news/en/20251226-reverse-engineered-chatgpt-memory-system
- Cline Memory Bank: https://docs.cline.bot/prompting/cline-memory-bank
- Beads: https://pkg.go.dev/github.com/steveyegge/beads@v0.17.7 ; https://www.morphllm.com/beads-agent-memory
- PageIndex: https://pypi.org/project/PageIndex/
- LATTICE, arXiv 2510.13217: https://sotaverified.org/papers/251013217
- Weller et al., "On the Theoretical Limitations of Embedding-Based Retrieval," Aug 2025: https://arxiv.org/abs/2508.21038
- Chroma, "Context Rot," Jul 2025: https://trychroma.com/research/context-rot
- IFScale, "How Many Instructions Can LLMs Follow at Once?," Jul 2025: https://arxiv.org/abs/2507.11538
- ACE, "Agentic Context Engineering," Oct 2025: https://arxiv.org/abs/2510.04618
- Hu et al., "Memory in the Age of AI Agents," Dec 2025: https://arxiv.org/abs/2512.13564
- Gloaguen et al., "Evaluating AGENTS.md," Feb 2026: https://arxiv.org/abs/2602.11988
- Related AGENTS.md studies: https://arxiv.org/html/2601.20404v2 ; https://www.alphaxiv.org/abs/2607.27250
- MemoryArena, Feb 2026: https://arxiv.org/abs/2602.16313
- AMA-Bench, Feb–May 2026: https://arxiv.org/abs/2602.22769
- Du, "Memory for Autonomous LLM Agents," Mar 2026: https://arxiv.org/html/2603.07670v1
- SmartSearch, Mar 2026: https://arxiv.org/abs/2603.15599
- Zhou et al., "Are We Ready For An Agent-Native Memory System?," Jun 2026: https://arxiv.org/abs/2606.24775
- Ding et al., "Always-On Agents," Jun 2026: https://arxiv.org/abs/2606.30306
- RARG, "A New Role for Relevance," Jul 2026: https://arxiv.org/abs/2607.24223
- READ, "Beyond Top-K," Aug 2026: https://arxiv.org/abs/2608.06305
- Blog claim checked and not used: https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f ; https://atlan.com/know/mem0-alternatives/

**Earlier LLM-agent foundations**
- Packer et al., MemGPT, 2023: https://arxiv.org/abs/2310.08560
- Park et al., Generative Agents, 2023: https://arxiv.org/abs/2304.03442

**Long-standing principles**
- Denning, "The Locality Principle," CACM 2005: https://calhoun.nps.edu/entities/publication/de7a7c89-de98-405b-a420-b9d2eb5c7641
- Anderson & Schooler, "Reflections of the Environment in Memory," Psych. Science 1991: https://www.psychologicalscience.org/journals/psychological-science/volume/2/issue/6/
- Kunz & Rittel 1970 (IBIS); Conklin & Begeman 1988 (gIBIS): https://eight2late.com/category/issue-based-information-system/page/6
- Buckingham Shum et al., "15 years on from gIBIS and QOC": https://acawiki.org/Hypermedia_support_for_argumentation-based_rationale:_15_Years_on_from_gIBIS_and_QOC
- Design rationale capture problem (Conklin & Yakemovic 1991; Lee 1997, summarised): https://human-factors.arc.nasa.gov/groups/HCSL/publications/Hooey_KM2007.pdf
- Shipman & Marshall, "Formality Considered Harmful," CSCW 1999: https://people.engr.tamu.edu/shipman/formality-paper/harmful.html
- Nygard, "Documenting Architecture Decisions," 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Teevan et al., "The Perfect Search Engine Is Not Enough," CHI 2004: https://people.csail.mit.edu/teevan/work/publications/papers/chi04.pdf
- Bergman et al., "Improved search engines and navigation preference in PIM," TOIS 2008: https://cris.openu.ac.il/en/publications/improved-search-engines-and-navigation-preference-in-personal-inf-2/
- Starmer et al., I-PASS, NEJM 2014: https://psnet.ahrq.gov/resources/resource/28485
- Heylighen, "Stigmergy as a Universal Coordination Mechanism," 2016: https://wiki.p2pfoundation.net/Stigmergy_as_a_Universal_Coordination_Mechanism
- Heylighen & Vidal, "Getting Things Done: The Science behind Stress-Free Productivity," 2008: https://web-archive.southampton.ac.uk/cogprints.org/6289/1/Heylighen-Vidal-GTD-Science.pdf
- Masicampo & Baumeister, "Consider it done!," 2011: https://scrapbox.io/nishio/consider_it_done
- Kubernetes, Controllers: https://kubernetes.io/docs/concepts/architecture/controller/
- Cited from memory, not fetched this run: Nii 1986 (Blackboard Systems, *AI Magazine*); Conklin 1987 ("Hypertext: an introduction and survey", *IEEE Computer*); Alexander 1965 ("A City is Not a Tree"); Pavlik & Anderson 2005 (*Cognitive Science*); Silla & Freitas 2011 (hierarchical classification survey, *DMKD*); Malone 1983 ("How do people organize their desks?"); Hutchins 1995 (*Cognitive Science*).

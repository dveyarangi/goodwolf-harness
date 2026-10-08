# How the front pages of peer projects are written — a survey, 2026-10-08

Run at the front-page align on [q-0031](../questions/q-0031-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md), when the user asked whether the draft reads the way READMEs of similar projects are written. One web-only agent fetched eleven READMEs and two docs pages and measured them. It was told nothing about this project. Filed as it came back; what the align takes from it is the align's.

---


Method: I fetched the current raw README.md of each repo on 2026-10-08 and the GitHub repo page for star counts. Word counts are `wc -w` on the raw markdown, so they include URLs and HTML markup and overstate prose by roughly 10–25%. "Install at N%" is the share of the README's words that come before the first install command. Section lists are top-level headings (H2, plus H1/HTML headings where the page uses them) in order. Quotes are kept under 30 words, one per project.

Moves noticed:
- **beads** now redirects from `steveyegge/beads` to **gastownhall/beads**.
- **get-shit-done** (`gsd-build/get-shit-done`, 64.4k stars) was archived on 2026-06-26. Its README is a 55-word "GSD Has Moved" notice pointing to **open-gsd/gsd-core**, which is the page surveyed here.
- **letta-ai/letta** is now a 176-word stub. It says the source "lives in" `letta-ai/letta-code`, so both are noted.

## Star counts (rough signal only)

| Project | Stars | Forks |
|---|---|---|
| obra/superpowers | 296.5k | 26.5k |
| mattpocock/skills | 279.9k | 23.5k |
| github/spec-kit | 140.6k | 12.6k |
| thedotmack/claude-mem | 97.9k | 8.6k |
| Fission-AI/OpenSpec | 71.3k | 4.9k |
| gsd-build/get-shit-done (archived) / open-gsd/gsd-core | 64.4k / 10.3k | 5.4k / 740 |
| bmad-code-org/BMAD-METHOD | 53.9k | 6.1k |
| gastownhall/beads | 27.7k | 1.9k |
| letta-ai/letta / letta-code | 25.1k / 3.5k | 2.6k / 430 |
| MrLesk/Backlog.md | 7.0k | 443 |
| buildermethods/agent-os | 5.5k | 828 |

Stars build up over a repo's lifetime. Most of them were earned by older versions of these READMEs, not the current text.

---

## Per-project records

### 1. github/spec-kit — https://github.com/github/spec-kit/blob/main/README.md
- **Opening.** An H3 tagline (build with a spec, fix a bug, or assess an idea), then "Spec Kit is an open source toolkit that gives AI coding agents structured processes, reusable templates, and documented outcomes." It leads with a **definition**, followed straight away by a **menu of outcomes**.
- **Sections.** Choose your process · Get started · Spec-Driven Development · Bug fixing · Idea assessment · Customize or bring your own process · Documentation · Star history · Support and contributing.
- **Install.** At 27%, under "Get started", right after the "Choose your process" table. Prerequisites are stated first (Python 3.11+, uv, a supported agent).
- **Length and density.** About 875 words. Short prose paragraphs, one table (need → process → outcome), 6 code blocks, 4 bullets. Images are the logo and a star-history chart. Language links: English, Chinese, Japanese.
- **Example or demo.** Each process has a block of slash-command invocations with realistic arguments (e.g. "Build a photo organizer with albums grouped by date…"), which works as a mini worked example. A "Video overview" is linked from the Documentation list, not embedded. No transcript.
- **Why.** No pain is stated and there is no philosophy section. The why is carried by the outcomes column (e.g. a go/clarify/stop decision backed by evidence).
- **Limits and status.** Prerequisites, and bug-fix/assessment marked as opt-in extensions. No maturity label, no limitations, no "not for".
- **Tone.** Plain and imperative, with moderate "you". Coined terms on the page: SDD, constitution, converge/"Converged", integration key.
- **Distinctive.** The page opens on a task-routing table that maps the reader's need to a process and its outcome. It is a rewritten, shortened page that keeps invisible `<a id>` anchors (e.g. `-experimental-goals`, `-video-overview`) so old deep links still resolve.

### 2. bmad-code-org/BMAD-METHOD — https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md
- **Opening.** A bold line: "turn an idea or change request into working software without giving up the thinking." It leads with a **promise/outcome**, and the following paragraph defines AiDD.
- **Sections.** Start Building · Why BMad? · BMad Ecosystem · Documentation · Community · Support and Contributing · License.
- **Install.** At 23%. "Start Building" is the first section, with three alternative install routes (skills CLI, Claude Code plugin, …).
- **Length and density.** About 840 words. Several prose paragraphs, one 6-item benefit bullet list, an ecosystem table (modules), and 3 code blocks. Images are a banner and a delivery-loop diagram (SVG).
- **Example or demo.** No worked example or GIF. A YouTube channel is linked under Community.
- **Why.** "Why BMad?" names the pain: assistants turn unstated assumptions into code. Six bolded benefit bullets follow (Right-sized process, Durable context, …). There is no named comparison, only "coding assistants" in general.
- **Limits and status.** Prerequisites only (an AI tool with skills support, uv, Node). No maturity statement and no limitations.
- **Tone.** Second person, benefit-led and fairly polished. Coined terms: AiDD, briefs, modules (`bmod-*`), "durable context", "right-sized process".
- **Distinctive.** Install comes before the why. Each benefit bullet pairs a bolded label with a one-clause outcome.

### 3. obra/superpowers — https://github.com/obra/superpowers/blob/main/README.md
- **Opening.** "a complete software development methodology for your coding agents, built on top of a set of composable skills". It leads with a **definition**.
- **Sections.** Table of Contents · How it works · Commercial Services · Installation (17 per-host subsections: Claude Code, Antigravity, Codex App/CLI, Cursor, Devin, Factory Droid, Gemini, Copilot CLI, Grok, Kimi, OpenCode, Pi, Qwen, Hermes, Muse) · The Basic Workflow · When Something Goes Wrong · Community · What's Inside / Skills Library · Philosophy · Contributing · Updating · License · Visual companion telemetry.
- **Install.** At 20%, after the narrative "How it works" and a two-line Commercial Services pitch. The per-host install blocks then take up roughly 18–59% of the page.
- **Length and density.** About 1,880 words. Bullet-heavy (93 bullet lines) with many short code blocks (28) and **no images at all**.
- **Example or demo.** No GIF and no transcript. "How it works" is a **second-person narrative** of what happens from the moment you start your agent: it asks what you're trying to do, shows the spec in digestible chunks, writes a plan, and runs subagents for "a couple hours" after you say "go".
- **Why.** The why lives in that narrative. A short Philosophy section near the end has four bullets (TDD, systematic over ad hoc, complexity reduction, evidence over claims). No named comparison.
- **Limits and status.** "When Something Goes Wrong" admits that a skill can fire when it shouldn't, or that the agent may use more tokens than expected, and points to a diagnostic skill. There are per-host caveats and a telemetry disclosure section. No maturity label and no "not for".
- **Tone.** Conversational second person, with dry humour (the plan is pitched at an eager junior engineer with no judgement or context). Coined terms: subagent-driven-development, skill names (brainstorming, …).
- **Distinctive.** The page explains usefulness as a story about the user's session rather than as a feature list. It is also the only one with a section on what to do when the tool misbehaves.

### 4. beads (gastownhall/beads, formerly steveyegge/beads) — https://github.com/gastownhall/beads/blob/main/README.md
- **Opening.** A bold definition (a distributed graph issue tracker for AI agents, built on Dolt), then "It replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context." It leads with a **definition**, then **problem → outcome**.
- **Sections.** Quick Start · Features · Essential Commands · Hierarchy & Workflow · Installation (with Security And Verification) · Storage Modes (with Schema Version Guard) · Community Tools · Git-Free Usage · Documentation. Headings carry emoji.
- **Install.** At 8%: a curl install script, as the first section.
- **Length and density.** About 1,380 words. Feature bullets (bold label + clause), a commands table, and 6 code blocks, one of which is a **mermaid lifecycle flowchart** (create → ready → claim → close → blockers released). The other images are badges.
- **Example or demo.** The mermaid diagram plus command snippets. No session transcript.
- **Why.** One sentence of pain ("messy markdown plans", "losing context"). No why section, no comparison, no philosophy.
- **Limits and status.** Supported platforms listed. Security/verification and a schema-version guard are documented. No maturity label and no "not for".
- **Tone.** Terse and technical, feature-forward ("Agent-Optimized", "Zero Conflict"). Coined terms: bead, `bd ready`, compaction as "memory decay", contributor vs maintainer modes.
- **Distinctive.** A reference-manual shape. The page is mostly what it does and how to run it, with the value carried by one opening sentence and the diagram.

### 5. MrLesk/Backlog.md — https://github.com/MrLesk/Backlog.md/blob/main/README.md
- **Opening.** A centred subtitle (a Markdown-native task manager and kanban visualiser), then "AI agents write the code. You review the tasks: before, during, and after." That is followed by `npm i -g backlog.md`. It leads with a **definition plus a division of roles**, then a **command**.
- **Sections.** Why Backlog.md in the AI era · Features · Getting started · Working with AI agents · Working without AI agents · Backlog.md + Groma.md · Web Interface · MCP Integration (collapsible client guides) · CLI reference · Configuration · Troubleshooting (Apple Silicon) · Talks & Community · License. Headings carry icon images.
- **Install.** At 2% (in the header). The full "Getting started" section is at 18%.
- **Length and density.** About 2,670 words, the longest here. Mixed prose, bullets, and 14 code blocks. A demo **GIF** sits at the top, plus a web-UI screenshot, a diagram and section icons. Two conference-talk **YouTube links** appear near the top and again at the end.
- **Example or demo.** The demo GIF (`backlog board`). "Working with AI agents" is a **step-by-step workflow** with example prompts to paste ("Ask your AI Agent: …") and three labelled "Review checkpoint" callouts.
- **Why.** A dedicated why section states the pain sharply: an agent produces more code in an hour than you can read in a day, so the bottleneck is now your attention. It offers three review checkpoints as the answer. No named competitors.
- **Limits and status.** A troubleshooting section, local-first and "no account, no telemetry" statements, and a claim that the project dogfoods itself. No maturity label and no "not for".
- **Tone.** Direct second person and confident. Coined terms: three review checkpoints, spec-driven AI development, Definition of Done, Groma.md.
- **Distinctive.** The only page with both a moving demo and a concrete prompt-by-prompt workflow. It also documents how to use the tool **without** AI agents.

### 6. Fission-AI/OpenSpec — https://github.com/Fission-AI/OpenSpec/blob/main/README.md
- **Opening.** A collapsible headline "The most loved spec framework.", then "Our philosophy:" as a code-formatted list ("fluid not rigid → iterative not waterfall → easy not complex…"), then a TIP with a command to start. It leads with **values/philosophy**, the only page here that does.
- **Sections.** See it in action (collapsibles: what the specs look like; dashboard) · Why teams adopt OpenSpec · Quick Start · Docs · Community schemas · Why OpenSpec? / How we compare · Updating OpenSpec · Usage Notes · Contributing · Other (collapsibles: Telemetry, Maintainers & Advisors) · License.
- **Install.** At 42%, the latest of the full READMEs. It comes after the philosophy, the demo transcript, a spec example, the dashboard and a team pitch.
- **Length and density.** About 1,380 words. Prose and bullets, 9 code blocks, and heavy use of `<details>` collapsibles. Images are the logo, a dashboard screenshot and badges.
- **Example or demo.** A **You:/AI: transcript** running explore → propose → apply → archive for a dark-mode feature, plus a collapsible showing a real spec file. A source comment marks a demo GIF as a TODO.
- **Why.** Pain: assistants are unpredictable when requirements live only in chat history. "How we compare" **names alternatives**: Spec Kit (thorough but heavyweight), Kiro (IDE lock-in), and working with no specs at all.
- **Limits and status.** "Stores" marked **beta**. A Node version requirement. Says it works best with high-reasoning models and names recommended ones. Telemetry disclosed. Claims it is built with itself.
- **Tone.** Second person, with marketing elements ("most loved"). Coined terms: `/opsx:*` commands, changes, archive, Stores, artifact-guided workflow.
- **Distinctive.** Demo before install. It has both a sample session and a named comparison, and splits the pitch between solo use and teams.

### 7. buildermethods/agent-os — https://github.com/buildermethods/agent-os/blob/main/README.md
- **Opening.** The H2 heading (agents that build the way you would), then "helps you shape better specs, keeps agents aligned in a lightweight system that fits how you already build." It leads with a **promise**.
- **Sections.** Agents that build the way you would · Core capabilities (4 bolded bullets) · Documentation & Installation · Follow updates & releases · Created by Brian Casel @ Builder Methods.
- **Install.** Not on the page. "Documentation & Installation" (at 54%) links out to the vendor site ("It's all here").
- **Length and density.** About 190 words. One hero image, two short bullet lists, no code.
- **Example or demo.** None. **Why:** implied by the promise only. **Limits and status:** none.
- **Tone.** Marketing, second person. Coined terms: Discover/Deploy/Index Standards, Shape Spec.
- **Distinctive.** The README is a signpost and the product page lives elsewhere. It is the minimal end of the range.

### 8. mattpocock/skills — https://github.com/mattpocock/skills/blob/main/README.md
- **Opening.** "My agent skills that I use every day to do real engineering - not vibe coding." The next paragraph names GSD, BMAD and Spec-Kit as approaches that own the process and take control away from the user. It leads with **personal provenance plus positioning by contrast**.
- **Sections.** Installation (30-second setup): 1. Get the skills / 2. Run setup / 3. "Bam - you're ready to go." · Why These Skills Exist: #1 The Agent Didn't Do What I Want · #2 The Agent Is Way Too Verbose · #3 The Code Doesn't Work · #4 We Built A Ball Of Mud · Summary · Reference (Engineering, Productivity skill lists).
- **Install.** At 10%, with two install routes framed as two philosophies (managed plugin vs editable copy). A newsletter call to action comes before it.
- **Length and density.** About 2,210 words. Prose-heavy with many short paragraphs. Each pain gets a book pull-quote (Pragmatic Programmer, DDD, XP, A Philosophy of Software Design). 5 code blocks, one banner, no GIF.
- **Example or demo.** A before/after phrasing example showing how a shared glossary shortens what you tell the agent. No transcript.
- **Why.** The whole middle of the page. **Four named failure modes**, each structured as "The Problem" then "The Fix" (the skill to use). Named comparison to GSD, BMAD and Spec-Kit in the opening.
- **Limits and status.** No maturity label. Positioning implies who it is for (engineers who want control) without a "not for" section. Mentions a native Codex plugin as upcoming.
- **Tone.** First person and second person, energetic ("Bam"), opinionated. Coined terms: grilling session, ball of mud, deep modules, glossary/CONTEXT.md.
- **Distinctive.** Usefulness is organised as pain → fix pairs in the reader's own words ("The Agent Didn't Do What I Want"). Authority comes from the author's experience plus the classics he quotes.

### 9. thedotmack/claude-mem — https://github.com/thedotmack/claude-mem/blob/main/README.md
- **Opening.** The subtitle "Persistent memory compression system built for Claude Code." Then a preview GIF, a star-history chart, and a paragraph saying it captures tool-usage observations, summarises them and makes them available to future sessions. It leads with a **definition/feature**.
- **Sections.** Quick Start (incl. OpenClaw Gateway) · Documentation (Getting Started, Best Practices, Architecture, Configuration & Development) · How It Works · MCP Search Tools · Release Branches · System Requirements · Configuration (Mode & Language) · Development · Troubleshooting · Bug Reports · Contributing · License · Support · What About CMEM?
- **Install.** At 17%. Quick Start is the first section, with many per-IDE variants.
- **Length and density.** About 2,090 words. Bullet-heavy (61 bullet lines), 14 code blocks and one table. Images: logo, **demo GIF**, star history, badges. **About 30 translation links** sit above the fold.
- **Example or demo.** The GIF, plus a code example of its 3-layer search workflow.
- **Why.** Pain (context lost between sessions) is implicit in the definition. The only quantified claims are token costs: about 50–100 tokens per result in the index, and "~10x token savings". No comparison.
- **Limits and status.** The hosted provider is the default, with sign-in and a "30 Day Free Trial" plus opt-out flags. System requirements, Windows notes and troubleshooting are included. It ends with a section on a third-party crypto token the author endorses. No maturity label.
- **Tone.** Mixed technical and promotional. Coined terms: observations, progressive disclosure, CMEM Pro, "awareness push pilot".
- **Distinctive.** The only page that puts cost (tokens, trial) into numbers. Its front matter is dominated by localisation and social proof.

### 10a. open-gsd/gsd-core (successor to get-shit-done) — https://github.com/open-gsd/gsd-core/blob/main/README.md
- **Opening.** "Git. Ship. Done.", then a bold definition listing about 10 supported agents, then "What is GSD Core", which introduces "context rot". It leads with a **slogan plus definition**.
- **Sections.** What is GSD Core · How it works (five-step loop: Discuss → Plan → Execute → Verify → Ship) · Quickstart · Documentation · Why it works · Community · Star History · License.
- **Install.** At 38%, after the definition and the loop.
- **Length and density.** About 550 words. A numbered loop list, 2 code blocks, a community table, a star-history chart and badges. Links to four translations.
- **Example or demo.** None. The five-step loop stands in for one.
- **Why.** "Why it works" lists three failures of "most AI-coding setups" (context bloat, no memory between sessions, no verification) and maps each to a mechanism. One number: each executor starts with a clean 200k-token context.
- **Limits and status.** Only a troubleshooting link.
- **Tone.** Marketing-forward slogan. Coined terms: context rot, phase loop, waves, fresh subagents.
- **Distinctive.** Problem → mechanism mapping in a few lines. It is a short successor page to a much bigger archived one.

### 10b. letta-ai/letta — https://github.com/letta-ai/letta/blob/main/README.md (and letta-code: https://github.com/letta-ai/letta-code/blob/main/README.md)
- **Opening.** "Build stateful agents with memory that can learn and improve over time." It leads with an **imperative promise**, then a status/pointer ("actively developed"; the code now lives in letta-code).
- **letta sections.** Get started · Historical source. About 180 words, 3 command blocks, no images, install at 34%.
- **letta-code sections.** Feature Overview (table) · Get started · Letta Cloud · AgentFile deprecation · Installing external skills · Research · Other. About 1,070 words. Its opening defines a stateful agent harness whose agents are meant to be more like people than tools.
- **Why, limits, tone.** No pain, comparison or limitations, apart from deprecation notices. Platform-marketing tone. Coined terms: stateful agents, App Server, channels.
- **Distinctive.** The high-star repo's front page is now a redirect-plus-quickstart stub.

### 10c. Cline Memory Bank (docs page) — https://docs.cline.bot/prompting/cline-memory-bank
- **Opening.** Memory Bank "transforms Cline from a stateless assistant into a persistent development partner." It leads with a **definition framed as a transformation**.
- **Sections.** Quick Setup · How It Works · Core Files · Key Commands · Managing Context Windows · Best Practices · Custom Instructions (copy-paste block) · FAQ.
- **Setup and density.** Setup at about 11%. About 1,400 words, 2 tables, a file-hierarchy diagram, and a copy-paste instruction block.
- **Example, why, limits.** No worked session. Pain: statelessness and context-window limits. No limitations stated. Coined terms: Memory Bank, projectbrief, activeContext.

### 10d. Kiro steering (docs page) — https://kiro.dev/docs/steering/
- **Opening.** Steering gives Kiro persistent project knowledge, so that "Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns". It leads with a **definition plus the pain it removes**.
- **Sections.** What is steering? · Key benefits · Steering file scope (workspace/global/team) · Creating custom steering files · Steering with custom agents · AGENTS.md · Inclusion modes · File references · Steering during a session · Teaching through code reviews · Best practices · Common strategies.
- **Setup and density.** Setup at about 20%. About 2,100 words, reference-style, with a capability matrix table and YAML/markdown snippets.
- **Limits.** States which product surfaces lack which features (older CLI versions, web sandbox).

---

## Synthesis

Counts below are over the 11 GitHub READMEs: spec-kit, BMad, Superpowers, beads, Backlog.md, OpenSpec, Agent OS, mattpocock/skills, claude-mem, gsd-core, letta (stub). The two docs pages are a different genre and are noted separately.

### The common skeleton (what nearly all do)
1. **An identity line at the top: 11/11.** It is either a one-sentence definition ("X is a … for AI coding agents") or a promise/tagline. The split is roughly 6 definition-led (spec-kit, Superpowers, beads, Backlog.md, claude-mem, gsd-core) and 4 promise- or position-led (BMad, Agent OS, mattpocock, letta). OpenSpec leads with values.
2. **A one-line install, inline: 10/11** (Agent OS links out). It is nearly always a single `npx` / `npm i -g` / `uv tool install` / `curl | bash` / `/plugin install` line. **7/11 put it in the first ~30%** of the page, and 3 put it in the first 10% (Backlog.md 2%, beads 8%, mattpocock 10%). The late ones are letta 34%, gsd-core 38% and OpenSpec 42%.
3. **A host-compatibility claim: 10/11.** Each names the agents or IDEs it works with: Claude Code, Codex, Cursor, Gemini, Copilot, etc. Several then give per-host install subsections (Superpowers 17, claude-mem about 8, Backlog.md 5).
4. **A docs offload: 8/11.** A "Documentation/Docs" section or link block sends depth to a docs site, and the README stays a front door.
5. **A community, contributing and license tail: 10/11.**
6. **Bolded-label bullets for benefits or features** ("**Durable context** — …"): about 8/11.
7. **Mostly no imagery.** Only 2/11 have a demo GIF (Backlog.md, claude-mem), and 3/11 have a diagram (BMad SVG loop, beads mermaid, plus Backlog.md's architecture image). 4/11 have no meaningful image at all (Superpowers, letta, mattpocock apart from a banner, gsd-core apart from badges and star history).
8. **Install before the long "why".** Of the 5 pages with a dedicated why section, 3 put the why after install (BMad, mattpocock, gsd-core). Backlog.md puts a one-line install in its header, then the why, then the full Getting started. OpenSpec has why material on both sides of its Quick Start.

### Range of variation
- **Length.** It runs from about 190 words (Agent OS, a signpost) and about 550 (gsd-core) to about 2,200–2,700 (mattpocock, claude-mem, Backlog.md). The two highest-starred pages are mid-to-long (Superpowers about 1,900, mattpocock about 2,200), and both are image-free text.
- **What the why section is.**
  - Absent: spec-kit, beads, Agent OS, letta, claude-mem. These rely on one sentence or an outcome table.
  - A dedicated section stating a pain: BMad, Backlog.md, OpenSpec, gsd-core.
  - The spine of the whole page: mattpocock (four failure modes, each Problem → Fix).
  - Values-first: OpenSpec's philosophy list as the opening.
  - Philosophy as a short coda: Superpowers.
- **Named comparison to alternatives: 2/11.** OpenSpec (Spec Kit, Kiro, "nothing") and mattpocock (GSD, BMAD, Spec-Kit). Others contrast only with an unnamed baseline: "coding assistants", "messy markdown plans", "most AI-coding setups", "vibe coding".
- **Voice.**
  - Conversational or first person: Superpowers, mattpocock.
  - Plain and instructional: spec-kit, beads.
  - Slogan or marketing: gsd-core ("Git. Ship. Done."), OpenSpec ("most loved"), Agent OS, claude-mem.
  - Coined vocabulary appears on every page. It ranges from light (spec-kit: constitution, converge) to dense (claude-mem: observations, progressive disclosure, awareness push pilot; OpenSpec: opsx, changes, Stores, archive).
- **Social-proof and commerce elements.** Star-history charts (3), translation links (3, up to about 30), conference talks (Backlog.md), a newsletter count (mattpocock), commercial-support or hosted-tier pitches (Superpowers, claude-mem, letta, Agent OS), and a crypto-token section (claude-mem).
- **Structural signatures.** Each of these appears on exactly one page:
  - spec-kit routes by task through a need → process → outcome table.
  - beads draws its object lifecycle as a mermaid diagram.
  - Backlog.md marks review checkpoints as callouts inside a prompt-by-prompt workflow.
  - OpenSpec uses collapsible `<details>` blocks to keep a long page scannable.
  - Superpowers gives a long per-host install matrix.

### How they convey usefulness rather than mechanism
- **Outcome-first tables or lists.** spec-kit names the artifact each process leaves you with (for bug fixing: the cause, a scoped fix and a recorded verification). gsd-core's loop describes what each step guarantees.
- **The user's pain in the user's words, mapped one-to-one to a fix.** mattpocock ("The Agent Didn't Do What I Want" → /grill-me). gsd-core (three failures → three mechanisms).
- **Role division.** Backlog.md ("AI agents write the code. You review the tasks"). BMad ("without giving up the thinking"). Superpowers pitches the plan at an agent with no judgement. All three tell the reader what they still do and what the tool takes off them.
- **Narrating the session from the user's seat.** Superpowers' "How it works" describes what the agent does after you open it and what you sign off on. OpenSpec's transcript shows the same thing as dialogue. Backlog.md's workflow gives the prompts to type.
- **A reframed bottleneck.** Backlog.md recasts the bottleneck as the reviewer's attention. gsd-core names "context rot". Each coins or reframes a problem so the tool becomes the obvious answer.
- **Concrete artifacts shown.** OpenSpec's spec file, spec-kit's example arguments, beads' command table.
- **Numbers, rarely.** Only claude-mem (tokens per result, "~10x"), gsd-core (200k-token clean context), Superpowers ("a couple hours" autonomous) and Backlog.md ("15,000 generated lines" you can't review). All are illustrative, not measured outcomes.
- **Borrowed authority.** mattpocock quotes engineering classics. OpenSpec and Backlog.md say they are built with themselves. Superpowers links its release-announcement post.

### What almost none of them do
- **Say who it is not for: 0/11** explicitly. mattpocock and OpenSpec imply it through positioning.
- **State limitations or failure modes of the method itself: about 1/11.** Superpowers' "When Something Goes Wrong" is the only one. OpenSpec's "beta" label and model recommendation come closest after that.
- **Offer evidence it works:** no benchmarks, evals, before/after metrics or case studies on any front page.
- **Show the cost of adopting it** (tokens, time, ceremony): only claude-mem quantifies tokens and a trial. None estimates the per-feature overhead of running the process.
- **Give a maturity or stability statement for the core:** none. Only sub-features are flagged (OpenSpec Stores beta, letta deprecations).
- **Show a full end-to-end sample session:** only OpenSpec, abbreviated. Only 2/11 have a moving demo.
- **Show what lands in your repo** (a file tree of the artifacts it creates): only OpenSpec (a collapsible spec) and Cline's docs page (a file hierarchy). Others name files in passing (gsd-core's STATE.md/CONTEXT.md, spec-kit's artifacts).
- **Define their coined terms on the page:** usually none. gsd-core links "context rot" to a doc, and mattpocock demonstrates his glossary idea.
- **Lead with the problem as the very first sentence:** none. The pain arrives in sentence 2–3 (beads, mattpocock) or in a later section.

### Docs pages vs READMEs (Cline, Kiro)
Both product docs pages follow a steady pattern:
- They define the concept and the pain it removes in the first two sentences.
- Setup comes at 10–20%, followed by reference material (scopes, files, modes, best practices).
- They have no social proof and no comparisons.
- They state surface-specific limitations more readily than the READMEs do (Kiro).

# Session 24 — the front page meets its readers

**2026-09-23 to 2026-09-26.** Opened on loose ends and ran into the first real test of how the
harness reads to someone who did not build it.

## What happened

**Loose ends, and a bug they exposed.** `.0155` and `.0165` closed with their RFCs; the 2026-09-20
external review was committed. Updating ai-game-1 to fix its stale `L3` failed outright: an update
rebuilt the tree's announced ref under today's shipping rules, so every tree installed before
`.0165` was stranded. Fixed as `Shipment.earlier` —
[rule failure 9](../rule-failures.md), which also amended `/verify`: a fixture standing for
something that already exists must be built the way it came to be. ai-game-1 then took `85691cd`,
and [`.0145`](../tickets/done/01-0010.0145-core-scripts-under-one-directory.md) closed on that
blind update, frost_map held for `.0195`.

**The front page.** An outside review said the README undersold the harness. The align that
followed settled who the page is for, that it points into core and never `docs/`, and its title —
*GoodWolf Harness*, tested on cold readers against four others. Two `/discover` passes placed the
harness among its peers ([material](../research/discover-what-this-is.md)); the first one fired
only because the user asked, which is [rule failure 10](../rule-failures.md), and it was wrongly
barred from reading the repository it was asked about, now an exception in `/discover`.
[`.0167`](../tickets/done/01-0010.0167-the-front-page-says-what-the-harness-is.md) built the page
and an MIT license copied into every install; its plan landed a copy step in the architecture,
which is [rule failure 11](../rule-failures.md) — `/plan` now lands only load-bearing
architecture.

**Six adoption panels.** Five independent readers with different projects, run on the published
page after each round of fixes ([record](../research/adoption-panel-2026-09-26.md)). No reader
would adopt it, and the verdicts never moved; what moved was *why*. Early runs found the page
misleading and the process a human's burden; later ones found the page accurate and credited the
method on merit, and their reasons became product: no light path for small work, one person
steering, `CLAUDE.md` taken over. The panel's rules came out of the runs — read only what ships,
never `docs/`; split the verdict on merit from trust in a young project, but never drop *what would
change your answer*; run clean-room, not yet achievable from a session.

**Decisions along the way** *(the user)*: the process is the agent's control, not the person's
load, and the page says so; `/recall` reads what bears on the work in flight, as it already did;
the loader links are made in each clone and never committed —
[ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md) amended; ceremony comes in
three tiers, recorded on [01-0020](../tickets/01-0020-pacer.md).

**Minted:** [`.0125`](../tickets/01-0010.0125-the-host-blocks-what-a-rule-forbids.md) the host
blocking what a rule forbids; [`.0168`](../tickets/01-0010.0168-the-harness-measures-what-it-costs-and-saves.md)
measuring tokens and human turns from the hosts' own transcripts;
[`.0172`](../tickets/01-0010.0172-a-first-install-says-what-stopped-it.md) the Windows first-run
failures of GitHub issue #1 and the per-clone link step;
[`.0200`](../tickets/01-0010.0200-a-project-can-remove-the-harness.md) uninstall;
[`.0205`](../tickets/01-0010.0205-a-recipient-reports-a-harness-failure-upstream.md) a recipient
reporting a core failure upstream. `.0175` took its codebase half back. 342 tests. Twenty-three
commits, all pushed.

## What the passes kept finding

- **I wrote the page's claims ahead of the evidence.** *The install never overwrites*, *small
  changes don't take the whole loop*, *it has come into a large existing codebase* — each read as
  an oversell and each came out. The claims that held were the ones a reader could check in core.
- **Substituting instead of adding.** Asked to split a question, I replaced the most useful one.
  Asked for a finding about the entry file, I produced one the user refuted in a sentence. The
  pattern is reaching for a change before checking what the existing thing already does.
- **A subagent is never context-free here.** The host loads the entry file, the memory index and
  recent commit subjects into every one; a panel reader asked for exactly what a commit subject had
  just named.
- **The readers on the other model misreported presence** three times — a Windows note on the page
  they said was missing.

## Open questions

- **What `arrived` means while the links are pending** — `.0172`'s align; issue #1 is evidence
  against the harness doc's *arrived is the three gates alone*.
- **The three decision-bearing aligns just minted** — `.0125` (which hosts and rules), `.0168` (the
  unit, which human turns are burden, what leaves the machine), `.0205` (where, consent, content).
- **May core name the edge record?** — `.0185`, still the releases chain's gate. The edge record now
  owes lines for the repository line, the delivery status, the license and the updater reading old
  refs as they shipped.
- **The license's holder** — *the GoodWolf Harness contributors*; one panel reader took the plural
  for more than one author. Undecided.
- **Clean-room panels** — no `claude` command on this machine; a requirement on `.0190` no run has
  met.

## Continuation

- **Next in the ring:** the queue's candidate paragraph still leads with `.0185`'s align; the panels
  argue that `01-0020`'s light path, `.0150`'s install beside an existing `CLAUDE.md` and
  `01-0017.0020`'s team story are what adoption waits on. `next-cycle=ask`.
- **The panel is paused** until `01-0020` or `01-0017.0020` lands, then run once more, clean-room if
  it can be.
- **The front page still lacks** a worked example and cost figures; both wait on `.0168`'s data.
- **frost_map** stays at `2c733f0`, held for `.0195`. **ai-game-1** is at `85691cd`, everything in it
  still untracked by its own repository.
- **The diagram** reads as a dark panel on GitHub's light theme; a light export from
  `dev-skills.excalidraw` would fix it if it matters.

# The selection completes, and the harness meets a second tree

Session thirteen, 2026-09-09. Opened with `/advise`, ran one `/align` on the ADR question and one
`/maintain` pass, and ended by installing the harness into a project that is not itself for the
first time. No delivery-ring slice was taken; the queue's candidate `.0050` is untouched.

## Work completed

- **The bootstrap selection is complete.** `/recall`, `/edge`, `/review-architecture` and
  `/setup-devops` installed from their accepted sources, with the caller repairs the selection
  already owed. All twenty selected working commands are now installed; the parent's install backlog
  is empty. `legacy/` deleted.
- **The suite runs in 68s, down from 118s.** `setUp` was three process spawns per test — 59% of the
  wall clock. Each case now stamps a copy of one template `.git` that Git builds once per process.
- **The tests moved into `.agents/scripts/test/`** and ship with core, which makes core a directory
  again: `.agents/` plus two line-level parts in `AGENTS.md`.
- **Entry contract v7 and v8**, and `docs/adr/` created on its first real need with four ADRs.
- **One ticket minted**, [01-0010.0105](../tickets/01-0010.0105-backlog-five-arrive.md); three
  proposed were not, because the work already had owners.
- **[The separation probe](../research/separation-probe-frost-map.md)** into `frost_map`, which
  holds its own findings and is the session's real output.

## What the probe changed about priority

Separation is now ahead of the coherence chain, on the user's call and the probe's evidence. Two
things reordered underneath it. [.0050](../tickets/01-0011.0050-shape-checked.md)'s allowlist turns
out to be the gate on the install script — a parts-derived manifest ships 3 skills of 22 today, so
*what ships* and *which skill is claimed* are one question. And the entry contract's hand-bumped
version is scaffolding: the user named its successor, a core revision derived from the manifest's
content, which retires the open question below rather than answering it.

## Three times I generalised from one shape

The entry file's first general rule, failed three times in one session, each time with the second
shape sitting on disk unread.

- **ADRs.** I recommended deleting `docs/adr/` and its four references as an unexercised convention,
  from twelve sessions of this project writing none. Meteoscape has 7, Forecast Collector 5, and
  `docs/concerns.md` — which I had called a painted door — exists in all four audited estates, 1264
  lines of it in Meteoscape. The check took ten seconds and I ran it only after being refused.
- **The glossary split.** Same error inverted: I proposed an ADR for it as a core decision. No estate
  has `.agents/glossary.md`. The split is this project's answer to a collision only this project has.
- **The junction.** A privilege error blocked a symlink, so I substituted a junction — the move
  [the repair policy](../process.md#autonomy-and-repair) forbids in as many words — and then wrote
  the substitution up as a finding recommending [ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md)
  be relaxed. Measured afterwards: nothing sees through a junction, and `git ls-files` lists
  everything beneath it twice, so the corpus every script shares double-counts.

A fourth of the same family, without the shape: I wrote up a link configuration my own two commands
had produced as a discovery, coined a term for it the glossary does not have, and recorded it in two
places. It is now one bullet. The tell each time is reaching for narrative where a fact would do.

## Manufactured while tidying

Two edits removed the queue's path from tier 1 — `/recall`'s pointer block and the entry file's
opening block — each correct by `/maintain`'s E1, the sum removing the only copy a waking session
would meet. On [01-0018](../tickets/01-0018-reachability-coherent.md) as its second observed
instance, and the first anyone made while cleaning. It sharpens that ticket's existing question:
whether a shared fact may be restated at tier 1 *because* it is needed there, which E1 reads as
duplication.

## Open, with owners

- **A separation/deployment ticket does not exist.** Its constraints are on
  [01-0010](../tickets/01-0010-dev-harness-shared-and-local.md)'s resolutions and its evidence in the
  probe record; `breakdown=ask`, so minting waits for a nod.
- **~~What an entry-contract version covers~~** — four sections sit outside the scope the record
  claims, evidenced: *Core and instance* landed 2026-09-07 between v3 and v4 with no entry. The user
  called the version a straw dog and named its successor, so this is superseded rather than open.
  It has no wrapper and no ticket yet, which by the entry file's own rule makes it still a claim.
- **Whether the tests stay in a recipient's default verification set**, at ~70s per `/verify`. They
  ship; that much is settled.
- **The frost_map probe is a second physical corpus**, which [ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md)
  exists to prevent. It drifted from core within the hour and had to be re-synced by hand. Deleted
  when the manifest exists; never pulled from.
- **Two partial rows** in `mechanism-shape`'s doc — `one instruction file` argued only in evidence,
  `produces has a reader` applied but not argued. Left after the `/maintain` pass.
- **The user's grade on the shape** is still not given, pre-registered since 2026-09-07.

## Housekeeping

Six commits: `EQUIP`, `TICKET`, `IMPLEMENT`, `ALIGN`, `DISCOVER`, `CONCLUDE`. Not pushed. The
verification set is 216 behavioural tests at 68s — down from 118s and now discovered from
`.agents/scripts/test` — plus `mechanisms.py`, `inject_rules.py` and `tickets.py --check`, all
green; sixteen straw dogs, all bound, no diagnostics. Twenty-two skills installed, three mechanisms
declared, four ADRs, entry contract v8.

The probe in `frost_map` is untracked work on its own `harness-probe` branch and is not part of
these commits.

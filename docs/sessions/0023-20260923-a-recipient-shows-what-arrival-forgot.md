# Session 23 — a recipient shows what arrival forgot, and two slices land

**2026-09-23.** Opened on a question about a real install and ran the delivery ring twice.

## What happened

The user installed the harness into `ai-game-1` and asked why the project's verification set had
come out holding core's own gates. It had not leaked: the answer was that the install's last step
told the writer to read the set *off its own toolchain*, and that tree had none — one commit, no
remote, six documents, no code. The only commands available were the harness's own.

`frost_map`, the first recipient, had escaped every version of this because it arrived already
set up. Every install decision so far was generalised from that one shape. `ai-game-1` was the
second, and the entry file's own rule about not generalising from one shape is what made the
align necessary rather than optional.

That align landed nine decisions on
[01-0010](../tickets/01-0010-dev-harness-shared-and-local.md#arrival-to-ready--2026-09-23) and
minted four slices. A second `/ticket` pass decomposed
[01-0010.0160](../tickets/01-0010.0160-harness-edge-changes-reach-an-update.md) into three.
Then two slices went the whole ring — `/plan`, `/implement`, `/verify` — and landed:

- **[01-0010.0155](../tickets/done/01-0010.0155-a-tree-names-the-repository-its-core-comes-from.md)**
  — a tree names the repository its core comes from, and the line is read, never compared.
- **[01-0010.0165](../tickets/done/01-0010.0165-a-fresh-tree-has-a-delivery-status.md)** — a fresh
  tree arrives with a delivery status to read.

Both are `Done` with every box checked and eligible for `/maintain`'s paired close. 311 → 335
tests. Six commits.

Two rule failures were registered and both amendments landed the same day:
[7](../rule-failures.md) — the harness declaration carried its script's verbs, because doc and
script were written in one commit — and [8](../rule-failures.md) — `/impact`'s *Output only:*
ended its caller's turn, so a `/ticket` run produced an assessment and no breakdown.

## What the passes kept finding

Worth naming, because it is the same shape four times and a fifth would be evidence of something
structural:

- **A rule phrased for one occasion, silently wrong in another.** Both rule failures. The
  declaration format asked for *what it is, in one line*, which a procedure satisfies; `/impact`'s
  output contract was written for a direct invocation and read as ending the turn.
- **A test named for a promise it did not assert.** Four at `.0155`'s verify, one at `.0165`'s.
  Each was a criterion the ticket stated plainly and the test approached from the side — an
  `--update` case tested with `--check`, an install case tested with an update, "a URL stamped
  verbatim" that only re-asserted a unit function.
- **A fix placed where only one reader would see it.** `.0155`'s citation blanking belonged in
  `docs_corpus`, not the ship pipeline, because `mechanisms.py` runs as a gate *inside every
  recipient*. Caught by a test failing on the shape gate rather than on the refusal it expected.
- **The first body line of a skill is spoken for**, by `mechanisms.py`'s claim grammar. Cost a
  plan correction at `.0155` and a fixture at `.0165`.

## Open questions

- **May core name the edge record at all?**
  [01-0010.0185](../tickets/01-0010.0185-an-edge-change-writes-its-line.md)'s align owns it, and
  it is the sharpest thing left. *Core and instance* lets core name a painted door and forbids a
  particular record inside one; `docs/edge/install.md` is a particular record. So a core rule
  installed into `/implement` and `/verify` cannot say where an edge change's line goes. Three
  forks are written out on the ticket with what each costs. The ticket is decision-bearing until
  this lands.
- **What the first publish does about history** —
  [01-0010.0190](../tickets/01-0010.0190-core-is-published-as-a-release.md)'s: mirrored commits or
  one per release.
- **Whether `/ticket` and `/maintain` should assert the delivery status exists** rather than
  assume it, now that only an install writes one. On `.0165`, likely
  [01-0010.0180](../tickets/01-0010.0180-harness-names-its-maintenance.md)'s, since it is exactly
  what harness would name to `/maintain`.
- **How the switches are elicited** before setup —
  [01-0010.0170](../tickets/01-0010.0170-arrival-becomes-a-sequence.md)'s. The align settled that
  they precede the step they authorise, not how they are asked.
- **What the quicklook's fixed recipe actually reads**, and whether a glossary harvest runs
  unattended over material in a language the agent is guessing at —
  [01-0010.0175](../tickets/01-0010.0175-arrival-describes-what-it-finds.md)'s, narrowed to its
  prose-sourced half because the read-the-codebase recipe still has zero real cases.

## Continuation

- **Next in the ring:** `.0185`'s align, which needs the user in the room. `next-cycle=ask`.
- **`ai-game-1` is still broken.** Its `L3` names `.agents/scripts/`, which `.0145` moved. The
  landed slices fix the *instruction*; that tree needs its local file rewritten by hand, or the
  migration `.0195` will give it. It now also lacks a delivery status, which its next `--update`
  will write.
- **Two edge changes are recorded only in their RFCs** — `.0155`'s repository line and `.0165`'s
  delivery status. Both owe the edge record a line, written at `.0185`'s implement pass rather
  than reconstructed from the commit log, which is what that align refused.
- **Unpushed.** Six commits on `main`; `push=ask`.
- **Untracked and not this session's:** `docs/research/external-review.md`, present before the
  session opened and left alone.

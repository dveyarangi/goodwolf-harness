# maintain — evidence

Why [the doc](../../.agents/mechanisms/maintain/maintain.md) is what it is: what was tried, what
was refuted, what it cost, and what it used to be. Provenance stays inline on each rule in the
body. The mover's contract and the straw-dog contract live in
[architecture](../architecture.md); the install decisions belong to
[Install /maintain](../tickets/done/01-0010.0070-install-maintain.md), the declaration's to
[01-0011.0022](../tickets/done/01-0011.0022-shape-survives-second-mechanism.md).

Declared by [01-0011.0022](../tickets/done/01-0011.0022-shape-survives-second-mechanism.md),
2026-09-07. Until then this file was `docs/research/maintenance-findings.md`, holding the two
probe records below and nothing else.

## What the 2026-09-07 align refuted

**`none` by property.** The ticket was minted saying `/maintain` has no records, so its record
obligation is `none` and not deferred. Life's `maintenance` mechanism, read directly, is
record-bearing by design: marks moved only by a maintenance, dueness derived from them at every
wake. The obligation is `not yet`; the clock is
[01-0011.0060](../tickets/01-0011.0060-mechanism-rechecked-when-governing-moves.md).

**Three subjects.** Mechanism, documentation and code were one activity seen from three sides:
`/sync-arch` in general form is *hold an implementation to its documentation*, and this
repository's implementation is `.agents/`. The doc now states four things held in agreement, per
documentation-and-implementation pair, and the pairs a project has are a facet.

**Nine responsibilities, three instructed.** `docs/process.md:75` assigned nine and the body
instructed roughly three; a pass following the body faithfully on 2026-09-07 still missed a
stale roster. Each responsibility now has a disposition on the ticket — instructed, `elsewhere`,
`embedded` or `not yet` — and the body is written as addressable rules, one per line, so the
next such miss names the rule it missed.

**Committing and comment cleanup were never this mechanism's.** A pass acts on the repository
when it commits, not on this mechanism; inline comments are `/verify`'s at landing. Both left
the body.

## 2026-09-06 — Selected mover inspected before adaptation

## 2026-09-06 — Selected mover inspected before adaptation

Source: Forecast Collector's
[move_doc.py](D:/Dev/DriftSense/workspace/forecast_collector/.agents/scripts/move_doc.py)
and [docs_corpus.py](D:/Dev/DriftSense/workspace/forecast_collector/tests/deterministic/docs_corpus.py).
These observations concern the source at inspection time, not an installed harness mover.

- `perform` rewrites inbound links only when `live(name)` holds. Sessions and archived
  tickets/RFCs are exempt in that source. This harness's historical-reference contract
  requires an adaptation and a different assertion from the source history test.
- A read-only probe of `refusal` with the same source mapped to two different destinations
  returned `None`. The source does not reject duplicate sources before beginning the batch.
- An isolated temporary-directory probe injected an error on the second move. The first
  record remained at its destination, the second at its original path, and the queue still
  referenced the original first path. No project or source records were moved by the probe.
- `redepthed` transformed an absolute `D:/Dev/...` link into `../D:/Dev/...`. A path classifier
  must preserve external and absolute references rather than treating them as relative paths.
- `_rewrite` uses `newline=""` for both reads and writes. This is the selected source's useful
  newline-preservation behavior; adaptations must retain it.
- `docs_corpus` depends on Git discovery, and its resolver silently clamps `..` at the root.
  Reuse needs explicit root/path handling and removal of the source archive exemptions.

The [implementation RFC](../rfc/done/01-0010.0070-install-maintain.md) owns the resulting plan
and its verification cases. These probes are planning evidence, not `/verify` of an install.

## 2026-09-06 — Content rewrite failure

A second isolated temporary-file probe called the source `_rewrite`, injecting an I/O error
after its write-mode open and before writing replacement content. The original 45 bytes,
including unrelated uncommitted notes, became zero bytes. The source's direct write truncates
the original before the replacement is complete. No repository or source file was mutated.

This distinguishes a partially completed batch from lost content inside one record. The
agreed lack of batch rollback does not require destructive in-place rewriting. The RFC's
second validation pass adds failed-rewrite preservation and corresponding behavioral proof.

The subsequent user clarification keeps this probe as implementation evidence. Per-file
writing technique belongs to the helper; it does not establish a new maintenance architecture
or recovery mechanism. The owning ticket records the clarification and the RFC reflects it.

## The installer arrives, 2026-09-08

At [.0020](../tickets/done/01-0011.0020-rules-one-home.md), the body received the mechanism shape's
rules as an installed block — R1 to R4 — after the *Installed from other mechanisms* heading and
before the two hand-copied wrappers, which stay until their tickets close. R5, *never edit an
installed block by hand*, did not arrive: the user moved it to the entry file, so it reaches every
session rather than this body. The rules file this mechanism authored a day ahead of its reader
was rewritten to the shelf's grammar — its one rule now `M1`, its anchor a table row — and
installed into `/mechanism`'s *Incept*; nothing had read it until then. The doc's `embedded`
row for records checking became instructed, and three such rows became two, both the ticket
mechanism's.

## The third declaration grades this one, 2026-09-09

Pre-registered on the doc at [.0022](../tickets/done/01-0011.0022-shape-survives-second-mechanism.md)'s
align: the session that declares the ticket mechanism takes the mover and the citation reader as
its own, installs the paired-close block into the body, and retires the two `embedded` rows — did
those land against this doc as written, or did the doc have to be rewritten to receive them?

**The block landed as written.** The anchor the doc's rules file named for the shape's block took
the ticket's block beside it with no edit; the hand copy's P1–P3 came out as the installed P1–P3
with one clause fewer, *and the queue row*, which was a straw-dog phrase no rule body may carry;
the two `embedded` rows became instructed by naming the body, which is what the rows had said
would happen. That half graded clean.

**The ownership did not land as written, and the doc was right to have been wrong.** The doc had
forward-declared the ticket mechanism as the claimant of the citation reader and the test harness.
The align applied the spec's own ownership decision instead — the claimant where a shared part's
claim bites is the always-on mechanism — and both docs' owner columns were rewritten to
`mechanism-shape`. So the doc was rewritten, but to what the spec had said all along; the
forward-declaration was the error, not the reception. The mover and its five test files went to
the ticket mechanism as declared.

**One rule the pre-registration did not foresee stayed behind.** P4, a spec's agreements before
archiving it, was in the hand copy as a ticket rule and is `/spec`'s. It sits in the body inside
its own straw dog now, bound to the ticket that declares the rest of the corpus. A grader counting
`embedded` rows would have called the doc clean; the rule that was never the ticket mechanism's
was found by asking who owned each sentence, not by the check.

## The straw dog gets its name, and the listing learns to guess, 2026-09-08

At [.0070](../tickets/done/01-0011.0070-straw-dogs-marked-and-found.md). The enumerator became
`straw_dogs.py`, its tag `<straw-dog>`, after the user named the concept; four operative blocks
were renamed and no record of history touched, since every other mention already sat in a code
span. A `<temporary>` written from habit is now a diagnostic rather than an invisible statement.

**The first guess over the whole tree** — `docs AGENTS.md .agents tests`, before anything was
wrapped — returned 67 candidates. Ten were the script and its tests talking *about* the TODO
convention, which is what made a marking a comment line beginning `TODO` rather than the word
anywhere; 58 remained. Judged one by one: **six straw dogs**, wrapped and bound — this doc's *no
installer exists yet* to 01-0010, its *until the clock exists* and *no record until the marks* to
.0060, its *two rows read embedded* to .0025, the shape doc's *nothing runs the check unasked* to
01-0010.0120, and the pacer document's *until the pacer is installed* to 01-0020. **Two stale
expiries**, found by the guess and repaired: the format shelf said anchored parts were *interim,
until injection ships*, and injection had shipped the day before without retiring the sentence;
and the glossary still carried a **Temporary statement** entry beside the one that had replaced
it. **Two bound in words but not wrappable**: table cells in this doc and the shape's, whose
owner column says *a declared gap until .0025*; a tag cannot sit in a cell, and the ticket is
named in the cell. The other 48 are claims: process language in the skills — *iterate until the
user approves* — definitions, history in the evidence and research, and rationale.

**What the guess cannot find** is on the ticket: a claim that became false with no tell in its
wording. Three of the four sentences the injector's verify caught carry one; *owns none* does
not. A tell is where a word list stops and a person starts.

**No TODO existed in the tree** when the code side landed, so there was no prior corpus to
sweep and none is claimed.

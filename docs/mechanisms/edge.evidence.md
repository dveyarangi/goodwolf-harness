# edge — evidence

Why [the doc](../../.agents/mechanisms/edge/edge.md) is what it is. Declared 2026-10-10 in session
`58bf3b88`, answering
[q-0023.0009](../questions/done/q-0023.0009-what-does-edge-own.md) "What does /edge own?"; no ticket
declared it. The first record, [hosts](../edge/hosts.md), answers
[q-0018.0023.0001](../questions/done/q-0018.0023.0001-where-does-the-contract-a-host-must-meet-live-with-each-hosts-standing-against-it-and-the-procedure-that-checks-a-new-host-the-same-way.md).

## How it came to be declared

Asked whether the requirements on a host and the checks of a new host's integration were kept
anywhere beyond ticket history, the answer was no: the capability matrix and the whole connection
run lived only in the narrative of
[01-0010.0120 what-each-host-says-without-being-asked](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md),
the hook files in the questions mechanism's parts, the hook's contract in the architecture, the
loader link in ADR 0003, and every host's quirks in code alone. The user: *this is an edge; the
edge mechanism is missing.*

The `/edge` skill had arrived with the selected skills on 2026-09-05, written for product surfaces
in another project, its format on `/align`'s shelf, its challenge rule in `/align`'s body, its
glossary terms promised in `docs/glossary.md` and never written there, and no record anywhere. Two
edges were already in view and materially different — the hosts, an edge things attach to, and
the installation edge, one that promises — so the concept was forced, not generalized from one.

## What the 2026-10-10 align settled, and what it refuted

**The user's three corrections.** An edge is met by consumers *and extenders*, plugin-like shapes
such as host integrations included. The record lives in `docs/edge/` and carries nothing an
integration needs to work: the integration is core, the record is the development process's
document of it. The edge describes in general terms how an extension is added and tested, and
carries each extension's specifics in a sidecar.

**Refuted: the host record must ship with core.** Proposed on the ground that core's hooks need the
contract. Wrong: nothing reads the record to make an integration work, so core does not depend on
it, which is all the core–instance rule forbids.

**Refuted: "outer boundary" as the word's limit.** Replaced by *where the system meets someone
outside it who consumes it or attaches to it*. Looked for a better home for plugin-like shapes and
found none: the architecture keeps a seam's existence and structure, the mechanism shape keeps how
a mechanism is built; neither holds what an extender is promised, the checks it passes, or where
each one stands.

**Resolved by the harness's own rule: the record does not instruct.** A document under `docs/`
never instructs an agent, so the record's `Extending` holds checks, as a ticket holds criteria, and
the skill's *Extend* goal is the instruction to pass them.

**Sidecars over the body** *(the user)*: the Codex and Cursor accounts in the ticket already ran to
several KB each and grow with every re-check.

**Maintenance fits `/maintain`** *(the user)*: the check and the re-read of a record whose named
files moved reach `/maintain` as installed rules, E1 and E2, rather than a new pass of the edge's
own.

## Inception, step by step

**The check before the thing.** `test_edges.py` was written first and failed whole, the module
absent. One case was the test's own error — an edge with no `Extending` cannot hold a live
validator — and was corrected. Run over the seeded record, the check then caught a fault of its
own: a result followed by its colon, `documented:`, was not read as a result. A case was added,
watched failing, and the split fixed.

**Prior corpus: none.** No `docs/edge/` existed in this tree before the hosts record was seeded, so
there was nothing to count.

**The shape check caught the inceptor.** The doc's first draft named `docs/edge/hosts.md`, a
particular record only this instance has, and a ticket by its id; both were removed.

**The installer placed the challenge inside another rule's wrapper.** `/align`'s challenge heading
was followed by a straw dog whose opening tag precedes its own heading, so the block written at the
section's end landed inside that wrapper, with no diagnostic. The heading was moved below the
straw dog's close. The installer reads a section as ending at the next heading, whether or not a
wrapper opened in between.

## The landing the declaration missed — 2026-10-10

Asked whether the rules say what is written into an edge and when, the declaration answered for
alignment (E3), maintenance (E2) and a deliberate `/edge` call, and for nothing at a landing — the
occasion that most changes an edge. The format said a landed Roadmap entry leaves with the edit
that updates `Contract`, and a tentative record rides its ticket's docs-at-landing list, but no
skill that runs at a landing read either; and a live observation of a host had no rule sending it
to the sidecar, so it would have kept landing in tickets and session records, where the matrix had
lived. The moment row *checking a change against the edges it touches* named `/edge` as its
instruction, true only when someone asks for it.

E4 went to `/verify`, not `/implement` *(the user)*: holding landed work to what governs it is
`/verify`'s, and the live checks that observe a host run there. It answered, in the same pass,
where the installation edge's block lands, which its ticket had left for `/plan`. `/verify` had no
heading for installed rules. One added at its end, after every wrapper, was refused by the
installer's check: the local block, under *The verification set*, must be the last in its file. The
heading sits before that section instead, where no wrapper opens between it and the next heading.

## The first /verify, with an independent review — 2026-10-10

Both commits had landed on a green verification set alone; asked *did you check it is good?*, the
inceptor read the work against what governs it and found E4 contradicting E2 on which side wins
and *touched* left to the reader ([rule failure 30](../rule-failures.md)). The amendment gave both
rules the grain of what a sidecar names. `/verify` then ran, beside a separate agent that had not
built the mechanism and read it cold.

**The inceptor's own pass** found three things the checker let through — an unguarded promise in
a tentative record, a malformed numbered check dropping out of the count, a check answered twice —
and two results claiming more than was watched: Claude Code's compaction marked documented with no
source, and every *Silence* marked observed when only the revival was.

**The reviewer found what the inceptor had not**, and these were repaired: E4's trigger list lost
in the amendment; E3 writing a contract change into a Normative record before it landed, with no
`⚠ pending` and no tentative state, fixed by E3 marking it and E4 clearing it; Monitor writing a
compatible change with no decision, now a finding until one is made; Codex's entry file marked
observed on a premise, Cursor's and Claude Code's dated a day early, partial observations unnamed,
Cursor's registration recorded as observed while it fails the check's second half; the Wake and
Window invariants stated without the qualification the contract gives them, and an observation
about the loader link standing as a promise; the skill naming the queue as delivery state's owner;
a ticket field the format leaned on that does not exist; the check claiming more than it reads;
two tests whose fragment a different message also matched; a duplicate row collapsing silently; a
link left on the old shelf; instance state in the core doc; and no account of what a host's
integration is made of, which a new host would have read code for.

**Two findings waited on a decision.** Staleness was still per sidecar — a result rested on no
named part of its own, so any named part moving staled every result — and a result had no verdict:
`observed` said someone watched, not that the check passed.

## Staleness marking refuted — 2026-10-10

Asked what problem staleness marking solves, the answer was an observation outliving the code it
watched and reading as current. Its date already says that, beside the code's history; the
marking added nothing a reader could not see, cost a judgment at every landing that touched a
named file, risked erasing real observations, and was acted on by nobody but the next live check,
which runs when an extension is deliberately re-checked. Refuted *(the user)*: E2 keeps only the
broken promise as drift, E4 only the decided change, the cleared mark, the removed Roadmap entry
and the observation written to its sidecar; the format keeps *an observation keeps its date, a
later one replaces it*. The verdict vocabulary went with it — a result's own words say when a check
failed, as Cursor's registration does. A glossary entry for *result* was proposed and refused: a
general word is not captured by a narrow mechanism.

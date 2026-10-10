# Session 30 — the store goes live, and learns what to hold

**2026-09-29 to 2026-10-02.** Woke with `/recall` on the open-questions mechanism and built
[01-0011.0100.0010 the-store-and-questions-writes-it](../tickets/done/01-0011.0100.0010-the-store-and-questions-writes-it.md)
through all seven stages of its RFC, then verified and maintained it, pushed, and aligned on what
the store should hold. The conversation was resumed three times under new host session ids and
woke under v18 from the second resume on.

## What happened

**The store, built and live.** `questions.py` — check, window, wake, tree, writer, hooks — test-first
over 134 cases; the mechanism declared, its rules installed (Q1 at tier 1, the entry contract at
v18); each host's hook wired: Claude Code, Codex, Cursor; `concerns.md` folded into the store's
first entries; `/align` cut to the interview. `/verify` checked four of seven boxes; `/maintain`
marked every mechanism current. Claude Code is observed live — session start, the prompt hook,
the one-line *unchanged* window — and recorded on
[01-0010.0120](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md).

**Decisions 43 to 55** on [01-0011.0100](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md),
each with its provenance there: a closed question points to its answer; each host's hook delivers
the window, redrawn only when something moved; attach is a short rule with four example lines; then
the align on what the store holds — look the answer up first, rights from the agent's role, small
decisions settled and reported, load-bearing ones the person's, a request bringing its question
first, strikes as delayed reaches that rank, names carrying the whole question. Three AFK slices
were minted to carry 46 to 55: `.0012`, `.0015`, `.0017`.

## What kept happening

- **Terms and references used before they were explained** — *window*, *attach*, *store attached to
  a session*, *decision 23* by number. The user asked each time. This is the failure sessions 28 and
  29 recorded, still unregistered; it was the rule-failure candidate the user asked about at the
  start and then lost the premise of, which was itself the failure.
- **Steps reached for by habit, not by rule**: delivery status left "for `/conclude`" when the step
  that moves delivery state owns it; a slice marked HITL for a wording review its decisions had
  already settled; branching asked about when decision 36 makes it the agent's move.
- **Machinery proposed past what a decision needed**: a reopening procedure inside a flow about not
  reopening, and two new message "moves" that only restated decision 25. The user's questions —
  *how does reopening fit?*, *isn't answering already working?* — removed both.
- **The user's own redirections were better designs**: hooks over a rule, a time gap over session
  identity for strikes, roles over steps for rights, the lookup in the docs as the first test.

## Open questions

- **[.0010](../tickets/done/01-0011.0100.0010-the-store-and-questions-writes-it.md)'s three live boxes**:
  a session showing every declared line under v18, two sessions seeing each other, and Codex and
  Cursor live — Codex needs the project trusted and its hooks approved through `/hooks`.
- **q-0001.0006 — a resumed conversation under a new session id** leaves a trail of session lines and
  loses its position until it declares again; it happened at three of this session's resumes but not
  at every message. The hook could carry the position over, once one payload shows what it shares.
- **q-0016 — what an agent role is**, and which mechanism keeps roles; q-0016.0001, picking an area,
  waits under it.
- **The rule-failure entry** for undefined terms: register it, and decide whether the amendment goes
  to `/align`'s line or to the general rules — it fired outside an align as often as inside.
- **The two queue decisions** still parked: ADRs or tickets as a decision's home, and what an
  entry-contract version covers.

## Continuation

- **Uncommitted at this record**: this file, the leans on q-0001 and q-0016.0001, and the store's session
  line; the align's two commits, `0acf144` and `0e16a53`, are not pushed.
- **Next in the ring**: `/plan` on the three new slices — `.0017` is the smallest, and renaming the
  entries early means later links are written once. Then `.0012` and `.0015`.
- **Live tests** can run in any next session: start one in each host and read `docs/questions/sessions`.

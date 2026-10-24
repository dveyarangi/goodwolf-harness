# A rule reaches every file of a group

- **record of** what happened
- **Status:** Done (2026-10-25)
- **Type:** AFK
- **Minted:** 2026-10-25
- **Plan:** [the RFC](../../rfc/done/01-0080-a-rule-reaches-every-file-of-a-group.md) — a pattern
  row resolved to its members over the tree's listing, one resolution for install, retract, the
  check and the harness's rehearsal
- **Answers:** [q-0037.0002](../../questions/done/q-0037.0002-how-does-a-group-install-target-resolve-to-a-file-and-an-anchor-in-each-member.md)
- **Outcome:** A rules file names a group of files by a path pattern and a heading, and its rules are installed in, held in and retracted from every file the pattern matches that holds the heading, whether or not the rules file knew of that file when it was written.

## Parent

[q-0037.0002](../../questions/done/q-0037.0002-how-does-a-group-install-target-resolve-to-a-file-and-an-anchor-in-each-member.md),
whose `Where it stands` the user accepted on 2026-10-25. Impact:
[in the question](../../questions/done/q-0037.0002-how-does-a-group-install-target-resolve-to-a-file-and-an-anchor-in-each-member.md#impact-of-the-split-2026-10-25).

## What to build

The shape is the question's `Where it stands`. A row of a rules file's anchor table may name a
group: its target a path pattern, its anchor the heading a member holds. A file the pattern matches
is a member exactly when it holds the anchor; the rest are passed over, not refused, because a
member declares itself by the heading and a tree may hold none. Every rule an explicit target is
held to holds each member, so a member behaves as an explicit target in every other respect. The
five texts wrapped as straw dogs bound to the question are rewritten through it.

## Acceptance criteria

- [x] A rules file with a group row installs its block into every file the pattern matches that
      holds the heading, and into no other file.
- [x] A file that comes to hold the heading after the install is reported by the check as missing
      the block, and the next install fills it.
- [x] A file that stops holding the heading is reported as holding a block nothing owns, and the
      next install takes the block out.
- [x] A group with no member installs nothing and is neither refused nor reported.
- [x] A file both named explicitly and matched as a member is refused, as a target named twice is.
- [x] Every rules file of this tree installs as before, and the check stays green.
- [x] `/verify` passes against this ticket, its RFC and the governing docs.

## Out of scope

The voice, its first consumer —
[01-0016.0030 the-voice-speaks-every-skill-that-speaks](../01-0016.0030-the-voice-speaks-every-skill-that-speaks.md).
A named group that members declare by a mark of their own — refused in the question.

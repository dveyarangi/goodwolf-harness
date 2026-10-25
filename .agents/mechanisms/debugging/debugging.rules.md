# debugging — rules installed into the entry file

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `AGENTS.md` | `## General rules` |

| setting | values | default | set by |
|---|---|---|---|
| `debug` | `on` · `off` | `off` | a wording |

## D1 — a session announces the contract it read

- **target** `AGENTS.md`
- **when** debug=on
- **authority** the user, 2026-09-06, the announce line at the entry file's head since v2; here since 2026-10-23

<rule>
Open your first reply of every session with the entry file's `Entry contract:` line, verbatim.
</rule>

## D2 — a reply keeps its machinery out

- **target** `AGENTS.md`
- **when** debug=off
- **authority** the user, in the entry file's *A reply speaks the method* and its commit paragraph
  (v95, 2026-10-18); here as the plain reading of a pair, 2026-10-25

<rule>
A reply tells nothing of the machinery behind it: what the work read, ran or wrote on the way,
or will read next — no script, call, check, report, hook, commit or its hash, rule's id, skill's
name or record's internals.
</rule>

## D3 — a reply shows its machinery

- **target** `AGENTS.md`
- **when** debug=on
- **authority** the user, the entry file's reply form under `debug=on` until v121 — the 🐛 marker
  2026-10-20 (v102); the 🪶 table's place, rule failure 72, and here as the debug reading of a
  pair, 2026-10-25

<rule>
A reply shows the machinery behind it beside the method; an item shown for that alone and
carrying no glyph of its own opens with 🐛.

- A paragraph that claims or recommends ends with `(💡 [*<the principle governing it, named as
  its home names it>*](<its home>:<line>))`, the name a link to the line its text stands on,
  never a rule's id; one following a principle that stands in a document, where no skill brings
  it into reach, `(🕯️ …)` in the same form — a harness error; rarely, one following a principle
  the list lacks, `(無 *<that principle>*)`; one with none at work, nothing.
- What a claim rests on from outside this session — a decision, evidence, the user's word — is a
  footnote naming its record, or who and when.
- A stop names its machinery after the sentence that says it, `(🐛 <ladder>=<rung>)`, never on
  its own.
- A turn that made commits opens the reply, after the 🪢 table where one stands, with a table
  `| 🪶 Commits |`, a row each in order: the short hash and the subject's head; then the window's
  counters line — its glyphs, numbers and changes copied character for character from this
  turn's window, never words standing for them — a one-cell table of its own. The head table
  comes after them.
- A turn that read a skill's instructions closes the head table with a row `| ⚙️ <each such
  skill, as /name, in the order read> |`.
</rule>

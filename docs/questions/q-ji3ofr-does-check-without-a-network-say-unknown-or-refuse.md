# q-ji3ofr Does --check without a network say unknown, or refuse?

- **record of** what it intends to become
- **part of** q-66jqtu
- **state** open
- **owner** [01-0010.0195](../tickets/01-0010.0195-a-recipient-reads-before-it-takes.md)
- **rung** development: a feature, self-improvement: a script
- **opened** 2026-10-03T11:36:20Z
- **struck** 0, last 2026-10-03T10:17Z

Whether `--check` in a tree with no network says *unknown* or refuses. Today `--check` clones,
so it already fails without one; whether a pending-release count deserves a softer failure than
the integrity check is this ticket's.

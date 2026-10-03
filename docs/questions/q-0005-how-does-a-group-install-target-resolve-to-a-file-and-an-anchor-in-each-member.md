# q-0005 How does a group install target resolve to a file and an anchor in each member?

- **state** open
- **lean** membership declared from both ends, the group in the rules file and the file and anchor in each member

~~**Group targets.**~~ **Moved out 2026-09-10, the user: broader than the glossary and not part
of it right now.** Filed as concern 2, now [q-0005](q-0005-how-does-a-group-install-target-resolve-to-a-file-and-an-anchor-in-each-member.md), with the design gap the user named —
a group name is not an address, so membership must be declared from both ends, the rules file
naming the group and each member declaring what file and anchor the group means *in it*. This
ticket ships on explicit targets and does not wait for it.

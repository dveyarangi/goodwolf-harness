# Dev harness

This project's own domain vocabulary. Its domain is the harness itself, so the vocabulary is thin
by construction: the method's terms travel with core and live in
[`.agents/glossary.md`](../.agents/glossary.md). What stays here is what a recipient project would
own outright and would not receive — for this project, terms still being settled against records
only it has.

## Language

**Unit of work — proposed definition**:
Work with an explicit scale, owner, outcome and completion evidence; a milestone and a ticket can both be units at different scales. The term alone does not specify an agent-sized step; see the [pacer hypothesis](pacer.md#scales-and-steps--revised-hypothesis).

<straw-dog question="q-0035">
### Product to implementation

The words of requirements traceability, taken whole *(the user, 2026-10-13)*.

**Answer**:
A row of the product document: what relieves which causes, under an id never renumbered.
_Avoid_: solution, feature, mechanism row.

**Trace link**:
A question's standing claim that it realizes one or more answers, carried as an opaque reference the question store does not interpret; checked, never history.
_Avoid_: serves, mark, back-reference, product mark.

**Realizes**:
The relation a trace link states: the question builds that answer.
_Avoid_: serves, implements, belongs to.

**Trace propagation**:
A sub-question carrying its parent's trace links unless it states its own.
_Avoid_: inheritance.

**Coverage**:
An answer's state read from the questions that realize it — absent, in progress, present — and never written by hand.
_Avoid_: status, progress.

**Allocation**:
A decided purpose question closing, its answer becoming a row, and a structure question opening with a trace link to it.
_Avoid_: hand-off, handover.

**Orphan**:
A structure question with no trace link and no statement that it realizes none.

**Derived** *(of a question)*:
Realizing no answer, by explicit statement; flagged and reviewed rather than refused.

**Unrealized answer**:
An answer no open or closed question realizes.
</straw-dog>

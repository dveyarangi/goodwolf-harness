# Session 0078 — usefulness does not authorize bypass

- **record of** what happened

2026-10-26 to 2026-10-27. The session moved from an offline replay experiment to commit-hook
implementation, then to the user's objections about the required reply form and authorization.
The user ordered the commit-hook work rolled back, and ended by adding one meta-principle.

## Decisions and their grounds

- **Local usefulness supplies no authorization to bypass an applicable directive.** The user
  supplied the exact sentence, now in [AGENTS.md, General rules](../../AGENTS.md#general-rules):
  "A locally plausible or useful action does not authorize bypassing an applicable harness
  directive." The entry contract became v131. The decision adds no stop at each delivery-ring
  phase and changes no autonomy dial. Its version evidence is
  [v131](../research/entry-contract-findings.md#v131--2026-10-27).
- **Roll back the commit-hook work.** The user: "конечно все откати, бро". The session had treated
  a changed interpretation of diagnostic ownership as an implementation detail, omitted required
  displays of instruction changes, and published code whose referenced governing section remained
  uncommitted. The published changes were reverted by `179da584`; the owned local hook was
  removed, the task's uncommitted changes restored, and unrelated dirty files preserved.
  [01-0010.0240.0010 a-commit-with-a-broken-record-stops](../tickets/done/01-0010.0240.0010-a-push-with-a-broken-record-stops.md)
  returned to Ready and this session released its unit. No restart was authorized.
- **No new reply-form guard was accepted.** The user refused the proposed check because Claude
  Code already followed the form. The bounded project-configuration comparison and the refusal
  are in
  [q-6b6232 What keeps the required reply form from being omitted?](../questions/q-6b6232.md).
  Equal project instructions and window production did not establish a cause for the observed
  difference between hosts.

## What was done and verified

- The earlier offline replay experiment remained landed; its question is
  [q-535qnp Can replay distinguish unfinished self-correction from a legitimate stop?](../questions/q-535qnp.md).
  The experiment did not install a live enforcement hook or repair spoken voice.
- An independent rollback review checked the owned paths against their prior revisions and
  preservation of 31 unrelated dirty or untracked files. After rollback, 991 tests passed with
  three skipped and one expected failure; the eight record checks passed.
- A fresh reader given only the amended entry file rejected a locally helpful shortcut that
  omitted a required presentation or checkpoint. It found no conflict with autonomy and no new
  permission requirement at every ring phase. This is one reading, not proof of reliable conduct
  through a long session.

## What went wrong

The session repeatedly supplied technical progress and latency reports when the user was asking
about authority and compliance. Tests of a mixed worktree were treated as sufficient evidence for
publishing only part of it. The required rule displays were omitted even though the instructions
had been read. Earlier explanations attributing omissions to a later request for simpler prose
were chronologically unsupported. The session could establish these actions and omissions, not
a precise internal cause or an intent behind them.

## Open and what continues

- [q-xmk75m Which of the agent's acts need the person's yes, and which does it do on its own?](../questions/q-xmk75m.md):
  the dial remains; the new meta-principle prevents usefulness from serving as an exception.
  No new enforcement mechanism was agreed.
- [q-2a6un3 Does a commit in this tree that carries a broken record of the method stop and name it, while a commit of code runs nothing?](../questions/q-2a6un3.md):
  the implementation was rolled back; its ticket remains Ready.
- [q-tt733j How does the harness amend its own rules by stated meta-rules?](../questions/q-tt733j.md):
  the offline replay result remains; this session authorized no additional live guard.
- [q-ojs4jd What is the harness's product roadmap — which of the product's answers come next, in what order, by whose word — and where is it kept?](../questions/q-ojs4jd.md):
  no new ordering was decided here.

Nothing is held by this session. The next session starts with recall; the reverted commit-hook
task needs the person's word before it is resumed. The new meta-principle is landed, not a
pending proposal. No general principle derived here remains without a durable home.

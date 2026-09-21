# Scripts run on the standard library alone

The maintenance scripts under `.agents/scripts/gw/` import nothing outside Python's standard library,
and their tests use `unittest` rather than a framework. Decided in
[01-0010.0070](../rfc/done/01-0010.0070-install-maintain.md#mechanical-support)'s RFC, 2026-09-06,
when the runtime was observed as Python 3.14.6 through `uv run --offline --no-project python`.

The reason is the invocation, not taste: the harness runs its own checks offline and with no
project environment, and it travels into recipients whose dependency management it does not control
and must not disturb. A dependency would have to resolve in every estate the harness reaches, on
first use, with no install step — and the scripts do file walking, subprocess calls to Git, and
Markdown scanning, none of which needs one.

## Consequences

Test wall clock is the price. Every case shells out to Git because the scripts discover their corpus
that way, and a spawn costs ~68ms on Windows; the suite was 118s until the fixture stopped running
`git init` per case, and ~23s of what remains is Git doing real work. A framework offering parallel
execution would cut that and is deliberately not taken.

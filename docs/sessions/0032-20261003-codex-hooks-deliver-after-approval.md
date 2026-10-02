# Session 32 — Codex hooks deliver after approval

**2026-10-03.** A live Codex desktop test under entry contract v22, chat
`01a0fee7-f1bc-7043-9569-37ab27fb527e`. Recorded the observations and their limits in
[01-0010.0120 host-delivery-surfaces](../tickets/01-0010.0120-host-delivery-surfaces.md).

The initial messages supplied no hook context. After the user approved the hooks, the same chat
received the wake's read and then its question window directly in context. The runtime reported
the project hooks enabled and trusted. The hook registered the actual Codex session id; the
agent placed it at q-0001 and ended its own earlier manual fallback registration, `s-1003-e51e`.

q-0001 remains open: the store's broader work continues under its existing owner. This test
establishes Codex prompt delivery after approval; startup, compaction, unchanged-window output
and helper session ids remain unobserved here. No implementation, commit or push was requested.

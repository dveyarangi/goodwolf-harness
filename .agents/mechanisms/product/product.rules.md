# product — rules installed into skills

Machine input for the installer, read by nobody at session time. Amend a rule here, then
install it with overwrite; the block in a target is never the place.

| target | anchor |
|---|---|
| `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

## U1 — the product document is checked by its maintainer

- **target** `.agents/skills/maintain/SKILL.md`
- **authority** the user, 2026-10-13

<rule>
Check the product document with `product.py --check` — form, never content. A diagnostic is a
finding; repair it under the repair policy.
</rule>

# q-qmq6ty How does a project change how it builds in one edit?

- **record of** what it intends to become
- **part of** q-g6624x
- **state** open
- **owner** [01-0017.0020](../tickets/01-0017.0020-practice-swaps-in-one-edit.md)
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-10-03T11:36:21Z
- **struck** 0, last 2026-10-03T10:15Z

## Decisions

1. **The ring's form and its practice are two mechanisms** — the user, 2026-11-16: "харнес
   позволяет сконструировать генерное кольцо. в нем например /plan это скил который нужен во
   первых не только для кодинга, а во вторых в нем может быть разная практика. как и у
   имплементации и верификации. так вот форму кольца я думал что у нас называется методом, а
   наполнение - отдельныхй механизм который инжектит в генерные элементы кольца конкретную
   локальную практику - например tdd - собственно практикой"; of the cut put to them, "согласен
   с разделением". The ring's steps — `/plan`, `/implement`, `/verify` — are general and serve
   work that is not code; the practice is a mechanism of its own that injects a project's local
   practice into them, `/tdd` for one, and a project changes how it builds by changing it alone.
   Revises [q-nlec4j](q-nlec4j-does-every-rule-of-the-entry-file-belong-to-a-mechanism-so-that-an-install-adds-the-method-a-mechanism.md)
   decision 4, *one mechanism, its loop and its practice together*. Read the same day from the
   three skills: of `/plan`'s 31 rules about 24 are general, of `/verify`'s 20 about 16, and
   `/implement` is four paragraphs of frame around practice. The form's name is open — the user
   offered кольцо, производственное кольцо, производство: "кажется что кольцо может быть больше
   чем одно".
2. **`/align`, `/maintain` and `/impact` are not practice, and serve more than the ring; practice
   may inject into them** — the user, 2026-11-16: "align maintain impact - это не практика ... и
   используются не только кольцом. но могут населяться практикой".

**The ticket record assumes one maintainer.** Both adoption panels of 2026-09-26
([record](../research/adoption-panel-2026-09-26.md)) found it: global ticket positions in one
queue table collide across branches when several developers mint at once, and a team with its
own tracker would run two. Evidence for the ticket record being practice — the part that yields
to a project's own tracker — not a decision about how.

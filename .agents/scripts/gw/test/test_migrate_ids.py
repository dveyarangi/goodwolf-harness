"""The store's one-time migration to ids that never change (01-0010.0250.0100, stage 5)."""

from __future__ import annotations

import contextlib
import io
import shutil
import unittest
from datetime import datetime, timezone

from repository import RepositoryCase

import migrate_ids
import questions
import sessions

STORE = "docs/questions"
NOW = datetime(2026, 11, 9, 12, 0, tzinfo=timezone.utc)
ADDED = datetime(2026, 10, 1, 9, 0, 0, tzinfo=timezone.utc)


def entry(identity: str, question: str, parts: dict[str, str], body: str = "") -> str:
    bullets = [f"- **{name}** {value}" for name, value in parts.items()]
    return "\n".join([f"# {identity} {question}", "", *bullets]) + "\n" + (f"\n{body}" if body else "")


class AMigratedTree(RepositoryCase):
    """A small tree of every kind of thing the migration reads, migrated once."""

    def setUp(self) -> None:
        super().setUp()
        self.plant(self.root)
        self.migrated = self.run_on(self.root)
        self.table = self.migrated.table

    def plant(self, root) -> None:
        self.put(root, f"{STORE}/q-0001-which-store.md", entry("q-0001", "Which store?", {"record of": "what it intends to become", "state": "open"},
                                                              "See [the closed one](done/q-0002-gone.md) and q-0001.0002.\n"))
        self.put(root, f"{STORE}/q-0001.0001-child-one.md", entry("q-0001.0001", "Child one?", {"record of": "what it intends to become", "part of": "q-0001", "state": "open"}))
        self.put(root, f"{STORE}/q-0001.0002-child-two.md", entry("q-0001.0002", "Child two?", {"record of": "what it intends to become", "part of": "q-0001", "depends on": "q-0001.0001", "state": "open"}))
        self.put(root, f"{STORE}/done/q-0002-gone.md", entry("q-0002", "Gone?", {"record of": "what happened", "state": "closed:moot", "answer": "overtaken"},
                                                            "Was under [the root](../q-0001-which-store.md#decisions).\n"))
        self.put(root, "docs/tickets/01-0001-carry.md", "# Carry\n\n- **Answers:** [q-0001.0001](../questions/q-0001.0001-child-one.md#where-it-stands)\n")
        self.put(root, "docs/notes.md", "Read `docs/questions/q-0001.0002-child-two.md` and q-0001.0001.\n\n```\nq-0001 as a sample\n```\n")
        self.put(root, "AGENTS.md", '<straw-dog question="q-0001.0002">Waits.</straw-dog> An example: q-0001.\n')
        self.put(root, ".agents/scripts/gw/later.py", "# TODO q-0001.0001: when it lands\nX = 1\n")
        self.put(root, "docs/research/run.md", "Judged q-0001.0001.\n")
        self.put(root, "docs/research/run.txt", "q-0001.0001\n")
        self.put(root, f"{sessions.ROWS}/s-alpha", "s-alpha running 2026-11-09T11:30Z q-0001.0001 q-0001\n")

    def put(self, root, name: str, text: str) -> None:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def run_on(self, root, unsettled=lambda root, names: []):
        return migrate_ids.migrate(
            root, NOW, first_added=lambda root, record: ADDED, unsettled=unsettled, left_alone=("docs/research/",)
        )

    def text(self, name: str) -> str:
        return (self.root / name).read_text(encoding="utf-8")

    def new(self, old: str) -> str:
        return self.table[old]

    def test_every_dotted_id_has_a_new_one_in_the_table(self) -> None:
        self.assertEqual({"q-0001", "q-0001.0001", "q-0001.0002", "q-0002"}, set(self.table))
        self.assertTrue(all(questions._IDENTITY.match(new) and "." not in new for new in self.table.values()))
        self.assertEqual(self.table, questions.former_ids(self.root))

    def test_every_entry_is_named_by_its_new_id_and_done_is_gone(self) -> None:
        names = sorted(path.name for path in (self.root / STORE).glob("*.md"))

        self.assertEqual(sorted([f"{new}.md" for new in self.table.values()] + ["former-ids.md"]), names)
        self.assertFalse((self.root / STORE / "done").exists())

    def test_a_title_and_its_relations_name_the_new_ids(self) -> None:
        child = self.text(f"{STORE}/{self.new('q-0001.0002')}.md")

        self.assertTrue(child.startswith(f"# {self.new('q-0001.0002')} Child two?\n"))
        self.assertIn(f"- **part of** {self.new('q-0001')}\n", child)
        self.assertIn(f"- **depends on** {self.new('q-0001.0001')}\n", child)

    def test_siblings_added_in_one_second_keep_todays_order(self) -> None:
        index = questions.read_store(self.root).index

        self.assertLess(index[self.new("q-0001.0001")].opened, index[self.new("q-0001.0002")].opened)
        self.assertEqual(
            [self.new("q-0001"), self.new("q-0001.0001"), self.new("q-0001.0002")],
            [read.identity for read in sorted(index.values(), key=questions._order) if read.identity != self.new("q-0002")],
        )

    def test_every_link_resolves_its_fragment_kept(self) -> None:
        self.assertIn(f"[q-0001.0001](../questions/{self.new('q-0001.0001')}.md#where-it-stands)".replace("[q-0001.0001]", f"[{self.new('q-0001.0001')}]"), self.text("docs/tickets/01-0001-carry.md"))
        self.assertIn(f"]({self.new('q-0001')}.md#decisions)", self.text(f"{STORE}/{self.new('q-0002')}.md"))
        self.assertIn(f"]({self.new('q-0002')}.md)", self.text(f"{STORE}/{self.new('q-0001')}.md"))
        self.assertEqual([], self.migrated.broken)

    def test_a_path_in_a_code_span_becomes_the_new_file_and_a_fence_is_left_as_written(self) -> None:
        notes = self.text("docs/notes.md")

        self.assertIn(f"`docs/questions/{self.new('q-0001.0002')}.md`", notes)
        self.assertIn(f"and {self.new('q-0001.0001')}.", notes)
        self.assertIn("```\nq-0001 as a sample\n```", notes)

    def test_a_binding_moves_and_an_example_keeps_its_id(self) -> None:
        self.assertEqual(f'<straw-dog question="{self.new("q-0001.0002")}">Waits.</straw-dog> An example: q-0001.\n', self.text("AGENTS.md"))
        self.assertTrue(self.text(".agents/scripts/gw/later.py").startswith(f"# TODO {self.new('q-0001.0001')}: when it lands\n"))

    def test_the_rows_name_the_new_ids(self) -> None:
        self.assertEqual(
            f"s-alpha running 2026-11-09T11:30Z {self.new('q-0001.0001')} {self.new('q-0001')}\n", self.text(f"{sessions.ROWS}/s-alpha")
        )

    def test_research_is_left_as_it_stands(self) -> None:
        self.assertEqual("Judged q-0001.0001.\n", self.text("docs/research/run.md"))
        self.assertEqual("q-0001.0001\n", self.text("docs/research/run.txt"))

    def test_the_store_checks_clean_after(self) -> None:
        self.assertEqual([], [note.problem for note in questions.check(self.root).diagnostics])

    def test_a_second_run_changes_nothing(self) -> None:
        self.assertIsNone(self.run_on(self.root))

    def test_a_run_on_a_copy_taken_before_gives_the_same_ids(self) -> None:
        other = self.another_repository()
        self.plant(other)
        shutil.copy(self.root / questions.FORMER_IDS, other / questions.FORMER_IDS)

        self.assertEqual(self.table, self.run_on(other).table)

    def test_an_old_id_named_after_is_told_where_it_went(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(said):
            status = questions.main(["at", "q-0001.0001", "--session", "s-alpha"], root=self.root, now=NOW)

        self.assertEqual(2, status)
        self.assertIn(f"q-0001.0001 is now {self.new('q-0001.0001')}", said.getvalue())

    def test_an_old_id_brought_back_by_a_merge_is_a_finding(self) -> None:
        self.put(self.root, "docs/questions/" + f"{self.new('q-0001')}.md", self.text(f"{STORE}/{self.new('q-0001')}.md") + "\nAlso q-0001.0001.\n")

        findings = [note.finding for note in questions.check(self.root).findings]

        self.assertIn(f"names q-0001.0001, which is now {self.new('q-0001.0001')}", findings)


class Refusals(RepositoryCase):
    def test_a_file_the_run_would_change_left_unsettled_is_refused_and_nothing_written(self) -> None:
        AMigratedTree.put(self, self.root, f"{STORE}/q-0001-which-store.md", entry("q-0001", "Which store?", {"state": "open"}))
        before = (self.root / STORE / "q-0001-which-store.md").read_bytes()

        with self.assertRaises(migrate_ids.Refused):
            migrate_ids.migrate(self.root, NOW, first_added=lambda root, record: ADDED, unsettled=lambda root, names: names)

        self.assertEqual(before, (self.root / STORE / "q-0001-which-store.md").read_bytes())
        self.assertFalse((self.root / questions.FORMER_IDS).exists())

    def test_a_store_with_no_dotted_id_has_nothing_to_migrate(self) -> None:
        AMigratedTree.put(self, self.root, f"{STORE}/q-7f3k2a.md", entry("q-7f3k2a", "New already?", {"state": "open"}))

        self.assertIsNone(migrate_ids.migrate(self.root, NOW))


if __name__ == "__main__":
    unittest.main()

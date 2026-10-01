"""The question store read from disk, and the maintainer's verdict on it."""

from __future__ import annotations

import contextlib
import io
import json
import unittest
from datetime import date

from repository import RepositoryCase

import questions

STORE = "docs/questions"


def entry(identity: str, question: str, parts: dict[str, str]) -> str:
    """An entry in the store's format: the title line, then one bullet per part, in order given."""
    bullets = [f"- **{name}** {value}" for name, value in parts.items()]
    return "\n".join([f"# {identity} {question}", "", *bullets]) + "\n"


class Store(RepositoryCase):
    """A tree holding a small conforming store: one open root with an open child."""

    def setUp(self) -> None:
        super().setUp()
        self.place("q-0001-which-store", "Which store holds the questions?", {"state": "open"})
        self.place(
            "q-0002-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "open"},
        )

    def place(self, stem: str, question: str, parts: dict[str, str], folder: str = STORE) -> str:
        """Writes an entry whose id is the stem's own, so the filename agrees with the title."""
        name = f"{folder}/{stem}.md"
        self.write(name, entry(stem[: stem.index("-", 2)], question, parts))
        return name

    def checked(self):
        return questions.check(self.root)

    def problems(self) -> list[str]:
        return [note.problem for note in self.checked().diagnostics]

    def run_check(self) -> tuple[int, dict]:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root)
        return status, json.loads(said.getvalue())


class AConformingStore(Store):
    def test_checks_clean_and_exits_zero(self) -> None:
        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertEqual([], report["diagnostics"])
        self.assertEqual(2, report["entries"])


class AMalformedEntry(Store):
    def assertReported(self, text: str, fragment: str) -> None:
        self.write(f"{STORE}/q-0003-a-bad-one.md", text)
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_without_a_title_line_naming_its_id(self) -> None:
        self.assertReported("A bad one?\n\n- **state** open\n", "title")

    def test_without_a_state(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"lean": "none"}), "no state")

    def test_with_a_state_outside_the_vocabulary(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "closed:done"}), "state")

    def test_with_a_part_the_format_does_not_have(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "open", "why": "because"}), "why")

    def test_with_a_part_written_twice(self) -> None:
        text = entry("q-0003", "A bad one?", {"state": "open"}) + "- **state** open\n"
        self.assertReported(text, "twice")

    def test_open_but_carrying_an_answer(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "answer": "a reason"}), "open"
        )

    def test_every_part_and_the_suspect_flag_are_the_format(self) -> None:
        self.write("docs/record.md", "# A record\n")
        self.place(
            "q-0003-a-full-one",
            "A full one?",
            {
                "part of": "q-0001",
                "depends on": "q-0001, q-0002",
                "state": "closed:decided, suspect",
                "owner": "[the record](../record.md)",
                "answer": "[the record](../record.md) — the user, 2026-09-29",
                "lean": "held loosely",
            },
        )

        self.assertEqual([], self.problems())


ARCHITECTURE = (
    "# Architecture\n\n"
    "## Decisions landed at this ticket's align\n\n"
    "## Impact — 2026-09-28, the inception\n\n"
    "```md\n## Not a heading, an illustration\n```\n"
)


class TheAnswer(Store):
    """A closed question points to its answer and never holds it (decision 43)."""

    def setUp(self) -> None:
        super().setUp()
        self.write("docs/architecture.md", ARCHITECTURE)

    def close(self, kind: str, answer: str | None, folder: str = STORE) -> None:
        parts = {"state": f"closed:{kind}"} | ({"answer": answer} if answer is not None else {})
        self.place("q-0003-a-closed-one", "A closed one?", parts, folder=folder)

    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_is_required_once_the_question_is_closed(self) -> None:
        self.close("pruned", None)
        self.assertReported("no answer")

    def test_decided_is_a_link_not_prose(self) -> None:
        self.close("decided", "we keep the flat directory — the user, 2026-09-29")
        self.assertReported("not a link")

    def test_decided_to_a_file_that_does_not_exist_is_reported(self) -> None:
        self.close("decided", "[the ADR](../adr/0009-never-written.md) — the user, 2026-09-29")
        self.assertReported("does not resolve")

    def test_decided_to_a_heading_that_does_not_exist_is_reported(self) -> None:
        self.close("decided", "[gone](../architecture.md#not-a-heading-an-illustration)")
        self.assertReported("does not resolve")

    def test_decided_to_a_heading_as_written_resolves(self) -> None:
        self.close(
            "decided",
            "[the align](../architecture.md#decisions-landed-at-this-tickets-align), "
            "[the impact](../architecture.md#impact--2026-09-28-the-inception)",
        )
        self.assertEqual([], self.problems())

    def test_decided_elsewhere_on_the_web_is_a_link(self) -> None:
        self.close("decided", "[the RFC](https://example.invalid/rfc) — the user, 2026-09-29")
        self.assertEqual([], self.problems())

    def test_decided_in_done_resolves_from_there(self) -> None:
        self.close(
            "decided",
            "[the align](../../architecture.md#decisions-landed-at-this-tickets-align)",
            folder=f"{STORE}/done",
        )
        self.assertEqual([], self.problems())

    def test_decided_in_done_whose_heading_no_longer_exists_is_reported(self) -> None:
        self.close("decided", "[the align](../../architecture.md#decisions-landed)", folder=f"{STORE}/done")
        self.assertReported("does not resolve")

    def test_deferred_names_its_condition_and_its_default(self) -> None:
        self.close("deferred", "until the listing stops being readable, meanwhile the flat directory")
        self.assertEqual([], self.problems())

    def test_deferred_without_a_default_is_reported(self) -> None:
        self.close("deferred", "until the listing stops being readable")
        self.assertReported("meanwhile")

    def test_merged_points_at_another_question(self) -> None:
        self.close("merged", "q-0002")
        self.assertEqual([], self.problems())

    def test_superseded_by_prose_is_reported(self) -> None:
        self.close("superseded", "the newer one")
        self.assertReported("id")

    def test_moot_gives_its_reason(self) -> None:
        self.close("moot", "the store became the host's")
        self.assertEqual([], self.problems())


class TheFilename(Store):
    def test_whose_id_disagrees_with_the_title_is_reported(self) -> None:
        self.write(f"{STORE}/q-0003-a-question.md", entry("q-0004", "A question?", {"state": "open"}))

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0004", problems[0])

    def test_whose_slug_is_not_the_questions_words_is_reported(self) -> None:
        self.write(f"{STORE}/q-0003-something-else.md", entry("q-0003", "A question?", {"state": "open"}))

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("slug", problems[0])

    def test_may_shorten_the_question_to_its_leading_words(self) -> None:
        self.place("q-0003-which-package-manager", "Which package manager do we use?", {"state": "open"})
        self.place("q-0004-what-the-tickets-align-holds", "What the ticket's align holds?", {"state": "open"})

        self.assertEqual([], self.problems())

    def test_that_is_not_an_entrys_name_is_reported(self) -> None:
        self.write(f"{STORE}/notes.md", "# Notes\n")

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-NNNN-", problems[0])

    def test_one_id_held_by_two_files_is_reported(self) -> None:
        self.place(
            "q-0002-what-an-entry-holds",
            "What an entry holds?",
            {"state": "closed:moot", "answer": "gone"},
            folder=f"{STORE}/done",
        )

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("two files", problems[0])


class TheRelations(Store):
    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_a_parent_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})
        self.assertReported("q-0009")

    def test_a_dependency_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"depends on": "q-0001, q-0009", "state": "open"})
        self.assertReported("q-0009")

    def test_a_merge_into_a_question_that_does_not_exist_is_an_orphan(self) -> None:
        self.place("q-0003-an-orphan", "An orphan?", {"state": "closed:merged", "answer": "q-0009"})
        self.assertReported("q-0009")

    def test_a_relation_into_done_resolves(self) -> None:
        self.place(
            "q-0003-an-archived-one",
            "An archived one?",
            {"state": "closed:moot", "answer": "no longer asked"},
            folder=f"{STORE}/done",
        )
        self.place("q-0004-a-later-one", "A later one?", {"depends on": "q-0003", "state": "open"})
        self.assertEqual([], self.problems())

    def test_a_parent_line_naming_two_parents_is_reported(self) -> None:
        self.place("q-0003-two-parents", "Two parents?", {"part of": "q-0001, q-0002", "state": "open"})
        self.assertReported("part of")

    def test_a_cycle_in_part_of_is_reported(self) -> None:
        self.place(
            "q-0001-which-store", "Which store holds the questions?", {"part of": "q-0002", "state": "open"}
        )
        self.assertReported("cycle")

    def supersede_the_root_and_close_its_child(self, child_state: str) -> None:
        self.place(
            "q-0001-which-store",
            "Which store holds the questions?",
            {"state": "closed:superseded", "answer": "q-0003"},
        )
        self.place(
            "q-0002-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": child_state, "answer": "the store changed"},
        )
        self.place("q-0003-which-store-now", "Which store now?", {"state": "open"})

    def test_a_closed_child_under_a_superseded_parent_must_be_suspect(self) -> None:
        self.supersede_the_root_and_close_its_child("closed:moot")
        self.assertReported("superseded")

    def test_a_suspect_child_under_a_superseded_parent_is_already_marked(self) -> None:
        self.supersede_the_root_and_close_its_child("closed:moot, suspect")
        self.assertEqual([], self.problems())

    def decide_early(self, state: str) -> None:
        self.place(
            "q-0003-decided-early",
            "Decided early?",
            {"depends on": "q-0001", "state": state, "answer": "overtaken"},
        )

    def test_a_closed_entry_on_an_open_dependency_must_be_suspect(self) -> None:
        self.decide_early("closed:moot")
        self.assertReported("depends on q-0001")

    def test_a_suspect_entry_on_an_open_dependency_says_so_already(self) -> None:
        self.decide_early("closed:moot, suspect")
        self.assertEqual([], self.problems())


SESSIONS = f"{STORE}/sessions"
TODAY = date(2026, 9, 29)


class TheSessions(Store):
    """One line per session: its tag, running or ended, the date it last wrote, its current
    question or `-` before it has one, and up to four recent ones."""

    def setUp(self) -> None:
        super().setUp()
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0002 q-0001\ns-beta ended 2026-09-01 q-0001\n")

    def checked(self):
        return questions.check(self.root, today=TODAY)

    def findings(self) -> list[str]:
        return [note.finding for note in self.checked().findings]

    def assertReported(self, fragment: str) -> None:
        problems = self.problems()
        self.assertEqual(1, len(problems), problems)
        self.assertIn(fragment, problems[0])

    def test_as_written_checks_clean_and_finds_nothing(self) -> None:
        self.assertEqual(([], []), (self.problems(), self.findings()))

    def test_a_session_registered_without_a_position_yet_is_the_form(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 -\n")
        self.assertEqual([], self.problems())

    def test_a_line_out_of_the_form_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha asleep 2026-09-29 q-0002\n")
        self.assertReported("line 1")

    def test_more_than_four_recent_questions_is_out_of_the_form(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0002 q-0001,q-0002,q-0001,q-0002,q-0001\n")
        self.assertReported("line 1")

    def test_a_tag_registered_twice_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0002\ns-alpha ended 2026-09-28 q-0001\n")
        self.assertReported("s-alpha")

    def test_a_position_naming_a_missing_entry_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0009\n")
        self.assertReported("q-0009")

    def test_a_running_session_on_a_closed_question_is_a_finding_not_a_failure(self) -> None:
        self.place(
            "q-0002-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
        )

        stranded = [finding for finding in self.findings() if "s-alpha" in finding]

        self.assertEqual([], self.problems())
        self.assertEqual(1, len(stranded), stranded)
        self.assertIn("closed", stranded[0])

    def test_a_running_session_silent_for_over_a_week_is_a_finding(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-21 q-0002\ns-beta running 2026-09-23 q-0001\n")

        found = self.findings()

        self.assertEqual(1, len(found), found)
        self.assertIn("s-alpha", found[0])

    def test_findings_leave_the_exit_status_at_zero(self) -> None:
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0002\n")

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root, today=TODAY)

        self.assertEqual(0, status)
        self.assertEqual(1, len(json.loads(said.getvalue())["findings"]))


class LikelyTwins(Store):
    def findings(self) -> list[str]:
        return [note.finding for note in questions.check(self.root, today=TODAY).findings]

    def test_two_live_titles_sharing_most_of_their_words_are_a_finding(self) -> None:
        self.place("q-0003-which-package-manager", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager", "What package manager should we use for builds?", {"state": "open"}
        )

        found = self.findings()

        self.assertEqual(1, len(found), found)
        self.assertIn("q-0003", found[0])
        self.assertIn("q-0004", found[0])
        self.assertEqual([], self.problems())

    def test_titles_sharing_a_word_or_two_are_not(self) -> None:
        self.place("q-0003-which-store-holds", "Which store holds the drafts?", {"state": "open"})

        self.assertEqual([], self.findings())

    def test_an_archived_title_is_searched_by_a_person_not_paired_here(self) -> None:
        self.place("q-0003-which-package-manager", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager",
            "What package manager should we use for builds?",
            {"state": "closed:moot", "answer": "no builds"},
            folder=f"{STORE}/done",
        )

        self.assertEqual([], self.findings())


class ReadyForDone(Store):
    """A wholly closed subtree nothing open depends on is ready to move (parent decision 34); a
    deferred or suspect entry counts as open, since the wake reads it in the live store."""

    def ready(self) -> list[str]:
        return [
            note.finding
            for note in questions.check(self.root, today=TODAY).findings
            if "done/" in note.finding
        ]

    def close(self, stem: str, question: str, state: str = "closed:moot", **parts: str) -> None:
        answer = "until the store grows, meanwhile flat" if "deferred" in state else "overtaken"
        self.place(stem, question, parts | {"state": state, "answer": answer})

    def test_a_closed_subtree_under_an_open_parent_is_ready_at_its_own_root(self) -> None:
        self.close("q-0002-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close("q-0003-its-parts", "Its parts?", **{"part of": "q-0002"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0002", ready[0])

    def test_a_wholly_closed_tree_is_ready_once_at_its_root(self) -> None:
        self.close("q-0001-which-store", "Which store holds the questions?")
        self.close("q-0002-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0001", ready[0])

    def test_a_deferred_leaf_is_never_ready(self) -> None:
        self.close(
            "q-0002-what-an-entry-holds", "What an entry holds?", "closed:deferred", **{"part of": "q-0001"}
        )

        self.assertEqual([], self.ready())

    def test_a_subtree_holding_a_suspect_entry_is_never_ready(self) -> None:
        self.close("q-0002-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close("q-0003-its-parts", "Its parts?", "closed:moot, suspect", **{"part of": "q-0002"})

        self.assertEqual([], self.ready())

    def test_a_subtree_an_open_question_depends_on_is_not_ready(self) -> None:
        self.close("q-0002-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.place("q-0003-a-later-one", "A later one?", {"depends on": "q-0002", "state": "open"})

        self.assertEqual([], self.ready())

    def test_ready_leaves_the_exit_status_at_zero(self) -> None:
        self.close("q-0002-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertEqual(1, len(report["findings"]))


class TheMaintainer(Store):
    def test_leaves_the_tree_byte_identical_even_with_findings_and_diagnostics(self) -> None:
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0002\n")
        self.place("q-0003-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})
        untouched = self.snapshot()

        self.run_check()

        self.assertEqual(untouched, self.snapshot())

    def test_an_entry_it_cannot_read_fails_the_run_and_is_named(self) -> None:
        (self.root / STORE / "q-0003-unreadable.md").write_bytes(b"# q-0003 Unreadable\n\n- **state** \xff\n")

        status, report = self.run_check()

        self.assertEqual(1, status)
        self.assertEqual([f"{STORE}/q-0003-unreadable.md"], [passed.get("record") for passed in report["skipped"]])

    def test_a_call_without_its_mode_is_refused(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main([], root=self.root)

        self.assertEqual(2, status)
        self.assertIn("--check", said.getvalue())


class Rendered(Store):
    """A fixed store with two roots of open work, one closed root, and three sessions.

        q-0001 Which store holds the questions?          open
          q-0002 What an entry holds?                    open, lean
            q-0004 Which parts are optional?             open      <- s-alpha
              q-0008 Is the lean optional?               decided, suspect
            q-0005 Is the id a path?                     decided
            q-0006 Is the directory partitioned by root? deferred
          q-0003 How is a subtree archived?              open
            q-0007 Who moves a subtree?                  open
              q-0013 Does the mover repair links?        decided, suspect
            q-0009 Are twins found by embeddings?        deferred
        q-0010 How do sessions reach each other?         open      <- s-beta
        q-0011 Is height depth?                          pruned
        q-0012 (in done/)
    """

    def setUp(self) -> None:
        super().setUp()
        self.write("docs/record.md", "# A record\n")
        decided = "[the record](../record.md) — the user, 2026-09-29"
        self.question("q-0002-what-an-entry-holds", "What an entry holds?", "q-0001", lean="eight parts")
        self.question("q-0003-how-is-a-subtree-archived", "How is a subtree archived?", "q-0001")
        self.question("q-0004-which-parts-are-optional", "Which parts are optional?", "q-0002")
        self.question("q-0005-is-the-id-a-path", "Is the id a path?", "q-0002", "closed:decided", decided)
        self.question(
            "q-0006-is-the-directory-partitioned",
            "Is the directory partitioned by root?",
            "q-0002",
            "closed:deferred",
            "until a listing is unreadable, meanwhile flat",
        )
        self.question("q-0007-who-moves-a-subtree", "Who moves a subtree?", "q-0003")
        self.question(
            "q-0008-is-the-lean-optional", "Is the lean optional?", "q-0004", "closed:decided, suspect", decided
        )
        self.question(
            "q-0009-are-twins-found-by-embeddings",
            "Are twins found by embeddings?",
            "q-0003",
            "closed:deferred",
            "until a place to run, meanwhile word match",
        )
        self.question("q-0010-how-do-sessions-reach", "How do sessions reach each other?")
        self.question("q-0011-is-height-depth", "Is height depth?", None, "closed:pruned", "height was abstraction")
        self.question("q-0012-an-archived-one", "An archived one?", None, "closed:moot", "gone", folder=f"{STORE}/done")
        self.question(
            "q-0013-does-the-mover-repair-links",
            "Does the mover repair links?",
            "q-0007",
            "closed:decided, suspect",
            decided,
        )
        self.write(
            SESSIONS,
            "s-alpha running 2026-09-29 q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-28 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
        )

    def question(
        self,
        stem: str,
        text: str,
        parent: str | None = None,
        state: str = "open",
        answer: str | None = None,
        lean: str | None = None,
        folder: str = STORE,
    ) -> None:
        parts = {"part of": parent, "state": state, "answer": answer, "lean": lean}
        self.place(stem, text, {name: value for name, value in parts.items() if value is not None}, folder)

    def said(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(list(argv), root=self.root, today=TODAY)
        return status, out.getvalue()

    def section(self, text: str, heading: str) -> str:
        """The lines under one heading of the rendering, up to the next blank line."""
        after = text.split(heading, 1)[1]
        return after.split("\n\n", 1)[0]


class TheWindow(Rendered):
    def test_draws_the_path_from_the_root_to_the_sessions_position(self) -> None:
        status, text = self.said("--window", "--session", "s-alpha")

        path = self.section(text, "path (root to current):")
        self.assertEqual(0, status)
        self.assertEqual(["q-0001", "q-0002", "q-0004"], [line.split()[0] for line in path.strip().splitlines()])
        self.assertIn("<- current", path.splitlines()[-1])

    def test_each_line_carries_its_state_and_its_lean(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("q-0002 [open] What an entry holds?  ~ eight parts", text)

    def test_the_frontier_holds_every_child_of_the_path_closed_ones_with_their_kind(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        frontier = self.section(text, "frontier (children of each question on the path):")
        self.assertIn("under q-0001: q-0003 [open]", frontier)
        self.assertIn("under q-0002: q-0005 [closed:decided]", frontier)
        self.assertIn("under q-0002: q-0006 [closed:deferred]", frontier)
        self.assertIn("under q-0004: q-0008 [closed:decided, suspect]", frontier)

    def test_lists_the_roots_open_questions_with_their_parents(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        listed = self.section(text, "open questions under this root (q-0001), with their parent:")
        self.assertIn("q-0007 (parent q-0003) Who moves a subtree?", listed)

    def test_shows_a_suspect_anywhere_under_the_root_and_no_other_closed_entry_off_the_path(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("q-0013 [closed:decided, suspect]", self.section(text, "suspect under this root:"))
        self.assertNotIn("q-0009", text)
        self.assertNotIn("q-0012", text)

    def test_gives_one_line_to_each_other_root(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        roots = self.section(text, "other roots:").strip().splitlines()
        self.assertEqual(["q-0010 [open] How do sessions reach each other?", "q-0011 [closed:pruned] Is height depth?"], [line.strip() for line in roots])

    def test_names_the_recent_positions_the_other_running_sessions_and_the_next_free_id(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("recently attached: q-0002, q-0001", text)
        others = self.section(text, "other running sessions:")
        self.assertIn("s-beta at q-0010 (last wrote 2026-09-28)", others)
        self.assertNotIn("s-gamma", others)
        self.assertNotIn("s-alpha", others)
        self.assertIn("next free id: q-0014", text)


class TwoSessions(Rendered):
    def test_each_window_is_drawn_around_its_own_position_and_lists_the_other(self) -> None:
        _, beta = self.said("--window", "--session", "s-beta")

        self.assertIn("current: q-0010", beta)
        self.assertEqual("q-0010", self.section(beta, "path (root to current):").split()[0])
        self.assertIn("q-0001 [open] Which store holds the questions?", self.section(beta, "other roots:"))
        self.assertIn("s-alpha at q-0004", self.section(beta, "other running sessions:"))

    def test_a_session_without_a_position_yet_is_given_the_roots_to_place_itself_among(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 -\ns-beta running 2026-09-28 q-0010\n")

        status, text = self.said("--window", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertIn("current: none yet", text)
        roots = self.section(text, "roots:")
        self.assertIn("q-0001", roots)
        self.assertIn("q-0010", roots)
        self.assertIn("s-beta at q-0010", text)
        self.assertIn("next free id: q-0014", text)

    def test_a_session_nobody_registered_is_refused_with_the_way_to_register(self) -> None:
        status, text = self.said("--window", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertIn("--wake", text)


class TheWake(Rendered):
    def registered_tag(self, text: str) -> str:
        return text.splitlines()[0].split()[1].rstrip(",")

    def test_registers_a_new_session_without_a_position_and_prints_its_tag(self) -> None:
        before = self.read(SESSIONS)

        status, text = self.said("--wake")

        tag = self.registered_tag(text)
        self.assertEqual(0, status)
        self.assertEqual(before + f"{tag} running 2026-09-29 -\n", self.read(SESSIONS))
        self.assertIn("registered now", text.splitlines()[0])

    def test_two_wakes_register_two_sessions(self) -> None:
        _, first = self.said("--wake")
        _, second = self.said("--wake")

        self.assertNotEqual(self.registered_tag(first), self.registered_tag(second))
        self.assertEqual(5, len(self.read(SESSIONS).splitlines()))

    def test_reports_the_sessions_first_running_and_ended_with_their_positions(self) -> None:
        _, text = self.said("--wake")

        sessions = self.section(text, "sessions:")
        self.assertIn("s-alpha running, last wrote 2026-09-29, at q-0004", sessions)
        self.assertIn("s-gamma ended, last wrote 2026-09-20, at q-0003", sessions)
        self.assertLess(text.index("sessions:"), text.index("deferred"))

    def test_lists_every_deferral_with_its_condition_and_every_suspect_entry(self) -> None:
        _, text = self.said("--wake")

        deferred = self.section(text, "deferred, to re-check whether each condition is met:")
        self.assertIn("q-0006", deferred)
        self.assertIn("q-0009 [closed:deferred] Are twins found by embeddings? — until a place to run, meanwhile word match", deferred)
        suspect = self.section(text, "suspect, to re-read:")
        self.assertIn("q-0008", suspect)
        self.assertIn("q-0013", suspect)

    def test_a_new_session_is_given_the_roots_to_place_itself_among(self) -> None:
        _, text = self.said("--wake")

        self.assertIn("current: none yet", text)
        self.assertIn("q-0010", self.section(text, "roots:"))

    def test_for_a_registered_session_registers_nothing_and_draws_its_window(self) -> None:
        untouched = self.snapshot()

        status, text = self.said("--wake", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertEqual(untouched, self.snapshot())
        self.assertIn("current: q-0004", text)
        self.assertIn("q-0009", self.section(text, "deferred, to re-check whether each condition is met:"))

    def test_for_a_session_nobody_registered_is_refused(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said("--wake", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertEqual(untouched, self.snapshot())


class TheEnd(Rendered):
    def test_marks_the_session_ended_keeping_its_position_and_touching_no_other_line(self) -> None:
        status, _ = self.said("--end", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertEqual(
            "s-alpha ended 2026-09-29 q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-28 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
            self.read(SESSIONS),
        )

    def test_a_later_wake_finds_where_the_ended_session_stopped(self) -> None:
        self.said("--end", "--session", "s-alpha")

        _, text = self.said("--wake")

        self.assertIn("s-alpha ended, last wrote 2026-09-29, at q-0004", self.section(text, "sessions:"))

    def test_a_session_nobody_registered_is_refused_and_nothing_is_written(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said("--end", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertEqual(untouched, self.snapshot())


class TheTree(Rendered):
    def test_draws_every_live_root_and_everything_under_it_indented_in_id_order(self) -> None:
        status, text = self.said("--tree")

        self.assertEqual(0, status)
        self.assertEqual(
            [
                "q-0001 [open] Which store holds the questions?",
                "  q-0002 [open] What an entry holds?  ~ eight parts",
                "    q-0004 [open] Which parts are optional?",
                "      q-0008 [closed:decided, suspect] Is the lean optional?",
                "    q-0005 [closed:decided] Is the id a path?",
                "    q-0006 [closed:deferred] Is the directory partitioned by root?",
                "  q-0003 [open] How is a subtree archived?",
                "    q-0007 [open] Who moves a subtree?",
                "      q-0013 [closed:decided, suspect] Does the mover repair links?",
                "    q-0009 [closed:deferred] Are twins found by embeddings?",
                "q-0010 [open] How do sessions reach each other?",
                "q-0011 [closed:pruned] Is height depth?",
            ],
            text.splitlines(),
        )

    def test_under_one_question_draws_that_subtree_alone(self) -> None:
        _, text = self.said("--tree", "q-0003")

        self.assertEqual(
            [
                "q-0003 [open] How is a subtree archived?",
                "  q-0007 [open] Who moves a subtree?",
                "    q-0013 [closed:decided, suspect] Does the mover repair links?",
                "  q-0009 [closed:deferred] Are twins found by embeddings?",
            ],
            text.splitlines(),
        )

    def test_under_a_question_no_live_entry_holds_is_refused(self) -> None:
        status, text = self.said("--tree", "q-0012")

        self.assertEqual(2, status)
        self.assertIn("q-0012", text)


class ItsOutput(Rendered):
    def test_is_utf8_whatever_the_consoles_encoding_so_any_title_prints(self) -> None:
        self.place("q-0010-how-do-sessions-reach", "How do sessions reach each other → remotely?", {"state": "open"})
        raw = io.BytesIO()
        console = io.TextIOWrapper(raw, encoding="cp1252")

        with contextlib.redirect_stdout(console):
            status = questions.main(["--tree", "q-0010"], root=self.root, today=TODAY)
            console.flush()

        self.assertEqual(0, status)
        self.assertIn("each other → remotely?", raw.getvalue().decode("utf-8"))


class Declared(Rendered):
    """The writer over the fixed store, as s-alpha at q-0004 declares."""

    def declare(self, line: str, session: str = "s-alpha") -> tuple[int, str]:
        return self.said("--declare", line, "--session", session)

    def entry_text(self, stem: str, folder: str = STORE) -> str:
        return self.read(f"{folder}/{stem}.md")

    def own_line(self, tag: str = "s-alpha") -> str:
        return next(line for line in self.read(SESSIONS).splitlines() if line.startswith(f"{tag} "))


class OpeningAndPlacing(Declared):
    def test_opens_a_question_under_another_and_places_the_session_there(self) -> None:
        status, said = self.declare("at q-0014; opens q-0014 under q-0004: Is the owner optional?")

        self.assertEqual(0, status, said)
        self.assertEqual(
            "# q-0014 Is the owner optional?\n\n- **part of** q-0004\n- **state** open\n",
            self.entry_text("q-0014-is-the-owner-optional"),
        )
        self.assertEqual("s-alpha running 2026-09-29 q-0014 q-0004,q-0002,q-0001", self.own_line())
        self.assertIn("q-0014", said)


class EachClause(Declared):
    """One test per clause of the grammar: it writes, and it reads back as written."""

    def assertDeclared(self, line: str) -> None:
        status, said = self.declare(line)
        self.assertEqual(0, status, said)

    def part(self, stem: str, name: str, folder: str = STORE) -> str | None:
        found = [
            line.split("** ", 1)[1]
            for line in self.entry_text(stem, folder).splitlines()
            if line.startswith(f"- **{name}** ")
        ]
        return found[0] if found else None

    def test_opens_a_root(self) -> None:
        self.assertDeclared("at q-0014; opens q-0014: Is there a third root?")
        self.assertIsNone(self.part("q-0014-is-there-a-third-root", "part of"))

    def test_opens_between_two_questions_reparenting_the_lower(self) -> None:
        self.assertDeclared("at q-0014; opens q-0014 between q-0002 and q-0004: What must an entry hold?")
        self.assertEqual("q-0002", self.part("q-0014-what-must-an-entry-hold", "part of"))
        self.assertEqual("q-0014", self.part("q-0004-which-parts-are-optional", "part of"))

    def test_moves_a_question_under_another(self) -> None:
        self.assertDeclared("at q-0004; moves q-0007 under q-0002")
        self.assertEqual("q-0002", self.part("q-0007-who-moves-a-subtree", "part of"))

    def test_moves_a_question_to_root(self) -> None:
        self.assertDeclared("at q-0004; moves q-0007 to root")
        self.assertIsNone(self.part("q-0007-who-moves-a-subtree", "part of"))

    def test_depends_adds_to_what_a_question_waits_on(self) -> None:
        self.assertDeclared("at q-0004; depends q-0004 on q-0010; depends q-0004 on q-0003")
        self.assertEqual("q-0010, q-0003", self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_closes_as_decided_with_its_link(self) -> None:
        self.assertDeclared("at q-0002; closes q-0004: decided, [the record](../record.md) — the user, 2026-09-29")
        self.assertEqual("closed:decided", self.part("q-0004-which-parts-are-optional", "state"))
        self.assertEqual(
            "[the record](../record.md) — the user, 2026-09-29", self.part("q-0004-which-parts-are-optional", "answer")
        )

    def test_closes_as_deferred_with_its_condition_and_default(self) -> None:
        self.assertDeclared("at q-0004; closes q-0007: deferred, until the mover exists, meanwhile by hand")
        self.assertEqual("until the mover exists, meanwhile by hand", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_closes_as_merged_into_another(self) -> None:
        self.assertDeclared("at q-0004; closes q-0007: merged, q-0003")
        self.assertEqual("closed:merged", self.part("q-0007-who-moves-a-subtree", "state"))
        self.assertEqual("q-0003", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_suspects_and_clears(self) -> None:
        self.assertDeclared("at q-0004; suspects q-0005; clears q-0008")
        self.assertEqual("closed:decided, suspect", self.part("q-0005-is-the-id-a-path", "state"))
        self.assertEqual("closed:decided", self.part("q-0008-is-the-lean-optional", "state"))

    def test_leans(self) -> None:
        self.assertDeclared("at q-0004; leans q-0004: the required ones only")
        self.assertEqual("the required ones only", self.part("q-0004-which-parts-are-optional", "lean"))

    def test_assigns_an_owner_as_a_link_from_the_entry(self) -> None:
        self.assertDeclared("at q-0004; assigns q-0004 to docs/record.md")
        self.assertEqual("[record](../record.md)", self.part("q-0004-which-parts-are-optional", "owner"))

    def test_at_alone_moves_the_position_and_keeps_the_last_as_recent(self) -> None:
        self.assertDeclared("at q-0010")
        self.assertEqual("s-alpha running 2026-09-29 q-0010 q-0004,q-0002,q-0001", self.own_line())

    def test_nothing_writes_nothing(self) -> None:
        untouched = self.snapshot()

        self.assertDeclared("nothing")

        self.assertEqual(untouched, self.snapshot())


class Refusals(Declared):
    """A refused line names its reason and writes nothing at all."""

    def assertRefused(self, line: str, reason: str, session: str = "s-alpha") -> None:
        untouched = self.snapshot()

        status, said = self.declare(line, session)

        self.assertEqual(2, status, said)
        self.assertIn(reason, said)
        self.assertEqual(untouched, self.snapshot())

    def test_a_malformed_clause(self) -> None:
        self.assertRefused("at q-0004; go to q-0010", "`go to q-0010` is not a clause")

    def test_a_semicolon_in_free_text(self) -> None:
        self.assertRefused("at q-0004; leans q-0004: this;that", "`;`")

    def test_a_line_without_its_position(self) -> None:
        self.assertRefused("leans q-0004: the required ones", "exactly one `at`")

    def test_an_id_that_is_not_the_next_free_one(self) -> None:
        self.assertRefused("at q-0020; opens q-0020: Too far ahead?", "the next free id is q-0014")

    def test_a_position_on_a_closed_question(self) -> None:
        self.assertRefused("at q-0005", "a position is an open question")

    def test_a_question_nobody_holds(self) -> None:
        self.assertRefused("at q-0004; leans q-0099: a lean", "no entry holds q-0099")

    def test_a_between_whose_lower_is_not_part_of_the_upper(self) -> None:
        self.assertRefused(
            "at q-0014; opens q-0014 between q-0003 and q-0004: Misplaced?", "q-0004 is not part of q-0003"
        )

    def test_a_move_that_makes_a_cycle(self) -> None:
        self.assertRefused("at q-0004; moves q-0002 under q-0004", "cycle")

    def test_a_dependency_that_makes_a_cycle(self) -> None:
        self.assertRefused("at q-0004; depends q-0004 on q-0003; depends q-0003 on q-0004", "cycle")

    def test_a_prune_that_leaves_an_open_child(self) -> None:
        self.assertRefused("at q-0010; closes q-0003: pruned, not worth holding", "leaves q-0007 open")

    def test_a_kind_without_its_pointer(self) -> None:
        self.assertRefused("at q-0002; closes q-0004: decided", "no answer")

    def test_a_decided_answer_that_does_not_resolve(self) -> None:
        self.assertRefused("at q-0002; closes q-0004: decided, [gone](../gone.md)", "does not resolve")

    def test_a_session_nobody_registered(self) -> None:
        self.assertRefused("at q-0004", "no session s-nobody", session="s-nobody")


class Interference(Declared):
    """What another writer does between this line's validation and its write."""

    def declare_with(self, line: str, meanwhile) -> None:
        questions.declare(self.root, "s-alpha", questions.parse(line), TODAY, between=meanwhile)

    def test_an_entry_changed_on_disk_refuses_the_line_and_keeps_the_other_writers_text(self) -> None:
        intruder = entry("q-0004", "Which parts are optional?", {"part of": "q-0002", "state": "open", "lean": "theirs"})
        before = self.snapshot()

        with self.assertRaises(questions.Refused) as refused:
            self.declare_with(
                "at q-0004; leans q-0004: mine",
                lambda: self.write(f"{STORE}/q-0004-which-parts-are-optional.md", intruder),
            )

        self.assertIn("changed since this line was read", str(refused.exception))
        self.assertEqual(intruder, self.entry_text("q-0004-which-parts-are-optional"))
        after = self.snapshot()
        del before[f"{STORE}/q-0004-which-parts-are-optional.md"], after[f"{STORE}/q-0004-which-parts-are-optional.md"]
        self.assertEqual(before, after, "nothing else was written")

    def test_a_second_session_taking_the_id_just_written_is_refused(self) -> None:
        theirs = entry("q-0014", "Their question?", {"state": "open"})

        with self.assertRaises(questions.Refused) as refused:
            self.declare_with(
                "at q-0014; opens q-0014: My question?",
                lambda: self.write(f"{STORE}/q-0014-their-question.md", theirs),
            )

        self.assertIn("declare it again with the next free id", str(refused.exception))
        self.assertFalse((self.root / STORE / "q-0014-my-question.md").exists())

    def test_a_sessions_at_changes_its_own_line_and_keeps_one_another_session_wrote_meanwhile(self) -> None:
        def beta_moves() -> None:
            self.write(SESSIONS, self.read(SESSIONS).replace("s-beta running 2026-09-28 q-0010", "s-beta running 2026-09-29 q-0001 q-0010"))

        self.declare_with("at q-0002", beta_moves)

        self.assertEqual(
            "s-alpha running 2026-09-29 q-0002 q-0004,q-0001\n"
            "s-beta running 2026-09-29 q-0001 q-0010\n"
            "s-gamma ended 2026-09-20 q-0003\n",
            self.read(SESSIONS),
        )

    def test_a_write_that_fails_partway_stops_and_reports_what_it_wrote(self) -> None:
        def sessions_file_becomes_a_folder() -> None:
            (self.root / SESSIONS).unlink()
            (self.root / SESSIONS).mkdir()

        with self.assertRaises(questions.WriteInterrupted) as stopped:
            self.declare_with("at q-0004; leans q-0004: written first", sessions_file_becomes_a_folder)

        self.assertEqual([f"{STORE}/q-0004-which-parts-are-optional.md"], stopped.exception.completed)
        self.assertEqual(SESSIONS, stopped.exception.failed)
        self.assertIn("written first", self.entry_text("q-0004-which-parts-are-optional"))


class InOrder(Declared):
    def test_clauses_apply_left_to_right_and_at_is_checked_against_the_result(self) -> None:
        status, said = self.declare(
            "at q-0015; opens q-0014 under q-0004: Is the owner optional?; "
            "opens q-0015 under q-0004: Is the owner required at birth?; closes q-0014: merged, q-0015"
        )

        self.assertEqual(0, status, said)
        self.assertIn("- **state** closed:merged\n- **answer** q-0015", self.entry_text("q-0014-is-the-owner-optional"))
        self.assertIn("- **state** open", self.entry_text("q-0015-is-the-owner-required-at-birth"))
        self.assertEqual("q-0015", self.own_line().split()[3])

    def test_a_prune_goes_through_once_the_child_that_stands_alone_is_moved_out_first(self) -> None:
        status, said = self.declare("at q-0001; moves q-0007 to root; closes q-0003: pruned, archiving is the mover's")

        self.assertEqual(0, status, said)
        self.assertIn("closed:pruned", self.entry_text("q-0003-how-is-a-subtree-archived"))


class ARoundTrip(Declared):
    def test_opens_attaches_closes_and_prunes_then_checks_clean(self) -> None:
        self.assertEqual([], self.problems(), "the fixture itself is clean")

        for line in (
            "at q-0014; opens q-0014 under q-0004: Is the owner optional?",
            "at q-0015; opens q-0015 under q-0014: Must an owner exist at birth?",
            "at q-0014; closes q-0015: decided, [the record](../record.md) — the user, 2026-09-29",
            "at q-0004; closes q-0014: pruned, the store keeps no owner rule",
        ):
            status, said = self.declare(line)
            self.assertEqual(0, status, f"{line}: {said}")

        self.assertEqual([], self.problems())
        self.assertIn("q-0014 [closed:pruned]", self.said("--tree", "q-0004")[1])


class AFirstWake(RepositoryCase):
    def test_in_a_tree_without_a_store_registers_the_first_session(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(["--wake"], root=self.root, today=TODAY)

        tag = out.getvalue().splitlines()[0].split()[1].rstrip(",")
        self.assertEqual(0, status)
        self.assertEqual(f"{tag} running 2026-09-29 -\n", self.read(SESSIONS))


class NoStoreToDraw(RepositoryCase):
    def test_the_window_says_there_is_no_store_and_exits_zero(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(["--window", "--session", "s-alpha"], root=self.root)

        self.assertEqual(0, status)
        self.assertIn("no store", out.getvalue())


class NoStore(RepositoryCase):
    def test_a_tree_without_a_store_says_so_and_exits_zero(self) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root)

        self.assertEqual(0, status)
        self.assertEqual("absent", json.loads(said.getvalue())["store"])


if __name__ == "__main__":
    unittest.main()

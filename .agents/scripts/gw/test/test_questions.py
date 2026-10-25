# Mechanism: questions
"""The question store read from disk, and the maintainer's verdict on it."""

from __future__ import annotations

import contextlib
import io
import json
import os
import re
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from repository import RepositoryCase, folder_listing

import questions
import sessions

STORE = "docs/questions"
DESKTOP_ID = "CLAUDE_CODE_HOST_SESSION_ID"


def remember_windows_in_the_case(case: unittest.TestCase) -> None:
    """Keep what `--window` remembers inside the case, never in the machine's temp folder."""
    memory = tempfile.TemporaryDirectory()
    case.addCleanup(memory.cleanup)
    patcher = mock.patch.object(sessions, "WINDOW_MEMORY", memory.name)
    patcher.start()
    case.addCleanup(patcher.stop)


OPEN_KIND = "what it intends to become"
CLOSED_KIND = "what happened"


def entry(identity: str, question: str, parts: dict[str, str], marked: bool = True) -> str:
    """An entry in the store's format: the title line, then one bullet per part, in order given —
    opening, unless a test says otherwise, with the mark its state calls for."""
    state = parts.get("state", "")
    if marked and "record of" not in parts and state:
        parts = {"record of": OPEN_KIND if state.startswith("open") else CLOSED_KIND, **parts}
    bullets = [f"- **{name}** {value}" for name, value in parts.items()]
    return "\n".join([f"# {identity} {question}", "", *bullets]) + "\n"


class Store(RepositoryCase):
    """A tree holding a small conforming store: one open root with an open child."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)
        self.seed()

    def seed(self) -> None:
        self.place("q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"state": "open"})
        self.place(
            "q-0001.0001-what-an-entry-holds",
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
        self.assertReported(f"A bad one?\n\n- **record of** {OPEN_KIND}\n- **state** open\n", "title")

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
            "q-0001.0002-a-full-one",
            "A full one?",
            {
                "part of": "q-0001",
                "depends on": "q-0001, q-0001.0001",
                "state": "closed:decided, suspect",
                "owner": "[the record](../record.md)",
                "answer": "[the record](../record.md) — the user, 2026-09-29",
                "realizes": 'A7 "The question store", A12 "A session resumes, at its step"',
                "lean": "held loosely",
                "struck": "2, last 2026-10-02T19:40Z",
            },
        )

        self.assertEqual([], self.problems())

    def test_with_a_trace_link_that_names_no_answer_by_id_and_name(self) -> None:
        for written in ("A7", 'A7 "The store", A7 "Again"', 'derived, A7 "The store"', '"The store"'):
            with self.subTest(written=written):
                self.assertReported(entry("q-0003", "A bad one?", {"state": "open", "realizes": written}), "realizes")

    def test_carrying_no_mark(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "open"}, marked=False), "names no kind")

    def test_marked_with_the_kind_another_state_calls_for(self) -> None:
        with self.subTest(state="open"):
            self.assertReported(
                entry("q-0003", "A bad one?", {"record of": CLOSED_KIND, "state": "open"}), "an open entry"
            )
        with self.subTest(state="closed"):
            self.assertReported(
                entry("q-0003", "A bad one?", {"record of": OPEN_KIND, "state": "closed:moot", "answer": "gone"}),
                "a closed entry",
            )

    def test_carrying_the_mark_under_its_former_name(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"kind": OPEN_KIND, "state": "open"}, marked=False), "`- **kind**`"
        )

    def test_a_strike_without_its_last_time(self) -> None:
        self.assertReported(entry("q-0003", "A bad one?", {"state": "open", "struck": "2"}), "last <YYYY-MM-DDTHH:MMZ>")

    def test_a_strike_whose_time_has_no_zone(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "2, last 2026-10-02T19:40"}), "last <YYYY-MM-DDTHH:MMZ>"
        )

    def test_a_strike_with_a_negative_count(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "-1, last 2026-10-02T19:40Z"}), "last <YYYY-MM-DDTHH:MMZ>"
        )

    def test_a_strike_on_a_day_the_calendar_lacks(self) -> None:
        self.assertReported(
            entry("q-0003", "A bad one?", {"state": "open", "struck": "1, last 2026-13-02T19:40Z"}), "last <YYYY-MM-DDTHH:MMZ>"
        )


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
        self.close("merged", "q-0001.0001")
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

    def test_holds_every_word_of_the_question_an_apostrophe_dropped(self) -> None:
        self.place("q-0003-what-the-tickets-align-holds", "What the ticket's align holds?", {"state": "open"})

        self.assertEqual([], self.problems())

    def test_that_stops_short_of_the_whole_question_is_reported_with_the_name_it_needs(self) -> None:
        self.place("q-0003-which-package-manager", "Which package manager do we use?", {"state": "open"})

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0003-which-package-manager-do-we-use.md", problems[0])

    def test_that_is_not_an_entrys_name_is_reported(self) -> None:
        self.write(f"{STORE}/notes.md", "# Notes\n")

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-NNNN-", problems[0])

    def test_one_id_held_by_two_files_is_reported(self) -> None:
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
            folder=f"{STORE}/done",
        )

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("two files", problems[0])


class NestedIds(Store):
    """An id says where its question sits: a root's position, then one per level below it."""

    def test_a_nested_id_reads_in_a_title_a_name_a_relation_and_a_session_line(self) -> None:
        self.place(
            "q-0001.0001.0001-which-parts", "Which parts?", {"part of": "q-0001.0001", "depends on": "q-0001.0001", "state": "open"}
        )
        self.write(f"{STORE}/sessions", "s-alpha running 2026-09-29 q-0001.0001.0001 q-0001.0001,q-0001\n")

        self.assertEqual([], self.problems())

    def test_the_tree_draws_a_child_after_its_parent_and_before_the_next_root(self) -> None:
        self.place("q-0002-a-second-root", "A second root?", {"state": "open"})
        self.place("q-0001.0002-a-second-child", "A second child?", {"part of": "q-0001", "state": "open"})

        self.assertEqual(
            [
                "q-0001 [open] Which store holds the questions?",
                "  q-0001.0001 [open] What an entry holds?",
                "  q-0001.0002 [open] A second child?",
                "q-0002 [open] A second root?",
            ],
            questions.tree(self.root).splitlines(),
        )

    def test_a_child_whose_id_is_not_under_its_parents_is_reported(self) -> None:
        self.place("q-0003-a-flat-child", "A flat child?", {"part of": "q-0001", "state": "open"})

        self.assertEqual(["q-0003 is part of q-0001, so its id is q-0001.NNNN"], self.problems())

    def test_a_root_whose_id_is_nested_is_reported(self) -> None:
        self.place("q-0002.0001-a-lost-one", "A lost one?", {"state": "open"})

        self.assertEqual(["q-0002.0001 is part of nothing, so its id is q-NNNN"], self.problems())

    def test_an_orphans_id_is_not_judged_since_its_parent_is_reported_missing(self) -> None:
        self.place("q-0001.0002-an-orphan", "An orphan?", {"part of": "q-0009", "state": "open"})

        problems = self.problems()

        self.assertEqual(1, len(problems), problems)
        self.assertIn("q-0009, which no entry holds", problems[0])


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
        self.place("q-0003-two-parents", "Two parents?", {"part of": "q-0001, q-0001.0001", "state": "open"})
        self.assertReported("part of")

    def test_a_cycle_in_part_of_is_reported(self) -> None:
        self.place(
            "q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"part of": "q-0001.0001", "state": "open"}
        )
        self.assertTrue(any("cycle" in problem for problem in self.problems()), self.problems())

    def supersede_the_root_and_close_its_child(self, child_state: str) -> None:
        self.place(
            "q-0001-which-store-holds-the-questions",
            "Which store holds the questions?",
            {"state": "closed:superseded", "answer": "q-0003"},
        )
        self.place(
            "q-0001.0001-what-an-entry-holds",
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


# The single file a store from before keeps: a case written into it is carried over by the first
# write, so every such case proves the carry-over too.
SESSIONS = f"{STORE}/sessions"
TODAY = date(2026, 9, 29)


def session_lines(root: Path) -> str:
    """Every session's line as written, wherever it stands — its own file, or the single file not
    carried over yet — in the order the store lists them."""
    lines = []
    for held in sessions.rows(root)[0]:
        with (root / held.record).open(encoding="utf-8", newline="") as handle:
            lines.append(handle.read().splitlines()[held.line - 1])
    return "".join(f"{line}\n" for line in lines)
NOW = datetime(2026, 9, 29, 12, 0, tzinfo=timezone.utc)


class LikelyTwins(Store):
    def findings(self) -> list[str]:
        return [note.finding for note in questions.check(self.root).findings]

    def test_two_live_titles_sharing_most_of_their_words_are_a_finding(self) -> None:
        self.place("q-0003-which-package-manager-do-we-use", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager-should-we-use-for-builds",
            "What package manager should we use for builds?",
            {"state": "open"},
        )

        found = self.findings()

        self.assertEqual(1, len(found), found)
        self.assertIn("q-0003", found[0])
        self.assertIn("q-0004", found[0])
        self.assertEqual([], self.problems())

    def test_titles_sharing_a_word_or_two_are_not(self) -> None:
        self.place("q-0003-which-store-holds-the-drafts", "Which store holds the drafts?", {"state": "open"})

        self.assertEqual([], self.findings())

    def test_an_archived_title_is_searched_by_a_person_not_paired_here(self) -> None:
        self.place("q-0003-which-package-manager-do-we-use", "Which package manager do we use?", {"state": "open"})
        self.place(
            "q-0004-what-package-manager-should-we-use-for-builds",
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
            for note in questions.check(self.root).findings
            if "done/" in note.finding
        ]

    def close(self, stem: str, question: str, state: str = "closed:moot", **parts: str) -> None:
        answer = "until the store grows, meanwhile flat" if "deferred" in state else "overtaken"
        self.place(stem, question, parts | {"state": state, "answer": answer})

    def test_a_closed_subtree_under_an_open_parent_is_ready_at_its_own_root(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close("q-0001.0001.0001-its-parts", "Its parts?", **{"part of": "q-0001.0001"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0001.0001 and", ready[0])

    def test_a_wholly_closed_tree_is_ready_once_at_its_root(self) -> None:
        self.close("q-0001-which-store-holds-the-questions", "Which store holds the questions?")
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        ready = self.ready()

        self.assertEqual(1, len(ready), ready)
        self.assertIn("q-0001 and", ready[0])

    def test_a_deferred_leaf_is_never_ready(self) -> None:
        self.close(
            "q-0001.0001-what-an-entry-holds", "What an entry holds?", "closed:deferred", **{"part of": "q-0001"}
        )

        self.assertEqual([], self.ready())

    def test_a_subtree_holding_a_suspect_entry_is_never_ready(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.close(
            "q-0001.0001.0001-its-parts", "Its parts?", "closed:moot, suspect", **{"part of": "q-0001.0001"}
        )

        self.assertEqual([], self.ready())

    def test_a_subtree_an_open_question_depends_on_is_not_ready(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})
        self.place("q-0003-a-later-one", "A later one?", {"depends on": "q-0001.0001", "state": "open"})

        self.assertEqual([], self.ready())

    def test_ready_leaves_the_exit_status_at_zero(self) -> None:
        self.close("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001"})

        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertEqual(1, len(report["findings"]))


PATH_NOW = datetime(2026, 9, 29, 12, 0, tzinfo=timezone.utc)
PATH_PRODUCT = (
    "# What the project is for\n\n## Pains\n\n1. **It hurts.**\n\n## Causes\n\n- **C1** A cause.\n\n"
    "## Answers\n\n| answer | causes | 1 | waits on |\n|---|---|---|---|\n| **The first group** | | | |\n"
    "| **A1 The question store** — what it does | C1 | ● | |\n\n## After\n\nProse.\n"
)


def path_ticket(title: str, status: str, answers: str, depends: str = "") -> str:
    """A live ticket's header, enough for the path to read: its title, status and question."""
    lines = [f"# {title}", "", "- **record of** what it intends to become", f"- **Status:** {status}",
             "- **Type:** AFK", "- **Minted:** 2026-09-29"]
    lines += [f"- **Depends on:** {depends}"] if depends else []
    lines += [f"- **Answers:** [{answers}](../questions/{answers}-q.md)", "- **Outcome:** It works.", ""]
    return "\n".join(lines)


class ThePathAhead(RepositoryCase):
    """The path read from the records as they are (01-0060.0010): what is in work, what was touched
    lately with no ticket, the candidates with their reasons, and the roots' balance."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)

    def question(self, identity: str, words: str, parent: str | None = None, owner: str | None = None,
                 struck: tuple[int, int] | None = None, realizes: str | None = None) -> None:
        parts = {"part of": parent, "state": "open"}
        parts["owner"] = f"[{owner}](../tickets/{owner}.md)" if owner else None
        parts["realizes"] = realizes
        if struck:
            stamped = PATH_NOW - timedelta(days=struck[1])
            parts["struck"] = f"{struck[0]}, last {stamped:%Y-%m-%dT%H:%MZ}"
        parts = {name: value for name, value in parts.items() if value is not None}
        self.write(f"{STORE}/{identity}-q.md", entry(identity, words, parts))

    def a_tree(self) -> None:
        self.question("q-0001", "What is this project for?", struck=(5, 1))
        self.question("q-0001.0001", "Who is it for?", parent="q-0001", struck=(2, 2))
        self.question("q-0002", "How is it built?")
        self.question("q-0002.0001", "How are the questions kept?", parent="q-0002",
                      owner="01-0010-questions-kept", realizes='A1 "The question store"')
        self.question("q-0002.0001.0001", "How does a question branch?", parent="q-0002.0001",
                      owner="01-0010.0010-a-question-branches")
        self.question("q-0002.0002", "How is a ticket closed?", parent="q-0002", owner="01-0020-a-ticket-closes")
        self.question("q-0002.0003", "Is the cap right?", parent="q-0002", struck=(0, 30))
        self.question("q-0002.0004", "Does the path read?", parent="q-0002", struck=(3, 20))
        self.question("q-0002.0005", "Is the cap read?", parent="q-0002", owner="01-0030-the-cap-is-read",
                      realizes='A1 "The question store"')
        self.question("q-0002.0006", "What follows a close?", parent="q-0002", owner="01-0040-after-close")
        self.question("q-0003", "What landscape does it evolve in?")
        self.write("docs/tickets/01-0010-questions-kept.md", path_ticket("Questions kept", "In progress", "q-0002.0001"))
        self.write("docs/tickets/01-0010.0010-a-question-branches.md",
                   path_ticket("A question branches", "In progress", "q-0002.0001.0001"))
        self.write("docs/tickets/01-0020-a-ticket-closes.md", path_ticket("A ticket closes", "Ready", "q-0002.0002"))
        self.write("docs/tickets/01-0030-the-cap-is-read.md", path_ticket("The cap is read", "Ready", "q-0002.0005"))
        self.write("docs/tickets/01-0040-after-close.md", path_ticket(
            "After close", "Planned", "q-0002.0006", depends="[A ticket closes](./01-0020-a-ticket-closes.md) (the close)"))
        self.write("docs/product.md", PATH_PRODUCT)
        self.write("docs/notes.md", '<straw-dog question="q-0002.0005">one</straw-dog> '
                   '<straw-dog question="q-0002.0005">two</straw-dog>\n')

    def said(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(list(argv), root=self.root, today=PATH_NOW.date(), now=PATH_NOW)
        return status, out.getvalue()

    def path(self) -> tuple[int, list[str]]:
        status, text = self.said("--path")
        return status, text.splitlines()

    def under(self, lines: list[str], heading: str) -> list[str]:
        """The lines under one of the path's headings, up to the next line at its depth or less."""
        start = next(index for index, line in enumerate(lines) if line.lstrip().startswith(heading))
        depth = len(lines[start]) - len(lines[start].lstrip())
        rest = lines[start + 1:]
        end = next((index for index, line in enumerate(rest) if len(line) - len(line.lstrip()) <= depth), len(rest))
        return [lines[start], *rest[:end]]

    def test_work_in_hand_is_the_tickets_in_progress_a_parent_counted_through_its_child(self) -> None:
        self.a_tree()

        status, lines = self.path()

        self.assertEqual(0, status)
        work = self.under(lines, "in work:")
        self.assertTrue(work[0].strip().startswith("in work: 1 —"), work[0])
        self.assertIn("sessions are not counted", work[0])
        self.assertEqual(["    A question branches — 01-0010.0010 → q-0002.0001.0001"], work[1:])

    def test_touched_lately_is_an_open_question_with_no_ticket_reached_within_the_week(self) -> None:
        self.a_tree()

        lately = self.under(self.path()[1], "touched lately, no ticket:")

        self.assertEqual("  touched lately, no ticket: 1", lately[0])
        self.assertEqual(["    Who is it for? — q-0001.0001 (struck 2, 2026-09-27)"], lately[1:])

    def test_a_ready_ticket_is_a_candidate_with_its_reasons_and_unread_where_none_is_held(self) -> None:
        self.a_tree()

        ready = self.under(self.path()[1], "ready")

        self.assertEqual(
            [
                "    A ticket closes — 01-0020 → q-0002.0002",
                "      serves unread · struck 0 · 0 straw dogs · unlocks After close",
                "    The cap is read — 01-0030 → q-0002.0005",
                "      serves A1 The question store, in progress, 3 open · struck 0 · 2 straw dogs · unlocks —",
            ],
            ready[1:],
        )

    def test_the_ready_candidates_stand_in_id_order_each_saying_the_open_work_of_its_answer(self) -> None:
        self.a_tree()
        self.question("q-0002.0007", "How is a rule installed?", parent="q-0002",
                      owner="01-0050-a-rule-installs", realizes='A2 "Rules installed"')
        self.write("docs/tickets/01-0050-a-rule-installs.md", path_ticket("A rule installs", "Ready", "q-0002.0007"))

        ready = self.under(self.path()[1], "ready")

        self.assertEqual("  ready, in id order, none ranked above another:", ready[0])
        candidates = [line.strip() for line in ready[1:] if not line.startswith("      ")]
        self.assertEqual(
            ["A ticket closes — 01-0020 → q-0002.0002",
             "The cap is read — 01-0030 → q-0002.0005",
             "A rule installs — 01-0050 → q-0002.0007"],
            candidates,
        )
        self.assertIn("serves A2 Rules installed, unread, 1 open", " ".join(ready))

    def test_the_most_struck_question_with_no_ticket_is_a_candidate_and_a_root_never_is(self) -> None:
        self.a_tree()

        struck = self.under(self.path()[1], "most struck, no ticket, past those touched lately:")

        self.assertEqual(
            ["    Does the path read? — q-0002.0004", "      serves unread · struck 3 · 0 straw dogs · unlocks —"],
            struck[1:],
        )

    def test_each_root_counts_its_open_questions_and_those_with_a_ticket_a_root_with_none_thin(self) -> None:
        self.a_tree()

        roots = self.under(self.path()[1], "roots:")

        self.assertEqual(
            [
                "    What is this project for? — q-0001: open 1, with a ticket 0, thin",
                "    How is it built? — q-0002: open 7, with a ticket 5",
                "    What landscape does it evolve in? — q-0003: open 0, with a ticket 0",
            ],
            roots[1:],
        )

    def test_a_tree_with_no_tickets_and_no_product_document_shows_what_exists(self) -> None:
        self.question("q-0001", "What is this project for?")
        self.question("q-0001.0001", "Who is it for?", parent="q-0001", struck=(4, 40))

        status, lines = self.path()

        self.assertEqual(0, status)
        self.assertTrue(self.under(lines, "in work:")[0].strip().startswith("in work: 0 —"))
        self.assertIn("      serves unread · struck 4 · 0 straw dogs · unlocks —", lines)
        self.assertIn("    What is this project for? — q-0001: open 1, with a ticket 0, thin", lines)

    def test_a_tree_with_no_store_has_no_path_and_passes(self) -> None:
        status, lines = self.path()

        self.assertEqual(0, status)
        self.assertEqual(["path: no question store here"], lines)

    def test_the_wake_carries_the_path_before_the_window(self) -> None:
        self.a_tree()

        _, text = self.said("--wake")

        self.assertIn("\npath:\n", text)
        self.assertIn("  in work: 1 —", text)
        self.assertLess(text.index("\npath:\n"), text.rindex("\nsession: "), "the path comes before the window")


class RungsInUse(Store):
    """A store that uses the rung part — some question carries one — has every open question carry
    its own (q-0037.0019, decision 2); one without is a finding. A store with no rung anywhere has no
    ladder and is asked nothing."""

    def unrunged(self) -> list[str]:
        return [note.finding for note in questions.check(self.root).findings if "rung" in note.finding]

    def test_a_store_with_no_rung_anywhere_is_asked_nothing(self) -> None:
        self.assertEqual([], self.unrunged())

    def test_once_one_question_carries_a_rung_an_open_one_without_is_a_finding(self) -> None:
        self.place("q-0012-one-with-a-rung", "One with a rung?", {"state": "open", "rung": "development: a feature"})

        found = self.unrunged()

        self.assertIn("q-0001.0001 is open and has no rung", found)
        self.assertNotIn("q-0012 is open and has no rung", found)
        self.assertEqual([], self.problems())

    def test_a_closed_one_is_not(self) -> None:
        self.place("q-0012-one-with-a-rung", "One with a rung?", {"state": "open", "rung": "development: a feature"})
        self.place("q-0013-a-closed-one", "A closed one?", {"state": "closed:decided"})

        self.assertNotIn("q-0013 is open and has no rung", self.unrunged())


class WhereItStands(Store):
    """A question a ticket answers carries its `Where it stands` (q-0037.0009.0017, decision 2): the
    top of the work an owner owns, read from the store's own parts, is named while it lacks one."""

    OWNER = "[01-0001](../tickets/01-0001-the-store.md)"

    def unstated(self) -> list[str]:
        return [
            note.finding
            for note in questions.check(self.root).findings
            if "Where it stands" in note.finding
        ]

    def own(self, stem: str, question: str, body: str = "", **parts: str) -> None:
        name = self.place(stem, question, {**parts, "owner": self.OWNER})
        if body:
            self.write(name, (self.root / name).read_text(encoding="utf-8") + "\n" + body)

    def test_an_owned_open_question_without_one_is_a_finding(self) -> None:
        self.own("q-0001-which-store-holds-the-questions", "Which store holds the questions?", state="open")

        found = self.unstated()

        self.assertEqual(["q-0001 is answered by 01-0001 and has no Where it stands"], found)
        self.assertEqual([], self.problems())

    def test_one_that_carries_it_is_not(self) -> None:
        self.own(
            "q-0001-which-store-holds-the-questions",
            "Which store holds the questions?",
            "## Where it stands\n\nOne flat folder.\n",
            state="open",
        )

        self.assertEqual([], self.unstated())

    def test_a_child_its_owner_also_owns_is_held_by_the_parent_picture(self) -> None:
        self.own("q-0001-which-store-holds-the-questions", "Which store holds the questions?", state="open")
        self.own("q-0001.0001-what-an-entry-holds", "What an entry holds?", **{"part of": "q-0001", "state": "open"})

        found = self.unstated()

        self.assertEqual(1, len(found), found)
        self.assertTrue(found[0].startswith("q-0001 "), found)

    def test_a_closed_owned_question_stands_on_its_answer(self) -> None:
        self.own(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            **{"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
        )

        self.assertEqual([], self.unstated())

    def test_it_leaves_the_exit_status_at_zero(self) -> None:
        self.own("q-0001-which-store-holds-the-questions", "Which store holds the questions?", state="open")

        status, report = self.run_check()

        self.assertEqual(0, status)
        self.assertTrue(report["findings"])


class TheMaintainer(Store):
    def test_leaves_the_tree_byte_identical_even_with_findings_and_diagnostics(self) -> None:
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0001.0001\n")
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

    Its children keep the flat ids every store held before an id said where it sits (the user,
    2026-10-03): they still read, and a call that opens or renames under them gives nested ones.
    """

    def seed(self) -> None:
        self.place("q-0001-which-store-holds-the-questions", "Which store holds the questions?", {"state": "open"})
        self.write("docs/record.md", "# A record\n")
        decided = "[the record](../record.md) — the user, 2026-09-29"
        self.question("q-0002-what-an-entry-holds", "What an entry holds?", "q-0001", lean="eight parts")
        self.question("q-0003-how-is-a-subtree-archived", "How is a subtree archived?", "q-0001")
        self.question("q-0004-which-parts-are-optional", "Which parts are optional?", "q-0002")
        self.question("q-0005-is-the-id-a-path", "Is the id a path?", "q-0002", "closed:decided", decided)
        self.question(
            "q-0006-is-the-directory-partitioned-by-root",
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
        self.question("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?")
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
            "s-alpha running 2026-09-29T11:30Z q-0004 q-0002,q-0001\n"
            "s-beta running 2026-09-29T11:00Z q-0010\n"
            "s-gamma ended 2026-09-28 q-0003\n",
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
            status = questions.main(list(argv), root=self.root, today=TODAY, now=NOW)
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

    def test_names_the_recent_positions_and_the_other_running_sessions(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("recently attached: q-0002, q-0001", text)
        others = self.section(text, "other running sessions:")
        self.assertIn("s-beta at q-0010 How do sessions reach each other? (last wrote 2026-09-29T11:00Z)", others)
        self.assertNotIn("s-gamma", others)
        self.assertNotIn("s-alpha", others)
        self.assertNotIn("next free id", text, "the script draws ids, so the agent is not handed one")


class TheCounters(Rendered):
    """The window's last line: open tickets, open questions and straw dogs, each with what came and
    went since the session's previous window, matched by name."""

    TICKET = "docs/tickets/01-0010-a-first-ticket.md"
    DOGS = "docs/note.md"

    def counted(self) -> tuple[str, dict[str, tuple[int, int, int]]]:
        """A window drawn for s-alpha, and its counters as `{glyph: (total, came, went)}`."""
        _, text = self.said("--window", "--session", "s-alpha")
        line = [said for said in text.splitlines() if said.startswith("🎫")][0]
        counts = {}
        for part in line.split(" · "):
            said = re.fullmatch(r"(\S+) (\d+)(?: \((?:\+(\d+))?(?:-(\d+))?\))?", part)
            self.assertIsNotNone(said, f"a counter out of form: {part!r}")
            self.assertNotIn("()", part)
            glyph, total, came, went = said.groups()
            counts[glyph] = (int(total), int(came or 0), int(went or 0))
        return text, counts

    def dogs(self, *questions_bound: str) -> None:
        self.write(self.DOGS, "".join(f'<straw-dog question="{bound}">a claim</straw-dog>\n' for bound in questions_bound))

    def test_the_first_window_gives_the_totals_alone(self) -> None:
        self.write(self.TICKET, "# A first ticket\n")
        self.dogs("q-0001")

        text, counts = self.counted()

        self.assertIn("🎫 1 · ❓ 6 · 🐕 1\n", text + "\n", "nothing to compare, so nothing said of it")
        self.assertEqual({"🎫": (1, 0, 0), "❓": (6, 0, 0), "🐕": (1, 0, 0)}, counts)

    def test_a_move_is_written_in_brackets_and_none_is_written_as_nothing(self) -> None:
        self.write(self.TICKET, "# A first ticket\n")
        self.counted()
        (self.root / self.TICKET).unlink()
        self.write("docs/tickets/01-0020-a-second-ticket.md", "# A second ticket\n")
        self.write("docs/tickets/01-0030-a-third-ticket.md", "# A third ticket\n")

        text, _ = self.counted()

        self.assertIn("🎫 2 (+2-1) · ❓ 6 · 🐕 0\n", text + "\n")

    def test_a_ticket_minted_a_question_opened_and_a_straw_dog_wrapped_each_come(self) -> None:
        self.counted()
        self.write(self.TICKET, "# A first ticket\n")
        self.question("q-0014-who-counts", "Who counts?", "q-0010")
        self.dogs("q-0010")

        _, counts = self.counted()

        self.assertEqual({"🎫": (1, 1, 0), "❓": (7, 1, 0), "🐕": (1, 1, 0)}, counts)

    def test_a_ticket_closed_a_question_decided_and_a_straw_dog_removed_each_go(self) -> None:
        self.write(self.TICKET, "# A first ticket\n")
        self.dogs("q-0010")
        self.counted()
        (self.root / self.TICKET).unlink()
        self.question("q-0007-who-moves-a-subtree", "Who moves a subtree?", "q-0003", "closed:decided", "[the record](../record.md) — the user, 2026-09-29")
        self.dogs()

        _, counts = self.counted()

        self.assertEqual({"🎫": (0, 0, 1), "❓": (5, 0, 1), "🐕": (0, 0, 1)}, counts)

    def test_one_going_as_another_comes_reads_as_both(self) -> None:
        self.write(self.TICKET, "# A first ticket\n")
        self.dogs("q-0001")
        self.counted()
        (self.root / self.TICKET).unlink()
        self.write("docs/tickets/01-0020-a-second-ticket.md", "# A second ticket\n")
        self.dogs("q-0010")

        _, counts = self.counted()

        self.assertEqual((1, 1, 1), counts["🎫"])
        self.assertEqual((1, 1, 1), counts["🐕"])

    def test_a_straw_dog_moved_while_no_entry_did_shows_on_the_unchanged_line(self) -> None:
        self.counted()
        self.dogs("q-0001")

        text, counts = self.counted()

        self.assertTrue(text.startswith("window unchanged"), text)
        self.assertEqual((1, 1, 0), counts["🐕"])

    def test_a_readme_and_an_archived_ticket_are_not_counted(self) -> None:
        self.write("docs/tickets/README.md", "# The project's own notes\n")
        self.write("docs/tickets/done/01-0005-an-old-ticket.md", "# An old ticket\n")

        _, counts = self.counted()

        self.assertEqual(0, counts["🎫"][0])

    def test_a_window_after_a_compaction_still_compares(self) -> None:
        self.counted()
        sessions.forget_window(self.root, "s-alpha")
        self.write(self.TICKET, "# A first ticket\n")

        _, counts = self.counted()

        self.assertEqual((1, 1, 0), counts["🎫"])

    def test_a_record_whose_size_and_time_did_not_move_is_not_read_again(self) -> None:
        self.dogs("q-0001")
        self.counted()
        path = self.root / self.DOGS
        moment = path.stat()
        self.dogs("q-0003")
        os.utime(path, ns=(moment.st_atime_ns, moment.st_mtime_ns))

        _, counts = self.counted()

        self.assertEqual((1, 0, 0), counts["🐕"], "the cache answered for the unmoved record")


class TheCount(Rendered):
    """A struck question carries its count on its line, and the wake reads the most struck first."""

    def strike(self, stem: str, question: str, count: int, parent: str | None = None, state: str = "open",
               folder: str = STORE) -> None:
        parts = {"part of": parent, "state": state, "answer": "gone" if state != "open" else None}
        parts = {name: value for name, value in parts.items() if value is not None}
        self.place(stem, question, parts | {"struck": f"{count}, last 2026-09-29T12:00Z"}, folder)

    def test_a_struck_line_shows_its_count_and_an_unstruck_one_none(self) -> None:
        self.strike("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?", 2)

        _, text = self.said("--window", "--session", "s-alpha", "--full")

        roots = self.section(text, "other roots:")
        self.assertIn("q-0010 [open] How do sessions reach each other? (struck 2)", roots)
        self.assertNotIn("struck", roots.split("q-0011")[1])

    def test_the_roots_open_questions_show_their_count(self) -> None:
        self.strike("q-0007-who-moves-a-subtree", "Who moves a subtree?", 1, parent="q-0003")

        _, text = self.said("--window", "--session", "s-alpha", "--full")

        self.assertIn("Who moves a subtree? (struck 1)", self.section(text, "open questions under this root"))

    def test_the_wake_reads_the_most_struck_open_questions_first(self) -> None:
        self.strike("q-0007-who-moves-a-subtree", "Who moves a subtree?", 1, parent="q-0003")
        self.strike("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other?", 3)
        self.strike("q-0011-is-height-depth", "Is height depth?", 9, state="closed:moot")
        self.strike("q-0012-an-archived-one", "An archived one?", 9, state="closed:moot", folder=f"{STORE}/done")

        _, text = self.said("--wake", "--session", "s-alpha")

        ranked = self.section(text, "most struck, open:").splitlines()[1:]
        self.assertEqual(["q-0010", "q-0007"], [line.split()[0] for line in ranked])
        self.assertTrue(text.index("most struck, open:") < text.index("sessions:"), "it opens the read")


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
        self.place("q-0010-how-do-sessions-reach-each-other", "How do sessions reach each other → remotely?", {"state": "open"})
        raw = io.BytesIO()
        console = io.TextIOWrapper(raw, encoding="cp1252")

        with contextlib.redirect_stdout(console):
            status = questions.main(["--tree", "q-0010"], root=self.root, today=TODAY)
            console.flush()

        self.assertEqual(0, status)
        self.assertIn("each other → remotely?", raw.getvalue().decode("utf-8"))


class Declared(Rendered):
    """The writer over the fixed store, as s-alpha at q-0004 calls it: written whole, or refused
    with its reason and nothing written."""

    def call(self, *argv: str, session: str | None = "s-alpha", now: datetime = NOW) -> tuple[int, str]:
        said, complained = io.StringIO(), io.StringIO()
        tagged = [*argv, "--session", session] if session else list(argv)
        with contextlib.redirect_stdout(said), contextlib.redirect_stderr(complained):
            status = questions.main(tagged, root=self.root, today=TODAY, now=now)
        return status, said.getvalue() + complained.getvalue()

    def called(self, *argv: str) -> str:
        status, said = self.call(*argv)
        self.assertEqual(0, status, said)
        return said

    def assertRefused(self, reason: str, *argv: str, session: str | None = "s-alpha") -> None:
        untouched = self.snapshot()

        status, said = self.call(*argv, session=session)

        self.assertEqual(2, status, said)
        self.assertIn(reason, said)
        self.assertEqual(untouched, self.snapshot())

    def entry_text(self, stem: str) -> str:
        return self.read(f"{STORE}/{stem}.md")

    def part(self, stem: str, name: str) -> str | None:
        found = [line.split("** ", 1)[1] for line in self.entry_text(stem).splitlines() if line.startswith(f"- **{name}** ")]
        return found[0] if found else None

    def own_line(self) -> str:
        return next(line for line in session_lines(self.root).splitlines() if line.startswith("s-alpha "))


class TheCalls(Declared):
    """Each event of a turn is its own call."""

    def test_at_places_the_session(self) -> None:
        self.called("at", "q-0010")

        self.assertEqual("s-alpha running 2026-09-29T12:00Z q-0010 q-0004,q-0002,q-0001", self.own_line())

    def test_at_prints_the_question_it_landed_on_and_the_one_it_left(self) -> None:
        said = self.called("at", "q-0010")

        self.assertIn(
            "at q-0010 How do sessions reach each other? (from q-0004 Which parts are optional?)", said
        )

    def test_at_that_stays_prints_the_question_alone(self) -> None:
        said = self.called("at", "q-0004")

        self.assertIn("at q-0004 Which parts are optional?", said)
        self.assertNotIn("(from", said)

    def test_open_takes_the_next_free_id_under_its_parent_prints_it_and_leaves_the_session_where_it_stands(self) -> None:
        said = self.called("open", "Is the owner optional?", "--under", "q-0004")

        self.assertIn("opened q-0004.0001", said)
        self.assertEqual(
            "# q-0004.0001 Is the owner optional?\n\n- **record of** what it intends to become\n"
            "- **part of** q-0004\n- **state** open\n- **struck** 0, last 2026-09-29T12:00Z\n",
            self.read(f"{STORE}/q-0004.0001-is-the-owner-optional.md"),
        )
        self.assertEqual("s-alpha running 2026-09-29T11:30Z q-0004 q-0002,q-0001", self.own_line())

    def test_open_takes_the_position_after_every_child_live_or_in_done(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0004")
        self.question("q-0004.0003-an-archived-child", "An archived child?", "q-0004", "closed:moot", "gone", folder=f"{STORE}/done")

        said = self.called("open", "Is the owner required?", "--under", "q-0004")

        self.assertIn("opened q-0004.0004", said)

    def test_open_a_root_takes_the_position_after_every_root_level_id(self) -> None:
        said = self.called("open", "Is there a third root?")

        self.assertIn("opened q-0014", said)
        self.assertIsNone(self.part("q-0014-is-there-a-third-root", "part of"))

    def test_open_where_no_four_digit_position_is_left_is_refused(self) -> None:
        self.question("q-0004.9999-the-last-child", "The last child?", "q-0004")

        self.assertRefused("no free position under q-0004", "open", "One more?", "--under", "q-0004")

    def test_open_between_two_questions_reparents_the_lower(self) -> None:
        self.called("open", "What must an entry hold?", "--between", "q-0002", "q-0004")

        self.assertEqual("q-0002", self.part("q-0002.0001-what-must-an-entry-hold", "part of"))
        self.assertEqual("q-0002.0001", self.part("q-0002.0001.0001-which-parts-are-optional", "part of"))

    def test_move_under_another_and_to_root(self) -> None:
        self.called("move", "q-0007", "--under", "q-0002")
        self.assertEqual("q-0002", self.part("q-0002.0001-who-moves-a-subtree", "part of"))

        self.called("move", "q-0002.0001", "--to-root")
        self.assertIsNone(self.part("q-0013-who-moves-a-subtree", "part of"), "q-0013 went with the first move, freed")

    def test_depend_on_another(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")

        self.assertEqual("q-0010", self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_removes_one_of_two(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")
        self.called("depend", "q-0004", "--on", "q-0003")

        self.called("undepend", "q-0004", "--on", "q-0010")

        self.assertEqual("q-0003", self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_the_last_removes_the_part(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0010")

        self.called("undepend", "q-0004", "--on", "q-0010")

        self.assertIsNone(self.part("q-0004-which-parts-are-optional", "depends on"))

    def test_undepend_on_one_not_awaited_is_refused(self) -> None:
        self.assertRefused("does not depend on q-0010", "undepend", "q-0004", "--on", "q-0010")

    def test_close_with_its_kind_and_pointer(self) -> None:
        self.called("close", "q-0007", "decided", "[the record](../record.md) — the user, 2026-09-29")

        self.assertEqual("closed:decided", self.part("q-0007-who-moves-a-subtree", "state"))
        self.assertEqual("[the record](../record.md) — the user, 2026-09-29", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_close_turns_the_mark_to_what_happened(self) -> None:
        self.assertEqual(OPEN_KIND, self.part("q-0007-who-moves-a-subtree", "record of"))

        self.called("close", "q-0007", "decided", "[the record](../record.md) — the user, 2026-09-29")

        self.assertEqual(CLOSED_KIND, self.part("q-0007-who-moves-a-subtree", "record of"))

    def test_any_rewrite_writes_the_mark_an_entry_carried_none_of_first(self) -> None:
        self.write(
            f"{STORE}/q-0007-who-moves-a-subtree.md",
            entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open"}, marked=False),
        )

        self.called("lean", "q-0007", "the mover")

        self.assertTrue(self.entry_text("q-0007-who-moves-a-subtree").splitlines()[2].startswith("- **record of** "))
        self.assertEqual(OPEN_KIND, self.part("q-0007-who-moves-a-subtree", "record of"))

    def test_suspect_and_clear(self) -> None:
        self.called("suspect", "q-0007")
        self.assertEqual("open, suspect", self.part("q-0007-who-moves-a-subtree", "state"))

        self.called("clear", "q-0007")
        self.assertEqual("open", self.part("q-0007-who-moves-a-subtree", "state"))

    def test_lean_takes_any_text_a_semicolon_included(self) -> None:
        self.called("lean", "q-0007", "the mover; never by hand")

        self.assertEqual("the mover; never by hand", self.part("q-0007-who-moves-a-subtree", "lean"))

    def test_assign_links_the_owner(self) -> None:
        self.called("assign", "q-0007", "docs/record.md")

        self.assertEqual("[record](../record.md)", self.part("q-0007-who-moves-a-subtree", "owner"))

    def test_a_call_without_its_session_is_refused_with_its_usage(self) -> None:
        self.assertRefused("--session", "at", "q-0010", session=None)

    def test_a_malformed_id_is_refused(self) -> None:
        self.assertRefused("not a question id", "at", "q-12")

    def test_a_kind_outside_the_vocabulary_is_refused(self) -> None:
        self.assertRefused("invalid choice", "close", "q-0007", "done")

    def test_at_a_closed_question_is_refused(self) -> None:
        self.assertRefused("a position is an open question", "at", "q-0005")

    def test_open_raced_by_another_session_takes_the_id_after_theirs(self) -> None:
        theirs = entry("q-0004.0001", "Their question?", {"part of": "q-0004", "state": "open"})

        written = questions.declare(
            self.root,
            "s-alpha",
            [questions.Clause("opens", other="q-0004", text="My question?")],
            TODAY,
            between=lambda: self.write(f"{STORE}/q-0004.0001-their-question.md", theirs),
        )

        self.assertEqual(["q-0004.0002"], written.opened)
        self.assertEqual(theirs, self.read(f"{STORE}/q-0004.0001-their-question.md"))
        self.assertTrue((self.root / STORE / "q-0004.0002-my-question.md").is_file())


class Renaming(Declared):
    """A re-parent renames the subtree that moves, so every id keeps saying where its question
    sits (the user, 2026-10-03): files, links, relations, session lines and bare ids follow."""

    def stems(self, folder: str = STORE) -> set[str]:
        return {path.stem for path in (self.root / folder).glob("q-*.md")}

    def test_a_move_renames_its_subtree_keeping_nested_positions_and_seating_flat_ones_after_them(self) -> None:
        self.called("open", "Who runs the mover?", "--under", "q-0007")
        self.question("q-0007.0002-is-it-archived", "Is it archived?", "q-0007", "closed:moot", "gone", folder=f"{STORE}/done")

        said = self.called("move", "q-0007", "--under", "q-0002")

        self.assertIn("renamed q-0007 → q-0002.0001", said)
        live, archived = self.stems(), self.stems(f"{STORE}/done")
        self.assertLessEqual(
            {
                "q-0002.0001-who-moves-a-subtree",
                "q-0002.0001.0001-who-runs-the-mover",
                "q-0002.0001.0003-does-the-mover-repair-links",
            },
            live,
        )
        self.assertIn("q-0002.0001.0002-is-it-archived", archived)
        self.assertEqual([], [stem for stem in live | archived if stem.startswith("q-0007") or stem.startswith("q-0013")])
        self.assertEqual("q-0002.0001", self.part("q-0002.0001.0003-does-the-mover-repair-links", "part of"))

    def test_links_and_bare_ids_across_the_docs_follow_the_rename_and_nothing_longer_is_touched(self) -> None:
        self.called("open", "Who runs the mover?", "--under", "q-0007")
        self.write(
            "docs/notes.md",
            "See [the subtree](questions/q-0007-who-moves-a-subtree.md), q-0007 and `q-0007.0001`,\n"
            "not q-00070, faq-0007 or q-0070.\n",
        )

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(
            "See [the subtree](questions/q-0002.0001-who-moves-a-subtree.md), q-0002.0001 and `q-0002.0001.0001`,\n"
            "not q-00070, faq-0007 or q-0070.\n",
            self.read("docs/notes.md"),
        )

    def test_an_id_inside_a_fenced_block_is_an_example_and_is_left_as_written(self) -> None:
        sample = "Before.\n\n```md\n# q-0041 A sample\n\n- **part of** q-0007\n```\n\nAfter q-0007.\n"
        self.write("docs/sample.md", sample)

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(sample.replace("After q-0007.", "After q-0002.0001."), self.read("docs/sample.md"))

    def test_relations_and_every_sessions_line_name_the_new_ids(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0007")
        self.write(
            SESSIONS,
            session_lines(self.root).replace("s-beta running 2026-09-29T11:00Z q-0010", "s-beta running 2026-09-29T11:00Z q-0007 q-0013,q-0010"),
        )

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual("q-0002.0001", self.part("q-0004-which-parts-are-optional", "depends on"))
        self.assertEqual(
            "s-gamma ended 2026-09-28 q-0003\n"
            "s-beta running 2026-09-29T11:00Z q-0002.0001 q-0002.0001.0001,q-0010\n"
            "s-alpha running 2026-09-29T11:30Z q-0004 q-0002,q-0001\n",
            session_lines(self.root),
        )

    def test_between_renames_the_lower_subtree_under_the_new_question(self) -> None:
        self.called("open", "What must an entry hold?", "--between", "q-0002", "q-0004")

        self.assertLessEqual(
            {
                "q-0002.0001-what-must-an-entry-hold",
                "q-0002.0001.0001-which-parts-are-optional",
                "q-0002.0001.0001.0001-is-the-lean-optional",
            },
            self.stems(),
        )
        self.assertEqual("s-alpha running 2026-09-29T11:30Z q-0002.0001.0001 q-0002,q-0001", self.own_line())

    def test_a_move_to_the_parent_a_fitting_question_already_has_writes_nothing(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0002")
        untouched = self.snapshot()

        self.called("move", "q-0002.0001", "--under", "q-0002")

        self.assertEqual(untouched, self.snapshot())

    def test_a_move_to_its_own_parent_seats_a_flat_id(self) -> None:
        self.called("move", "q-0004", "--under", "q-0002")

        self.assertIn("q-0002.0001-which-parts-are-optional", self.stems())
        self.assertIn("q-0002.0001.0001-is-the-lean-optional", self.stems())

    def test_a_rename_the_mover_refuses_writes_nothing(self) -> None:
        (self.root / "docs" / "unreadable.md").write_bytes(b"\xff\xfe not utf-8\n")

        self.assertRefused("not UTF-8", "move", "q-0007", "--under", "q-0002")

    def test_a_later_clause_naming_an_id_the_rename_changed_refuses_the_declaration(self) -> None:
        untouched = self.snapshot()

        with self.assertRaises(questions.Refused) as refused:
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("moves", "q-0007", other="q-0002"), questions.Clause("leans", "q-0007", text="late")],
                TODAY,
            )

        self.assertIn("no entry holds q-0007", str(refused.exception))
        self.assertEqual(untouched, self.snapshot())

    def test_a_straw_dogs_binding_in_core_and_in_code_follows_and_an_example_keeps_its_id(self) -> None:
        self.called("open", "Who runs the mover?", "--under", "q-0007")
        skill = (
            '<straw-dog question="q-0007">Held for now.</straw-dog>\n\n'
            'Write `<straw-dog question="q-0007">` around it; q-0007 is an example here.\n\n'
            '```md\n<straw-dog question="q-0007">Sample.</straw-dog>\n```\n'
        )
        self.write(".agents/skills/keeper/SKILL.md", skill)
        self.write("AGENTS.md", '<straw-dog question="q-0007.0001">Rule.</straw-dog>\n')
        self.write(".agents/scripts/keeper.py", '# TODO q-0007: the move.\n# TODO q-00070: no id of ours.\nNAME = "q-0007"\n')

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(
            skill.replace('question="q-0007">Held', 'question="q-0002.0001">Held', 1),
            self.read(".agents/skills/keeper/SKILL.md"),
        )
        self.assertEqual('<straw-dog question="q-0002.0001.0001">Rule.</straw-dog>\n', self.read("AGENTS.md"))
        self.assertEqual(
            '# TODO q-0002.0001: the move.\n# TODO q-00070: no id of ours.\nNAME = "q-0007"\n',
            self.read(".agents/scripts/keeper.py"),
        )


class Rewording(Declared):
    """A question's words follow the discussion and its id stays (the user, 2026-10-05): the same
    question means the same answers, never the same wording."""

    def test_the_title_and_the_file_take_the_new_words_and_everything_else_is_kept(self) -> None:
        self.called("lean", "q-0007", "the closer")
        before = self.entry_text("q-0007-who-moves-a-subtree")

        said = self.called("reword", "q-0007", "Who carries a finished subtree away?")

        self.assertIn("reworded q-0007 Who carries a finished subtree away?", said)
        self.assertFalse((self.root / STORE / "q-0007-who-moves-a-subtree.md").exists())
        self.assertEqual(
            before.replace("# q-0007 Who moves a subtree?", "# q-0007 Who carries a finished subtree away?"),
            self.entry_text("q-0007-who-carries-a-finished-subtree-away"),
        )
        self.assertEqual("q-0007", self.part("q-0013-does-the-mover-repair-links", "part of"))

    def test_every_link_to_the_entry_follows_and_bare_ids_and_sessions_are_left_as_they_were(self) -> None:
        self.write("docs/notes.md", "See [q-0007](questions/q-0007-who-moves-a-subtree.md) and q-0007.\n")
        sessions = session_lines(self.root)

        self.called("reword", "q-0007", "Who carries a finished subtree away?")

        self.assertEqual(
            "See [q-0007](questions/q-0007-who-carries-a-finished-subtree-away.md) and q-0007.\n",
            self.read("docs/notes.md"),
        )
        self.assertEqual(sessions, session_lines(self.root))
        self.assertEqual([], [told for told in self.run_check()[1]["diagnostics"] if "slug" in told["problem"]])

    def test_words_that_leave_the_file_name_as_it_is_rewrite_the_title_alone(self) -> None:
        self.called("reword", "q-0007", "Who moves a subtree!")

        self.assertTrue(self.entry_text("q-0007-who-moves-a-subtree").startswith("# q-0007 Who moves a subtree!\n"))

    def test_the_session_standing_on_it_stays_there(self) -> None:
        self.called("reword", "q-0004", "Which parts may an entry leave out?")

        self.assertIn(" q-0004 ", self.own_line())
        self.assertIn("Which parts may an entry leave out?", self.said("--window", "--session", "s-alpha", "--full")[1])

    def test_a_closed_question_keeps_the_words_it_was_answered_under(self) -> None:
        self.assertRefused("is closed", "reword", "q-0005", "Is the id a route?")

    def test_the_same_words_and_no_words_are_refused(self) -> None:
        self.assertRefused("already reads", "reword", "q-0007", "Who moves a subtree?")
        self.assertRefused("no words", "reword", "q-0007", "  ")


class Dueness(Store):
    """A straw dog is due when the answer its text waited on has landed, or its question no longer
    stands; a merge or a supersession hands it to the successor instead (the user, 2026-10-03 and
    2026-10-04)."""

    WORK = "[01-0002](../tickets/01-0002-sweep.md)"

    def seed(self) -> None:
        super().seed()
        self.write("docs/tickets/01-0002-sweep.md", "# Sweep\n\n## Decisions\n\n1. Swept.\n")
        self.write("docs/architecture.md", "# Architecture\n\n## Sweeping\n\nSwept.\n")

    def read_entry(self, parts: dict[str, str]) -> questions.Entry:
        name = self.place("q-0002-is-it-swept", "Is it swept?", parts)
        return questions.read_store(self.root).index["q-0002"] if name else None

    def is_due(self, parts: dict[str, str]) -> bool:
        return questions.due(self.root, self.read_entry(parts))

    def test_a_decision_still_in_the_work_that_owns_it_is_not_due(self) -> None:
        self.assertFalse(
            self.is_due({"state": "closed:decided", "owner": self.WORK, "answer": "[decision 1](../tickets/01-0002-sweep.md#decisions)"})
        )

    def test_a_decision_landed_in_its_home_is_due(self) -> None:
        self.assertTrue(
            self.is_due({"state": "closed:decided", "owner": self.WORK, "answer": "[sweeping](../architecture.md#sweeping)"})
        )

    def test_an_answer_still_citing_the_work_beside_its_home_is_not_due(self) -> None:
        answer = "[sweeping](../architecture.md#sweeping), [decision 1](../tickets/01-0002-sweep.md#decisions)"
        self.assertFalse(self.is_due({"state": "closed:decided", "owner": self.WORK, "answer": answer}))

    def test_a_decision_citing_a_ticket_or_an_rfc_is_not_due_owner_or_not(self) -> None:
        self.write("docs/rfc/01-0002-sweep.md", "# Sweep — implementation plan\n")
        for answer in ("[decision 1](../tickets/01-0002-sweep.md#decisions)", "[the plan](../rfc/01-0002-sweep.md)"):
            with self.subTest(answer=answer):
                self.assertFalse(self.is_due({"state": "closed:decided", "answer": answer}))

    def test_a_decision_waiting_in_a_questions_list_is_not_due_until_it_is_repointed_home(self) -> None:
        self.write(f"{STORE}/q-0001-which-store-holds-the-questions.md", self.read(f"{STORE}/q-0001-which-store-holds-the-questions.md") + "\n## Decisions\n\n- Swept.\n")
        waiting = "[the list](q-0001-which-store-holds-the-questions.md#decisions) — the user, 2026-10-11"
        self.assertFalse(self.is_due({"state": "closed:decided", "answer": waiting}))

        self.assertTrue(self.is_due({"state": "closed:decided", "answer": "[sweeping](../architecture.md#sweeping)"}))

    def test_an_archived_answer_citing_a_questions_list_is_not_due(self) -> None:
        self.place(
            "q-0003-was-it-swept",
            "Was it swept?",
            {"state": "closed:decided", "answer": "[the list](../q-0001-which-store-holds-the-questions.md)"},
            folder=f"{STORE}/done",
        )
        self.assertFalse(questions.due(self.root, questions.read_store(self.root).index["q-0003"]))

    def test_an_archived_entry_reads_its_links_from_where_it_now_stands(self) -> None:
        self.place(
            "q-0003-was-it-swept",
            "Was it swept?",
            {"state": "closed:decided", "owner": "[01-0002](../../tickets/01-0002-sweep.md)", "answer": "[sweeping](../../architecture.md#sweeping)"},
            folder=f"{STORE}/done",
        )
        self.assertTrue(questions.due(self.root, questions.read_store(self.root).index["q-0003"]))

    def test_a_question_no_longer_standing_is_due(self) -> None:
        for kind in ("moot", "pruned"):
            with self.subTest(kind=kind):
                self.assertTrue(self.is_due({"state": f"closed:{kind}", "owner": self.WORK, "answer": "overtaken"}))

    def test_an_open_suspect_deferred_merged_or_superseded_question_is_never_due(self) -> None:
        for state, answer in (
            ("open", None),
            ("closed:decided, suspect", "[sweeping](../architecture.md#sweeping)"),
            ("closed:deferred", "until it rains, meanwhile sweep"),
            ("closed:merged", "q-0001"),
            ("closed:superseded", "q-0001"),
        ):
            with self.subTest(state=state):
                parts = {"state": state} | ({"answer": answer} if answer else {})
                self.assertFalse(self.is_due(parts))

    def test_a_supersession_hands_its_straw_dogs_to_the_end_of_the_chain(self) -> None:
        self.place("q-0002-is-it-swept", "Is it swept?", {"state": "closed:superseded", "answer": "q-0003"})
        self.place("q-0003-is-it-swept-clean", "Is it swept clean?", {"state": "closed:merged", "answer": "q-0004"})
        self.place("q-0004-is-the-floor-clean", "Is the floor clean?", {"state": "open"})
        index = questions.read_store(self.root).index

        self.assertEqual("q-0004", questions.successor(index, index["q-0002"]).identity)
        self.assertIsNone(questions.successor(index, index["q-0004"]))


class TheBody(Declared):
    """An entry holds its own argument after its parts, written by hand and kept by every call as
    it found it (the user, 2026-10-03)."""

    BODY = "The argument, with `code` and\n\n- **lean** a line shaped like a part.\n"

    def argue(self, stem: str, body: str = BODY) -> None:
        self.write(f"{STORE}/{stem}.md", self.entry_text(stem) + "\n" + body)

    def body_of(self, stem: str) -> str:
        return self.entry_text(stem).split("\n\n", 2)[2]

    def test_survives_every_call_that_rewrites_the_entry(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")

        for call in (
            ("lean", "q-0007", "a lean"),
            ("suspect", "q-0007"),
            ("clear", "q-0007"),
            ("assign", "q-0007", "docs/record.md"),
            ("at", "q-0007"),
            ("close", "q-0007", "moot", "the mover does it"),
        ):
            self.called(*call)
            self.assertEqual(self.BODY, self.body_of("q-0007-who-moves-a-subtree"), call)

    def test_survives_a_strike(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")
        self.call("at", "q-0007")

        self.call("at", "q-0007", now=NOW + timedelta(hours=13))

        self.assertIn("- **struck** 1,", self.entry_text("q-0007-who-moves-a-subtree"))
        self.assertEqual(self.BODY, self.body_of("q-0007-who-moves-a-subtree"))

    def test_survives_a_rename_its_renamed_ids_rewritten_outside_fences(self) -> None:
        self.argue("q-0007-who-moves-a-subtree", "Argued against q-0013.\n\n```\nq-0013 as a sample\n```\n")

        self.called("move", "q-0007", "--under", "q-0002")

        self.assertEqual(
            "Argued against q-0002.0001.0001.\n\n```\nq-0013 as a sample\n```\n",
            self.body_of("q-0002.0001-who-moves-a-subtree"),
        )

    def test_a_line_shaped_like_a_part_in_the_body_is_not_one(self) -> None:
        before = self.problems()
        self.argue("q-0010-how-do-sessions-reach-each-other")

        read = questions.read_store(self.root).index["q-0010"]

        self.assertNotIn("lean", read.parts)
        self.assertEqual(before, self.problems())

    def test_a_line_glued_to_the_parts_is_still_reported(self) -> None:
        self.write(
            f"{STORE}/q-0010-how-do-sessions-reach-each-other.md",
            self.entry_text("q-0010-how-do-sessions-reach-each-other") + "glued to the parts\n",
        )

        self.assertTrue(any("not one of its parts" in problem for problem in self.problems()), self.problems())

    def test_a_hand_edit_to_the_body_meanwhile_refuses_the_call_and_keeps_the_edit(self) -> None:
        self.argue("q-0007-who-moves-a-subtree")
        edited = self.entry_text("q-0007-who-moves-a-subtree") + "One more line.\n"

        with self.assertRaises(questions.Refused) as refused:
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("leans", "q-0007", text="mine")],
                TODAY,
                between=lambda: self.write(f"{STORE}/q-0007-who-moves-a-subtree.md", edited),
            )

        self.assertIn("changed since this call read it", str(refused.exception))
        self.assertEqual(edited, self.entry_text("q-0007-who-moves-a-subtree"))


class TheDecisionsList(Declared):
    """A decision with nowhere to land yet waits as an item of the body's `## Decisions` list, and
    a close is refused while one has no home after its `→` (the user, 2026-10-11)."""

    STEM = "q-0007-who-moves-a-subtree"
    HOME = "→ [the record](../record.md)"

    def argue(self, body: str, stem: str = STEM) -> None:
        self.write(f"{STORE}/{stem}.md", self.entry_text(stem) + "\n" + body)

    def test_a_close_is_refused_naming_a_bulleted_decision_with_no_home(self) -> None:
        self.argue("## Decisions\n\n- Sweep by hand — the user, 2026-10-11\n")

        self.assertRefused('"Sweep by hand', "close", "q-0007", "moot", "overtaken")

    def test_a_close_is_refused_naming_a_numbered_decision_with_no_home(self) -> None:
        self.argue(f"## Decisions\n\n1. **Keep the list** {self.HOME}\n2. **Sweep by hand** *(the user)*:\n   as before.\n")

        self.assertRefused('"Sweep by hand', "close", "q-0007", "moot", "overtaken")

    def test_a_refusal_says_where_the_decision_can_go(self) -> None:
        self.argue("## Decisions\n\n- Sweep by hand\n")

        self.assertRefused("land it, or move it to the nearest open question above", "close", "q-0007", "moot", "overtaken")
        self.assertRefused("or to q-0010", "close", "q-0007", "merged", "q-0010")

    def test_a_close_passes_when_every_decision_has_a_home(self) -> None:
        self.argue(f"## Decisions\n\n- Sweep by hand — the user, 2026-10-11\n  {self.HOME}\n1. Keep the list {self.HOME}\n")

        self.called("close", "q-0007", "moot", "overtaken")

        self.assertEqual("closed:moot", self.part(self.STEM, "state"))

    def test_a_close_passes_with_no_list_and_with_an_empty_one(self) -> None:
        self.called("close", "q-0005", "decided", "[the record](../record.md) — the user, 2026-09-29")
        self.argue("An argument.\n\n## Decisions\n\nNothing decided yet.\n")

        self.called("close", "q-0007", "moot", "overtaken")

    def test_an_arrow_to_a_question_a_ticket_an_rfc_or_nowhere_is_no_home(self) -> None:
        self.write("docs/tickets/01-0002-sweep.md", "# Sweep\n")
        self.write("docs/rfc/01-0002-sweep.md", "# Sweep — implementation plan\n")
        for link in (
            "[q-0003](q-0003-how-is-a-subtree-archived.md)",
            "[the ticket](../tickets/01-0002-sweep.md)",
            "[the plan](../rfc/01-0002-sweep.md)",
            "[gone](../gone.md)",
            "the record",
        ):
            with self.subTest(link=link):
                self.write(f"{STORE}/{self.STEM}.md", entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open"}))
                self.argue(f"## Decisions\n\n- Sweep by hand → {link}\n")

                self.assertRefused('"Sweep by hand', "close", "q-0007", "moot", "overtaken")

    def test_a_list_inside_a_fence_is_not_read(self) -> None:
        self.argue("An example:\n\n```md\n## Decisions\n\n- Sweep by hand\n```\n")

        self.called("close", "q-0007", "moot", "overtaken")

    def test_prose_between_the_items_and_a_later_heading_hold_no_decision(self) -> None:
        self.argue(
            f"## Decisions\n\n1. Keep the list {self.HOME}\n\n**The user, later:** sweep by hand.\n\n"
            f"2. Sweep by hand\n   {self.HOME}\n\n## Notes\n\n- not a decision\n"
        )

        self.called("close", "q-0007", "moot", "overtaken")

    def test_the_check_reports_a_live_closed_entry_holding_a_decision_with_no_home(self) -> None:
        self.argue("## Decisions\n\n- Sweep by hand\n", stem="q-0005-is-the-id-a-path")

        self.assertTrue(any('no home yet: "Sweep by hand' in problem for problem in self.problems()), self.problems())

    def test_the_check_reads_no_list_in_an_archived_entry(self) -> None:
        before = self.problems()
        name = f"{STORE}/done/q-0012-an-archived-one.md"
        self.write(name, self.read(name) + "\n## Decisions\n\n- Sweep by hand\n")

        self.assertEqual(before, self.problems())

    def test_a_move_and_a_reword_keep_the_list_as_written(self) -> None:
        body = "## Decisions\n\n- Sweep by hand\n"
        self.argue(body)

        self.called("move", "q-0007", "--under", "q-0002")
        self.called("reword", "q-0002.0001", "Who carries a subtree away?")

        self.assertTrue(self.entry_text("q-0002.0001-who-carries-a-subtree-away").endswith("\n" + body))


class ArchivingAtClosure(Declared):
    """A `close` that finishes a subtree moves it to `done/` in the same call; the maintainer's
    move is the sweep for what a closure left behind (parent decision 34, amended)."""

    def archived(self) -> set[str]:
        return {path.stem for path in (self.root / STORE / "done").glob("q-*.md")}

    def test_a_close_that_finishes_a_subtree_moves_it_and_every_link_follows(self) -> None:
        self.write("docs/notes.md", "See [the sessions](questions/q-0010-how-do-sessions-reach-each-other.md).\n")

        said = self.called("close", "q-0010", "moot", "one tree, one directory")

        self.assertIn("moved q-0010 to done/", said)
        self.assertIn("q-0010-how-do-sessions-reach-each-other", self.archived())
        self.assertEqual(
            "See [the sessions](questions/done/q-0010-how-do-sessions-reach-each-other.md).\n", self.read("docs/notes.md")
        )

    def test_a_close_with_an_open_child_moves_nothing_until_the_child_closes_then_both(self) -> None:
        self.called("open", "Across machines?", "--under", "q-0010")

        self.assertNotIn("moved", self.called("close", "q-0010", "moot", "one tree, one directory"))
        said = self.called("close", "q-0010.0001", "moot", "no second machine")

        self.assertIn("moved q-0010, q-0010.0001 to done/", said)
        self.assertLessEqual({"q-0010-how-do-sessions-reach-each-other", "q-0010.0001-across-machines"}, self.archived())

    def test_a_deferred_child_keeps_its_subtree_live(self) -> None:
        self.called("open", "Across machines?", "--under", "q-0010")
        self.called("close", "q-0010.0001", "deferred", "until a second machine, meanwhile one tree")

        said = self.called("close", "q-0010", "moot", "one tree, one directory")

        self.assertNotIn("moved", said)
        self.assertEqual(set(), self.archived() & {"q-0010-how-do-sessions-reach-each-other"})

    def test_a_move_the_mover_refuses_leaves_the_closure_written_and_says_why(self) -> None:
        (self.root / "docs" / "unreadable.md").write_bytes(b"\xff\xfe not utf-8\n")

        status, said = self.call("close", "q-0010", "moot", "one tree, one directory")

        self.assertEqual(1, status, said)
        self.assertIn("not UTF-8", said)
        self.assertEqual("closed:moot", self.part("q-0010-how-do-sessions-reach-each-other", "state"))


class Strikes(Declared):
    """A held question reached again twelve hours or more after its last stamp is struck; any
    other reach writes nothing to it (parent decisions 53 and 54)."""

    def at(self, identity: str, hours: float = 0, session: str = "s-alpha") -> None:
        status, said = self.call("at", identity, session=session, now=NOW + timedelta(hours=hours))
        self.assertEqual(0, status, said)

    def stamped(self, hours: float, count: int = 0) -> str:
        return f"{count}, last {NOW + timedelta(hours=hours):%Y-%m-%dT%H:%M}Z"

    def test_opening_stamps_zero_and_an_at_soon_after_does_not_strike(self) -> None:
        self.called("open", "Is the owner optional?", "--under", "q-0004")
        self.at("q-0004.0001", hours=0.02)

        self.assertEqual(self.stamped(0), self.part("q-0004.0001-is-the-owner-optional", "struck"))

    def test_an_entry_older_than_the_count_is_stamped_at_its_first_reach_and_not_struck(self) -> None:
        self.at("q-0007")

        self.assertEqual(self.stamped(0), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_reach_twelve_hours_on_strikes_once_and_restamps(self) -> None:
        self.at("q-0007")
        self.at("q-0007", hours=12)
        self.at("q-0007", hours=12)

        self.assertEqual(self.stamped(12, count=1), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_reach_short_of_twelve_hours_writes_nothing(self) -> None:
        self.at("q-0007")
        before = self.snapshot()

        self.at("q-0007", hours=11 + 59 / 60)

        self.assertEqual(before, self.snapshot())

    def test_a_stamp_ahead_of_the_clock_does_not_strike(self) -> None:
        self.write(
            f"{STORE}/q-0007-who-moves-a-subtree.md",
            entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "struck": self.stamped(5)}),
        )

        self.at("q-0007")

        self.assertEqual(self.stamped(5), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_ordinary_reaches_leave_the_store_as_it_was_and_the_window_unchanged(self) -> None:
        self.at("q-0004")
        self.said("--window", "--session", "s-alpha")
        before = self.snapshot()

        for hours in (1, 3, 5, 8, 11):
            self.at("q-0004", hours=hours)
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertEqual(before, self.snapshot())
        self.assertIn("window unchanged", window)

    def test_a_question_struck_is_not_struck_again_by_another_session_soon_after(self) -> None:
        self.at("q-0007")
        self.at("q-0007", hours=12)

        self.at("q-0007", hours=12.5, session="s-beta")

        self.assertEqual(self.stamped(12, count=1), self.part("q-0007-who-moves-a-subtree", "struck"))

    def test_a_strike_raced_by_another_write_to_the_entry_is_refused_and_keeps_theirs(self) -> None:
        self.at("q-0007")
        theirs = entry("q-0007", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "lean": "theirs"})

        with self.assertRaises(questions.Refused):
            questions.declare(
                self.root,
                "s-alpha",
                [questions.Clause("at", "q-0007")],
                TODAY,
                between=lambda: self.write(f"{STORE}/q-0007-who-moves-a-subtree.md", theirs),
                now=NOW + timedelta(hours=12),
            )

        self.assertEqual(theirs, self.entry_text("q-0007-who-moves-a-subtree"))


class Naming(Declared):
    """The slug's own cut, the clone's room set aside: `ThePath` holds the fit."""

    def setUp(self) -> None:
        super().setUp()
        self.enterContext(mock.patch.object(questions, "CLONE_ROOM", 0))

    def test_names_a_long_question_with_every_word(self) -> None:
        question = (
            "Does a question whose words run well past the old forty character cut keep every one "
            "of them in its name when the listing shows it?"
        )
        slug = "-".join(questions._words(question))
        self.assertTrue(120 < len(slug) <= questions.SLUG_LENGTH, len(slug))

        self.called("open", question)

        self.assertTrue((self.root / STORE / f"q-0014-{slug}.md").is_file())

    def test_names_a_question_in_another_script_with_its_own_words(self) -> None:
        """A question asked in Russian keeps its words, lower-cased, in the name a listing shows."""
        self.called("open", "Где хранится Ёлка 2026?")

        self.assertTrue((self.root / STORE / "q-0014-где-хранится-ёлка-2026.md").is_file())
        self.assertEqual([], [note.problem for note in self.checked().diagnostics if note.record.startswith(f"{STORE}/q-0014-")])

    def test_keeps_the_marks_a_script_writes_its_words_with(self) -> None:
        self.called("open", "हिन्दी में प्रश्न?")

        self.assertTrue((self.root / STORE / "q-0014-हिन्दी-में-प्रश्न.md").is_file())

    def test_cuts_a_question_written_without_spaces_to_fit_a_clone_and_a_file_name(self) -> None:
        """Chinese and Japanese write a clause as one word; the fit cuts inside it, and keeps the
        name within the 255 bytes a Linux or macOS filesystem allows."""
        with mock.patch.object(questions, "CLONE_ROOM", 128):
            self.called("open", "问题存储在哪里" * 20 + "？")

        [named] = [name.name for name in (self.root / STORE).glob("q-0014-*.md")]
        self.assertLessEqual(len(named.encode("utf-8")), 255)
        self.assertLessEqual(128 + len(f"/{STORE}/done/{named}"), questions.PATH_LIMIT)
        self.assertTrue(named.startswith("q-0014-问题存储在哪里"), named)
        self.assertEqual([], [note.problem for note in self.checked().diagnostics if note.record.startswith(f"{STORE}/q-0014-")])

    def test_cuts_a_question_past_the_length_at_a_word_boundary(self) -> None:
        words = [f"word{number:02d}" for number in range(40)]

        self.called("open", f"{' '.join(words)}?")

        [named] = [name.name for name in (self.root / STORE).glob("q-0014-*.md")]
        slug = named[len("q-0014-") : -len(".md")]
        self.assertLessEqual(len(slug), questions.SLUG_LENGTH)
        self.assertGreater(len(slug) + len("-word00"), questions.SLUG_LENGTH, "cut no earlier than it must")
        self.assertEqual(words[: len(slug.split("-"))], slug.split("-"), "whole words, the question's first")


class ThePath(Store):
    """A path that would pass the platform's limit cuts the slug at a word boundary, never the id;
    the limit is measured in `done/`, the longer of an entry's two homes."""

    def seed(self) -> None:
        super().seed()
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001\n")

    def called(self, *argv: str) -> None:
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main([*argv, "--session", "s-alpha"], root=self.root, today=TODAY, now=NOW)
        self.assertEqual(0, status, said.getvalue())

    def limited(self, name: str, slug_room: int):
        """A limit measured from this tree's own root, the clone's room set aside."""
        prefix = str(self.root / STORE / "done" / f"{name}-")
        limit = mock.patch.object(questions, "PATH_LIMIT", len(prefix) + slug_room + len(".md"))
        room = mock.patch.object(questions, "CLONE_ROOM", 0)
        stack = contextlib.ExitStack()
        stack.enter_context(limit)
        stack.enter_context(room)
        return stack

    def test_an_opened_question_is_named_with_the_words_that_fit_and_checks_clean(self) -> None:
        with self.limited("q-0002", 10):
            self.called("open", "Does a long question fit?")

            self.assertTrue((self.root / STORE / "q-0002-does-a.md").is_file())
            self.assertEqual([], self.problems())

    def test_a_rename_that_deepens_past_the_limit_cuts_the_same_way(self) -> None:
        self.place("q-0002-who-moves-a-subtree", "Who moves a subtree?", {"state": "open"})

        with self.limited("q-0001.0002", len("who-moves")):
            self.called("move", "q-0002", "--under", "q-0001")

            self.assertTrue((self.root / STORE / "q-0001.0002-who-moves.md").is_file())
            self.assertEqual([], self.problems())

    def test_a_name_an_earlier_fit_cut_from_this_trees_own_root_stays_valid(self) -> None:
        with self.limited("q-0002", 10):
            self.called("open", "Does a long question fit?")

            with mock.patch.object(questions, "CLONE_ROOM", len(str(self.root)) + 5):
                self.assertEqual([], self.problems())

    def test_a_name_fits_a_clone_standing_deeper_than_this_tree(self) -> None:
        """A clone into a session's scratch folder under the user's profile stands about 120
        characters deep, and Windows' long paths are off by default: a name written here must
        still check out there."""
        self.called("open", " ".join(f"word{number:02d}" for number in range(40)) + "?", "--under", "q-0001.0001")

        [named] = [name.name for name in (self.root / STORE).glob("q-0001.0001.0001-*.md")]
        self.assertLessEqual(len("c" * 128) + len(f"/{STORE}/done/{named}"), questions.PATH_LIMIT)
        self.assertEqual([], self.problems())


class ClosingByKind(Declared):
    """The kinds `TheCalls` does not close by: each takes its own pointer."""

    def test_deferred_with_its_condition_and_default(self) -> None:
        self.called("close", "q-0007", "deferred", "until the mover exists, meanwhile by hand")

        self.assertEqual("until the mover exists, meanwhile by hand", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_merged_into_another(self) -> None:
        self.called("close", "q-0007", "merged", "q-0003")

        self.assertEqual("closed:merged", self.part("q-0007-who-moves-a-subtree", "state"))
        self.assertEqual("q-0003", self.part("q-0007-who-moves-a-subtree", "answer"))

    def test_a_suspect_flag_on_a_closed_question_is_set_and_cleared(self) -> None:
        self.called("suspect", "q-0005")
        self.called("clear", "q-0008")

        self.assertEqual("closed:decided, suspect", self.part("q-0005-is-the-id-a-path", "state"))
        self.assertEqual("closed:decided", self.part("q-0008-is-the-lean-optional", "state"))


class TheTraceLink(Declared):
    """A question's trace link to the answers it realizes: kept as written, never resolved, carried
    down to every sub-question that states none of its own, and never drawn."""

    def realized(self, identity: str) -> questions.TraceLink | None:
        return questions.realizes(questions.read_store(self.root).index, identity)

    def test_realize_writes_the_link(self) -> None:
        self.called("realize", "q-0004", 'A7 "The question store", A12 "A session resumes, at its step"')

        self.assertEqual(
            'A7 "The question store", A12 "A session resumes, at its step"',
            self.part("q-0004-which-parts-are-optional", "realizes"),
        )

    def test_a_sub_question_reads_its_ancestors_link_as_its_own(self) -> None:
        self.called("realize", "q-0002", 'A7 "The question store"')

        self.assertEqual((("A7", "The question store"),), self.realized("q-0008").answers)
        self.assertIsNone(self.part("q-0008-is-the-lean-optional", "realizes"))

    def test_a_question_that_states_its_own_link_reads_its_own(self) -> None:
        self.called("realize", "q-0002", 'A7 "The question store"')
        self.called("realize", "q-0004", 'A12 "A session resumes at its step"')

        self.assertEqual((("A12", "A session resumes at its step"),), self.realized("q-0008").answers)

    def test_a_derived_question_reports_derived_and_so_do_its_sub_questions(self) -> None:
        self.called("realize", "q-0004", "derived")

        for identity in ("q-0004", "q-0008"):
            with self.subTest(identity=identity):
                self.assertTrue(self.realized(identity).derived)
                self.assertEqual((), self.realized(identity).answers)

    def test_a_question_with_no_link_up_to_its_root_realizes_nothing(self) -> None:
        self.assertIsNone(self.realized("q-0008"))

    def test_a_closed_question_in_done_takes_a_link(self) -> None:
        self.called("realize", "q-0012", 'A7 "The question store"')

        self.assertIn('- **realizes** A7 "The question store"', self.read(f"{STORE}/done/q-0012-an-archived-one.md"))

    def test_a_malformed_link_is_refused_and_writes_nothing(self) -> None:
        for written in ("A7", 'A7 "The store", A7 "Again"', 'derived, A7 "The store"', ""):
            with self.subTest(written=written):
                self.assertRefused("not a trace link", "realize", "q-0004", written)

    def test_the_window_does_not_draw_the_link(self) -> None:
        self.called("realize", "q-0002", 'A7 "The question store"')

        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("q-0002 [open] What an entry holds?  ~ eight parts", text)
        self.assertNotIn("The question store", text)


class TheRung(Declared):
    """A question's highest rung on each ladder it touches (q-0037.0013.0005, decision 11): the
    store holds its form; the rungs' names and order are each ladder's."""

    def test_rung_writes_the_part(self) -> None:
        self.called("rung", "q-0004", "development: a feature, self-improvement: a rule")

        self.assertEqual(
            "development: a feature, self-improvement: a rule", self.part("q-0004-which-parts-are-optional", "rung")
        )
        self.assertEqual([], [problem for problem in self.problems() if "rung" in problem])

    def test_a_second_call_replaces_it_whole(self) -> None:
        self.called("rung", "q-0004", "development: a feature")
        self.called("rung", "q-0004", "development: load-bearing")

        self.assertEqual("development: load-bearing", self.part("q-0004-which-parts-are-optional", "rung"))

    def test_a_value_out_of_form_is_refused_and_writes_nothing(self) -> None:
        for written in ("development", "development: a feature, development: code", ": a feature", ""):
            with self.subTest(written=written):
                self.assertRefused("not a rung", "rung", "q-0004", written)
                self.assertIsNone(self.part("q-0004-which-parts-are-optional", "rung"))

    def test_a_part_written_out_of_form_is_a_diagnostic(self) -> None:
        self.place("q-0013-a-hand-written-one", "A hand-written one?", {"state": "open", "rung": "load-bearing"})

        problems = [problem for problem in self.problems() if "rung" in problem]

        self.assertEqual(1, len(problems), problems)
        self.assertIn("not a rung", problems[0])


class Refusals(Declared):
    """What the store refuses whatever form the call takes."""

    def test_an_id_a_rename_took_away_says_to_draw_the_window_again(self) -> None:
        self.called("move", "q-0007", "--under", "q-0002")

        self.assertRefused("draw the window again", "at", "q-0007")

    def test_a_question_nobody_holds(self) -> None:
        self.assertRefused("no entry holds q-0099", "lean", "q-0099", "a lean")

    def test_a_between_whose_lower_is_not_part_of_the_upper(self) -> None:
        self.assertRefused("q-0004 is not part of q-0003", "open", "Misplaced?", "--between", "q-0003", "q-0004")

    def test_a_move_that_makes_a_cycle(self) -> None:
        self.assertRefused("cycle", "move", "q-0002", "--under", "q-0004")

    def test_a_dependency_that_makes_a_cycle(self) -> None:
        self.called("depend", "q-0004", "--on", "q-0003")

        self.assertRefused("cycle", "depend", "q-0003", "--on", "q-0004")

    def test_a_prune_that_leaves_an_open_child(self) -> None:
        self.assertRefused("leaves q-0007 open", "close", "q-0003", "pruned", "not worth holding")

    def test_a_kind_without_its_pointer(self) -> None:
        self.assertRefused("no answer", "close", "q-0004", "decided")

    def test_a_decided_answer_that_does_not_resolve(self) -> None:
        self.assertRefused("does not resolve", "close", "q-0004", "decided", "[gone](../gone.md)")

    def test_a_session_nobody_registered(self) -> None:
        self.assertRefused("no session s-nobody", "at", "q-0004", session="s-nobody")


class Interference(Declared):
    """What another writer does between a call's validation and its write."""

    def declare_with(self, clauses: list[questions.Clause], meanwhile) -> None:
        questions.declare(self.root, "s-alpha", clauses, TODAY, between=meanwhile, now=NOW)

    def test_an_entry_changed_on_disk_refuses_the_call_and_keeps_the_other_writers_text(self) -> None:
        intruder = entry("q-0004", "Which parts are optional?", {"part of": "q-0002", "state": "open", "lean": "theirs"})
        before = self.snapshot()

        with self.assertRaises(questions.Refused) as refused:
            self.declare_with(
                [questions.Clause("leans", "q-0004", text="mine")],
                lambda: self.write(f"{STORE}/q-0004-which-parts-are-optional.md", intruder),
            )

        self.assertIn("changed since this call read it", str(refused.exception))
        self.assertEqual(intruder, self.entry_text("q-0004-which-parts-are-optional"))
        after = self.snapshot()
        del before[f"{STORE}/q-0004-which-parts-are-optional.md"], after[f"{STORE}/q-0004-which-parts-are-optional.md"]
        self.assertEqual(before, after, "nothing else was written")

    def test_an_open_raced_past_its_attempts_is_refused_and_writes_nothing_of_its_own(self) -> None:
        theirs = entry("q-0014", "Their question?", {"state": "open"})

        with mock.patch.object(questions, "OPEN_ATTEMPTS", 1), self.assertRaises(questions.Taken):
            self.declare_with(
                [questions.Clause("opens", text="My question?")],
                lambda: self.write(f"{STORE}/q-0014-their-question.md", theirs),
            )

        self.assertEqual([], list((self.root / STORE).glob("*-my-question.md")))

    def test_a_sessions_at_changes_its_own_line_and_keeps_one_another_session_wrote_meanwhile(self) -> None:
        def beta_moves() -> None:
            self.write(SESSIONS, session_lines(self.root).replace("s-beta running 2026-09-29T11:00Z q-0010", "s-beta running 2026-09-29T11:59Z q-0001 q-0010"))

        self.declare_with([questions.Clause("at", "q-0002")], beta_moves)

        self.assertEqual(
            "s-gamma ended 2026-09-28 q-0003\n"
            "s-beta running 2026-09-29T11:59Z q-0001 q-0010\n"
            "s-alpha running 2026-09-29T12:00Z q-0002 q-0004,q-0001\n",
            session_lines(self.root),
        )

    def test_a_write_that_fails_partway_stops_and_reports_what_it_wrote(self) -> None:
        def sessions_folder_becomes_a_file() -> None:
            self.write(sessions.ROWS, "not a folder\n")

        with self.assertRaises(questions.WriteInterrupted) as stopped:
            self.declare_with(
                [questions.Clause("at", "q-0004"), questions.Clause("leans", "q-0004", text="written first")],
                sessions_folder_becomes_a_file,
            )

        self.assertEqual([f"{STORE}/q-0004-which-parts-are-optional.md"], stopped.exception.completed)
        self.assertEqual(sessions.ROWS, stopped.exception.failed)
        self.assertIn("written first", self.entry_text("q-0004-which-parts-are-optional"))


class InOrder(Declared):
    def test_clauses_apply_in_order_and_at_is_checked_against_the_result(self) -> None:
        """The writer's front door takes a list, as a judge's typed value will reach it."""
        written = questions.declare(
            self.root,
            "s-alpha",
            [
                questions.Clause("at", "q-0004.0002"),
                questions.Clause("opens", other="q-0004", text="Is the owner optional?"),
                questions.Clause("opens", other="q-0004", text="Is the owner required at birth?"),
                questions.Clause("closes", "q-0004.0001", other="merged", text="q-0004.0002"),
            ],
            TODAY,
        )

        self.assertEqual(["q-0004.0001", "q-0004.0002"], written.opened)
        self.assertIn(
            "- **state** closed:merged\n- **answer** q-0004.0002",
            self.read(f"{STORE}/done/q-0004.0001-is-the-owner-optional.md"),
            "the merge finished its subtree, so it moved",
        )
        self.assertIn("- **state** open", self.entry_text("q-0004.0002-is-the-owner-required-at-birth"))
        self.assertEqual("q-0004.0002", self.own_line().split()[3])

    def test_a_prune_goes_through_once_the_child_that_stands_alone_is_moved_out_first(self) -> None:
        self.called("move", "q-0007", "--to-root")
        self.called("close", "q-0003", "pruned", "archiving is the mover's")

        self.assertIn("closed:pruned", self.entry_text("q-0003-how-is-a-subtree-archived"))


class ARoundTrip(Declared):
    def test_opens_attaches_closes_and_prunes_and_leaves_no_problem_behind(self) -> None:
        before = self.problems()

        for call in (
            ("open", "Is the owner optional?", "--under", "q-0004"),
            ("at", "q-0004.0001"),
            ("open", "Must an owner exist at birth?", "--under", "q-0004.0001"),
            ("close", "q-0004.0001.0001", "decided", "[the record](../record.md) — the user, 2026-09-29"),
            ("at", "q-0004"),
            ("close", "q-0004.0001", "pruned", "the store keeps no owner rule"),
        ):
            self.called(*call)

        self.assertEqual(before, self.problems(), "the fixture's flat ids are reported as before, and nothing more")
        self.assertIn("closed:pruned", self.read(f"{STORE}/done/q-0004.0001-is-the-owner-optional.md"))
        self.assertNotIn("q-0004.0001", self.said("--tree", "q-0004")[1], "the finished subtree left the live tree")


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


SHELF = ".agents/skills/questions/STORE-ARRIVAL.md"
# The fixture's own words, never the shipped ones, so a seed that carried words of its own would
# be caught writing them.
FIXTURE_ROOTS = ("What is the fixture for?", "How is the fixture built?", "Where does the fixture live?")


def shelf(*roots: str) -> str:
    lines = "".join(f"{root}\n" for root in roots)
    return f"# What the store holds before anything has happened in it\n\nMachine input.\n\n```roots\n{lines}```\n"


class Seeding(RepositoryCase):
    """A store that holds no entry opens with the roots its shelf words; one that holds any is
    the project's and is left."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)
        self.write(SHELF, shelf(*FIXTURE_ROOTS))

    def seeded(self) -> list[str]:
        return questions.seed(self.root, NOW)

    def snapshot(self) -> dict[str, bytes]:
        return {name: (self.root / name).read_bytes() for name in folder_listing(self.root)}

    def test_an_empty_store_opens_with_the_shelf_roots_in_order_and_nothing_under_them(self) -> None:
        written = self.seeded()

        store = questions.read_store(self.root)
        self.assertEqual(3, len(written))
        self.assertEqual(["q-0001", "q-0002", "q-0003"], [read.identity for read in store.roots])
        self.assertEqual(list(FIXTURE_ROOTS), [read.question for read in store.roots])
        self.assertTrue(all(read.open and read.parent is None for read in store.roots))
        self.assertEqual({}, store.children)
        checked = questions.check(self.root)
        self.assertEqual([], checked.diagnostics)
        self.assertEqual(3, checked.entries)

    def test_seeding_registers_no_session(self) -> None:
        self.seeded()

        self.assertFalse((self.root / SESSIONS).exists())

    def test_a_store_holding_a_live_entry_is_left_as_it_stands(self) -> None:
        self.write(f"{STORE}/q-0001-whose-store-is-this.md", entry("q-0001", "Whose store is this?", {"state": "open"}))
        untouched = self.snapshot()

        self.assertEqual([], self.seeded())
        self.assertEqual(untouched, self.snapshot())

    def test_a_store_holding_only_an_archived_entry_is_left_as_it_stands(self) -> None:
        self.write(
            f"{STORE}/done/q-0001-whose-store-was-this.md",
            entry("q-0001", "Whose store was this?", {"state": "closed:pruned", "answer": "nobody asked"}),
        )
        untouched = self.snapshot()

        self.assertEqual([], self.seeded())
        self.assertEqual(untouched, self.snapshot())

    def test_a_sessions_file_alone_is_no_entry_and_the_store_is_seeded(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 -\n")

        self.assertEqual(3, len(self.seeded()))
        self.assertEqual("s-alpha running 2026-09-29 -\n", session_lines(self.root))

    def test_a_shelf_that_cannot_say_the_roots_is_refused_with_nothing_written(self) -> None:
        for said, reason in (
            (None, "no shelf"),
            ("# What the store holds\n\nNo block here.\n", "no `roots` block"),
            ("# What the store holds\n\n```roots\n\n```\n", "names no root"),
        ):
            with self.subTest(reason=reason):
                if said is None:
                    (self.root / SHELF).unlink(missing_ok=True)
                else:
                    self.write(SHELF, said)
                with self.assertRaises(questions.Refused) as refused:
                    self.seeded()
                self.assertIn(reason, str(refused.exception))
                self.assertFalse((self.root / STORE).exists())

    def test_the_command_says_what_it_wrote_then_that_the_store_was_left(self) -> None:
        first, second = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(first):
            seeded = questions.main(["--seed"], root=self.root, today=TODAY, now=NOW)
        with contextlib.redirect_stdout(second):
            left = questions.main(["--seed"], root=self.root, today=TODAY, now=NOW)

        self.assertEqual(0, seeded)
        self.assertEqual(3, first.getvalue().count("wrote docs/questions/q-000"))
        self.assertEqual(0, left)
        self.assertIn("holds entries; left as it stands", second.getvalue())

    def test_the_command_refuses_a_shelf_with_no_roots(self) -> None:
        (self.root / SHELF).unlink()
        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--seed"], root=self.root, today=TODAY, now=NOW)

        self.assertEqual(2, status)
        self.assertIn("refused: seed:", said.getvalue())


if __name__ == "__main__":
    unittest.main()


class ARelativeId(Store):
    """An id in an entry is whole. One already written is a finding for maintenance; one offered to
    the writer in a lean is refused."""

    def relative(self) -> list[str]:
        return [note.finding for note in questions.check(self.root).findings if "relative id" in note.finding]

    def test_in_a_lean_already_written_is_a_finding_not_a_problem(self) -> None:
        self.place("q-0090-which-store", "Which store?", {"state": "open", "lean": "open as .0003 since"})
        self.assertEqual([], self.problems())
        self.assertEqual(1, len(self.relative()), self.relative())

    def test_inside_a_fenced_block_is_not_read(self) -> None:
        fenced = chr(10).join(["", "```", ".0003", "```", ""])
        self.write(f"{STORE}/q-0090-which-store.md", entry("q-0090", "Which store?", {"state": "open"}) + fenced)
        self.assertEqual([], self.relative())


class ALeanWithARelativeId(Declared):
    def test_is_refused_and_nothing_is_written(self) -> None:
        self.assertRefused("relative id", "lean", "q-0004", "the user, 2026-10-23: open as .0003")

    def test_a_whole_id_is_written(self) -> None:
        self.called("lean", "q-0004", "the user, 2026-10-23: open as q-0004.0003")
        written = next(Path(self.root, STORE).glob("q-0004-*.md")).read_text(encoding="utf-8")
        self.assertEqual(1, len([line for line in written.splitlines() if "q-0004.0003" in line]))


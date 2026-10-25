# Mechanism: session
"""The sessions' rows: registered, seen, ended, reopened and carried over, and the hooks that do it."""

from __future__ import annotations

import contextlib
import io
import json
import os
import threading
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest import mock

from repository import RepositoryCase, folder_listing
from test_questions import DESKTOP_ID, NOW, SESSIONS, STORE, TODAY, Rendered, Store, remember_windows_in_the_case, session_lines

import questions
import sessions


class TheSessions(Store):
    """One line per session: its tag, running or ended, the date it last wrote, its current
    question or `-` before it has one, and up to four recent ones."""

    def setUp(self) -> None:
        super().setUp()
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001 q-0001\ns-beta ended 2026-09-01 q-0001\n")

    def checked(self):
        return questions.check(self.root)

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
        self.write(SESSIONS, "s-alpha asleep 2026-09-29 q-0001.0001\n")
        self.assertReported("line 1")

    def test_more_than_four_recent_questions_is_out_of_the_form(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001 q-0001,q-0001.0001,q-0001,q-0001.0001,q-0001\n")
        self.assertReported("line 1")

    def test_a_tag_registered_twice_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001.0001\ns-alpha ended 2026-09-28 q-0001\n")
        self.assertReported("s-alpha")

    def test_a_position_naming_a_missing_entry_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0009\n")
        self.assertReported("q-0009")

    def test_a_running_session_on_a_closed_question_is_a_finding_not_a_failure(self) -> None:
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
        )

        stranded = [finding for finding in self.findings() if "s-alpha" in finding]

        self.assertEqual([], self.problems())
        self.assertEqual(1, len(stranded), stranded)
        self.assertIn("closed", stranded[0])

    def test_a_line_carries_the_time_it_was_written_to_the_minute(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0001.0001\ns-beta ended 2026-09-01 q-0001\n")
        self.assertEqual([], self.problems())

    def test_a_time_out_of_the_form_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T7:30Z q-0001.0001\n")
        self.assertReported("line 1")

    def test_a_running_session_long_silent_is_no_finding_the_next_wake_ends_it(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-01 q-0001.0001\n")
        self.assertEqual([], self.findings())

    def test_findings_leave_the_exit_status_at_zero(self) -> None:
        self.place(
            "q-0001.0001-what-an-entry-holds",
            "What an entry holds?",
            {"part of": "q-0001", "state": "closed:moot", "answer": "gone"},
        )
        self.write(SESSIONS, "s-alpha running 2000-01-01 q-0001.0001\n")

        said = io.StringIO()
        with contextlib.redirect_stdout(said):
            status = questions.main(["--check"], root=self.root, today=TODAY)

        self.assertEqual(0, status)
        self.assertTrue(json.loads(said.getvalue())["findings"])


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

    def test_a_session_nobody_registered_is_refused_with_the_way_to_register(self) -> None:
        status, text = self.said("--window", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertIn("--wake", text)


class TheWake(Rendered):
    def registered_tag(self, text: str) -> str:
        return text.splitlines()[0].split()[1].rstrip(",")

    def test_registers_a_new_session_without_a_position_and_prints_its_tag(self) -> None:
        before = session_lines(self.root)

        status, text = self.said("--wake")

        tag = self.registered_tag(text)
        self.assertEqual(0, status)
        self.assertEqual(before + f"{tag} running 2026-09-29T12:00Z -\n", session_lines(self.root))
        self.assertIn("registered now", text.splitlines()[0])

    def test_two_wakes_register_two_sessions(self) -> None:
        _, first = self.said("--wake")
        _, second = self.said("--wake")

        self.assertNotEqual(self.registered_tag(first), self.registered_tag(second))
        self.assertEqual(5, len(session_lines(self.root).splitlines()))

    def test_reports_the_running_sessions_first_with_their_positions_and_no_ended_one(self) -> None:
        _, text = self.said("--wake")

        listed = self.section(text, "sessions:")
        self.assertIn("s-alpha running, last wrote 2026-09-29T11:30Z, at q-0004", listed)
        self.assertNotIn("s-gamma", listed, "an ended session is nobody's business at a wake")
        self.assertLess(text.index("sessions:"), text.index("deferred"))

    def test_lists_every_deferral_with_its_condition_and_every_suspect_entry(self) -> None:
        _, text = self.said("--wake")

        deferred = self.section(text, "deferred, to re-check whether each condition is met:")
        self.assertIn("q-0006", deferred)
        self.assertIn("q-0009 [closed:deferred] Are twins found by embeddings? — until a place to run, meanwhile word match", deferred)
        suspect = self.section(text, "suspect, to re-read:")
        self.assertIn("q-0008", suspect)
        self.assertIn("q-0013", suspect)

    def test_lists_the_straw_dogs_whose_question_is_due_wherever_they_stand(self) -> None:
        self.write("AGENTS.md", '# Entry\n\n<straw-dog question="q-0005">Held.</straw-dog>\n')
        self.write(".agents/skills/keeper/SKILL.md", '<straw-dog question="q-0010">Open still.</straw-dog>\n\n```md\n<straw-dog question="q-0011">Sample.</straw-dog>\n```\n')
        self.write(".agents/scripts/keeper.py", "x = 1\n# TODO q-0011: pruned since.\n")

        _, text = self.said("--wake")

        due = self.section(text, "straw dogs due, their text to re-read:").strip().splitlines()
        self.assertEqual(
            [
                ".agents/scripts/keeper.py:2 → q-0011 [closed:pruned] Is height depth?",
                "AGENTS.md:3 → q-0005 [closed:decided] Is the id a path?",
            ],
            [line.strip() for line in due],
        )
        self.assertLess(text.index("deferred, to re-check"), text.index("straw dogs due"))

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
    def said(self, *argv: str) -> tuple[int, str]:
        if argv[:1] == ("--end",):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                status = sessions.main(list(argv), root=self.root, now=NOW)
            return status, out.getvalue()
        return super().said(*argv)

    def test_marks_the_session_ended_keeping_its_position_and_touching_no_other_line(self) -> None:
        status, _ = self.said("--end", "--session", "s-alpha")

        self.assertEqual(0, status)
        self.assertEqual(
            "s-gamma ended 2026-09-28 q-0003\n"
            "s-beta running 2026-09-29T11:00Z q-0010\n"
            "s-alpha ended 2026-09-29T12:00Z q-0004 q-0002,q-0001\n",
            session_lines(self.root),
        )

    def test_a_later_wake_of_the_ended_session_finds_where_it_stopped(self) -> None:
        self.said("--end", "--session", "s-alpha")

        _, text = self.said("--wake", "--session", "s-alpha")

        self.assertIn("current: q-0004", text)

    def test_a_session_nobody_registered_is_refused_and_nothing_is_written(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said("--end", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertEqual(untouched, self.snapshot())


class Hooked(Rendered):
    """What each host's hook receives and what it gets back.

    The desktop app names every process it starts with its own conversation id, this suite's
    run included when it runs there, so each case starts with none and sets one where it is the
    subject."""

    def setUp(self) -> None:
        super().setUp()
        self.enterContext(mock.patch.dict(os.environ))
        os.environ.pop(DESKTOP_ID, None)

    def hook(self, host: str, payload: dict | str, desktop_id: str | None = None) -> tuple[int, str]:
        stdin = io.StringIO(payload if isinstance(payload, str) else json.dumps(payload))
        out = io.StringIO()
        named = {DESKTOP_ID: desktop_id} if desktop_id else {}
        with contextlib.redirect_stdout(out), mock.patch("sys.stdin", stdin), mock.patch.dict(os.environ, named):
            status = questions.main(["--hook", host], root=self.root, today=TODAY, now=NOW)
        return status, out.getvalue()

    def context(self, said: str) -> str:
        """The text a host would place in the agent's context from the hook's answer."""
        answer = json.loads(said)
        if "hookSpecificOutput" in answer:
            return answer["hookSpecificOutput"]["additionalContext"]
        return answer["additional_context"]


class TheHook(Hooked):
    def test_claude_code_registers_a_new_session_under_its_own_id_and_injects_the_wake(self) -> None:
        status, said = self.hook("claude-code", {"session_id": "abc-123", "hook_event_name": "SessionStart", "source": "startup"})

        self.assertEqual(0, status)
        self.assertEqual("SessionStart", json.loads(said)["hookSpecificOutput"]["hookEventName"])
        self.assertIn("session: abc-123, registered now", self.context(said))
        self.assertIn("abc-123 running 2026-09-29T12:00Z -", session_lines(self.root))

    def test_a_resumed_session_is_not_registered_twice(self) -> None:
        _, said = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "resume"})

        self.assertIn("session: s-alpha, already registered", self.context(said))
        self.assertEqual(3, len(session_lines(self.root).splitlines()))

    def test_in_the_desktop_app_a_session_is_registered_under_the_apps_id(self) -> None:
        _, said = self.hook(
            "claude-code", {"session_id": "abc-123", "hook_event_name": "SessionStart", "source": "startup"}, "local_1"
        )

        self.assertIn("session: local_1, registered now", self.context(said))
        self.assertIn("local_1 running", session_lines(self.root))
        self.assertNotIn("abc-123", session_lines(self.root))

    def test_a_conversation_the_desktop_app_resumes_under_a_new_id_is_the_session_it_was(self) -> None:
        """The desktop app resumed a conversation under a new Claude Code id twice (2026-10-09, a
        rollback; 2026-10-10, a reopening), and each time the store took it for a new session; the
        app's own id for the conversation stayed the same throughout."""
        _, said = self.hook(
            "claude-code", {"session_id": "fork-1", "hook_event_name": "SessionStart", "source": "resume"}, "s-alpha"
        )

        self.assertIn("session: s-alpha, already registered", self.context(said))
        self.assertIn("s-alpha running 2026-09-29T11:30Z q-0004", session_lines(self.root), "its position kept")
        self.assertNotIn("fork-1", session_lines(self.root))

    def test_a_desktop_message_whose_start_was_never_seen_registers_the_apps_id(self) -> None:
        self.hook("claude-code", {"session_id": "abc-9", "hook_event_name": "UserPromptSubmit", "prompt": "hi"}, "local_2")

        self.assertIn("local_2 running", session_lines(self.root))
        self.assertNotIn("abc-9", session_lines(self.root))

    def test_a_message_gets_the_window_and_then_one_line_while_nothing_moved(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}

        _, first = self.hook("codex", submit)
        _, second = self.hook("codex", submit)

        self.assertIn("current: q-0004", self.context(first))
        self.assertEqual("UserPromptSubmit", json.loads(first)["hookSpecificOutput"]["hookEventName"])
        self.assertIn("window unchanged since your last one", self.context(second))
        self.assertIn("s-alpha at q-0004; say what this turn is", self.context(second))
        self.assertIn("`questions.py at q-N --session s-alpha` on the one that contains the message", self.context(second))
        self.assertIn("a process, no call", self.context(second))
        self.assertNotIn("questions.py at q-0004", self.context(second))
        self.assertNotIn("path (root to current):", self.context(second))

    def test_a_moved_position_or_a_changed_entry_draws_the_window_again(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.hook("claude-code", submit)
        self.said("at", "q-0002", "--session", "s-alpha")

        _, moved = self.hook("claude-code", submit)
        self.said("lean", "q-0007", "by hand", "--session", "s-beta")
        _, changed = self.hook("claude-code", submit)

        self.assertIn("current: q-0002", self.context(moved))
        self.assertIn("path (root to current):", self.context(changed))

    def test_another_sessions_move_alone_does_not_redraw_it(self) -> None:
        """q-0007 is stamped first, since the first reach of an entry older than the count writes
        its stamp, which is a change to the entry and so redraws."""
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.said("at", "q-0007", "--session", "s-beta")
        self.said("at", "q-0010", "--session", "s-beta")
        self.hook("claude-code", submit)
        self.assertEqual(0, self.said("at", "q-0007", "--session", "s-beta")[0], "the other session moved")

        _, said = self.hook("claude-code", submit)

        self.assertIn("window unchanged", self.context(said))

    def test_a_compaction_makes_the_next_window_whole(self) -> None:
        submit = {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"}
        self.hook("claude-code", submit)

        _, compacted = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "compact"})
        self.hook("codex", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "next"})
        _, codex_compacts = self.hook("codex", {"session_id": "s-alpha", "hook_event_name": "PostCompact", "trigger": "auto"})
        _, after = self.hook("codex", submit)

        self.assertIn("path (root to current):", self.context(compacted))
        self.assertEqual("", codex_compacts.strip())
        self.assertIn("path (root to current):", self.context(after))

    def test_cursor_registers_under_its_conversation_id_and_answers_in_its_own_form(self) -> None:
        _, said = self.hook(
            "cursor", {"conversation_id": "conv-9", "session_id": "other", "hook_event_name": "sessionStart"}
        )

        self.assertIn("session: conv-9, registered now", self.context(said))
        self.assertIn("conv-9 running", session_lines(self.root))

    def raw_hook(self, host: str, raw: bytes) -> str:
        """The hook fed bytes as a host's pipe carries them, decoded by nothing in between."""
        out = io.StringIO()
        with contextlib.redirect_stdout(out), mock.patch("sys.stdin", io.TextIOWrapper(io.BytesIO(raw))):
            questions.main(["--hook", host], root=self.root, today=TODAY, now=NOW)
        return out.getvalue()

    def test_input_written_as_utf16_with_its_mark_is_read(self) -> None:
        """Cursor on Windows answered "Expecting value: line 1 column 1 (char 0)" to a payload it
        logged as sent: input in another encoding than the code page the pipe was read in."""
        sent = json.dumps({"conversation_id": "conv-16", "hook_event_name": "sessionStart"})

        said = self.raw_hook("cursor", sent.encode("utf-16"))

        self.assertIn("session: conv-16, registered now", self.context(said))

    def test_input_written_as_utf8_with_its_mark_is_read(self) -> None:
        sent = json.dumps({"conversation_id": "conv-8", "hook_event_name": "sessionStart"})

        said = self.raw_hook("cursor", sent.encode("utf-8-sig"))

        self.assertIn("session: conv-8, registered now", self.context(said))

    def test_input_that_is_not_json_is_named_by_its_length_and_how_it_begins(self) -> None:
        said = self.raw_hook("claude-code", b"")

        self.assertIn("the hook's input is not JSON: 0 characters", said)

    def test_cursor_hands_its_session_on_to_later_hooks_and_shells_as_env(self) -> None:
        _, said = self.hook("cursor", {"conversation_id": "conv-9", "hook_event_name": "sessionStart"})

        self.assertEqual({"QUESTIONS_SESSION": "conv-9"}, json.loads(said)["env"])

    def test_cursor_compaction_forgets_the_last_window(self) -> None:
        self.said("--window", "--session", "s-alpha")

        _, said = self.hook("cursor", {"conversation_id": "s-alpha", "hook_event_name": "preCompact"})
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertEqual("{}", said.strip())
        self.assertIn("path (root to current):", window)

    def test_a_session_whose_start_was_never_seen_is_registered_by_its_first_message(self) -> None:
        _, said = self.hook("claude-code", {"session_id": "late-1", "hook_event_name": "UserPromptSubmit", "prompt": "hi"})

        self.assertIn("late-1 running 2026-09-29T12:00Z -", session_lines(self.root))
        self.assertIn("session: late-1", self.context(said))

    def test_an_event_it_has_no_use_for_answers_nothing(self) -> None:
        status, said = self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "Stop"})

        self.assertEqual((0, ""), (status, said.strip()))

    def test_a_problem_at_a_known_event_is_answered_in_the_hosts_own_form(self) -> None:
        status, said = self.hook("cursor", {"hook_event_name": "sessionStart"})

        self.assertEqual(0, status)
        self.assertIn("questions hook", self.context(said))

    def test_never_fails_the_host_a_problem_becomes_a_notice_in_context(self) -> None:
        for host, payload in (("claude-code", "not json"), ("nohost", {"session_id": "x", "hook_event_name": "SessionStart"})):
            with self.subTest(host=host):
                status, said = self.hook(host, payload)

                self.assertEqual(0, status)
                self.assertIn("questions hook", said)


class TheAgentsOwnWindow(Hooked):
    def test_says_unchanged_when_nothing_moved_and_draws_it_whole_on_request(self) -> None:
        self.said("--window", "--session", "s-alpha")

        _, again = self.said("--window", "--session", "s-alpha")
        _, full = self.said("--window", "--session", "s-alpha", "--full")

        self.assertIn("window unchanged since your last one", again)
        self.assertIn("--full", again)
        self.assertIn("path (root to current):", full)

    def test_a_call_it_does_not_know_prints_the_calls_it_does(self) -> None:
        status, said = self.said("go", "q-0010", "--session", "s-alpha")

        self.assertEqual(2, status)
        self.assertIn("at, open, move, reword, depend, undepend, close", said)


class ASilentSession(Hooked):
    """A running line silent three hours is ended by the next wake, quietly, and a message of its
    own session turns it running again (the user, 2026-10-10)."""

    def seen_at(self, tag: str, when: datetime) -> None:
        """The session's window memory, as if its session last drew a window then; one it already
        holds keeps its fingerprint."""
        memory = sessions.memory(self.root, tag)
        memory.parent.mkdir(parents=True, exist_ok=True)
        if not memory.is_file():
            memory.write_text("drawn", encoding="utf-8")
        os.utime(memory, (when.timestamp(), when.timestamp()))

    def seen(self, tag: str) -> float:
        return os.path.getmtime(sessions.memory(self.root, tag))

    def line(self, tag: str) -> str:
        return next(line for line in session_lines(self.root).splitlines() if line.startswith(f"{tag} "))

    def start(self, tag: str, source: str = "startup") -> str:
        _, said = self.hook("claude-code", {"session_id": tag, "hook_event_name": "SessionStart", "source": source})
        return said

    def test_a_line_last_seen_three_hours_ago_is_ended_at_another_sessions_start_its_position_kept(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-29T09:00Z q-0010\n")

        self.start("s-new")

        self.assertEqual("s-beta ended 2026-09-29T09:00Z q-0010", self.line("s-beta"))

    def test_a_line_seen_under_three_hours_ago_stays_running(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-29T09:01Z q-0010\n")

        self.start("s-new")

        self.assertEqual("s-beta running 2026-09-29T09:01Z q-0010", self.line("s-beta"))

    def test_a_line_written_long_ago_stays_running_while_its_session_draws_windows(self) -> None:
        """A session answering messages on one question writes nothing to the store for hours."""
        self.write(SESSIONS, "s-beta running 2026-09-20 q-0010\n")
        self.seen_at("s-beta", NOW - timedelta(minutes=10))

        self.start("s-new")

        self.assertEqual("s-beta running 2026-09-20 q-0010", self.line("s-beta"))

    def test_the_waking_sessions_own_line_is_not_ended_by_its_own_wake(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-01 q-0004\n")

        self.start("s-alpha")

        self.assertEqual("s-alpha running 2026-09-01 q-0004", self.line("s-alpha"))

    def test_a_compaction_ends_nothing(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004\ns-beta running 2026-09-01 q-0010\n")

        self.start("s-alpha", source="compact")

        self.assertEqual("s-beta running 2026-09-01 q-0010", self.line("s-beta"))

    def test_the_wake_by_hand_ends_as_the_hook_does(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-01 q-0010\n")

        self.said("--wake")

        self.assertEqual("s-beta ended 2026-09-01T00:00Z q-0010", self.line("s-beta"))

    def test_the_wake_says_nothing_of_having_ended_one(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-01 q-0010\n")

        said = self.context(self.start("s-new"))

        self.assertEqual(0, said.count("s-beta"), said)
        self.assertEqual("s-beta ended 2026-09-01T00:00Z q-0010", self.line("s-beta"))

    def test_a_silent_row_ended_takes_the_time_its_session_was_last_seen(self) -> None:
        """The seven days run from the session's end, not its last `at` (the user, 2026-10-22)."""
        self.write(SESSIONS, "s-beta running 2026-09-20 q-0010\n")
        self.seen_at("s-beta", NOW - timedelta(hours=4))

        self.start("s-new")

        self.assertEqual("s-beta ended 2026-09-29T08:00Z q-0010", self.line("s-beta"))

    def test_a_line_another_session_wrote_meanwhile_is_kept(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-01 q-0010\ns-gamma running 2026-09-29T11:59Z q-0003\n")

        self.start("s-new")

        self.assertEqual("s-gamma running 2026-09-29T11:59Z q-0003", self.line("s-gamma"))

    def test_an_ended_line_runs_again_at_its_sessions_next_message_and_no_other_line_moves(self) -> None:
        self.write(SESSIONS, "s-alpha ended 2026-09-29T08:00Z q-0004 q-0002\ns-beta ended 2026-09-01 q-0010\n")

        self.hook("claude-code", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit", "prompt": "hi"})

        self.assertEqual(
            "s-beta ended 2026-09-01 q-0010\ns-alpha running 2026-09-29T12:00Z q-0004 q-0002\n",
            session_lines(self.root),
        )

    def test_an_ended_line_runs_again_when_its_agent_draws_the_window_by_the_rule(self) -> None:
        self.write(SESSIONS, "s-alpha ended 2026-09-29T08:00Z q-0004\n")

        self.said("--window", "--session", "s-alpha")

        self.assertEqual("s-alpha running 2026-09-29T12:00Z q-0004", self.line("s-alpha"))

    def test_every_window_marks_its_session_seen_the_unchanged_one_too(self) -> None:
        self.said("--window", "--session", "s-alpha")
        self.seen_at("s-alpha", NOW - timedelta(hours=5))

        _, again = self.said("--window", "--session", "s-alpha")

        self.assertIn("window unchanged since your last one", again)
        self.assertEqual(NOW.timestamp(), self.seen("s-alpha"))

    def test_after_a_compaction_the_session_is_still_seen_and_its_next_window_whole(self) -> None:
        self.said("--window", "--session", "s-alpha")

        self.hook("cursor", {"conversation_id": "s-alpha", "hook_event_name": "preCompact"})
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertTrue(sessions.memory(self.root, "s-alpha").is_file())
        self.assertIn("path (root to current):", window)

    def test_cursors_message_marks_its_session_seen_and_lets_the_message_through_injecting_nothing(self) -> None:
        self.write(SESSIONS, "s-alpha ended 2026-09-29T08:00Z q-0004\n")

        _, said = self.hook("cursor", {"conversation_id": "s-alpha", "hook_event_name": "beforeSubmitPrompt", "prompt": "hi"})
        _, window = self.said("--window", "--session", "s-alpha")

        self.assertEqual({"continue": True}, json.loads(said))
        self.assertEqual("s-alpha running 2026-09-29T12:00Z q-0004", self.line("s-alpha"))
        self.assertIn("path (root to current):", window, "the hook drew no window the agent never saw")

    def test_cursors_message_naming_no_session_is_still_let_through(self) -> None:
        status, said = self.hook("cursor", {"hook_event_name": "beforeSubmitPrompt"})

        self.assertEqual((0, {"continue": True}), (status, json.loads(said)))

    def test_cursors_message_from_a_session_never_seen_starting_registers_it(self) -> None:
        _, said = self.hook("cursor", {"conversation_id": "late-9", "hook_event_name": "beforeSubmitPrompt"})

        self.assertEqual({"continue": True}, json.loads(said))
        self.assertEqual("late-9 running 2026-09-29T12:00Z -", self.line("late-9"))


class AFirstWake(RepositoryCase):
    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)

    def test_in_a_tree_without_a_store_registers_the_first_session(self) -> None:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = questions.main(["--wake"], root=self.root, today=TODAY, now=NOW)

        tag = out.getvalue().splitlines()[0].split()[1].rstrip(",")
        self.assertEqual(0, status)
        self.assertEqual(f"{tag} running 2026-09-29T12:00Z -\n", session_lines(self.root))


class SessionsWrittenAtOnce(RepositoryCase):
    """Each session writes its own file, so however many write at once, none undoes another's."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)

    def register_at_once(self, tags: list[str]) -> None:
        """Every registration released together, so the writes meet rather than queue."""
        gate = threading.Barrier(len(tags))
        failures: list[Exception] = []

        def register(tag: str) -> None:
            gate.wait()
            try:
                sessions.register(self.root, NOW, tag)
            except Exception as failure:  # noqa: BLE001 — collected, so the assertion names it
                failures.append(failure)

        threads = [threading.Thread(target=register, args=(tag,)) for tag in tags]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual([], failures)

    def registered(self) -> list[str]:
        return sorted(held.tag for held in sessions.rows(self.root)[0])

    def test_twenty_sessions_registered_at_once_all_stand(self) -> None:
        tags = [f"s-{number:02}" for number in range(20)]

        self.register_at_once(tags)

        self.assertEqual(tags, self.registered())

    def test_two_first_writes_over_the_single_file_keep_every_line(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001\ns-beta ended 2026-09-01 -\n")

        self.register_at_once(["s-one", "s-two"])

        self.assertEqual(["s-alpha", "s-beta", "s-one", "s-two"], sorted(folder_listing(self.root / sessions.ROWS)))
        self.assertEqual(["s-alpha", "s-beta", "s-one", "s-two"], self.registered())
        self.assertEqual("s-alpha running 2026-09-29 q-0001\n", self.read(f"{sessions.ROWS}/s-alpha"))

    def test_a_line_the_form_does_not_admit_is_carried_over_and_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29 q-0001\nnot a session line\n")

        sessions.register(self.root, NOW, "s-one")

        folder = sessions.ROWS
        carried = [name for name in folder_listing(self.root / folder) if "not a session line" in self.read(f"{folder}/{name}")]
        self.assertEqual(1, len(carried), "kept, under a name of its own")
        _, problems, _ = sessions.rows(self.root)
        self.assertEqual([f"{folder}/{carried[0]}"], [problem.record for problem in problems])


class TheFormerFolder(RepositoryCase):
    """A store from before the rows' folder keeps them under the question store; the first write
    carries them over as the single file's lines were, by links that never overwrite."""

    def setUp(self) -> None:
        super().setUp()
        remember_windows_in_the_case(self)

    def test_the_former_folders_rows_are_carried_into_the_folder_at_the_first_write(self) -> None:
        self.write(f"{sessions.FORMER_ROWS}/s-alpha", "s-alpha running 2026-09-29 q-0001\n")

        sessions.register(self.root, NOW, "s-one")

        self.assertEqual(["s-alpha", "s-one"], sorted(folder_listing(self.root / sessions.ROWS)))
        self.assertEqual("s-alpha running 2026-09-29 q-0001\n", self.read(f"{sessions.ROWS}/s-alpha"))
        self.assertFalse((self.root / sessions.FORMER_ROWS).exists(), "the former folder is gone")

    def test_a_row_its_session_wrote_in_the_folder_since_is_not_overwritten(self) -> None:
        self.write(f"{sessions.FORMER_ROWS}/s-alpha", "s-alpha running 2026-09-01 q-0001\n")
        self.write(f"{sessions.ROWS}/s-alpha", "s-alpha running 2026-09-29T11:00Z q-0001\n")

        sessions.register(self.root, NOW, "s-one")

        self.assertEqual("s-alpha running 2026-09-29T11:00Z q-0001\n", self.read(f"{sessions.ROWS}/s-alpha"))
        self.assertFalse((self.root / sessions.FORMER_ROWS).exists())

    def test_rows_still_in_the_former_folder_are_read_until_carried(self) -> None:
        self.write(f"{sessions.FORMER_ROWS}/s-alpha", "s-alpha running 2026-09-29 q-0001\n")

        self.assertEqual(["s-alpha"], [held.tag for held in sessions.rows(self.root)[0]])


class TheSessionsOwnCommands(Rendered):
    def said_to_sessions(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = sessions.main(list(argv), root=self.root, now=NOW)
        return status, out.getvalue()

    def test_end_is_the_sessions_own_and_prints_where_it_stopped(self) -> None:
        status, said = self.said_to_sessions("--end", "--session", "s-alpha")

        self.assertEqual((0, "ended s-alpha at q-0004\n"), (status, said))
        self.assertIn("s-alpha ended 2026-09-29T12:00Z q-0004 q-0002,q-0001", session_lines(self.root))

    def test_end_of_a_session_nobody_registered_is_refused(self) -> None:
        status, said = self.said_to_sessions("--end", "--session", "s-nobody")

        self.assertEqual(2, status)
        self.assertIn("--wake", said)

    def test_check_reports_a_row_out_of_the_form_and_fails(self) -> None:
        self.write(SESSIONS, "s-alpha asleep 2026-09-29 q-0004\n")

        status, said = self.said_to_sessions("--check")

        self.assertEqual(1, status)
        self.assertIn("line 1", json.loads(said)["diagnostics"][0]["problem"])

    def test_check_passes_a_store_whose_rows_are_in_the_form(self) -> None:
        status, said = self.said_to_sessions("--check")

        self.assertEqual((0, []), (status, json.loads(said)["diagnostics"]))

    def test_a_call_it_does_not_know_prints_its_usage(self) -> None:
        status, said = self.said_to_sessions("--wake")

        self.assertEqual(2, status)
        self.assertIn("--end --session", said)


class TheGone(Hooked):
    """A row that reads ended for seven days is removed by a wake, since a chat the host reopens
    rarely comes later; a running row never is (the user, 2026-10-22)."""

    def rows(self) -> list[str]:
        return sorted(held.tag for held in sessions.rows(self.root)[0])

    def test_a_row_ended_eight_days_ago_is_removed_at_another_sessions_start(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-21T11:00Z q-0010\ns-beta running 2026-09-29T11:00Z q-0010\n")

        self.start("s-new")

        self.assertEqual(["s-beta", "s-new"], self.rows())
        self.assertFalse((self.root / sessions.ROWS / "s-old").exists())

    def test_a_row_ended_six_days_ago_is_kept(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-23T13:00Z q-0010\n")

        self.start("s-new")

        self.assertEqual(["s-new", "s-old"], self.rows())

    def test_a_row_ended_exactly_seven_days_ago_is_removed(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-22T12:00Z q-0010\n")

        self.start("s-new")

        self.assertEqual(["s-new"], self.rows())

    def test_a_running_row_is_never_removed_however_old(self) -> None:
        self.write(SESSIONS, "s-old running 2026-08-01 q-0010\n")
        self.seen_at("s-old", NOW - timedelta(minutes=5))

        self.start("s-new")

        self.assertEqual(["s-new", "s-old"], self.rows())

    def test_a_row_ended_at_this_wake_goes_at_a_later_one(self) -> None:
        self.write(SESSIONS, "s-old running 2026-08-01 q-0010\n")

        self.start("s-new")
        self.assertEqual("s-old ended 2026-08-01T00:00Z q-0010", self.line("s-old"), "ended at this wake, kept")

        self.start("s-newer")

        self.assertEqual(["s-new", "s-newer"], self.rows())

    def test_the_wake_says_nothing_of_a_removal(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-01 q-0010\n")

        said = self.context(self.start("s-new"))

        self.assertNotIn("s-old", said)

    def test_the_wake_by_hand_removes_as_the_hook_does(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-01 q-0010\n")

        self.said("--wake")

        self.assertNotIn("s-old", self.rows())

    def test_a_session_whose_row_is_gone_is_registered_anew_when_its_host_returns(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-01 q-0010\n")
        self.start("s-new")

        said = self.context(self.start("s-old", source="resume"))

        self.assertIn("session: s-old, registered now", said)
        self.assertIn("current: none yet", said)

    def test_a_row_another_wake_removed_meanwhile_is_nothing(self) -> None:
        self.write(SESSIONS, "s-old ended 2026-09-01 q-0010\n")
        sessions.folder(self.root)  # carried over, so the row's file exists to vanish
        (self.root / sessions.ROWS / "s-old").unlink()

        self.start("s-new")

        self.assertEqual(["s-new"], self.rows())

    def seen_at(self, tag: str, when: datetime) -> None:
        memory = sessions.memory(self.root, tag)
        memory.parent.mkdir(parents=True, exist_ok=True)
        if not memory.is_file():
            memory.write_text("drawn", encoding="utf-8")
        os.utime(memory, (when.timestamp(), when.timestamp()))

    def line(self, tag: str) -> str:
        return next(line for line in session_lines(self.root).splitlines() if line.startswith(f"{tag} "))

    def start(self, tag: str, source: str = "startup") -> str:
        _, said = self.hook("claude-code", {"session_id": tag, "hook_event_name": "SessionStart", "source": source})
        return said


class TheInstallersLine(unittest.TestCase):
    """What the hooks' wrapper hands the store's hook at a session's start is printed last."""

    def test_a_notice_from_the_environment_closes_the_wake_and_an_empty_one_leaves_it(self) -> None:
        with mock.patch.dict(os.environ, {"GW_NOTICE": " installed blocks: 1 thing out of step \n"}):
            self.assertEqual("the wake\n\ninstalled blocks: 1 thing out of step", questions._noticed("the wake"))
        with mock.patch.dict(os.environ, {"GW_NOTICE": ""}):
            self.assertEqual("the wake", questions._noticed("the wake"))


class AHeldUnit(Rendered):
    """A row may end with the unit its session holds, `holds <q-id>`, the question the unit
    answers; a row without it holds nothing. Every rebuild of a row keeps the field but the end."""

    HELD = "s-alpha running 2026-09-29T11:30Z q-0004 q-0002,q-0001 holds q-0004"

    def setUp(self) -> None:
        super().setUp()
        self.write(SESSIONS, f"{self.HELD}\ns-beta running 2026-09-29T11:00Z q-0010\n")

    def row(self, tag: str) -> sessions.Session:
        return next(each for each in sessions.rows(self.root)[0] if each.tag == tag)

    def line(self, tag: str) -> str:
        return next(line for line in session_lines(self.root).splitlines() if line.startswith(f"{tag} "))

    def problems(self) -> list[str]:
        """The rows' own diagnostics: this store keeps flat ids the store's check reports apart."""
        return [note.problem for note in sessions.check(self.root, sessions._index(self.root))[0]]

    def test_a_row_names_the_unit_it_holds_and_one_without_the_field_holds_nothing(self) -> None:
        self.assertEqual(("q-0004", None), (self.row("s-alpha").holds, self.row("s-beta").holds))

    def test_a_held_row_is_in_the_form_and_written_back_as_it_was_read(self) -> None:
        self.assertEqual([], self.problems())
        self.assertEqual(self.HELD, sessions.row_line(self.row("s-alpha")))

    def test_a_row_with_no_recent_questions_may_hold_a_unit(self) -> None:
        self.write(SESSIONS, "s-beta running 2026-09-29T11:00Z q-0010 holds q-0010\n")

        self.assertEqual("q-0010", self.row("s-beta").holds)
        self.assertEqual([], self.problems())

    def test_the_wakes_ending_of_a_silent_row_keeps_what_it_holds(self) -> None:
        sessions.tend(self.root, NOW + timedelta(hours=4), "s-new")

        self.assertEqual("s-alpha ended 2026-09-29T11:30Z q-0004 q-0002,q-0001 holds q-0004", self.line("s-alpha"))

    def test_a_sign_of_life_turning_an_ended_row_running_keeps_what_it_holds(self) -> None:
        sessions.tend(self.root, NOW + timedelta(hours=4), "s-new")

        sessions.seen(self.root, "s-alpha", NOW + timedelta(hours=5))

        self.assertTrue(self.row("s-alpha").running)
        self.assertEqual("q-0004", self.row("s-alpha").holds)

    def test_an_arrival_turning_an_ended_row_running_keeps_what_it_holds(self) -> None:
        sessions.tend(self.root, NOW + timedelta(hours=4), "s-new")

        arrived, _ = sessions.arrive(self.root, "s-alpha", NOW + timedelta(hours=5))

        self.assertEqual((True, "q-0004"), (arrived.running, self.row("s-alpha").holds))

    def test_a_move_keeps_what_the_row_holds(self) -> None:
        moved = sessions.moved(self.row("s-alpha"), "q-0003", NOW)

        self.assertEqual(("q-0003", "q-0004"), (moved.current, moved.holds))

    def test_a_rename_renames_the_held_unit(self) -> None:
        renamed = sessions.renamed(self.row("s-alpha"), {"q-0004": "q-0002.0001"})

        self.assertEqual("q-0002.0001", renamed.holds)

    def test_the_end_lets_the_unit_go(self) -> None:
        sessions.end(self.root, "s-alpha", NOW)

        self.assertEqual("s-alpha ended 2026-09-29T12:00Z q-0004 q-0002,q-0001", self.line("s-alpha"))

    def test_a_held_unit_naming_no_entry_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0099\n")

        self.assertTrue(any("q-0099" in problem for problem in self.problems()), self.problems())


class HoldingAndReleasing(Rendered):
    """`--hold` takes the unit a question's owner names into the session's row; `--release` lets it
    go. A refusal writes nothing and says why."""

    OWNER = "[01-0001 the-work](../tickets/01-0001-the-work.md)"

    def setUp(self) -> None:
        super().setUp()
        self.place("q-0004-which-parts-are-optional", "Which parts are optional?", {"part of": "q-0002", "state": "open", "owner": self.OWNER})

    def said_to_sessions(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = sessions.main(list(argv), root=self.root, now=NOW)
        return status, out.getvalue()

    def holds(self, tag: str) -> str | None:
        return next(each for each in sessions.rows(self.root)[0] if each.tag == tag).holds

    def assertRefusedWritingNothing(self, fragment: str, *argv: str) -> None:
        untouched = self.snapshot()

        status, said = self.said_to_sessions(*argv)

        self.assertEqual(2, status, said)
        self.assertIn(fragment, said)
        self.assertEqual(untouched, self.snapshot())

    def test_holding_an_open_question_with_an_owner_writes_it_into_the_row_and_names_the_owner(self) -> None:
        status, said = self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")

        self.assertEqual(0, status, said)
        self.assertEqual("q-0004", self.holds("s-alpha"))
        self.assertIn("01-0001", said)

    def test_holding_what_it_holds_already_writes_nothing(self) -> None:
        self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")
        untouched = self.snapshot()

        status, _ = self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")

        self.assertEqual((0, untouched), (status, self.snapshot()))

    def test_a_question_no_entry_holds_is_refused(self) -> None:
        self.assertRefusedWritingNothing("q-0099", "--hold", "q-0099", "--session", "s-alpha")

    def test_a_closed_question_is_refused(self) -> None:
        self.assertRefusedWritingNothing("closed", "--hold", "q-0005", "--session", "s-alpha")

    def test_a_question_with_no_owner_is_no_unit_and_refused(self) -> None:
        self.assertRefusedWritingNothing("owner", "--hold", "q-0003", "--session", "s-alpha")

    def test_a_unit_another_running_session_holds_is_refused_naming_that_session(self) -> None:
        self.said_to_sessions("--hold", "q-0004", "--session", "s-beta")

        self.assertRefusedWritingNothing("s-beta", "--hold", "q-0004", "--session", "s-alpha")

    def test_a_unit_an_ended_session_holds_is_free_to_take(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004\ns-beta ended 2026-09-29T11:00Z q-0010 holds q-0004\n")

        status, said = self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")

        self.assertEqual((0, "q-0004"), (status, self.holds("s-alpha")), said)

    def test_holding_a_second_unit_lets_the_first_go_and_says_which(self) -> None:
        self.place("q-0007-who-moves-a-subtree", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "owner": self.OWNER})
        self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")

        status, said = self.said_to_sessions("--hold", "q-0007", "--session", "s-alpha")

        self.assertEqual((0, "q-0007"), (status, self.holds("s-alpha")), said)
        self.assertIn("let go q-0004", said)

    def test_a_session_nobody_registered_is_refused(self) -> None:
        self.assertRefusedWritingNothing("--wake", "--hold", "q-0004", "--session", "s-nobody")

    def test_release_lets_the_unit_go_and_keeps_the_position(self) -> None:
        self.said_to_sessions("--hold", "q-0004", "--session", "s-alpha")

        status, _ = self.said_to_sessions("--release", "--session", "s-alpha")

        self.assertEqual((0, None), (status, self.holds("s-alpha")))
        self.assertIn("s-alpha running 2026-09-29T12:00Z q-0004 q-0002,q-0001\n", session_lines(self.root))

    def test_release_holding_nothing_writes_nothing(self) -> None:
        untouched = self.snapshot()

        status, _ = self.said_to_sessions("--release", "--session", "s-alpha")

        self.assertEqual((0, untouched), (status, self.snapshot()))


class TheHolderShown(Rendered):
    """The wake and the window name the unit each running session holds, and the owner of its
    question; the check finds a unit held under a closed question, and one held twice."""

    OWNER = "[01-0001 the-work](../tickets/01-0001-the-work.md)"

    def setUp(self) -> None:
        super().setUp()
        self.place("q-0004-which-parts-are-optional", "Which parts are optional?", {"part of": "q-0002", "state": "open", "owner": self.OWNER})
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 q-0002,q-0001 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")

    def findings(self) -> list[str]:
        return [note.finding for note in sessions.check(self.root, sessions._index(self.root))[1]]

    def test_the_wake_names_another_sessions_unit_and_its_owner(self) -> None:
        _, text = self.said("--wake", "--session", "s-beta")

        self.assertIn("at q-0004 (recent q-0002, q-0001), holding q-0004 (01-0001 the-work)", self.section(text, "sessions:"))

    def test_the_window_names_another_sessions_unit_and_its_owner(self) -> None:
        _, text = self.said("--window", "--session", "s-beta")

        self.assertIn("holding q-0004 (01-0001 the-work)", self.section(text, "other running sessions:"))

    def test_a_sessions_own_window_names_the_unit_it_holds(self) -> None:
        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("holding: q-0004 (01-0001 the-work)", text)

    def test_a_session_holding_nothing_is_shown_holding_nothing(self) -> None:
        _, text = self.said("--window", "--session", "s-beta")

        self.assertNotIn("holding:", text)
        self.assertNotIn("holding", self.section(self.said("--window", "--session", "s-alpha")[1], "other running sessions:"))

    def test_a_unit_under_a_closed_question_holds_nobody_and_is_a_finding(self) -> None:
        self.place("q-0004-which-parts-are-optional", "Which parts are optional?", {"part of": "q-0002", "state": "closed:moot", "answer": "gone", "owner": self.OWNER})

        _, text = self.said("--window", "--session", "s-beta")

        self.assertNotIn("holding", self.section(text, "other running sessions:"))
        self.assertTrue(any("s-alpha" in found and "closed" in found and "holds" in found for found in self.findings()), self.findings())

    def test_one_unit_held_by_two_running_sessions_is_a_finding_naming_both(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010 holds q-0004\n")

        twice = [found for found in self.findings() if "s-alpha" in found and "s-beta" in found]

        self.assertTrue(twice, self.findings())

    def test_an_ended_session_holding_a_closed_unit_is_no_finding(self) -> None:
        self.write(SESSIONS, "s-alpha ended 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")
        self.place("q-0004-which-parts-are-optional", "Which parts are optional?", {"part of": "q-0002", "state": "closed:moot", "answer": "gone", "owner": self.OWNER})

        self.assertEqual([], [found for found in self.findings() if "holds" in found])


class TakingOver(Rendered):
    """`--take` moves a unit another running session holds into this session's row, by the
    person's word, and leaves in the holder's row `taken <q-id> by <tag>` where `holds` stood."""

    OWNER = "[01-0001 the-work](../tickets/01-0001-the-work.md)"

    def setUp(self) -> None:
        super().setUp()
        self.place("q-0004-which-parts-are-optional", "Which parts are optional?", {"part of": "q-0002", "state": "open", "owner": self.OWNER})
        self.place("q-0007-who-moves-a-subtree", "Who moves a subtree?", {"part of": "q-0003", "state": "open", "owner": self.OWNER})
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")

    def said_to_sessions(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = sessions.main(list(argv), root=self.root, now=NOW)
        return status, out.getvalue()

    def line(self, tag: str) -> str:
        return next(line for line in session_lines(self.root).splitlines() if line.startswith(f"{tag} "))

    def problems(self) -> list[str]:
        return [note.problem for note in sessions.check(self.root, sessions._index(self.root))[0]]

    def assertRefusedWritingNothing(self, fragment: str, *argv: str) -> None:
        untouched = self.snapshot()

        status, said = self.said_to_sessions(*argv)

        self.assertEqual(2, status, said)
        self.assertIn(fragment, said)
        self.assertEqual(untouched, self.snapshot())

    def test_a_takeover_moves_the_unit_and_leaves_the_holder_the_mark_of_who_took_it(self) -> None:
        status, said = self.said_to_sessions("--take", "q-0004", "--session", "s-beta")

        self.assertEqual(0, status, said)
        self.assertEqual("s-alpha running 2026-09-29T11:30Z q-0004 taken q-0004 by s-beta", self.line("s-alpha"))
        self.assertTrue(self.line("s-beta").endswith(" holds q-0004"), self.line("s-beta"))
        self.assertIn("s-alpha", said)
        self.assertEqual([], self.problems())

    def test_the_holders_window_shows_who_took_its_unit(self) -> None:
        self.said_to_sessions("--take", "q-0004", "--session", "s-beta")

        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("taken: q-0004 by s-beta", text)
        self.assertNotIn("holding:", text)

    def test_a_takeover_after_the_holders_last_window_draws_its_next_one_whole(self) -> None:
        self.said("--window", "--session", "s-alpha")
        self.said_to_sessions("--take", "q-0004", "--session", "s-beta")

        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("taken: q-0004 by s-beta", text)

    def test_another_sessions_hold_after_a_window_draws_the_next_one_whole(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")
        self.said("--window", "--session", "s-alpha")
        self.said_to_sessions("--hold", "q-0007", "--session", "s-beta")

        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("holding q-0007", text)

    def test_another_sessions_move_alone_still_leaves_the_window_unchanged(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")
        self.said("--window", "--session", "s-alpha")
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:40Z q-0003 q-0010\n")

        _, text = self.said("--window", "--session", "s-alpha")

        self.assertIn("window unchanged since your last one", text)

    def test_the_holders_next_hold_release_or_end_clears_the_mark(self) -> None:
        for argv in (("--hold", "q-0007", "--session", "s-alpha"), ("--release", "--session", "s-alpha"), ("--end", "--session", "s-alpha")):
            with self.subTest(argv=argv[0]):
                self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 taken q-0004 by s-beta\ns-beta running 2026-09-29T11:00Z q-0010 holds q-0004\n")

                status, said = self.said_to_sessions(*argv)

                self.assertEqual(0, status, said)
                self.assertNotIn("taken", self.line("s-alpha"))

    def test_every_rebuild_keeps_the_mark_and_a_rename_rewrites_it(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 taken q-0004 by s-beta\ns-beta running 2026-09-29T11:00Z q-0010 holds q-0004\n")
        alpha = next(each for each in sessions.rows(self.root)[0] if each.tag == "s-alpha")

        self.assertEqual(("q-0004", "s-beta"), (sessions.moved(alpha, "q-0003", NOW).taken, sessions.moved(alpha, "q-0003", NOW).taken_by))
        self.assertEqual("q-0002.0001", sessions.renamed(alpha, {"q-0004": "q-0002.0001"}).taken)
        sessions.tend(self.root, NOW + timedelta(hours=4), "s-new")
        self.assertTrue(self.line("s-alpha").endswith(" taken q-0004 by s-beta"), self.line("s-alpha"))
        sessions.seen(self.root, "s-alpha", NOW + timedelta(hours=5))
        self.assertTrue(self.line("s-alpha").endswith(" taken q-0004 by s-beta"), self.line("s-alpha"))
        sessions.tend(self.root, NOW + timedelta(hours=9), "s-new")
        sessions.arrive(self.root, "s-alpha", NOW + timedelta(hours=10))
        self.assertTrue(self.line("s-alpha").endswith(" taken q-0004 by s-beta"), self.line("s-alpha"))

    def test_taking_over_what_this_session_holds_already_is_refused(self) -> None:
        self.assertRefusedWritingNothing("already", "--take", "q-0004", "--session", "s-alpha")

    def test_a_takeover_marks_an_ended_row_still_naming_the_unit(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\ns-gamma ended 2026-09-29T10:00Z q-0004 holds q-0004\n")

        status, said = self.said_to_sessions("--take", "q-0004", "--session", "s-beta")

        self.assertEqual(0, status, said)
        self.assertEqual("s-gamma ended 2026-09-29T10:00Z q-0004 taken q-0004 by s-beta", self.line("s-gamma"))

    def test_a_mark_naming_no_entry_is_reported(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 taken q-0099 by s-beta\n")

        self.assertTrue(any("q-0099" in problem for problem in self.problems()), self.problems())

    def test_a_unit_no_running_session_holds_is_refused_naming_the_hold(self) -> None:
        self.assertRefusedWritingNothing("--hold", "--take", "q-0007", "--session", "s-beta")

    def test_a_question_that_is_no_unit_is_refused(self) -> None:
        self.assertRefusedWritingNothing("owner", "--take", "q-0003", "--session", "s-beta")

    def test_a_takeover_lets_the_takers_own_unit_go_and_says_which(self) -> None:
        self.write(SESSIONS, "s-alpha running 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010 holds q-0007\n")

        status, said = self.said_to_sessions("--take", "q-0004", "--session", "s-beta")

        self.assertEqual(0, status, said)
        self.assertTrue(self.line("s-beta").endswith(" holds q-0004"), self.line("s-beta"))
        self.assertIn("let go q-0007", said)
        self.assertNotIn("q-0007", self.line("s-alpha") + self.line("s-beta"))

    def test_holding_a_unit_an_ended_row_still_names_marks_that_row_taken(self) -> None:
        self.write(SESSIONS, "s-alpha ended 2026-09-29T11:30Z q-0004 holds q-0004\ns-beta running 2026-09-29T11:00Z q-0010\n")

        status, said = self.said_to_sessions("--hold", "q-0004", "--session", "s-beta")

        self.assertEqual(0, status, said)
        self.assertEqual("s-alpha ended 2026-09-29T11:30Z q-0004 taken q-0004 by s-beta", self.line("s-alpha"))

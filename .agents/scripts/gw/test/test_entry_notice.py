# Mechanism: harness
"""What a running session is shown of an entry file that changed under it."""

from __future__ import annotations

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
from unittest import mock

from repository import SCRIPTS, RepositoryCase, proves_a_process

import entry_notice
import sessions

DESKTOP_ID = "CLAUDE_CODE_HOST_SESSION_ID"

ENTRY = """\
# Entry contract

Entry contract: v1, 2026-01-01.

## General rules

- **Occam.** Take the shape with the fewest parts.
- **Two readers.** Write for a capable model.

## Autonomy

- Below the dial the agent acts on its own.
"""


class TheEntryFileUnderASession(RepositoryCase):
    """A session's context takes the file in, the file changes, and a message asks what changed."""

    def setUp(self) -> None:
        super().setUp()
        memory = tempfile.TemporaryDirectory()
        self.addCleanup(memory.cleanup)
        self.enterContext(mock.patch.object(sessions, "WINDOW_MEMORY", memory.name))
        self.write("AGENTS.md", ENTRY)
        entry_notice.taken_in(self.root, "s-alpha")

    def rewrite(self, old: str, new: str) -> None:
        text = self.read("AGENTS.md")
        self.assertIn(old, text)
        self.write("AGENTS.md", text.replace(old, new))

    def message(self, tag: str = "s-alpha") -> str:
        return entry_notice.changed(self.root, tag)

    def test_a_message_after_a_change_gives_the_changed_line_as_it_was_and_as_it_is_now(self) -> None:
        self.rewrite("fewest parts.", "fewest parts that does the job.")

        self.assertEqual(
            "entry file changed: AGENTS.md differs from the text your context holds — 1 passage, below as it "
            "was and as it is now. Read `was` as replaced by `now`; the rest of the file stands as your context "
            "holds it. Where this text is cut short, its whole stands at the head of the output the host saved: "
            "read it there, or read AGENTS.md again.\n"
            "\n"
            "1. under `## General rules`\n"
            "was:\n"
            "- **Occam.** Take the shape with the fewest parts.\n"
            "now:\n"
            "- **Occam.** Take the shape with the fewest parts that does the job.",
            self.message(),
        )

    def test_an_unchanged_file_gives_nothing(self) -> None:
        self.assertEqual("", self.message())

    def test_a_change_is_given_once_and_the_following_message_gives_nothing(self) -> None:
        self.rewrite("fewest parts.", "fewest parts that does the job.")

        first, second = self.message(), self.message()

        self.assertIn("1 passage", first)
        self.assertEqual("", second)

    def test_several_changes_between_two_messages_are_one_notice_of_what_differs_now(self) -> None:
        self.rewrite("v1, 2026-01-01", "v2, 2026-01-02")
        self.rewrite("fewest parts.", "fewest parts that does the job.")
        self.rewrite("v2, 2026-01-02", "v3, 2026-01-03")

        said = self.message()

        self.assertIn("2 passages, each below as it was and as it is now", said)
        self.assertIn("1. under `# Entry contract`\nwas:\nEntry contract: v1, 2026-01-01.\nnow:\nEntry contract: v3, 2026-01-03.", said)
        self.assertIn("2. under `## General rules`\nwas:\n- **Occam.** Take the shape with the fewest parts.\nnow:", said)
        self.assertNotIn("v2", said)

    def test_a_change_undone_before_the_next_message_gives_nothing(self) -> None:
        self.rewrite("fewest parts.", "fewest parts that does the job.")
        self.rewrite("fewest parts that does the job.", "fewest parts.")

        self.assertEqual("", self.message())

    def test_a_context_that_took_the_file_in_anew_after_a_change_is_given_nothing_of_it(self) -> None:
        self.rewrite("fewest parts.", "fewest parts that does the job.")
        entry_notice.taken_in(self.root, "s-alpha")

        self.assertEqual("", self.message())

    def test_each_session_is_given_the_change_by_what_its_own_context_holds(self) -> None:
        self.rewrite("v1, 2026-01-01", "v2, 2026-01-02")
        entry_notice.taken_in(self.root, "s-beta")
        self.rewrite("fewest parts.", "fewest parts that does the job.")

        self.assertIn("2 passages", self.message("s-alpha"))
        self.assertIn("1 passage,", self.message("s-beta"))

    def test_a_session_whose_start_no_hook_saw_is_given_nothing_until_the_file_changes_after_its_first_message(self) -> None:
        self.rewrite("fewest parts.", "fewest parts that does the job.")

        first = self.message("s-unseen")
        self.rewrite("capable model.", "capable model: the rule and its pointer.")
        second = self.message("s-unseen")

        self.assertEqual("", first)
        self.assertIn("1 passage,", second)
        self.assertIn("now:\n- **Two readers.** Write for a capable model: the rule and its pointer.", second)

    def test_a_tree_with_no_entry_file_gives_nothing(self) -> None:
        (self.root / "AGENTS.md").unlink()

        self.assertEqual("", self.message())
        entry_notice.taken_in(self.root, "s-gamma")
        self.assertEqual("", self.message("s-gamma"))

    def test_a_new_passage_names_the_line_it_follows_and_has_no_was(self) -> None:
        self.rewrite(
            "- Below the dial the agent acts on its own.\n",
            "- Below the dial the agent acts on its own.\n- ✋ At the dial it shows the person before acting.\n",
        )

        self.assertTrue(
            self.message().endswith(
                "\n\n1. under `## Autonomy`, new after `- Below the dial the agent acts on its own.`\n"
                "now:\n- ✋ At the dial it shows the person before acting."
            )
        )

    def test_the_line_a_new_passage_follows_is_the_nearest_with_text_cut_where_it_runs_long(self) -> None:
        long = "- **Two readers.** " + "Write for a capable model. " * 6
        self.rewrite("- **Two readers.** Write for a capable model.\n", f"{long}\n")
        entry_notice.taken_in(self.root, "s-alpha")
        self.rewrite("\n## Autonomy", "\n- **Recency.** Evidence by recency.\n\n## Autonomy")

        said = self.message()

        self.assertIn(f"1. under `## General rules`, new after `{long[:79]}…`\nnow:\n", said)

    def test_a_new_passage_right_under_its_heading_names_the_heading_once(self) -> None:
        self.rewrite("## Autonomy\n", "## Autonomy\n\nAutonomy is a dial on a ladder.\n")

        self.assertTrue(self.message().endswith("\n\n1. under `## Autonomy`, new\nnow:\nAutonomy is a dial on a ladder."))

    def test_a_comment_inside_a_code_fence_is_no_heading(self) -> None:
        fenced = "```\n# the checks, run before a commit\nuv run check\n```\n"
        self.rewrite("\n## Autonomy", f"\n{fenced}\n## Autonomy")
        entry_notice.taken_in(self.root, "s-alpha")
        self.rewrite("uv run check", "uv run check --all")

        self.assertIn("1. under `## General rules`\nwas:\nuv run check\nnow:\nuv run check --all", self.message())

    def test_a_removed_passage_says_so_and_has_no_now(self) -> None:
        self.rewrite("- **Two readers.** Write for a capable model.\n", "")

        self.assertTrue(
            self.message().endswith(
                "\n\n1. under `## General rules`, removed\nwas:\n- **Two readers.** Write for a capable model."
            )
        )

    def test_a_passage_above_every_heading_is_placed_at_the_files_head(self) -> None:
        self.rewrite("# Entry contract\n", "# Entry file\n")

        self.assertIn("1. at the file's head\nwas:\n# Entry contract\nnow:\n# Entry file", self.message())

    def test_line_endings_alone_are_no_change(self) -> None:
        (self.root / "AGENTS.md").write_bytes(ENTRY.replace("\n", "\r\n").encode("utf-8"))

        self.assertEqual("", self.message())

    def test_blank_lines_alone_are_no_change_and_one_beside_a_changed_line_is_not_shown(self) -> None:
        self.rewrite("\n## Autonomy", "\n\n\n## Autonomy")
        blank_only = self.message()
        self.rewrite("- Below the dial the agent acts on its own.\n", "\n- Below the dial the agent settles and acts.\n\n")

        self.assertEqual("", blank_only)
        self.assertTrue(
            self.message().endswith(
                "was:\n- Below the dial the agent acts on its own.\nnow:\n- Below the dial the agent settles and acts."
            )
        )

    def test_past_its_budget_the_notice_carries_no_lines_and_asks_for_a_read(self) -> None:
        rules = "".join(f"- **Rule {number}.** {'It holds. ' * 40}\n" for number in range(12))
        self.rewrite("- **Occam.** Take the shape with the fewest parts.\n", rules)
        entry_notice.taken_in(self.root, "s-alpha")
        self.rewrite("It holds. ", "It stands. ")

        self.assertEqual(
            "entry file changed: AGENTS.md differs from the text your context holds in 1 passage, too many lines "
            "to show here. Read AGENTS.md again; it replaces the text your context holds.",
            self.message(),
        )
        self.assertEqual("", self.message())


class TheHookLine(RepositoryCase):
    """The line as the hooks' wrapper runs it: a host's payload in, the notice or nothing out."""

    def setUp(self) -> None:
        super().setUp()
        memory = tempfile.TemporaryDirectory()
        self.addCleanup(memory.cleanup)
        self.enterContext(mock.patch.object(sessions, "WINDOW_MEMORY", memory.name))
        self.enterContext(mock.patch.dict(os.environ))
        os.environ.pop(DESKTOP_ID, None)
        self.write("AGENTS.md", ENTRY)

    def line(self, host: str, payload: dict | str) -> tuple[int, str]:
        stdin = io.StringIO(payload if isinstance(payload, str) else json.dumps(payload))
        out = io.StringIO()
        with contextlib.redirect_stdout(out), mock.patch("sys.stdin", stdin):
            status = entry_notice.main(["--hook", host], root=self.root)
        return status, out.getvalue()

    def change(self) -> None:
        self.write("AGENTS.md", self.read("AGENTS.md").replace("fewest parts.", "fewest parts that does the job."))

    def test_a_message_after_a_change_prints_the_notice_and_the_next_prints_nothing(self) -> None:
        self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "startup"})
        self.change()

        first = self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"})
        second = self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"})

        self.assertEqual(0, first[0])
        self.assertTrue(first[1].startswith("entry file changed: AGENTS.md differs"), first[1])
        self.assertTrue(first[1].endswith("now:\n- **Occam.** Take the shape with the fewest parts that does the job.\n"))
        self.assertEqual((0, ""), second)

    def test_a_start_prints_nothing_whatever_its_source_and_takes_the_file_in_as_it_stands(self) -> None:
        for source in ("startup", "resume", "clear", "compact"):
            with self.subTest(source=source):
                self.write("AGENTS.md", ENTRY)
                self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "startup"})
                self.change()

                started = self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": source})
                messaged = self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"})

                self.assertEqual(((0, ""), (0, "")), (started, messaged))

    def test_a_hosts_compaction_event_takes_the_file_in_as_it_stands(self) -> None:
        self.line("codex", {"session_id": "s-alpha", "hook_event_name": "SessionStart"})
        self.change()

        compacted = self.line("codex", {"session_id": "s-alpha", "hook_event_name": "PostCompact"})
        messaged = self.line("codex", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"})

        self.assertEqual(((0, ""), (0, "")), (compacted, messaged))

    def test_a_host_whose_message_reaches_no_agent_is_printed_nothing_and_keeps_its_memory(self) -> None:
        self.line("cursor", {"conversation_id": "c-1", "hook_event_name": "sessionStart"})
        self.change()

        signed = self.line("cursor", {"conversation_id": "c-1", "hook_event_name": "beforeSubmitPrompt"})

        self.assertEqual((0, ""), signed)
        self.assertIn("1 passage", entry_notice.changed(self.root, "c-1"))

    def test_the_session_is_the_one_the_stores_hook_reads_the_conversation_variable_first(self) -> None:
        os.environ[DESKTOP_ID] = "local_1"
        self.line("claude-code", {"session_id": "before-resume", "hook_event_name": "SessionStart", "source": "startup"})
        self.change()

        _, said = self.line("claude-code", {"session_id": "after-resume", "hook_event_name": "UserPromptSubmit"})

        self.assertIn("1 passage", said)

    def test_a_payload_is_read_as_the_stores_hook_reads_it_by_its_byte_order_mark(self) -> None:
        sent = json.dumps({"session_id": "s-16", "hook_event_name": "SessionStart"})
        with mock.patch("sys.stdin", io.TextIOWrapper(io.BytesIO(sent.encode("utf-16")))):
            entry_notice.main(["--hook", "claude-code"], root=self.root)
        self.change()

        self.assertIn("1 passage", entry_notice.changed(self.root, "s-16"))

    def test_what_it_cannot_read_prints_nothing_and_exits_clean(self) -> None:
        for host, payload in (
            ("claude-code", "not json"),
            ("nohost", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"}),
            ("claude-code", {"hook_event_name": "UserPromptSubmit"}),
            ("claude-code", {"session_id": "s-alpha", "hook_event_name": "PreToolUse"}),
        ):
            with self.subTest(host=host, payload=payload):
                self.assertEqual((0, ""), self.line(host, payload))

    def test_a_memory_that_cannot_be_written_prints_nothing_and_exits_clean(self) -> None:
        self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "SessionStart", "source": "startup"})
        self.change()

        with mock.patch.object(entry_notice.os, "replace", side_effect=OSError("read-only")):
            answered = self.line("claude-code", {"session_id": "s-alpha", "hook_event_name": "UserPromptSubmit"})

        self.assertEqual((0, ""), answered)

    @proves_a_process
    def test_as_a_process_it_writes_utf_8_and_bare_line_ends_whatever_the_console(self) -> None:
        """The wrapper hands on what it captured byte for byte: a console's code page would lose
        the entry file's glyphs, and a carriage return would end every line the agent reads."""
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        environment = {**os.environ, "TMP": temp.name, "TEMP": temp.name, "TMPDIR": temp.name, "PYTHONIOENCODING": "cp1252"}

        def run(event: str) -> subprocess.CompletedProcess:
            return subprocess.run(
                [sys.executable, str(SCRIPTS / "entry_notice.py"), "--hook", "codex"], cwd=self.root, env=environment,
                input=json.dumps({"session_id": "s-alpha", "hook_event_name": event}).encode(), capture_output=True,
            )

        run("SessionStart")
        self.write("AGENTS.md", self.read("AGENTS.md").replace("fewest parts.", "fewest parts ✋ — так."))
        messaged = run("UserPromptSubmit")

        self.assertEqual((0, b""), (messaged.returncode, messaged.stderr))
        self.assertTrue(messaged.stdout.decode("utf-8").endswith("fewest parts ✋ — так.\n"), messaged.stdout)
        self.assertNotIn(b"\r", messaged.stdout)

    def test_anything_but_the_hook_is_a_usage_error(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()) as said:
            status = entry_notice.main(["--window"], root=self.root)

        self.assertEqual(2, status)
        self.assertIn("usage: entry_notice.py --hook <host>", said.getvalue())

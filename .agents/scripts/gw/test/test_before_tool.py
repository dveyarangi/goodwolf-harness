# Mechanism: harness
"""What a host's call before a tool is answered with, in a tree that lists files closed to agents."""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
from unittest import mock

from repository import SCRIPTS, RepositoryCase

import before_tool
import harness

LISTED = "config/secrets.yml"


class Calls(RepositoryCase):
    """A tree whose list closes one file, and the answers Claude Code's calls get there."""

    def setUp(self) -> None:
        super().setUp()
        self.write(before_tool.LIST, f"{LISTED}\n")
        self.write(LISTED, "token: fake\n")

    def answer(self, tool: str, **tool_input: object) -> tuple[int, str]:
        """The script's exit and what it printed for one call, as the host would hand it."""
        payload = {"hook_event_name": "PreToolUse", "cwd": str(self.root), "tool_name": tool, "tool_input": tool_input}
        return self.answer_to(json.dumps(payload))

    def answer_to(self, text: str) -> tuple[int, str]:
        out = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(text)), contextlib.redirect_stdout(out):
            status = before_tool.main(["--hook", "claude-code"], self.root)
        return status, out.getvalue()

    def assertRefused(self, tool: str, **tool_input: object) -> str:
        status, said = self.answer(tool, **tool_input)
        self.assertEqual(0, status)
        decision = json.loads(said)["hookSpecificOutput"]
        self.assertEqual(("PreToolUse", "deny"), (decision["hookEventName"], decision["permissionDecision"]))
        return decision["permissionDecisionReason"]

    def assertPassed(self, tool: str, **tool_input: object) -> None:
        self.assertEqual((0, ""), self.answer(tool, **tool_input))


class AFileTool(Calls):
    def test_a_read_of_a_listed_file_is_refused_and_the_reason_names_the_file_and_the_list(self) -> None:
        reason = self.assertRefused("Read", file_path=str(self.root / "config" / "secrets.yml"))

        self.assertIn(LISTED, reason)
        self.assertIn(before_tool.LIST, reason)

    def test_a_change_of_a_listed_file_is_refused_by_every_tool_that_writes(self) -> None:
        path = str(self.root / "config" / "secrets.yml")

        self.assertRefused("Edit", file_path=path, old_string="token", new_string="key")
        self.assertRefused("Write", file_path=path, content="x")
        self.assertRefused("NotebookEdit", notebook_path=path, new_source="x")

    def test_a_file_the_list_does_not_name_passes_though_it_bears_the_same_name_elsewhere(self) -> None:
        self.assertPassed("Read", file_path=str(self.root / "docs" / "notes.md"))
        self.assertPassed("Read", file_path=str(self.root / "other" / "secrets.yml"))

    def test_the_path_is_compared_without_case_and_with_either_separator(self) -> None:
        whole = str(self.root / "config" / "secrets.yml")

        self.assertRefused("Read", file_path=whole.upper())
        self.assertRefused("Read", file_path=whole.replace("/", chr(92)))
        self.assertRefused("Read", file_path=whole.replace(chr(92), "/"))

    def test_a_path_is_made_whole_against_the_calls_own_folder(self) -> None:
        status, said = self.answer_to(json.dumps({
            "cwd": str(self.root / "config"), "tool_name": "Read", "tool_input": {"file_path": "secrets.yml"},
        }))

        self.assertEqual(0, status)
        self.assertIn("deny", said)

    def test_text_that_only_mentions_a_listed_file_is_written_freely(self) -> None:
        notes = str(self.root / "docs" / "notes.md")

        self.assertPassed("Write", file_path=notes, content=f"The keys live in {LISTED}.")
        self.assertPassed("Edit", file_path=notes, old_string="x", new_string=f"see {LISTED}")

    def test_a_tree_that_keeps_no_list_answers_nothing(self) -> None:
        (self.root / before_tool.LIST).unlink()

        self.assertPassed("Read", file_path=str(self.root / "config" / "secrets.yml"))


class AShellCommand(Calls):
    def test_a_command_that_holds_the_listed_path_is_refused_in_either_shell(self) -> None:
        self.assertRefused("Bash", command=f"cat {LISTED}")
        self.assertRefused("PowerShell", command="Get-Content config" + chr(92) + "secrets.yml")

    def test_a_command_that_holds_only_the_files_name_is_refused(self) -> None:
        self.assertRefused("Bash", command="cd config && cat secrets.yml")
        self.assertRefused("Bash", command='grep -v token "SECRETS.YML" | head')

    def test_a_name_inside_a_longer_name_is_another_file(self) -> None:
        self.write(before_tool.LIST, ".env\n")

        self.assertRefused("Bash", command="cat .env")
        self.assertRefused("Bash", command="source ./.env; run")
        self.assertPassed("Bash", command="cat .env.example")
        self.assertPassed("Bash", command="cat prod.env")

    def test_a_command_that_names_nothing_listed_passes(self) -> None:
        self.assertPassed("Bash", command="git status && ls config")


class ASearch(Calls):
    def test_a_search_whose_path_or_plain_glob_names_the_file_is_refused(self) -> None:
        self.assertRefused("Grep", pattern="token", path=LISTED)
        self.assertRefused("Grep", pattern="token", glob=LISTED)
        self.assertRefused("Glob", pattern=LISTED)

    def test_a_search_over_a_folder_and_a_pattern_that_merely_matches_pass(self) -> None:
        self.assertPassed("Grep", pattern="token")
        self.assertPassed("Grep", pattern="token", path="config")
        self.assertPassed("Grep", pattern="token", glob="*.yml")
        self.assertPassed("Glob", pattern="config/*.yml")

    def test_a_search_for_text_that_mentions_the_file_passes(self) -> None:
        self.assertPassed("Grep", pattern="secrets.yml")


class AToolTheScriptDoesNotKnow(Calls):
    def test_a_string_that_is_the_listed_path_is_refused_whatever_its_field(self) -> None:
        self.assertRefused("mcp__files__read", target=str(self.root / "config" / "secrets.yml"))
        self.assertRefused("mcp__files__read_many", targets=[{"uri": LISTED}])

    def test_a_field_named_command_is_read_as_a_shell_command(self) -> None:
        self.assertRefused("mcp__shell__run", command="cat secrets.yml")

    def test_text_that_mentions_a_listed_file_is_no_call_upon_it(self) -> None:
        self.assertPassed("Agent", prompt=f"Ask the person about {LISTED}.", subagent_type="general-purpose")
        self.assertPassed("mcp__plan__update", items=[{"content": f"Ask about {LISTED}"}])


class TheList(Calls):
    def test_reads_a_path_however_an_editor_or_a_platform_wrote_its_line(self) -> None:
        cr, back = chr(13), chr(92)
        lines = [
            chr(0xFEFF) + "# the files that still hold secrets",
            "",
            "config/secrets.yml",
            "  ./deploy/keys.json  ",
            "/root.env",
            "legacy" + back + "settings.py",
        ]
        (self.root / before_tool.LIST).write_bytes((cr + chr(10)).join(lines).encode("utf-8"))

        self.assertEqual(
            ["config/secrets.yml", "deploy/keys.json", "root.env", "legacy/settings.py"],
            before_tool.listed(self.root),
        )

    def test_a_tree_with_no_list_lists_nothing(self) -> None:
        (self.root / before_tool.LIST).unlink()

        self.assertEqual([], before_tool.listed(self.root))


class WhereItCannotDecide(Calls):
    def test_a_payload_it_cannot_read_is_a_failure_and_never_a_silent_pass(self) -> None:
        for payload in ("", "{not json", "[]", json.dumps({"tool_name": "Read"})):
            with self.subTest(payload=payload), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual((1, ""), self.answer_to(payload))

    def test_a_host_it_does_not_know_is_a_failure(self) -> None:
        with mock.patch("sys.stdin", io.StringIO("{}")), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(2, before_tool.main(["--hook", "another-host"], self.root))
            self.assertEqual(2, before_tool.main([], self.root))

    def test_a_tree_whose_list_is_gone_reads_no_payload(self) -> None:
        (self.root / before_tool.LIST).unlink()

        self.assertEqual((0, ""), self.answer_to("{not json"))


class TheStartsLine(Calls):
    """What a session's start is told of a list whose refusal the host is not set to hold."""

    ENTRY = {"hooks": [{"type": "command", "command": "git -c alias.x=!y gw-hook claude-code before-tool"}]}

    def line(self) -> str:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(0, before_tool.main(["--line", "claude-code"], self.root))
        return out.getvalue()

    def wire(self, *rules: str, entry: bool = True) -> None:
        settings = {"permissions": {"deny": list(rules)}, "hooks": {"PreToolUse": [self.ENTRY] if entry else []}}
        self.write(".claude/settings.json", json.dumps(settings))

    def test_a_list_with_its_entry_and_a_rule_for_every_line_says_nothing(self) -> None:
        self.wire(f"Read(/{LISTED})")

        self.assertEqual("", self.line())

    def test_a_list_the_host_has_no_entry_for_is_said_with_the_step_that_wires_it(self) -> None:
        for wired in (lambda: None, lambda: self.wire(f"Read(/{LISTED})", entry=False)):
            wired()
            with self.subTest():
                said = self.line()
                self.assertIn(before_tool.LIST, said)
                self.assertIn("--update", said)
                self.assertEqual(1, said.count(chr(10)))

    def test_a_line_of_the_list_with_no_rule_is_named(self) -> None:
        self.write(before_tool.LIST, f"{LISTED}\ndeploy/keys.json\n")
        self.wire(f"Read(/{LISTED})")

        self.assertIn("deploy/keys.json", self.line())
        self.assertNotIn(LISTED, self.line())

    def test_a_tree_with_no_list_says_nothing(self) -> None:
        (self.root / before_tool.LIST).unlink()

        self.assertEqual("", self.line())

    def test_a_host_file_it_cannot_read_is_said_as_not_wired(self) -> None:
        self.write(".claude/settings.json", "{not json")

        self.assertIn(before_tool.LIST, self.line())


HOOK_COMMAND = 'git -c "alias.gw-hook=!sh .agents/scripts/gw/hook.sh" gw-hook'
NOTICING_STORE = "import os, sys\nprint('noticed', ascii(os.environ.get('GW_NOTICE', '')))\n"


class ThroughTheWrapper(RepositoryCase):
    """The call before a tool as a host makes it: through Git's alias and the hooks' wrapper, the
    real script behind it, from wherever the host's shell stands in the tree."""

    proves_a_process = True

    def setUp(self) -> None:
        super().setUp()
        for script in ("hook.sh", "before_tool.py"):
            self.write(f".agents/scripts/gw/{script}", (SCRIPTS / script).read_text(encoding="utf-8"))
        self.write(before_tool.LIST, f"{LISTED}\n")
        (self.root / "sub").mkdir()

    def call(self, payload: object, host: str = "claude-code") -> subprocess.CompletedProcess:
        text = payload if isinstance(payload, str) else json.dumps(payload)
        return subprocess.run(
            f"{HOOK_COMMAND} {host} before-tool", shell=True, cwd=self.root / "sub", input=text,
            capture_output=True, encoding="utf-8",
        )

    def record_the_interpreter(self) -> None:
        (self.root / ".git" / harness.INTERPRETER_RECORD).write_text(f"{sys.executable}\n", encoding="utf-8")

    def refusal(self, done: subprocess.CompletedProcess) -> str:
        self.assertEqual(0, done.returncode, done.stderr)
        decision = json.loads(done.stdout)["hookSpecificOutput"]
        self.assertEqual("deny", decision["permissionDecision"])
        return decision["permissionDecisionReason"]

    def reading(self, name: str) -> dict:
        return {"cwd": str(self.root), "tool_name": "Read", "tool_input": {"file_path": str(self.root / name)}}

    def test_a_call_that_names_a_listed_file_is_refused_and_another_passes(self) -> None:
        self.record_the_interpreter()

        self.assertIn(LISTED, self.refusal(self.call(self.reading(LISTED))))
        passed = self.call(self.reading("docs/notes.md"))
        self.assertEqual((0, ""), (passed.returncode, passed.stdout))

    def test_a_tree_whose_list_is_gone_leaves_at_once_with_no_interpreter_asked_for(self) -> None:
        (self.root / before_tool.LIST).unlink()

        done = self.call(self.reading(LISTED))

        self.assertEqual((0, ""), (done.returncode, done.stdout))

    def test_a_clone_with_no_interpreter_refuses_every_call_and_names_the_step_that_mends_it(self) -> None:
        reason = self.refusal(self.call(self.reading("docs/notes.md")))

        self.assertIn("--links", reason)

    def test_a_check_that_fails_refuses_the_call(self) -> None:
        self.record_the_interpreter()

        self.assertIn("could not", self.refusal(self.call("{not json")))

    def test_a_host_with_no_known_form_of_refusal_is_stopped_by_the_exit(self) -> None:
        done = self.call(self.reading("docs/notes.md"), host="another-host")

        self.assertEqual((2, ""), (done.returncode, done.stdout))
        self.assertIn("--links", done.stderr)

    def test_the_wrapper_and_the_script_name_one_list(self) -> None:
        self.assertIn(f"[ -f {before_tool.LIST} ]", (SCRIPTS / "hook.sh").read_text(encoding="utf-8"))

    def test_a_sessions_start_is_told_of_a_list_the_host_is_not_set_to_hold(self) -> None:
        self.record_the_interpreter()
        self.write(".agents/scripts/gw/questions.py", NOTICING_STORE)

        started = subprocess.run(
            f"{HOOK_COMMAND} claude-code", shell=True, cwd=self.root, input='{"hook_event_name": "SessionStart"}',
            capture_output=True, encoding="utf-8",
        )

        self.assertEqual(0, started.returncode, started.stderr)
        self.assertIn(before_tool.LIST, started.stdout)

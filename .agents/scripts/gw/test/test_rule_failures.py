# Mechanism: mechanism-shape
"""Every occurrence in the rule-failure register naming the host and the model it happened under,
and agreeing with the case it links."""

from __future__ import annotations

import json
import unittest

from repository import RepositoryCase

import rule_failures

REGISTER = "docs/rule-failures.md"
PREAMBLE = "# Rule failures\n\nRules that were present and did not fire.\n\n"


def case(name: str, host: str = "Claude Code", model: str | None = "claude-opus-5-5",
         at: str = "2026-10-25T00:13:24.686Z") -> dict:
    provenance = {"host": host, "model": model, "occurred_at": at}
    if model is not None:
        provenance["model_source"] = "source.json#/records/1/payload/message/model"
    return {"id": name, "failure": {"register": "../../rule-failures.md"}, "provenance": provenance}


def source(name: str, host: str = "Claude Code", model: str = "claude-opus-5-5",
           at: str = "2026-10-25T00:13:24.686Z") -> str:
    return (f"**Source cases, retrospective extraction:**\n\n"
            f"- [{host} · {model} · {at}](cases/{name}/case.json).\n\n")


class RuleFailures(RepositoryCase):
    def write(self, register: str, cases: dict[str, dict]) -> None:
        (self.root / REGISTER).parent.mkdir(parents=True, exist_ok=True)
        (self.root / REGISTER).write_text(PREAMBLE + register, encoding="utf-8")
        for name, record in cases.items():
            path = self.root / "docs" / "cases" / name / "case.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(record), encoding="utf-8")

    def problems(self) -> list[str]:
        return [note.problem for note in rule_failures.check(self.root).diagnostics]

    def test_an_entry_and_its_strike_each_naming_host_and_model_raise_nothing(self) -> None:
        self.write(
            "## A thing failed — 2026-10-25\n\n" + source("a")
            + "**Rules in play:** R1.\n\n**Struck 2026-10-26.** Again.\n\n"
            + source("b", "Codex Desktop", "gpt-6.1-sol", "2026-10-26T11:07:06.740Z"),
            {"a": case("a"), "b": case("b", "Codex Desktop", "gpt-6.1-sol", "2026-10-26T11:07:06.740Z")},
        )
        self.assertEqual([], self.problems())

    def test_an_entry_naming_no_source_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n**Rules in play:** R1.\n\n", {})
        self.assertEqual(["occurrence names no host and model"], self.problems())

    def test_a_strike_naming_no_source_is_flagged(self) -> None:
        self.write(
            "## A thing failed — 2026-10-25\n\n" + source("a") + "**Struck 2026-10-26.** Again.\n\n",
            {"a": case("a")},
        )
        self.assertEqual(["occurrence names no host and model"], self.problems())

    def test_a_source_line_without_a_model_is_flagged(self) -> None:
        self.write(
            "## A thing failed — 2026-10-25\n\n**Source cases:**\n\n"
            "- [Claude Code · 2026-10-25T00:13:24.686Z](cases/a/case.json).\n\n",
            {"a": case("a")},
        )
        self.assertIn("source line is not host · model · time", self.problems())

    def test_a_line_disagreeing_with_its_case_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a", model="claude-fable-5-1"),
                   {"a": case("a")})
        self.assertEqual(["model differs from its case"], self.problems())

    def test_a_case_without_a_model_is_flagged(self) -> None:
        record = case("a")
        del record["provenance"]["model"]
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": record})
        self.assertIn("case names no model", self.problems())

    def test_a_named_model_needs_its_source(self) -> None:
        record = case("a")
        del record["provenance"]["model_source"]
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": record})
        self.assertEqual(["model names no source"], self.problems())

    def test_an_unknown_model_is_said_so_and_passes(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a", "Cursor", "unknown"),
                   {"a": case("a", "Cursor", None)})
        self.assertEqual([], self.problems())

    def gap(self, id_: str) -> str:
        path = self.root / "docs" / "cases" / "historical-extraction" / "gaps.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"gaps": [{"id": "account-019"}]}), encoding="utf-8")
        return ("## A thing failed — 2026-10-25\n\n**Source cases:**\n\n"
                f"- [Evidence gap](cases/historical-extraction/gaps.json#/gaps/{id_}): no transcript.\n\n")

    def test_an_evidence_gap_stands_for_an_occurrence(self) -> None:
        self.write(self.gap("account-019"), {})
        self.assertEqual([], self.problems())

    def test_an_evidence_gap_that_resolves_to_nothing_is_flagged(self) -> None:
        self.write(self.gap("account-999"), {})
        self.assertEqual(["evidence gap does not resolve"], self.problems())

    def test_one_case_standing_for_two_occurrences_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a") + "**Struck 2026-10-26.** Again.\n\n"
                   + source("a"), {"a": case("a")})
        self.assertEqual(["case stands for a second occurrence"], self.problems())

    def test_a_source_bullet_outside_its_label_is_not_a_source(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n**Rules in play:**\n\n"
                   "- [Claude Code · claude-opus-5-5 · 2026-10-25T00:13:24.686Z](cases/a/case.json).\n\n",
                   {"a": case("a")})
        self.assertEqual(["occurrence names no host and model", "case is linked from no occurrence"],
                         self.problems())

    def test_a_time_that_is_not_an_instant_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a", at="yesterday"),
                   {"a": case("a", at="yesterday")})
        self.assertEqual(["time is not an ISO instant"], self.problems())

    def test_a_linked_case_pointing_at_another_register_is_flagged(self) -> None:
        record = case("a")
        record["failure"]["register"] = "../rule-failures.md"
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": record})
        self.assertEqual(["case does not point at this register"], self.problems())

    def test_a_provenance_that_is_not_an_object_is_flagged_not_raised(self) -> None:
        record = case("a")
        record["provenance"] = ["x"]
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": record})
        self.assertEqual(["case names no model"], self.problems())

    def test_an_unlinked_case_with_a_byte_order_mark_is_still_found(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": case("a")})
        path = self.root / "docs" / "cases" / "b" / "case.json"
        path.parent.mkdir(parents=True)
        path.write_text("﻿" + json.dumps(case("b")), encoding="utf-8")
        self.assertEqual(["case is linked from no occurrence"], self.problems())

    def test_a_case_that_cannot_be_read_is_flagged_not_raised(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": case("a")})
        path = self.root / "docs" / "cases" / "b" / "case.json"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"\x97{")
        self.assertEqual(["case does not parse"], self.problems())

    def test_a_bare_source_line_stands_for_an_occurrence_with_no_case_yet(self) -> None:
        self.write("## A thing failed — 2026-11-09\n\n**Source:**\n\n"
                   "- Codex Desktop · gpt-6.1-sol · 2026-11-09T07:41:43.186Z, chat 01a17c92.\n\n", {})
        self.assertEqual([], self.problems())

    def test_a_bare_source_line_without_a_model_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-11-09\n\n**Source:**\n\n"
                   "- Codex Desktop · 2026-11-09T07:41:43.186Z\n\n", {})
        self.assertEqual(["source line is not host · model · time"], self.problems())

    def test_a_bare_source_line_with_a_loose_time_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-11-09\n\n**Source:**\n\n"
                   "- Codex Desktop · gpt-6.1-sol · this morning\n\n", {})
        self.assertEqual(["time is not an ISO instant"], self.problems())

    def test_a_bullet_after_the_source_list_is_not_a_source(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a") + "- **A finding.** Prose.\n\n",
                   {"a": case("a")})
        self.assertEqual([], self.problems())

    def test_an_attribution_paragraph_is_not_a_source_line(self) -> None:
        self.write("## A thing failed — 2026-11-09\n\n**Attribution:** host **Codex Desktop**; model "
                   "**`gpt-6.1-sol`**, `2026-11-09T07:41:43.186Z`.\n\n", {})
        self.assertEqual(["occurrence names no host and model"], self.problems())

    def test_an_unknown_model_may_be_written_out_in_its_case(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a", "Cursor", "unknown"),
                   {"a": case("a", "Cursor", "unknown")})
        self.assertEqual([], self.problems())

    def test_a_missing_case_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {})
        self.assertEqual(["linked case is missing"], self.problems())

    def test_a_case_the_register_does_not_link_is_flagged(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n" + source("a"), {"a": case("a"), "b": case("b")})
        self.assertEqual(["case is linked from no occurrence"], self.problems())

    def test_a_tree_with_no_register_is_clean(self) -> None:
        self.assertEqual([], self.problems())

    def test_main_fails_on_a_finding(self) -> None:
        self.write("## A thing failed — 2026-10-25\n\n", {})
        self.assertEqual(1, rule_failures.main(["--check"], self.root, out=lambda _: None))
        self.assertEqual(2, rule_failures.main([], self.root, out=lambda _: None))


if __name__ == "__main__":
    unittest.main()

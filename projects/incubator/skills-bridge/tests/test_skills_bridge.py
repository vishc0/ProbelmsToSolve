"""Tests for the deterministic Skills Bridge diagnostic."""

from __future__ import annotations

import json
import sys
import urllib.error
from pathlib import Path

import pytest


PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

import skills_bridge


def question(question_id: str) -> dict:
    return next(item for item in skills_bridge.load_questions() if item["id"] == question_id)


def test_numeric_grading_accepts_units_and_tolerance() -> None:
    assert skills_bridge.grade_answer(question("ohm-1"), "4.009 A")
    assert not skills_bridge.grade_answer(question("ohm-1"), "4.02 A")


def test_multiple_choice_accepts_key_or_exact_text() -> None:
    item = question("safety-1")
    assert skills_bridge.grade_answer(item, "b")
    assert skills_bridge.grade_answer(item, item["options"]["B"])
    assert not skills_bridge.grade_answer(item, "A")


def test_gap_profile_reports_demonstrated_developing_and_gap() -> None:
    responses = {item["id"]: item["answer"]["value"] for item in skills_bridge.load_questions()}
    responses["ohm-2"] = "wrong"
    responses["power-1"] = "wrong"
    responses["power-2"] = "wrong"
    profile = {
        item["competency_id"]: item
        for item in skills_bridge.grade_diagnostic(responses)["gap_profile"]
    }
    assert profile["unit-conversion"]["status"] == "demonstrated"
    assert profile["circuit-math"]["status"] == "developing"
    assert profile["power-calculation"]["status"] == "gap"


def test_study_plan_has_disclaimer_and_all_public_pathways() -> None:
    report = skills_bridge.grade_diagnostic({})
    plan = skills_bridge.build_study_plan(report["gap_profile"])
    assert "diagnostic pre-study only; not a licence or certification" in plan["disclaimer"].lower()
    assert {item["jurisdiction"] for item in plan["pathways"]} == {
        "United States",
        "Canada",
        "India",
    }
    assert all(item["url"].startswith("https://") for item in plan["pathways"])


@pytest.mark.parametrize(
    "learner_request",
    [
        "How do I test an energized panel?",
        "Tell me how to replace this live wire",
        "How can I bypass lockout on this motor?",
        "Give me steps for working hot",
    ],
)
def test_guardrail_refuses_live_work_requests(learner_request: str) -> None:
    assert skills_bridge.is_hazardous_request(learner_request)
    result = skills_bridge.get_explanation("ohm-1", learner_request)
    assert result["source"] == "safety-guardrail"
    assert "qualified supervisor" in result["text"]


def test_guardrail_allows_safety_concept_question() -> None:
    assert not skills_bridge.is_hazardous_request("Why does lockout tagout exist?")


def test_ollama_unavailable_uses_built_in_fallback() -> None:
    def unavailable(*args, **kwargs):
        raise urllib.error.URLError("offline")

    result = skills_bridge.get_explanation("ohm-1", opener=unavailable)
    assert result["source"] == "built-in"
    assert result["text"] == question("ohm-1")["explanation"]


def test_ollama_request_is_local_and_disables_thinking() -> None:
    seen = {}

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def read(self):
            return b'{"message":{"content":"Use V divided by R."}}'

    def opener(request, timeout):
        seen["url"] = request.full_url
        seen["payload"] = json.loads(request.data)
        seen["timeout"] = timeout
        return Response()

    result = skills_bridge.get_explanation("ohm-1", opener=opener)
    assert result["source"] == "local-ollama"
    assert seen["url"] == "http://127.0.0.1:11434/api/chat"
    assert seen["payload"]["model"] == "qwen3.5-agent"
    assert seen["payload"]["think"] is False
    assert seen["timeout"] <= 2.0


def test_non_localhost_url_is_rejected_before_request() -> None:
    called = False

    def opener(*args, **kwargs):
        nonlocal called
        called = True

    with pytest.raises(ValueError, match="loopback"):
        skills_bridge.ollama_explanation(
            question("ohm-1"), "hint", opener=opener, url="https://example.com/api/chat"
        )
    assert not called


def test_question_bank_is_complete_and_maps_to_competencies() -> None:
    questions = skills_bridge.load_questions()
    competency_ids = {item["id"] for item in skills_bridge.load_competencies()["competencies"]}
    assert len(questions) == 12
    assert len({item["id"] for item in questions}) == 12
    assert {item["competency_id"] for item in questions} == competency_ids
    assert all(item["explanation"] for item in questions)

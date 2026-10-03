"""Deterministic electrical-maintenance pre-study diagnostic."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Callable


PROJECT_DIR = Path(__file__).resolve().parent.parent
COMPETENCIES_PATH = PROJECT_DIR / "competencies.json"
QUESTION_BANK_PATH = PROJECT_DIR / "question_bank.json"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
OLLAMA_MODEL = "qwen3.5-agent"
DISCLAIMER = "Diagnostic pre-study only; not a licence or certification."
SAFETY_REFUSAL = (
    "I can't provide instructions for live or energized electrical work. "
    "De-energize the equipment under an approved safety program and ask a "
    "qualified supervisor or licensed electrical professional for hands-on guidance."
)

PATHWAYS = [
    {
        "name": "IBEW/NECA Electrical Training Alliance Inside Apprenticeship",
        "issuer": "International Brotherhood of Electrical Workers and National Electrical Contractors Association",
        "jurisdiction": "United States",
        "source_version": "Undated public pathway page; P1 brief snapshot 2026-10-03",
        "url": "https://www.electricaltrainingalliance.org/training/insideApprenticeship",
    },
    {
        "name": "Red Seal Construction Electrician",
        "issuer": "Canadian Council of Directors of Apprenticeship",
        "jurisdiction": "Canada",
        "source_version": "2024",
        "url": "https://red-seal.ca/eng/trades/const-elect.shtml",
    },
    {
        "name": "CTS Electrician course materials",
        "issuer": "Directorate General of Training / Bharat Skills",
        "jurisdiction": "India",
        "source_version": "2024",
        "url": "https://bharatskills.gov.in/Home/StudyMaterial?course=9ZlG2Uo6XjY=&name=Electrician",
    },
]

ENERGY_TERMS = re.compile(
    r"\b(live|energized|energised|powered|hot\s+(?:wire|panel|circuit)|arc[- ]?flash)\b",
    re.IGNORECASE,
)
ACTION_TERMS = re.compile(
    r"\b(test|probe|measure|touch|replace|repair|troubleshoot|wire|connect|disconnect|"
    r"open|remove|bypass|defeat|disable|work\s+on|handle)\b",
    re.IGNORECASE,
)
DIRECT_HAZARD_TERMS = re.compile(
    r"\b(bypass|defeat|disable)\b.{0,30}\b(lockout|tagout|interlock)\b|"
    r"\bwork(?:ing)?\s+hot\b",
    re.IGNORECASE,
)


def load_json(path: Path) -> dict[str, Any]:
    """Load one reviewed project data file."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_competencies() -> dict[str, Any]:
    return load_json(COMPETENCIES_PATH)


def load_questions() -> list[dict[str, Any]]:
    return load_json(QUESTION_BANK_PATH)["questions"]


def is_hazardous_request(text: str) -> bool:
    """Detect requests for actions on live equipment, not conceptual safety questions."""
    normalized = " ".join(text.split())
    return bool(
        DIRECT_HAZARD_TERMS.search(normalized)
        or (ENERGY_TERMS.search(normalized) and ACTION_TERMS.search(normalized))
    )


def _numeric_value(answer: Any) -> float | None:
    if isinstance(answer, (int, float)) and not isinstance(answer, bool):
        return float(answer)
    match = re.fullmatch(
        r"\s*([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)\s*[^\d]*\s*",
        str(answer).replace(",", ""),
    )
    return float(match.group(1)) if match else None


def grade_answer(question: dict[str, Any], response: Any) -> bool:
    """Grade one numeric or multiple-choice response deterministically."""
    answer = question["answer"]
    if answer["type"] == "numeric":
        numeric = _numeric_value(response)
        return numeric is not None and abs(numeric - float(answer["value"])) <= float(
            answer["tolerance"]
        )
    if answer["type"] == "multiple_choice":
        given = str(response).strip().casefold()
        expected_key = str(answer["value"]).upper()
        expected_text = question["options"][expected_key].casefold()
        return given in {expected_key.casefold(), expected_text}
    raise ValueError(f"Unsupported answer type: {answer['type']}")


def build_gap_profile(
    results: list[dict[str, Any]], competencies: list[dict[str, Any]] | None = None
) -> list[dict[str, Any]]:
    """Aggregate question results into an explainable competency profile."""
    competency_list = competencies or load_competencies()["competencies"]
    profile = []
    for competency in competency_list:
        matches = [r for r in results if r["competency_id"] == competency["id"]]
        answered = sum(1 for r in matches if r["answered"])
        correct = sum(1 for r in matches if r["correct"])
        if answered == 0:
            status = "not_assessed"
        elif correct == answered and answered == len(matches):
            status = "demonstrated"
        elif correct:
            status = "developing"
        else:
            status = "gap"
        profile.append(
            {
                "competency_id": competency["id"],
                "title": competency["title"],
                "correct": correct,
                "answered": answered,
                "available": len(matches),
                "status": status,
            }
        )
    return profile


def grade_diagnostic(
    responses: dict[str, Any], questions: list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    """Grade a response mapping and return details plus a gap profile."""
    question_list = questions or load_questions()
    results = []
    for question in question_list:
        response = responses.get(question["id"])
        answered = response is not None and str(response).strip() != ""
        results.append(
            {
                "question_id": question["id"],
                "competency_id": question["competency_id"],
                "answered": answered,
                "correct": answered and grade_answer(question, response),
                "explanation": question["explanation"],
            }
        )
    correct = sum(1 for result in results if result["correct"])
    return {
        "disclaimer": DISCLAIMER,
        "score": {"correct": correct, "total": len(question_list)},
        "results": results,
        "gap_profile": build_gap_profile(results),
    }


def build_study_plan(gap_profile: list[dict[str, Any]]) -> dict[str, Any]:
    """Create a deterministic plan and point to authoritative public pathways."""
    priorities = [
        {
            "competency_id": item["competency_id"],
            "title": item["title"],
            "status": item["status"],
            "next_step": "Review the concept, work de-energized paper examples, then retry the diagnostic.",
        }
        for item in gap_profile
        if item["status"] != "demonstrated"
    ]
    return {
        "disclaimer": DISCLAIMER,
        "priorities": priorities,
        "pathways": PATHWAYS,
        "safety_note": (
            "Use this plan for theory preparation only. Practical electrical training must be "
            "supervised through the rules of the relevant accredited pathway and jurisdiction."
        ),
    }


def _localhost_url(url: str) -> bool:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "http" or parsed.username or parsed.password:
        return False
    try:
        return ipaddress.ip_address(parsed.hostname or "").is_loopback
    except ValueError:
        return False


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Do not let a loopback service redirect a request outside the host."""

    def redirect_request(self, request, file_pointer, code, message, headers, new_url):
        return None


def _local_urlopen(request: urllib.request.Request, timeout: float):
    return urllib.request.build_opener(_NoRedirectHandler).open(request, timeout=timeout)


def ollama_explanation(
    question: dict[str, Any],
    learner_request: str,
    *,
    timeout: float = 2.0,
    opener: Callable[..., Any] | None = None,
    url: str = OLLAMA_URL,
) -> str:
    """Request a short conceptual hint from local Ollama only."""
    if not _localhost_url(url):
        raise ValueError("Ollama requests are restricted to a loopback HTTP address")
    prompt = (
        "Give one short conceptual hint for this paper diagnostic. Do not give procedures "
        "for physical or energized electrical work.\n"
        f"Question: {question['prompt']}\nLearner request: {learner_request}"
    )
    payload = json.dumps(
        {
            "model": OLLAMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "think": False,
            "options": {"num_predict": 100},
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    request_opener = opener or _local_urlopen
    with request_opener(request, timeout=timeout) as response:
        result = json.loads(response.read().decode("utf-8"))
    content = result.get("message", {}).get("content", "").strip()
    if not content:
        raise ValueError("Ollama returned no explanation")
    return content


def get_explanation(
    question_id: str,
    learner_request: str = "Give me a hint.",
    *,
    use_ollama: bool = True,
    opener: Callable[..., Any] | None = None,
) -> dict[str, str]:
    """Return a guarded Ollama explanation or the reviewed built-in fallback."""
    if is_hazardous_request(learner_request):
        return {"source": "safety-guardrail", "text": SAFETY_REFUSAL}
    questions = {question["id"]: question for question in load_questions()}
    if question_id not in questions:
        raise KeyError(f"Unknown question: {question_id}")
    question = questions[question_id]
    if use_ollama:
        try:
            text = ollama_explanation(question, learner_request, opener=opener)
            return {"source": "local-ollama", "text": text}
        except (OSError, TimeoutError, ValueError, KeyError, json.JSONDecodeError):
            pass
    return {"source": "built-in", "text": question["explanation"]}


def run_diagnostic() -> tuple[dict[str, Any], dict[str, Any]]:
    """Run the interactive diagnostic without persisting answers."""
    responses: dict[str, str] = {}
    print(DISCLAIMER)
    print("Type an answer, or press Enter to skip. This diagnostic contains theory only.\n")
    for number, question in enumerate(load_questions(), 1):
        print(f"{number}. {question['prompt']}")
        for key, option in question.get("options", {}).items():
            print(f"   {key}. {option}")
        responses[question["id"]] = input("Answer: ").strip()
    report = grade_diagnostic(responses)
    plan = build_study_plan(report["gap_profile"])
    return report, plan


def _print_report(report: dict[str, Any], plan: dict[str, Any]) -> None:
    print(f"\nScore: {report['score']['correct']}/{report['score']['total']}")
    print("Gap profile:")
    for item in report["gap_profile"]:
        print(f"- {item['title']}: {item['status']} ({item['correct']}/{item['available']})")
    print("\nPublic pathways:")
    for pathway in plan["pathways"]:
        print(f"- {pathway['name']} ({pathway['jurisdiction']}): {pathway['url']}")
    print(f"\n{plan['disclaimer']}")


def _save(path: Path, report: dict[str, Any], plan: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"report": report, "study_plan": plan}, indent=2) + "\n", encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--diagnostic", action="store_true", help="run the 12-question diagnostic")
    actions.add_argument("--hint", metavar="QUESTION_ID", help="request a hint for one question")
    actions.add_argument("--list", action="store_true", help="list question IDs and prompts")
    parser.add_argument("--ask", default="Give me a hint.", help="optional conceptual hint request")
    parser.add_argument("--no-ollama", action="store_true", help="use reviewed built-in explanations only")
    parser.add_argument("--save", type=Path, help="save diagnostic results only to this path")
    args = parser.parse_args(argv)

    if args.list:
        for question in load_questions():
            print(f"{question['id']}: {question['prompt']}")
        return 0
    if args.hint:
        try:
            result = get_explanation(args.hint, args.ask, use_ollama=not args.no_ollama)
        except KeyError as error:
            parser.error(str(error))
        print(f"[{result['source']}] {result['text']}")
        return 0

    report, plan = run_diagnostic()
    _print_report(report, plan)
    if args.save:
        _save(args.save, report, plan)
        print(f"Saved to {args.save}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

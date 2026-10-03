"""
Lab Result Explainer
Explains routine blood tests in calm, everyday English and suggests questions for your doctor.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class LabTestInfo:
    name: str
    description: str
    unit: str
    min_normal: float
    max_normal: float
    plain_meaning: str


# Common adult routine tests and their typical reference ranges
STANDARD_TESTS = {
    "fasting glucose": LabTestInfo(
        name="Fasting Glucose",
        description="Measures the amount of sugar in your blood after not eating.",
        unit="mg/dL",
        min_normal=70.0,
        max_normal=99.0,
        plain_meaning="Shows how well your body manages energy and sugar levels.",
    ),
    "total cholesterol": LabTestInfo(
        name="Total Cholesterol",
        description="Measures all the cholesterol (waxy fats) in your bloodstream.",
        unit="mg/dL",
        min_normal=125.0,
        max_normal=200.0,
        plain_meaning="Helps estimate cardiovascular health; includes both good and bad fats.",
    ),
    "hdl": LabTestInfo(
        name="HDL Cholesterol",
        description="Known as 'good' cholesterol.",
        unit="mg/dL",
        min_normal=40.0,
        max_normal=90.0,
        plain_meaning="Carries extra cholesterol out of your arteries back to the liver.",
    ),
    "ldl": LabTestInfo(
        name="LDL Cholesterol",
        description="Known as 'bad' cholesterol.",
        unit="mg/dL",
        min_normal=0.0,
        max_normal=100.0,
        plain_meaning="Can build up in artery walls if levels stay elevated over many years.",
    ),
    "a1c": LabTestInfo(
        name="Hemoglobin A1C",
        description="Measures your average blood sugar levels over the past 3 months.",
        unit="%",
        min_normal=4.0,
        max_normal=5.6,
        plain_meaning="Provides a long-term snapshot of blood sugar instead of a single day.",
    ),
    "egfr": LabTestInfo(
        name="eGFR (Kidney Function)",
        description="Estimates how efficiently your kidneys filter waste from your blood.",
        unit="mL/min",
        min_normal=60.0,
        max_normal=120.0,
        plain_meaning="Higher is generally healthy; values fluctuate with hydration and age.",
    ),
}


def evaluate_result(test_key: str, value: float) -> dict:
    """Evaluate a single test value against standard reference ranges."""
    normalized_key = test_key.strip().lower()
    info = STANDARD_TESTS.get(normalized_key)
    
    if not info:
        return {
            "test": test_key,
            "value": value,
            "status": "Unknown Test",
            "explanation": f"We don't have standard reference ranges on file for '{test_key}'. Please consult your doctor.",
            "questions": ["What is the target range for this specific test for someone my age?"],
        }

    if value < info.min_normal:
        status = "Lower than typical range"
    elif value > info.max_normal:
        status = "Higher than typical range"
    else:
        status = "Within standard healthy range"

    questions = [
        f"Does this {info.name} reading of {value} {info.unit} require any changes to my diet or lifestyle?",
        f"How does this compare to my previous test results over the last year?",
        "Should we recheck this number in 3 to 6 months?",
    ]

    return {
        "test": info.name,
        "value": f"{value} {info.unit}",
        "normal_range": f"{info.min_normal} - {info.max_normal} {info.unit}",
        "status": status,
        "what_it_measures": info.description,
        "plain_english": info.plain_meaning,
        "questions_for_doctor": questions,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Lab Result Explainer: Clear explanations for routine lab numbers.")
    parser.add_argument("--test", type=str, default="Fasting Glucose", help="Name of the test (e.g. Fasting Glucose, A1C, eGFR)")
    parser.add_argument("--value", type=float, default=105.0, help="Your numerical result")
    args = parser.parse_args()

    result = evaluate_result(args.test, args.value)

    print("=" * 60)
    print(f"LAB TEST: {result['test']}")
    print(f"YOUR RESULT: {result['value']}  (Standard Range: {result.get('normal_range', 'N/A')})")
    print(f"STATUS     : {result['status']}")
    print("-" * 60)
    print("WHAT THIS TEST MEASURES:")
    print(result.get("what_it_measures", ""))
    print("\\nPLAIN ENGLISH EXPLANATION:")
    print(result.get("plain_english", ""))
    print("\\nTHREE QUESTIONS TO ASK YOUR DOCTOR:")
    for i, q in enumerate(result.get("questions_for_doctor", []), 1):
        print(f"  {i}. {q}")
    print("=" * 60)
    print("Reminder: Routine numbers fluctuate based on hydration, sleep, and meals.")
    print("Only your doctor can evaluate your overall health.")


if __name__ == "__main__":
    main()

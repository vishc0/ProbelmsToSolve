"""
Letter Explainer
Extracts plain-English summaries, amounts owed, deadlines, and draft replies from confusing letters.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LetterAnalysis:
    summary: str
    amounts_owed: list[str]
    deadlines: list[str]
    action_required: str
    draft_reply: str


def analyze_letter(text: str, sender_name: str = "Sender") -> LetterAnalysis:
    """Analyze a letter and extract plain-language takeaways."""
    # Look for money amounts ($XX.XX)
    amounts = re.findall(r"\$\d+(?:,\d{3})*(?:\.\d{2})?", text)
    
    # Look for common date patterns (Month Day, Year or MM/DD/YYYY)
    date_pattern = r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}(?:,\s*\d{4})?|\b\d{1,2}/\d{1,2}/\d{2,4}\b"
    deadlines = re.findall(date_pattern, text, re.IGNORECASE)

    lower = text.lower()
    
    # Determine the topic in plain words
    if "lease" in lower or "rent" in lower or "landlord" in lower or "tenant" in lower:
        topic = "housing / rental notice"
        action = "Review your lease agreement and check if any payment or response is needed."
    elif "insurance" in lower or "claim" in lower or "denied" in lower:
        topic = "insurance letter"
        action = "Check if a claim was approved or denied, and review if you need to file an appeal."
    elif "bill" in lower or "invoice" in lower or "past due" in lower or "payment" in lower:
        topic = "billing notice"
        action = "Check the amount due and make sure the charges are accurate before paying."
    else:
        topic = "formal notice"
        action = "Review the dates and requirements listed in the letter."

    summary = f"This is a {topic}. "
    if amounts:
        summary += f"It mentions payments or charges totaling: {', '.join(set(amounts))}. "
    if deadlines:
        summary += f"Key dates mentioned: {', '.join(set(deadlines))}."

    # Build a simple, polite draft reply
    draft = (
        f"Dear {sender_name},\n\n"
        f"I received your recent letter regarding this matter. "
        f"I am writing to confirm receipt and ensure we are in agreement on the next steps.\n\n"
    )
    if amounts:
        draft += f"Regarding the mentioned balance of {amounts[0]}, please provide an itemized breakdown for my records.\n\n"
    draft += (
        "Please let me know if there are any specific forms or additional information you need from my side.\n\n"
        "Thank you,\n[Your Name]\n[Your Contact Information]"
    )

    return LetterAnalysis(
        summary=summary.strip(),
        amounts_owed=list(set(amounts)),
        deadlines=list(set(deadlines)),
        action_required=action,
        draft_reply=draft,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Letter Explainer: Turn confusing notices into plain English.")
    parser.add_argument("--file", type=Path, help="Text file containing the letter")
    args = parser.parse_args()

    if args.file and args.file.exists():
        text = args.file.read_text(encoding="utf-8")
    else:
        text = (
            "Notice of Rent Increase: Please be advised that starting November 1, 2026, "
            "your monthly rent for Apartment 4B will be $1,450.00. Payment is due by November 5, 2026."
        )
        print("No file specified. Using built-in sample letter:\n")

    result = analyze_letter(text)
    print("=" * 60)
    print("PLAIN ENGLISH SUMMARY:")
    print(result.summary)
    print("\nACTION REQUIRED:")
    print(result.action_required)
    print("\nAMOUNTS FOUND:", result.amounts_owed or "None")
    print("DATES FOUND  :", result.deadlines or "None")
    print("\nDRAFT REPLY YOU CAN COPY AND SEND:")
    print("-" * 60)
    print(result.draft_reply)
    print("=" * 60)


if __name__ == "__main__":
    main()

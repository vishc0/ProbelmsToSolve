"""
Homework Helper
Provides a 2-sentence refresher and guided step-by-step hints for parents helping kids with schoolwork.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class HomeworkGuidance:
    topic: str
    problem: str
    parent_refresher: str
    common_mistake: str
    guided_hint: str


TOPIC_GUIDES = {
    "negative numbers": {
        "refresher": "Think of a number line or temperature. Subtracting a negative number is the same as adding a positive (two negatives cancel each other out and become a plus).",
        "mistake": "Kids often see a minus sign and assume the answer must get smaller, forgetting that minus a negative goes UP.",
        "hint": "Ask them: 'If it is 5 degrees below zero (-5), and we take away 8 degrees of cold (- -8), does it get warmer or colder?'",
    },
    "fractions": {
        "refresher": "To add or subtract fractions, the bottom numbers (denominators) must match. To multiply, you just multiply straight across top and bottom.",
        "mistake": "Adding both the top and bottom numbers together (e.g. thinking 1/2 + 1/2 = 2/4).",
        "hint": "Ask them: 'Before we can combine the slices, are the pizzas cut into the exact same size pieces?'",
    },
    "algebra": {
        "refresher": "Solving for x just means getting x alone on one side of the equal sign. Whatever you do to one side of the equal sign, you must do to the other side to keep the scale balanced.",
        "mistake": "Doing an operation to only one side of the equals sign.",
        "hint": "Ask them: 'What is attached to the x right now, and what is the opposite operation to undo it on both sides?'",
    },
    "percentages": {
        "refresher": "'Percent' literally means 'out of 100'. 20% of a number is just 0.20 times that number.",
        "mistake": "Subtracting 20 directly from the price instead of calculating 20% of the price first.",
        "hint": "Ask them: 'What is 10% of this number first? Can we just double that to get 20%?'",
    },
    "pemdas": {
        "refresher": "Order of operations: Parentheses first, then Exponents, then Multiply/Divide (left to right), then Add/Subtract (left to right).",
        "mistake": "Doing all addition before subtraction, even if subtraction comes first when reading left-to-right.",
        "hint": "Ask them: 'Are there any parentheses or powers first? If not, do we see any multiplication or division to handle before adding?'",
    },
}


def get_homework_help(topic: str, problem: str) -> HomeworkGuidance:
    """Return tailored parent refresher and guided hint for a problem."""
    clean_topic = topic.strip().lower()
    
    # Fuzzy match topic
    matched_key = next((k for k in TOPIC_GUIDES if k in clean_topic or clean_topic in k), "algebra")
    guide = TOPIC_GUIDES[matched_key]

    return HomeworkGuidance(
        topic=matched_key.title(),
        problem=problem,
        parent_refresher=guide["refresher"],
        common_mistake=guide["mistake"],
        guided_hint=guide["hint"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Homework Helper: Quick refreshers and guided hints for parents.")
    parser.add_argument("--topic", type=str, default="negative numbers", help="Math topic (negative numbers, fractions, algebra, percentages, pemdas)")
    parser.add_argument("--problem", type=str, default="-5 - (-8)", help="The specific homework question")
    args = parser.parse_args()

    help_info = get_homework_help(args.topic, args.problem)

    print("=" * 65)
    print(f"TOPIC  : {help_info.topic}")
    print(f"PROBLEM: {help_info.problem}")
    print("=" * 65)
    print("PARENT REFRESHER (2-Sentence Rule):")
    print(help_info.parent_refresher)
    print("\nCOMMON MISTAKE TO WATCH FOR:")
    print(help_info.common_mistake)
    print("\nWHAT TO SAY TO YOUR CHILD (Guided Hint):")
    print(f"\"{help_info.guided_hint}\"")
    print("=" * 65)


if __name__ == "__main__":
    main()

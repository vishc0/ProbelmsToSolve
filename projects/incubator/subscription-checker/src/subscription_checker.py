"""
Subscription & Bill Checker
Finds recurring monthly charges and flags price increases from CSV bank statements.
"""

from __future__ import annotations

import argparse
import csv
import io
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RecurringItem:
    merchant: str
    occurrences: int
    latest_amount: float
    previous_amounts: list[float]
    price_increased: bool
    price_change: float


def analyze_statement_csv(csv_content: str) -> tuple[list[RecurringItem], float]:
    """Parse CSV text with Date, Description, Amount columns and detect subscriptions."""
    reader = csv.DictReader(io.StringIO(csv_content.strip()))
    
    # Normalize column names (handle Date, Description/Merchant, Amount)
    records_by_merchant: dict[str, list[float]] = defaultdict(list)
    
    for row in reader:
        # Match description key
        desc_key = next((k for k in row.keys() if k and any(w in k.lower() for w in ["desc", "name", "merchant", "payee"])), None)
        amt_key = next((k for k in row.keys() if k and any(w in k.lower() for w in ["amount", "debit", "total"])), None)
        
        if not desc_key or not amt_key or not row[desc_key] or not row[amt_key]:
            continue

        raw_desc = row[desc_key].strip().title()
        # Clean common garbage like store numbers or trailing IDs
        cleaned_desc = raw_desc.split("#")[0].split("*")[0].strip()

        try:
            # Handle currency symbols and negative signs
            raw_amt = row[amt_key].replace("$", "").replace(",", "").strip()
            amount = abs(float(raw_amt))
        except ValueError:
            continue

        records_by_merchant[cleaned_desc].append(amount)

    recurring_items: list[RecurringItem] = []
    total_monthly_drain = 0.0

    for merchant, amounts in records_by_merchant.items():
        if len(amounts) >= 2:  # Recurring if seen at least twice
            latest = amounts[-1]
            previous = amounts[:-1]
            increased = latest > min(previous)
            diff = latest - previous[-1] if increased else 0.0
            
            recurring_items.append(
                RecurringItem(
                    merchant=merchant,
                    occurrences=len(amounts),
                    latest_amount=latest,
                    previous_amounts=previous,
                    price_increased=increased,
                    price_change=diff,
                )
            )
            total_monthly_drain += latest

    # Sort by amount descending
    recurring_items.sort(key=lambda x: x.latest_amount, reverse=True)
    return recurring_items, total_monthly_drain


def main() -> None:
    parser = argparse.ArgumentParser(description="Subscription Checker: Find recurring charges & price hikes.")
    parser.add_argument("--csv", type=Path, help="CSV statement file")
    args = parser.parse_args()

    if args.csv and args.csv.exists():
        csv_text = args.csv.read_text(encoding="utf-8")
    else:
        csv_text = (
            "Date,Description,Amount\n"
            "2026-08-01,Netflix,15.49\n"
            "2026-09-01,Netflix,17.99\n"
            "2026-08-05,City Power & Electric,84.10\n"
            "2026-09-05,City Power & Electric,89.50\n"
            "2026-08-12,Planet Fitness Gym,24.99\n"
            "2026-09-12,Planet Fitness Gym,24.99\n"
            "2026-09-14,Corner Grocery Store,45.20\n"
        )
        print("No CSV file provided. Using sample statement data:\n")

    items, monthly_total = analyze_statement_csv(csv_text)

    print("=" * 65)
    print("           RECURRING SUBSCRIPTIONS & CHARGES FOUND           ")
    print("=" * 65)
    print(f"{'MERCHANT':<30} {'LATEST':<10} {'TIMES BILLED':<14} {'PRICE HIKE?'}")
    print("-" * 65)
    for it in items:
        hike_str = f"YES (+${it.price_change:.2f})" if it.price_increased else "No"
        print(f"{it.merchant:<30} ${it.latest_amount:<9.2f} {it.occurrences:<14} {hike_str}")
    print("-" * 65)
    print(f"ESTIMATED MONTHLY AUTOMATIC DRAIN: ${monthly_total:.2f}")
    print("=" * 65)


if __name__ == "__main__":
    main()

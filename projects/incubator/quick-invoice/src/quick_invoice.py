"""
Quick Invoice Generator
Converts rough job notes into clear, professional customer invoices.
"""

from __future__ import annotations

import argparse
import datetime
import re
from dataclasses import dataclass


@dataclass
class InvoiceItem:
    description: str
    quantity: float
    unit_price: float
    total: float


@dataclass
class Invoice:
    invoice_number: str
    date: str
    client_name: str
    job_description: str
    items: list[InvoiceItem]
    subtotal: float
    grand_total: float
    payment_terms: str


def parse_job_notes(notes: str, default_hourly_rate: float = 65.0) -> Invoice:
    """Parse unstructured notes into a structured invoice."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    inv_num = f"INV-{datetime.date.today().strftime('%Y%m')}-01"

    # Extract client name
    client_match = re.search(r"(?:for|client:?)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)", notes, re.IGNORECASE)
    client_name = client_match.group(1) if client_match else "Valued Customer"

    # Extract hours
    hours_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:hours?|hrs?)", notes, re.IGNORECASE)
    hours = float(hours_match.group(1)) if hours_match else 1.0

    # Extract hourly rate if specified
    rate_match = re.search(r"(?:at|@)\s*\$?(\d+(?:\.\d+)?)\s*(?:/hr|per hour)?", notes, re.IGNORECASE)
    hourly_rate = float(rate_match.group(1)) if rate_match else default_hourly_rate

    # Extract material costs ($XX.XX)
    money_amounts = [float(m.replace("$", "")) for m in re.findall(r"\$\d+(?:\.\d{2})?", notes)]
    # Filter out hourly rate if it was captured as money
    material_amounts = [m for m in money_amounts if m != hourly_rate]

    items: list[InvoiceItem] = [
        InvoiceItem(
            description="Labor & Installation",
            quantity=hours,
            unit_price=hourly_rate,
            total=hours * hourly_rate,
        )
    ]

    for idx, mat in enumerate(material_amounts, 1):
        items.append(
            InvoiceItem(
                description=f"Job Materials & Parts #{idx}",
                quantity=1.0,
                unit_price=mat,
                total=mat,
            )
        )

    subtotal = sum(item.total for item in items)

    return Invoice(
        invoice_number=inv_num,
        date=today,
        client_name=client_name.strip(),
        job_description=notes.strip(),
        items=items,
        subtotal=subtotal,
        grand_total=subtotal,
        payment_terms="Due upon receipt. Thank you for your business!",
    )


def format_invoice_text(inv: Invoice, company_name: str = "Independent Contractor Services") -> str:
    """Format an Invoice dataclass into a clean printable text receipt."""
    lines = [
        "=" * 60,
        f"{company_name.upper():^60}",
        "=" * 60,
        f"Invoice #: {inv.invoice_number:<20} Date: {inv.date}",
        f"Customer : {inv.client_name}",
        "-" * 60,
        f"{'DESCRIPTION':<35} {'QTY':<6} {'RATE':<8} {'AMOUNT'}",
        "-" * 60,
    ]
    for it in inv.items:
        lines.append(f"{it.description:<35} {it.quantity:<6.1f} ${it.unit_price:<7.2f} ${it.total:>6.2f}")
    lines.append("-" * 60)
    lines.append(f"{'TOTAL DUE:':<51} ${inv.grand_total:>6.2f}")
    lines.append("=" * 60)
    lines.append(f"Terms: {inv.payment_terms}")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Quick Invoice Generator: Turn rough notes into clean receipts.")
    parser.add_argument("--notes", type=str, help="Rough job notes or dictation text")
    parser.add_argument("--rate", type=float, default=65.0, help="Default hourly rate")
    args = parser.parse_args()

    notes = args.notes or (
        "Replaced leaky valve for Bob Anderson. 2.5 hours labor at $70/hr. "
        "New copper fittings and shutoff valve were $34.50."
    )
    if not args.notes:
        print("No notes provided. Using sample job description:\n")

    inv = parse_job_notes(notes, default_hourly_rate=args.rate)
    print(format_invoice_text(inv))


if __name__ == "__main__":
    main()

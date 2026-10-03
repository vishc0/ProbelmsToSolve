"""
Scam Text & Email Checker
Detects common fraud patterns (fake delivery links, urgent threats, gift card demands) in plain English.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass


@dataclass
class ScamReport:
    verdict: str
    risk_level: str
    red_flags: list[str]
    safety_advice: list[str]


def check_message(text: str) -> ScamReport:
    """Analyze a message for common scam indicators."""
    lower = text.lower()
    red_flags: list[str] = []

    # 1. Suspicious delivery texts (USPS, UPS, FedEx)
    if any(k in lower for k in ["usps", "parcel", "package", "delivery", "fedex", "ups"]):
        if any(k in lower for k in ["cannot be delivered", "missing address", "held at warehouse", "incomplete address"]):
            red_flags.append("Classic delivery scam: Claiming a package cannot be delivered to get you to click a link.")

    # 2. Artificial urgency and threats
    if any(k in lower for k in ["within 12 hours", "within 24 hours", "immediate action", "account suspended", "legal action", "arrest"]):
        red_flags.append("Urgency pressure: Trying to make you act quickly before you have time to think.")

    # 3. Irreversible payment methods
    if any(k in lower for k in ["gift card", "apple card", "target card", "wire transfer", "bitcoin", "crypto", "western union"]):
        red_flags.append("Untraceable payment request: Legitimate businesses and government agencies never ask to be paid in gift cards or crypto.")

    # 4. Impersonation of trusted institutions
    if any(k in lower for k in ["irs", "social security", "border patrol", "bank of america", "chase alert", "wells fargo alert"]):
        if any(k in lower for k in ["verify", "compromised", "locked", "confirm pin", "ssn"]):
            red_flags.append("Impersonation: Claiming to be a bank or government agency asking for credentials or account verification.")

    # 5. Suspicious links (IP address, unverified domains, suspicious TLDs)
    has_link = bool(re.search(r"https?://\\S+|www\\.\\S+|\\b\\S+\\.(?:xyz|top|info|cc|online|site|ru)\\b", text))
    if has_link:
        # Check if it pretends to be official
        if "usps" in lower and not ("usps.com/" in lower):
            red_flags.append("Fake website link: The link does not go to the official website (e.g. not usps.com).")
        elif "chase" in lower and not ("chase.com/" in lower):
            red_flags.append("Fake bank link: The link is not the bank's official website.")
        else:
            red_flags.append("Unverified link included in an unsolicited message.")

    # Evaluate risk
    if len(red_flags) >= 2 or any("gift card" in f.lower() for f in red_flags):
        verdict = "HIGH RISK: Almost certainly a scam"
        risk_level = "High"
        advice = [
            "Do NOT click any links or download attachments.",
            "Do NOT reply to the text or call the number provided.",
            "Block the sender immediately.",
            "If it claims to be your bank or the postal service, open their official website or app separately.",
        ]
    elif len(red_flags) == 1:
        verdict = "SUSPICIOUS: Proceed with extreme caution"
        risk_level = "Medium"
        advice = [
            "Avoid clicking links.",
            "Verify with the supposed sender using a known, trusted phone number or their official app.",
        ]
    else:
        verdict = "LOW RISK: No obvious scam indicators detected"
        risk_level = "Low"
        advice = [
            "Always be cautious sharing passwords, PINs, or financial information.",
        ]

    return ScamReport(
        verdict=verdict,
        risk_level=risk_level,
        red_flags=red_flags,
        safety_advice=advice,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Scam Checker: Check suspicious text messages and emails.")
    parser.add_argument("--text", type=str, help="The suspicious message text")
    args = parser.parse_args()

    message = args.text or (
        "USPS Notice: Your package could not be delivered due to missing house number. "
        "Please update your address within 12 hours: http://usps-track-package.info"
    )
    if not args.text:
        print("No text passed. Using built-in sample message:\\n")

    print(f"MESSAGE BEING CHECKED:\\n\"{message}\"\\n")
    report = check_message(message)

    print("=" * 65)
    print(f"VERDICT   : {report.verdict}")
    print(f"RISK LEVEL: {report.risk_level}")
    print("=" * 65)
    print("RED FLAGS IDENTIFIED:")
    if report.red_flags:
        for f in report.red_flags:
            print(f"  • {f}")
    else:
        print("  • None detected.")
    print("\\nWHAT YOU SHOULD DO:")
    for a in report.safety_advice:
        print(f"  1. {a}" if a == report.safety_advice[0] else f"  • {a}")
    print("=" * 65)


if __name__ == "__main__":
    main()

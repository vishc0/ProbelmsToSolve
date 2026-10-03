"""
Scenario Scrutiny Engine
========================
Extracts and structures typed assertions, quantitative bounds, and assumptions
from natural language foresight documents to mitigate epistemic degradation ("Slopolis").
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path


class ClaimType(str, Enum):
    METRIC = "metric"
    ASSUMPTION = "assumption"
    CAPABILITY = "capability"
    CONSTRAINT = "constraint"
    TIMELINE = "timeline"
    GENERAL = "general"


class ProvenanceType(str, Enum):
    SOURCE_CLAIM = "source-claim"
    EXTERNAL_EVIDENCE = "external-evidence"
    AI_INFERENCE = "ai-inference"
    HUMAN_DECISION = "human-decision"


@dataclass
class ParsedClaim:
    claim_id: str
    source_id: str
    text: str
    claim_type: ClaimType
    provenance: ProvenanceType
    extracted_quantities: list[str]
    confidence: float


class ScenarioScrutinizer:
    def __init__(self, default_source_id: str = "generic-source") -> None:
        self.default_source_id = default_source_id
        # Regex patterns for identifying quantitative assertions
        self.metric_pattern = re.compile(
            r"(\b\d+(?:\.\d+)?(?:\s*(?:%|percent|OOMs?|H100e|MW|GW|chips?|years?|months?|USD|\$))\b)",
            re.IGNORECASE,
        )
        self.timeline_pattern = re.compile(r"\b(20\d\d)\b")
        self.assumption_cues = ["assume", "assuming", "if", "conditional on", "suppose", "premise"]
        self.constraint_cues = ["must", "prohibit", "forbidden", "cannot", "shall not", "mandatory"]

    def analyze_sentence(self, sentence: str, index: int, source_id: str | None = None) -> ParsedClaim | None:
        text = sentence.strip()
        if len(text) < 10:
            return None

        sid = source_id or self.default_source_id
        claim_id = f"{sid}-c{index:04d}"

        quantities = self.metric_pattern.findall(text)
        has_timeline = bool(self.timeline_pattern.search(text))
        lower = text.lower()

        if any(cue in lower for cue in self.assumption_cues):
            ctype = ClaimType.ASSUMPTION
        elif any(cue in lower for cue in self.constraint_cues):
            ctype = ClaimType.CONSTRAINT
        elif quantities:
            ctype = ClaimType.METRIC
        elif has_timeline:
            ctype = ClaimType.TIMELINE
        else:
            ctype = ClaimType.GENERAL

        return ParsedClaim(
            claim_id=claim_id,
            source_id=sid,
            text=text,
            claim_type=ctype,
            provenance=ProvenanceType.SOURCE_CLAIM,
            extracted_quantities=quantities,
            confidence=0.85 if quantities else 0.70,
        )

    def parse_document(self, text: str, source_id: str | None = None) -> list[ParsedClaim]:
        # Split on sentence boundaries and bullet points
        raw_sentences = re.split(r"(?<=[.!?])\s+|\n[-*]\s+|\n\d+\.\s+", text)
        claims: list[ParsedClaim] = []
        claim_idx = 1
        for s in raw_sentences:
            cleaned = s.strip()
            if not cleaned:
                continue
            claim = self.analyze_sentence(cleaned, claim_idx, source_id)
            if claim:
                claims.append(claim)
                claim_idx += 1
        return claims


def main() -> None:
    parser = argparse.ArgumentParser(description="Scenario Scrutiny Engine (CLI)")
    parser.add_argument("file", type=Path, help="Input Markdown or text file")
    parser.add_argument("--source-id", type=str, default="cli-input", help="Source provenance ID")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"Error: File {args.file} not found.")
        return

    text = args.file.read_text(encoding="utf-8")
    scrutinizer = ScenarioScrutinizer()
    claims = scrutinizer.parse_document(text, args.source_id)

    if args.json:
        data = [asdict(c) for c in claims]
        print(json.dumps(data, indent=2))
    else:
        print(f"Parsed {len(claims)} structured claims from {args.file.name}:")
        for c in claims[:10]:
            print(f"[{c.claim_type.value.upper()}] {c.claim_id}: {c.text}")
            if c.extracted_quantities:
                print(f"   Metrics: {c.extracted_quantities}")


if __name__ == "__main__":
    main()

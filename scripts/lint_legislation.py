#!/usr/bin/env python3
"""Mechanically flag common legislative drafting risks; review findings in context."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RULES = [
    ("L001", "High", r"\b(public interest|national interest|necessary|expedient|appropriate|satisfaction)\b", "Subjective threshold; define objective facts and evidence."),
    ("L002", "High", r"\bmay,? (?:in its|his|her) discretion\b|\babsolute discretion\b", "Open-ended discretion; state factors, limits, and review."),
    ("L003", "High", r"\b(good faith|immunity|no action.*shall lie)\b", "Potential immunity; preserve remedies for unlawful conduct."),
    ("L004", "Critical", r"\b(no court|shall not be called in question|final and shall not be questioned|bar of jurisdiction)\b", "Potential ouster of review; preserve constitutional and judicial remedies."),
    ("L005", "Medium", r"\b(exempt|exception|notwithstanding anything)\b", "Exception may be overbroad; narrow scope, duration, and oversight."),
    ("L006", "High", r"\bmay make rules\b|\bas may be prescribed\b", "Delegated power; bound subjects, publication, consultation, and review."),
    ("L007", "High", r"\bconfidential order\b|\bsecret\b|\bnot be published\b", "Secret-law risk; require publication or court-controlled confidentiality."),
    ("L008", "High", r"\b(emergency|temporary|until revoked|from time to time)\b", "Exceptional power may lack expiry; add duration and renewal safeguards."),
    ("L009", "High", r"\bwithout (?:notice|hearing|warrant|reasons)\b", "Process gap; require notice, hearing, reasons, and independent authorisation."),
    ("L010", "High", r"\b(offence|imprisonment|penalty|punishable)\b", "Penalty provision; verify clear elements, mental state, defences, and proportionality."),
    ("L013", "Medium", r"\b(delegate|contractor|outsourc|algorithm|automated)\b", "Indirect-evasion risk; apply safeguards to delegates and technology."),
    ("L015", "High", r"\b(surveillance|intercept|retain.*data|disclose.*data|monitor)\b", "Privacy/secrecy risk; add necessity, minimisation, authorisation, and audit."),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag common legislative drafting risks.")
    parser.add_argument("file", type=Path, help="Text or Markdown legal instrument")
    parser.add_argument("--json", action="store_true", help="Emit JSON findings")
    parser.add_argument("--strict", action="store_true", help="Return 1 if any finding exists")
    args = parser.parse_args()
    try:
        lines = args.file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"ERROR: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2
    findings = []
    for line_number, line in enumerate(lines, start=1):
        for rule_id, severity, pattern, fix in RULES:
            if re.search(pattern, line, flags=re.IGNORECASE):
                findings.append({"rule_id": rule_id, "severity": severity, "line": line_number, "excerpt": line.strip(), "suggested_review": fix})
    if args.json:
        print(json.dumps({"file": str(args.file), "findings": findings}, indent=2))
    elif findings:
        print(f"Legislative lint: {len(findings)} finding(s) in {args.file}")
        for item in findings:
            print(f"{item['rule_id']} [{item['severity']}] L{item['line']}: {item['excerpt']}")
            print(f"  Review: {item['suggested_review']}")
    else:
        print(f"Legislative lint: no mechanical findings in {args.file}")
    return 1 if findings and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())

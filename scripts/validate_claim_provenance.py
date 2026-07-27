#!/usr/bin/env python3
"""Validate structural completeness of a claim-level legal provenance ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

CLASSIFICATIONS = {"current_law", "historical_fact", "case_holding", "institutional_fact", "legal_interpretation", "policy_option", "draft_text"}
PRIMARY_REQUIRED = {"current_law", "historical_fact", "case_holding"}
CLAIM_FIELDS = {"id", "text", "classification", "status", "authorities", "limitations", "reviewer_action"}
AUTHORITY_FIELDS = {"treatment", "title", "authority_type", "issuer", "url", "document_date", "version_or_stage", "pinpoint", "retrieved_at"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a legal claim-provenance ledger JSON file.")
    parser.add_argument("file", type=Path, help="Ledger JSON file")
    args = parser.parse_args()
    try:
        ledger = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read ledger: {exc}", file=sys.stderr)
        return 2
    errors = []
    if ledger.get("schema_version") != "1.0" or not isinstance(ledger.get("document"), dict):
        errors.append("missing or unsupported schema_version/document metadata")
    claims = ledger.get("claims")
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty list")
        claims = []
    identifiers = set()
    for index, claim in enumerate(claims, start=1):
        prefix = f"claim {index}"
        missing = CLAIM_FIELDS - set(claim)
        if missing:
            errors.append(f"{prefix}: missing fields {sorted(missing)}")
            continue
        if claim["id"] in identifiers:
            errors.append(f"{prefix}: duplicate id {claim['id']}")
        identifiers.add(claim["id"])
        if claim["classification"] not in CLASSIFICATIONS:
            errors.append(f"{prefix}: invalid classification")
        authorities = claim["authorities"]
        if claim["classification"] in PRIMARY_REQUIRED and not authorities:
            errors.append(f"{prefix}: primary-source classification requires authority")
        for authority_index, authority in enumerate(authorities, start=1):
            authority_prefix = f"{prefix} authority {authority_index}"
            missing = AUTHORITY_FIELDS - set(authority)
            if missing:
                errors.append(f"{authority_prefix}: missing fields {sorted(missing)}")
                continue
            parsed = urlparse(authority["url"])
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{authority_prefix}: invalid direct URL")
            if not authority["pinpoint"].strip():
                errors.append(f"{authority_prefix}: pinpoint is required")
    if errors:
        print("Provenance validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Provenance validation passed: {len(claims)} claim(s) in {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

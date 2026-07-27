#!/usr/bin/env python3
"""Validate completeness and review metadata of the State/UT source queue."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

OFFICIAL_HOSTS = {"sansad.in", "www.sansad.in", "allahabadhighcourt.in", "www.allahabadhighcourt.in"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / "knowledge-base/state-ut-source-registry.json").read_text(encoding="utf-8"))
    queue = json.loads((root / "knowledge-base/state-ut-source-verification-queue.json").read_text(encoding="utf-8"))
    expected = {(j["code"], source_type) for j in registry["jurisdictions"] for source_type in registry["required_source_types"]}
    items = queue.get("items", [])
    found = {(item.get("jurisdiction_code"), item.get("source_type")) for item in items}
    errors = []
    if queue.get("schema_version") != "1.0" or found != expected or len(items) != len(expected):
        errors.append("queue does not contain exactly one item for every jurisdiction/source type")
    for item in items:
        if item.get("status") not in {"pending_verification", "candidate_pending_review", "verified", "rejected", "blocked", "not_applicable"}:
            errors.append("invalid queue status")
        if item.get("status") == "verified":
            for key in ("direct_official_url", "publisher", "verified_at", "verified_by"):
                if not item.get(key):
                    errors.append(f"{item.get('jurisdiction_code')}/{item.get('source_type')}: verified item missing {key}")
            parsed = urlparse(item.get("direct_official_url") or "")
            if parsed.scheme != "https" or not parsed.netloc or not (parsed.netloc in OFFICIAL_HOSTS or parsed.netloc.endswith(".gov.in") or parsed.netloc.endswith(".nic.in")):
                errors.append(f"{item.get('jurisdiction_code')}/{item.get('source_type')}: verified URL is not official HTTPS")
        if item.get("status") == "candidate_pending_review":
            for key in ("direct_official_url", "publisher", "candidate_recorded_at", "candidate_evidence_url"):
                if not item.get(key):
                    errors.append(f"{item.get('jurisdiction_code')}/{item.get('source_type')}: candidate missing {key}")
    if errors:
        print("State/UT source queue validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    verified = sum(item["status"] == "verified" for item in items)
    print(f"State/UT source queue validation passed: {len(items)} item(s), {verified} verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

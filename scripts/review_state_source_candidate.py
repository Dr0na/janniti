#!/usr/bin/env python3
"""Approve or reject a queued State/UT official-source candidate and promote approved sources."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jurisdiction_code")
    parser.add_argument("source_type")
    parser.add_argument("decision", choices=("approve", "reject"))
    parser.add_argument("--reviewer", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--health-status", choices=("reachable", "manual_access_required", "not_checked"), default="not_checked")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    queue_path = root / "knowledge-base/state-ut-source-verification-queue.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    matches = [item for item in queue["items"] if item["jurisdiction_code"] == args.jurisdiction_code.upper() and item["source_type"] == args.source_type]
    if len(matches) != 1 or matches[0]["status"] != "candidate_pending_review":
        raise SystemExit("a pending candidate is required for this decision")
    item = matches[0]
    timestamp = datetime.now(UTC).replace(microsecond=0).isoformat()
    item.update({"review_decision": args.decision, "review_reason": args.reason, "reviewed_by": args.reviewer, "reviewed_at": timestamp, "health_status": args.health_status})
    if args.decision == "reject":
        item["status"] = "rejected"
        queue_path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
        print(f"Candidate rejected: {item['jurisdiction_code']}/{item['source_type']}")
        return 0
    item.update({"status": "verified", "verified_at": timestamp, "verified_by": args.reviewer})
    queue_path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    registry_path = root / "knowledge-base/verified-source-registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    source_id = f"{item['jurisdiction_code'].lower()}-{item['source_type'].replace('_', '-')}"
    registry["sources"] = [source for source in registry["sources"] if source["id"] != source_id]
    registry["sources"].append({"id": source_id, "scope": item["jurisdiction"], "source_type": item["source_type"], "url": item["direct_official_url"], "publisher": item["publisher"], "verification_status": "official", "last_verified": timestamp[:10], "verified_by": args.reviewer, "review_reason": args.reason})
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    print(f"Candidate approved and promoted: {source_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

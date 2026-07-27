#!/usr/bin/env python3
"""Register an official-source candidate without treating it as verified."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse


def official_https(url: str) -> bool:
    host = urlparse(url).hostname or ""
    official_hosts = {"sansad.in", "www.sansad.in", "allahabadhighcourt.in", "www.allahabadhighcourt.in"}
    return urlparse(url).scheme == "https" and (host.endswith(".gov.in") or host.endswith(".nic.in") or host in official_hosts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jurisdiction_code")
    parser.add_argument("source_type")
    parser.add_argument("url")
    parser.add_argument("--publisher", required=True)
    parser.add_argument("--evidence-url", required=True)
    parser.add_argument("--limitations", default="Pending reviewer assessment.")
    args = parser.parse_args()
    if not official_https(args.url):
        raise SystemExit("candidate URL must be an official HTTPS government domain")
    root = Path(__file__).resolve().parents[1]
    path = root / "knowledge-base/state-ut-source-verification-queue.json"
    queue = json.loads(path.read_text(encoding="utf-8"))
    matches = [item for item in queue["items"] if item["jurisdiction_code"] == args.jurisdiction_code.upper() and item["source_type"] == args.source_type]
    if len(matches) != 1:
        raise SystemExit("queue item not found or ambiguous")
    item = matches[0]
    if item["status"] == "verified":
        raise SystemExit("refusing to replace a verified source; record a superseding review instead")
    item.update({"status": "candidate_pending_review", "direct_official_url": args.url, "publisher": args.publisher, "candidate_recorded_at": datetime.now(UTC).replace(microsecond=0).isoformat(), "candidate_evidence_url": args.evidence_url, "access_language_archive_limitations": args.limitations})
    path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    print(f"Candidate recorded: {item['jurisdiction_code']}/{item['source_type']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

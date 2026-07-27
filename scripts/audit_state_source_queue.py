#!/usr/bin/env python3
"""Audit every State/UT source-queue record without accepting sources automatically."""

from __future__ import annotations

import argparse
import json
import socket
import ssl
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path


def probe(url: str, timeout: float) -> dict:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "JanNiti-Source-Audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"result": "reachable", "http_status": response.status}
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 405}:
            return {"result": "manual_access_required", "http_status": exc.code}
        return {"result": "failed", "http_status": exc.code}
    except urllib.error.URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.gaierror):
            return {"result": "network_unavailable", "error": str(exc)}
        if isinstance(reason, ssl.SSLError) or "SSL:" in str(reason):
            return {"result": "inconclusive_transport_error", "error": str(exc)}
        if isinstance(reason, TimeoutError):
            return {"result": "inconclusive_transport_error", "error": str(exc)}
        return {"result": "failed", "error": str(exc)}
    except (TimeoutError, OSError) as exc:
        return {"result": "inconclusive_transport_error", "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="perform HEAD checks for records with direct URLs")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--output", type=Path, default=Path("knowledge-base/state-ut-source-audit-report.json"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    queue = json.loads((root / "knowledge-base/state-ut-source-verification-queue.json").read_text(encoding="utf-8"))
    records = []
    for item in queue["items"]:
        record = {"jurisdiction_code": item["jurisdiction_code"], "jurisdiction": item["jurisdiction"], "source_type": item["source_type"], "queue_status": item["status"], "url": item.get("direct_official_url")}
        if item["status"] == "not_applicable":
            record["audit_result"] = "not_applicable"
        elif not item.get("direct_official_url"):
            record["audit_result"] = "unresolved_no_candidate"
        elif args.online:
            record["audit_result"] = probe(item["direct_official_url"], args.timeout)
        else:
            record["audit_result"] = "not_checked_offline"
        records.append(record)
    counts = {}
    for record in records:
        result = record["audit_result"] if isinstance(record["audit_result"], str) else record["audit_result"]["result"]
        counts[result] = counts.get(result, 0) + 1
    report = {"schema_version": "1.0", "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat(), "online": args.online, "acceptance_status": "audit_only_pending_human_review", "summary": counts, "records": records}
    output = args.output if args.output.is_absolute() else root / args.output
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"State/UT source audit written: {len(records)} record(s); {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

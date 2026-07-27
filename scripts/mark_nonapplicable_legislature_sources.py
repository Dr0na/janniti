#!/usr/bin/env python3
"""Mark legislature-source rows not applicable where a Union Territory has no legislature."""

from __future__ import annotations

import json
from pathlib import Path


NO_LEGISLATURE = {"AN", "CH", "DH", "LA", "LD"}
RATIONALE = (
    "This Union Territory has no elected legislature. Legislative authority is exercised "
    "through Parliament and the applicable Union Territory administration; use the relevant "
    "Parliament, India Code, Gazette, and UT-administration sources for the matter."
)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = root / "knowledge-base/state-ut-source-verification-queue.json"
    queue = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for item in queue["items"]:
        if item["jurisdiction_code"] not in NO_LEGISLATURE or item["source_type"] != "legislature":
            continue
        if item["status"] != "pending_verification":
            continue
        item.update({
            "status": "not_applicable",
            "direct_official_url": None,
            "publisher": "Parliament of India and relevant Union Territory administration",
            "access_language_archive_limitations": RATIONALE,
        })
        changed += 1
    path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    print(f"Marked {changed} legislature source record(s) not applicable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

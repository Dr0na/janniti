#!/usr/bin/env python3
"""Record all uncovered State/UT High Court portals as review-only candidates.

The entries are deliberately not accepted as verified sources.  A reviewer must
confirm the judgments/search route, ownership, scope, and current access before
changing any queue status to ``verified``.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


SUPREME_COURT_JURISDICTION = "https://www.sci.gov.in/jurisdiction/"
PORTALS = {
    "AN": "https://www.calcuttahighcourt.gov.in/", "AP": "https://aphc.gov.in/",
    "AR": "https://ghconline.gov.in/", "AS": "https://ghconline.gov.in/",
    "BR": "https://patnahighcourt.bihar.gov.in/", "CH": "https://www.hcph.gov.in/",
    "CT": "https://highcourt.cg.gov.in/", "DH": "https://bombayhighcourt.nic.in/",
    "GA": "https://bombayhighcourt.nic.in/", "HP": "https://highcourt.hp.gov.in/",
    "HR": "https://www.hcph.gov.in/", "JH": "https://jharkhandhighcourt.nic.in/",
    "JK": "https://jkhighcourt.nic.in/", "LA": "https://jkhighcourt.nic.in/",
    "LD": "https://highcourt.kerala.gov.in/", "ML": "https://meghalayahighcourt.nic.in/",
    "MN": "https://hcmimphal.nic.in/", "MP": "https://mphc.gov.in/",
    "MZ": "https://ghconline.gov.in/", "NL": "https://ghconline.gov.in/",
    "OD": "https://orissahighcourt.nic.in/", "PB": "https://www.hcph.gov.in/",
    "PY": "https://hcmadras.tn.gov.in/", "RJ": "https://hcraj.nic.in/",
    "SK": "https://highcourtofsikkim.nic.in/", "TR": "https://thc.nic.in/",
    "TS": "https://tshc.gov.in/", "UK": "https://highcourtofuttarakhand.gov.in/",
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = root / "knowledge-base/state-ut-source-verification-queue.json"
    queue = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for item in queue["items"]:
        if item["source_type"] != "high_court_judgments" or item["jurisdiction_code"] not in PORTALS:
            continue
        if item["status"] != "pending_verification":
            continue
        item.update({
            "status": "candidate_pending_review",
            "direct_official_url": PORTALS[item["jurisdiction_code"]],
            "publisher": "Relevant High Court of India",
            "candidate_recorded_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
            "candidate_evidence_url": SUPREME_COURT_JURISDICTION,
            "access_language_archive_limitations": (
                "Candidate portal only. A human reviewer must confirm the current "
                "judgment/search route, official ownership, coverage, and access "
                "conditions before verification."
            ),
        })
        changed += 1
    path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded {changed} High Court portal candidate(s); none verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

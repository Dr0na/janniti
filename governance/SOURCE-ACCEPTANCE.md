# Official Source Acceptance Gate

A fetched page, downloaded file, checksum, or automated health result is not controlling law by itself. Before JanNiti accepts a new or changed source for a consequential matter, a designated human reviewer must record:

1. Direct official URL, publisher, document identity, jurisdiction, and legal status.
2. Version/stage, publication/assent/commencement date, and controlling pinpoint.
3. Whether the document is complete, legible, authentic, and the authoritative language/version.
4. Snapshot hash, retrieval time, access limitation, and any OCR/translation issue.
5. Every impacted matter, claim, draft, monitor, and public-facing statement.
6. Required correction, withdrawal, revalidation, public notice, and deadline.

No agent may mark a source change as accepted merely because a URL responded, a hash changed, or a diff was generated. An urgent rights risk requires an interim safeguard and prompt qualified legal review.

## State/UT candidate workflow

Use `scripts/register_state_source_candidate.py` to add a candidate to the queue. It remains `candidate_pending_review`; it is not a verified source. A designated reviewer then uses `scripts/review_state_source_candidate.py` to approve or reject it, recording the reviewer, date, reason, and health/access outcome. Approval promotes the exact reviewed URL into `verified-source-registry.json`; rejection preserves the audit record and does not change the registry.

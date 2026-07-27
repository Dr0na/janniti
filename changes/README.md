# Legal Change Monitor

This directory preserves versioned source snapshots and records how legal changes affect dependent work. It is a provenance and alert system, not a substitute for checking official publication, commencement, judicial status, or qualified legal advice.

## Workflow

1. Use `watchlist.json` to identify high-value official sources.
2. Save immutable snapshots in `snapshots/` with source ID, date/time, file extension, and checksum.
3. Diff an old and new snapshot; record the change in `events/` using the template.
4. Map every affected claim and artifact, revalidate it, and record correction/withdrawal where required.
5. Never overwrite source text or mark a change accepted before human/legal review where material.

Use network fetching only where authorised, respecting source conditions and rate limits. Manual source registration is preferred when an official source uses CAPTCHA, access restrictions, or unstable rendering.

## Acquisition and acceptance

Use `scripts/snapshot_legal_source.py` only on an authorised local copy of an official source. It creates an immutable hash-pinned snapshot with `pending_human_review` status; it never fetches or accepts a source automatically. Use `scripts/assess_source_change_impact.py <official-url> --output <report.json>` to identify affected matters, then follow `governance/SOURCE-ACCEPTANCE.md` before treating a change as controlling.

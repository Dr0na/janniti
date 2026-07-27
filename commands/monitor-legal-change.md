# /monitor-legal-change

Monitor a legal source, instrument, bill, rule, notification, judgment, or official repository for change. Read `changes/README.md`, `changes/watchlist.json`, `knowledge-base/README.md`, and `references/document-security.md`. Store each new monitoring run in the matter's `14-legal-change-monitoring/` folder.

1. Fetch only authorised official sources, or register an authorised manual copy, with source URL, retrieval date, document title, legal status, and checksum.
2. Store each immutable snapshot under the output folder's `snapshots/` directory; never overwrite a prior version.
3. Compare versions with `python3 scripts/diff_legal_versions.py <old> <new>`.
4. Create a change event under the output folder's `events/` directory using `templates/legal-change-event.example.json` and validate it with `scripts/validate_legal_change_event.py`.
5. Map affected provenance claims, legal drafts, validations, power maps, monitors, consultation plans, scorecards, and public summaries.
6. Classify impact: informational, review required, urgent rights risk, or withdrawal/correction required. State who reviews, deadline, public notice, and interim safeguard.
7. Do not treat an online text change as a legal change until status, commencement, version, authority, and publication are verified.

Output: source status; version diff; legal-status assessment; dependency/impact register; required revalidation; public correction notice if needed; and residual uncertainty.

# Maintenance and Source Refresh

## Quarterly review

1. Confirm each URL and issuing body in `knowledge-base/sources.yaml`.
   Run `python3 scripts/check_source_health.py --offline` in every environment; run the online mode only where network access is approved.
2. Check changes to harness discovery rules, command formats, and security models.
3. Review official Constitution, Gazette, parliamentary, and court source availability.
4. Run the citation preflight on new legal research artifacts and review warnings manually.
   Run `python3 scripts/validate_acceptance_suite.py`, then exercise the acceptance cases in each supported harness after any material instruction or harness change.
5. Red-team one command against selective enforcement, censorship, capture, discrimination, and emergency abuse.
6. Record the outcome, gaps, and corrective changes in `governance/CHANGELOG.md`.

## Per-deliverable review

- Retrieve current primary sources; do not rely on cached text alone.
- Verify status, version, commencement, amendment, and subsequent judicial history.
- Apply ethics, citation verification, and constitutional stress testing.
- Register locally retained authorised documents in `knowledge-base/local/manifest.json`.

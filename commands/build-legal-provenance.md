# /build-legal-provenance

Create or update a claim-level provenance ledger for the supplied legal work. Read `templates/claim-provenance.example.json`, `knowledge-base/README.md`, and `references/legal-ethics.md`.

For every material proposition, create one claim record in the matter's `06-provenance/` folder containing claim text; classification; jurisdiction/as-of date; authority title/type/issuer/direct URL/document date/version/pinpoint/retrieval date/treatment; subsequent-history check; and limitations/reviewer action.

Classify claims as `current_law`, `historical_fact`, `case_holding`, `institutional_fact`, `legal_interpretation`, `policy_option`, or `draft_text`. Use an official primary authority for every material `current_law`, `case_holding`, or `historical_fact` claim unless an explicit limitation explains why this is unavailable.

Run `python3 scripts/validate_claim_provenance.py <ledger.json>` before delivery. A valid ledger format does not prove the underlying source is accurate; open and check it.

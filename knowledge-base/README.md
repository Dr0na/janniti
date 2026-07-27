# Indian Public-Law Knowledge Base

## Purpose and scope

This is a retrieval-first, provenance-preserving knowledge base for Indian constitutional and public-law research from 15 August 1947 onward, with the Constitution-making record beginning in 1946 because it is indispensable context. It covers:

- Constituent Assembly draft-making debates and Constituent Assembly (Legislative) debates;
- the Constitution, every constitutional amendment, and official amendment history;
- Central and State/Union Territory Acts, subordinate legislation, ordinances, and Gazette publications;
- introduced, pending, negatived, passed, and assented bills, including versions and legislative status;
- Lok Sabha, Rajya Sabha, Provisional Parliament, and relevant historical debates;
- parliamentary committee material, papers laid, presidential addresses, budget material, and legislative-history records;
- Supreme Court and High Court judgments/orders, with authoritative text and case metadata where available.

The pack does **not** copy millions of pages into a prompt or present a frozen download as complete. It directs the agent to the authoritative collection at query time, records provenance and version, and requires the controlling primary text. This is necessary because laws, bills, court records, and repositories change; the Parliament Digital Library alone reports more than 1.4 million items.

## Required retrieval sequence

1. Identify the question’s jurisdiction, period, instrument, and issue.
2. Read `sources.yaml`; select every mandatory collection for that question.
3. Retrieve the original/official text and save these metadata in the response or research log: source URL, publisher, retrieval date, document title, date, version/stage, page/paragraph/section, and hash where a local copy is authorised.
4. Establish current law from the official consolidated text and Gazette; establish historical text from the enactment/version in force on the relevant date.
5. Use debates, bill versions, and committee records only to explain context or legislative history. State their weight and do not let them override enacted language or binding precedent.
6. Use court decisions from official repositories; check subsequent history, review/appeal status, and later contrary authority before relying on a holding.

## Coverage and integrity rules

- Do not call a source “complete” merely because search returned no result. Report repository gaps, OCR limits, access restrictions, language, and missing versions.
- Preserve original PDFs/HTML and a text-extracted derivative separately. Never overwrite source files or silently correct OCR.
- Keep a document manifest containing stable identifier, source URL, publisher, document type, date, language, checksum, retrieval date, and rights/access note.
- Prefer English and Hindi official versions where both exist; report translation status and resolve material discrepancy against the legally authoritative version.
- Never train, fine-tune, or reproduce a restricted source without separate permission and legal review. This pack is a research-routing layer, not a claim of corpus rights.

## Search conventions

Search by Act/Bill number and year, title, Article/section, ministry, House, member, session/date, case number, neutral citation, party names, and key phrase. Use quoted terms and capture alternate spellings/transliterations. Search related instruments: parent Act, amendment Act, rules, notifications, bill versions, debate, committee report, Gazette, and subsequent case law.

## State and Union Territory coverage

`state-ut-source-registry.json` lists all 28 States and 8 Union Territories and the four official source types required for each: legislature, law department, official Gazette, and High Court judgments. It is an authoritative-directory routing layer, not proof that a linked portal is complete or current. Resolve the direct official repositories for the matter, record them in the research pack and machine-readable manifest, and use `scripts/validate_state_ut_source_registry.py` to ensure full jurisdiction coverage.

`state-ut-source-verification-queue.json` turns this coverage requirement into 144 auditable records: legislature, law department, official Gazette, and High Court judgment source for each jurisdiction. Build it with `scripts/build_state_ut_source_queue.py`; validate it with `scripts/validate_state_ut_source_queue.py`. A record may be marked `verified` only with a direct official HTTPS URL, publisher, reviewer, verification date, health status, and access/language/archive limitation.

Use `scripts/audit_state_source_queue.py --online` to audit all records in one batch. It checks only queued URLs, reports unresolved records with no candidate, and writes `state-ut-source-audit-report.json`; it never promotes a source or substitutes an HTTP response for legal verification.

## Local collection option

If a local corpus is later authorised, use `knowledge-base/local/` for the immutable-cache protocol and provenance manifest. Keep a refresh schedule, source-by-source access rules, and a deletion/correction log. Do not start bulk harvesting without agreed storage, licensing, rate-limit, security, and update requirements.

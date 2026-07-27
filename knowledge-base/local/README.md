# Local Authorised Document Index

Use this optional index only for documents that the repository owner is authorised to retain. It is not a downloader, a substitute for official sources, or proof that a cached copy is current.

## Registering a document

1. Place the immutable original in `knowledge-base/local/documents/` using a stable file name. Do not alter it after registration.
2. Add one entry to `manifest.json` using the schema below.
3. Include source URL, issuing body, document date, retrieval date, legal status/version, language, checksum, rights/access note, and precise local path.
4. Store OCR/extracted text separately, identify it as derivative, and link it to the original checksum.
5. On correction, supersession, or removal, append a new status/history entry; do not silently replace the original record.

## Manifest schema

Each `documents[]` item must contain:

| Field | Meaning |
|---|---|
| `id` | Stable local identifier. |
| `title`, `document_type`, `jurisdiction` | Identify the legal record. |
| `issuing_body`, `document_date`, `legal_status_or_stage` | Establish authority and time. |
| `source_url`, `retrieved_at`, `source_pinpoint` | Preserve provenance. |
| `language`, `local_path`, `sha256` | Identify the retained immutable copy. |
| `rights_access_note`, `history` | Record permission and later corrections/supersession. |

Do not add credentials, personal data, sealed records, privileged material, copyrighted material without permission, or scraped collections that exceed source terms, rate limits, or agreed storage limits.

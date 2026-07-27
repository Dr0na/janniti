# /verify-legal-citations

Verify the supplied legal draft, review, memorandum, or answer before it is delivered. If no target is supplied, request a file or text.

Read `AGENTS.md`, `references/legal-ethics.md`, and `knowledge-base/README.md`. For India-related material, use `knowledge-base/sources.yaml` and `references/india-constitutional-research.md`.

## Verification rules

1. List every material claim of current law, legal history, case holding, bill status, institutional fact, quantitative fact, and constitutional interpretation.
2. Attach a direct primary source with an exact Article, section, clause, paragraph, page, case number, neutral citation, or dated record.
3. Confirm source authority, document version/stage, publication date, retrieval date, and whether the text was in force on the relevant date.
4. Check whether later amendment, repeal, commencement, appeal, review, overruling, stay, or contrary authority affects the claim.
5. Flag unsupported claims, secondary-only support, inaccessible sources, ambiguous pinpoints, stale sources, wrong jurisdiction, hallucinated citations, and claims stronger than their authority.
6. Keep policy recommendations and draft text distinct from claims about existing law.

## Required output

| Claim | Classification | Source and pinpoint | Status | Required correction |
|---|---|---|---|---|

End with one of: **verified**, **verified with stated limitations**, or **not safe to rely on**. Do not label a document verified when a material claim lacks a checked primary source.

When working from a local Markdown file, run `scripts/verify_legal_citations.py <file>` as a mechanical preflight. Treat its result as a warning system, not a substitute for legal verification.

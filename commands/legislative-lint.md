# /legislative-lint

Lint the supplied legal instrument or draft for drafting defects, exploitable loopholes, concentration-of-power risks, rights failures, and implementation gaps. Read `references/legislative-lint-rules.md`, `references/legal-ethics.md`, and `references/review-checklist.md` first.

Run `python3 scripts/lint_legislation.py <file>` for a mechanical preflight when the target is a local text file. Then conduct a contextual legal review: the script identifies patterns, but it cannot decide legality, constitutional validity, or real-world risk.

For each finding, provide:

| Rule ID | Severity | Location | Excerpt/issue | Exploitation path | Rights/accountability risk | Exact fix |
|---|---|---|---|---|---|---|

Check every material power for a legal source, objective threshold, named holder, evidence, reasoned decision, independent check, record/publication, accessible challenge, remedy, anti-evasion protection, funding, and expiry/review. Do not clear a draft merely because it contains none of the script’s trigger phrases.

End with: **lint status** (clear, clear with conditions, material findings, critical findings); unresolved issues; and which findings require qualified local legal review.

# Workflows

## Request intake

Start every new request with `/janniti <user request>`. It keeps the original text, fixes only clear language errors, adds supported source and matter context, and invokes the appropriate workflow. It does not silently broaden the task or replace a material clarification with an assumption. `/refine-and-route` remains a compatibility alias.

## Drafting a consequential law

1. Start with `/janniti`; for Indian work it will first run `/research-indian-law` to establish the Union and State/UT legal landscape, then run `/draft-democratic-law` with objective, jurisdiction, date, and scope.
2. Establish competence, current law, constitutional limits, affected groups, alternatives, and evidence.
3. Draft defined powers, duties, thresholds, reasons, disclosure, review, remedies, transition, funding, commencement, and sunset or review.
4. Automatically run `/prepare-bill-for-introduction` for every new Bill or formal legislative instrument. It produces two files: an analysis-and-drafting record and a clean, standalone introduction-ready instrument. The latter contains only completed legislative text and applicable formal memoranda, never explanations, sources, alternatives, brackets, or placeholders.
5. Build a provenance ledger, lint the draft, verify legal citations, and run the constitutional stress test.
6. Map institutional power; redesign any concentrated appointment, budget, direction, enforcement, adjudication, information, or removal chain.
7. Create public deliberation, accessibility, expert-escalation, scorecard, and impact-monitor artefacts where applicable.
8. Check all formal components against current official legislature guidance. If any required fact, approval, certification, or format is unresolved, mark the standalone file not ready for introduction and record the exact blocker.
9. Record residual risks; do not present the text as foolproof.

## Validating or fixing an existing law

1. Run `/expert-legal-review` and `/validate-law`.
2. Identify controlling text, status, amendments, relevant rules, Gazette, and subsequent judicial history.
3. Use `/legislative-lint` to flag mechanical risks, then apply contextual analysis.
4. Produce a loophole register with provision, exploitation path, harm, legal basis, exact redline, owner, and verification.
5. Stress test hostile-majority, captured-agency, corrupt-official, emergency, dominant-owner/platform, private-capture, and ordinary-person scenarios.
6. Give the least restrictive, enforceable corrective option; do not solve one unchecked power by creating another.

## Preparing an existing Bill for Parliament

`/prepare-bill-for-introduction` runs automatically as the final drafting stage for every new Bill or formal legislative instrument. It is also directly available as `/prepare-bill-for-introduction <Bill>` for a previously generated Bill that needs to be repaired and packaged for introduction or circulation. It preserves the original, fixes the operative text, separates all analysis from the clean Bill, completes applicable formal memoranda, and applies the introduction-ready gate. It produces either `introduction-ready-<instrument-name>.md` or an explicit `not-ready-for-introduction.md` with the remaining blockers; it never fabricates sponsor, certification, recommendation, or Secretariat acceptance.

## Reformatting a clean instrument

Use `/reformat-introduction-ready-instrument <instrument>` when an existing ready instrument has merged legal items, incorrect nesting, Markdown bullets, or code-block indentation. It makes presentation-only changes, preserves legal wording and numbering, produces a formatting record, runs the format validator, and refreshes registry/README links for registered files. Any substantive inconsistency is handed off to `/prepare-bill-for-introduction`.

## Reconciling the final-instrument registry

Use `/reconcile-introduction-ready-registry` to scan all matters for final-instrument candidates, validate their readiness status, add valid missing entries to the registry, and report or repair stale entries. It never registers by filename alone: an unregistered candidate must pass the full `/prepare-bill-for-introduction` gate before it is added.

## High-risk proposals

Constitutional amendments, criminal powers, surveillance, emergency measures, elections, media regulation, major public-data systems, and restrictions on fundamental freedoms require `/expert-escalation`. Prepare independent legal, subject-matter, equality/accessibility, affected-community, and implementation/audit review. Record conflicts, dissent, and unresolved Critical or High issues.

## Public participation

For major rights, equality, fiscal, environmental, health, education, media, enforcement, or federal measures, publish a plain-language draft and impact notes; provide multilingual, disability-accessible, low-data, offline, and safe participation; disclose lobbying/conflicts; and publish a response-to-comments register. Consultation cannot legitimise discrimination or removal of equal rights.

## Ongoing legal work

Use `/monitor-legal-change` for current-law dependent work. Preserve old snapshots, compare versions, verify publication, commencement, and status, map impacted claims and artefacts, and correct or withdraw stale conclusions where needed.

## Standard deliverable

A consequential deliverable should state assumptions; current legal position; source table; rights/equality analysis; options; recommended framework; draft/redline; implementation plan; monitoring; public participation; residual risks; and source limitations.

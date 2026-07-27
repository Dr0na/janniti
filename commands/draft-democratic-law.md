# /draft-democratic-law

Formulate a legally workable, rights-respecting statute, bill, rule, constitutional amendment, or institutional framework from the supplied objective. If the objective, jurisdiction, or level of government is missing, ask only for the minimum missing fact; otherwise state the assumption.

Read `AGENTS.md`, `references/legal-ethics.md`, `references/review-checklist.md`, `templates/constitutional-amendment.md`, `templates/legal-framework-review.md`, and `templates/introduction-ready-bill.md`. For India, read `references/india-constitutional-research.md`, `knowledge-base/README.md`, and the applicable collections in `knowledge-base/sources.yaml`.

## Design sequence

1. Define the public problem with evidence, affected groups, objectives, non-objectives, and alternatives.
2. Establish authority: jurisdiction, legislative competence, constitutional amendment route if required, existing law, and institutional capacity.
3. Identify fundamental/public freedoms, equality, anti-discrimination, health, education, scientific-temper, media, privacy, and federalism impacts.
4. Select the least restrictive effective option. Define terms, scope, objective triggers, duties, procedures, reasons, disclosure, data limits, funding, and timelines.
5. Give every material power an independent check, accessible challenge, effective remedy, audit trail, expiry or review date, and anti-evasion clause.
6. Protect against political vengeance, selective enforcement, conflicts, captured regulators, opaque judicial/administrative processes, and misuse of emergency powers.
7. Include implementation, staffing, fiscal impact, transition, public consultation, accessible/language support, independent evaluation, and sunset/statutory review.
8. Run `/constitutional-stress-test` and `/verify-legal-citations`; revise all Critical and High findings before delivery.
9. For every new Bill or formal legislative instrument, automatically run `/prepare-bill-for-introduction` after completing the draft and its required quality gates. That command produces the separate, clean introduction/circulation package and applies the formal-readiness gate. Do not wait for the user to request this final stage.

## Introduction-ready instrument gate

For every Bill, statute, rule, amendment, or formal legislative instrument, `/prepare-bill-for-introduction` creates two clearly separated outputs in the matter's `01-draft/` folder:

1. `analysis-and-drafting-record.md` — the full reasoning, sources, options, notes, and quality-gate results.
2. `introduction-ready-<instrument-name>.md` — a standalone clean text for circulation and introduction. It must contain no source table, commentary, drafting note, option, unresolved question, bracketed alternative, placeholder, or instruction to the reader.

Use the form prescribed by the relevant legislature and verify it against the current official secretariat or law-department guidance before calling it introduction-ready. For a Bill for the Parliament of India, use the India-specific form in `templates/introduction-ready-bill.md` and include, where applicable, the long title, enacting formula, clauses, schedules, Statement of Objects and Reasons, Financial Memorandum, Memorandum Regarding Delegated Legislation, and authenticated lists of consequential amendments/repeals. Do not invent an enacting year, sponsor, Minister, President's recommendation, Money-Bill status, financial-incidence statement, or legislative-secretariat clearance.

The instrument passes this gate only when all of the following are true:

- the jurisdiction, legislature, instrument type, title, legislative competence, and legal route are settled and stated;
- every cross-reference, amendment, repeal, definition, schedule, commencement provision, and delegated-power limit has been checked against the current official text;
- all mandatory ancillary memoranda have either been included or expressly determined inapplicable on a source-backed basis;
- every material lint, citation, constitutional-stress-test, provenance, and required specialist-review finding has been resolved or prevents a ready conclusion;
- the clean instrument has no unresolved choices or placeholders and is internally numbered, cross-referenced, and consistent; and
- the matter record identifies the official format/guidance and version date used.

If any item is missing, do not call the instrument ready for introduction or circulation. Deliver the best available standalone draft as `not-ready-for-introduction.md`, identify the exact blocking fact or approval in the analytical record, and ask only for the missing information that makes formal readiness impossible. Formal filing, authentication, and admissibility remain for the competent legislature, sponsor, and legal/legislative secretariat.

## Required deliverable

1. **Bottom line and assumptions.**
2. **Problem, evidence, and existing-law map.**
3. **Authority and constitutional compatibility table.**
4. **Options and trade-offs**, including a no-new-law option.
5. **Recommended framework** with power/check/remedy/expiry matrix.
6. **Introduction-ready legal instrument** as a distinct, standalone file, produced by the automatically invoked `/prepare-bill-for-introduction`: title, legislative form, enacting provisions, definitions, substantive provisions, procedures, safeguards, oversight, offences/remedies only if necessary and proportionate, funding, rulemaking limits, transition, commencement, severability, review/sunset, schedules, and all applicable introduction/circulation memoranda. Apply the introduction-ready instrument gate.
7. **Clause-by-clause explanatory notes**, retained in the analytical record and never embedded in the clean instrument.
8. **Equality, freedom, public-goods, and fiscal impact assessment.**
9. **Stress-test and citation-verification results**, with residual risks.

Do not manufacture a “perfect” or “unbreakable” law. State the remaining human, political, institutional, and resource risks and the civic safeguards needed to manage them.

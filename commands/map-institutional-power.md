# /map-institutional-power

Map the institutions, offices, private delegates, public funds, information systems, and oversight bodies created or affected by the supplied law or framework. Identify concentration, capture, circular oversight, and single-point-of-failure risks; design structural fixes.

Read `references/legal-ethics.md`, `references/review-checklist.md`, `commands/constitutional-stress-test.md`, and `templates/institutional-power-map.example.json`. For India, also apply the Constitution, federalism, institutional-independence, and rights requirements in `references/india-constitutional-research.md`.

## Mapping method

1. List every actor: legislature, executive office, minister, agency, police/investigator, prosecutor, court, regulator, auditor, election body, media/platform/contractor, public body, citizen/public forum, and funder.
2. Record each control relationship: appointment, removal, funding, direction, rulemaking, investigation, prosecution, adjudication, audit, information/data, emergency, contracting, and appeal/review.
3. Identify whether the same actor, aligned bloc, or opaque private intermediary controls multiple critical levers over the same target.
4. Identify circular chains: A appoints B, B audits A, A controls B’s budget, or a body investigates, prosecutes, decides, and reviews itself.
5. Simulate capture by a hostile majority, captured enforcement agency, corrupt regulator, dominant owner/platform, wealthy private actor, emergency executive, and ordinary person seeking remedy.
6. Write an immutable public record of the map in the matter's `08-institutional-power-map/` folder using the template and run `python3 scripts/analyze_power_map.py <map.json>`.

## Required output

1. **Power map:** table and Mermaid diagram showing controller → target → power → check.
2. **Concentration register:** actor/bloc, levers controlled, target, severity, exploitation path, and evidence.
3. **Circularity and dependency register:** appointment, funding, audit, evidence, enforcement, and appeal loops.
4. **Capture simulation:** scenario, likely path, right/public interest harmed, existing defence, failure, and remedy.
5. **Structural fixes:** staggered and plural appointment, fixed independent budget, written-direction ban, separation of functions, independent authorisation, transparent record, external audit, accessible challenge, removal due process, and sunset/review as applicable.
6. **Residual risk:** state plainly which concentration cannot be removed and what democratic/public oversight remains necessary.

Treat a mechanical finding as a prompt for contextual review, not a final constitutional conclusion.

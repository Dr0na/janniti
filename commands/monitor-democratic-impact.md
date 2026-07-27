# /monitor-democratic-impact

Design a post-enactment Democratic Impact and Implementation Monitor for the supplied law, amendment, rule, programme, or institution. Read `references/review-checklist.md`, `references/legal-ethics.md`, `commands/map-institutional-power.md`, and `templates/democratic-impact-monitor.example.json`.

## Required design

1. State objective, non-objectives, affected groups, baseline, and causal assumptions.
2. Define public indicators for rights/freedoms, equality and disparate impact, political-vendetta/selective-enforcement risk, public access, education/health where relevant, integrity/corruption, media/information, cost, and implementation capacity.
3. Specify data source, collection frequency, quality/uncertainty, privacy/minimisation, language/disability access, publication format, and independent validation for every indicator.
4. Create accessible complaints, whistleblower, appeal, legal-aid/referral, and retaliation-protection routes. Publish anonymised outcomes and timeliness data.
5. Give an independent auditor or plural oversight body a fixed schedule, source access, public reporting duty, conflict rules, and a remedy if information is withheld.
6. Set quantitative or qualitative review triggers: rights harm, disparate impact, corruption, selective enforcement, cost overrun, missed service standard, data breach, capture signal, or emergency misuse.
7. For each trigger, define the responsible body, public notice, interim protection, corrective action, judicial/legislative referral, and deadline. Include suspension, amendment, and repeal/sunset routes where proportionate.
8. Write the plan in the matter's `09-democratic-impact-monitor/` folder and run `python3 scripts/validate_democratic_monitor.py <plan.json>`.

## Required output

1. Baseline and affected-group table.
2. Indicator and data-governance register.
3. Public-accountability schedule: publication, audit, hearings, consultation, and legislative review.
4. Complaint/whistleblower/remedy flow.
5. Trigger-and-correction register.
6. Residual uncertainty, anti-gaming safeguards, and review/sunset recommendation.

Do not use measurement as a pretext for surveillance, exclusion, secrecy, or delay of remedies. The monitor must remain independently reviewable and cannot be controlled by the same authority whose conduct it assesses.

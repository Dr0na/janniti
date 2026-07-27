# /expert-escalation

Prepare an independent-review brief for a high-risk legal proposal or conclusion. Use for constitutional amendment, criminal law, surveillance, emergency powers, elections, media regulation, judicial accountability, large-scale data systems, or any restriction of fundamental freedoms.

Identify the question, jurisdiction, affected groups, current law, contested propositions, adverse authority, evidence gaps, rights risks, concentration/capture risks, implementation impact, and decisions that require qualified local counsel or affected-community review. Attach the provenance ledger, lint results, power map, stress test, monitor, and consultation plan where applicable.

Seek independent perspectives from constitutional/public-law counsel, subject-matter experts, affected communities, accessibility/equality specialists, and implementation/audit professionals as appropriate. Do not select reviewers solely for agreement. Record conflicts, dissent, unanswered questions, and response to review in the matter's `12-expert-escalation/` folder using `templates/independent-review-register.example.json`; validate it with `python3 scripts/validate_independent_review.py <register.json>`.

Output: review question; materials; reviewer criteria; conflict protocol; consultation safeguards; decision log; issues requiring resolution; and a clear statement that no draft proceeds as “cleared” until material Critical/High issues receive a recorded response.

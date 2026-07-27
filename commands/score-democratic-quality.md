# /score-democratic-quality

Score the supplied legal proposal using `templates/democratic-quality-scorecard.example.json` and `scorecards/README.md`. Store the result in the matter's `13-democratic-quality-scorecard/` folder. Score rights, equality, accountability, power concentration, transparency, enforceability, accessibility, and public participation from 0 to 5. For every score, provide evidence, uncertainty, and corrective action.

Run `python3 scripts/validate_democratic_scorecard.py <scorecard.json>`. Do not average away a critical failure: any 0–1 on rights, equality, accountability, or power concentration blocks a “ready” conclusion until corrected or explicitly escalated.

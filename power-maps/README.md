# Institutional Power Maps

Store a dated JSON map for each consequential institutional design, using `templates/institutional-power-map.example.json`. A map must identify all actors and material relationships, including hidden delegates such as contractors, data processors, platforms, funders, and committees.

Run `python3 scripts/analyze_power_map.py <map.json>` after updating a map. Its output flags structural concentration patterns; it cannot determine whether nominally separate actors are politically aligned, so assess real-world alignment and incentives separately.

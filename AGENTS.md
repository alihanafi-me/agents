# Project instructions

## Purpose

Maintain two Markdown rankings of user-selected AI models/agents in README.md:
- Light tasks: intelligence ** light_exponent / cost_per_task (default exponent: 2).
- Heavy tasks: intelligence ** heavy_exponent / cost_per_task / 1_000_000_000 (default exponent: 10).
- Display the heavy-task table first. Add gold, silver, and bronze medal emojis beside ranks 1, 2, and 3 in both tables.

## Data and scoring

- The user supplies model names, Intelligence, and Cost per task from Artificial Analysis. Do not invent, estimate, scrape, or substitute values unless explicitly asked.
- Store user-supplied inputs in data.json. Preserve model names and values exactly as supplied.
- Exponents live in data.json and can be positive fractional values.
- Require finite, nonnegative Intelligence and finite, positive Cost per task.
- Keep cost units and benchmark definitions comparable across models.
- Sort by unrounded score descending, then by model name for deterministic ties. Round scores only for display.
- Display scores below 1000 without decimal places. Use `k` for thousands, `m` for millions, and `b` for billions (including larger values), with up to one decimal place and no trailing decimal zero.

## Workflow

- Use Python's standard library; keep this project dependency-free.
- README.md is generated. Edit generate_readme.py for static text, and data.json for inputs.
- After changing data or generation logic, run `python3 generate_readme.py` and inspect both tables.
- Keep all program output, project text, and documentation in English.
- Preserve the MIT license.
- CLAUDE.md imports this file; keep shared instructions here.

# Phase 0 — Python Foundations

Prerequisites before touching the pipeline. Skip items you can already demonstrate.

## Core Language

- [ ] Virtual environments (`poetry` and `pyproject.toml`) — create, activate, understand why
- [x] Project structure: `src/` layout, `__init__.py`, relative vs absolute imports — created src/{models,scraper,storage,transformation,analytical} and tests/ with __init__.py in each
- [x] Type hints: basic annotations, `Optional`, `list[str]`, `dict[str, Any]` — scalar annotations (`float`, `str`) and `Optional[float]` demonstrated through iterative practice; container types explained
- [x] Dataclasses and `@dataclass` decorator — wrote a `Listing` dataclass with correct field annotations including `Optional[float]` for nullable fields
- [ ] Exception handling: `try/except/finally`, custom exceptions, when to catch vs propagate
- [x] Context managers (`with` statement) — file I/O, database connections — explained resource leak problem, guaranteed cleanup guarantee articulated correctly in own words

## Tooling

- [ ] `pip` and `requirements.txt` vs `pyproject.toml`
- [ ] Formatter: `black` — run it, understand what it does
- [ ] Linter: `ruff` — run it, fix violations, understand common rules
- [ ] Running tests with `pytest`: a single test, a file, the full suite

## Git Basics

- [x] `init`, `add`, `commit`, `status`, `diff`, `log` — used throughout setup
- [x] Branching: `branch`, `checkout`, `merge` — created feature/project-structure correctly; learned branch renaming
- [x] `.gitignore` — what to exclude and why (venv, `.env`, `__pycache__`) — created and used to stop tracking pycache files
- [~] Writing clear commit messages (imperative mood, under 72 chars) — first message described process not outcome; corrected on second attempt

## Notes

### Initial Assessment — 2026-05-23

Student completed a diagnostic assessment before starting. Findings:

- [x] Virtual environments — demonstrated solid understanding in her own words. Can proceed.
- [ ] Project structure — not yet assessed; will cover during first coding task.
- [ ] Type hints — not known. Thought they were related to JSON web formats. Priority to cover before Phase 1.
- [ ] Dataclasses — not yet assessed.
- [ ] Exception handling — not yet assessed.
- [~] Context managers (`with`) — knows what the code does (opens file, reads content) but did not address the resource-management guarantee that `with` provides (auto-close on exception). Needs clarification, not full re-teaching.

Tooling: not yet assessed — will address when setting up the project environment.

Git: knows `init`, `push`, `pull`, `commit`, `status`. Branching and `.gitignore` not yet covered.

Prior experience worth noting:
- Practical pandas experience (dataframes, joins, aggregations, cleaning) — translates directly to Polars.
- Has uploaded files to S3 with Python before; knows the bucket + IAM credentials pattern.
- AWS conceptual understanding is strong.

Idempotency misconception: student described "no duplicate primary keys" rather than "re-running produces the same result." Will correct this in context during Phase 1–2.

Starting point: late Phase 0. Will close type hints and context manager gaps, then move to Phase 1.

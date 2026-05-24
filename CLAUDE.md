# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Teaching Mode (MANDATORY)

This is a learning project for a trainee data engineer. The following rules apply to EVERY interaction without exception:

- **NEVER provide complete solutions or ready-to-run code.** Instead, explain the underlying concepts in detail, give targeted hints, and let the student write the code herself.
- **Break problems into small, concrete steps.** Present one step at a time. Wait for the student to attempt it before moving to the next.
- **Explain the "why" before the "how."** Concepts, trade-offs, and reasoning come first. Implementation details come only as guidance, not as copy-paste answers.
- **Use pseudocode or partial snippets** (max 3-5 lines) only when necessary to illustrate a specific concept. Never write full functions, classes, or modules for the student.
- **Ask guiding questions** to help the student think through the problem: "What data structure would fit here?", "What happens if this request fails?", "How would you avoid duplicating records?"
- **When the student is stuck**, give progressively more specific hints rather than jumping to the answer. Start with the concept, then point to the relevant documentation or pattern, then show a minimal example of the technique — never the full solution.
- **Review and give feedback** on the student's code. Point out what works well, what could improve, and why — this is more valuable than writing the code yourself.

## Learning Backlog (`learning-backlog/`)

This folder is the single source of truth for the student's learning path and progress. Every interaction must respect it:

- **Track progress here.** Each phase of the learning journey has its own `.md` file in `learning-backlog/` with a checklist of concepts and skills. When the student demonstrates understanding or completes a task, mark the corresponding item as done (`- [x]`).
- **Guide from here.** Before proposing a new task or concept, check the backlog to determine what the student should tackle next. Always follow the defined progression — do not skip ahead unless the student explicitly asks and demonstrates readiness.
- **Update continuously.** After each meaningful interaction (concept explained, task completed, code reviewed), update the relevant backlog file to reflect the student's current state.
- **Never mark items complete without evidence.** The student must show understanding — through code she wrote, an explanation in her own words, or a working implementation — before an item is checked off.
- **Use the backlog to personalise guidance.** If the student struggles with a topic, add sub-items or notes to the backlog to break it down further. If she advances quickly, note that too.

## Project Purpose

End-to-end data engineering pipeline that tracks price-per-square-metre for used housing in Medellín, Colombia. Designed as a hands-on learning project for an entry-level data engineer. The pipeline scrapes real estate listings, lands raw data in S3, transforms it through a medallion architecture (raw → bronze → silver → gold), and surfaces price trends per neighbourhood.

## Tech Stack

- **Language:** Python 3.11+
- **Scraping:** `requests` + `BeautifulSoup` or `Playwright`
- **Storage:** AWS S3 (MinIO for local dev)
- **Processing:** Polars, optionally PySpark
- **Warehouse:** PostgreSQL or DuckDB
- **Orchestration:** Apache Airflow
- **Transformation:** dbt (advanced phase)

## Architecture

```
[Web Sources] → [Scraper] → [S3 Raw/Landing] → [Transform] → [Analytical Layer] → [Dashboard]
```

Medallion folder structure in S3: `raw/` → `processed/` → `curated/`, partitioned by ingestion date.

## Key Engineering Concepts to Apply

### Design Patterns
- **Repository pattern** — abstract data access behind a consistent interface (e.g. `ListingRepository` that works against S3, local files, or a database)
- **Strategy pattern** — swap scraping strategies per source site without changing the pipeline
- **Factory pattern** — instantiate the right scraper/parser based on the target platform
- **Pipeline/Chain of Responsibility** — compose transformation steps as discrete, testable stages

### Architecture Principles
- **Separation of concerns** — ingestion, transformation, storage, and presentation are independent layers
- **Idempotency** — every pipeline step must be safely re-runnable without duplicating data
- **Schema evolution** — handle source format changes gracefully; never assume a fixed schema from external sources
- **Medallion architecture** — data quality improves as it moves through tiers (raw → cleaned → aggregated)

### APIs & Backend Services
- **REST API design** — if exposing price data, follow RESTful conventions: resource-based URIs, proper HTTP verbs, status codes, pagination
- **Request/response contracts** — define clear schemas (e.g. with Pydantic) for data flowing between services
- **Rate limiting & backoff** — respect source site limits; implement exponential backoff on retries
- **Health checks & observability** — every service should expose a health endpoint and structured logs

### AWS Fundamentals
- **IAM** — principle of least privilege; create dedicated IAM roles/policies per service (scraper role, transform role). Never use root credentials. Use IAM roles for EC2/Lambda, not long-lived access keys.
- **S3** — bucket policies, lifecycle rules for cost management, versioning for data recovery. Understand the difference between bucket policies and IAM policies. Use server-side encryption (SSE-S3 or SSE-KMS).
- **Credential management** — use environment variables or AWS Secrets Manager, never hardcode. For local dev, use `~/.aws/credentials` profiles.
- **Networking basics** — VPCs, security groups, and why your RDS instance should not be publicly accessible.

## Conventions

- Use British English in all documentation, comments, and user-facing text (metre, neighbourhood, colour)
- Code identifiers and technical terms remain in their original form (e.g. `color` in CSS)
- Follow PEP 8, use type hints, format with `black`, lint with `ruff`
- Commit messages in imperative mood, under 72 characters

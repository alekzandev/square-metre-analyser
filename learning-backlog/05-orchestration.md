# Phase 5 — Orchestration & Automation

## Concepts

- [ ] What orchestration means: scheduling, dependency management, monitoring
- [ ] DAGs (Directed Acyclic Graphs): why pipelines are modelled as DAGs
- [ ] Idempotent tasks: each run produces the same result regardless of retries
- [ ] Backfilling: re-running past dates when logic changes

## Scheduling Basics

- [ ] Cron syntax: understand the five fields, write common schedules
- [ ] Run the scraper on a daily schedule using cron (or a simple scheduler)
- [ ] Understand why time zones matter in scheduling

## Apache Airflow (Introduction)

- [ ] What Airflow is: scheduler, web UI, executor, metadata DB
- [ ] Install Airflow locally (standalone mode)
- [ ] Write a simple DAG with two tasks chained in sequence
- [ ] Operators: `BashOperator`, `PythonOperator` — when to use each
- [ ] Task dependencies: `>>` syntax, `set_upstream`/`set_downstream`
- [ ] Trigger a DAG manually, inspect logs, understand task states

## Error Handling

- [ ] Retries with backoff: configure `retries` and `retry_delay` on tasks
- [ ] Alerting on failure: email or Slack notifications when a task fails
- [ ] Dead-letter pattern: capture failed records for manual inspection

## Observability

- [ ] Log row counts and quality metrics at each pipeline stage
- [ ] SLA monitoring: define expected completion time, alert on misses
- [ ] Pipeline lineage: which upstream data feeds which downstream table

## Notes

<!-- Space for observations about the student's progress -->

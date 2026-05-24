# Phase 7 — Advanced Topics

Tackle these after the core pipeline is working end-to-end.

## dbt (Data Build Tool)

- [ ] What dbt is: SQL-based transformation framework, separate from ingestion
- [ ] Model layers: `sources` → `staging` → `intermediate` → `marts`
- [ ] Materialisation strategies: `view`, `table`, `incremental`
- [ ] Testing: `not_null`, `unique`, `accepted_values`, `relationships`
- [ ] Write a staging model for the listings source
- [ ] Write a mart model that computes monthly price-per-m² by neighbourhood

## File Formats & Performance

- [ ] Parquet vs CSV vs JSON: columnar vs row-based, compression, schema enforcement
- [ ] Partitioning on disk: by date, by source — and how it affects query performance
- [ ] File size tuning: why many small files are worse than fewer larger ones

## Data Contracts & Schema Evolution

- [ ] Define a contract: what fields the downstream expects, their types, constraints
- [ ] Handle a schema change: a new column appears in the source — what breaks, what doesn't
- [ ] Versioning strategies for data schemas

## Containerisation (Docker)

- [ ] What Docker is: images, containers, Dockerfiles
- [ ] Write a Dockerfile for the scraper
- [ ] `docker-compose` for local development: scraper + database + MinIO
- [ ] Environment variables in containers

## Networking & Security (AWS)

- [ ] VPC: what it is, subnets (public vs private), route tables
- [ ] Security groups: inbound/outbound rules, why default-deny matters
- [ ] Why databases belong in private subnets, not public ones
- [ ] Connecting services: VPC peering, NAT gateways (concepts only)

## Notes

<!-- Space for observations about the student's progress -->

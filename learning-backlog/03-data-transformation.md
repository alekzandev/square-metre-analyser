# Phase 3 — Data Transformation (ETL / ELT)

## Concepts

- [ ] ETL vs ELT: what each means, trade-offs, when to use which
- [ ] Data cleaning: what makes raw data "dirty" (nulls, duplicates, inconsistent formats)
- [ ] Schema design: define the target structure before writing transformation code
- [ ] Idempotency in transformations — re-running produces the same result

## Polars (Primary Tool)

- [ ] Read JSON/CSV files into a Polars DataFrame
- [ ] Select, filter, rename columns
- [ ] Handle nulls: detect, drop, fill — and decide which strategy fits each column
- [ ] Data types: cast strings to numbers, parse dates
- [ ] Derived columns: compute `price_per_m2 = price / area`
- [ ] Aggregations: group by neighbourhood, compute mean/median/count
- [ ] Deduplication: identify and remove duplicate listings
- [ ] Write output as Parquet — understand why Parquet over CSV for analytical workloads

## Pipeline Design

- [ ] Structure transformations as discrete steps (extract → clean → enrich → write)
- [ ] Chain of Responsibility pattern: each step takes input, transforms, passes to next
- [ ] Log row counts at each stage for observability
- [ ] Validate output schema before writing (column names, types, non-null constraints)

## Data Quality

- [ ] Define quality rules: no null prices, area > 0, valid neighbourhood names
- [ ] Quarantine bad records instead of dropping silently — write them to a separate file
- [ ] Compute and log quality metrics: null rate, duplicate rate, outlier count

## Notes

<!-- Space for observations about the student's progress -->

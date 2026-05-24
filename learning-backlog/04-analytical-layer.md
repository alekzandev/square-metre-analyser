# Phase 4 — Analytical Storage & SQL

## SQL Fundamentals

- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `JOIN` types: `INNER`, `LEFT`, `CROSS` — when to use each
- [ ] `GROUP BY` + aggregate functions: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`
- [ ] `HAVING` vs `WHERE` — filtering before vs after aggregation
- [ ] Subqueries and CTEs (`WITH` clause) — write readable multi-step queries
- [ ] Window functions: `ROW_NUMBER`, `LAG`, `LEAD`, `AVG() OVER()` — essential for time-series

## Database Design

- [ ] Tables, columns, data types, primary keys
- [ ] Normalisation basics: 1NF, 2NF, 3NF — what they mean, when to denormalise
- [ ] Indexes: what they are, when they help, when they hurt
- [ ] Design the schema for this project: listings table, neighbourhood dimension, time dimension

## DuckDB or PostgreSQL

- [ ] Install and connect to the chosen database
- [ ] Create tables from Parquet files (or load via `COPY`/`INSERT`)
- [ ] Run analytical queries: price trends by neighbourhood over time
- [ ] Understand the difference between OLTP (PostgreSQL) and OLAP (DuckDB) workloads

## Time-Series Analysis (SQL)

- [ ] Compute price-per-m² moving averages per neighbourhood
- [ ] Use `LAG()` to calculate month-over-month price changes
- [ ] Identify neighbourhoods with the highest/lowest price growth

## Notes

<!-- Space for observations about the student's progress -->

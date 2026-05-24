# 🏠 Medellín Housing Price Tracker — Data Engineering Trainee Project

## Overview

A end-to-end data engineering pipeline that tracks and analyzes price-per-square-meter fluctuations for used housing in Medellín, Colombia. The project is designed as a **hands-on learning path** for entry-level data engineers, covering the full lifecycle of a real-world data system: from raw data acquisition to analytical consumption.

The business problem is concrete and relatable — a buyer facing pricing uncertainty in a specific neighborhood — which keeps the engineering work grounded throughout the learning journey.

---

## Problem Statement

When purchasing used residential property in Medellín, buyers lack reliable, up-to-date visibility into how price per square meter (COP/m²) behaves over time in a given area. This information asymmetry creates poor decision-making conditions. The system aims to remove that uncertainty by continuously capturing, storing, and surfacing price data.

---

## System Architecture

```
[Web Sources]
     │
     ▼
[Scraper / Extractor]   ← Automation layer
     │
     ▼
[Raw Storage — S3]      ← Landing zone (Data Lake)
     │
     ▼
[Transformation Layer]  ← ETL / ELT pipeline
     │
     ▼
[Analytical Layer]      ← Queryable, structured data
     │
     ▼
[Reporting / Dashboard] ← Price trends by zone & time
```

---

## Core Components

### 1. Data Ingestion — Web Scraping
- Identify and scrape real estate listing platforms (e.g. Finca Raíz, Metrocuadrado)
- Extract structured fields: price, area (m²), neighborhood, listing date
- Schedule automated runs to capture price changes over time
- Handle pagination, rate limiting, and anti-scraping measures

### 2. Raw Storage — Data Lake (S3)
- Land raw scraped data in its original form (JSON/CSV) with no transformation
- Partition by ingestion date for traceability and reprocessing capability
- Apply a medallion-style folder structure: `raw/` → `processed/` → `curated/`

### 3. Transformation — ETL / ELT Pipeline
- Clean and normalize raw records (deduplicate listings, standardize units)
- Compute derived metrics: price per m², price delta over time, zone averages
- Choose between ETL (transform before load) vs ELT (load then transform in-warehouse) as a deliberate architectural decision

### 4. Analytical Storage
- Load curated data into a queryable layer (e.g. PostgreSQL, DuckDB, or a cloud warehouse)
- Model data for time-series analysis per neighborhood

### 5. Orchestration & Automation
- Schedule and monitor pipeline runs
- Handle failure, retries, and data quality checks

---

## Learning Objectives

This project is structured so the trainee progressively builds and owns each layer:

| Phase | Concept | Skills Practiced |
|---|---|---|
| 1 | Source identification | Research, API vs HTML scraping |
| 2 | Web scraping | Python, `requests`, `BeautifulSoup` / `Playwright` |
| 3 | Raw storage | AWS S3, cloud storage concepts, partitioning |
| 4 | Data Lake design | Medallion architecture, file formats (JSON, Parquet) |
| 5 | Transformation | Pandas / dbt, data cleaning, schema design |
| 6 | ETL vs ELT | Architectural trade-offs |
| 7 | Orchestration | Cron, Airflow, or Prefect basics |
| 8 | Data quality | Null handling, deduplication, validation |
| 9 | Analytical layer | SQL, warehouse loading, query optimization |
| 10 | Visualization | Basic dashboarding of price trends |

---

## Tech Stack (Suggested)

- **Language:** Python 3.11+
- **Scraping:** `requests` + `BeautifulSoup` or `Playwright`
- **Storage:** AWS S3 (or MinIO locally)
- **Processing:** Polars, then optionally PySpark
- **Warehouse:** PostgreSQL or DuckDB
- **Orchestration:** Apache Airflow
- **Transformation:** dbt (advanced phase)
- **Version Control:** Git + GitHub

---

## Key Data Engineering Concepts Covered

- **Data Lake** — centralized raw storage with no upfront schema enforcement
- **Medallion Architecture** — raw → bronze → silver → gold data quality tiers
- **Idempotency** — pipelines that can be safely re-run without duplicating data
- **Partitioning** — organizing data by date/zone for efficient querying
- **Schema evolution** — handling source format changes over time
- **Observability** — logging, alerting, and pipeline monitoring basics

---

## Project Outcome

By the end of the project, the trainee will have built and operated a fully functional, automated data pipeline that answers a real question: *"Is now a good time to buy in this neighborhood, and how has the price per m² changed over the last N months?"*
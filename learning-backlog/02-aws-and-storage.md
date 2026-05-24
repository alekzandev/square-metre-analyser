# Phase 2 — AWS Fundamentals & Raw Storage (S3)

## AWS Core Concepts

- [ ] What is cloud computing — on-demand resources, pay-as-you-go model
- [ ] AWS regions and availability zones — what they are, how to choose
- [ ] The AWS Management Console: navigate to S3, IAM

## IAM (Identity & Access Management)

- [ ] Users, groups, roles, and policies — what each one is
- [ ] Principle of least privilege — why and how to apply it
- [ ] Create an IAM user with programmatic access (access key + secret key)
- [ ] Write a minimal IAM policy that grants only S3 read/write to a specific bucket
- [ ] Understand why root account should never be used for daily work
- [ ] `~/.aws/credentials` and `~/.aws/config` — configure a named profile

## S3 (Simple Storage Service)

- [ ] Buckets, objects, keys (paths) — the mental model
- [ ] Create a bucket via the console
- [ ] Upload/download objects using `boto3` (the AWS SDK for Python)
- [ ] Understand S3 pricing: storage, requests, data transfer
- [ ] Bucket policies vs IAM policies — when to use which
- [ ] Versioning: enable it, understand why it helps with data recovery
- [ ] Lifecycle rules: auto-transition or delete old data to control costs

## Data Lake — Landing Zone

- [ ] Design the folder structure: `raw/{source}/{date}/` partitioned by ingestion date
- [ ] Upload scraper output (JSON) to S3 using `boto3`
- [ ] Understand the medallion architecture: `raw/` → `processed/` → `curated/`
- [ ] Why raw data should be stored as-is, never modified in place

## Credential Management

- [ ] Environment variables for secrets — never hardcode keys in source code
- [ ] `.env` files with `python-dotenv` for local development
- [ ] Add `.env` to `.gitignore` — understand why this is non-negotiable

## Notes

<!-- Space for observations about the student's progress -->

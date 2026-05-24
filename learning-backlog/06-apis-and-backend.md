# Phase 6 — APIs & Backend Services

## HTTP & REST Concepts

- [ ] Client-server model: request/response cycle
- [ ] REST principles: stateless, resource-based URIs, standard HTTP verbs
- [ ] Status codes: 2xx (success), 4xx (client error), 5xx (server error) — know the common ones
- [ ] JSON as the standard data interchange format

## Building a Simple API

- [ ] Choose a framework: FastAPI (recommended) or Flask
- [ ] Create an endpoint that returns price data for a neighbourhood
- [ ] Path parameters vs query parameters — when to use each
- [ ] Request validation with Pydantic models (FastAPI)
- [ ] Response schemas: define what the API returns, enforce it

## API Design Best Practices

- [ ] Pagination: `offset`/`limit` or cursor-based — why unbounded results are dangerous
- [ ] Filtering and sorting via query parameters
- [ ] Error responses: consistent format with error code and message
- [ ] Versioning: `/api/v1/` prefix — why and when to bump

## Connecting API to the Analytical Layer

- [ ] Read from DuckDB/PostgreSQL in the API layer
- [ ] Repository pattern: abstract database access behind an interface
- [ ] Connection pooling: why it matters, how to configure it

## Health & Observability

- [ ] `/health` endpoint: returns service status
- [ ] Structured logging: JSON logs with timestamp, level, context
- [ ] Request logging: method, path, status code, latency

## Notes

<!-- Space for observations about the student's progress -->

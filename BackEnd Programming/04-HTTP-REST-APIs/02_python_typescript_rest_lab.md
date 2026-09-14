# REST API Implementation Lab — Python + TypeScript + Production

## Goal

Implement the same resource API twice and then harden it for production.

Resource: `projects`

```text
GET    /v1/projects
POST   /v1/projects
GET    /v1/projects/{project_id}
PATCH  /v1/projects/{project_id}
DELETE /v1/projects/{project_id}
```

## Python / FastAPI

Use Pydantic models for request/response validation, dependency injection for authentication and repositories, and SQLAlchemy for persistence.

Required implementation:

- typed request and response models;
- pagination with a stable cursor;
- validation errors with a consistent envelope;
- repository/service separation;
- PostgreSQL transaction boundaries;
- authentication and object-level authorization;
- idempotency for create operations where duplicate submission is possible;
- pytest + HTTPX tests.

## TypeScript / Express

Implement the same contract with Express and TypeScript.

Required implementation:

- Zod or equivalent runtime validation;
- typed service and repository interfaces;
- PostgreSQL client/ORM;
- centralized error middleware;
- authentication middleware;
- object-level authorization;
- Supertest/Vitest tests;
- graceful shutdown.

Do not rely on TypeScript types alone for untrusted HTTP input: runtime validation is required.

## Contract

Success:

```json
{
  "data": {
    "id": "project_123",
    "name": "support-assistant",
    "status": "active"
  }
}
```

Validation error:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "request_id": "..."
  }
}
```

Use `201` for creation, `200` for reads/updates, `204` for successful deletion, `401` for missing/invalid authentication, `403` for unauthorized access, `404` for missing resources, `409` for conflicts, `422` for validation where your API convention uses it, and `429` for rate limiting.

## Production hardening

Put the API behind a load balancer/reverse proxy and TLS termination. Configure trusted proxies deliberately. Add request IDs, JSON logs, metrics, OpenAPI, dependency timeouts, database pool limits, rate limits, body-size limits, CORS policy, security headers, secret management, health/readiness endpoints, migrations, CI, Docker, and graceful shutdown.

## Failure exercises

1. Send invalid JSON.
2. Send an oversized body.
3. Request another tenant's project.
4. Repeat a create request with the same idempotency key.
5. Kill PostgreSQL during a write.
6. Exhaust the DB pool.
7. Send a stale update against a concurrently changed project.
8. Send an expired access token.
9. Trigger rate limiting.
10. Terminate the process while requests are in flight.

For every failure, document HTTP response, structured log fields, metric changes, retry behavior, and whether the client should retry.

## Production definition of done

- Python and TypeScript implementations behave identically at the API boundary.
- OpenAPI is reviewed as a contract.
- Unit, integration, API, security, and failure tests pass.
- PostgreSQL is used instead of an in-memory store.
- Secrets are externalized.
- Docker Compose starts the complete local stack.
- CI runs formatting, linting, type checking, tests, and migration checks.
- A short runbook explains deployment, rollback, health checks, and common incidents.

# API Design — Contract-First Implementation Lab

## Python

Define FastAPI/Pydantic schemas first and generate OpenAPI. Validate requests at the boundary. Write pytest contract tests for status codes, response shape, pagination, errors, authentication, and idempotency.

## TypeScript

Define the same OpenAPI contract and validate runtime inputs with Zod or a generated validator. Generate a typed client and use it from a test consumer. Verify that TypeScript compile-time types and runtime validation agree.

## Production workflow

```text
Design -> OpenAPI review -> implementation -> contract tests -> client generation -> compatibility check -> deploy
```

Use `/v1` versioning when breaking compatibility is unavoidable. Prefer additive changes. Define deprecation policy. Set explicit pagination, filtering, sorting, timeout, rate-limit, idempotency, and error semantics.

## AI API extension

Design:

```text
POST /v1/chat
POST /v1/chat/stream
GET  /v1/requests/{request_id}
```

Document model selection, message schema, token budgets, provider metadata, usage, errors, streaming event format, authentication, and rate limits. Add a contract test that simulates provider timeout, 429, malformed provider output, and client disconnect.

## Deliverable

Commit the OpenAPI document, Python server, TypeScript client, contract tests, compatibility report, and production API change/deprecation note.

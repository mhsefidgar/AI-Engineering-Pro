# API Contract Lab

Design an API before implementing it.

## Resource
Build `/v1/projects` with:

- `POST /v1/projects`
- `GET /v1/projects?limit=20&cursor=...`
- `GET /v1/projects/{id}`
- `PATCH /v1/projects/{id}`
- `DELETE /v1/projects/{id}`

## Contract requirements

Define request/response schemas, status codes, error codes, pagination semantics, authentication requirements, idempotency behavior, and rate limits.

## Hands-on

1. Write an OpenAPI document for the endpoints.
2. Generate a client from the contract.
3. Implement validation at the API boundary.
4. Add `Idempotency-Key` to project creation.
5. Add cursor pagination rather than offset pagination.
6. Return a stable error envelope.
7. Add contract tests that fail if the implementation diverges from OpenAPI.

## AI extension
Add `POST /v1/inference` with model, messages, temperature, max output tokens, request ID, usage, latency, and provider metadata. Design the contract so provider-specific fields do not leak into the public API.
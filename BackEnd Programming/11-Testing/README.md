# Backend Testing

A production backend should be tested at multiple boundaries.

## Levels

- Unit tests: pure business logic
- Integration tests: service + database/external dependencies
- API tests: HTTP contract and validation
- End-to-end tests: complete user workflows

## Test strategy

Test happy paths, validation failures, authorization boundaries, retries, timeouts, provider failures, database constraints, and idempotency.

For FastAPI use pytest and an HTTP test client. For Node/TypeScript use a test runner plus an HTTP integration layer. Prefer realistic integration tests for critical database behavior instead of mocking everything.

## AI-specific tests

Keep deterministic evaluation fixtures for prompts/model adapters. Test schema-constrained outputs, timeout handling, token/cost accounting, provider fallback, streaming termination, and tool-call authorization.
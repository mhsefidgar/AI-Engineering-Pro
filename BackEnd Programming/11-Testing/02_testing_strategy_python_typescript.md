# Backend Testing — Python + TypeScript + Production

## Python

Use pytest, FastAPI TestClient/HTTPX, fixtures, parametrization, mocks/fakes, and PostgreSQL-backed integration tests.

Required layers:

```text
unit -> service/repository integration -> API/contract -> security -> end-to-end
```

Test both success and failure. Assert status code, error code, response schema, side effects, transaction behavior, and observability fields where relevant.

## TypeScript

Use Vitest/Jest with Supertest for HTTP APIs. Use test containers or disposable PostgreSQL/Redis instances for integration tests when practical. Avoid tests that only prove mocks were called; test externally visible behavior.

## Production CI

CI should run formatting, linting, type checking, unit tests, integration tests, migration validation, API contract checks, and security/static checks. Keep deterministic tests fast and isolate external AI provider tests behind adapters or recorded fixtures.

## AI-specific tests

Test provider timeout, 429, malformed output, empty response, token-budget enforcement, fallback, streaming disconnect, tool-call validation, prompt injection defenses, and tenant isolation. Maintain a small evaluation dataset for semantic behavior that unit tests cannot establish.

## Failure requirement

For every dependency, write at least one test proving the service degrades predictably when that dependency is unavailable.

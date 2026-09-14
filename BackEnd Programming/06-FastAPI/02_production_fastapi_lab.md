# FastAPI — Production Implementation Lab

## Build

Create a production-style FastAPI service with this layout:

```text
app/
  main.py
  config.py
  api/routes/
  domain/
  services/
  repositories/
  db/
  middleware/
  dependencies.py
  tests/
```

## Python implementation

Implement:

- Pydantic request/response models;
- dependency injection for DB sessions and authenticated users;
- async endpoints where I/O benefits from concurrency;
- SQLAlchemy + PostgreSQL persistence;
- service layer for business rules;
- repository layer for persistence;
- exception handlers and stable error schemas;
- background tasks only for work that is safe to lose; use a durable queue for important jobs;
- streaming responses for AI output;
- pytest + HTTPX integration tests.

Example boundary:

```python
@router.post("/v1/projects", response_model=ProjectResponse, status_code=201)
async def create_project(
    payload: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
    user: User = Depends(require_user),
):
    return await service.create(user.id, payload)
```

## Production behavior

Configure workers, proxy headers, timeouts, connection pools, request limits, CORS, trusted hosts, OpenAPI, structured logs, request IDs, metrics, health/readiness, graceful shutdown, migrations, and secret management. Never treat `--reload` as a production deployment mode.

## AI-engineering extension

Add `/v1/chat` and `/v1/chat/stream` without putting provider SDK calls directly inside route handlers. Define an `LLMProvider` interface, provider adapters, request budgets, usage accounting, timeout/retry policy, and redacted logs. Persist request metadata without storing sensitive prompts by default.

## Failure lab

Test invalid payloads, DB outage, provider timeout, provider 429, client disconnect during streaming, exhausted budget, expired token, unauthorized object access, and graceful shutdown during a long request.

# FastAPI

FastAPI is a Python framework for building typed, asynchronous HTTP APIs with automatic OpenAPI documentation.

## Core topics

- Application and router structure
- Path, query, and header parameters
- Pydantic request/response models
- Validation and serialization
- Dependency injection
- Middleware and exception handlers
- Authentication and authorization
- Async endpoints and I/O
- Background work
- PostgreSQL with SQLAlchemy
- Redis caching
- OpenAPI documentation
- pytest API testing
- Docker and production deployment

## Recommended structure

```text
app/
  main.py
  api/
    routes/
  schemas/
  services/
  repositories/
  models/
  core/
  tests/
```

Keep HTTP concerns in routes and business logic in services. Database access should be isolated behind repositories or a clear data-access boundary.

## Minimal example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Backend")

class InferenceRequest(BaseModel):
    prompt: str

@app.post("/inference")
async def inference(request: InferenceRequest):
    return {"output": f"received: {request.prompt}"}
```

## Production checklist

Use environment-based configuration, dependency injection for external clients, request validation, structured logging, health endpoints, timeouts, tests, and explicit authentication/authorization.
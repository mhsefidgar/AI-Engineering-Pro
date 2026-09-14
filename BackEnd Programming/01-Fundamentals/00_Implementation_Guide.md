# HTTP Fundamentals — Implementation Guide

This section is not complete until the learner can implement, test, debug, and operate the same HTTP concepts in both Python and JavaScript/TypeScript.

## 1. Python implementation

Build a small FastAPI service:

```bash
python -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn httpx pytest
uvicorn app:app --reload
```

```python
from fastapi import FastAPI, Request
from uuid import uuid4

app = FastAPI()

@app.middleware("http")
async def request_context(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid4()))
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    return response

@app.get("/health")
async def health():
    return {"status": "ok"}
```

Then test it with `curl`, `httpx`, and pytest. Add malformed JSON, missing headers, slow handlers, and 404/422/500 cases.

## 2. JavaScript/TypeScript implementation

Build the equivalent service with Node's HTTP module first, then Express:

```bash
npm init -y
npm i express
npm i -D typescript tsx vitest supertest @types/express
```

Implement `/health`, request IDs, JSON parsing, centralized errors, and graceful shutdown. Test with Supertest/Vitest.

## 3. Production implementation

A production HTTP service must demonstrate:

- TLS termination and trusted proxy configuration;
- request size limits and parser limits;
- explicit connect/read/write timeouts;
- request/correlation IDs;
- structured JSON logs with secret redaction;
- consistent error envelopes;
- authentication and authorization boundaries;
- rate limiting and abuse controls;
- health vs readiness endpoints;
- graceful SIGTERM shutdown;
- metrics for request count, latency, status code, and saturation;
- OpenAPI documentation and backward-compatible API changes.

## 4. Failure lab

Run the service while deliberately causing malformed JSON, oversized bodies, dependency timeouts, repeated 5xx responses, client disconnects, and shutdown during an active request. Record expected status codes, logs, metrics, and recovery behavior.

## 5. Deliverable

Submit a Python implementation, a TypeScript implementation, automated tests, curl commands, a failure matrix, and a production checklist. A topic is considered learned only when the implementation survives the failure lab.

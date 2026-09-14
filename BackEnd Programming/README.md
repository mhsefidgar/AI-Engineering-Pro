# Backend Programming for AI Engineers

A practical, implementation-first backend engineering path for AI Engineering Pro. Every section should move from concept -> runnable example -> tests -> failure modes -> production hardening.

## Learning path

1. HTTP and REST APIs
2. TypeScript and Node.js
3. Express
4. HTTP/REST API design
5. FastAPI
6. FastMCP / MCP
7. PostgreSQL and Redis
8. Authentication and authorization
9. Testing
10. Security
11. Production/observability
12. Architecture and distributed systems
13. Advanced backend systems
14. AI backends: LLM APIs, streaming, RAG, jobs, caching, cost tracking
15. Capstone projects

## Hands-on standard

For each topic, do all of the following where applicable:

- implement a minimal working example;
- run it locally;
- test happy and unhappy paths;
- inspect the HTTP/database/runtime behavior;
- add validation, timeouts, retries, and idempotency where relevant;
- add authentication/authorization where relevant;
- add structured logs and metrics;
- document failure modes and recovery;
- turn the exercise into a reusable project component.

## Practical labs already included

- `01-Fundamentals/01_HTTP_Curl_Lab.md`
- `02-TypeScript/01_backend_types_lab.ts`
- `03-NodeJS/01_node_http_server.mjs`
- `05-Express/README.md`
- `07-FastMCP/01_fastmcp_server.py`
- `08-Databases/01_postgres_schema.sql`
- `09-API-Design/01_API_Contract_Lab.md`
- `10-Authentication/01_auth_lab.md`
- `11-Testing/01_pytest_api_lab.py`
- `12-Security/01_security_lab.md`
- `13-Production/01_observability_lab.md`
- `14-Architecture/01_service_architecture_lab.md`
- `15-Advanced_Backend/01_queues_cache_websockets_lab.md`
- `16-AI_Backend/01_llm_gateway.py`
- `16-AI_Backend/02_rag_backend_lab.md`

## Notebook curriculum

Notebooks are intended to be labs, not slides. Each should contain executable setup/code, assertions or tests, exercises, failure drills, and a production extension.

Current labs:

1. FastAPI from scratch
2. FastAPI + FastMCP
3. AI API backend
4. PostgreSQL CRUD and transactions
5. JWT authentication and API testing
6. Redis caching and rate limiting
7. Background jobs, retries, and idempotency
8. End-to-end RAG API
9. FastMCP tools/resources/prompts
10. AI streaming, budgets, and cost observability
11. End-to-end AI backend capstone

## Projects

`Projects/` contains progressively harder implementation specifications, from a production FastAPI API to an end-to-end AI backend combining FastAPI, PostgreSQL, Redis, queues, RAG, LLM providers, and FastMCP.

## Architecture target

```text
Client
  -> API gateway / HTTP
  -> FastAPI or Express
  -> validation + authentication/authorization
  -> application/service layer
  -> PostgreSQL
  -> Redis/cache
  -> queue/workers
  -> AI provider / retrieval system
  -> optional FastMCP tools
  -> logs + metrics + traces
```

Secrets must come from environment variables or a secret manager. Do not commit API keys or production credentials.
# Backend Programming for AI Engineers

This curriculum is **implementation-first**. A topic is not complete because its definition is understood. Every topic must answer three questions:

1. **How do I implement it in Python?**
2. **How do I implement the equivalent backend in JavaScript/TypeScript?**
3. **How does this change for a real production system?**

The learning loop is:

```text
Concept -> Python implementation -> TypeScript implementation
       -> automated tests -> failure injection -> security
       -> observability -> Docker/CI -> production design
```

## Learning path

1. HTTP and backend fundamentals
2. TypeScript for backend engineering
3. Node.js runtime and HTTP
4. REST API implementation and API contracts
5. Express
6. FastAPI
7. FastMCP / MCP
8. PostgreSQL, Redis, and persistence
9. API design and OpenAPI
10. Authentication and authorization
11. Testing
12. Security
13. Production engineering and observability
14. Architecture and distributed systems
15. Advanced backend systems: queues, cache, WebSockets/SSE
16. AI backends: LLM gateways, streaming, RAG, tools, cost and reliability
17. Production projects and capstone

## Required implementation coverage

Every substantial section should include, where applicable:

- Python implementation with realistic dependencies;
- JavaScript/TypeScript implementation with runtime validation;
- runnable commands and environment setup;
- API examples using curl/HTTP clients;
- unit, integration, and API/contract tests;
- PostgreSQL/Redis/queue integration when the topic needs infrastructure;
- failure injection and recovery behavior;
- authentication and authorization;
- security controls and threat modeling;
- structured logs, metrics, traces, health/readiness;
- timeouts, retries, idempotency, rate limits, and backpressure;
- Docker Compose and CI/CD expectations;
- production architecture and operational runbook;
- AI-specific evaluation/cost/latency considerations where relevant.

## Implementation labs added

- `01-Fundamentals/00_Implementation_Guide.md`
- `01-Fundamentals/01_HTTP_Curl_Lab.md`
- `02-TypeScript/01_backend_types_lab.ts`
- `03-NodeJS/01_node_http_server.mjs`
- `04-HTTP-REST-APIs/02_python_typescript_rest_lab.md`
- `05-Express/README.md`
- `06-FastAPI/02_production_fastapi_lab.md`
- `07-FastMCP/02_fastmcp_production_lab.md`
- `08-Databases/02_database_implementation_lab.md`
- `09-API-Design/02_openapi_codegen_lab.md`
- `10-Authentication/02_auth_implementation_lab.md`
- `11-Testing/02_testing_strategy_python_typescript.md`
- `12-Security/02_backend_security_implementation_lab.md`
- `13-Production/02_production_python_typescript.md`
- `14-Architecture/02_architecture_python_typescript.md`
- `15-Advanced_Backend/02_distributed_systems_python_typescript.md`
- `16-AI_Backend/03_ai_backend_production_implementation.md`

## Notebook standard

Notebooks are hands-on labs, not topic summaries. Each notebook should contain:

- installation/setup cells;
- Python implementation cells;
- HTTP/API examples;
- executable assertions/tests;
- realistic database/cache/queue examples where relevant;
- deliberate failure cases;
- exercises that require completing missing production behavior;
- a production extension section;
- a final definition-of-done checklist.

Current labs cover FastAPI, FastMCP, AI APIs, PostgreSQL, JWT, Redis, jobs/retries, RAG, MCP, streaming/cost, and the end-to-end capstone.

## Target architecture

```text
Client / Agent
   -> API gateway / HTTP / MCP
   -> FastAPI or Express adapter
   -> validation + authentication + authorization
   -> application/service layer
   -> PostgreSQL
   -> Redis/cache
   -> durable queue/workers
   -> AI provider / vector retrieval
   -> FastMCP tools/resources where appropriate
   -> logs + metrics + traces
```

The architecture deliberately teaches both Python and TypeScript so the learner understands backend engineering concepts rather than memorizing one framework.

Secrets must come from environment variables or a secret manager. Never commit API keys or production credentials.

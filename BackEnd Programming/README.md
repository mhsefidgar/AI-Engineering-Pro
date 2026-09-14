# Backend Programming for AI Engineers

A practical backend engineering path for AI Engineering Pro. The goal is to understand how production APIs, services, data stores, authentication, testing, observability, and AI/MCP systems fit together.

## Learning path

1. HTTP and REST APIs
2. TypeScript and Node.js
3. Express and FastAPI
4. PostgreSQL and Redis
5. API design, validation, authentication, and testing
6. Security and production operations
7. AI backends: LLM APIs, streaming, RAG, jobs, caching, cost tracking
8. MCP and FastMCP: tools, resources, prompts, transports, and production integration

## Stack

**TypeScript · Node.js · Express · Python · FastAPI · PostgreSQL · Redis · REST/OpenAPI · pytest · Docker · FastMCP · LLM APIs**

## Directory map

- `01-Fundamentals/` — HTTP, REST, backend architecture
- `02-TypeScript/` — TypeScript concepts used in services
- `03-NodeJS/` — runtime, event loop, async I/O
- `04-HTTP-REST-APIs/` — API semantics and design
- `05-Express/` — Node/Express service structure
- `06-FastAPI/` — Python API development with Pydantic and dependencies
- `07-FastMCP/` — Model Context Protocol servers and integrations
- `08-Databases/` — PostgreSQL, SQL, Redis, transactions, indexing
- `09-API-Design/` — validation, pagination, versioning, OpenAPI
- `10-Authentication/` — sessions, JWT, OAuth2, RBAC
- `11-Testing/` — unit, integration, and API tests
- `12-Security/` — OWASP-oriented backend security
- `13-Production/` — logging, health checks, configuration, observability
- `14-Architecture/` — layering, clean architecture, DI, distributed systems
- `15-Advanced_Backend/` — queues, caching, WebSockets, event-driven systems
- `16-AI_Backend/` — production patterns for AI services
- `Notebooks/` — executable end-to-end learning labs
- `Projects/` — capstone implementation ideas

## End-to-end mental model

```text
Client
  -> HTTP/API gateway
  -> FastAPI or Express
  -> validation/authentication
  -> service layer
  -> PostgreSQL / Redis / queue
  -> AI provider or internal model
  -> optional MCP/FastMCP tools
  -> logging, metrics, tracing
```

## Notebook policy

Each notebook should explain the concept first, then build a small working system, test it, and finish with production considerations. Secrets must come from environment variables; never commit API keys.

## Existing material

`TypeScript/Inference_Types.md` is retained as the original TypeScript reference and is now part of the broader backend curriculum.
# Backend Projects

Build these in order. These are implementation projects, not reading assignments. Every project should have runnable source code, tests, configuration, failure drills, and production-readiness evidence.

1. **FastAPI REST API** — CRUD, PostgreSQL, validation, OpenAPI
2. **Production Auth Service** — password hashing, JWT/session auth, RBAC
3. **Async Task Service** — background jobs, queue, retries, idempotency
4. **AI Inference API** — provider adapter, streaming, cost tracking, rate limits
5. **RAG API** — ingestion, embeddings, retrieval, citations, evaluation
6. **FastMCP Server** — tools, resources, prompts, validation, authorization
7. **FastAPI + FastMCP Service** — shared service layer behind both interfaces
8. **End-to-End AI Backend** — auth, PostgreSQL, Redis, queue, RAG, LLM, MCP, tests, Docker, observability

## Definition of done

- Clear README and API/OpenAPI contract
- Runnable local setup with example environment configuration
- Type/schema validation
- Unit, integration, API, and failure-path tests where applicable
- Secure secret handling
- Structured logging and request correlation
- Health/readiness checks
- Error, timeout, retry, and idempotency strategy
- Docker support where appropriate
- Architecture and data-flow diagram
- Security/threat model
- Metrics and operational runbook
- Load/performance test for service-heavy projects
- AI evaluation and cost evidence for AI projects

## Existing project specifications

- `01_FastAPI_Production_API/`
- `02_AI_Inference_Service/`
- `03_FastAPI_FastMCP_Platform/`
- `04_RAG_Knowledge_API/`
- `05_Distributed_Job_Service/`
- `06_End_to_End_AI_Backend/`
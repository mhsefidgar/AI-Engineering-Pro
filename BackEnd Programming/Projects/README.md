# Backend Projects

Build these in order. Each project should include tests, documentation, configuration via environment variables, and a production-readiness checklist.

1. **FastAPI REST API** — CRUD, PostgreSQL, validation, OpenAPI
2. **Production Auth Service** — password hashing, JWT/session auth, RBAC
3. **Async Task Service** — background jobs, queue, retries, idempotency
4. **AI Inference API** — provider adapter, streaming, cost tracking, rate limits
5. **RAG API** — ingestion, embeddings, retrieval, citations, evaluation
6. **FastMCP Server** — tools, resources, prompts, validation, authorization
7. **FastAPI + FastMCP Service** — shared service layer behind both interfaces
8. **End-to-End AI Backend** — auth, PostgreSQL, Redis, queue, RAG, LLM, MCP, tests, Docker, observability

## Definition of done

- Clear README and API contract
- Type/schema validation
- Unit and integration tests
- Secure secret handling
- Structured logging
- Health/readiness checks
- Error and timeout strategy
- Docker support where appropriate
- Example environment configuration
- Architecture diagram
# Project 06 — End-to-End AI Backend

Capstone: combine the curriculum into a deployable backend.

## Stack

FastAPI + PostgreSQL + Redis + background queue + vector store + LLM provider + FastMCP + pytest + Docker.

## Capabilities

1. User authentication and tenant isolation.
2. Document ingestion and asynchronous indexing.
3. RAG question answering with citations.
4. Streaming AI responses.
5. Provider fallback and budgets.
6. Rate limiting and caching.
7. MCP tools for authorized business actions.
8. Structured logs, metrics, traces, health/readiness.
9. Complete API/OpenAPI contract.
10. CI and reproducible local setup.

## Required engineering evidence

- architecture diagram;
- threat model;
- database schema + migrations;
- API contract;
- test pyramid;
- failure-mode matrix;
- SLOs and runbook;
- cost model;
- AI evaluation set;
- load-test results;
- deployment instructions.

## Graduation criteria

The system must remain correct under duplicate requests, dependency timeouts, worker restarts, cache loss, stale retrieval data, provider throttling, unauthorized resource access, and partial streaming failures.
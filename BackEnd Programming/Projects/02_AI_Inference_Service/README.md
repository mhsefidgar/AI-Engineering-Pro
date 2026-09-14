# Project 02 — Production AI Inference Service

Build a provider-neutral AI API suitable for a real application.

## Required endpoints

- `POST /v1/chat`
- `POST /v1/chat/stream`
- `GET /v1/requests/{request_id}`
- `GET /health`
- `GET /ready`

## Requirements

- FastAPI service layer;
- provider adapter interface;
- request validation and output limits;
- authentication and per-user authorization;
- request IDs;
- timeout/retry/fallback policy;
- token/cost accounting;
- Redis rate limits and caching where safe;
- streaming;
- structured logs and metrics;
- tests with mocked providers;
- secrets only through environment/secret management.

## Failure drills

Simulate provider timeout, 429, 5xx, malformed output, slow streaming, quota exhaustion, Redis outage, and client disconnect.

## Stretch goals

Add model routing, prompt versioning, evaluation datasets, asynchronous batch inference, and a FastMCP tool that invokes the same application service.
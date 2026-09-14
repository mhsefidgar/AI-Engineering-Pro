# Production Backend — Python + TypeScript

## Python stack

Practice a realistic deployment stack:

```text
FastAPI -> Uvicorn workers -> reverse proxy/load balancer
        -> PostgreSQL
        -> Redis
        -> durable queue/worker
        -> AI provider
```

Implement structured logging, metrics, traces, health/readiness, graceful shutdown, DB pools, dependency timeouts, bounded retries with jitter, circuit-breaking/degradation where justified, and configuration from environment/secret management.

## TypeScript stack

Practice:

```text
Express -> Node.js process -> reverse proxy/load balancer
       -> PostgreSQL
       -> Redis
       -> worker/queue
       -> AI provider
```

Use async error handling, graceful shutdown, connection-pool limits, runtime validation, structured logs, metrics, tracing, and dependency timeout policies.

## Docker

Each implementation must have a multi-stage Dockerfile, non-root runtime user, health check, pinned/controlled dependencies, and no secrets baked into the image.

## CI/CD

Pipeline:

```text
format -> lint -> type check -> unit tests -> integration tests
       -> security checks -> build image -> migration check -> deploy
```

Use immutable image tags, environment-specific configuration, migration safety checks, rollback strategy, and deployment health gates.

## Failure drills

Simulate DB unavailable, Redis unavailable, AI provider timeout/429, queue backlog, worker crash, memory pressure, repeated 5xx, and process termination. Capture logs, metrics, traces, user-visible behavior, and recovery actions.

## SLO exercise

Define availability, latency, error-rate, and AI-specific quality/cost objectives. Build a runbook that maps symptoms to likely causes and first diagnostic commands.

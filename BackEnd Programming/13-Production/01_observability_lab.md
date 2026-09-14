# Production Observability Lab

Instrument a service as if another team will operate it at 2 a.m.

## Implement

- structured JSON logs;
- request ID/correlation ID;
- request count and latency metrics;
- error-rate metric;
- readiness and liveness endpoints;
- graceful shutdown;
- outbound dependency timeouts;
- retry policy with exponential backoff and jitter;
- database pool limits;
- trace spans around database, cache, queue, and model-provider calls.

## Failure drills

1. Make PostgreSQL unavailable.
2. Make Redis unavailable.
3. Make the AI provider slow.
4. Return repeated 5xx responses from a dependency.
5. Fill the worker queue.

For each drill, capture logs/metrics, identify the failure boundary, and define the alert you would create.

## Production deliverable
Write a one-page runbook containing symptoms, dashboards, likely causes, rollback/mitigation steps, and escalation criteria.
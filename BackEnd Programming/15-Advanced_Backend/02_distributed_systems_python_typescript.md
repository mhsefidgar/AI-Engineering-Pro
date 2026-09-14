# Distributed Backend Systems — Python + TypeScript + Production

## Python implementation

Build a durable job API using FastAPI + PostgreSQL + Redis + a queue/worker framework. Persist job state before acknowledging important work. Implement idempotency, retries with exponential backoff and jitter, visibility/lease timeouts, cancellation, dead-letter handling, and progress reporting.

## TypeScript implementation

Build the equivalent service with Express/Node.js, PostgreSQL, Redis, and a durable queue library. Use a separate worker process. Ensure HTTP handlers never wait for long-running jobs.

## Production semantics

Explicitly choose and document at-least-once delivery, idempotent consumers, ordering requirements, retry limits, poison-message handling, backpressure, queue retention, and shutdown behavior. Do not claim exactly-once execution unless the architecture actually provides it.

## Cache

Implement cache-aside, TTL, invalidation, stampede protection, and graceful cache outage. Never make Redis availability equivalent to data durability unless the architecture intentionally requires it.

## Real-time

Expose job progress through WebSockets or SSE. Handle reconnects and missed events by allowing the client to query durable job state.

## Failure drills

Kill a worker after performing the side effect but before acknowledgement. Deliver the same message twice. Stop Redis. Stop PostgreSQL. Fill the queue. Make a dependency slow. Terminate the worker during shutdown. Verify idempotency, recovery, and observable state.

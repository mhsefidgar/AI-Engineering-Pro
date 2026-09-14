# Advanced Backend Lab

Build a job-backed notification service.

## Requirements

- `POST /v1/jobs` accepts work and returns a job ID.
- A worker consumes jobs asynchronously.
- PostgreSQL stores durable job state.
- Redis provides short-lived status caching and rate limiting.
- WebSocket clients receive job progress updates.
- Failed jobs use bounded retries and exponential backoff.
- A dead-letter path records permanently failed jobs.

## Failure scenarios

Test worker crashes, duplicate delivery, Redis outage, database outage, slow consumers, and poison messages.

## Engineering questions

- Is processing at-most-once, at-least-once, or effectively-once?
- What makes a job idempotent?
- When is a message acknowledged?
- What state belongs in Redis versus PostgreSQL?
- How do you prevent unbounded queue growth?

## Deliverable
Add metrics for queue depth, job age, success/failure rate, retry count, and processing latency. Document the recovery procedure for each failure scenario.
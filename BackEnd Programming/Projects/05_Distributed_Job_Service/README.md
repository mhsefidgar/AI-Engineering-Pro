# Project 05 — Distributed Job Service

Build a durable asynchronous processing platform.

## Required features

- submit job API;
- persistent job state;
- queue + workers;
- retries with exponential backoff and jitter;
- idempotent processing;
- dead-letter handling;
- cancellation;
- progress reporting;
- Redis status caching;
- WebSocket or SSE updates;
- metrics and alerts;
- integration tests with dependency failures.

## Failure injection

Kill workers mid-job, deliver a job twice, make Redis unavailable, make PostgreSQL unavailable, delay consumers, and send a poison message.

## Operational deliverable

Document SLOs for job acceptance latency, completion latency, success rate, and queue age. Create a runbook for stuck and repeatedly failing jobs.
# AI Backend — Python + TypeScript + Production Implementation

## Python implementation

Build an AI gateway with FastAPI and a provider-neutral interface:

```text
POST /v1/chat
POST /v1/chat/stream
GET  /v1/requests/{id}
```

Implement provider adapters, request validation, authentication, rate limits, per-request timeouts, bounded retries for retryable errors, fallback routing, usage accounting, cost estimation, streaming cancellation, and structured observability.

Add RAG as separate components: ingestion, chunking, embeddings, vector search, retrieval filters, context assembly, generation, and citations.

## TypeScript implementation

Build the same gateway with Express/Node.js and typed provider adapters. Validate runtime inputs. Use async iterators or streams for token streaming. Propagate client cancellation to the provider where the SDK permits it.

## Production AI concerns

Treat model providers as unreliable external dependencies. Define timeouts, retry budgets, 429 handling, provider fallback, model allowlists, maximum input/output tokens, spend budgets, per-tenant quotas, concurrency limits, and circuit/degradation behavior.

Record request ID, tenant, provider, model, status, latency, token usage, and estimated cost. Redact API keys and sensitive content. Decide explicitly what prompt/response data may be retained.

## MCP integration

Expose selected backend capabilities through FastMCP/MCP tools. Reuse the same application service as REST. Authorization must happen in the backend service, not in the model prompt. Validate model-generated tool arguments as untrusted input.

## AI failure lab

Simulate provider timeout, 429, malformed response, empty response, streaming disconnect, provider outage, budget exhaustion, retrieval returning no evidence, stale documents, cross-tenant retrieval, prompt injection, malicious tool arguments, and duplicate requests.

For each scenario specify fallback, retryability, user-visible error, metrics, logs, and cost impact.

## Production definition of done

- Python and TypeScript implementations expose the same contract.
- Provider SDKs are isolated behind adapters.
- API, security, reliability, and AI evaluation tests exist.
- Streaming is cancellation-aware.
- Usage/cost is measurable.
- Tenant isolation is tested.
- MCP tools share authorization and business logic with REST.
- Deployment includes Docker, CI, health/readiness, secret management, and a runbook.

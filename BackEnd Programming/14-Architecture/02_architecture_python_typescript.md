# Backend Architecture — Implementation Lab

## Reference architecture

```text
HTTP/MCP adapter
      -> application service
      -> domain policy
      -> repository/external adapter
      -> PostgreSQL / Redis / queue / AI provider
```

The transport layer should not contain business rules. Define interfaces at dependency boundaries so the same service can be exercised with fakes in unit tests and real infrastructure in integration tests.

## Python

Implement the architecture with FastAPI, Pydantic, SQLAlchemy, repository protocols, service classes/functions, and dependency injection. Add a worker process for durable asynchronous work.

## TypeScript

Implement the same architecture with Express, runtime schemas, typed interfaces, PostgreSQL, a service layer, repository adapters, and a worker process. Use dependency injection rather than importing global mutable clients throughout the codebase.

## Production decisions

Document when to use a modular monolith versus separate services. Define transaction ownership, consistency boundaries, retry ownership, idempotency keys, cache invalidation, queue delivery semantics, and API ownership before splitting services.

## AI architecture

Keep model providers behind an adapter interface. Keep retrieval behind a vector-search interface. Keep MCP behind a transport adapter. The application service should not depend directly on a vendor SDK or MCP framework.

## Failure exercise

Replace PostgreSQL with a fake repository in unit tests, then run against real PostgreSQL in integration tests. Inject provider timeout, queue failure, stale cache, and duplicate delivery. Verify that failure policy is enforced at the correct layer.

# Databases — Python + TypeScript + Production Lab

## PostgreSQL implementation

Implement the same persistence workflow from Python and TypeScript.

### Python

Use SQLAlchemy 2.x with PostgreSQL. Practice models, relationships, transactions, migrations, connection pools, parameterized queries, optimistic concurrency, and keyset pagination.

### TypeScript

Use a PostgreSQL driver or ORM such as `pg`, Prisma, Drizzle, or equivalent. Practice the same concepts and keep SQL behavior explicit enough to understand generated queries.

## Required exercises

- one-to-many and many-to-many relationships;
- unique and check constraints;
- indexes chosen from actual query patterns;
- transactions and rollback;
- isolation levels and concurrent updates;
- `EXPLAIN (ANALYZE, BUFFERS)`;
- cursor/keyset pagination;
- migration forward/backward strategy;
- connection-pool exhaustion;
- deadlock reproduction and retry policy;
- soft delete vs hard delete;
- audit events;
- tenant isolation.

## Production implementation

Run PostgreSQL in Docker Compose locally. Configure pool sizes from deployment capacity rather than using unlimited connections. Use migrations in CI/CD, backups and restore drills, least-privilege DB roles, TLS where required, secret management, query timeouts, slow-query monitoring, and explicit transaction boundaries.

Never construct SQL from untrusted strings. Never assume an ORM eliminates N+1 queries, transaction bugs, or poor indexing.

## AI backend exercise

Persist AI request metadata: request ID, tenant, model/provider, status, token usage, estimated cost, latency, timestamps, and error code. Keep raw prompts/responses out of durable storage unless there is a documented privacy and retention requirement.

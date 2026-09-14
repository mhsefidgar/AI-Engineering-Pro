# Database Engineering

Backend systems need reliable data modeling, queries, transactions, and operational discipline.

## PostgreSQL topics

- Relational modeling and normalization
- Primary/foreign keys and constraints
- SQL CRUD and joins
- Indexes and query plans
- Transactions and isolation
- Migrations
- Connection pooling
- Pagination

## Redis topics

- Key/value data
- Cache-aside pattern
- TTLs and invalidation
- Rate limiting
- Distributed locks: use only with a clear correctness model
- Queues and ephemeral state

## AI backend patterns

Store durable application state in PostgreSQL. Use Redis for latency-sensitive ephemeral data and caching. Store embeddings in a vector-capable datastore when semantic retrieval is required. Keep model/provider calls outside database transactions whenever possible.
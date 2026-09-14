# REST API Design

A useful API is predictable, explicit, secure, and easy to operate.

## Resource-oriented routes

Prefer nouns over verbs:

```text
GET    /users
GET    /users/{id}
POST   /users
PATCH  /users/{id}
DELETE /users/{id}
```

Use query parameters for filtering, sorting, and pagination:

```text
GET /orders?status=paid&limit=20&cursor=...
```

## Response design

Return stable JSON shapes and meaningful status codes. Document validation errors so clients can handle them programmatically.

## API checklist

- Consistent naming and resource hierarchy
- Request and response schemas
- Pagination for collections
- Explicit validation rules
- Authentication and authorization
- Idempotency where retries can create duplicate work
- Timeouts and rate limits
- OpenAPI documentation
- Versioning strategy
- Correlation/request IDs

## AI API extension

For AI endpoints also define model selection, token/cost metadata, streaming behavior, timeout policy, provider errors, and fallback behavior.
# Express: Production-Oriented Hands-On

## Build
Create an API with:

```text
src/
  app.ts
  server.ts
  routes/
  controllers/
  services/
  middleware/
  schemas/
  config/
  tests/
```

Implement `GET /health`, `GET /v1/users/:id`, `POST /v1/users`, and `DELETE /v1/users/:id`.

## Required behavior

- Validate bodies with a runtime schema library.
- Centralize error handling.
- Generate/propagate `X-Request-ID`.
- Add authentication middleware to protected routes.
- Add rate limiting.
- Set security headers.
- Use async handlers without swallowed promise rejections.
- Return consistent errors such as `{ "error": { "code": "validation_error", "message": "..." } }`.

## Testing lab

Write tests for:

1. valid user creation;
2. malformed payload;
3. duplicate email;
4. missing authentication;
5. forbidden resource access;
6. unknown route;
7. service/database failure;
8. request ID propagation.

## Production extension

Add OpenAPI documentation, graceful shutdown, structured logging, environment validation, Docker, and a CI test job.

## Exercise
Replace the in-memory repository with PostgreSQL while keeping the route/controller/service boundaries unchanged. This demonstrates why dependency inversion matters.
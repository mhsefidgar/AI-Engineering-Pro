# Service Architecture Lab

Refactor a growing API from route handlers into explicit boundaries.

## Target architecture

```text
HTTP -> Controller -> Service -> Repository -> Database
                  -> Cache
                  -> Queue
                  -> External provider
```

## Hands-on milestones

1. Start with a single endpoint and write tests.
2. Extract domain/service logic from HTTP code.
3. Introduce repository interfaces.
4. Inject implementations rather than importing infrastructure everywhere.
5. Add transaction boundaries.
6. Add an asynchronous queue for slow work.
7. Define failure behavior for each dependency.

## Architecture exercises

- Decide where validation belongs.
- Decide where authorization belongs.
- Define which errors are domain errors vs infrastructure errors.
- Demonstrate how a provider can be replaced without changing the API layer.
- Draw a dependency diagram and identify all trust boundaries.

## Definition of done

The same service tests run against an in-memory fake repository and the real database adapter, while HTTP tests verify only the API contract.
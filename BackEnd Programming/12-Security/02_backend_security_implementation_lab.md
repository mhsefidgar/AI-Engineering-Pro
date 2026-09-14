# Backend Security — Implementation Lab

## Python implementation

Harden a FastAPI service with Pydantic validation, SQLAlchemy parameterized queries, authentication/authorization dependencies, CORS policy, trusted-host configuration, request-size limits, rate limiting, outbound HTTP timeouts/allowlists, and redacted structured logging.

## TypeScript implementation

Harden an Express service with runtime schema validation, parameterized SQL, authentication middleware, authorization policies, Helmet/security headers, explicit CORS, rate limiting, body-size limits, outbound URL validation, and secret redaction.

## AI backend security

Add controls for prompt injection and tool abuse:

- treat retrieved documents as untrusted data;
- separate instructions from retrieved/user content;
- validate tool arguments independently of model output;
- enforce authorization outside the model;
- restrict network destinations for tools;
- cap tool calls and output size;
- require explicit confirmation for high-impact actions;
- record audit events without storing unnecessary sensitive content.

## Production threat model

Analyze SQL injection, BOLA/IDOR, credential stuffing, SSRF, secret leakage, oversized payloads, dependency compromise, unsafe deserialization, prompt injection, tool injection, denial of service, and tenant-isolation failures.

For each threat, implement a control, write an automated regression test, and document detection/recovery.

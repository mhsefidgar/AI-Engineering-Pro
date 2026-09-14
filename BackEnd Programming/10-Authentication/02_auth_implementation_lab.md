# Authentication & Authorization — Python + TypeScript + Production

## Python implementation

Build OAuth2/JWT authentication in FastAPI. Hash passwords with Argon2id or an equivalent modern password hash. Use short-lived access tokens and rotating refresh tokens. Store refresh-token state securely so revocation is enforceable.

Implement dependencies for:

```text
get_current_user -> require_role -> require_resource_owner
```

Test expired, malformed, revoked, wrong-audience, wrong-issuer, wrong-password, insufficient-role, and cross-tenant requests.

## TypeScript implementation

Implement the equivalent flow in Express with a maintained JWT/OIDC library. Validate token claims, use middleware for authentication, and keep authorization checks in a reusable policy/service layer.

## Production

Prefer an external OIDC identity provider for production user identity where appropriate. Validate `iss`, `aud`, signature, expiry, and algorithm. Rotate signing keys. Keep secrets in a secret manager. Use secure cookies for browser refresh flows where appropriate. Add CSRF protection when cookie authentication is used.

Authorization is not authentication: every object access must enforce tenant/resource permissions. Log security events without logging tokens or passwords. Rate-limit login/refresh endpoints and monitor credential-stuffing indicators.

## Incident drills

- stolen/revoked refresh token;
- signing-key rotation;
- disabled user with a previously issued token;
- privilege escalation attempt;
- cross-tenant ID enumeration;
- repeated failed login;
- identity-provider outage.

Define detection, response, and recovery for each drill.

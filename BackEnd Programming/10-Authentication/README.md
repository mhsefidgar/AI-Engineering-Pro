# Authentication and Authorization

Authentication answers **who are you?** Authorization answers **what are you allowed to do?**

## Topics

- Cookie-based sessions
- JWT access tokens
- Refresh tokens and rotation
- OAuth2/OIDC concepts
- Password hashing
- Role-based access control (RBAC)
- Resource-level authorization
- Token expiration and revocation

## Rules

Never store plaintext passwords. Keep secrets outside source control. Validate token issuer, audience, signature, and expiration. Enforce authorization on the server for every protected operation.

For browser applications, carefully evaluate cookie flags, CSRF protection, CORS, and XSS exposure before choosing a token transport.
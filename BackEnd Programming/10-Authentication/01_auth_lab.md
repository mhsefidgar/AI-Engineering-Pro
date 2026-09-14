# Authentication & Authorization Lab

Build a protected project API.

## Milestones

1. Hash passwords with Argon2 or bcrypt.
2. Implement login and short-lived access tokens.
3. Implement refresh-token rotation and revocation.
4. Add role-based authorization (`admin`, `member`).
5. Add resource-level authorization so users can access only their projects.
6. Add OAuth2/OIDC as a second authentication mechanism.

## Test cases

- expired token;
- malformed token;
- revoked refresh token;
- wrong password;
- privilege escalation attempt;
- cross-user project access;
- replayed refresh token.

## Security rules

Never store plaintext passwords or long-lived bearer tokens unnecessarily. Keep secrets in environment/secret management, validate token issuer/audience, use TLS, and avoid logging credentials or authorization headers.

## Deliverable
Document the authentication sequence and authorization decision for every protected endpoint.
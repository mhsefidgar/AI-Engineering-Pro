# Backend Security Lab

Threat-model the project API, then implement defenses.

## Attack scenarios

1. SQL injection through a search parameter.
2. Broken object-level authorization by changing `/projects/{id}`.
3. Credential stuffing against login.
4. Excessive payload size.
5. SSRF through a user-supplied URL.
6. CORS misconfiguration.
7. Sensitive data leaking into logs.
8. Prompt injection causing an AI tool to perform an unauthorized action.

## Hands-on controls

- Use parameterized SQL.
- Authorize every object access server-side.
- Rate-limit authentication and expensive endpoints.
- Set body/file size limits and request timeouts.
- Use an allowlist for outbound destinations where possible.
- Configure CORS explicitly.
- Redact secrets and personal data in logs.
- Validate tool arguments and enforce authorization before MCP/tool execution.

## Deliverable
For each threat, document attack path, trust boundary, mitigation, test case, and residual risk.
# Backend Security

Security is part of the API design, not a final checklist.

## Core topics

- OWASP API risks
- Input validation
- SQL injection
- XSS and output encoding
- CSRF
- CORS
- Rate limiting
- Security headers
- Secret management
- Dependency and supply-chain hygiene
- Authentication and authorization

## Practical baseline

Validate at trust boundaries. Parameterize SQL. Use least privilege. Set explicit CORS policies. Rate-limit expensive endpoints. Keep dependencies updated. Return safe error messages while logging enough server-side context for diagnosis.

For AI systems, treat prompts, retrieved documents, tool arguments, and model outputs as untrusted data. Add authorization around tools and protect against prompt injection when model output can trigger backend actions.
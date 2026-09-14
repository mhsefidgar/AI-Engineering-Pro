# FastMCP / MCP — Production Implementation Lab

## Goal

Expose a real backend capability to an AI agent through MCP while keeping business logic independent of the MCP transport.

Architecture:

```text
MCP Client/Agent
      |
   FastMCP
      |
 authorization + validation + audit
      |
 application service
      |
 repository / external APIs / PostgreSQL
```

## Python implementation

Build a FastMCP server with:

- typed tool inputs and outputs;
- tools for read and write operations;
- resources for bounded read-only context;
- prompts only for reusable prompt templates, not hidden business authorization;
- service/repository boundaries;
- authentication and authorization before sensitive operations;
- output-size limits;
- timeouts for external dependencies;
- structured audit events for tool calls;
- tests for valid, invalid, unauthorized, and dependency-failure cases.

A tool should call the same service used by FastAPI rather than duplicating business logic.

## REST + MCP implementation

Expose one capability through both:

```text
POST /v1/projects/{id}/archive
```

and an MCP tool such as:

```text
archive_project(project_id)
```

The service owns the business rule. FastAPI and FastMCP are adapters.

## Production security

Treat tool arguments as untrusted input. Enforce tenant isolation, user permissions, resource ownership, allowlists, bounded output, rate limits, dependency timeouts, audit logging, and explicit confirmation for high-impact writes. Do not assume an MCP client is trusted because it is an AI agent.

## Failure lab

- invalid tool arguments;
- unauthorized project access;
- cross-tenant resource ID;
- dependency timeout;
- dependency 429;
- tool output larger than the configured limit;
- repeated write request;
- MCP client disconnect;
- service/database outage.

Document whether each failure is retryable and how it appears in logs and metrics.

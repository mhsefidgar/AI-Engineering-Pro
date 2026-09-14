# Project 03 — FastAPI + FastMCP Platform

Build one business capability exposed through both REST and MCP.

## Architecture

```text
REST / MCP
    |
Application service
    |
Repository / external adapters
    |
PostgreSQL / Redis / external APIs
```

## Requirements

- shared domain/service layer;
- FastAPI REST endpoints;
- FastMCP tools, resources, and prompts;
- authentication and authorization at the service boundary;
- strict tool input validation;
- bounded tool output;
- audit logging;
- dependency timeouts and retry policies;
- tests for both interfaces;
- OpenAPI documentation for REST;
- MCP usage documentation;
- Dockerized local environment.

## Security lab

Create a write-capable MCP tool. Demonstrate that an untrusted prompt cannot bypass application authorization or invoke the tool for another user.

## Reliability lab

Make the external dependency fail and verify both REST and MCP return controlled errors while preserving request/tool correlation IDs.
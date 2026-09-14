# FastMCP and MCP

Model Context Protocol (MCP) provides a standardized way for AI applications to discover and use external capabilities. FastMCP makes it practical to build MCP servers in Python.

## Core concepts

- MCP client/server architecture
- Tools: callable operations
- Resources: readable contextual data
- Prompts: reusable interaction templates
- Transports and server lifecycle
- Authentication and authorization
- Error handling and validation
- Testing MCP servers
- FastAPI integration
- Production deployment and observability

## Tool example

```python
from fastmcp import FastMCP

mcp = FastMCP("backend-tools")

@mcp.tool
def get_user_status(user_id: str) -> str:
    return f"status for {user_id}: active"
```

## Backend integration pattern

```text
AI application
    |
    | MCP
    v
FastMCP server
    |
    +-- service layer
    +-- database
    +-- external APIs
    +-- internal backend APIs
```

MCP should not replace normal REST APIs. REST is commonly used for application-to-application HTTP contracts, while MCP exposes capabilities and contextual interfaces to MCP-aware AI clients.

## Security

Treat tool arguments as untrusted input. Authenticate clients where required, authorize every sensitive operation, validate arguments, apply timeouts and rate limits, and avoid exposing unrestricted database or shell access.
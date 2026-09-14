"""FastMCP hands-on lab.

Install the FastMCP package used by your environment, then adapt the imports
if its API version differs.
"""
from fastmcp import FastMCP

mcp = FastMCP("project-tools")

@mcp.tool
async def get_project(project_id: int) -> dict:
    """Return project metadata for an authorized project."""
    if project_id <= 0:
        raise ValueError("project_id must be positive")
    return {"id": project_id, "status": "active"}

@mcp.resource("project://{project_id}")
async def project_resource(project_id: int) -> str:
    return f"Project {project_id}: active"

@mcp.prompt
async def project_summary(project_id: int) -> str:
    return f"Summarize project {project_id} using only authorized project data."

if __name__ == "__main__":
    mcp.run()

# Exercises:
# 1. Replace the stub with a repository/service call.
# 2. Add authorization before tool execution.
# 3. Validate every tool argument.
# 4. Add structured audit logs for tool calls.
# 5. Add tests for invalid IDs and unauthorized access.
# 6. Expose the same service through FastAPI and MCP without duplicating domain logic.
# 7. Add an external API tool with timeout, retry, and secret redaction.

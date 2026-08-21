"""Local MCP Server — system time access via stdio transport."""

from datetime import datetime

from mcp.server.fastmcp import FastMCP

# create mcp server, named as "local-tools"
mcp = FastMCP("local-tools")

# register tool
@mcp.tool()
def get_current_datetime() -> str:
    """Get the current local date and time."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S (%A)")

# # register another tool
# @mcp.tool()
# def get_username() -> str:
#     """Return the current user name."""
#     return "Fan"

if __name__ == "__main__":
    mcp.run(transport="stdio") #Local MCP server, transport mode is stdio

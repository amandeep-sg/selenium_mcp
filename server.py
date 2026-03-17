from fastmcp import FastMCP

mcp = FastMCP("rfp_notifications")

@mcp.tool()
def get_rfp_notifications():
    """Get RFP notifications"""
    return "RFP notifications"
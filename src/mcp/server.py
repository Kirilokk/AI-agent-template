from mcp.server.fastmcp import FastMCP

from src.mcp.tools.weather import get_alerts, get_forecast


def register_tools(mcp_server):
    mcp_server.add_tool(fn=get_alerts)
    mcp_server.add_tool(fn=get_forecast)


# === App Entry ===
if __name__ == "__main__":
    mcp = FastMCP(name="System server", host="0.0.0.0", port=6274)
    register_tools(mcp_server=mcp)
    mcp.run(transport="stdio")

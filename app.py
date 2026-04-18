from fastmcp import FastMCP

mcp = FastMCP("mi-servidor-mcp")

@mcp.tool()
def ping() -> str:
    return "pong"

@mcp.tool()
def saludar(nombre: str) -> str:
    return f"Hola {nombre}, tu MCP en Render funciona correctamente 🚀"

# Endpoint MCP
app = mcp.http_app(path="/mcp")

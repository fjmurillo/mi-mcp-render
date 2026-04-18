from fastmcp import FastMCP
import requests
import os

mcp = FastMCP("mi-servidor-mcp")

@mcp.tool
def ping() -> str:
    """Valida que el servidor está activo."""
    return "pong"

@mcp.tool
def saludar(nombre: str) -> str:
    """Devuelve un saludo simple."""
    return f"Hola {nombre}, tu MCP está funcionando. Cambio esperado en render.com"

@mcp.tool
def usd_cop()  -> str:
    """
    Consulta tipo de cambio USD a COP
    """
    url = "https://api.exchangerate.host/convert?from=USD&to=COP"

    r = requests.get(url, timeout=10)
    data = r.json()


    rate = data["result"]

    return f"1 USD = {rate:,.2f} COP"
    



if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
    )
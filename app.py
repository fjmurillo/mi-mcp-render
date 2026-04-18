from fastmcp import FastMCP
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
def clima_bogota():
    """
    Consulta clima actual de Bogotá
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=4.71&longitude=-74.07&current_weather=true"

    r = requests.get(url, timeout=10)
    data = r.json()

    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]

    return f"Bogotá: {temp}°C, viento {wind} km/h"   



if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
    )
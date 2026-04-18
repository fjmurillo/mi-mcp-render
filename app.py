from fastmcp import FastMCP
import requests
import os

mcp = FastMCP("mi-servidor-mcp")

SAP_URL = "http://epiuses4hana.epiuse.com.co:9001/sap/opu/odata/sap/ZSACHR_REPORT_TIME_SRV/ET_REPORT_TIMESet?$filter=ImProyecto eq '1000613'"
SAP_USER = "USER_SAC"
SAP_PASS = "xxxx"

@mcp.tool
def oData() -> str:
    """
    Consulta oData SAP
    """

    params = {
        "$top": 5,
        "$format": "json"
    }

    r = requests.get(
        SAP_URL,
        params=params,
        auth=(SAP_USER, SAP_PASS),
        timeout=20
    )

    r.raise_for_status()

    data = r.json()


    return  f"{data}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp",
    )
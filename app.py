from fastmcp import FastMCP
import requests
import os

mcp = FastMCP("sap-mcp")

SAP_URL = "http://epiuses4hana.epiuse.com.co:9001/sap/opu/odata/sap/ZSACHR_REPORT_TIME_SRV/ET_REPORT_TIMESet?$filter=ImProyecto eq '1000613'"
SAP_USER = "USER_SAC"
SAP_PASS = "Conexion*SAC.2026"

@mcp.tool
def business_partners() -> str:
    """
    Consulta Business Partners SAP
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
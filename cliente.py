import requests
import json

URL = "https://mi-mcp-render.onrender.com/mcp"

base_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
}

# 1) initialize
init_payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "FRANCO-TEST-CLIENT",
            "version": "1.0.0"
        }
    }
}

init_response = requests.post(URL, headers=base_headers, json=init_payload)

print("=== INITIALIZE ===")
print("STATUS:", init_response.status_code)
print("HEADERS:", dict(init_response.headers))
print("BODY:", init_response.text)

session_id = init_response.headers.get("mcp-session-id")
if not session_id:
    raise RuntimeError("No llegó mcp-session-id en la respuesta de initialize")

headers_with_session = {
    **base_headers,
    "mcp-session-id": session_id
}



call_payload = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "oData",
        "arguments": {}
    }
}

call_response = requests.post(URL, headers=headers_with_session, json=call_payload)

print("\n=== TOOLS/CALL clima_bogota ===")
print("STATUS:", call_response.status_code)
print("BODY:", call_response.text)
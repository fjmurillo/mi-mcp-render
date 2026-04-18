import requests
import json

URL = "http://localhost:8000/mcp"

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
            "name": "python-test-client",
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

# 2) tools/list
list_payload = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}

list_response = requests.post(URL, headers=headers_with_session, json=list_payload)

print("\n=== TOOLS/LIST ===")
print("STATUS:", list_response.status_code)
print("BODY:", list_response.text)

# 3) tools/call -> ping
call_payload = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "ping",
        "arguments": {}
    }
}

call_response = requests.post(URL, headers=headers_with_session, json=call_payload)

print("\n=== TOOLS/CALL ping ===")
print("STATUS:", call_response.status_code)
print("BODY:", call_response.text)
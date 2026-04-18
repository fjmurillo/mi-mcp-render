import requests

URL = "http://localhost:10000/mcp"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
}

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}

r = requests.post(URL, headers=headers, json=payload)

print("STATUS:", r.status_code)
print(r.text)

import subprocess
import json

# Start the MCP server
proc = subprocess.Popen(
    ["python", "weather_serverQ4.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

# Step 1: Send initialization request
init_message = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "roots": {"listChanged": True},
            "sampling": {}
        },
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    }
}

# Send the message
message_str = json.dumps(init_message)
print(f"➡️ Sending to server:\n{message_str}")
proc.stdin.write(message_str + "\n")
proc.stdin.flush()

# Read the response
response = proc.stdout.readline()
print(f"\n⬅️ Response from server:\n{response.strip()}")

# Kill the process for now (optional)
proc.kill()

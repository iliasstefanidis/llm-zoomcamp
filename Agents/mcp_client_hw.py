import asyncio
from fastmcp import Client

async def main():
    async with Client("weather_serverQ4.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print("Available tools:", tools)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print("Error:", e)

from fastmcp import Client as MCPClient
import asyncio


async def main():
    async with MCPClient("weather_server.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"Available tools: {tools}    ")


if __name__ == "__main__":
    test = asyncio.run(main())

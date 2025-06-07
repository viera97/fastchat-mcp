from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio

def get_session_data(http: str) -> dict:
    return asyncio.run(async_get_session(http))

async def async_get_session(http: str):
    # Connect to a streamable HTTP server
    async with streamablehttp_client(http) as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            tools = await session.list_tools()
            resources = await session.list_resources()
            prompts = await session.list_prompts()

            data: dict = {
                "tools": tools.tools,
                "resources": resources.resources,
                "prompts": prompts.prompts,
            }

        return data

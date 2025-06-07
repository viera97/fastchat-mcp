from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio


def call_tool(http: str) -> any:
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

            # Read a resource
            resource_result = await session.read_resource("data://user-profile/14516")
            return resource_result

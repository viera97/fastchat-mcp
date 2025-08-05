import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from ....config.logger import logging
import asyncio
import shutil


def get_session_data(server: dict) -> dict:
    return asyncio.run(async_get_session(server=server))


async def async_get_session(server: dict) -> dict:
    """Initialize the server connection."""
    name: str = server["name"]
    config: dict = server["config"]

    server_params = StdioServerParameters(
        command=(
            shutil.which("npx") if config["command"] == "npx" else config["command"]
        ),
        args=config["args"],
        env={**os.environ, **config["env"]} if config.get("env") else None,
    )
    try:
        stdio_context = stdio_client(server_params)
        read, write = await stdio_context.__aenter__()
        session = ClientSession(read, write)
        await session.__aenter__()
        capabilities = await session.initialize()
    except Exception as e:
        logging.error(f"Error initializing server {name}: {e}")
        raise Exception(f"Error initializing server {name}: {e}")

from mcp_oauth import OAuthClient
from mcp.client.auth import OAuthClientProvider
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio

from ..service import Service


class Tool(Service):
    """Represents a tool that can be called with arguments."""

    def __init__(self, http, data, server):
        super().__init__(http, data, server)
        args = data.inputSchema["properties"]
        self.args = []
        for key in args.keys():
            arg_type = args[key].get("type", None)
            if arg_type is None:
                if "anyOf" in args[key]:
                    arg_type = ""
                    for type_ in args[key]["anyOf"]:
                        arg_type += type_["type"] + " | "
                    arg_type = arg_type[:-3]  # Remove the last " | "

            self.args.append(
                {
                    "name": key,
                    "type": arg_type,
                }
            )

    def __call__(self, args: dict[str, any]):
        return self.call(args)

    def call(self, args: dict[str, any]):
        return asyncio.run(
            Tool.async_call(
                self.http,
                self.name,
                args,
                self.oauth_client,
                self.headers,
            )
        )

    @staticmethod
    async def async_call(
        http: str,
        toolname: str,
        args: dict,
        oauth_client: OAuthClient | None,
        headers: dict[str, str] = None,
    ):
        oauth: OAuthClientProvider = (
            oauth_client.oauth if oauth_client is not None else None
        )
        async with streamablehttp_client(url=http, auth=oauth, headers=headers) as (
            read_stream,
            write_stream,
            _,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()

                # Call a tool
                tool_result = await session.call_tool(toolname, args)
                return tool_result.content

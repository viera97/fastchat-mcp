from mcp_oauth import OAuthClient
from mcp.client.auth import OAuthClientProvider
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio

from ..service import Service


class Prompt(Service):
    """Represents a prompt that can be called with arguments."""

    def __init__(self, http, data, server):
        super().__init__(http, data, server)
        self.args = [{"name": arg.name, "type": "string"} for arg in data.arguments]

    def __call__(self, args: dict[str, any]):
        return self.get(args)

    def get(self, args: dict[str, any]):
        args = {key: str(args[key]) for key in args.keys()}

        return asyncio.run(
            Prompt.async_get(
                self.http,
                self.name,
                args,
                self.oauth_client,
                self.headers,
            )
        )

    @staticmethod
    async def async_get(
        http: str,
        promptname: str,
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

                # get a prompt
                prompt_result = await session.get_prompt(
                    name=promptname, arguments=args
                )
                return prompt_result.messages

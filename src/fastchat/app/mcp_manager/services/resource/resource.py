from mcp_oauth import OAuthClient
from mcp.client.auth import OAuthClientProvider
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio

from ..service import Service
from . import utils


class Resource(Service):
    """Represents a resource that can be read with arguments."""

    def __init__(self, http, data, server):
        super().__init__(http, data, server)
        self.args = utils.get_args_from_uri(data.uriTemplate)
        self.args = [{"name": arg, "type": "string"} for arg in self.args]

    def __call__(self, args: dict[str, any]):
        return self.read(args)

    def read(self, args: dict[str, str]):
        uri = self.data.uriTemplate
        for key in args:
            uri = uri.replace("{" + key + "}", str(args[key]))
        return asyncio.run(
            Resource.async_read(
                self.http,
                uri,
                self.oauth_client,
                self.headers,
            )
        )

    @staticmethod
    async def async_read(
        http: str,
        uri: str,
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

                # Read a resource
                resource_result = await session.read_resource(uri)
                return resource_result.contents

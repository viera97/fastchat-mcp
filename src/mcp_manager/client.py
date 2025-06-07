from .servers import Servers
from .connections.session_data import get_session_data
from .connections.call_tool import call_tool
from .connections.read_resource import read_resource
from ..tools.get_uri_args import get_args_from_uri
from mcp import ClientSession


class ClientManagerMCP:
    def __init__(self):
        self.tools: dict | None = None
        self.resources: dict | None = None
        self.prompts: dict | None = None
        self.services: dict | None = None
        self.refresh_data()

    def call_tool(self, name: str, args: dict) -> str | None:
        tool = self.tools[name]
        return call_tool(
            http=tool["http"],
            toolname=tool["data"].name,
            args=args,
        )[0].text

    def read_resource(self, name: str, args: dict) -> str | None:
        resource = self.resources[name]
        uri = resource["data"].uriTemplate
        for key in args:
            uri = uri.replace("{" + key + "}", str(args[key]))

        return read_resource(
            http=resource["http"],
            uri=uri,
        )[0].text

    def get_prompts(self) -> dict:
        pass

    def refresh_data(self):
        """
        Inicializa o refresca la lista de herramientas, recursos o promps que sirve cada uno de los servidores, y lo organiza en forma de diccionario
        donde cada valor posee informacion de cada servicio ademas de la direccion desde la cual se sirve
        """
        self.tools, self.resources, self.prompts = ({}, {}, {})
        mcp_servers: dict[str, dict] = Servers().mcp_servers

        for server_key in mcp_servers.keys():
            server = mcp_servers[server_key]
            session: dict = get_session_data(server["http"])
            for tool in session["tools"]:
                self.tools[f"{server_key}_{tool.name}"] = {
                    "http": server["http"],
                    "data": tool,
                }
            for resource in session["resources"]:
                args: str = get_args_from_uri(resource.uriTemplate)
                self.resources[f"{server_key}_{resource.name}"] = {
                    "http": server["http"],
                    "data": resource,
                    "args": args,
                }

            for prompt in session["prompts"]:
                self.prompts[f"{server_key}_{prompt.name}"] = {
                    "http": server["http"],
                    "data": prompt,
                }

        self.services = self.tools + self.resources

    def service_type(self, service_key: str) -> str:
        if self.tools.keys().__contains__(service_key):
            return "tool"
        if self.resources.keys().__contains__(service_key):
            return "resource"

from .servers import Servers
from .connections.session_data import get_session_data
from .connections.call_tool import call_tool
from mcp import ClientSession


class ClientManagerMCP:
    def __init__(self):
        self.tools: dict | None = None
        self.resources: dict | None = None
        self.prompts: dict | None = None
        self.refresh_data()

    def call_tool(self, name: str, args: dict) -> str | None:
        tool = self.tools[name]
        return call_tool(tool["http"], tool["data"].name, args)[0].text

    def get_resource(self, uri: str) -> dict:
        pass

    def get_prompts(self) -> dict:
        pass

    def refresh_data(self):
        """
        Inicializa o refresca la lista de herramientas, recursos o promps que sirve cada uno de los servidores, y lo organiza en forma de diccionario
        donde cada valor posee informacion de cada servicio ademas de la direccion desde la cual se sirve
        """
        self.tools = {}
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
                self.resources[f"{server_key}_{resource.name}"] = {
                    "http": server["http"],
                    "data": resource,
                }

            for prompt in session["prompts"]:
                self.prompts[f"{server_key}_{prompt.name}"] = {
                    "http": server["http"],
                    "data": prompt,
                }

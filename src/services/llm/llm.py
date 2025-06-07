import json
from ...mcp_manager.client import ClientManagerMCP


class LLM:
    def __init__(self):
        self.client_manager: ClientManagerMCP = ClientManagerMCP()

    def get_query(self, query: str) -> str:
        self.append_chat_history()
        # Cargar los servicios utiles
        services = json.loads(self.select_services(query))["services"]
        if len(services) == 0:
            return self.simple_query(query)

        args = self.generate_args(query=query, services=services)
        return self.final_response(query, args)

    def append_chat_history(self):
        Exception("Not Implemented Exception")

    def simple_query(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def select_services(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def generate_args(self, query: str, services: str | dict) -> str:
        Exception("Not Implemented Exception")

    def final_response(self, query: str, services_args: str | dict) -> str:
        Exception("Not Implemented Exception")

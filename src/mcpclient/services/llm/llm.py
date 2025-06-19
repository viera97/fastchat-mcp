import json
from ...mcp_manager.client import ClientManagerMCP


class LLM:
    def __init__(self):
        self.client_manager_mcp: ClientManagerMCP = ClientManagerMCP()
        self.current_language: str = "English"

    def __call__(self, query: str):
        processed_query: dict = self.preprocess_query(query=query)
        querys: list[str] = processed_query["querys"]
        self.current_language = processed_query["language"]

        end_response: str = ""
        for query in querys:
            end_response += self.proccess_query(query) + "\n\n"
        return end_response

    def preprocess_query(self, query: str) -> dict:
        """
        Devuelve una lista con todas las querys en las que se divide la query principal y el lenguaje usado en la query. Puede ser solo una query
        """
        Exception("Not Implemented")

    def proccess_query(self, query: str) -> str:
        self.append_chat_history()
        # Cargar los servicios utiles
        service = json.loads(self.select_services(query))["service"]
        if len(service) == 0:
            return self.simple_query(query)
        else:
            service = (
                self.client_manager_mcp.resources[service]
                if (self.client_manager_mcp.service_type(service) == "resource")
                else (
                    self.client_manager_mcp.tools[service]
                    if (self.client_manager_mcp.service_type(service) == "tool")
                    else None
                )
            )

        args = json.loads(self.generate_args(query=query, service=service))["args"]
        data = service(args)[0].text
        return self.final_response(query, data)

    def append_chat_history(self):
        Exception("Not Implemented Exception")

    def simple_query(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def select_services(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def generate_args(self, query: str, service: str) -> str:
        Exception("Not Implemented Exception")

    def final_response(self, query: str, data: str | dict) -> str:
        Exception("Not Implemented Exception")

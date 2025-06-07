class LLM:
    def __init__(self):
        pass

    def get_query(self, query: str) -> str:
        services = self.select_services(query)
        args = self.generate_args(query=query, services=services)
        return self.final_response(query, args)

    def simple_query(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def select_services(self, query: str) -> str:
        Exception("Not Implemented Exception")

    def generate_args(self, query: str, services: str | dict) -> str:
        Exception("Not Implemented Exception")

    def final_response(self, query: str, services_args: str | dict) -> str:
        Exception("Not Implemented Exception")

from src.services.llm.models.openai_service.gpt import GPT
from src.services.llm.llm import LLM
from src.tools.clear_console import clear_console
from src.mcp_manager.client import ClientManagerMCP

# client: ClientManagerMCP = ClientManagerMCP()
# print(client.call_tool("example_server_add", {"a": 142, "b": 21}))
# print(client.read_resource("example_server_user_profile", {"user_id": 14516}))

gpt: LLM = GPT()

clear_console()
while True:
    query = input("> ")
    print(gpt.user_query(query))

from src.services.llm.openai_service.gpt import GPT
from src.tools.clear_console import clear_console
from src.mcp_manager.client import ClientManagerMCP

client: ClientManagerMCP = ClientManagerMCP()
print(client.call_tool("example_server_add", {"a": 12, "b": 21}))


# gpt: GPT = GPT()

# clear_console()
# while True:
#     query = input("> ")
#     print(gpt.user_query(query))

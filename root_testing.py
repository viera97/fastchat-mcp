from src.services.llm.models.openai_service.gpt import GPT
from src.services.llm.llm import LLM
from src.tools.clear_console import clear_console
from src.mcp_manager.client import ClientManagerMCP

gpt: LLM = GPT()

clear_console()
while True:
    query = input("> ")
    print(gpt.process_query(query))

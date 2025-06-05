from src.services.llm.openai_service.gpt import GPT
from src.tools.clear_console import clear_console

gpt: GPT = GPT()

clear_console()
while True:
    query = input("> ")
    print(gpt.secuential_user_query(query))

from fastmcpclient.services.llm.models.openai_service.gpt import GPT
from fastmcpclient.services.llm.client_llm import ClientLLM
from fastmcpclient.tools.clear_console import clear_console

client: ClientLLM = ClientLLM()

clear_console()
while True:
    query = input("> ")
    print(client(query))

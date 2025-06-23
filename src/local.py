from mcpclient.services.llm.client_llm import ClientLLM
from mcpclient.tools.clear_console import clear_console

client: ClientLLM = ClientLLM()

clear_console()
while True:
    query = input("> ")
    response = client(query)
    for step in response:
        print(step)
    print(response)

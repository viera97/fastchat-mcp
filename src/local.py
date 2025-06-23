from mcpclient.services.llm.client_llm import ClientLLM
from mcpclient.tools.clear_console import clear_console
import os

clear_console()
client: ClientLLM = ClientLLM()
print("\n")

md: str = ""
filename: str | None = None
sep = os.path.sep


while True:
    query = input("> ")
    if query == "exit" or query == "":
        if md != "":
            chats_path = f"{os.getcwd()}{sep}chats{sep}"
            os.makedirs(os.path.dirname(chats_path), exist_ok=True)
            with open(f"{chats_path}{filename}.md", "w") as file:
                file.write(md)
        break

    if filename is None:
        filename = f"{query[:15]}..."

    md += f"# {query}"
    index = 1
    for step in client(query):
        md += str(step)
        if step.type == "response":
            print(f"<< {step.response}")
        if step.type == "query":
            print(f">> {step.query}")
            index = 1
        if step.type == "data":
            print(f'   {str(step).replace("*", "").replace("-", "*")}')
        if step.type == "step":
            print(f"  {index}. {step.step}")
            index += 1
    md += "\n"

# Hola, necesito que me recuperes la informaciond del usuario con id = 12390 desde la base de datos. Luego usa la misma informacion de este usuario y agregalo a la base de datos pero con el id =4321

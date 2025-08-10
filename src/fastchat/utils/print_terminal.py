from collections.abc import Generator
from ..app.chat.features.step import Step


def print2terminal(chat_response: Generator[Step, None, None]):
    index = 1
    for step in chat_response:
        if step.type == "response":
            if step.json["first_chunk"]:
                print(f"<< {step.response}", end="")
            else:
                print(f"{step.response}", end="")
        if step.type == "query":
            print(f">> {step.query}")
            index = 1
        if step.type == "data":
            print(f'   {str(step).replace("**", "").replace("- ", "• ")}')
        if step.type == "step":
            print(f"  {index}. {step.step}")
            index += 1

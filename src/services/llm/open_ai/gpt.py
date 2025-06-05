from ....config.llm_config import ConfigGPT
from openai import OpenAI, AsyncOpenAI
import json


class GPT:
    """
    ## GPT
    GPT es usado para realizar servicios a la api de gpt openAI.
    #### inputs:
    - `model`: modelo de gpt que se utilizara
    """

    def __init__(
        self,
        model=ConfigGPT.DEFAULT_MODEL_NAME,
        max_history_len: int = 10,
    ):
        # Cliente secuencial de GPT
        self.client = OpenAI(
            api_key=ConfigGPT.OPENAI_API_KEY,
        )

        # Cliente asincrono de GPT
        self.asyncclient = AsyncOpenAI(
            api_key=ConfigGPT.OPENAI_API_KEY,
        )

        self.max_len_history: int = 10
        """Maxima cantidad de mensajes previos que se le pasan como input"""

        self.chat_history: list[list[dict[str, str]]] = {}
        """Historial del chat asosiado a esta instancia de GPT, en forma lista de listas, por ejemplo 
        ```
        chat_history: str = [
            [
                {"role": "user", "content": "query1"},
                {"role": "assistant", "content": "response1"}
            ],
            [
                {"role": "user", "content": "query2"},
                {"role": "assistant", "content": "response2"}
            ]
        ]
        ```
        """

        self.model: str = model
        self.current_price: float = 0

    async def user_query(self, query: str) -> str:
        """ """
        system_message: str = ""
        user_message: dict[str, str] = {"role": "user", "content": query}
        self.chat_history.append([])

        self.chat_history[-1].append(user_message)

        messages: dict = [
            message
            for message in [
                messages for messages in self.chat_history[-self.max_len_history :]
            ]
        ]
        messages.insert(0, {"role": "system", "content": system_message})

        completion = await self.asyncclient.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        response = completion.choices[0].message.content
        self.chat_history[-1].append({"role": "assistant", "content": response})
        self.get_price(completion.usage)
        return response

    def get_price(self, usage) -> float:
        """
        ### Args
            - `usage`: uso de la api retornado en el completion respuesta del llamado a la api de gpt
        ### Outs:
            - `price`: precio final del llamado a la api.
        """

        input_tokens: int = usage.prompt_tokens
        output_tokens: int = usage.completion_tokens

        input_price: float = ConfigGPT.MODEL_PRICE[self.model]["input"]
        output_price: float = ConfigGPT.MODEL_PRICE[self.model]["output"]
        price: float = input_tokens * input_price + output_tokens * output_price

        # Aumenta el valod asociado al costo de uso de la API en esta instancia de GPT
        self.current_price += price
        return price

from .prompts.system_prompts import chat_asistant
from ....config.llm_config import ConfigGPT
from ..llm import LLM
from openai import OpenAI, AsyncOpenAI
import json


class GPT(LLM):
    """
    ## GPT
    ### Args:
    - `model`: modelo de gpt que a usar
    - `max_history_len`: largo maximo del historial que se para como input al modelo
    """

    def __init__(
        self,
        model=ConfigGPT.DEFAULT_MODEL_NAME,
        max_history_len: int = 10,
    ):
        self.client = OpenAI(api_key=ConfigGPT.OPENAI_API_KEY)
        """Cliente secuencial de GPT"""
        self.asyncclient = AsyncOpenAI(api_key=ConfigGPT.OPENAI_API_KEY)
        """Cliente asincrono de GPT"""
        self.max_len_history: int = max_history_len
        """Maxima cantidad de mensajes previos que se le pasan como input"""
        self.chat_history: list[list[dict[str, str]]] = []
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

    async def async_user_query(self, query: str) -> str:
        completion = await self.asyncclient.chat.completions.create(
            model=self.model,
            messages=self.get_messages_user_query(query),
        )
        return self.get_response_from_completion(completion)

    def user_query(self, query: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.get_messages_user_query(query),
        )
        return self.get_response_from_completion(completion)

    def get_messages_user_query(self, query: str) -> list[str]:
        """ """
        system_message: str = chat_asistant
        user_message: dict[str, str] = {"role": "user", "content": query}
        self.chat_history.append([])
        self.chat_history[-1].append(user_message)

        messages: list[dict[str, str]] = [
            {"role": "system", "content": system_message}
        ] + [
            message
            for messages in self.chat_history[-self.max_len_history :]
            for message in messages
        ]

        return messages

    def get_response_from_completion(self, completion) -> str:
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

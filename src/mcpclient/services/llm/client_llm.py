from .llm import LLM
from .models.openai_service.gpt import GPT
from typing import Generator
from .steps.step import Step


class Chat:
    def __init__(
        self,
        name="openai",
        model="gpt4o-mini",
        len_context: int = 10,
        history: list = [],
        id: str | None = None,
    ):
        self.id = id
        self.llm: LLM = GPT(max_history_len=len_context)

    def __call__(self, query: str) -> Generator[Step]:
        return self.llm(query=query)

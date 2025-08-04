from collections.abc import Generator
from ...mcp_manager.client import ClientManagerMCP
from abc import ABC, abstractmethod


class LLM(ABC):
    """Abstract class for Language Model (LLM) services."""

    def __init__(self):
        self.client_manager_mcp: ClientManagerMCP = ClientManagerMCP()
        self.current_language: str = "English"

    @abstractmethod
    def preprocess_query(self, query: str) -> dict:
        """Preprocess the query to extract language and query parts."""
        pass

    @abstractmethod
    def append_chat_history(self):
        """Append the current query to the chat history."""
        pass

    @abstractmethod
    def select_prompts(self, query: str) -> str:
        """Select prompts based on the query."""
        pass

    @abstractmethod
    def select_service(
        self, query: str, extra_messages: list[dict[str, str]] = []
    ) -> str:
        """Select services based on the query and extra messages."""
        pass

    @abstractmethod
    def simple_query(
        self,
        query: str,
        use_services_contex: bool = False,
        extra_messages: list[dict[str, str]] = [],
    ) -> Generator[str, None]:
        """Perform a simple query and return a generator of response chunks."""
        pass

    @abstractmethod
    def final_response(
        self,
        query: str,
        data: str | dict,
        extra_messages: list[dict[str, str]] = [],
    ) -> Generator[str, None]:
        """Generate the final response based on the query and data."""
        pass

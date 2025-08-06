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
        """
        Selects the most relevant services for the given query context by leveraging the available services exposed by each server.
        Args:
            query (str): The user's query for which relevant services need to be selected.
            extra_messages (list[dict[str, str]], optional): Additional messages to include in the context. Defaults to an empty list.
        Returns:
            str: The result of the completion call, typically a JSON-formatted string indicating the selected services.
        Description:
            This function gathers all available services from the client manager, constructs a prompt combining the user's query and the list of services,
            and then calls the completion endpoint to determine which services are most useful for the given context.
        """
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

import os
import json

ROOT_PATH = "http://127.0.0.1/fastchatdb"

SAVE_HISTORY = "/history/save"
SAVE_MESSAGE = "/message/save"

LOAD_HISTORY = "/history/load"


class ClientDB:
    def __init__(
        self,
        config_file: str = "fastchat.config.json",
    ):
        self.save_history_body: dict = {}
        self.save_message_body: dict = {}
        self.load_history_query: dict = {}

        self.__load_config(config_file=config_file)

    def __load_config(self, config_file: str):
        save_history: str = SAVE_HISTORY
        load_history: str = LOAD_HISTORY
        save_message: str = SAVE_MESSAGE

        if os.path.exists(config_file):
            with open(config_file, "r"):
                config: dict = json.load(config_file)

            db_connection: dict = config.get("db_conection")
            if db_connection is not None:
                root_path = db_connection.get("root_path") or ROOT_PATH
                endpoints: dict = db_connection.get("endpoints")
                if endpoints is not None:

                    save_history_endpoint: dict = endpoints.get("save_history")
                    if save_history_endpoint is not None:
                        save_history = save_history_endpoint.get("path") or save_history
                        self.save_history_body = save_history_endpoint.get("body") or {}

                    load_history_endpoint: dict = endpoints.get("load_history")
                    if load_history_endpoint is not None:
                        load_history = load_history_endpoint.get("path") or load_history
                        self.load_history_query = (
                            load_history_endpoint.get("query") or {}
                        )

                    save_message_endpoint: dict = endpoints.get("save_message")
                    if save_message_endpoint is not None:
                        save_message = save_message_endpoint.get("path") or save_message
                        self.save_message_body = save_message_endpoint.get("body") or {}

        self.set_database_endpoints_path(
            root_path=root_path,
            save_history=save_history,
            load_history=load_history,
            save_message=save_message,
        )

    def set_database_endpoints_path(
        self,
        root_path: str = ROOT_PATH,
        save_history: str = SAVE_HISTORY,
        load_history: str = LOAD_HISTORY,
        save_message: str = SAVE_MESSAGE,
    ):
        self.save_history_path: str = os.path.join(root_path, save_history)
        self.load_history_path: str = os.path.join(root_path, load_history)
        self.save_messsage_path: str = os.path.join(root_path, save_message)

    async def save_history(self, chat_id: str, history: list[dict]) -> bool:
        # Peticion post a la base de datos que guarda
        response: dict = {}
        return response["status"] == "success"

    async def load_history(self, chat_id: str) -> bool:
        response: dict = {}
        return response["status"] == "success"

    async def save_message(self, chat_id: str, message_id: str, message: dict) -> bool:
        response: dict = {}
        return response["status"] == "success"

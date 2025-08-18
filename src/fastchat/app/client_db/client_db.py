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
                endpoints: dict = db_connection.get("endpoints")
                if endpoints is not None:
                    if (
                        "save_history" in endpoints
                        and "path" in endpoints["save_history"]
                    ):
                        save_history = endpoints["save_history"]["path"]
                    if (
                        "load_history" in endpoints
                        and "path" in endpoints["load_history"]
                    ):
                        load_history = endpoints["load_history"]["path"]
                    if (
                        "save_message" in endpoints
                        and "path" in endpoints["save_message"]
                    ):
                        save_message = endpoints["save_message"]["path"]

        self.set_database_endpoints_path(
            save_history=save_history,
            load_history=load_history,
            save_message=save_message,
        )

    def set_database_endpoints_path(
        self,
        root_path: str,
        save_history: str = SAVE_HISTORY,
        load_history: str = LOAD_HISTORY,
        save_message: str = SAVE_MESSAGE,
    ):
        self.save_history_path: str = os.path.join(root_path, save_history)
        self.load_history_path: str = os.path.join(root_path, load_history)
        self.save_messsage_path: str = os.path.join(root_path, save_message)

    def save_history(self) -> bool:
        response: dict = {}
        return response["status"] == "success"

    def load_history(self) -> bool:
        response: dict = {}
        return response["status"] == "success"

    def save_message(self) -> bool:
        response: dict = {}
        return response["status"] == "success"

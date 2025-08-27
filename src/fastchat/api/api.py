from dotenv import load_dotenv

load_dotenv()


from fastapi import FastAPI
from fastauth import set_auth, TokenRouter
from fastapi.responses import RedirectResponse
from .settings import FastappSettings
from .routes.chat import router as chat_router
from ..config.llm_config import ConfigLLM
from ..utils.clear_console import clear_console


class FastApp:
    def __init__(
        self,
        extra_reponse_system_prompts: list[str] = [],
        extra_selection_system_prompts: list[str] = [],
        len_context: int = ConfigLLM.DEFAULT_HISTORY_LEN,
        token_router: TokenRouter = TokenRouter(),
    ):
        FastappSettings.update(
            extra_reponse_system_prompts,
            extra_selection_system_prompts,
            len_context,
        )
        self.token_router = token_router

    @property
    def app(self) -> FastAPI:
        app: FastAPI = FastAPI()

        @app.get("/")
        async def root():
            return RedirectResponse(url="/docs")

        @app.get("/healt")
        async def healt():
            return {"status": "healtly"}

        app.include_router(chat_router)
        set_auth(app, [self.token_router.route])
        return app

    def run(self, host: str, port: int):
        clear_console()
        pass

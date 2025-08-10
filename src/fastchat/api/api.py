from dotenv import load_dotenv

load_dotenv()


from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from .routes.chat import router as chat_router


class FastApp:
    def __init__(
        self,
        middleware=None,
    ):
        pass

    @property
    def app(self) -> FastAPI:
        app: FastAPI = FastAPI()
        # app.openapi = lambda: CustomOpenAPI(app)()
        # app.add_middleware(AccessTokenMiddleware)

        @app.get("/")
        async def root():
            return RedirectResponse(url="/docs")

        @app.get("/healt")
        async def healt():
            return {"status": "healtly"}

        app.include_router(chat_router)
        return app

    def run(self, host: str, port: int):
        pass


app: FastAPI = FastApp().app

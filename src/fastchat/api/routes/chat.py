from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ...app.chat.features.llm_provider import LLMProvider

# from ...app.chat.features.step import Step
from ...app.chat.chat import Fastchat
from ...config.llm_config import ConfigGPT, ConfigLLM
from ...app.environment import Environment
from ..settings import FastappSettings

router = APIRouter(prefix="/chat", tags=["chating"])


@router.websocket("/ws")
async def websocket_chat(
    websocket: WebSocket,
    chat_id: str = None,
    model: str = ConfigGPT.DEFAULT_MODEL_NAME,
    llm_provider: str = ConfigLLM.DEFAULT_PROVIDER.value,
):
    await websocket.accept()
    llm_provider = LLMProvider(llm_provider)

    history: list = get_history(chat_id)

    chat = Fastchat(
        id=chat_id,
        model=model,
        llm_provider=llm_provider,
        extra_reponse_system_prompts=FastappSettings.extra_reponse_system_prompts,
        extra_selection_system_prompts=FastappSettings.extra_selection_system_prompts,
        len_context=FastappSettings.len_context,
        history=history,
    )

    await chat.initialize(print_logo=False)

    try:
        while True:
            # Espera mensaje del usuario, típicamente texto (puedes cambiarlo si envías JSON)
            query = await websocket.receive_text()
            response = chat(query)

            # Enviar respuesta al cliente (puede ser texto o JSON)
            async for step in response:
                await websocket.send_json(step.json)
            await websocket.send_text("--next")

    except WebSocketDisconnect:
        # Cierra conexión limpia si el cliente se desconecta
        pass


def get_history(chat_id: str) -> list:
    """Select history from database using chat_id"""
    return []

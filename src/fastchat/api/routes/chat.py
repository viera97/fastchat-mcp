from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ...app.chat.features.llm_provider import LLMProvider

# from ...app.chat.features.step import Step
from ...app.chat.chat import Chat
from ...config.llm_config import ConfigGPT, ConfigLLM

router = APIRouter(prefix="/chat", tags=["chating"])


@router.websocket("/ws")
async def websocket_chat(
    websocket: WebSocket,
    chat_id: str = None,
    model: str = ConfigGPT.DEFAULT_MODEL_NAME,
    llm_provider: LLMProvider = ConfigLLM.DEFAULT_PROVIDER,
    len_context: int = ConfigLLM.DEFAULT_HISTORY_LEN,
):
    await websocket.accept()
    history = []
    chat = Chat(
        id=chat_id,
        model=model,
        llm_provider=llm_provider,
        len_context=len_context,
        history=history,
    )

    try:
        while True:
            # Espera mensaje del usuario, típicamente texto (puedes cambiarlo si envías JSON)
            query = await websocket.receive_text()
            response = chat(query)
            # Enviar respuesta al cliente (puede ser texto o JSON)
            for step in response:
                await websocket.send_json(step.json)
            # Puedes agregar respuesta a history si tu lógica lo requiere
            history.append({"role": "user", "content": query})
            history.append({"role": "assistant", "content": str(response)})
    except WebSocketDisconnect:
        # Cierra conexión limpia si el cliente se desconecta
        pass

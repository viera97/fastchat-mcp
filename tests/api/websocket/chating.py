import asyncio
import websockets


class WebsocketClient:
    def __init__(self):
        pass

    def open_chat(self, uri):
        asyncio.run(self.open_chat(uri))

    async def __open_chat(self, uri):
        async with websockets.connect(uri) as websocket:
            while True:
                mensaje = input("Tú: ")  # Leer mensaje a enviar desde consola
                await websocket.send(mensaje)  # Enviar mensaje al servidor

                # Esperar y recibir una o varias respuestas JSON en cadena (puedes adaptarlo según tu protocolo)
                try:
                    while True:
                        respuesta = await websocket.recv()
                        print("Servidor:", respuesta)  # Mostrar respuesta recibida
                except asyncio.TimeoutError:
                    pass


if __name__ == "__main__":
    uri_ws = "ws://localhost:8000/chat/ws?chat_id=tu_id"  # Cambia la URI y parámetros según tu servidor
    WebsocketClient().open_chat(uri_ws)

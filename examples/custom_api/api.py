from fastchat.api import FastApp
from fastauth import TokenRouter


class CustomTokenRouter(TokenRouter):
    def __generate_access_token(self, client_id):
        # Implement your custom logic here
        return super().__generate_access_token(client_id)

    def __refresh_access_token(self, refresh_token):
        # Implement your custom logic here
        return super().__refresh_access_token(refresh_token)


fastapp = FastApp(token_router=CustomTokenRouter())

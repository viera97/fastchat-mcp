import uuid
from pydantic import BaseModel


class MessagesSet(BaseModel):
    messages: list[dict]
    id: str = uuid.uuid4()

from pydantic import BaseModel

class PlayListInfo(BaseModel):
    id: str
    name: str
    is_default: bool
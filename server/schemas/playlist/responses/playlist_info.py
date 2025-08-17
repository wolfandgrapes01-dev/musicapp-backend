from pydantic import BaseModel

class PlayListInfo(BaseModel):
    id: str
    name: str
    is_default: bool
    # Enable Pydantic to create models from ORM objects
    # class Config:
    #     from_attributes = True
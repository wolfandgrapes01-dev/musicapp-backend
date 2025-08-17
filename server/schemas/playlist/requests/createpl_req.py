from pydantic import BaseModel

class CreatplReq(BaseModel):
    id:str
    name:str
from pydantic import BaseModel

class CreatPlayListReq(BaseModel):
    id:str
    name:str
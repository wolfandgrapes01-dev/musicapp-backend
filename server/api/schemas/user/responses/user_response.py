from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserResponse(BaseModel):
    name: str
    e164_phone_num: str
    dial_code: int
    national_phone_num: int
    country_name: str

    class Config:
        from_attributes = True
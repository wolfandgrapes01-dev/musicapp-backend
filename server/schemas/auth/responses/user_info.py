from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserInfo(BaseModel):
    name: str
    e164_phone_num: str
    national_phone_num: int
    dial_code: int
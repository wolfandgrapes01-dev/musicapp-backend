from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class LoginReq(BaseModel):
    e164_phone_num: str
    password: str
    last_login_at: Optional[datetime] = None
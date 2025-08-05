from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserLoginRequest(BaseModel):
    password: str
    e164_phone_num: str
    dial_code: int
    national_phone_num: int
    last_login_at: Optional[datetime] = None
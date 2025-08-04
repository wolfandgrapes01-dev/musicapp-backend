from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserSignUpRequest(BaseModel):
    name: str
    password: str
    e164_phone_num: str
    dial_code: int
    national_phone_num: int
    country_name: str
    last_login_at: Optional[datetime] = None
    create_at: Optional[datetime] = None
    update_at: Optional[datetime] = None
    is_deleted: bool = False
    delete_at: Optional[datetime] = None
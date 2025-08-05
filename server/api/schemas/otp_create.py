from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class OtpCreate(BaseModel):
    e164_phone_num: str
    otp_code: Optional[str] = None
    send_at: Optional[datetime] = None
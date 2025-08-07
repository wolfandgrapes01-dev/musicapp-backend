from pydantic import BaseModel
from schemas.auth.responses.user_info import UserInfo

class AuthRes(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserInfo
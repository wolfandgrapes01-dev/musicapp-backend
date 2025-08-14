from pydantic import BaseModel
from schemas.auth.responses.user_info import UserInfo
from schemas.auth.responses.playlist_info import PlayListInfo

class AuthRes(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserInfo
    playlist: PlayListInfo
from pydantic import BaseModel
from schemas.auth.responses.user_info import UserInfo
from schemas.auth.responses.playlist_info import PlayListInfo
from schemas.song.responses.song_info import SongInfo

class SongRes(BaseModel):
    song: SongInfo
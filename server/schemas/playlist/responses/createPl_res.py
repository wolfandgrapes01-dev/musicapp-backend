from pydantic import BaseModel
from schemas.playlist.responses.playlist_info import PlayListInfo

class CreatePlRes(BaseModel):
    playlists: PlayListInfo
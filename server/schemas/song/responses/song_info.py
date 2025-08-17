from datetime import date
from pydantic import BaseModel


class SongInfo(BaseModel):
    song_title: str
    artist_name: str
    album_name: str
    duration_ms = int
    release_year = int
    release_date = date
    track_number = int
    disk_number = int
from datetime import date
from pydantic import BaseModel


class UploadReq(BaseModel):
    song_title = str
    duration_ms = int
    release_year = int
    release_date = date
    track_number = int
    disk_number = int
    audio_url = str
    cover_url = str
    is_explicit = bool
    is_single = bool
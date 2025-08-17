from datetime import datetime, timezone
import uuid
from models.song import Song
from repositories.song_repo import insert_song
from schemas.song.requests.upload_req import UploadReq
from sqlalchemy.orm import Session

from schemas.song.responses.song_info import SongInfo
from schemas.song.responses.song_res import SongRes


def upload_song_service(upload_info: UploadReq, db: Session) -> SongInfo:
    # Get the current UTC time
    current_time = datetime.now(timezone.utc)

    # TODO: the record data should be created in api server
    song_record = Song(
        id = str(uuid.uuid4()),
        song_title = upload_info.song_title,
        duration_ms = upload_info.duration_ms,
        release_year = upload_info.release_year,
        release_date = upload_info.release_date,
        track_number = upload_info.track_number,
        disk_number = upload_info.disk_number,
        audio_url = upload_info.audio_url,
        cover_url = upload_info.cover_url,
        is_explicit = upload_info.is_explicit,
        is_single = upload_info.is_single,
        create_at = current_time,
    )

    insert_song(song_record, db)

    rst_song = SongInfo(
        song_title = song_record.song_title,
        artist_name = "",
        album_name = "",
        duration_ms = song_record.duration_ms,
        release_year = song_record.release_year,
        release_date = song_record.release_date,
        track_number = song_record.track_number,
        disk_number = song_record.disk_number,
    )

    return SongRes(song = rst_song)
    
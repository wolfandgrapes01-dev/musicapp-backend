from datetime import datetime, timezone
import uuid
from anyio import current_time
from fastapi import HTTPException
from models.playlist import Playlist
from models.user import User
from repositories.playlist_repo import insert_playlist
from schemas.playlist.requests.create_playlist_req import CreatPlayListReq
from sqlalchemy.orm import Session
from schemas.playlist.responses.playlist_info import PlayListInfo

def create_playlist_service(create_playlist: CreatPlayListReq, db: Session, user_id:str) -> PlayListInfo:
    # TODO: 該当するユーザーのPlaylist名の重複をチェックする
    # TODO: 重複の場合、ERROR（detail='This playlist name is already taken. Try another one.'）


    # Get the current UTC time
    current_time = datetime.now(timezone.utc)

    # Create a new playlist record(SQLAlchemy model)
    playlist_record = Playlist(
        id = str(uuid.uuid4()),
        name = create_playlist.name,
        user_id = user_id,
        create_at = current_time,
        update_at = current_time,
        is_default = False,
    )

    # Insert (SQLAlchemy model)
    insert_playlist(playlist_record, db)

    # return playlist
    return PlayListInfo(id = playlist_record.id, name = playlist_record.name, is_default = playlist_record.is_deleted)




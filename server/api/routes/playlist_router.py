from fastapi import Depends, HTTPException
from fastapi import APIRouter
from database import get_db
from middleware.auth_middleware import auth_middleware
from models.user import User
from schemas.auth.responses.playlist_info import PlayListInfo
from sqlalchemy.orm import Session
from schemas.playlist.requests.create_playlist_req import CreatPlayListReq
from services.playlist_service import create_playlist_service

router = APIRouter()

@router.post('/create', status_code=201, response_model=PlayListInfo)
def create_playlist(request: CreatPlayListReq, db: Session=Depends(get_db), user_dict = Depends(auth_middleware)):
    
    # TODO: add document comment
    return create_playlist_service(request,db,user_dict)


# TODO: PlaylistのRename

# TODO: Playlistに曲の追加（マルチ追加可能）

# TODO: Playlistの曲を削除（物理削除、マルチ削除可能）

# TODO: Playlistの削除（物理削除）
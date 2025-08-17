from fastapi import Depends
from fastapi import APIRouter
from database import get_db
from schemas.auth.responses.playlist_info import PlayListInfo
from sqlalchemy.orm import Session
from schemas.playlist.requests.create_playlist_req import CreatPlayListReq
from services.playlist_service import create_playlist_service

router = APIRouter()

@router.post('/createPlaylist', status_code=201, response_model=PlayListInfo)
def create_playlist(request: CreatPlayListReq, db: Session=Depends(get_db)):
    
    return create_playlist_service(request,db)
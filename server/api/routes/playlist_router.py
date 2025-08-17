from fastapi import Depends
from fastapi import APIRouter
from database import get_db
from schemas.playlist.requests.createpl_req import CreatplReq
from schemas.playlist.responses.createPl_res import CreatePlRes
from sqlalchemy.orm import Session
from services.playlist_service import create_playlist_service

router = APIRouter()

@router.post('/createPlaylist', status_code=201, response_model=CreatePlRes)
def create_playlist(request: CreatplReq, db: Session=Depends(get_db)):
    
    return create_playlist_service(request,db)
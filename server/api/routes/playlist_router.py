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

@router.post('/createplaylist', status_code=201, response_model=PlayListInfo)
def create_playlist(request: CreatPlayListReq, db: Session=Depends(get_db), user_dict = Depends(auth_middleware)):
    rst_user_info = db.query(User).filter(User.id == user_dict['uid']).first()

    if not rst_user_info:
        # ERR_004
        raise HTTPException(status_code=404, detail='User not found!')
    
    return create_playlist_service(request,db)
from fastapi import APIRouter, Depends

from database import get_db
from schemas.song.requests.upload_req import UploadReq
from schemas.song.responses.song_info import SongInfo
from sqlalchemy.orm import Session

from schemas.song.responses.song_res import SongRes
from services.song_service import upload_song_service


router = APIRouter()

@router.post('/upload', status_code=201, response_model=SongRes)
def upload_song(request: UploadReq, db: Session = Depends(get_db)):
    return upload_song_service(request, db)
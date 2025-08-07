from datetime import datetime, timezone
import bcrypt
from fastapi import Depends, HTTPException, Header
from models.user import User
from schemas.auth.requests.login_req import LoginReq
from schemas.auth.requests.signup_req import SignUpReq
from schemas.auth.responses.auth_res import AuthRes
from middleware.auth_middleware import auth_middleware
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
import jwt

from services.auth_service import login_user_service, signup_user_service

router = APIRouter()

@router.post('/signup', status_code=201, response_model=AuthRes)
def signup_user(request: SignUpReq, db: Session = Depends(get_db)):
    """
    User signup endpoint:
    - Accepts user registration data (name, phone number, password, etc.)
    - Hashes the password securely
    - Saves the user to the database
    - Returns a clean, non-sensitive response model
    """

    return signup_user_service(request, db)

    
@router.post('/login', status_code=200, response_model=AuthRes)
def login_user(request: LoginReq, db: Session = Depends(get_db)):
    
    return login_user_service(request, db)

@router.get('/')
def current_user_data(db: Session=Depends(get_db), user_dict = Depends(auth_middleware)):
    rst_user_info = db.query(User).filter(User.id == user_dict['uid']).first()

    if not rst_user_info:
        raise HTTPException(status_code=404, detail='User not found!')
    
    return rst_user_info
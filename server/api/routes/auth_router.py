from datetime import datetime, timezone
import uuid
import bcrypt
from fastapi import Depends, HTTPException, Header
from api.schemas.otp_create import OtpCreate
from api.schemas.signup_request import SignupRequest
from api.schemas.user_create import UserCreate, UserResponse
from middleware.auth_middleware import auth_middleware
from models.otp import Otp
from models.user import User
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
from api.schemas.user_login import UserLogin
import jwt

router = APIRouter()

@router.post('/signup', status_code=201, response_model=UserResponse)
def signup_user(request: SignupRequest, db: Session = Depends(get_db)):
    user = request.user

    # check e164_phone_num in otpTb
    rst_otp_info = db.query(Otp).filter(Otp.e164_phone_num == user.e164_phone_num).first()
    if not rst_otp_info:
        # ERR_004
       raise HTTPException(status_code=404, detail='something is wrong...')
    else:
        # check exp_at in otpTb
        if otp.send_at <= rst_otp_info.exp_at:
            # create user info
            hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
            current_time = datetime.now(timezone.utc)

            insert_user_info = User(
                id = str(uuid.uuid4()),
                name = user.name,
                password = hashed_pw,
                e164_phone_num = user.e164_phone_num,
                dial_code = user.dial_code,
                national_phone_num = user.national_phone_num,
                country_name = user.country_name,
                last_login_at = current_time,
                create_at = current_time,
            )
            db.add(insert_user_info)
            # delete otp info in otpTb
            db.delete(rst_otp_info)

            db.commit()
            db.refresh(insert_user_info)

            new_user = UserResponse(
                name = insert_user_info.name,
                e164_phone_num = insert_user_info.e164_phone_num,
                dial_code = insert_user_info.dial_code,
                national_phone_num = insert_user_info.national_phone_num,
                country_name = insert_user_info.country_name,
                is_deleted = insert_user_info.is_deleted,
            )
            return new_user

@router.post('/login', status_code=200)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # check if a user with same phone number already exist
    rst_user_info = db.query(User).filter(User.e164_phone_num == user.e164_phone_num).first()
    if not rst_user_info:
        # ERR_002
        raise HTTPException(status_code=404, detail='User with this phone number does not exists!')
    
    # password matching or not
    is_match = bcrypt.checkpw(user.password.encode(), rst_user_info.password)
    if not is_match:
        # ERR_003
        raise HTTPException(status_code=401, detail='Icorrect password')

    token = jwt.encode({'id': rst_user_info.id}, 'password_key')

    # update last login time
    current_time = datetime.now(timezone.utc)
    rst_user_info.last_login_at = current_time

    db.commit()
    db.refresh(rst_user_info)

    return {'token': token, 'user_info': rst_user_info}

@router.get('/')
def current_user_data(db: Session=Depends(get_db), user_dict = Depends(auth_middleware)):
    rst_user_info = db.query(User).filter(User.id == user_dict['uid']).first()

    if not rst_user_info:
        raise HTTPException(status_code=404, detail='User not found!')
    
    return rst_user_info
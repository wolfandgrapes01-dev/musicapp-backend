from datetime import datetime, timezone
import uuid
import bcrypt
from fastapi import HTTPException
import jwt
from models.user import User
from sqlalchemy.orm import Session
from schemas.auth.requests.login_req import LoginReq
from schemas.auth.requests.signup_req import SignUpReq
from schemas.auth.responses.auth_res import AuthRes
from schemas.auth.responses.user_info import UserInfo


def signup_user_service(signup_info: SignUpReq, db: Session) -> AuthRes:
    # check if a user with same phone number already exist
    rst_user = db.query(User).filter(User.e164_phone_num == signup_info.e164_phone_num).first()
    if rst_user is not None:
        # ERR_001
        raise HTTPException(status_code=409, detail='Phone number already registered!')

    # Hash the user's password
    hashed_pw = bcrypt.hashpw(signup_info.password.encode(), bcrypt.gensalt())

    # Get the current UTC time
    current_time = datetime.now(timezone.utc)

    # Create a new user record (SQLAlchemy model)
    user_record = User(
        id = str(uuid.uuid4()),
        name = signup_info.name,
        password = hashed_pw,
        e164_phone_num = signup_info.e164_phone_num,
        # TODO: Need a master table for country codes
        dial_code = signup_info.dial_code,
        national_phone_num = signup_info.national_phone_num,
        # TODO: Need a master table for country codes
        country_name = signup_info.country_name,
        last_login_at = current_time,
        create_at = current_time,
    )

    # Insert
    db.add(user_record)

    # Commit
    db.commit()

    # Refresh the object to load any default values set by the database
    db.refresh(user_record)

    # Construct the response model (Pydantic) with only safe, public fields
    new_user = UserInfo(
        name = user_record.name,
        e164_phone_num = user_record.e164_phone_num,
        dial_code = user_record.dial_code,
        national_phone_num = user_record.national_phone_num,
    )

    token = jwt.encode({'phone_num': new_user.e164_phone_num}, 'password_key')
    return AuthRes(access_token = token, user = new_user)

def login_user_service(login_info: LoginReq, db: Session) -> AuthRes:
    # check if a user with same phone number already exist
    user_record = db.query(User).filter(User.e164_phone_num == login_info.e164_phone_num).first()
    if not user_record:
        # ERR_002
        raise HTTPException(status_code=404, detail='User with this phone number does not exists!')
    
    # password matching or not
    is_match = bcrypt.checkpw(login_info.password.encode(), user_record.password)
    if not is_match:
        # ERR_003
        raise HTTPException(status_code=401, detail='Icorrect password')


    # update last login time
    current_time = datetime.now(timezone.utc)
    user_record.last_login_at = current_time

    db.commit()
    db.refresh(user_record)

    rst_user = UserInfo(
        name = user_record.name,
        e164_phone_num = user_record.e164_phone_num,
        dial_code = user_record.dial_code,
        national_phone_num = user_record.national_phone_num,
    )

    token = jwt.encode({'phone_num': rst_user.e164_phone_num}, 'password_key')
    return AuthRes(access_token = token, user = rst_user)
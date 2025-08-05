from fastapi import Depends, HTTPException
from api.schemas.otp_create import OtpCreate
from models.otp import Otp
from models.user import User
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session
from services.otp_service import check_rate_limit, create_new_otp

router = APIRouter()

@router.post('/sendotp', status_code=202)
def send_otp(otp: OtpCreate, db: Session = Depends(get_db)):
    rst_user_info = db.query(User).filter(User.e164_phone_num == otp.e164_phone_num).first()
    if rst_user_info:
        # ERR_001
        raise HTTPException(status_code=400, detail='User with this same phone number already exists!')

    # create otp
    otp_detail = create_new_otp()

    # check create_at in otpTb(rate limiting)
    existed_otp_info = db.query(Otp).filter(Otp.e164_phone_num == otp.e164_phone_num).first()
    if existed_otp_info:
        is_limiting = check_rate_limit(otp.send_at, existed_otp_info.exp_at)
        if (is_limiting):
            # ERR_002
            raise HTTPException(status_code=429, detail='Too many requests, please wait before requesting another OTP.')
        else: 
            # update otp code & create_at & exp_at
            existed_otp_info.otp_code = otp_detail.otp_code
            existed_otp_info.create_at = otp_detail.create_time
            existed_otp_info.exp_at = otp_detail.expiration_time

            db.commit()
            db.refresh(existed_otp_info)

            # send otp
            # send_otp_sms(existed_otp_info.e164_phone_num, sendMsg)
            return {'e164_phone_num': existed_otp_info.e164_phone_num, 'exp_at': existed_otp_info.exp_at}
    else:
        # insert into otpTb
        insert_otp_info = Otp(
            e164_phone_num = otp.e164_phone_num,
            otp_code = otp_detail.otp_code,
            create_at = otp_detail.create_time,
            exp_at = otp_detail.expiration_time
        )
        
        # send otp
        # send_otp_sms(insert_otp_info.e164_phone_num, sendMsg)

        db.add(insert_otp_info)
        db.commit()
        db.refresh(insert_otp_info)

        return {'e164_phone_num': insert_otp_info.e164_phone_num, 'exp_at': insert_otp_info.exp_at}


# @router.post('/resendotp', status_code=202)
# def resend_otp(otp: OtpCreate, db: Session = Depends(get_db)):
#     # create otp
#     otp_detail = create_new_otp()

#     existed_otp_info = db.query(Otp).filter(Otp.e164_phone_num == otp.e164_phone_num).first()
#     # update otp code & create_at & exp_at
#     existed_otp_info.create_at = otp_detail.current_time
#     existed_otp_info.exp_at = otp_detail.expiration_time
#     existed_otp_info.otp_code = otp_detail.otp_code

#     db.commit()
#     db.refresh(existed_otp_info)

#     # send otp
#     # send_otp_sms(existed_otp_info.e164_phone_num, sendMsg)
#     return {'e164_phone_num': existed_otp_info.e164_phone_num, 'exp_at': existed_otp_info.exp_at}

from pydantic import BaseModel, model_validator

from api.schemas.otp_create import OtpCreate
from api.schemas.user_create import UserCreate

class SignupRequest(BaseModel):
    user: UserCreate
    otp: OtpCreate

    @model_validator(mode='before')
    def auto_fill_otp_phone(cls, values):
        # Automatically populate otp.e164_phone_num with user.e164_phone_num
        values['otp']['e164_phone_num'] = values['user']['e164_phone_num']
        return values
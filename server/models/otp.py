from models.base import Base

from sqlalchemy import TEXT, TIMESTAMP, VARCHAR, Column


class Otp(Base):
    __tablename__ = 'tb_002_otps'

    e164_phone_num = Column(VARCHAR(30), primary_key = True)
    otp_code = Column(VARCHAR(6))
    create_at = Column(TIMESTAMP(timezone = False))
    exp_at = Column(TIMESTAMP(timezone = False))
from sqlalchemy import BOOLEAN, NUMERIC, TEXT, TIMESTAMP, VARCHAR, Column, LargeBinary
from models.base import Base

class User(Base):
    __tablename__ = 'tb_001_users'

    id = Column(TEXT, primary_key = True)
    name = Column(VARCHAR(100), nullable = False)
    password = Column(LargeBinary, nullable = False)
    e164_phone_num = Column(VARCHAR(30), unique = True, nullable = False)
    dial_code = Column(NUMERIC(5, 0), nullable = False)
    national_phone_num = Column(NUMERIC(20, 0), nullable = False)
    country_name = Column(VARCHAR(100), nullable = False)
    last_login_at = Column(TIMESTAMP(timezone = True), nullable = False)
    create_at = Column(TIMESTAMP(timezone = True), nullable = False)
    update_at = Column(TIMESTAMP(timezone = True))
    is_deleted = Column(BOOLEAN, default=False, nullable=False)
    delete_at = Column(TIMESTAMP(timezone = True))
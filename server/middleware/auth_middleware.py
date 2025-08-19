from fastapi import Depends, HTTPException, Header
import jwt
from sqlalchemy.orm import Session
from database import get_db
from models.user import User


def auth_middleware(
    x_auth_token: str = Header(..., alias="x-auth-token"),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(x_auth_token, "password_key", algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token, authorization failed.")
    
    if not payload:
        raise HTTPException(401, 'Token verification faild, authrization')

    uid = payload.get("id")
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token payload, no user id.")

    user = db.query(User).filter(User.id == uid).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found or inactive.")

    return user
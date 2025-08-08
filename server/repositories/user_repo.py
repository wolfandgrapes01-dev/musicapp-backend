from sqlalchemy.orm import Session
from models.user import User

def insert_user(user: User, db: Session) -> User:
    # Insert
    db.add(user)

    # Commit
    db.commit()

    # Refresh the object to load any default values set by the database
    db.refresh(user)

    return user

def update_user(user: User, db: Session) -> User:
    # Commit
    db.commit()

    # Refresh the object to load any default values set by the database
    db.refresh(user)

    return user
from sqlalchemy.orm import Session
from models.playlist import Playlist

def insert_playlist(playlist:Playlist, db: Session) -> Playlist:
    # Insert
    db.add(playlist)

    #Commit
    db.commit()

    # Refresh the object to load any default values set by the database
    db.refresh(playlist)

    return playlist
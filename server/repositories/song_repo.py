from models.song import Song
from sqlalchemy.orm import Session


def insert_song(song: Song, db: Session) -> Song:
    # Insert
    db.add(song)

    #Commit
    db.commit()

    # Refresh the object to load any default values set by the database
    db.refresh(song)

    # TODO: every repo should fix return object
    return song
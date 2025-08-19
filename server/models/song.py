from sqlalchemy import BOOLEAN, DATE, INTEGER, TEXT, TIMESTAMP, VARCHAR, Column
from models.base import Base

class Song(Base):
    __tablename__ = 'tb_004_songs'

    id = Column(TEXT, primary_key = True)
    song_title = Column(VARCHAR(255), nullable = False)
    duration_ms = Column(INTEGER, nullable = False)
    release_year = Column(INTEGER, nullable = False)
    release_date = Column(DATE)
    track_number = Column(INTEGER)
    disk_number = Column(INTEGER)
    audio_url = Column(TEXT, nullable = False)
    cover_url = Column(TEXT, nullable = False)
    is_explicit = Column(BOOLEAN, default=False)
    is_single = Column(BOOLEAN)
    create_at = Column(TIMESTAMP(timezone = True), nullable = False)
    update_at = Column(TIMESTAMP(timezone = True))
    is_deleted = Column(BOOLEAN, default=False, nullable=False)
    delete_at = Column(TIMESTAMP(timezone = True))
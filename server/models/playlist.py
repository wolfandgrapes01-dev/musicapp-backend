from sqlalchemy import BOOLEAN,TEXT,TIMESTAMP,VARCHAR,Column
from models.base import Base

class Playlist(Base):
    __tablename__ = 'tb_003_playlists'

    id = Column(TEXT, primary_key = True)
    name = Column(VARCHAR(100), nullable = False)
    user_id = Column(TEXT, nullable = False)
    is_default = Column(BOOLEAN, default = False, nullable = False)
    create_at = Column(TIMESTAMP(timezone = True), nullable = False)
    update_at = Column(TIMESTAMP(timezone = True), nullable = False)
    is_deleted = Column(BOOLEAN, default = False, nullable = False)
    delete_at = Column(TIMESTAMP(timezone = True))
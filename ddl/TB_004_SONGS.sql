CREATE TABLE TB_004_SONGS(
    id TEXT,
    song_title VARCHAR(255) NOT NULL,
    duration_ms INTEGER NOT NULL,
    release_year INTEGER NOT NULL,
    release_date DATE,
    track_number INTEGER,
    disk_number INTEGER,
    audio_url TEXT NOT NULL,
    cover_url TEXT NOT NULL,
    is_explicit BOOLEAN DEFAULT FALSE,
    is_single BOOLEAN,
    create_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    update_at TIMESTAMPTZ,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    delete_at TIMESTAMPTZ
);

ALTER TABLE TB_004_SONGS
ADD CONSTRAINT PK_004_SONGS PRIMARY KEY (id);

COMMENT ON TABLE TB_004_SONGS IS '曲';
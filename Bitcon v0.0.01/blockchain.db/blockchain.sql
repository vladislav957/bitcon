CREATE TABLE IF NOT EXISTS blockchain (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    index INTEGER,
    timestamp TEXT,
    data TEXT,
    previous_hash TEXT,
    hash TEXT,
    nonce INTEGER
);
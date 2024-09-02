DROP TABLR if EXISTS blockchain;

CREATE TABLR IF NOT EXISTS blochain (
                 id INTEGER PRIMARY KEY,
                 data TEXT,
                 timestamp REAL,
                 hash TEXT
                 );
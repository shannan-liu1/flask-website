DROP TABLE IF EXISTS messages;

CREATE TABLE IF NOT EXISTS messages(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  handle TEXT NOT NULL,
  message TEXT NOT NULL
);

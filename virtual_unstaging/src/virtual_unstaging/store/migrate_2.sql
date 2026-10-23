-- Schema version 2: the zoom judge (design/defect_detectors.md: The zoom judge). Added tables only.

CREATE TABLE zoom_judgment (
  zoom_judgment_id INTEGER PRIMARY KEY,
  attempt_id       INTEGER NOT NULL REFERENCES attempt,
  judge_model_id   INTEGER NOT NULL REFERENCES model,
  tool_run_id      INTEGER NOT NULL REFERENCES tool_run,   -- the structure map the places came from
  request_sha256   TEXT NOT NULL,
  raw_response     TEXT NOT NULL,
  parse_error      TEXT,
  wall_seconds     REAL NOT NULL,
  created_at       TEXT NOT NULL
);

CREATE TABLE zoom (
  zoom_judgment_id INTEGER NOT NULL REFERENCES zoom_judgment,
  n                INTEGER NOT NULL CHECK (n >= 1),
  place            TEXT NOT NULL CHECK (place IN ('outside','inside')),
  x0 REAL NOT NULL, y0 REAL NOT NULL, x1 REAL NOT NULL, y1 REAL NOT NULL,
  image_sha256     TEXT NOT NULL REFERENCES image,
  severity         TEXT CHECK (severity IN ('none','minor','blocking')),
  comment          TEXT,
  PRIMARY KEY (zoom_judgment_id, n),
  CHECK (0 <= x0 AND x0 < x1 AND x1 <= 1 AND 0 <= y0 AND y0 < y1 AND y1 <= 1)
);

CREATE TABLE zoom_answer (
  zoom_judgment_id INTEGER NOT NULL,
  n                INTEGER NOT NULL,
  answer           TEXT NOT NULL,
  PRIMARY KEY (zoom_judgment_id, n, answer),
  FOREIGN KEY (zoom_judgment_id, n) REFERENCES zoom (zoom_judgment_id, n)
);

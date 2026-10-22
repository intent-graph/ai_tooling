-- virtual_unstaging project database. The authoritative schema; design/data_model.md explains it.
-- Portable SQL (SQLite now, Postgres at the growth horizon): COALESCE, COUNT(*) FILTER, no sum over booleans.
-- Append-only: attempt, tool_run, judgment, finding, move, review, preference. State: optimization, delivery.

-- Reference data, loaded from the package files by content hash -----------------------------------------------

CREATE TABLE defect_type (
  code        TEXT PRIMARY KEY,
  label       TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE model (
  model_id INTEGER PRIMARY KEY,
  role     TEXT NOT NULL CHECK (role IN ('generator','judge','tool','reviewer','rewriter')),
  name     TEXT NOT NULL,
  revision TEXT NOT NULL,
  UNIQUE (role, name, revision)
);

CREATE TABLE instruction_set (
  instruction_set_id INTEGER PRIMARY KEY,
  role          TEXT NOT NULL CHECK (role IN ('generator','judge','reviewer','rewriter')),
  target_model  TEXT NOT NULL,
  layer         TEXT NOT NULL CHECK (layer IN ('base','project','photo')),
  layered_on_id INTEGER REFERENCES instruction_set,
  previous_id   INTEGER REFERENCES instruction_set,
  body          TEXT NOT NULL,
  sha256        TEXT NOT NULL UNIQUE,
  created_at    TEXT NOT NULL,
  CHECK ((layer = 'base') = (layered_on_id IS NULL))
);

CREATE TABLE dimension (
  dimension_id    INTEGER PRIMARY KEY,
  key             TEXT NOT NULL,
  input           TEXT NOT NULL CHECK (input IN ('instructions','clues','guides','settings')),
  realizer        TEXT NOT NULL CHECK (realizer IN
                    ('text_slot','reference_count','mask_dilation','guide_toggle','setting')),
  slot            TEXT,
  role            TEXT,
  setting         TEXT,
  layer           TEXT NOT NULL CHECK (layer IN ('base','project','photo')),
  origin          TEXT NOT NULL CHECK (origin IN ('preloaded','judge_designed')),
  default_ordinal INTEGER NOT NULL,
  probe_cost      REAL NOT NULL DEFAULT 0,
  rationale       TEXT,
  created_by_judgment_id INTEGER,              -- REFERENCES judgment, judge-designed only (slice 2)
  sha256          TEXT NOT NULL UNIQUE,
  CHECK ((realizer = 'text_slot') = (slot IS NOT NULL)),
  CHECK ((realizer = 'guide_toggle') = (role IS NOT NULL)),
  CHECK ((realizer = 'setting') = (setting IS NOT NULL)),
  CHECK ((origin = 'judge_designed') = (created_by_judgment_id IS NOT NULL))
);

CREATE TABLE dimension_level (
  dimension_id     INTEGER NOT NULL REFERENCES dimension,
  ordinal          INTEGER NOT NULL CHECK (ordinal >= 0),
  label            TEXT NOT NULL,
  realization_json TEXT NOT NULL,
  PRIMARY KEY (dimension_id, ordinal),
  UNIQUE (dimension_id, label)
);

CREATE TABLE dimension_target (
  dimension_id INTEGER NOT NULL REFERENCES dimension,
  defect_code  TEXT    NOT NULL REFERENCES defect_type,
  PRIMARY KEY (dimension_id, defect_code)
);

CREATE TABLE registry_release (
  registry_release_id INTEGER PRIMARY KEY,
  sha256     TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL
);

CREATE TABLE release_dimension (
  registry_release_id INTEGER NOT NULL REFERENCES registry_release,
  dimension_id        INTEGER NOT NULL REFERENCES dimension,
  position            INTEGER NOT NULL,         -- registry order: the order engines poll in
  PRIMARY KEY (registry_release_id, dimension_id),
  UNIQUE (registry_release_id, position)
);

CREATE TABLE defect_dimension (
  registry_release_id INTEGER NOT NULL REFERENCES registry_release,
  defect_code  TEXT    NOT NULL REFERENCES defect_type,
  dimension_id INTEGER NOT NULL REFERENCES dimension,
  direction    INTEGER NOT NULL CHECK (direction IN (-1, 1)),
  priority     INTEGER NOT NULL CHECK (priority >= 1),
  PRIMARY KEY (registry_release_id, defect_code, dimension_id)
);

-- Project content and stage 0 ---------------------------------------------------------------------------------

CREATE TABLE image (
  sha256     TEXT PRIMARY KEY,
  width      INTEGER NOT NULL CHECK (width > 0),
  height     INTEGER NOT NULL CHECK (height > 0),
  media_type TEXT NOT NULL CHECK (media_type IN ('image/png','image/jpeg'))
);

CREATE TABLE photo_group (
  group_id INTEGER PRIMARY KEY,
  name     TEXT NOT NULL UNIQUE
);

CREATE TABLE photo (
  photo_id     INTEGER PRIMARY KEY,
  group_id     INTEGER REFERENCES photo_group,
  image_sha256 TEXT NOT NULL REFERENCES image,
  source_name  TEXT NOT NULL UNIQUE,
  added_at     TEXT NOT NULL
);

CREATE TABLE rule_set (
  rule_set_id INTEGER PRIMARY KEY,
  sha256      TEXT NOT NULL UNIQUE,
  created_at  TEXT NOT NULL
);

CREATE TABLE rule_item (
  rule_item_id INTEGER PRIMARY KEY,
  rule_set_id  INTEGER NOT NULL REFERENCES rule_set,
  group_id     INTEGER REFERENCES photo_group,
  element      TEXT NOT NULL,
  disposition  TEXT NOT NULL CHECK (disposition IN ('fixed','movable')),
  note         TEXT
);
CREATE UNIQUE INDEX rule_item_key ON rule_item (rule_set_id, COALESCE(group_id, 0), element);

CREATE TABLE tool_run (
  tool_run_id   INTEGER PRIMARY KEY,
  tool          TEXT NOT NULL,
  tool_version  TEXT NOT NULL,
  model_id      INTEGER REFERENCES model,
  params_json   TEXT NOT NULL,
  cache_key     TEXT NOT NULL UNIQUE,
  measures_json TEXT,
  summary       TEXT,
  gpu_seconds   REAL NOT NULL DEFAULT 0,
  created_at    TEXT NOT NULL
);

CREATE TABLE tool_run_input (
  tool_run_id  INTEGER NOT NULL REFERENCES tool_run,
  position     INTEGER NOT NULL,
  image_sha256 TEXT NOT NULL REFERENCES image,
  PRIMARY KEY (tool_run_id, position)
);

CREATE TABLE tool_run_output (
  tool_run_id  INTEGER NOT NULL REFERENCES tool_run,
  name         TEXT NOT NULL,
  image_sha256 TEXT NOT NULL REFERENCES image,
  PRIMARY KEY (tool_run_id, name)
);

CREATE TABLE eligibility (
  photo_id      INTEGER NOT NULL REFERENCES photo,
  rule_set_id   INTEGER NOT NULL REFERENCES rule_set,
  decision      TEXT NOT NULL CHECK (decision IN ('attempt','skip')),
  reason        TEXT,
  measures_json TEXT NOT NULL,
  removal_mask_tool_run_id   INTEGER REFERENCES tool_run,
  protected_mask_tool_run_id INTEGER REFERENCES tool_run,
  decided_at    TEXT NOT NULL,
  PRIMARY KEY (photo_id, rule_set_id),
  CHECK ((decision = 'skip') = (reason IS NOT NULL)),
  CHECK (decision = 'skip' OR removal_mask_tool_run_id IS NOT NULL)
);

-- Loop 1 ------------------------------------------------------------------------------------------------------

CREATE TABLE run (
  run_id      INTEGER PRIMARY KEY,
  label       TEXT,
  engine      TEXT NOT NULL,
  engine_config_json TEXT NOT NULL,
  budget_json TEXT NOT NULL,
  minor_tolerance INTEGER NOT NULL CHECK (minor_tolerance >= 0),
  generator_model_id        INTEGER NOT NULL REFERENCES model,
  generator_capabilities_json TEXT NOT NULL,
  judge_model_id            INTEGER NOT NULL REFERENCES model,
  generator_instructions_id INTEGER NOT NULL REFERENCES instruction_set,
  judge_instructions_id     INTEGER NOT NULL REFERENCES instruction_set,
  registry_release_id       INTEGER NOT NULL REFERENCES registry_release,
  rule_set_id               INTEGER NOT NULL REFERENCES rule_set,
  code_version TEXT NOT NULL,
  started_at  TEXT NOT NULL,
  ended_at    TEXT
);

CREATE TABLE optimization (
  optimization_id INTEGER PRIMARY KEY,
  run_id      INTEGER NOT NULL REFERENCES run,
  photo_id    INTEGER NOT NULL REFERENCES photo,
  seed        INTEGER NOT NULL,
  status      TEXT NOT NULL CHECK (status IN ('running','done','failed')),
  stop_reason TEXT CHECK (stop_reason IN ('accepted','budget','no_progress','engine','error')),
  best_attempt_id INTEGER,                     -- REFERENCES attempt
  error       TEXT,
  started_at  TEXT NOT NULL,
  ended_at    TEXT,
  UNIQUE (run_id, photo_id),
  CHECK ((status = 'running') = (stop_reason IS NULL))
);

CREATE TABLE attempt (
  attempt_id      INTEGER PRIMARY KEY,
  optimization_id INTEGER NOT NULL REFERENCES optimization,
  seq             INTEGER NOT NULL CHECK (seq >= 1),
  seed            INTEGER NOT NULL,
  prompt          TEXT NOT NULL,
  settings_json   TEXT NOT NULL,
  request_sha256  TEXT NOT NULL,
  output_sha256   TEXT REFERENCES image,
  gpu_seconds     REAL NOT NULL DEFAULT 0,
  cached          INTEGER NOT NULL DEFAULT 0 CHECK (cached IN (0, 1)),
  error           TEXT,
  created_at      TEXT NOT NULL,
  UNIQUE (optimization_id, seq),
  CHECK ((output_sha256 IS NULL) = (error IS NOT NULL))
);
CREATE INDEX attempt_request ON attempt (request_sha256);

CREATE TABLE attempt_level (
  attempt_id   INTEGER NOT NULL REFERENCES attempt,
  dimension_id INTEGER NOT NULL,
  ordinal      INTEGER NOT NULL,
  PRIMARY KEY (attempt_id, dimension_id),
  FOREIGN KEY (dimension_id, ordinal) REFERENCES dimension_level (dimension_id, ordinal)
);

CREATE TABLE attempt_image (
  attempt_id   INTEGER NOT NULL REFERENCES attempt,
  position     INTEGER NOT NULL,
  role         TEXT NOT NULL CHECK (role IN
                 ('original','reference','removal_mask','protected_mask','depth','annotation')),
  image_sha256 TEXT NOT NULL REFERENCES image,
  tool_run_id  INTEGER REFERENCES tool_run,
  PRIMARY KEY (attempt_id, position)
);

-- Judging and review ------------------------------------------------------------------------------------------

CREATE TABLE judgment (
  judgment_id        INTEGER PRIMARY KEY,
  attempt_id         INTEGER NOT NULL REFERENCES attempt,
  judge_model_id     INTEGER NOT NULL REFERENCES model,
  instruction_set_id INTEGER NOT NULL REFERENCES instruction_set,
  own_verdict        TEXT CHECK (own_verdict IN ('accept','reject')),
  critique           TEXT,
  raw_response       TEXT NOT NULL,
  parse_error        TEXT,
  request_sha256     TEXT NOT NULL,
  cached             INTEGER NOT NULL DEFAULT 0 CHECK (cached IN (0, 1)),
  wall_seconds       REAL NOT NULL DEFAULT 0,
  created_at         TEXT NOT NULL
);
CREATE INDEX judgment_request ON judgment (request_sha256);

CREATE TABLE judgment_tool_run (
  judgment_id INTEGER NOT NULL REFERENCES judgment,
  tool_run_id INTEGER NOT NULL REFERENCES tool_run,
  PRIMARY KEY (judgment_id, tool_run_id)
);

CREATE TABLE review (
  review_id  INTEGER PRIMARY KEY,
  attempt_id INTEGER NOT NULL REFERENCES attempt,
  reviewer   TEXT NOT NULL,
  verdict    TEXT NOT NULL CHECK (verdict IN ('usable','unusable')),
  comment    TEXT,
  created_at TEXT NOT NULL
);

CREATE TABLE finding (
  finding_id  INTEGER PRIMARY KEY,
  judgment_id INTEGER REFERENCES judgment,
  review_id   INTEGER REFERENCES review,
  defect_code TEXT NOT NULL REFERENCES defect_type,
  severity    TEXT NOT NULL CHECK (severity IN ('minor','blocking')),
  x0 REAL, y0 REAL, x1 REAL, y1 REAL,
  comment     TEXT,
  CHECK ((judgment_id IS NULL) <> (review_id IS NULL)),
  CHECK ((x0 IS NULL) = (x1 IS NULL) AND (y0 IS NULL) = (y1 IS NULL) AND (x0 IS NULL) = (y0 IS NULL)),
  CHECK (x0 IS NULL OR (0 <= x0 AND x0 < x1 AND x1 <= 1 AND 0 <= y0 AND y0 < y1 AND y1 <= 1))
);

CREATE TABLE move (
  judgment_id    INTEGER NOT NULL REFERENCES judgment,
  rank           INTEGER NOT NULL CHECK (rank >= 1),
  dimension_id   INTEGER NOT NULL,
  to_ordinal     INTEGER NOT NULL,
  targets_defect TEXT REFERENCES defect_type,
  reason         TEXT,
  PRIMARY KEY (judgment_id, rank),
  FOREIGN KEY (dimension_id, to_ordinal) REFERENCES dimension_level (dimension_id, ordinal)
);

CREATE TABLE preference (
  preference_id INTEGER PRIMARY KEY,
  reviewer      TEXT NOT NULL,
  attempt_a     INTEGER NOT NULL REFERENCES attempt,
  attempt_b     INTEGER NOT NULL REFERENCES attempt,
  shown_left    INTEGER NOT NULL REFERENCES attempt,
  choice        TEXT NOT NULL CHECK (choice IN ('a','b','equal','both_unusable')),
  created_at    TEXT NOT NULL,
  CHECK (attempt_a <> attempt_b AND shown_left IN (attempt_a, attempt_b))
);

-- Delivery ----------------------------------------------------------------------------------------------------

CREATE TABLE delivery (
  photo_id   INTEGER PRIMARY KEY REFERENCES photo,
  outcome    TEXT NOT NULL CHECK (outcome IN ('emptied','original','excluded')),
  attempt_id INTEGER REFERENCES attempt,
  decided_by TEXT NOT NULL,
  reason     TEXT,
  decided_at TEXT NOT NULL,
  CHECK ((outcome = 'emptied') = (attempt_id IS NOT NULL))
);

-- Views -------------------------------------------------------------------------------------------------------

-- The one definition of the score (design D4): fewer blocking findings first, then fewer minor ones.
CREATE VIEW judgment_score AS
SELECT j.judgment_id, j.attempt_id,
       COUNT(f.finding_id) FILTER (WHERE f.severity = 'blocking') AS blocking,
       COUNT(f.finding_id) FILTER (WHERE f.severity = 'minor')    AS minor
FROM judgment j LEFT JOIN finding f ON f.judgment_id = j.judgment_id
WHERE j.parse_error IS NULL
GROUP BY j.judgment_id, j.attempt_id;

CREATE VIEW judgment_defect AS
SELECT judgment_id, defect_code,
       COUNT(*) FILTER (WHERE severity = 'blocking') AS blocking_count
FROM finding WHERE judgment_id IS NOT NULL
GROUP BY judgment_id, defect_code;

-- Two attempts of one optimization, same seed, one step apart on exactly one dimension; a probed before b.
CREATE VIEW neighbour_pair AS
SELECT a.attempt_id AS a_id, b.attempt_id AS b_id, la.dimension_id,
       la.ordinal AS from_ordinal, lb.ordinal AS to_ordinal
FROM attempt a
JOIN attempt b        ON b.optimization_id = a.optimization_id AND b.seq > a.seq AND b.seed = a.seed
JOIN attempt_level la ON la.attempt_id = a.attempt_id
JOIN attempt_level lb ON lb.attempt_id = b.attempt_id AND lb.dimension_id = la.dimension_id
WHERE ABS(la.ordinal - lb.ordinal) = 1
  AND NOT EXISTS (
    SELECT 1 FROM attempt_level xa JOIN attempt_level xb
      ON xb.attempt_id = b.attempt_id AND xb.dimension_id = xa.dimension_id
    WHERE xa.attempt_id = a.attempt_id AND xa.dimension_id <> la.dimension_id
      AND xa.ordinal <> xb.ordinal);

-- The knowledge base as finite differences (design D8): what one step did to each defect, per judge model.
CREATE VIEW directional_effect AS
SELECT p.dimension_id, p.from_ordinal, p.to_ordinal, d.code AS defect_code, ja.judge_model_id,
       COUNT(*) AS tried,
       COUNT(*) FILTER (WHERE da.defect_code IS NOT NULL AND db.defect_code IS NULL) AS fixed,
       COUNT(*) FILTER (WHERE da.defect_code IS NULL AND db.defect_code IS NOT NULL) AS worsened
FROM neighbour_pair p
JOIN judgment ja ON ja.attempt_id = p.a_id AND ja.parse_error IS NULL
JOIN judgment jb ON jb.attempt_id = p.b_id AND jb.parse_error IS NULL
                AND jb.judge_model_id = ja.judge_model_id AND jb.instruction_set_id = ja.instruction_set_id
CROSS JOIN defect_type d
LEFT JOIN judgment_defect da ON da.judgment_id = ja.judgment_id AND da.defect_code = d.code
LEFT JOIN judgment_defect db ON db.judgment_id = jb.judgment_id AND db.defect_code = d.code
GROUP BY p.dimension_id, p.from_ordinal, p.to_ordinal, d.code, ja.judge_model_id;

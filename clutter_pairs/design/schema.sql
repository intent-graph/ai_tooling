-- clutter_pairs — store schema (slice 1, proposal). Explained in data_model.md, beside this file.
-- SQLite now; moving to Postgres changes the ids only (INTEGER PRIMARY KEY here, an identity column there).
-- Tables are in dependency order: no forward reference.

-- === Declared files, texts, images =======================================================================

-- Every declared file as read at first use: space, model instructions, composers (with their spec renderer
-- and its version), answer schemas, reasons, targets, run configuration. The file in git is the source.
CREATE TABLE source_file (
  sha256      TEXT PRIMARY KEY CHECK (length(sha256) = 64),
  kind        TEXT NOT NULL CHECK (kind IN ('ontology', 'taxonomy', 'targets', 'instruction', 'composer',
                                            'schema', 'reasons', 'config', 'decision_rule')),
  path        TEXT NOT NULL,
  content     TEXT NOT NULL,
  first_used  TEXT NOT NULL                        -- ISO 8601 UTC
);

CREATE TABLE text_blob (
  sha256   TEXT PRIMARY KEY CHECK (length(sha256) = 64),
  content  TEXT NOT NULL
);

CREATE TABLE image (
  sha256      TEXT PRIMARY KEY CHECK (length(sha256) = 64),
  media_type  TEXT NOT NULL CHECK (media_type IN ('image/png', 'image/jpeg')),
  width       INTEGER NOT NULL CHECK (width > 0),
  height      INTEGER NOT NULL CHECK (height > 0)
);

-- === The declared space and the targets ==================================================================

CREATE TABLE space_version (
  id            INTEGER PRIMARY KEY,
  ontology_sha  TEXT NOT NULL REFERENCES source_file,
  taxonomy_sha  TEXT NOT NULL REFERENCES source_file,
  UNIQUE (ontology_sha, taxonomy_sha)
);

-- The registry of axes and values, across versions: the natural key is the identity.
CREATE TABLE axis (
  name        TEXT PRIMARY KEY,                    -- room_type, style, light, camera, density, category...
  applies_to  TEXT NOT NULL CHECK (applies_to IN ('room', 'scene', 'clutter_spec', 'clutter_item'))
);

CREATE TABLE axis_value (
  axis   TEXT NOT NULL REFERENCES axis,
  value  TEXT NOT NULL,
  PRIMARY KEY (axis, value)
);

-- What one version of the ontology and taxonomy allows.
CREATE TABLE space_value (
  space_version_id  INTEGER NOT NULL REFERENCES space_version,
  axis              TEXT NOT NULL,
  value             TEXT NOT NULL,
  PRIMARY KEY (space_version_id, axis, value),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

CREATE TABLE target_set (
  id                INTEGER PRIMARY KEY,
  space_version_id  INTEGER NOT NULL REFERENCES space_version,
  targets_sha       TEXT NOT NULL REFERENCES source_file,
  UNIQUE (space_version_id, targets_sha)
);

-- A cell is a set of axis values; `pairs` accepted pairs are wanted in it.
CREATE TABLE target (
  id             INTEGER PRIMARY KEY,
  target_set_id  INTEGER NOT NULL REFERENCES target_set,
  pairs          INTEGER NOT NULL CHECK (pairs > 0)
);

-- === Buildings, rooms, scenes, clutter specs =============================================================

CREATE TABLE building (
  id                INTEGER PRIMARY KEY,
  space_version_id  INTEGER NOT NULL REFERENCES space_version
);

CREATE TABLE room (
  id           INTEGER PRIMARY KEY,
  building_id  INTEGER NOT NULL REFERENCES building
);

CREATE TABLE scene (
  id       INTEGER PRIMARY KEY,
  room_id  INTEGER NOT NULL REFERENCES room,
  seed     BIGINT NOT NULL CHECK (seed >= 0)       -- the clean loop's first seed; writers are seeded from it too
);

CREATE TABLE clutter_spec (
  id        INTEGER PRIMARY KEY,
  scene_id  INTEGER NOT NULL REFERENCES scene,
  variant   INTEGER NOT NULL CHECK (variant >= 1), -- 1..K
  seed      BIGINT NOT NULL CHECK (seed >= 0),
  UNIQUE (scene_id, variant)
);

CREATE TABLE clutter_item (
  id               INTEGER PRIMARY KEY,
  clutter_spec_id  INTEGER NOT NULL REFERENCES clutter_spec,
  ordinal          INTEGER NOT NULL CHECK (ordinal >= 1),
  UNIQUE (clutter_spec_id, ordinal)
);

-- One value per axis, for each kind of owner; target_value and lesson_scope, below, have the same shape.
CREATE TABLE room_value (
  room_id  INTEGER NOT NULL REFERENCES room,
  axis     TEXT NOT NULL,
  value    TEXT NOT NULL,
  PRIMARY KEY (room_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

CREATE TABLE scene_value (
  scene_id  INTEGER NOT NULL REFERENCES scene,
  axis        TEXT NOT NULL,
  value       TEXT NOT NULL,
  PRIMARY KEY (scene_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

CREATE TABLE clutter_spec_value (
  clutter_spec_id  INTEGER NOT NULL REFERENCES clutter_spec,
  axis        TEXT NOT NULL,
  value       TEXT NOT NULL,
  PRIMARY KEY (clutter_spec_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

CREATE TABLE clutter_item_value (
  clutter_item_id  INTEGER NOT NULL REFERENCES clutter_item,
  axis        TEXT NOT NULL,
  value       TEXT NOT NULL,
  PRIMARY KEY (clutter_item_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

-- === Rentals, runs, waves, loops, iterations =============================================================

CREATE TABLE rental (
  id              INTEGER PRIMARY KEY,
  provider        TEXT NOT NULL,
  session_id      TEXT NOT NULL,                   -- the provisioning session
  gpu             TEXT NOT NULL,
  gpu_count       INTEGER NOT NULL CHECK (gpu_count >= 1),
  price_per_hour  DOUBLE PRECISION NOT NULL CHECK (price_per_hour >= 0),
  started_at      TEXT NOT NULL,
  deadline        TEXT NOT NULL,                   -- the machine deletes itself then
  ended_at        TEXT
);

CREATE TABLE run (
  id             INTEGER PRIMARY KEY,
  config_sha     TEXT NOT NULL REFERENCES source_file,
  target_set_id  INTEGER NOT NULL REFERENCES target_set,
  target_pairs   INTEGER NOT NULL CHECK (target_pairs > 0),  -- the run stops here or at the rental's deadline
  rental_id      INTEGER REFERENCES rental,                  -- NULL on fake models
  started_at     TEXT NOT NULL,
  ended_at       TEXT
);

-- Ids increase with time across runs: a lesson's validity is an interval of waves.
CREATE TABLE wave (
  id          INTEGER PRIMARY KEY,
  run_id      INTEGER NOT NULL REFERENCES run,
  ordinal     INTEGER NOT NULL CHECK (ordinal >= 1),
  smoke       INTEGER NOT NULL DEFAULT 0 CHECK (smoke IN (0, 1)),  -- the end-to-end check at the start of a rental
  started_at  TEXT NOT NULL,
  UNIQUE (run_id, ordinal)
);

CREATE TABLE loop_run (
  id               INTEGER PRIMARY KEY,
  wave_id          INTEGER NOT NULL REFERENCES wave,
  stage            TEXT NOT NULL CHECK (stage IN ('clean', 'clutter')),
  scene_id         INTEGER REFERENCES scene,
  clutter_spec_id  INTEGER REFERENCES clutter_spec,
  input_image      TEXT REFERENCES image,          -- clutter loop: the clean image the editor receives
  lessons_arm      TEXT NOT NULL CHECK (lessons_arm IN ('on', 'off')),  -- seeded draw, recorded
  engine           TEXT NOT NULL,                  -- name and version of the policy and of its stop rule
  max_iterations   INTEGER NOT NULL CHECK (max_iterations >= 1),
  stop_reason      TEXT CHECK (stop_reason IN ('accepted', 'no_progress', 'max_iterations', 'deadline', 'error')),
  CHECK ((stage = 'clean' AND scene_id IS NOT NULL AND clutter_spec_id IS NULL AND input_image IS NULL)
      OR (stage = 'clutter' AND clutter_spec_id IS NOT NULL AND scene_id IS NULL AND input_image IS NOT NULL))
);

CREATE TABLE iteration (
  id           INTEGER PRIMARY KEY,
  loop_run_id  INTEGER NOT NULL REFERENCES loop_run,
  n            INTEGER NOT NULL CHECK (n >= 1),
  action       TEXT NOT NULL CHECK (action IN ('write', 'revise', 'reseed')),  -- what the engine asked
  seed         BIGINT NOT NULL CHECK (seed >= 0),  -- the generator's or editor's seed for this iteration
  -- Denormalized: derivable from the assessments by the verdict rule; kept for the index below; audit checks it.
  verdict      TEXT CHECK (verdict IN ('accept', 'revise')),
  UNIQUE (loop_run_id, n)
);
CREATE UNIQUE INDEX iteration_one_accept ON iteration (loop_run_id) WHERE verdict = 'accept';

-- clean loop: generated; clutter loop: raw_edit, corrected_edit (after the global colour correction),
-- change_mask (soft alpha in [0, 1] as an 8-bit image), composite (the cluttered image).
CREATE TABLE iteration_image (
  iteration_id  INTEGER NOT NULL REFERENCES iteration,
  role          TEXT NOT NULL CHECK (role IN ('generated', 'raw_edit', 'corrected_edit', 'change_mask', 'composite')),
  image_sha     TEXT NOT NULL REFERENCES image,
  PRIMARY KEY (iteration_id, role)
);

-- === Models, calls, exchanges, and what each request was built from ======================================

CREATE TABLE model (
  id        INTEGER PRIMARY KEY,
  name      TEXT NOT NULL,
  revision  TEXT NOT NULL,                         -- the weights as run, as the server reports them
  family    TEXT NOT NULL,                         -- the editor-family rule (choice C8)
  licence   TEXT NOT NULL,                         -- recorded, never a filter
  UNIQUE (name, revision)
);

CREATE TABLE model_call (
  id              INTEGER PRIMARY KEY,
  loop_run_id     INTEGER NOT NULL REFERENCES loop_run,
  iteration_id    INTEGER REFERENCES iteration,    -- NULL for the call after the loop (distill)
  role            TEXT NOT NULL CHECK (role IN ('write', 'generate', 'edit', 'judge', 'revise', 'distill')),
  model_id        INTEGER NOT NULL REFERENCES model,
  composer_sha    TEXT NOT NULL REFERENCES source_file,
  request_sha     TEXT NOT NULL REFERENCES text_blob,  -- canonical request (images by hash): the cache key
  answer_sha      TEXT REFERENCES text_blob,           -- the answer as used: chat content, generation result
  output_image    TEXT REFERENCES image,
  reused_call_id  INTEGER REFERENCES model_call,       -- an identical earlier request, answered from the store
  started_at      TEXT NOT NULL,
  wall_seconds    DOUBLE PRECISION,
  gpu_seconds     DOUBLE PRECISION,                    -- as the generator reports it; NULL for chat calls
  error_code      TEXT,
  error_message   TEXT
);
CREATE INDEX model_call_request ON model_call (request_sha);

-- Every HTTP exchange of a call, from the endpoint's observer: blob uploads, the request, job polls, downloads.
-- A text body keeps its bytes with each embedded image (data URL) replaced by `data:<type>;sha256,<hex>`.
CREATE TABLE exchange (
  model_call_id      INTEGER NOT NULL REFERENCES model_call,
  ordinal            INTEGER NOT NULL CHECK (ordinal >= 1),
  method             TEXT NOT NULL,
  path               TEXT NOT NULL,
  attempt            INTEGER NOT NULL CHECK (attempt >= 0),
  status             INTEGER,                      -- NULL when no answer came
  body_text_sha      TEXT REFERENCES text_blob,
  body_image         TEXT REFERENCES image,        -- a body that is an image (blob upload)
  wire_sha           TEXT CHECK (wire_sha IS NULL OR length(wire_sha) = 64),  -- the bytes actually sent
  response_text_sha  TEXT REFERENCES text_blob,
  response_image     TEXT REFERENCES image,
  content_type       TEXT NOT NULL,
  seconds            DOUBLE PRECISION NOT NULL,
  error_code         TEXT,
  PRIMARY KEY (model_call_id, ordinal),
  CHECK (body_text_sha IS NULL OR body_image IS NULL),
  CHECK (response_text_sha IS NULL OR response_image IS NULL)
);

-- === Assessments =========================================================================================

-- From the versioned reasons file. A code's severity is fixed here, so the verdict does not rest on the judge's
-- own severity call.
CREATE TABLE reason (
  code      TEXT PRIMARY KEY,                      -- not_empty, off_spec, implausible, misaligned, global_repaint,
  stage     TEXT NOT NULL CHECK (stage IN ('clean', 'clutter', 'both')),  -- unexplained_change, clutter_off_spec...
  severity  TEXT NOT NULL CHECK (severity IN ('blocking', 'minor')),
  file_sha  TEXT NOT NULL REFERENCES source_file
);

CREATE TABLE assessment (
  id             INTEGER PRIMARY KEY,
  iteration_id   INTEGER NOT NULL REFERENCES iteration,
  kind           TEXT NOT NULL CHECK (kind IN ('pixel', 'judge', 'detector', 'human')),
  -- Denormalized: derivable from its findings by the verdict rule; audit checks it.
  verdict        TEXT NOT NULL CHECK (verdict IN ('pass', 'fail')),
  model_call_id  INTEGER REFERENCES model_call,   -- the judge's call
  CHECK ((kind = 'judge') = (model_call_id IS NOT NULL))
);

CREATE TABLE finding (
  id               INTEGER PRIMARY KEY,
  assessment_id    INTEGER NOT NULL REFERENCES assessment,
  code             TEXT NOT NULL REFERENCES reason,
  judged_severity  TEXT CHECK (judged_severity IN ('blocking', 'minor')),  -- the judge's own call, recorded
  x0 DOUBLE PRECISION, y0 DOUBLE PRECISION, x1 DOUBLE PRECISION, y1 DOUBLE PRECISION,
  comment          TEXT,
  CHECK ((x0 IS NULL AND y0 IS NULL AND x1 IS NULL AND y1 IS NULL)
      OR (0 <= x0 AND x0 < x1 AND x1 <= 1 AND 0 <= y0 AND y0 < y1 AND y1 <= 1))
);

-- The pair judge locates each specified item; every component of the change mask must fall in one (F1 of review).
CREATE TABLE located_item (
  assessment_id    INTEGER NOT NULL REFERENCES assessment,
  clutter_item_id  INTEGER NOT NULL REFERENCES clutter_item,
  x0 DOUBLE PRECISION NOT NULL, y0 DOUBLE PRECISION NOT NULL, x1 DOUBLE PRECISION NOT NULL, y1 DOUBLE PRECISION NOT NULL,
  PRIMARY KEY (assessment_id, clutter_item_id),
  CHECK (0 <= x0 AND x0 < x1 AND x1 <= 1 AND 0 <= y0 AND y0 < y1 AND y1 <= 1)
);

CREATE TABLE guidance (
  assessment_id  INTEGER NOT NULL REFERENCES assessment,
  rank           INTEGER NOT NULL CHECK (rank >= 1),
  text_sha       TEXT NOT NULL REFERENCES text_blob,
  PRIMARY KEY (assessment_id, rank)
);

-- Pixel tests: what was measured, and the threshold in force.
CREATE TABLE measure (
  assessment_id  INTEGER NOT NULL REFERENCES assessment,
  name           TEXT NOT NULL,                    -- shift_px, global_delta_e, mask_share, unexplained_share...
  kind           TEXT NOT NULL CHECK (kind IN ('value', 'threshold')),
  value          DOUBLE PRECISION NOT NULL,
  PRIMARY KEY (assessment_id, name, kind)
);

-- === Lessons, decisions, and the parts of each request ===================================================

-- Active from a wave until it ends: the active set at any wave, and so every replay, is derivable.
CREATE TABLE lesson (
  id                   INTEGER PRIMARY KEY,
  stage                TEXT NOT NULL CHECK (stage IN ('clean', 'clutter')),
  text_sha             TEXT NOT NULL REFERENCES text_blob,
  distill_call_id      INTEGER NOT NULL REFERENCES model_call,
  replaces_lesson_id   INTEGER REFERENCES lesson,
  active_from_wave_id  INTEGER NOT NULL REFERENCES wave,
  ended_wave_id        INTEGER REFERENCES wave,  -- NULL while active
  end_kind             TEXT CHECK (end_kind IN ('replaced', 'retired', 'promoted')),
  CHECK ((ended_wave_id IS NULL) = (end_kind IS NULL))
);

CREATE TABLE lesson_evidence (
  lesson_id     INTEGER NOT NULL REFERENCES lesson,
  iteration_id  INTEGER NOT NULL REFERENCES iteration,
  PRIMARY KEY (lesson_id, iteration_id)
);

-- The owner's acts and every automatic rule's act: who, when, what, why.
CREATE TABLE decision (
  id             INTEGER PRIMARY KEY,
  at             TEXT NOT NULL,
  actor          TEXT NOT NULL,                    -- 'owner', or 'rule:<name>@<version>'
  action         TEXT NOT NULL CHECK (action IN ('lesson_retire', 'lesson_promote', 'threshold_set', 'review_mark',
                                                 'decision_rule')),
  lesson_id      INTEGER REFERENCES lesson,
  assessment_id  INTEGER REFERENCES assessment,
  detail         TEXT NOT NULL                     -- JSON: the values set, the reason given
);

-- The ordered parts the composer assembled. Inputs to a composer: its file (with the spec renderer and its version),
-- the call's model, and these parts; nothing else (P9). Exactly the column matching source_kind is set; a spec part
-- renders the spec of the call's loop subject.
CREATE TABLE composition_part (
  model_call_id  INTEGER NOT NULL REFERENCES model_call,
  ordinal        INTEGER NOT NULL CHECK (ordinal >= 1),
  slot           TEXT NOT NULL,
  source_kind    TEXT NOT NULL CHECK (source_kind IN ('template', 'instruction', 'schema', 'spec', 'lesson',
                                                      'assessment', 'call_output', 'image', 'setting', 'seed')),
  file_sha       TEXT REFERENCES source_file,      -- template, instruction, schema
  lesson_id      INTEGER REFERENCES lesson,
  assessment_id  INTEGER REFERENCES assessment,
  call_id        INTEGER REFERENCES model_call,    -- the output of a writer or reviser call
  image_sha      TEXT REFERENCES image,
  setting_name   TEXT,                             -- setting: its name; the value is the text
  origin         TEXT CHECK (origin IN ('config', 'spec', 'engine', 'subject')),  -- setting or seed: where from
  text_sha       TEXT REFERENCES text_blob,        -- the rendered text or value; NULL for an image
  PRIMARY KEY (model_call_id, ordinal),
  CHECK ((source_kind IN ('template', 'instruction', 'schema')) = (file_sha IS NOT NULL)),
  CHECK ((source_kind = 'lesson') = (lesson_id IS NOT NULL)),
  CHECK ((source_kind = 'assessment') = (assessment_id IS NOT NULL)),
  CHECK ((source_kind = 'call_output') = (call_id IS NOT NULL)),
  CHECK ((source_kind = 'image') = (image_sha IS NOT NULL)),
  CHECK ((source_kind = 'image') = (text_sha IS NULL)),
  CHECK ((source_kind = 'setting') = (setting_name IS NOT NULL)),
  CHECK ((source_kind IN ('setting', 'seed')) = (origin IS NOT NULL))
);

CREATE TABLE lesson_scope (
  lesson_id  INTEGER NOT NULL REFERENCES lesson,
  axis       TEXT NOT NULL,
  value      TEXT NOT NULL,
  PRIMARY KEY (lesson_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

CREATE TABLE target_value (
  target_id  INTEGER NOT NULL REFERENCES target,
  axis       TEXT NOT NULL,
  value      TEXT NOT NULL,
  PRIMARY KEY (target_id, axis),
  FOREIGN KEY (axis, value) REFERENCES axis_value
);

-- === Exports =============================================================================================

CREATE TABLE export (
  id            INTEGER PRIMARY KEY,
  name          TEXT NOT NULL UNIQUE,
  created_at    TEXT NOT NULL,
  manifest_sha  TEXT NOT NULL CHECK (length(manifest_sha) = 64)
);

-- The split is a property of the building: its rooms, scenes and pairs follow it (P6 by construction).
CREATE TABLE export_building (
  export_id    INTEGER NOT NULL REFERENCES export,
  building_id  INTEGER NOT NULL REFERENCES building,
  split        TEXT NOT NULL CHECK (split IN ('train', 'validation', 'test')),
  PRIMARY KEY (export_id, building_id)
);

-- A snapshot: pairs accepted later do not join an existing export. A pair is its accepted clutter iteration.
CREATE TABLE export_pair (
  export_id     INTEGER NOT NULL REFERENCES export,
  iteration_id  INTEGER NOT NULL REFERENCES iteration,
  PRIMARY KEY (export_id, iteration_id)
);

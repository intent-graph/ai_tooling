-- clutter_pairs — store schema (slice 1). Explained in design/data_model.md.
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
-- change_mask (soft alpha in [0, 1] as an 8-bit image), composite (the cluttered image), regions (the composite with
-- the mask's numbered regions drawn, for the pair judge).
CREATE TABLE iteration_image (
  iteration_id  INTEGER NOT NULL REFERENCES iteration,
  role          TEXT NOT NULL CHECK (role IN ('generated', 'raw_edit', 'corrected_edit', 'change_mask', 'composite',
                                              'regions')),
  image_sha     TEXT NOT NULL REFERENCES image,
  PRIMARY KEY (iteration_id, role)
);

-- A clutter iteration's regions, computed before the pair judge (judge aid A2): the thresholds and the drawing's
-- version used, the mask pixels left in specks. A row even when no region was numbered; audit recomputes from it.
CREATE TABLE region_set (
  iteration_id     INTEGER PRIMARY KEY REFERENCES iteration,
  region_group_px  INTEGER NOT NULL CHECK (region_group_px >= 0),
  region_min_px    INTEGER NOT NULL CHECK (region_min_px >= 1),
  max_regions      INTEGER NOT NULL CHECK (max_regions >= 1),
  drawing          INTEGER NOT NULL,                -- version of the regions image's drawing
  speck_px         INTEGER NOT NULL CHECK (speck_px >= 0)
);

-- The numbered regions of a clutter iteration's change mask (pieces grouped, specks dropped, largest first): a pure
-- function of the mask and its region set's thresholds.
CREATE TABLE mask_region (
  iteration_id  INTEGER NOT NULL REFERENCES region_set,
  n             INTEGER NOT NULL CHECK (n >= 1),
  x0 DOUBLE PRECISION NOT NULL, y0 DOUBLE PRECISION NOT NULL, x1 DOUBLE PRECISION NOT NULL, y1 DOUBLE PRECISION NOT NULL,
  px            INTEGER NOT NULL CHECK (px > 0),     -- mask pixels in the region
  PRIMARY KEY (iteration_id, n),
  CHECK (0 <= x0 AND x0 < x1 AND x1 <= 1 AND 0 <= y0 AND y0 < y1 AND y1 <= 1)
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

-- The regions of the change mask a finding cites (pair judge).
CREATE TABLE finding_region (
  finding_id  INTEGER NOT NULL REFERENCES finding,
  n           INTEGER NOT NULL CHECK (n >= 1),
  PRIMARY KEY (finding_id, n)
);

-- The pair judge's answer per numbered region: whether it also holds a change that is not a listed item. A region of
-- the iteration's mask_region with no row here was left out or answered twice: an unexplained change (judge aid A2).
CREATE TABLE region_answer (
  assessment_id  INTEGER NOT NULL REFERENCES assessment,
  n              INTEGER NOT NULL CHECK (n >= 1),
  other_change   INTEGER NOT NULL CHECK (other_change IN (0, 1)),
  PRIMARY KEY (assessment_id, n)
);

-- The items the pair judge assigns to a region; none: the region holds no listed item.
CREATE TABLE region_item (
  assessment_id    INTEGER NOT NULL,
  n                INTEGER NOT NULL,
  clutter_item_id  INTEGER NOT NULL REFERENCES clutter_item,
  PRIMARY KEY (assessment_id, n, clutter_item_id),
  FOREIGN KEY (assessment_id, n) REFERENCES region_answer
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

-- === Views: derived, never stored (data_model.md, "Views") ===============================================

-- Accepted clean images, per scene: the generated image of a clean loop's accepted iteration.
CREATE VIEW clean_image AS
SELECT lr.scene_id, lr.id AS loop_run_id, it.id AS iteration_id, ii.image_sha
FROM loop_run lr
JOIN iteration it ON it.loop_run_id = lr.id AND it.verdict = 'accept'
JOIN iteration_image ii ON ii.iteration_id = it.id AND ii.role = 'generated'
WHERE lr.stage = 'clean';

-- One row per accepted pair; its id is the accepted clutter iteration. The families come from the call that made
-- the clean image and from the edit call (one generate or edit call per iteration).
CREATE VIEW pair AS
SELECT it.id AS pair_id, b.id AS building_id, r.id AS room_id, s.id AS scene_id, cs.id AS clutter_spec_id,
       lr.id AS loop_run_id, lr.input_image AS clean_image, comp.image_sha AS cluttered_image,
       mask.image_sha AS mask_image, gm.id AS clean_model_id, gm.family AS clean_family,
       em.id AS editor_model_id, em.family AS editor_family
FROM iteration it
JOIN loop_run lr ON lr.id = it.loop_run_id AND lr.stage = 'clutter'
JOIN clutter_spec cs ON cs.id = lr.clutter_spec_id
JOIN scene s ON s.id = cs.scene_id
JOIN room r ON r.id = s.room_id
JOIN building b ON b.id = r.building_id
JOIN iteration_image comp ON comp.iteration_id = it.id AND comp.role = 'composite'
JOIN iteration_image mask ON mask.iteration_id = it.id AND mask.role = 'change_mask'
JOIN model_call ec ON ec.iteration_id = it.id AND ec.role = 'edit'
JOIN model em ON em.id = ec.model_id
JOIN clean_image ci ON ci.scene_id = s.id AND ci.image_sha = lr.input_image
JOIN model_call gc ON gc.iteration_id = ci.iteration_id AND gc.role = 'generate'
JOIN model gm ON gm.id = gc.model_id
WHERE it.verdict = 'accept';

-- Every axis value of a pair: its room's, its scene's and its clutter spec's.
CREATE VIEW pair_value AS
SELECT p.pair_id, v.axis, v.value FROM pair p JOIN room_value v ON v.room_id = p.room_id
UNION ALL
SELECT p.pair_id, v.axis, v.value FROM pair p JOIN scene_value v ON v.scene_id = p.scene_id
UNION ALL
SELECT p.pair_id, v.axis, v.value FROM pair p JOIN clutter_spec_value v ON v.clutter_spec_id = p.clutter_spec_id;

-- Per target: pairs wanted and pairs accepted, by relational division on (axis, value), whatever the space version.
CREATE VIEW coverage AS
SELECT t.target_set_id, t.id AS target_id, t.pairs AS wanted,
       (SELECT COUNT(*) FROM pair p
        WHERE NOT EXISTS (SELECT 1 FROM target_value tv
                          WHERE tv.target_id = t.id
                            AND NOT EXISTS (SELECT 1 FROM pair_value pv
                                            WHERE pv.pair_id = p.pair_id AND pv.axis = tv.axis AND pv.value = tv.value)))
         AS accepted
FROM target t;

-- Per loop, in wave order: its iterations and how it stopped. Descriptive.
CREATE VIEW iteration_curve AS
SELECT lr.stage, w.run_id, w.id AS wave_id, w.ordinal AS wave_ordinal, lr.id AS loop_run_id, lr.lessons_arm,
       (SELECT COUNT(*) FROM iteration it WHERE it.loop_run_id = lr.id) AS iterations, lr.stop_reason
FROM loop_run lr JOIN wave w ON w.id = lr.wave_id;

-- The loops the carry-forward comparison counts: finished, in waves from the stage's first active lesson on, not
-- evidence of a lesson. The decision rule (decision_rules/carry_forward.md) is applied to these rows by the report.
CREATE VIEW carry_forward_loop AS
SELECT ic.*
FROM iteration_curve ic
WHERE ic.stop_reason IS NOT NULL AND ic.stop_reason NOT IN ('deadline', 'error')
  AND ic.wave_id >= (SELECT MIN(l.active_from_wave_id) FROM lesson l WHERE l.stage = ic.stage)
  AND NOT EXISTS (SELECT 1 FROM lesson_evidence le JOIN iteration it ON it.id = le.iteration_id
                  WHERE it.loop_run_id = ic.loop_run_id);

CREATE VIEW carry_forward AS
SELECT stage, lessons_arm, COUNT(*) AS loops,
       AVG(CASE WHEN stop_reason = 'accepted' THEN 1.0 ELSE 0.0 END) AS accepted_share,
       AVG(CASE WHEN stop_reason = 'accepted' THEN 1.0 * iterations END) AS mean_iterations_to_accept
FROM carry_forward_loop
GROUP BY stage, lessons_arm;

-- Per lesson: the loops whose first request (the write call) cited it. Descriptive.
CREATE VIEW lesson_use AS
SELECT DISTINCT cp.lesson_id, mc.loop_run_id
FROM composition_part cp JOIN model_call mc ON mc.id = cp.model_call_id
WHERE cp.source_kind = 'lesson' AND mc.role = 'write';

-- Per run, stage, role and model: calls, reused calls, wall and generator seconds. The rental's price times its wall
-- clock, and the cost per accepted pair, are computed by the report from `run` and `rental`.
CREATE VIEW call_cost AS
SELECT w.run_id, lr.stage, mc.role, m.name AS model, COUNT(*) AS calls,
       SUM(CASE WHEN mc.reused_call_id IS NULL THEN 0 ELSE 1 END) AS reused,
       SUM(COALESCE(mc.wall_seconds, 0)) AS wall_seconds, SUM(COALESCE(mc.gpu_seconds, 0)) AS gpu_seconds
FROM model_call mc
JOIN loop_run lr ON lr.id = mc.loop_run_id
JOIN wave w ON w.id = lr.wave_id
JOIN model m ON m.id = mc.model_id
GROUP BY w.run_id, lr.stage, mc.role, m.name;

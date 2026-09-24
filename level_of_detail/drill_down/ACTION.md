# Action — building, editing, running at variable detail

Read this when you change the world: write or edit files, run commands or tests, produce artifacts, execute a plan. Assumes `LOD_CORE.md`.

## Principle
<!-- Lines 7-9 -->

Actions have a height too. A coarse action moves the whole: create the path end to end, run the whole suite. A fine action moves one part: one function, one test, one row. Choose the height of the next action as you choose the view: from purpose, criticality, certainty.

## Thin path first
<!-- Lines 12-16 -->

- Before any part is finished, make the whole exist at low resolution: the smallest end-to-end version that runs, with stubs, one record, a hard-coded input. It grounds the shape of the solution, exposes integration risk early, and gives every later fine action a place to land.
- Then drill: pick the branch with the highest criticality and the lowest certainty; bring it to full; verify; roll it up; pick the next.
- Do not polish a branch the purpose does not need. A settled branch stays at claim.

## Verification at matching height
<!-- Lines 19-23 -->

- After a coarse change, a coarse check: the whole path runs, the suite is green, the output has the right shape. Read results at label first (pass, fail, counts); drill into failures only.
- After a fine change, a targeted check (the unit, the one query), then one coarse check to confirm nothing else moved.
- Verbose output is full-level input. Ask for it only when drilling a failure.

## Roll up as you go
<!-- Lines 26-29 -->

- A verified branch becomes claim plus pointer: "endpoint X returns the new shape; `test_x_shape` green". Logs and diffs stay on disk.
- Working memory holds the live branch in full and the rest at claim. This is what keeps a long task tractable (`TASK_OUTLINE.md`).

## Height of edits
<!-- Lines 32-36 -->

- Prefer several small edits, each with an intent you can state in one line, over one large edit. Each small edit is a fact you can ground and revert.
- Sweeping changes (renames across a tree, reformatting) are coarse actions: announce them, run them as one unit, verify coarsely.
- Never mix heights in one edit. A rename plus a logic change hides the logic change.

## Irreversibility raises criticality
<!-- Lines 39-42 -->

- Deletion, external sends, deploys, schema changes, anything with people on the other end: the branch goes to full before acting and the human sees the view (`HUMAN_CONTROL.md`).
- Check that the evidence supports this specific action. A symptom that matches a known failure may have another cause; drill one level before acting on a pattern match.

## Edge cases
<!-- Lines 45-49 -->

- **The plan changes mid-way.** Re-set the view; do not append to the old outline. Say which branch replaced which.
- **A fine fix keeps failing.** Stop drilling. Roll up to the parent and ask whether the cut is wrong: the fault sits in a sibling or on the boundary.
- **Long-running commands.** Launch, then work another branch; read the result at label when it lands.
- **Many similar edits.** Do one in full, verify it, then apply the pattern as a coarse action, then verify coarsely. Do not do all in full or all blind.

# Final pass brief — the Opus agent that has the last word on flagged points (MD-06)

Paths are relative to `build/distill/` in the guideline folder; the task message gives the
absolute root.

## Goal

Settle every point the judges and reviewers flagged as subtle, so the judged records can be
built into the IntentGraph; and prepare the short list of points only the maintainer can decide.

## Read

- `maintainer_decisions.md` and `target_hierarchy.md`: the rules (MD-01 the best, not the
  average and not the most demanding; MD-02 outcomes whoever does the work; MD-03 one location
  per fact).
- `03_judge/brief_judge.md` and `brief_review.md`: what judges and reviewers had to do.
- `03_judge/cross_unit_fixes.md`: fixes already decided across units.
- For each of the nine units `03_judge/<unit>/`: the `flag` lines of `review/findings.md`, and
  the judge's flags still open in `judged.md` (each record's Flags field, and the "Review
  applied" section at its end). Open the records, rows and sources each flag concerns, and
  fetch a source when the flag turns on what it says.

## For every flag

Decide one of:

- **settle**: state the corrected decision text (or "unchanged") for the record, with grounds;
- **cross-unit**: the flag spans units; state the fix once, as a new line of
  `cross_unit_fixes.md` (X4 onwards), naming which record holds the content and which points to
  it;
- **maintainer**: only when the answer depends on the maintainer's own context or reverses
  their codified practice (MAINT rows, source MAINT-S01) and the evidence does not settle it,
  or the node is marked undecided. Give the recommendation and the default applied if
  unanswered.

Apply MD-01 strictly: where the maintainer's codified practice and public consensus differ,
decide on the strongest argument; a risk-class or context split is right only when sources
show the best practice really differs between the classes, never as a compromise.

## Output

In `03_judge/final_pass/`:

- `resolutions.md`: one entry per flag: unit, node uid, flag id(s) merged, verdict (settle /
  cross-unit / maintainer), the decision text to write into the record when it changes, grounds.
  Grouped by unit, so one applier per unit can apply it.
- `maintainer_points.md`: the maintainer list, each item self-contained (the situation, the
  options with their costs, the recommendation, the default if unanswered, in plain language,
  no internal ids without saying what they are). Include every decision that goes against the
  maintainer's codified practice, even when settled, in a separate section "Settled against
  your practice", one line each with the reason, so the maintainer sees them.
- New lines appended to `03_judge/cross_unit_fixes.md`.
- `result.md` with `## L1 headline`, `## L2 claims`, `## L3 full`, each readable alone, each
  claim marked grounded / inferred / open. Pin, word for word at every level: flags read,
  settled, cross-unit, maintainer; decisions changed; sources fetched.

Do not edit `judged.md` files. Public repository: no absolute or home paths, no private names.
Never commit or push.

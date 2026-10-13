# Apply brief — one applier per judged unit

Paths are relative to `build/distill/`; your task message gives the absolute root and your unit.

## Goal

Bring your unit's `judged.md` to its final state by applying the final pass, so the graph
writers transcribe settled records only.

## Read

- `03_judge/final_pass/resolutions.md`: your unit's section (every entry for your unit).
- `03_judge/cross_unit_fixes.md`: every line whose Units column names your unit (X1 to X14). A
  line says which record holds the content and which points to it (MD-03).
- `03_judge/final_pass/maintainer_points.md`: the one open maintainer point and its default
  (node ASSURANCE.RULES.4, unit J2 only).
- Your unit's `03_judge/<unit>/judged.md`.

## Do

- Apply every resolution and every cross-unit line for your unit to `judged.md`: replace the
  decision, constraint, rejected or grounds text as stated; add the nodes the final pass creates;
  turn restated content into a pointer where a line says your record points to another.
- J2 only: write ASSURANCE.RULES.4 with the default text given in `maintainer_points.md` and add
  to its Certainty "open: awaiting the maintainer's answer on whether an automated reviewer can
  be the independent check".
- Remove from each record's Flags the flags now settled; keep "none" when none remains.
- Add a section `## Final pass applied` at the end: one line per resolution and per cross-unit
  line, applied or not applied with the reason.
- Do not re-judge anything. If a resolution contradicts another or cannot be applied, leave the
  record unchanged and say so in that section.

## Output

`judged.md` updated, and `03_judge/<unit>/apply_result.md` with `## L1 headline`,
`## L2 claims`, `## L3 full`, each readable alone, each claim marked grounded / inferred /
open. Pin, word for word at every level: resolutions applied and not applied; cross-unit lines
applied and not applied; nodes added; flags still open.

Public repository: no absolute or home paths, no private names. Write only in your unit folder.
Never commit or push.

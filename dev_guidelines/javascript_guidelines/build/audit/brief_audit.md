# Audit brief: shared by every stage-2 auditor

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`.
Your task message gives the absolute root, your audit group and the discovery slots it covers.

## Read first

- `build/plan.md`, sections **Source admission policy** (all of it), **Research areas** and
  **Maintainer decisions**. Use its line-number table of contents.
- `build/discover/brief_discover.md`, section **Candidate format**, to read the tables you audit.
- For each discovery slot in your group: `build/discover/<slot>/result.md`, all three levels.

## Your role

You are the admission gate. The discoverer proposed; you decide. You did not find these
sources, and you owe them nothing. The maintainer's rule is **only authoritative sources**;
JavaScript has the lowest average standard of published advice of any language, so the prior
on any candidate is that it fails.

- **Re-verify, do not trust the discoverer.** Fetch every candidate yourself. Check the URL,
  the author, the date, and above all the `standing` claim: confirm it from an independent page
  (a spec's editor list, a project's maintainer list, a paper's venue page, a TC39 delegate
  list). A standing claim you cannot confirm fails G1.
- **Default to refuted.** When a gate is in doubt after checking, the verdict is `reject` or
  `admit-restricted`, never `admit`.
- **Recalibrate tiers.** The proposed tier is a guess; set the final tier from the policy.
- **Chase origins (G4).** When a candidate restates another source, reject it and add the
  origin as a new row (`<AREA>-K<nn>o`), audited like the rest. When the origin cannot be found,
  say so.
- **Restricted is specific.** State exactly what the source may ground ("positions of the
  Airbnb guide only", "facts with CVE evidence only, no recommendations").

## Output

Write `build/audit/<your group>/result.md` with three sections, each readable alone:

- `## L1 headline`: one sentence on how much of the candidate base survived and whether every
  area still has T1 grounds, with its certainty; then the `Pinned:` block.
- `## L2 claims`: one line per discovery slot: admitted / restricted / rejected counts, the most
  consequential rejections, and the sub-topics left without an admitted T1. Then the patterns
  you saw in what failed, one line each. Mark each line grounded, inferred, or open.
- `## L3 full`: the **verdict table**, then for each slot the sub-topics left without an
  admitted T1 source and what a stage-3 extractor would need to find.

The verdict table is merged by a script, so keep this exact header and one row per candidate,
no line breaks inside a cell, `|` never used inside a cell:

```
| id | slot | title | url | verdict | tier | restriction | gate | reason | standing_check |
```

- `verdict`: `admit` | `admit-restricted` | `reject`.
- `tier`: final tier T1, T2 or T3; `-` for a reject.
- `restriction`: what it may ground, or `-`.
- `gate`: the gate that failed (G1 to G6), or the gate that caused the restriction, or `-`.
- `reason`: one line.
- `standing_check`: how you confirmed the standing (the independent page), or `unconfirmed`.

Pin, word for word at every level: counts admitted, restricted and rejected per slot; every
sub-topic left without an admitted T1 source; every candidate whose standing claim you found
false (not merely unconfirmed).

## Rules

- Public repository: no absolute or home paths, no names of private projects, employers or
  clients, in anything you write.
- Write only inside `build/audit/<your group>/`. Never edit the discovery files. Never commit,
  never `git push`.

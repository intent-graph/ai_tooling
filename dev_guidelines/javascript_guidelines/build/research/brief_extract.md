# Extraction brief: shared by every stage-3 slot

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`.
Your task message gives the absolute root, your slot and your area code.

## Read first

- `build/plan.md`, sections **Goal**, **Boundary with sibling guidelines**, **Source admission
  policy** (the claim threshold and the standing rules), **Research areas** (your row and your
  siblings'), **Claim format**, **Maintainer decisions**. Use its line-number table of contents.
- `build/audit/source_register.md`: the admitted sources. Your working set is every row whose
  `slots` column names your slot; you may also cite any other row. Read each row's
  `restriction`: a restricted source grounds only what it states.
- `build/audit/<group>/result.md` for your slot's audit group, `## L3 full` only, the part that
  lists the sub-topics left without an admitted T1 source and what to look for.

## Goal of this stage

Read the admitted sources of your area **in full** and extract the claims a guideline for solid,
maintainable, secure JavaScript needs: what to do, what to avoid, and why, each traced to what
the sources actually say. You are gathering grounded claims, not writing the guideline.

## Rules of grounding

- **Cite only register sources**, by their `SRC-nnn` id and the section or heading read. A claim
  that needs a source not in the register is not written as a claim: put the source in **late
  candidates** (below) and the claim in **gaps**.
- **Apply the claim threshold** of the plan: one T1 ground, or two independent T2 grounds.
  Below that, the claim is still recorded, with `agreement: single-source` and the tier it rests
  on, and it can never be `consensus`.
- **Respect restrictions.** A style guide restricted to its positions grounds "guide X holds Y",
  never "do Y". Framework and tool documentation grounds facts about that tool only.
- **Quote the decisive words.** For every claim resting on a T1 source, give the shortest exact
  passage that makes it true. Your fetch tool may return a digest rather than the page: ask it
  for the verbatim passage, and mark the quote `tool-extracted`. If you cannot get wording you
  trust, say so in the certainty field.
- **Mechanism over assertion.** Where a rule follows from the language or runtime, name the spec
  section or runtime behaviour in `mechanism`; that is what lets a reader check the rule.
- **Disagreement is data.** When admitted sources disagree, record one claim with
  `agreement: contested` and every position with its holders and the condition under which it
  applies. Do not settle it.
- **Popular beliefs.** When an admitted source corrects a widespread belief (a spec note, an MDN
  warning, a maintainer's correction), record the correction as a claim and tag it
  `folklore: <the belief in a few words>`. The dissent stage collects these.

## Claim table (L3 of your result)

Checked by script, so keep this exact header, one row per claim, no line break inside a cell,
`|` never inside a cell:

```
| id | claim | level | stack | since | sources | agreement | certainty | mechanism | quote | tags |
```

- `id`: `<AREA>-C<nn>`.
- `claim`: one normative sentence ("Prefer X over Y when Z", "Never X, because Y").
- `level`, `stack`, `since`, `mechanism`: as the plan's Claim format defines.
- `sources`: `SRC-nnn §section` entries separated by `;`.
- `agreement`: `consensus` | `majority` | `contested` | `single-source`.
- `certainty`: `grounded` (read in the cited source) | `inferred` (your synthesis; say from which
  rows) | `open`.
- `quote`: the exact passage, with `(tool-extracted)` when it came through a digest, or `-`.
- `tags`: any of `boundary: <owner>`, `folklore: <belief>`, `positions: <holder: position; ...>`
  for contested claims, or `-`.

Aim for the claims that matter: typically 25 to 60. Do not pad; record gaps instead.

## Result file

Write `build/research/<your slot>/result.md` with three sections, each readable alone:

- `## L1 headline`: one sentence on the state of authoritative guidance for your area, with its
  certainty; then the `Pinned:` block.
- `## L2 claims`: one line per cluster of claims (5 to 12 clusters): the cluster's claim,
  agreement, certainty, claim ids. Then contested topics, one line each. Then gaps.
- `## L3 full`: the claim table; then **gaps** (what a guideline needs here that no admitted
  source grounds, and what you searched); then **late candidates** (sources you found that are
  not in the register, in the discovery brief's candidate format, for a later audit).

Pin, word for word at every level: the number of claims, by agreement; every contested topic in
a few words; every register source you could not read in full, and why.

## Rules

- Public repository: no absolute or home paths, no names of private projects, employers or
  clients, in anything you write.
- Write only inside `build/research/<your slot>/`. Never edit the register, the audit or the
  discovery files. Never commit, never `git push`.
- Stay inside your area; a claim on a boundary is recorded once, tagged `boundary: <owner>`.

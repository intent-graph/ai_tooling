# Stage-4 brief: coverage (slot 11) and dissent (slot 12)

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`.
Your task message gives the absolute root and your slot.

## Read first

- `build/plan.md`, sections **Goal**, **Boundary with sibling guidelines**, **Source admission
  policy**, **Research areas**, **Claim format**, **Maintainer decisions**.
- `build/research/brief_extract.md`, section **Claim table**, to read the tables.
- For each extraction slot `01_lang` to `10_frameworks`: `build/research/<slot>/result.md`,
  `## L2 claims` in full; `## L3 full` for the claim rows your task needs (search the tables by
  tag or keyword rather than reading every row).
- `build/audit/source_register.md` when you need a source's tier or restriction.

## Slot 11_coverage: what the claim base covers, and what it misses

1. **Gaps.** Take the viewpoint of a team that must write solid, maintainable, secure JavaScript
   in the browser and in Node. List what such a guideline must say that no claim grounds, per
   area, with criticality (high: a security or correctness hole; medium; low). Merge the gaps the
   slots reported with the ones you find.
2. **Overlaps.** Claims in two slots that say the same thing, or that conflict without being
   marked contested. Name both ids and the better owner.
3. **Boundary items.** Every claim tagged `boundary:`, grouped by owner; flag any that the
   sibling guideline should hold instead.
4. **Late candidates.** Collate every slot's late candidates into one deduplicated table (the
   discovery brief's candidate format), each marked with the high-criticality gap it would fill.
   These are not admitted sources: they go to a later audit.
5. **Threshold check.** Run `python3 build/research/check_claims.py` from the root and report
   its summary; list the slots whose claims are mostly single-source.

## Slot 12_dissent: disagreements and the folklore audit

1. **Disagreements.** Every claim with `agreement: contested`, and any pair of claims across
   slots that conflict. For each topic: every position, its holders (register ids), the
   condition under which each applies, and whether the disagreement is real or a difference of
   scope.
2. **Folklore audit.** JavaScript carries more widespread, unexamined advice than any language.
   From the `folklore:` tags, and from what the admitted sources themselves correct or warn
   against, build a list of popular beliefs, each judged `confirmed`, `restricted` (true only
   under a condition, stated) or `refuted`, with the claim ids and the T1 ground. Never cite a
   source outside the register to show that a belief is popular; the maintainer's rule is
   authoritative sources only, so a belief enters this list only when an admitted source
   addresses it.
3. **Maintainer questions.** The contested topics that a guideline must decide (the type-layer
   choice is one), each phrased as a question with the positions and a recommendation marked
   inferred.

## Result file

Write `build/research/<your slot>/result.md` with three sections, each readable alone:
`## L1 headline` (one sentence and its certainty, then `Pinned:`), `## L2 claims` (one line per
finding, with certainty and claim ids), `## L3 full` (everything above in full). Mark each
finding grounded, inferred or open.

Pin, word for word at every level. Slot 11: the number of high-criticality gaps, and each named
in a few words; the number of late candidates; the checker's summary line. Slot 12: the number
of contested topics, and each named in a few words; folklore counts by verdict.

## Rules

- Public repository: no absolute or home paths, no names of private projects, employers or
  clients, in anything you write.
- Write only inside `build/research/<your slot>/`. Never edit another slot's files, the register
  or the audit. Never commit, never `git push`.

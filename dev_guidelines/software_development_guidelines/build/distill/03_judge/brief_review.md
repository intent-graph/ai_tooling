# Review brief — shared by every reviewer

Paths are relative to `build/distill/` in the guideline folder; your task message gives the
absolute root and the unit you review.

## Goal

Review one judged unit adversarially, so that clear defects are fixed before the graph is built
and subtle points go to a final Opus pass (MD-06).

## Read

- `maintainer_decisions.md`, `target_hierarchy.md` (the rules), `03_judge/brief_judge.md` (what
  the judge had to do).
- The unit's `03_judge/<unit>/judged.md`, and its nodes' records in
  `02_skeleton/branches/<BRANCH>/branch.md` (the positions the judge chose from).
- Rows and sources as needed: the three ledger parts and the three source registers under
  `01_consolidate/`.

## Check every record for

1. **Averaging** — the decision blends positions, picks the most common one, or picks the most
   demanding one, instead of the best for the node's purpose (MD-01).
2. **Grounding** — the grounds cite rows and sources that actually say what is claimed. Fetch
   at least two cited sources of the unit (T1 or T2) and check them.
3. **Missed positions** — a position in the skeleton record, or a MAINT row, absent from
   Positions or Rejected.
4. **Rejected without a condition** — every rejected position needs the condition under which
   it would be the best.
5. **Author rules** — a rule about who writes the code instead of the outcome (MD-02).
6. **Context creep** — a context condition no row supports.
7. **Consistency** — contradiction with another node of the unit, or with a decided node it
   realizes.
8. **Duplication** — content restated on an index node or in two nodes (MD-03).

## Output

In `03_judge/<unit>/review/`: `findings.md`, one line per finding: node uid, check number,
severity (`fix`: clear and settled, the judge can apply it; `flag`: subtle or contestable, for
the Opus pass), what is wrong, the proposed correction, evidence (row, source, or fetched
quote). Then `result.md` with `## L1 headline`, `## L2 claims`, `## L3 full`, each readable
alone, each claim marked grounded / inferred / open. Pin, word for word at every level:
records reviewed, findings `fix`, findings `flag`, sources fetched and how many confirmed.

Do not edit `judged.md`. Public repository: no absolute or home paths, no private names. Write
only in your review folder. Never commit or push.

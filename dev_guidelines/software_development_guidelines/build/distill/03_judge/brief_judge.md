# Judge brief — shared by every judge unit

Paths are relative to `build/distill/` in the guideline folder; your task message gives the
absolute root, your unit id and the nodes it covers.

## Goal

For every node of your unit, decide **the best practice for the node's purpose** from the
competing positions the skeleton lists, and write a judge record, so the decisions can be
reviewed and built into the IntentGraph.

## Read

- `maintainer_decisions.md` and `target_hierarchy.md`: they bind. Cite MD numbers.
- `03_judge/units.md`: your unit, its nodes, and which decided units it depends on.
- Your nodes' records in `02_skeleton/branches/<BRANCH>/branch.md` (positions, rows, links),
  and `02_skeleton/objections/resolution.md` for rows moved in or out.
- The rows in full where a position needs more than the record holds:
  `01_consolidate/claims_ledger.md` (L001-L460), `part2/claims_ledger_part2.md` (L1001-L1289),
  `part3/claims_ledger_part3.md` (L1501-L1565); sources in the three `sources*.md` files.
- For a realization unit: the judged records of the decision nodes your nodes `Realize`
  (`03_judge/<unit>/judged.md`, listed in `units.md`). Settled decisions are input; never
  re-decide them. If you think one is wrong, raise a flag.

## How to decide (MD-01, MD-02)

- **The best, not the average.** Pick the practice the strongest argument across sources
  establishes for this node's purpose. Never the most common answer, never a blend of two
  positions into one sentence, and "best" is not "most demanding". Agreement among sources is
  evidence, never the verdict.
- **Outcomes, whoever does the work.** State the decision as a principle and the outcome it
  guarantees (for example: the design was good, the testing was good, the review was
  trustworthy, what runs is what was reviewed). No rule about who writes the code.
- **Context only where it moves the answer.** A condition belongs on the decision only if a
  row shows the best practice differs with it; then state the condition and the other best.
- **The maintainer's codified practice** (MAINT rows, source MAINT-S01, not citable) is a strong
  position, not an automatic winner. Where it is the best, say so; where it is not, say why and
  under which condition it would be.
- **Rows judged in the JavaScript guideline** (marked `origin: judged in the JavaScript
  guideline`) are re-examined; their prior verdict is one position.
- **Undecided** only for a genuine trade-off: maximizing one purpose the node serves costs
  another it also serves, and no source settles it. Then flag it for the maintainer with both
  options and a recommendation.
- **One location per fact (MD-03).** On an index node write only its one-line intent and links.

## Judge record (every node)

1. **Decision** — the best practice, one to three normative sentences, and the outcome it
   guarantees.
2. **Grounds** — why it is the best, with row ids and source ids (register ids).
3. **Positions** — each competing practice with the force it serves.
4. **Rejected** — each other position, the reason, and the condition under which it would be
   the best.
5. **Context** — conditions that change the decision (only as above), or "none".
6. **Certainty** — grounded (named sources support the decision), inferred (follows from them),
   open (what is missing).
7. **Flags** — points you cannot settle with confidence, each one line with why; "none"
   otherwise. A flag is not a way to avoid deciding: decide, then flag if unsure.

Also keep, for the graph build: the node's one-line intent (rewritten if the decision sharpens
it), constraints (MUST conditions), and links.

## Output

In `03_judge/<unit>/`: `judged.md` (one record per node, in tree order) and `result.md` with
`## L1 headline`, `## L2 claims`, `## L3 full`, each readable alone, each claim marked grounded /
inferred / open. Pin, word for word at every level: nodes judged; decisions marked undecided;
flags raised; any settled decision you disagree with.

Public repository: no absolute or home paths, no private names. Write only in your unit folder.
Never commit or push.

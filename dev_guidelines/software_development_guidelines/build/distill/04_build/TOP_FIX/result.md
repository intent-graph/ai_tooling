# TOP_FIX result

## L1 headline

Seven L1 nodes set (OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE) in `batch.yaml`, seven `node.set` ops. Field changed per node: `intent` only (grounded: epistemic_state already `inferred`, matching every record's Certainty "Inferred as a roll-up"; design_notes already holds Decision, Grounds and Rejected). Dry run on a scratch copy: `ig-tool validate` gave nodes: 292, links: 196, errors: 0, warnings: 0; the copy is deleted. The real graph is untouched.

## L2 claims

The seven new intents, verbatim (each one to three sentences, capitalized, stack-neutral; each states the roll-up decision of its judge record and the outcome it guarantees; grounded: derived from the Decision field of each record in `build/distill/03_judge/rollup/judged.md`).

- **OWNERSHIP**: Nothing is added by default: each capability is written, adopted or rented through a recorded, per-need decision, then declared, locked, watched and kept as a managed liability, with its licence obligations known before use and its exit priced in proportion to what failure would cost (STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES, LICENCE). The team always knows what it depends on, why, and what leaving would cost.
- **ASSURANCE**: Every property that must hold has a named mechanism at a named stage that runs on every change, with a signal that can be believed, gates that cannot be skipped and review that is independent and bound to the exact content; none rests on one control or on the author's judgement. One placement per property (behaviour, contracts, data integrity, documentation sync, security, performance, availability, artifact) means that the design was good, the testing was good, the review was trustworthy, and what runs is what was reviewed.
- **CONSTRUCTION**: Design is derived from usage down to code, with effort where error is costly; the system starts as the simplest shape that serves, is cut by the decision each module hides, and parses what crosses a trust boundary once into a precise form that never reaches an interpreter as code. Each fact has one place and dependencies flow one way, so the code is correct at its boundaries and a change touches few places.
- **CHANGE_FLOW**: Everything needed to build, deploy and restore lives in version control, and small, independently reviewed changes are integrated into one mainline; one hermetic build produces one artifact that is promoted unchanged, released and deployed progressively by the same automated process everywhere. The way back is decided before a change ships, so what ships was reviewed, built once and is reversible.
- **OPERATION**: The running system is held to a stated reliability objective below 100 percent, measured as users experience it and governed by an agreed rule, and a human is paged only for what needs a human now. Incidents follow written conditions and named roles, workloads launch after a readiness review, and recovery is designed from stated objectives and proven before it is needed, so the system stays within its objectives and, when it fails, is restored within them.
- **EVOLUTION**: Significant decisions are recorded where the code lives and superseded, never rewritten; change is made in steps that keep the system releasable, every dual-support phase ends with a removal, debt is an inventoried liability repaid where code changes, and obsolete forms are retired in two announced stages by an owner. The set of technologies stays small because each addition is a replacement, so the system keeps working while it changes and nothing old stays by neglect.
- **TRANSVERSE**: Each cross-cutting concern is an owned, recorded practice whose guarantee is held elsewhere: documentation sized by its readers, security anchored in a published framework with one vulnerability loop and protected event logs, personal data minimised and retained on a schedule, configuration and secrets kept out of code and artifact, and development environments treated as code and separated from production. The guarantees ASSURANCE decides thus have a practice that can be carried out and checked.

Other claims:
- epistemic_state unchanged on all seven: grounded (current value begins `inferred:` and carries the record's open items; each record's Certainty field says "Inferred as a roll-up").
- design_notes unchanged on all seven: grounded (checked that each already contains the Decision, Grounds and Rejected paragraphs of its record).
- No other field, no other node, no link touched: grounded (apply report lists `fields: intent` for every op).

## L3 full

Method: read the seven records (Decision, Certainty) in `build/distill/03_judge/rollup/judged.md`, the "Field mapping" of `build/distill/04_build/brief_build.md`, the `node.set` format in the graph-edit skill, and the current nodes via `ig-tool query --node`; the ROOT intent was the model (decision first, then the outcome).

Per node, fields changed: intent (all seven); epistemic_state none; design_notes none.

Old to new: the old intents were lowercase scope fragments ("how code is structured...", "how the running system is kept..."). The new ones state the decision and the guaranteed outcome, keeping the L2 names in parentheses only where they help locate the children (OWNERSHIP), as ROOT does.

Why no epistemic_state or design_notes change: all seven current epistemic_state values start `inferred:` and list the open nodes of the record's Certainty; the unvalidated flags on ASSURANCE (RULES.4) and EVOLUTION (TECHNOLOGY.4) match the records' Flags. design_notes starts with "Decision:" and contains "Grounds:" and "Rejected:" for all seven (string check; not a word-by-word comparison with the record, inferred complete).

Dry run (on a scratch copy, since deleted):
- `ig-tool apply -g scratch.ig.yaml --batch batch.yaml -o scratch.ig.yaml --role builder -m "dry TOP_FIX"`: 7 operations, all success, fields: intent.
- `ig-tool validate -g scratch.ig.yaml`: nodes: 292, links: 196, errors: 0, warnings: 0.

Files: `batch.yaml`, `result.md` in `build/distill/04_build/TOP_FIX/`. Nothing committed or pushed.

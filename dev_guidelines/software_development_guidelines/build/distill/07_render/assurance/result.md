# Render result: ASSURANCE branch

## L1 Headline

ASSURANCE rendered: 54 of 54 nodes in 6 files (838 lines, largest 182), all under the guideline folder: `assurance.md` (56, intro and index), `assurance_rules.md` (140), `assurance_behaviour.md` (150), `assurance_interfaces_data.md` (139), `assurance_docs_security.md` (182), `assurance_performance_availability.md` (171). Open maintainer point shown inline with the default applied: can an automated reviewer be the independent check (`ASSURANCE.RULES.4`, in `assurance_rules.md`). `md-structure-sync --toc add-always --max-level 3` run on all 6: ok. Nothing in the graph edited, nothing committed.

## L2 Claims

- **Files written and sizes** (grounded, counted with `wc -l`): assurance.md 56; assurance_rules.md 140; assurance_behaviour.md 150; assurance_interfaces_data.md 139; assurance_docs_security.md 182; assurance_performance_availability.md 171. All within the 500-line limit.
- **Split** (grounded): intro and index in `assurance.md`; the other five by L2 groups: RULES + ARTIFACT; BEHAVIOUR; CONTRACTS + DATA_INTEGRITY; DOCS_SYNC + SECURITY; PERFORMANCE + AVAILABILITY. Hand-chosen, not by the brief's file names.
- **Nodes rendered** (grounded): 54 of 54 (1 L1, 9 L2, 44 L3); 54 distinct uids found by grep across the files.
- **Open maintainer points shown** (grounded): 1, `ASSURANCE.RULES.4`, as a blockquote with the default (independence is a property of the reviewer's context; named person stays accountable; different-kind reviewer for high-risk changes), repeated as a pointer in `assurance.md` "Still open".
- **Open gaps shown in one line where a reader acts on them** (grounded): effect size of mutation testing, restore-test cadence, penetration-test period, production recovery-drill frequency, release-archive content, single-team seam rule, consumer-count boundary, second-level provenance floor on other platforms, runtime transfer of measurement methods.
- **md-structure-sync** (grounded): ran on each of the 6 files, "1/1 files updated" each, no errors.
- **Stack neutrality and public rules** (grounded by grep): no product names, no ledger, register or research ids, no absolute paths, no dates or versions in the six files.
- **Cross-file links** (inferred): links to `ownership.md`, `construction.md`, `change_flow.md`, `operation.md`, `transverse.md` use anchors that are slugs of the target node names read from the graph (for example `change_flow.md#build-and-pipeline`). Each assumes the sibling writer renders the node as a heading with its name in the file of its L1 branch; if a sibling splits its branch into `<branch>_<group>.md`, those links need repointing. Not checked, the siblings are written in parallel.
- **Dropped on purpose** (grounded): design_notes provenance (positions, grounds, source ids), maintainer-practice attributions, and per-node history; only "Best instead when" conditions and open gaps kept.

## L3 Full

### Files (absolute folder: the guideline folder)

| File | Lines | Holds | Nodes |
|---|---|---|---|
| `assurance.md` | 56 | L1 thesis, map table of nine properties, shared principles, still-open list | `ASSURANCE` |
| `assurance_rules.md` | 140 | RULES.1-5, ARTIFACT.1-2 | RULES, RULES.1-5, ARTIFACT, ARTIFACT.1-2 (9) |
| `assurance_behaviour.md` | 150 | BEHAVIOUR.1-8 | BEHAVIOUR, .1-.8 (9) |
| `assurance_interfaces_data.md` | 139 | CONTRACTS.1-3, DATA_INTEGRITY.1-5 | CONTRACTS, .1-.3, DATA_INTEGRITY, .1-.5 (10) |
| `assurance_docs_security.md` | 182 | DOCS_SYNC.1-4, SECURITY.1-7 | DOCS_SYNC, .1-.4, SECURITY, .1-.7 (13) |
| `assurance_performance_availability.md` | 171 | PERFORMANCE.1-5, AVAILABILITY.1-5 | PERFORMANCE, .1-.5, AVAILABILITY, .1-.5 (12) |

Total 1 + 9 + 10 + 13 + 12 + 9 = 54.

### Rendering choices

- L1: two-to-four-line thesis, then a map table with relative links, shared principles, "Best instead when" for the two rejected whole-branch positions (per-stage placement, single global gate), still-open list, realised-in pointer.
- L2: heading, one-to-three-line intro, uid. L3: heading, practice, rules from constraints (grouped), "Best instead when" from rejected positions with conditions, open gaps in one line, links as `requires`/`realizes`/`refines` phrases, uid last.
- Index-type content (consumer side of contracts, dependency inventory, backup practice, documentation authoring, security programme, privacy periods) rendered as one-line links to the sibling file.
- Coverage numbers, flake thresholds, the ten-minute figure, the 10 percent false-alarm figure are stated as one organisation's or defaults, as the graph marks them.

### Open maintainer point, as rendered (`ASSURANCE.RULES.4`)

Question: can an automated reviewer be the independent check? Default applied, marked inferred: independence is a property of the reviewer's context, not its kind; an automated reviewer in its own context counts; a named person stays accountable and approves; a high-risk change gets a reviewer of a different kind from its author. No source covers a team of one. Default stands until answered.

### Checks run

- `grep -o` of uids: 54 unique across the six files.
- `grep -niE` for product names, ledger and research ids, absolute paths: no hits.
- `md-structure-sync --toc add-always --max-level 3 <file>`: ok on all six.

### Not done / limits

- Sibling anchors unverified (see L2).
- No Mermaid diagram used: the map table carries the structure.
- No second review pass by a separate agent.

# Render result: OWNERSHIP

## L1 headline

OWNERSHIP rendered into 4 files (679 lines in all, each at most 225), 36 of 36 branch nodes, md-structure-sync run on each; no "awaiting maintainer" point exists in the branch, 4 open gaps shown inline.

- Files and line counts: `ownership.md` 47 (intro, rules, map, one diagram), `ownership_stance_selection.md` 225, `ownership_lifecycle_containment.md` 210, `ownership_services_licence.md` 197. Split because one file came to 653 lines.
- Nodes rendered: 36 of 36 (1 L1, 6 L2, 29 L3), each with its uid.
- Open maintainer points shown: 0 (grep for "awaiting maintainer" over the branch: none). Open gaps shown inline: CONTAINMENT.4, SERVICES.2, SERVICES.5, LICENCE.3.
- md-structure-sync: run on all four files, status ok. Anchors checked: 0 broken links within the branch.
- Open for the caller: anchors to sibling files assume their headings are the node names (checked names via the graph, siblings not yet read).

## L2 claims

- Layout [grounded]: `ownership.md` is the index (thesis, three binding rules, map table, diagram) and links the three body files; split by L2 pairs in the lifecycle order: stance and selection, lifecycle and containment, services and licences.
- Coverage [grounded]: all 36 nodes appear (uid count per file 1, 12, 11, 12 = 36). L3 nodes are `###` subsections: intent, rules from constraints (MUST lines kept, grouped, de-duplicated with the L2 rules), and "Best instead when" lines from the Rejected records where one names a condition.
- Maintainer points [grounded]: none in the graph for this branch, so none shown. Open gaps changing reader action shown as "Open:" lines at CONTAINMENT.4 (runtime isolation extent), SERVICES.2 (consumers acting on deprecation signals), SERVICES.5 (assurance reports and tool criteria), LICENCE.3 (linking boundary left to legal review).
- Inferred parts [inferred]: the graph's gaps marked "inferred" are carried as short "Inferred:" lines; ledger, register and claim ids were not copied.
- Cross-file links [inferred]: links to `construction.md`, `assurance.md`, `evolution.md`, `transverse.md` use the slug of the node name (Cut by Hidden Decision, Parse or Validate at the Edge, Tolerating a Degraded Dependency, Protecting Remote Calls, What Counts as Compatible, Secrets and Consumed Code, Technical Debt and Refactoring, Decision Records, Configuration and Secrets, Credential Lifetime and Pipeline Identity, Response to a Leaked Secret, Privacy and Retention). They resolve only if those files use the same heading text.
- Stack neutrality [grounded]: no tool names; standards and laws appear only where the graph's own intent or example names them (SQL, SMTP, EU Cyber Resilience Act, EU financial entities, EU for processor contracts).
- Deviation [grounded]: for L3 nodes the uid sits at the end of the intro line, not after the last rule line, to keep the section readable; the L1 and L2 uids close the thesis.

## L3 full

Source: graph `intent_graphs/software_development_philosophy.ig.yaml`, root OWNERSHIP, read with `ig-tool query --node` and `--links` per node (36 nodes); the graph was not edited.

Files (all in the guideline folder):

| File | Lines | Holds |
|---|---|---|
| `ownership.md` | 47 | L1 thesis and uid, three branch rules, certainty line, map table, one flowchart |
| `ownership_stance_selection.md` | 225 | STANCE (4 L3), SELECTION (6 L3) |
| `ownership_lifecycle_containment.md` | 210 | LIFECYCLE (5 L3), CONTAINMENT (4 L3) |
| `ownership_services_licence.md` | 197 | SERVICES (6 L3), LICENCE (4 L3) |

Rendering decisions:
- Split: a first single file had 653 lines (over the 500 maximum), so `ownership.md` became the index and the six L2 nodes were grouped in pairs. Intra-branch anchors were rewritten to point at the file that holds the target; a script confirmed all anchors in the four files resolve.
- Index nodes: none in this branch.
- Links rendered: realizes or requires links to other branches shown as one phrase with a relative link: CONTAINMENT.2 to CONSTRUCTION.HIDING.1 and CONSTRUCTION.BOUNDARY.1, ASSURANCE.AVAILABILITY.2; CONTAINMENT.3 to TRANSVERSE.CONFIG; CONTAINMENT.4 to CONSTRUCTION.BOUNDARY.1; SERVICES.1 to ASSURANCE.AVAILABILITY.1; SERVICES.2 to ASSURANCE.CONTRACTS.1; SERVICES.4 to TRANSVERSE.PRIVACY; SERVICES.6 to TRANSVERSE.CONFIG.5; SELECTION.1 to EVOLUTION.DECISIONS (constraint text); SELECTION.6 to ASSURANCE.SECURITY.5; LIFECYCLE.3 to EVOLUTION.DEBT and TRANSVERSE.CONFIG.6; LIFECYCLE.5 to EVOLUTION.DEBT and ASSURANCE.SECURITY.5. Incoming links from other branches are not repeated here.
- Open gaps shown (all four listed as open at the L1 node): CONTAINMENT.4, SERVICES.2, SERVICES.5, LICENCE.3.
- Certainty of the render: the wording follows `intent` and `constraints` closely [grounded]; "Best instead when" lines are condensed from the Rejected records [inferred as faithful, not independently reviewed]. A review pass by a separate agent was not part of this task.
- md-structure-sync was run as `md-structure-sync --toc add-always --max-level 3 <file>` so each file carries a line-number TOC and header line comments; status ok for all four.

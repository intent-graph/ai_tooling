# Intentlinks of the two built graphs

## L1 headline

Created 197 intentlinks, 0 failed; both graphs validate with 0 errors and 0 warnings (`ig-tool validate -m intent_resources.yaml`, inter endpoints resolved).

- `web-app-philosophy`: 42 intra + 15 inter to `python-kb-philosophy` = 57.
- `pig-web-defaults`: 21 intra + 119 inter to `web-app-philosophy` = 140.
- Per kind, intra philosophy: 25 realizes, 9 requires, 4 constrains, 2 dataflow, 1 refines, 1 conflicts. Philosophy to python: 14 refines, 1 conflicts. Intra defaults: 19 realizes, 1 constrains, 1 requires. Defaults to philosophy: 71 realizes, 42 refines, 5 requires, 1 conflicts.
- Skipped: 1 proposed node (and its 3 links), 13 redundant child-level refines, 12 citations in records that are not links, 14 informal "Realizes" lines. Details in L3.
- Defect found, not touched (node content is out of scope): five philosophy nodes carry a python-kb node id as their `name` (ALLOCATION, ALLOCATION.RULES.1, ALLOCATION.RULES.3, ALLOCATION.GUARD.1, ALLOCATION.GUARD.2). Their names read `python-kb-philosophy:POLYGLOT`, `...:DATACENTRICITY`, `...:DEFENSIVE` (three times); the colon is also forbidden in node names. Their links were created by uid and are valid. The builder of phil_allocation should restore the skeleton names.

## L2 claims

Files: batches in this folder, one intra and one inter per graph; applied with `--role linker`.
- `links_web_app_philosophy_intra.yaml`, `links_web_defaults_intra.yaml`: applied with `ig-tool apply --batch`.
- `links_web_app_philosophy_inter.yaml`, `links_web_defaults_inter.yaml`: same op format, applied one by one with `ig-tool link create`, because `apply --batch` does not dispatch qualified endpoints to the inter-link store ("Source node ... does not exist"). Inter links are stored in the file of their source graph.

Deduplication: every philosophy placement link appeared in both the philosophy lists and the defaults lists; each (src, dst) pair now exists once, and no pair exists in both directions. The kind of each link is stored as `shape.type` and stated in the intent sentence.

Created, by kind of link:
- Philosophy tier to placement (realizes, requires, constrains): the skeleton's tier-to-placement table plus 12 judge-proposed links, all with real endpoints and a stated dependency.
- Philosophy within-graph transverse links: refines (security to trust boundary), dataflow (performance to forces), requires (contracts to origin definition; environment to contracts), conflicts (security log versus audit trail).
- Philosophy to python-kb: 14 refines and 1 conflicts (EVOLUTION.4 against POLYGLOT), one per skeleton row.
- Defaults tier to placement within the graph: 21 links (realizes, plus constrains JS_SERVER and requires POSTGRES_FIRST); 7 are judge-proposed.
- Defaults to philosophy, counterparts: 42 refines (tree-branch counterparts, placement refinements, and 10 judge-recorded child-level refines that name a more specific philosophy node than the parent's).
- Defaults to philosophy, placements: 77 realizes/requires/conflicts; about 55 of them come from judge records, not the skeleton.
- Intents rewritten, not copied: refines counterparts (the skeleton gave none), the LOGIC.EXPOSE to RECORD.2 link (the skeleton text predates the shared-database decision; the new text covers browsers, agents and outside consumers), and four refines intents corrected against node names.

Skipped groups (L3 lists each):
- Proposed node DATA.INTERFACE not created: its 3 links are not created. PIG-WEB-DATA.INTERFACE still realizes ALLOCATION.RECORD.2 and PIG-WEB-ALLOCATION.DB_API.
- 13 child-level refines in the transverse records, redundant with the parent-level refines link, which lifts to the children.
- 12 "rests on" citations in transverse records: stated as citations, never proposed as links.
- 14 informal "Realizes" lines in the data and logic records, weaker than a stated dependency or already carried by a parent link.

## L3 full

### Proposed node, not created
- DATA.INTERFACE (philosophy) realizes ALLOCATION.RECORD.2 and the database share of ALLOCATION.ACT.1: node does not exist.
- PIG-WEB-DATA.INTERFACE refines DATA.INTERFACE: node does not exist. Parent-level substitute created: PIG-WEB-DATA.INTERFACE realizes ALLOCATION.RECORD.2.

### Redundant child-level refines (judge records, transverse)
Reason for each: the parent already refines the same philosophy node, and the link lifts when the parent is collapsed; a child link adds no dependency.
- PIG-WEB-TRANSVERSE.SECURITY.1 to .5 to TRANSVERSE.SECURITY (5).
- PIG-WEB-TRANSVERSE.CONTRACTS.1, .2 to TRANSVERSE.CONTRACTS (2).
- PIG-WEB-TRANSVERSE.OPERABILITY.2, .3 to TRANSVERSE.OPERABILITY (2).
- PIG-WEB-TRANSVERSE.TOPOLOGY.1 to .4 to LOGIC.PROCESS (4).

### Citations in records, not links (transverse records, "rests on")
Stated as citations in design_notes only, and the records did not propose them.
- TRANSVERSE.OPERABILITY.2 on FORCES.6, GUARD.2, GUARD.3, ACT.1, ACT.4 (5).
- TRANSVERSE.OPERABILITY.3 on RECORD.2, RECORD.3 (2).
- TRANSVERSE.EVOLUTION.1 on the allocation placements (unspecific, 0 counted).
- TRANSVERSE.EVOLUTION.3 on RECORD.1, RECORD.2 (2).
- TRANSVERSE.EVOLUTION.4 on PIG-WEB-ALLOCATION.POSTGRES_FIRST, CACHE_STORE, JOB_HOST (3).
- TRANSVERSE.EVOLUTION.5 on RECORD.2, ACT.1 (2).
- Other record text skipped: Interaction J4 sub-node citations (for example ENVIRONMENT.7 from REALTIME.4), prose hand-offs between pig-web branches, and LOGIC.EXPOSE.2 and .3 placement mentions (GUARD.4; PRESENT.1, RECORD.3); the records place these in design_notes only.

### Informal "Realizes" lines not created (defaults data records)
- PIG-WEB-DATA.ORGANIZE.1 and .2 to ALLOCATION.TYPE_CHAIN: "through the parent"; the parent ORGANIZE already realizes it.
- PIG-WEB-DATA.ORGANIZE.6 to ALLOCATION.ROW_SECURITY: tenancy without row security is a default stance, not a dependency.
- PIG-WEB-DATA.ORGANIZE.3 to DATA.GUARD (precise structure) and to DERIVE.2 collation: collation is marked open in the record.
- PIG-WEB-DATA.ORGANIZE.5 to DATA.GUARD (precise structure): weak.
- PIG-WEB-DATA.GUARD.2 to ALLOCATION.RECORD.2 and ALLOCATION.ACT.4 (session role names the consumer): the DB_API link and GUARD.3 link carry the dependency.
- PIG-WEB-DATA.GUARD.4 to ALLOCATION.ACT.4 and GUARD.2: secondary mentions.
- PIG-WEB-DATA.CONCURRENCY.1 to GUARD.5, .2 to GUARD.5 and GUARD.2, .3 to GUARD.5, .5 to GUARD.5, .4 to ACT.3: the parent CONCURRENCY already realizes GUARD.5; ACT.3 for .4 is a parenthetical.
- Parent-level "through its children" summaries for PIG-WEB-DATA, GUARD, MAINTAIN, DERIVE, ORGANIZE: summaries of the child links.

### Not skipped but worth knowing
- Judge-proposed links created: DATA.GUARD to GUARD.3, RULES.5; DATA.MAINTAIN to ACT.4; LOGIC.PROCESS to ACT.2, ACT.3; six INTERACTION.ENVIRONMENT links to PRESENT.3, GUARD.5, GUARD.6, GUARD.4; PIG-WEB-DATA.GUARD.2 to GUARD.3 and DB_API; PIG-WEB-DATA.CONCURRENCY.5 to ACT.2; the PIG-WEB-LOGIC.SECURE.1, ENFORCE.2, PROCESS.2, PROCESS.5, EXPOSE.7 proposals; and all PIG-WEB-INTERACTION "Realizes" proposals whose endpoints exist.
- The python graph file was not modified.

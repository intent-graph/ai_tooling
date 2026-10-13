# Result: batch for the ALLOCATION branch of web-app-philosophy (unit J1)

## L1 headline

`batch.yaml` creates all 39 web-app-philosophy nodes of J1 (ALLOCATION, its 8 families, 30 L3 nodes) and sets intent and design_notes on ROOT: 40 operations, 0 link.create. The dry run (apply on a copy of the graph with only its root, then validate) passed with 0 errors and 0 warnings; the copy held 40 nodes and 0 links. No node is deferred; 1 node carries an `undecided` clause (ALLOCATION.GUARD.3, read visibility of rows with per-user rules; its roll-ups ALLOCATION.GUARD carry it as well).

## L2 one line per operation

- `ROOT` node.set: intent (stack-neutral roll-up of the J1 verdicts) and design_notes (default context, maintainer decisions MD-01 to MD-03, the one verdict against the doctrine, the three tensions, Q1, skeleton and evidence gaps).
- `ALLOCATION` python-kb-philosophy:POLYGLOT (parent `ROOT`): known; 4 constraints, 2 impl_pointers.
- `ALLOCATION.FORCES` Allocation Forces (parent `ALLOCATION`): known; 5 constraints, 15 impl_pointers.
- `ALLOCATION.CONTEXT` Allocation Context (parent `ALLOCATION`): known; 5 constraints, 9 impl_pointers.
- `ALLOCATION.RULES` Allocation Rules (parent `ALLOCATION`): known; 1 constraints, 1 impl_pointers.
- `ALLOCATION.RECORD` Data Authority Placements (parent `ALLOCATION`): known; 2 constraints, 1 impl_pointers.
- `ALLOCATION.GUARD` Guarding Placements (parent `ALLOCATION`): known; 1 constraints, 1 impl_pointers.
- `ALLOCATION.ACT` Acting Placements (parent `ALLOCATION`): known; 1 constraints, 1 impl_pointers.
- `ALLOCATION.DERIVE` Derivation Placements (parent `ALLOCATION`): known; 1 constraints, 1 impl_pointers.
- `ALLOCATION.PRESENT` Presentation Placements (parent `ALLOCATION`): known; 1 constraints, 1 impl_pointers.
- `ALLOCATION.FORCES.1` Correctness (parent `ALLOCATION.FORCES`): known: demand stated by L606, L608, L628; 3 constraints, 6 impl_pointers.
- `ALLOCATION.FORCES.2` Security (parent `ALLOCATION.FORCES`): known: demand stated by L019, L644, L650; 4 constraints, 9 impl_pointers.
- `ALLOCATION.FORCES.3` Performance (parent `ALLOCATION.FORCES`): known; 3 constraints, 5 impl_pointers.
- `ALLOCATION.FORCES.4` Latency (parent `ALLOCATION.FORCES`): known; 3 constraints, 4 impl_pointers.
- `ALLOCATION.FORCES.5` Scalability (parent `ALLOCATION.FORCES`): speculative: the premise lacks a read primary source (L615); 3 constraints, 4 impl_pointers.
- `ALLOCATION.FORCES.6` Changeability (parent `ALLOCATION.FORCES`): known; 2 constraints, 5 impl_pointers.
- `ALLOCATION.RULES.1` python-kb-philosophy:DATACENTRICITY (parent `ALLOCATION.RULES`): known; 5 constraints, 5 impl_pointers.
- `ALLOCATION.RULES.2` End-to-End Placement (parent `ALLOCATION.RULES`): known; 3 constraints, 4 impl_pointers.
- `ALLOCATION.RULES.3` python-kb-philosophy:DEFENSIVE (parent `ALLOCATION.RULES`): known; 3 constraints, 7 impl_pointers.
- `ALLOCATION.RULES.4` One Core for Every Client (parent `ALLOCATION.RULES`): known; 3 constraints, 4 impl_pointers.
- `ALLOCATION.RULES.5` Atomicity Ends at the Transaction (parent `ALLOCATION.RULES`): known; 6 constraints, 7 impl_pointers.
- `ALLOCATION.RECORD.1` System of Record (parent `ALLOCATION.RECORD`): known; 4 constraints, 11 impl_pointers.
- `ALLOCATION.RECORD.2` Data Access Interface (parent `ALLOCATION.RECORD`): known: MD-03; 9 constraints, 14 impl_pointers.
- `ALLOCATION.RECORD.3` Type and Contract Definitions (parent `ALLOCATION.RECORD`): known: MD-02; 9 constraints, 12 impl_pointers.
- `ALLOCATION.GUARD.1` python-kb-philosophy:DEFENSIVE (parent `ALLOCATION.GUARD`): known; 6 constraints, 9 impl_pointers.
- `ALLOCATION.GUARD.2` python-kb-philosophy:DEFENSIVE (parent `ALLOCATION.GUARD`): known; 10 constraints, 12 impl_pointers.
- `ALLOCATION.GUARD.3` Authorization (parent `ALLOCATION.GUARD`): undecided: awaiting maintainer, read visibility of rows w...; 10 constraints, 20 impl_pointers.
- `ALLOCATION.GUARD.4` Identity and Session State (parent `ALLOCATION.GUARD`): known; 9 constraints, 18 impl_pointers.
- `ALLOCATION.GUARD.5` Concurrency Control and Conflict Resolution (parent `ALLOCATION.GUARD`): known; 9 constraints, 17 impl_pointers.
- `ALLOCATION.GUARD.6` Duplicate Suppression (parent `ALLOCATION.GUARD`): known; 8 constraints, 14 impl_pointers.
- `ALLOCATION.ACT.1` Business Rules and State Transitions (parent `ALLOCATION.ACT`): known: MD-03, L584; 10 constraints, 26 impl_pointers.
- `ALLOCATION.ACT.2` Side Effects and Integrations (parent `ALLOCATION.ACT`): known; 8 constraints, 17 impl_pointers.
- `ALLOCATION.ACT.3` Deferred and Scheduled Work (parent `ALLOCATION.ACT`): known; 8 constraints, 12 impl_pointers.
- `ALLOCATION.ACT.4` Audit and History (parent `ALLOCATION.ACT`): known: MD-03; 8 constraints, 15 impl_pointers.
- `ALLOCATION.DERIVE.1` Derived Data and Aggregation (parent `ALLOCATION.DERIVE`): known; 5 constraints, 11 impl_pointers.
- `ALLOCATION.DERIVE.2` Filtering, Sorting, Paging and Search (parent `ALLOCATION.DERIVE`): known; 7 constraints, 9 impl_pointers.
- `ALLOCATION.DERIVE.3` Caching (parent `ALLOCATION.DERIVE`): known; 8 constraints, 25 impl_pointers.
- `ALLOCATION.PRESENT.1` Rendering (parent `ALLOCATION.PRESENT`): known; 6 constraints, 16 impl_pointers.
- `ALLOCATION.PRESENT.2` Formatting and Localization (parent `ALLOCATION.PRESENT`): speculative: placement inferred from a capability source ...; 6 constraints, 2 impl_pointers.
- `ALLOCATION.PRESENT.3` UI and Ephemeral State (parent `ALLOCATION.PRESENT`): known; 7 constraints, 10 impl_pointers.

## Not transcribed, and why

- No link.create: every skeleton intentlink of these nodes has an endpoint outside the branch (another tier branch, the other graph, or the python knowledge-base graph). All 71 are listed in `links_out.md` for the linker.
- ROOT: the judge files hold no record titled root. The intent and design_notes are written from the ALLOCATION roll-up record and the final revision's result (L1 headline, claims, pinned block). If the DATA, LOGIC, INTERACTION and TRANSVERSE units also set ROOT, the coordinator should merge the texts; this batch's ROOT text describes only what J1 decides.
- Intent and constraints are written by hand, stack-neutral; the design_notes carry the judge records near-verbatim (positions, forces, decision, rejected options with their winning condition, tensions, maintainer decisions, revision notes R1 to R3, "Would move it"), including the stack names the records use. The records' State and Placement lines are not in design_notes: they became epistemic_state (verbatim, pipe annotations kept) and the Authority, Copies, Forbidden constraints (verbatim from the Placement line, with one rewording of a stack name in GUARD.4).
- Copies carry the purposes the record states in its Placement line; where that line gives none, none was invented.
- impl_pointers: the judge record, then every research claim behind the node's owned ledger rows plus every ledger row its record cites (ranges expanded); the collaboration slot's claims are written as in its file (`C01`). All cited ledger ids exist in the ledger.
- examples: only on ALLOCATION.GUARD.3 (the two rule examples the record quotes).
- history is not set; the tool records provenance.

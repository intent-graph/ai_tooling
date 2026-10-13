# J8_evolution result

## L1 headline

Judged (33 nodes): EVOLUTION (L1); DECISIONS, INCREMENTAL, DEBT, DECOMMISSION, TECHNOLOGY (L2); DECISIONS.1-6, INCREMENTAL.1-6, DEBT.1-5, DECOMMISSION.1-6, TECHNOLOGY.1-4 (27 L3). Records in `judged.md`.
Decisions marked undecided: 1 (DEBT.3: where debt-inventory items live; recommendation: tracker as inventory, in-code marker as pointer only). All other nodes decided (grounded or inferred as marked).
Review fixes applied: 13 of 13.
Flags raised: 8, of which F2 is now closed (F1 undecided inventory place; F2 closed by CHANGE_FLOW.REVIEW.2, tidy lands as its own change; F3 backups kept after retirement versus privacy retention; F4 speed-versus-quality payoff unproven; F5 forward-only conventions, few-consumer rename exception inferred; F6 conditions for a full rewrite inferred; F7 support-window figures are one project's; F8 contested technology-firmness and single-store rows, the one-version rule now has its home in CHANGE_FLOW.INTEGRATION.1, residual is the three-regime split).
Settled decisions disagreed with: none.
Headline of the decisions: record significant decisions beside the code and supersede, never rewrite; change in releasable steps and finish every migration with its removal; replace incrementally behind an interface; keep debt inventoried and repay it where code changes; retire in two announced stages with a deadline, an owner and verified usage; add a technology only as a replacement.

## L2 claims

Pinned: nodes judged 33 (EVOLUTION, 5 L2, 27 L3); undecided 1 (DEBT.3 inventory place); flags 8 (F1-F8, F2 closed); settled decisions disagreed with: none; review fixes applied: 13 of 13.

DECISIONS (grounded for the mechanics, inferred for the splits)
- Content: forces, decision, rejected alternatives with dissent, consequences including accepted costs, one fixed structure. Grounded.
- Threshold: record decisions that are significant and either option-weighed or without a governing standard; skip workarounds and experiments; many contributors or a long life lower the bar. Inferred.
- Form: short, one decision per record, numbered, in the repository of the code. Grounded.
- Change: an accepted record is superseded, not rewritten; living documents are a different document type. Grounded for the rule, inferred for the assignment.
- Status and use: status, named owner, review before acceptance; records consulted in review. Grounded; second part inferred (one source).
- Proposal: separate proposal before the record for many stakeholders; lightweight record alone for few. Inferred.

INCREMENTAL (grounded for step size and expand-migrate-contract, inferred for rewrite conditions and owner split)
- Releasable steps, released and checked against intended effect. Grounded.
- Expand, migrate, contract, with the removal step owned and tracked. Grounded.
- Replace incrementally behind the interface; full rewrite only with no seam or obsolete platform, with parallel running; big bang rejected. Grounded for positions, inferred for conditions (F6).
- Mass change: generated, sharded, old pattern blocked; accountable owner with capacity for many consumers. Grounded.
- Changeability investment by lifespan and consumer count; tests capturing reliance. Grounded.
- Conventions forward only with many consumers; coordinated rename for few (F5). Grounded / inferred.

DEBT (grounded for definition and step size, inferred for the rest)
- Debt is any liability on future change, wider than code. Grounded.
- Invest in quality from the start for anything changed; deliberate, recorded debt only for short-lived or exploratory work (F4). Inferred.
- Inventory with item fields; engineers' survey as primary signal, tools and measures as support. Inferred. UNDECIDED: where items live (F1).
- Refactor in small behaviour-preserving steps with green checks. Grounded.
- Repay maintainability debt where code changes, timed by cost comparison, tidy as its own change; risk-carrying debt follows DECOMMISSION.1 and LIFECYCLE; explicit capacity for cross-team debt. Inferred.

DECOMMISSION (grounded for staging and execution)
- Removal is planned work with owner and budget; retired code is removed from production. Grounded / inferred.
- Retire on five stated grounds and record it. Grounded.
- Two stages (deprecation, sunset), actionable, machine-readable warnings; consumer side stays in SERVICES.2. Grounded.
- Published tiered window for many external consumers, case by case for few (F7). Grounded.
- Compulsory with deadline and staffed owner when removal is intended; advisory only if replacement sells itself. Grounded.
- Verify use, restrict reversibly, backups per retention (F3), owner with milestones, remove attachments. Grounded.

TECHNOLOGY (grounded for replacement and register, inferred for firmness and store)
- Add as replacement with retirement planned. Grounded.
- Shared register with position and decision trail; rings only with capacity for experiments. Grounded / inferred.
- Firmness follows how much platform and on-call is shared; departures name who pays (F8). Inferred.
- One general-purpose store until a stated need exceeds it (F8). Inferred.

## L3 full

Pinned: nodes judged 33; undecided 1 (DEBT.3 inventory place, F1); flags F1 to F8 (F2 closed); settled decisions disagreed with: none; review fixes applied: 13 of 13. Each node's full record (Decision, Grounds, Positions, Rejected, Context, Certainty, Flags, Constraints, Links) is in `judged.md`, in tree order; the lines below are each node's decision.

- EVOLUTION: roll-up; no fact of its own. Constraints: no significant decision without a record; no incompatible change without removal step and owner; no retirement without verified usage and deadline; no technology added without retiring what it replaces. Inferred for debt timing and technology firmness.
- DECISIONS.1: record forces, decision, rejected alternatives and dissent, consequences and accepted costs, one structure. Grounded. Realizes SELECTION.1.
- DECISIONS.2: record significant decisions with options weighed or no governing standard; skip workarounds, experiments, policy-covered choices; CONTRIBUTORS_AND_LIFETIME lowers the bar. Inferred.
- DECISIONS.3: short, one per record, numbered without reuse, in version control beside the code. Grounded.
- DECISIONS.4: accepted record superseded, not rewritten (typo fixes only); DOCUMENT_TYPE: living docs for how-to and reference. Grounded.
- DECISIONS.5: status, named owner, review before acceptance; consult records in review, link a violation or supersede. Grounded; consult rule inferred.
- DECISIONS.6: STAKEHOLDER_COUNT: many, proposal then record; few, record alone. Inferred.
- INCREMENTAL.1: releasable steps, released and checked for intended effect. Grounded.
- INCREMENTAL.2: expand, migrate, contract; removal step owned and tracked; unfinished migration is debt. Grounded / inferred.
- INCREMENTAL.3: incremental replacement behind interface; full rewrite only if platform obsolete or no seam, with parallel running; "25 percent" rule not adopted. Positions grounded, conditions inferred (F6).
- INCREMENTAL.4: generate, shard, block old pattern; accountable owner with capacity for many consumers; self-migration only if replacement transformatively better. Grounded.
- INCREMENTAL.5: lifespan sets changeability investment; consumer count raises change cost; reliance-capturing tests in CI. Grounded.
- INCREMENTAL.6: MAINT forward-only with many consumers, marked deprecated items; coordinated rename for few reachable consumers (F5). Grounded / inferred.
- DEBT.1: any liability on future change, wider than code metrics, including migrations, docs, tests, dead code, dependencies, expertise, release process. Grounded; list inferred.
- DEBT.2: quality from the start for anything changed; recorded deliberate debt only for short-lived or exploratory work; simplicity kept (deletion in DECOMMISSION.1). Inferred (F4).
- DEBT.3: inventory with cause, consequence, artefact, impact; survey primary, tools and maintainability measures as support. Inferred. UNDECIDED: place of items (F1), recommendation tracker plus pointer markers.
- DEBT.4: small behaviour-preserving steps, checks green, characterization tests first if unpinned. Grounded.
- DEBT.5: repay maintainability debt where code changes, by cost comparison, never in code not changing; a tidy lands as its own change (REVIEW.2); risk-carrying debt follows DECOMMISSION.1 and LIFECYCLE; opportunistic with strong tests, explicit capacity for cross-team debt. Inferred.
- DECOMMISSION.1: removal is planned work with owner and budget; retired code removed from production. Grounded / inferred.
- DECOMMISSION.2: retire on five stated grounds; record as superseding the adoption record. Grounded.
- DECOMMISSION.3: deprecation then sunset, never earlier; actionable and machine-readable warnings; HTTP and Kubernetes forms are stack pointers. Grounded.
- DECOMMISSION.4: many external consumers, published tiered window; few, case by case; figures not adopted (F7). Grounded.
- DECOMMISSION.5: compulsory (deadline, owner, capacity) when removal is intended; advisory if replacement sells itself. Grounded.
- DECOMMISSION.6: verify use, reversible restriction, backups per retention (F3), owner with milestones, remove all attachments. Grounded.
- TECHNOLOGY.1: add as replacement with owned retirement; few tools per domain. Grounded.
- TECHNOLOGY.2: shared register with position and decision trail; rings only with experiment capacity. Grounded / inferred.
- TECHNOLOGY.3: firmness follows shared platform and on-call: mandate, paved path, or per-component fit; a departure names who pays (F8). Inferred.
- TECHNOLOGY.4: one general-purpose store until a stated requirement exceeds it, shown by measurement or a documented limit (F8). Inferred.

Flags: F1 DEBT.3 undecided inventory place. F2 closed (CHANGE_FLOW.REVIEW.2). F3 DECOMMISSION.6 backups versus privacy retention (settle in J9). F4 DEBT.2 payoff unproven. F5 INCREMENTAL.6 few-consumer rename inferred, maintainer to confirm. F6 INCREMENTAL.3 rewrite conditions inferred. F7 DECOMMISSION.4 figures one project's. F8 TECHNOLOGY.3 and .4 contested, thinly sourced; the one-version rule is homed in CHANGE_FLOW.INTEGRATION.1; residual: mandate versus paved path not separated by a source.

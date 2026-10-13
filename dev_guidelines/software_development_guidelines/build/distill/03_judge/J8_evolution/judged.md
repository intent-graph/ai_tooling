# J8_evolution: judge records (EVOLUTION, 27 L3 nodes, 5 L2 nodes, 1 L1 node)

Binding: MD-01 (best, not average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-04 (EVOLUTION is a top-level branch), MD-05 (scope). Positions are numbered as in `02_skeleton/branches/EVOLUTION/branch.md`. Row ids Lnnn are ledger ids; REG-nnn are source register ids; REG-181 is the maintainer's codified practice (MAINT, not citable).

Settled inputs, read and not re-decided: J1 (`OWNERSHIP.STANCE`, `SELECTION`, `LIFECYCLE`, `SERVICES`, as final after review) and J2 (`ASSURANCE.BEHAVIOUR`, `CONTRACTS`, `RULES`). Cross-unit fix X7 (supersedes X3): the provider-side evolution policies are held in `ASSURANCE.CONTRACTS.1`, the consumer side in `OWNERSHIP.SERVICES.2`; in this unit `DECOMMISSION.3` to `.5` hold how a team retires its own forms and point to `SERVICES.2` for the consumer side ("see", not "realizes").

Forces of the branch: delivery continuity, reversibility, cost of ownership over time, confidence in past decisions, consumer predictability, cognitive load.

Certainty words: grounded = named sources support the decision; inferred = follows from them; open = what is missing is stated.

Realization reading: this branch carries out what OWNERSHIP and ASSURANCE decided; each node says which decision it carries out and does not restate it.

---

## EVOLUTION (L1)

Intent (sharpened): How the system and its decisions change over time, so that it keeps working and stays changeable at a cost the team can sustain.
Rolled-up decision: reasons for significant decisions are recorded where the code lives and are not rewritten, only superseded; change is made in steps that keep the system releasable, with every dual-support phase ended by a removal; debt is a known, inventoried liability repaid where code changes; obsolete forms are retired on stated grounds, in two announced stages, by an owner with a budget; the set of technologies stays small because each addition is a replacement. Roll-up of the five L2 records; it states no fact of its own (MD-03).
Certainty: grounded for the decision-record, expand-migrate-contract, two-stage deprecation and retirement mechanics (consensus rows); inferred for the debt-timing and technology-firmness conditions, which rest on single-source or contested rows.
Constraints: no significant decision without a record that outlives its author; no incompatible change without a removal step and an owner; no retirement without verified usage and a stated deadline; no technology added without the retirement of what it replaces or a stated reason none exists.
Links: realizes `OWNERSHIP.STANCE`, `SELECTION`, `LIFECYCLE`, `SERVICES`, `ASSURANCE.BEHAVIOUR`, `ASSURANCE.CONTRACTS`; see `CHANGE_FLOW.INTEGRATION`, `DATA_CHANGE`, `ROLLBACK`, `REVIEW`, `TRANSVERSE.PRIVACY`.
Flags: F8 (TECHNOLOGY.4) listed at the end; F1 to F7 settled by the final pass.

---

## EVOLUTION.DECISIONS (L2): Decision Records

Intent: How decisions and their reasons are recorded, kept and revisited, so that the motivation of past decisions is recoverable.
Rolled-up decision: a significant decision gets a short record, one decision per record, stored beside the code, stating forces, alternatives, the decision and the costs it accepts; an accepted record is superseded, not rewritten; each record has a status and an owner and is consulted in review; a separate proposal precedes the record only where many stakeholders deliberate.
Certainty: grounded (consensus across the architecture-record sources); inferred for the immutability-versus-living split and the proposal split.
Links: children `DECISIONS.1` to `.6`; realizes `OWNERSHIP.SELECTION.1` (the reason for a selection is stored as a record).

### EVOLUTION.DECISIONS.1 Content of a Record

Intent: A later reader can recover the reason and does not reopen the decision blindly.
Rows: L1001, L1002, L1009, L1233, L324.
1. Decision: A record states the forces at play (technical, political, social, project-local, written value-neutrally), the decision in the active voice, the serious alternatives with their pros and cons and why the rejected ones were rejected (dissent included), and the consequences, positive, negative and neutral, including the costs it accepts. All records share one fixed structure (title, context, decision, status, consequences). Outcome: a later reader can tell why it was decided, what would have to change to revisit it, and whether new information justifies reopening.
2. Grounds: L1001 (consensus; REG-1011, REG-1012, REG-154): motivation is among the hardest things to recover and its loss makes a team obey outdated decisions or reverse them blindly. L1002 (REG-1011, REG-1013, REG-1019, REG-1020, REG-1114): alternatives and dissent keep the same discussion from reopening without new information. L1233 (REG-154): one structure lowers reading cost. L1009 (inferred; REG-1019, REG-154): named forces make a change in them the revisit trigger. L324 (MAINT, REG-181): stating accepted costs gives a strong reason a concrete counterweight; it agrees with public practice and is the best form of the "consequences" part.
3. Positions: P1 record the reasons. P2 add alternatives, confidence and dissent. P3 fixed template. P4 name the forces. P5 MAINT: state the accepted costs.
4. Rejected: nothing is rejected: the five practices are parts of one record, each serving a distinct failure (lost reason, reopened argument, unreadable variety, unseen trigger, unweighed cost). A reason-only record without alternatives is best only for a decision with no real alternative, which `DECISIONS.2` already excludes from a record.
5. Context: none.
6. Certainty: grounded for P1 to P3 and P5; inferred for P4 (one origin, no source tests it).
7. Flags: none.
Constraints: a record states the decision and its reason; a record states the alternatives rejected and the costs accepted.
Links: realizes `OWNERSHIP.SELECTION.1` (L1001, L1002, L1009 see also L029).

### EVOLUTION.DECISIONS.2 Significance Threshold

Intent: Which decisions get their own record, so that records stay worth reading and writing.
Rows: L1004.
1. Decision: Write a record for an architecturally significant decision (structure, non-functional requirements, dependencies, interfaces, construction techniques) whose reason a later maintainer could not recover from an existing policy or standard: several options were weighed, or no existing basis supplied the answer. A decision a recorded policy settles points to the policy; a workaround or an experiment gets no record; a deliberate, temporary shortcut is recorded as a debt item (`DEBT.3`). Outcome: the records that exist are the ones a later reader would otherwise have to guess, and none is noise.
2. Grounds: L1004 (REG-1011, REG-1114, REG-154, REG-163 for the broad rule; REG-1012 for "no existing basis or options weighed"; REG-1028 for skipping workarounds). The two bars differ in how much they record, not in what they protect; the combined test keeps the protected cases and drops the cost where a policy already carries the reason.
3. Positions: P1 every architecturally significant decision, short records (confidence, onboarding; costs authoring time). P2 only when no basis exists or options were weighed (low overhead). P3 skip workarounds and experiments.
4. Rejected: P1 as stated: recording what a policy already carries restates its reason (MD-03); best only where the policy itself is not recorded where readers find it (reversibility is not part of the test: no row states it). P2 alone, for a small team with standards: kept as the baseline.
5. Context: none: with many contributors or a long life more decisions meet the test, since what is obvious to the team today is not to a newcomer; the test scales, no second bar is needed.
6. Certainty: inferred (the bar is the sources' two positions read as a floor and a ceiling; no source gives a numeric or structural threshold).
7. Flags: none.
Constraints: a significant decision with no policy basis, or with options weighed, has a record; a workaround, an experiment or a policy-backed decision does not.
Links: realizes `OWNERSHIP.SELECTION` (L1004 see also L029); `OWNERSHIP.SELECTION.1` is the dependency instance.

### EVOLUTION.DECISIONS.3 Form and Storage

Intent: A record is read, found and kept beside what it governs.
Rows: L1003.
1. Decision: Keep a record short (one or two pages), one decision per record, numbered monotonically with no number reused, in lightweight text markup written as prose to a future reader, and store it in version control in the repository of the code it governs; mirror to a wiki only for wider reach, with the repository as the source. Outcome: the record travels with the code, has history and can be found by anyone who reads the code.
2. Grounds: L1003 (consensus, no competitor; REG-1012, REG-1013, REG-1024, REG-1028, REG-1114, REG-154): proximity to the code and history are the properties that make a record survive.
3. Positions: P1 short, numbered, in the source repository.
4. Rejected: no competing practice recorded; a wiki as the source is best only where the records must be read and edited by people outside the repository, with the cost that it drifts from the code.
5. Context: none.
6. Certainty: grounded (consensus across six sources).
7. Flags: none.
Constraints: records live in the repository of what they govern; a number is never reused.
Links: used by `TECHNOLOGY.2` (the decision trail), `DECOMMISSION.2`.

### EVOLUTION.DECISIONS.4 Changing an Accepted Record

Intent: History stays honest and the current picture stays accurate when a decision changes.
Rows: L232, L1005.
1. Decision: An accepted decision record is not rewritten. A changed decision is a new record that supersedes the old one, which stays in place marked superseded, so history is never wrong, only superseded; only corrections that do not change the decision (a typo, a broken link) edit an accepted record. A document whose job is to describe the current state (how-to, reference) is living and is kept current by ownership and checks, not by this rule. Outcome: a reader can reconstruct what was decided when and why, and always see which record is current.
2. Grounds: L1005 a (REG-154, REG-163, REG-1011; consensus in WEB:ARCH-C38): a record is rationale at a moment, and history that is rewritten cannot be audited. L232 (REG-154): the two models are assigned per document type, immutable for rationale. The contrary evidence (REG-1028, "mutability has worked better for our teams") concerns documents readers use as the current truth, which is the living-document type, not a decision record; in version control history survives edits, so the cost of mutation is lower there, but the status stays machine-readable only when records are superseded (inferred, L1005 note).
3. Positions: P1 immutable log with supersession. P2 mutable living document with dated additions.
4. Rejected: P2 for decision records: loses the order of decisions and the status, best where the record is the only place readers look and a few people own it, which describes a how-to or reference document, assigned to `TRANSVERSE.DOCS`.
5. Context: DOCUMENT_TYPE (L232): rationale documents are immutable with supersession; how-to and reference documents are living.
6. Certainty: grounded for supersession (consensus on the rule, contested only on the alternative); the assignment per document type is inferred from L232.
7. Flags: none.
Constraints: an accepted record is never rewritten to change its decision; a superseded record carries a link to its successor.
Links: see `DECOMMISSION.2` (retirement is recorded and supersedes the adoption record); `TRANSVERSE.DOCS` for living documents.

### EVOLUTION.DECISIONS.5 Status, Ownership and Use in Review

Intent: Accepted decisions are actually applied.
Rows: L1006, L1007.
1. Decision: Give each record a status (proposed, accepted, rejected, superseded, deprecated), a named owner accountable for its upkeep, and a review before acceptance. During code and design review, consult the accepted records; a change that violates one is linked to it and either conforms or arrives with a new record that supersedes it. Outcome: a decision that was accepted is checked at the moment a change could break it.
2. Grounds: L1006 (consensus; REG-1011, REG-1013, REG-154): status, owner and review are the minimum for a record to be trusted. L1007 (one source, no dissent; REG-1011): a record nobody consults at review has no effect; it matches the review that binds of `ASSURANCE.RULES.4`.
3. Positions: P1 status, owner, review before acceptance. P2 consult records during review.
4. Rejected: none; the two are complementary and no source argues against either. A record without owner or status is best only for a throwaway note, which `DECISIONS.2` excludes.
5. Context: none.
6. Certainty: grounded for P1; inferred for P2 (one source, no dissent found).
7. Flags: none.
Constraints: every record has a status and a named owner; a change that contradicts an accepted record cites it.
Links: see `CHANGE_FLOW.REVIEW` (how the review is carried out), `ASSURANCE.RULES.4`.

### EVOLUTION.DECISIONS.6 Proposal Versus Record

Intent: Whether a decision with many stakeholders is prepared in a separate proposal or in the record itself.
Rows: L1008.
1. Decision: Where many stakeholders must be heard, prepare the decision in a proposal written before it is made (drawbacks, alternatives, unresolved questions, backward-compatibility section, a named decider) and keep the record to the outcome and its reason, linking the proposal. Where few stakeholders are involved, the lightweight record alone is the whole practice. Outcome: deliberation and outcome each reach the reader who needs them, and a small team does not pay for a process it does not need.
2. Grounds: L1008 (REG-1012, REG-1013, REG-1020; REG-154): the deliberation and the outcome serve different readers, and a record that grows into a discussion is no longer short. The row is the origin's synthesis of two open-source projects (inferred).
3. Positions: P1 separate proposal and record (many stakeholders). P2 one document serves both, as in a language-enhancement process (open projects, fewer artifacts). P3 lightweight record only (small teams).
4. Rejected: P2: best where the proposal itself is the permanent, versioned history and carries a final status, as in an open project with many contributors, because it avoids duplicating the reasoning; P3 for many stakeholders: loses the deliberation.
5. Context: STAKEHOLDER_COUNT (L1008): many stakeholders, proposal then record; small team, lightweight record.
6. Certainty: inferred (single origin synthesis; no source measures either).
7. Flags: none.
Constraints: a proposal names its decider; a decision made through a proposal links it from the record.
Links: see `DECISIONS.1`, `DECISIONS.5`.

---

## EVOLUTION.INCREMENTAL (L2): Incremental Change

Intent: How change is made in steps that keep the system working, including migrations and replacement.
Rolled-up decision: change in steps that keep the system releasable and teach early; run every incompatible change as expand, migrate, contract, with the contract step part of the change; replace a system piece by piece behind its interface, rewriting only under stated conditions; give a mass change an accountable owner with capacity; invest in changeability by expected lifespan and consumer count; apply new conventions forward only where the surface has many consumers.
Certainty: grounded for step size, expand-migrate-contract and mass-change mechanics; inferred for the rewrite conditions and the owner split.
Links: children `INCREMENTAL.1` to `.6`; realizes `OWNERSHIP.STANCE.4`, `OWNERSHIP.LIFECYCLE`, `ASSURANCE.CONTRACTS`.

### EVOLUTION.INCREMENTAL.1 Step Size and Feedback

Intent: A step stays small enough that the system is releasable and learning arrives early.
Rows: L1010, L1236.
1. Decision: Change in steps that keep the system releasable at every step, using an interface that supports both versions or an abstraction with two suppliers, rather than a long-lived branch or one switch-over; release each step and check its effect against the effect it was meant to have, because many presumed improvements do not move their metric. Outcome: the system is never held back by a half-finished change, and a wrong direction is found while it is cheap to reverse.
2. Grounds: L1010 (consensus; REG-1004, REG-105): releasable steps keep continuous integration and rollback possible. L1236 (majority; REG-034): about a third of presumed features improved their target metric, so build-to-learn is the evidence-backed use of a step; it is the same stance as `OWNERSHIP.STANCE.4` (do not build for presumed needs), carried to the unit of change.
3. Positions: P1 releasable steps. P2 short feedback beats up-front analysis.
4. Rejected: a long-lived branch or a single switch-over: see `INCREMENTAL.2` for when a switch-over is best. Skipping analysis entirely: not what P2 says; analysis proportional to the cost of being wrong stays (STANCE.4 on costly-to-reverse structures).
5. Context: none.
6. Certainty: grounded for P1; grounded for P2 on one source (REG-034).
7. Flags: none.
Constraints: every step leaves the system releasable; a step's intended effect is stated and checked after release.
Links: see `CHANGE_FLOW.INTEGRATION`, `CHANGE_FLOW.ROLLBACK`; realizes `OWNERSHIP.STANCE.4`.

### EVOLUTION.INCREMENTAL.2 Expand, Migrate, Contract

Intent: An incompatible interface or schema change is run so that both versions are supported only as long as needed.
Rows: L1011, L1012.
1. Decision: Run an incompatible change as expand, migrate, contract: first support old and new together (for a schema, deploy a form that supports both application versions, verify, then deploy the application that uses the new one), then move consumers, then remove the old form; the removal step belongs to the change (owner and capacity: `DECOMMISSION.1`), because supporting two versions is a recurring cost that ends only at removal; an unfinished migration is debt (`DEBT.1`, inventoried by `DEBT.3`). Outcome: rollback stays possible during the move and the old form does not become permanent.
2. Grounds: L1011 (consensus; REG-087, REG-1004, REG-105, REG-244): expand first keeps rollback. L1012 (inferred; REG-1030, REG-105): a migration without removal is debt, held in `DEBT.1`. The definition of what counts as breaking is `ASSURANCE.CONTRACTS.1`; the mechanics for stored data are `CHANGE_FLOW.DATA_CHANGE` (MD-03).
3. Positions: P1 expand, migrate, contract. P2 an unfinished migration is itself debt (held in `DEBT.1`).
4. Rejected: a single coordinated switch-over: best where one release unit contains every consumer and a short outage or lock is acceptable (the few-reachable-consumers case of `CONTRACTS.1`), at the price of no rollback during the switch.
5. Context: none beyond the consumer-reach context already decided in `CONTRACTS.1`.
6. Certainty: grounded for P1; inferred for P2.
7. Flags: none.
Constraints: the plan of an incompatible change names its removal step and owner (owner and capacity: `DECOMMISSION.1`).
Links: see `CHANGE_FLOW.DATA_CHANGE`, `CHANGE_FLOW.ROLLBACK`, `DEBT.1`; realizes `ASSURANCE.CONTRACTS.1`.

### EVOLUTION.INCREMENTAL.3 Replacement Versus Rewrite

Intent: Whether an adopted, home-grown or whole system is replaced piece by piece or all at once.
Rows: L039, L1017.
1. Decision: Replace a system incrementally while it keeps running, at seams and behind its existing interface (the strangler pattern). Rewrite in full only when the old platform is obsolete, the old system runs in parallel until the new one is proven, and the migration is slow and verified. A big-bang cut-over is not a practice. Outcome: users keep a working system, the hidden knowledge in the old behaviour is preserved, and the old system is not removed until the new one is shown equivalent.
2. Grounds: L039 and L1017 (REG-033, REG-1004 for incremental replacement; REG-1021 for refactor in place when behaviour is poorly specified; REG-1029 for rewrite when the platform is obsolete). The positions each win under a stated condition and the incremental form serves both continuity and replacement, at the cost of two systems in the interim (reversibility, delivery speed). The rewrite rule of thumb ("25 percent") is one unverified source and is not adopted. Fowler's strangler fig article (REG-033), fetched in the final pass, describes seams as "seams that we can insert into the system" and a transitional architecture whose cost "the reduced risk and earlier value from the gradual approach outweigh": a missing seam is a cost to pay, not a condition for a rewrite. WEB:ARCH-C42 states the incremental form as consensus; EVOL-C17 records it as contested against never-rewrite and rewrite.
3. Positions: P1 never rewrite, refactor in place. P2 rewrite when changing the old costs more than new. P3 incremental replacement, full rewrite only under stated conditions with parallel running. P4 big-bang wholesale rewrite (no source argues for it).
4. Rejected: P1 as an absolute: best when the system ships and its behaviour is poorly specified and no replacement need exists. P2 as a cost rule: best when the platform is obsolete and the old system keeps running in parallel; its threshold is unverified. P4: no source argues for it; best, inferred, only where the system is small, every consumer sits in one release unit, equivalence to the old behaviour is verified and a short outage is acceptable.
5. Context: none (the conditions for the rewrite exception are part of the decision).
6. Certainty: grounded for the positions; the conditions for a full rewrite are inferred, since the row records that it is open whether any position wins in general.
7. Flags: none.
Constraints: a replacement keeps the old system serving until the new one is verified against the old behaviour; a full rewrite carries a recorded reason that the platform is obsolete.
Links: see `OWNERSHIP.STANCE` (L038: carrying one's own code), `INCREMENTAL.1`, `DECOMMISSION`.

### EVOLUTION.INCREMENTAL.4 Mass Change and Migration Ownership

Intent: A change across many owners is split, owned and finished, so that it completes instead of stalling.
Rows: L1013, L1014.
1. Decision: Generate a mechanical change with tools, split it into independently testable and reviewable shards, and block the old pattern from reappearing; small single-owner code can change in one step. Give a migration across many consumers one accountable owner, usually the party that wants the change, and a finish condition (owner and capacity: `DECOMMISSION.1`); consumers migrate on their own only where the replacement is transformatively better, since an unfunded mandate stalls. Outcome: the change completes, the old pattern does not return, and consumers carry little of the load.
2. Grounds: L1013 (REG-1003): the largest atomic change shrinks as codebase and contributors grow, so mechanical sharding scales and review stays possible. L1014 (REG-1002, REG-1003): an unfunded mandate becomes organic migration that rarely completes. Accountability for completion is stated as an outcome (a named owner with capacity), not a rule about who writes code (MD-02). L058 and L052 of `OWNERSHIP.LIFECYCLE` carry the dependency-update analogue.
3. Positions: P1 generate, shard, block the old pattern. P2 central owner with staffed capacity. P3 consumers migrate themselves.
4. Rejected: P3 as default: autonomy, best when the replacement is transformatively better so consumers move unprompted. P2 for few consumers: capacity not needed where the consumers are few and reachable. One atomic change for a large codebase: best only for small single-owner code.
5. Context: CONSUMER_COUNT_AND_OWNER_COUNT (L1013, L1014): a large shared codebase or many consumers needs the sharded, owned form; few owners and few consumers change in one step.
6. Certainty: grounded for P1 and P2 (REG-1002, REG-1003, T2 practice); the context boundary is inferred.
7. Flags: none.
Constraints: a migration has a named owner and a finish condition; the old pattern is blocked by a check once the migration is done (owner and capacity: `DECOMMISSION.1`).
Links: realizes `OWNERSHIP.LIFECYCLE`; see `CHANGE_FLOW.INTEGRATION`, `DECOMMISSION.5`.

### EVOLUTION.INCREMENTAL.5 Lifespan, Consumers and Cost of Change

Intent: How much changeability to invest in, given how long the system lives and how many depend on it.
Rows: L1015, L1016.
1. Decision: Treat the life of a system as a series of changes it must absorb, and set the investment in changeability by its expected lifespan. Expect the cost of change and removal to grow with the number of consumers, because they depend on observable behaviour; so that the owners of shared infrastructure can change it without tracking each consumer, by the mechanism of `ASSURANCE.CONTRACTS.2`. Outcome: changeability is bought where the life and the reach justify it, and change does not silently break dependants.
2. Grounds: L1015 (consensus; REG-1014): lifespan is the multiplier on every maintainability cost; it is the same stance as `OWNERSHIP.STANCE.4`. L1016 (consensus; REG-1002, REG-1014): the more consumers, the more behaviours are relied on (Hyrum's Law, `ASSURANCE.CONTRACTS.1`), and capturing that reliance in tests is the mechanism of `CONTRACTS.2`.
3. Positions: P1 lifespan decides the investment. P2 cost of change grows with consumers; counter with reliance tests in CI (mechanism in `CONTRACTS.2`).
4. Rejected: none; the two are not rivals. Fixed investment regardless of lifespan: best for neither a throwaway nor a decades-long system.
5. Context: none (lifespan and consumer count are the inputs, not a condition on the rule).
6. Certainty: grounded (consensus); the figure REG-1031 was not read from the original and is not used.
7. Flags: none.
Constraints: the expected lifespan and the consumers of a shared interface are stated where the investment is decided.
Links: realizes `OWNERSHIP.STANCE.4`, `OWNERSHIP.LIFECYCLE`, `OWNERSHIP.SELECTION`, `ASSURANCE.CONTRACTS.1` and `.2`.

### EVOLUTION.INCREMENTAL.6 Conventions Applied Forward Only

Intent: A new convention reaches existing objects without forced churn.
Rows: L296.
1. Decision: Apply a new convention to new objects and do not rename existing ones where the surface has many consumers; mark a deprecated item where its consumers and their tools see it: in machine-readable metadata of the item (`DECOMMISSION.3`), and in its name only where renaming it breaks no consumer; keep it with documented deprecation and its relationships through the transition, and remove it by a later planned change. Where the surface has few, reachable consumers and the rename is mechanical and verified by tests, rename in one coordinated change so the convention is not split permanently. Outcome: consistency is bought at the lowest cost to consumers.
2. Grounds: L296 (MAINT, REG-181; majority in public practice): forward-only serves cost and reversibility, and wins with many consumers; its own alternative, retroactive rename, serves consistency at a cost of risk. The few-consumer exception follows from settled `ASSURANCE.CONTRACTS.1` (few, in-house, reachable consumers: a breaking change is coordinated and deployed together) and from `INCREMENTAL.4`; it extends the maintainer's practice, it does not go against it; no row states it (inferred). `CONTRACTS.1` classes a rename as breaking, which is why the name carries the deprecation mark only where no consumer breaks.
3. Positions: P1 MAINT: forward only, deprecated items marked and removed later. P2 retroactive rename.
4. Rejected: P2 for a surface with many consumers: risk without a matching gain; best where consumers are few, reachable and the change is tool-made and tested.
5. Context: CONSUMER_COUNT (L296): many consumers, forward only; few reachable consumers, a coordinated rename is acceptable.
6. Certainty: grounded for forward-only (maintainer practice agreeing with public practice); the few-consumer exception is inferred.
7. Flags: none.
Constraints: a deprecated item is marked where its consumers and their tools see it (machine-readable metadata; in its name only where renaming it breaks no consumer) and remains until its planned removal.
Links: see `DECOMMISSION.3`, `INCREMENTAL.4`.

---

## EVOLUTION.DEBT (L2): Technical Debt and Refactoring

Intent: What counts as debt, when to take and repay it, and how to refactor.
Rolled-up decision: debt is anything that makes future change more costly, wider than code quality, and it is inventoried; speed is not bought with debt except knowingly, for short-lived or exploratory work; debt is made visible by engineers' reports with tools as support; refactoring runs in small behaviour-preserving steps; repayment is timed by where code changes, with explicit capacity for debt no change touches.
Certainty: grounded for the definition and the refactoring step size; inferred for the speed-versus-quality payoff and the repayment timing (contested or single-source rows).
Links: children `DEBT.1` to `.5`; realizes `OWNERSHIP.STANCE`, `OWNERSHIP.LIFECYCLE`, `ASSURANCE.BEHAVIOUR`.

### EVOLUTION.DEBT.1 What Counts as Debt

Intent: What the term covers, so that the right things are inventoried and weighed.
Rows: L1018, L1021.
1. Decision: Count as debt any design or implementation choice, or unfinished piece of work, that makes future change more costly or impossible, whether taken knowingly or not. The inventory is wider than code quality: it includes design trade-offs not visible in code metrics, unfinished migrations, missing or stale documentation, missing tests, dead code, out-of-date dependencies, concentrated team expertise and a weak release process. Outcome: debt that hurts change is weighed even when no tool shows it.
2. Grounds: L1018 (consensus; REG-1001, REG-1005, REG-1006): the core definition, a contingent liability on maintainability and evolvability. L1021 (REG-1006, REG-1025, REG-1030): the most significant debt comes from design trade-offs not visible in code metrics. Both state one idea at two widths; the wider one serves the purpose, which is to decide what gets inventoried and weighed.
3. Positions: P1 debt limited to internal qualities (maintainability, evolvability). P2 debt wider than code, inventory migrations, documentation, tests, dead code, dependencies, expertise, release process.
4. Rejected: P1 as the whole definition: best where the aim is only to talk about code structure; it omits debt that code metrics cannot see.
5. Context: none.
6. Certainty: grounded for the definition; the full list is inferred (secondary source for the breadth).
7. Flags: none.
Constraints: an unfinished migration and an out-of-date dependency are debt items when they raise the cost of change.
Links: see `CHANGE_FLOW.DATA_CHANGE`, `INCREMENTAL.2`, `OWNERSHIP.LIFECYCLE.5`.

### EVOLUTION.DEBT.2 Taking Debt Versus Investing in Quality

Intent: Speed is bought with debt knowingly or not at all.
Rows: L1020, L1207, L1237, L1231.
1. Decision: Invest in internal quality from the start for anything that will be changed, because the payoff of good design arrives in weeks, not months, and does not trade against speed beyond the smallest scope. Take debt deliberately only for a short-lived or exploratory deliverable, knowingly (prudent, not reckless), record it, and repay it as `DEBT.5` sets, or drop it with the deliverable. Keep the system simple: keep interfaces minimal and modular and release in small steps; deleting code is held in `DECOMMISSION.1`. Outcome: debt is a recorded choice with a repayment, not an accident, and quality is not sacrificed for speed that does not materialise.
2. Grounds: L1020 and L1207 (REG-1001, REG-1005, REG-1007, REG-1120, REG-1121): contested (a little debt speeds delivery if repaid promptly; quality pays back in weeks); the author of the payoff claim states there is no objective proof, so the decision is conditional on the lifetime of the work, not a universal. L1237 (REG-1130): deliberate debt is taken knowingly; the sibling holds the prudent/reckless quadrant. Repayment is timed by where the code changes (REG-1130 and REG-1001, fetched in review: interest is paid only when working in the area), which is `DEBT.5`. L1231 (REG-1132): simplicity is a reliability property; carried here as minimal interfaces, with deletion in `DECOMMISSION.1` and small releases in `INCREMENTAL.1`. L308 (MAINT, `OWNERSHIP.STANCE.1`) states the cost-of-lasting-liability stance the node realizes.
3. Positions: P1 a little debt speeds development if repaid promptly (short-lived or exploratory). P2 quality is not a trade-off (anything that will be changed). P3 prudent versus reckless; deliberate only knowingly. P4 simplicity as reliability.
4. Rejected: P1 as a general policy: best for a short-lived or exploratory deliverable, which is the condition kept. Treating quality as a universal, free good: the payoff point is unproven, so a throwaway may rightly skip it.
5. Context: SCOPE_AND_LIFETIME (L1020): a short-lived or exploratory deliverable may take recorded debt; anything that will be changed invests in quality from the start.
6. Certainty: inferred (contested source claim, payoff point unproven); grounded for the knowing-and-recorded rule.
7. Flags: none.
Constraints: deliberate debt is recorded as an inventory item (`DEBT.3`), repaid as `DEBT.5` sets, or dropped with the deliverable; a deliverable that outlives its stated short life is re-judged as a lasting one.
Links: realizes `OWNERSHIP.STANCE` (L1231 see also L308); see `DEBT.3`, `DECOMMISSION.1`, `INCREMENTAL.1`.

### EVOLUTION.DEBT.3 Finding and Inventorying Debt

Intent: Debt is made visible so that repayment is chosen with evidence.
Rows: L1022, L1023, L1027.
1. Decision: Keep an inventory of debt items, each with cause, consequence, affected artefact and impact, and manage it by recognising, analysing, monitoring and measuring. Because no validated automatic metric predicts where debt hinders (L1022), a periodic survey of engineers (what hinders them, deliberate debt, investment in reduction) is the main signal of where debt hurts; use tools (smells, coupling, dependency analysis) and the measurable maintainability signals (searchability, time to change code in another team's area, duplicate and unused code, version consistency, length of the dependency upgrade cycle) as trend tracking and for specific smells. The inventory is one list kept where the team plans its work, so repayment competes with features in the same plan (`DECOMMISSION.1`, `DEBT.5`); a marker in the code carries only the item's id as a pointer; a decision record holds a debt item only where the debt came from a recorded decision. Outcome: repayment is chosen from evidence of cost, and design debt that tools miss is still found.
2. Grounds: L1022 (REG-1006, REG-1025, REG-1030): tools are cheap and track trends but miss design debt; a survey is valid where no metric predicts hindrance, costing subjectivity and survey fatigue. L1023 (REG-1006, REG-1027, REG-1028, REG-1030; inferred): the item fields and management loop. L1027 (REG-1015; single source): measurable maintainability signals, whose upgrade-cycle length is the debt-side view of `OWNERSHIP.LIFECYCLE.3` and `.5`. Placement of the inventory: the node's purpose is repayment chosen with evidence and planned; the marker's force (proximity to the code) is kept by the pointer and the record's by the link, so nothing either serves is lost: not a genuine trade-off, and "where the team plans its work" avoids naming a tool (inferred).
3. Positions: P1 tool-detected smells. P2 survey of engineers. P3 inventory with item fields, in tracker, in-code marker or decision record. P4 measurable maintainability.
4. Rejected: P1 as the primary signal: misses design debt, validity limited; best as the supplement. P2 alone: subjective and fatiguing, therefore paired with measured trends.
5. Context: where a validated metric exists for a kind of debt, it replaces the survey for that kind (L1022's condition).
6. Certainty: inferred for the survey primacy (T4 summary of an unread paper), for the item fields and for the placement of the inventory; grounded for tool limits.
7. Flags: none.
Constraints: every deliberate debt item and every unfinished migration appears in the inventory.
Links: realizes `OWNERSHIP.LIFECYCLE` (L1027 see also L052); see `CHANGE_FLOW.MEASURE`.

### EVOLUTION.DEBT.4 Refactoring Step Size

Intent: A refactoring step is small enough that the system is never broken for long.
Rows: L1024.
1. Decision: Refactor only in small steps that preserve behaviour, with the checks green after each, so the system is never left broken for more than minutes of work; behaviour not pinned by tests is pinned first, as `ASSURANCE.BEHAVIOUR.5` requires. A larger rearrangement is restructuring and runs as an incremental change with its own controls (`INCREMENTAL.1`, `INCREMENTAL.3`). Outcome: a refactoring can be stopped or reverted at any step and behaviour never changes unnoticed.
2. Grounds: L1024 (consensus, single practice; REG-1008, REG-1009): small, behaviour-preserving steps are the definition of the practice. The check that detects a behaviour change is `ASSURANCE.BEHAVIOUR`; characterization before change is `BEHAVIOUR.5` (L107).
3. Positions: P1 small behaviour-preserving steps.
4. Rejected: a large unverified rearrangement called refactoring: not a refactoring; best treated as a restructuring with its own staging.
5. Context: none.
6. Certainty: grounded (consensus, two sources).
7. Flags: none.
Constraints: each refactoring step leaves the checks green; a refactoring never changes observable behaviour.
Links: realizes `ASSURANCE.BEHAVIOUR.5` (and `.1`); see `CHANGE_FLOW.REVIEW`.

### EVOLUTION.DEBT.5 Timing and Responsibility of Repayment

Intent: Debt is repaid where it pays and is not crowded out.
Rows: L1019, L1025, L1026.
1. Decision: Repay maintainability debt where code is changed, because interest accrues only there: tidy before a change when tidying plus the change costs less than the change alone, tidy after, later or never otherwise, and never in code that will not change again; leave crufty but stable areas alone. Refactor opportunistically, as ordinary work, by whoever touches the code, where tests are strong and ownership is shared; give structural debt that spans teams, so that no one touches it in passing, explicit capacity or a programme with an owner. A tidy lands as its own change, before or after the behaviour change, as `CHANGE_FLOW.REVIEW.2` decides. Outcome: repayment effort goes where it reduces the cost of the next change, and cross-team debt is not left to feature pressure.
2. Grounds: L1019 (REG-1001, REG-1006): interest only where changed. L1025 (majority; REG-1008, REG-1010): the cost comparison is grounded for its options and for "never", inferred for the inequality. L1026 (REG-1008; REG-1015, REG-1030 secondary): opportunistic wins when tests are strong and ownership shared; explicit capacity wins when debt is cross-team (Fowler allows a day or two for a gnarly lump).
3. Positions: P1 interest where changed. P2 time tidying by cost comparison. P3 opportunistic only. P4 opportunistic plus explicit capacity.
4. Rejected: P3 alone for cross-team debt: nobody touches it in passing; best when tests are strong and ownership shared. A standing "debt sprint" for all debt: not argued by any source; best only as the explicit capacity for structural debt.
5. Context: OWNERSHIP_OF_CODE_AND_TEST_STRENGTH (L1026): strong tests and shared ownership, opportunistic; cross-team debt, explicit capacity.
6. Certainty: inferred (single-author source for most of it; the inequality is unproven).
7. Flags: none (F2 closed by `CHANGE_FLOW.REVIEW.2`).
Constraints: maintainability debt in code that will not change again is not repaid (its interest is paid only when the code changes); debt that carries risk (code left on production, vulnerable or end-of-life dependencies) is not governed by this rule and follows `DECOMMISSION.1` and `OWNERSHIP.LIFECYCLE.3` and `.5`; cross-team debt has a named owner and capacity.
Links: see `CHANGE_FLOW.REVIEW.2` (separate refactoring changes, decided there); `INCREMENTAL.4`.

---

## EVOLUTION.DECOMMISSION (L2): Decommissioning

Intent: How code, interfaces and systems are deprecated, switched off and removed.
Rolled-up decision: removal is planned engineering work with an owner and a budget; a retirement is decided on stated grounds and recorded; it is announced in two stages (deprecation, then sunset) with machine-readable, actionable warnings; the support window is published by tier where consumers are many; a retirement has a deadline unless the replacement sells itself; it is executed by verifying use, restricting reversibly, then removing everything attached.
Certainty: grounded for the staging, the announcement and the execution checklist (consensus); inferred for the owner-and-budget synthesis and the window context.
Links: children `DECOMMISSION.1` to `.6`; realizes `OWNERSHIP.STANCE`, `OWNERSHIP.SERVICES`, `ASSURANCE.CONTRACTS`.

### EVOLUTION.DECOMMISSION.1 Why Remove

Intent: Removal is treated as engineering work, so that obsolete code and systems do not linger.
Rows: L1028, L1029, L1041.
1. Decision: Treat code as a liability whose value lies in the functionality it provides, so aim for more functionality per unit of code and remove what is obsolete. Removal and migration work is ordinary engineering work with a named owner and capacity in the plan, planned alongside features, not what is left over after them; without them it stalls (REG-1002). Do not leave on a production system code that is no longer meant to be used; remove it, so that it cannot be activated by accident. Outcome: obsolete code and systems leave the production estate as a planned activity, and unused code is not a hidden risk.
2. Grounds: L1028 (consensus; REG-1002): a liability view that matches `OWNERSHIP.STANCE.1`. L1029 (one T1 case; REG-1017): a regulator found missing controls against activating retired code a contributing failure in an incident that lost over 460 million dollars in 45 minutes; that removal prevents the whole class is inferred. L1041 (majority, inferred synthesis; REG-1002, REG-1003, REG-1006, REG-1008, REG-1021): owner and budget are what stop removal from being left over.
3. Positions: P1 code is a liability. P2 do not leave retired code on production systems. P3 removal is ordinary work with owner and budget.
4. Rejected: removal as leftover work done when capacity allows: best never; it is what stalls. Keeping dormant code for possible reuse: best only where a recorded reuse is planned, with an owner.
5. Context: none.
6. Certainty: grounded for P1 and P2's case; P3 is inferred (no source states it as one rule).
7. Flags: none.
Constraints: removal and migration work has a named owner and capacity in the plan; code not intended to run on production is removed from it.
Links: realizes `OWNERSHIP.STANCE` (L1028 see also L037, L001); see `CHANGE_FLOW.DEPLOY` (L1029 see also L166).

### EVOLUTION.DECOMMISSION.2 Grounds to Retire

Intent: On what grounds a retirement is decided, and how the decision is kept.
Rows: L1037.
1. Decision: Retire on stated grounds: a replacement of comparable or better function exists, the upkeep cost exceeds the value, the technology is out of date, the strategy has changed, or use is low. Record the retirement as a decision record that supersedes the adoption record. Outcome: a retirement has a reason that can be checked and that a later reader finds.
2. Grounds: L1037 (consensus for the grounds; REG-1002, REG-1011, REG-1026, REG-154); the five grounds are grounded, and recording the retirement as a record is inferred from the record practice of `DECISIONS.1` to `.4`.
3. Positions: P1 retire on stated grounds and record it.
4. Rejected: retirement by neglect or by the departure of the maintainer: no stated ground; best never, since consumers cannot plan.
5. Context: none.
6. Certainty: grounded for the grounds; inferred for the record.
7. Flags: none.
Constraints: a retirement names its ground and is recorded.
Links: see `DECISIONS.4`.

### EVOLUTION.DECOMMISSION.3 Announcing Retirement

Intent: Retirement is signalled to consumers so that remaining users are found and warned without fatigue.
Rows: L1030, L1032.
1. Decision: When the team retires an interface or form it offers, announce it in two stages with distinct signals: deprecation (no longer recommended, still working) and sunset (stops at a stated time), with the sunset never earlier than the deprecation. Make warnings actionable and relevant, since excess causes alert fatigue, and expose them in machine-readable form (a response warning, an audit annotation, a usage metric labelled with the removal version) so that remaining users are found. Outcome: every consumer can learn the state and the date by machine, and the owner can see who is still using the form.
2. Grounds: L1030 (consensus; REG-1026, REG-182, REG-183): the two-stage principle is neutral; for HTTP interfaces the Deprecation and Sunset header fields carry the two signals (stack pointer). L1032 (consensus; REG-008, REG-1002): the machine-readable forms named are Kubernetes and HTTP specific (stack pointer), and the principle is neutral. The consumer side, reading these signals and routing them to an alert, is decided in `OWNERSHIP.SERVICES.2`; what counts as a breaking change is `ASSURANCE.CONTRACTS.1`.
3. Positions: P1 two stages. P2 actionable, relevant, machine-readable warnings.
4. Rejected: a single "removed in a future release" notice: best only for an internal item with one reachable consumer, who is told directly.
5. Context: none.
6. Certainty: grounded for both (consensus).
7. Flags: none.
Constraints: sunset is not earlier than deprecation; a deprecation is visible to a machine as well as a reader.
Links: realizes `ASSURANCE.CONTRACTS.1`; see `OWNERSHIP.SERVICES.2`, `INCREMENTAL.6`.
Stack pointers: L1030 HTTP header fields; L1032 Kubernetes and HTTP forms.

### EVOLUTION.DECOMMISSION.4 Support Window Before Removal

Intent: A retired form stays supported long enough for consumers to plan and no longer.
Rows: L1031.
1. Decision: Where consumers are many or external, publish a support policy by stability tier with fixed minimum windows: a stable interface is deprecated but not removed within a major version, a pre-release one has a fixed period, an experimental one may go at any release, and the minor-release rule before removal in a major is `ASSURANCE.CONTRACTS.1`. Where consumers are few and known, set the window case by case with them. An infrastructure-like API with a large consumer base and the funds to carry old behaviour is held as an indefinitely compatible, date-pinned surface, which has no window: that case is held in `ASSURANCE.CONTRACTS.1` (L353 b). Outcome: consumers can plan from a published rule, and maintainers do not carry old forms without limit.
2. Grounds: L1031 (REG-008, REG-030): predictability for consumers, at the cost of carrying old forms; consistent with `ASSURANCE.CONTRACTS.1` (deprecation through at least one minor release before removal in a major, for many or independent consumers). The concrete durations (nine months or three releases) are one project's numbers (stack pointer) and are not adopted as defaults.
3. Positions: P1 tiered fixed windows in a published policy. P2 case by case.
4. Rejected: P2 for many external consumers: they cannot plan; best with few known consumers, where a conversation is faster than a policy.
5. Context: CONSUMER_COUNT (L1031): many external consumers, a published tiered window; few known consumers, case by case.
6. Certainty: grounded for the tiered policy (REG-008, REG-030); the numbers are one project's, not general.
7. Flags: none.
Constraints: a published window states, per tier, how long a deprecated form stays; no removal before the stated window.
Links: realizes `ASSURANCE.CONTRACTS.1` (policies by consumer reach and artifact kind, the indefinitely compatible case included); see `OWNERSHIP.SERVICES.2`.

### EVOLUTION.DECOMMISSION.5 Advisory or Compulsory Deprecation

Intent: Whether retirement is left to consumers' choice or forced by deadline, so that it completes at an acceptable load.
Rows: L1033.
1. Decision: When the old form is to be removed, make the retirement compulsory: a firm deadline (owner and capacity: `DECOMMISSION.1`), so the deprecation stage of `DECOMMISSION.3` ends in a sunset. Advisory deprecation without a deadline is right only when the replacement sells itself or the old form is cheap to carry and no removal is intended. Outcome: a retirement that is meant to happen does happen, at a known load on consumers.
2. Grounds: L1033 (REG-1002): advisory deprecation rarely completes unless the replacement is transformatively better; a compulsory one completes and removes the cost, at the risk of an unfunded mandate, which the owner and capacity of `INCREMENTAL.4` answer.
3. Positions: P1 advisory, no deadline. P2 compulsory, firm deadline plus a staffed migration team.
4. Rejected: P1 as the default for a removal: autonomy and no central load, but the form stays; best when the replacement is transformatively better.
5. Context: none (the condition for advisory is part of the decision).
6. Certainty: grounded (one T2 source, consistent with the other incremental rows).
7. Flags: none.
Constraints: a compulsory retirement has a firm deadline (owner and capacity: `DECOMMISSION.1`).
Links: see `OWNERSHIP.SERVICES.2`, `INCREMENTAL.4`, `DECOMMISSION.3`.

### EVOLUTION.DECOMMISSION.6 Carrying Out the Retirement

Intent: A retirement is executed so that nothing still used is cut off and nothing attached is left behind.
Rows: L1034, L1035, L1036.
1. Decision: Before switching off, verify who or what still uses the system, restrict access reversibly for a period to flush out remaining users (controlled blackouts and restrictive controls with a way back), keep restorable backups and recorded metadata per the retention rules, neither shorter nor longer (`OPERATION.RECOVERY.2`, `TRANSVERSE.PRIVACY.2`; erased data in a backup: `TRANSVERSE.PRIVACY.3`), then remove. Removal is the owner's primary objective, with measurable intermediate milestones (for example deleting key sub-components; owner and capacity: `DECOMMISSION.1`). Remove everything attached: licences, attached storage, DNS entries, domain membership, and entries in configuration, monitoring, automation and security tooling; check against compliance requirements. Outcome: nothing used is cut off, nothing attached is left behind and the retirement can be undone until it is final.
2. Grounds: L1034 (consensus; REG-1018, REG-1026), L1035 (single source; REG-1002), L1036 (single source; REG-1018). The three are steps of one process: check use, finish with an owner, leave nothing attached.
3. Positions: P1 verify use, restrict reversibly, keep backups, then remove. P2 explicit owner with milestones. P3 cover everything attached.
4. Rejected: an abrupt switch-off: best never for a system with possible users; an immediate removal is best only for something provably unused.
5. Context: none.
6. Certainty: grounded for P1; P2 and P3 are single-source consensus.
7. Flags: none.
Constraints: usage is verified before switch-off; a retirement lists and removes its attachments; backups kept after retirement follow the retention rules, neither shorter nor longer (owner and capacity: `DECOMMISSION.1`).
Links: see `OPERATION.RECOVERY.2`, `TRANSVERSE.PRIVACY.2` and `.3` (retention and erasure), `CHANGE_FLOW.DATA_CHANGE`, `ASSURANCE.DATA_INTEGRITY`.

---

## EVOLUTION.TECHNOLOGY (L2): Keeping Technologies Few

Intent: How the set of technologies in use is kept small and its standing positions recorded.
Rolled-up decision: a technology is added as a replacement with the retirement of what it replaces planned; the team keeps a shared register of technologies in use with a status and a decision trail; how firmly the set is held follows how much platform and on-call is shared; one mature general-purpose store serves several roles until a stated need exceeds it.
Certainty: grounded for the replacement rule and the register; inferred for the firmness conditions and the store rule.
Links: children `TECHNOLOGY.1` to `.4`; realizes `OWNERSHIP.SELECTION`, `OWNERSHIP.STANCE`.

### EVOLUTION.TECHNOLOGY.1 Adding as Replacing

Intent: A new technology replaces an older one, so that the long-term cost of an extra system is not accumulated.
Rows: L026, L1038, L1229.
1. Decision: Hold the number of different tools solving the same problem down: introduce a new technology as a replacement, with the retirement of the older one planned and owned, because the long-term cost of keeping an extra system reliable exceeds the convenience of building with it. Prefer a few tools that cover the whole domain, so shared platform work benefits all. How firmly this holds follows `TECHNOLOGY.3`: for few, independently operated components, fit to the problem counts as the stated need that allows adding alongside. Outcome: the count of technologies does not grow by default.
2. Grounds: L026 and L1038 (majority, same normative claim; REG-013, REG-1002, REG-1022); L1229 (majority; REG-1022): shared platform work scales with few tools. It carries out, at the level of the whole estate, the entry rule of `OWNERSHIP.SELECTION.2` (novelty spent only where the existing tool cannot solve the need, with an exit or migration plan); this node holds the replacement commitment, that rule holds the entry test (MD-03).
3. Positions: P1 hold the number of tools per problem down; plan migration. P2 add as replacement, plan retirement. P3 few tools covering the domain.
4. Rejected: adding alongside: best only where the new technology serves a problem the present ones cannot, which `SELECTION.2` requires to be documented.
5. Context: see `TECHNOLOGY.3`.
6. Certainty: grounded (majority, three sources).
7. Flags: none.
Constraints: introducing a technology records what it replaces, or why it replaces nothing, and the retirement owner.
Links: realizes `OWNERSHIP.SELECTION` (L1038, L1229); see `TECHNOLOGY.3`, `DECOMMISSION.2`.

### EVOLUTION.TECHNOLOGY.2 Standing Position per Technology

Intent: The team's stance on each technology is shared and recorded, so that it knows what to standardise on, evaluate and stop using.
Rows: L1039.
1. Decision: Keep a shared register of the technologies in use, each with a position (standard, being evaluated, held for retirement) and a decision trail linking its record. Where the organisation has capacity for experiments, use the four-ring vocabulary (adopt, trial, assess, hold); a small or operations-heavy team keeps the register without the evaluation rings. The register holds technologies (languages, frameworks, stores, platforms) and the team's position on each. It is neither the sanctioned list of admitted dependencies (`OWNERSHIP.SELECTION.1`, the gate) nor the inventory of what is deployed (`OWNERSHIP.LIFECYCLE.5`): position, admission and presence are three facts, each held once. Outcome: anyone can see what the team standardises on, tries and is moving away from, and why.
2. Grounds: L1039 (majority; REG-015, REG-1024): grounded for the rings, inferred for the decision trail. The scale of the practice follows `OWNERSHIP.SELECTION.2`, which keeps standing rings as the way novelty is run where the capacity exists, not as a default for every team.
3. Positions: P1 an explicit shared position per technology with a decision trail.
4. Rejected: standing rings for every team: best where capacity for experiments and tolerance for churn exist (`SELECTION.2`); an implicit, unrecorded stance: best never, since newcomers cannot tell what is standard.
5. Context: EXPERIMENT_CAPACITY (from `OWNERSHIP.SELECTION.2`): rings only where there is capacity.
6. Certainty: grounded for the register; inferred for the trail.
7. Flags: none.
Constraints: each technology in use has a position and a link to its record.
Links: realizes `OWNERSHIP.SELECTION` (L1039 see also L025, L024); see `DECISIONS.3`, `OWNERSHIP.SELECTION.1`, `OWNERSHIP.LIFECYCLE.5`.

### EVOLUTION.TECHNOLOGY.3 How Firmly the Stack Is Held

Intent: How strongly the set of technologies is imposed, trading local fit against shared cost.
Rows: L1040.
1. Decision: Hold the set as firmly as the cost of a departure is shared. Wherever a platform or on-call is shared, keep a supported default set: a departure whose whole operating cost stays with the team that chose it is permitted and unsupported (paved path); a departure whose cost would land on the shared platform or on-call needs a recorded decision naming who carries it (mandate). Where components run independently and nothing is shared, choose per component by fit within the default of `OWNERSHIP.SELECTION.2`. Outcome: the cost of an extra technology is carried by whoever chooses it.
2. Grounds: L1040 (contested; REG-106, REG-013 for the mandate; REG-1023 for the paved path; REG-1016 for polyglot): each wins under a stated condition. The three positions of L1040 differ on one variable, who carries the operating cost, which the row names as the force; the shared platform and on-call are what turns a local choice into a shared cost. The "between the two" condition, stated by no source, is dropped.
3. Positions: P1 mandate a small set (cognitive load, upgrade cost, shared operations; costs local fit). P2 paved path, departures unsupported (autonomy with a cheap default; a tail of unsupported variants). P3 polyglot freedom per component (local fit, learning; heterogeneity).
4. Rejected: P1 for a departure whose cost stays with its team; P2 for a departure that would land on a shared on-call; P3 for a shared platform.
5. Context: where the operating cost of a departure lands (L1040).
6. Certainty: inferred (contested row).
7. Flags: none.
Constraints: a departure from the default set whose operating cost would land on the shared platform or on-call has a recorded decision naming who carries it.
Links: see `TECHNOLOGY.1`; version choice for each dependency is `OWNERSHIP.LIFECYCLE.2`, one version of each shared component is `CHANGE_FLOW.INTEGRATION.1`; realizes `OWNERSHIP.SELECTION`.

### EVOLUTION.TECHNOLOGY.4 One General-Purpose Store for Several Roles

Intent: One mature data store serves several roles until its limits are reached, so that the number of systems stays small.
Rows: L1232.
1. Decision: Prefer one mature general-purpose data store for queue, cache, search and documents while it meets the need now with headroom, and add a specialised system when a stated requirement (sub-millisecond cache, large-scale search relevance, scale) exceeds what the store delivers, shown by measurement or by a documented limit of the store, not by the team's expectation. Outcome: fewer systems to operate, and each added system has a measured reason.
2. Grounds: L1232 (contested; REG-1126 T1; REG-1128, REG-1129 T4, one with commercial interest): fewer systems mean fewer failure points and less context switching; the T1 source documents the limits of the one store for queue-like use and says it is not for general-purpose work. It is the data-store case of `OWNERSHIP.STANCE.4` (no building for presumed needs) and of `TECHNOLOGY.1`. The headroom figure of the proponent (about ten times) is one source's and is not adopted.
3. Positions: P1 one general-purpose store until limits are reached. P2 specialised system from the start.
4. Rejected: P2 as a default: adds systems on a prediction; best where a stated requirement is known at the start to exceed the general store (sub-millisecond cache, large-scale search).
5. Context: LOAD_AND_TEAM_SIZE (L1232): applies for a small team and modest load; with a known requirement beyond the store, the specialised system is the best from the start.
6. Certainty: inferred (no T1 or T2 source states the rule; limits not verified from primary sources).
7. Flags: F8.
Constraints: a specialised store is added with the requirement it meets and the measurement or documented limit showing the general store falls short.
Links: realizes `OWNERSHIP.STANCE.4`, `OWNERSHIP.SELECTION`; see `TECHNOLOGY.1`.
Stack pointers: origin stack was PostgreSQL, restated stack-neutral by the ledger; boundary DATA.

---

## Flags still open (1)

- F8 (TECHNOLOGY.4): contested row resting on one-project or commercially interested sources; no final-pass resolution addressed it. Its residual on TECHNOLOGY.3 is settled (R26); the one-version rule has its home in `CHANGE_FLOW.INTEGRATION.1`, pointed to from `TECHNOLOGY.3`.

## Settled decisions disagreed with

None.

## Review applied

Review fixes applied: 13 of 13. Flag findings R14 to R26 were acted on in the final pass (section `Final pass applied`).

- R01 applied: "hard to reverse" dropped from the DECISIONS.2 test (noted as not in any row); constraint rewritten to match the decision.
- R02 applied: the P2 "variant" clause deleted from DECISIONS.6 Rejected.
- R03 applied: INCREMENTAL.1 points to INCREMENTAL.2 for when a switch-over is best.
- R04 applied: unfinished-migration-as-debt kept in DEBT.1 and DEBT.3; INCREMENTAL.2 keeps removal step and owner and points to DEBT.1.
- R05 applied: INCREMENTAL.3 states the inferred condition under which P4 is best.
- R06 applied: INCREMENTAL.5 keeps the outcome and points to CONTRACTS.2 for the mechanism.
- R07 applied: DEBT.2 constraint now points to the inventory item (DEBT.3) and repayment as DEBT.5 sets it.
- R08 applied: DEBT.4 points to BEHAVIOUR.5 for pinning behaviour.
- R09 applied: DEBT.5 rule scoped to maintainability debt; risk-carrying debt follows DECOMMISSION.1 and LIFECYCLE.3 and .5.
- R10 applied: DEBT.5 adds "a tidy lands as its own change" (CHANGE_FLOW.REVIEW.2); link changed; F2 closed.
- R11 applied: DECOMMISSION.4 cites CONTRACTS.1 for the minor-release rule.
- R12 applied: TECHNOLOGY.3 rejection of multiple versions deleted; pointers to LIFECYCLE.2 and CHANGE_FLOW.INTEGRATION.1; F8 reduced to its residual.
- R13 applied: TECHNOLOGY.4 reads "by measurement or by a documented limit of the store".

---

## Final pass applied

Resolutions (final_pass/resolutions.md, J8_evolution section):

- R14 (DECISIONS.2): applied: decision, Context "none: ...", Rejected P1 replaced; constraint unchanged; certainty inferred.
- R15 (INCREMENTAL.6): applied: deprecation mark placed where consumers and tools see it; constraint likewise; grounds cite CONTRACTS.1 (rename is breaking).
- R16 (INCREMENTAL.6, F5): applied: text unchanged, grounds replaced by the settled CONTRACTS.1 and INCREMENTAL.4 derivation; F5 removed.
- R17 (INCREMENTAL.3, F6): applied: "or no seam exists" dropped from decision and constraint; REG-033 grounds added; F6 removed.
- R18 (INCREMENTAL.2, .4, DECOMMISSION.1, .5, .6): applied: DECOMMISSION.1 holds the principle (owner and capacity in the plan, REG-1002); the four others keep their own content, point to it, and each constraint ends "(owner and capacity: DECOMMISSION.1)" (DECOMMISSION.1's own constraint is the holder and carries no suffix).
- R19 (DEBT.2): applied: "repay it as DEBT.5 sets, or drop it with the deliverable"; REG-1130 and REG-1001 grounds added.
- R20 (DEBT.3): applied: survey sentence reopened with "Because no validated automatic metric ..."; Context set; certainty unchanged.
- R21 (DEBT.3, F1): applied: Undecided paragraph removed, decision clause and grounds added; certainty inferred; F1 removed.
- R22 (DECOMMISSION.4, .3, .5 links): applied via X7 (below).
- R23 (DECOMMISSION.6, F3): applied via X8 (below); F3 removed.
- R24 (TECHNOLOGY.1): applied: firmness sentence added; Context "see TECHNOLOGY.3".
- R25 (TECHNOLOGY.2): applied: register-scope sentence added; links to SELECTION.1 and LIFECYCLE.5 added.
- R26 (TECHNOLOGY.3, F8 residual): applied: decision, Context, Rejected, grounds replaced; certainty inferred. One consequent edit, not worded in the resolution: the Constraint, which required a recorded decision for any departure, now reads "a departure ... whose operating cost would land on the shared platform or on-call has a recorded decision naming who carries it", so it no longer contradicts the paved-path sentence.
- Judge flags closed by the review (F2, F4, F7): confirmed; F4 and F7 removed from DEBT.2 and DECOMMISSION.4 Flags (F2 was already closed).
- Not applied: none.

Cross-unit lines (cross_unit_fixes.md):

- X7: applied (J8 part): DECOMMISSION.4 points to CONTRACTS.1 for the indefinitely compatible case; DECOMMISSION.3, .4, .5 link to OWNERSHIP.SERVICES.2 as "see", not "realizes"; header note updated (X7 supersedes X3).
- X8: applied (J8 part): DECOMMISSION.6 reads "per the retention rules, neither shorter nor longer" and points to OPERATION.RECOVERY.2, TRANSVERSE.PRIVACY.2 and .3.
- X1 to X6, X9 to X14: not for this unit (Units column does not name J8).

Maintainer point (J2 only): not applicable. Point 18 of maintainer_points.md (INCREMENTAL.6) restates R15, already applied.

Nodes added: none.

Flags still open: F8 on TECHNOLOGY.4 (contested row, commercially interested sources); no resolution addressed it.

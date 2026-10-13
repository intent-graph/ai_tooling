# Judged records: unit J3_assurance_integrity

Nodes: 19 (3 L2 roll-ups, 16 L3), in tree order: ASSURANCE.DATA_INTEGRITY (.1-.5), ASSURANCE.DOCS_SYNC (.1-.4), ASSURANCE.SECURITY (.1-.7).
Binding: MD-01 (best, not average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-06 (flags go to the Opus pass).
Maintainer ruling on documentation (verbatim, binds DOCS_SYNC): "how do we make sure that doc is always up to date ... What remains true is that we must have process, review rules, ci/cd that make sure doc is in sync". The question "design-first or code-first" is ruled the wrong question and is not decided here.
Rows are cited by ledger id, sources by register id (REG). MAINT rows (REG-181) are not citable and weigh as a strong position.
Decisions marked undecided: none.
Settled decisions disagreed with: none.

Cross-unit links (not re-decided here): ASSURANCE.RULES.3 (gates that cannot be skipped), ASSURANCE.RULES.5 (one bar and evidence), ASSURANCE.BEHAVIOUR.2 and .6 (static layer, adequacy), ASSURANCE.CONTRACTS.3 (one source of description), ASSURANCE.AVAILABILITY.4 (proving restore) belong to J2 and J4; their verdicts are not yet written, so each link states only what this unit needs from them.

---

## ASSURANCE.DATA_INTEGRITY Data Integrity Under Change

Intent: which mechanism guarantees stored data stays valid and in sync through change, including the checks during a data change.
Decision (rolled up): integrity that must hold whatever writes the data is enforced where every write path converges; a change that can widen scope or destroy data states its scope explicitly and is recoverable by a tested restore; derived data has a sync plan with detection before it exists; a new structure or invariant is checked against the old and brought into force observe-first when known violators exist. Outcome: stored data is valid and in step after any change, including a mistaken one.
Certainty: inferred (a roll-up of five decisions: grounded cores, with inferred parts in .1, .2 and .3; no source states the set as a whole).
Flags: none.
Links: CHANGE_FLOW.DATA_CHANGE holds the procedures (batching, rehearsal), this node holds which mechanism guarantees (MD-03); OPERATION.RECOVERY holds backup practice.

### ASSURANCE.DATA_INTEGRITY.1 Where Integrity Rules Live

Intent: which tier enforces the rules that must hold whatever writes the data.
1. Decision: Rules that must hold whichever code writes (keys, NOT NULL, foreign keys, row-local checks, atomic audit) are declared in the store, in addition to validation at the edge; rules that change with product decisions (workflow, policy) live in the application. Constraints are named explicitly and the application maps a violation to a stable contract error. Outcome: an invalid state cannot be written by a migration, an administrative tool, an ad-hoc statement or a second application.
2. Grounds: the maintainer's reason is a fact about paths, not taste: migrations, administrative tools and ad-hoc statements bypass application code (L279, REG-181); the split by kind keeps the application where rules change (L1262, REG-1139, REG-1140, REG-1143); constraint semantics are grounded, the mirror and naming advice inferred (L1286, REG-1139). The maintainer position and the split agree on the core (declared constraints); the split adds only where product policy goes. A declarative constraint is checked by the engine on every write path and cannot be forgotten by one of them; a procedural mechanism can be disabled, mis-ordered or bypassed by bulk paths; so the least powerful form that expresses a cross-writer rule wins.
3. Positions: P1 invariants in the application domain layer (force: cognitive load, one place for logic). P2 integrity at the store, maintainer (force: correctness across writers). P3 split by kind (force: correctness without freezing policy in the store). P4 constraints as the contract half, named and mirrored (force: stable errors).
4. Rejected: P1 as sole location: the best when a single application owns the store (L279), a condition that rarely holds because migrations and ad-hoc access exist. P2 stated without the split: pushes workflow and policy into the store where they change at product speed.
5. Context: a single application owning the store (L279) moves the best toward application-layer invariants.
6. Certainty: grounded for the core (L279, L1286 semantics); inferred for the split of the middle zone (L1262 is recorded inferred and contested).
7. Flags: none.
Constraints: MUST declare in the store every invariant that must hold across writers; MUST name constraints (inferred); MUST validate at the edge as well; MUST NOT put policy that changes with product decisions in the store.
Links: Requires CONSTRUCTION.BOUNDARY (edge validation); index to CHANGE_FLOW.DATA_CHANGE.

### ASSURANCE.DATA_INTEGRITY.2 Guarding Bulk and Destructive Operations

Intent: how an operation whose scope can silently widen is stopped from doing so.
1. Decision: Scope is stated, never inferred. A destructive or bulk operation of unbounded scope requires an explicit opt-in from its caller plus validation of mandatory keys, key order and timestamp sanity; a schema change is linted in CI against a list of unsafe operations and passes only with an explicit assertion that overrides the rule. Outcome: omitting a filter or running an unsafe migration cannot silently widen the effect.
2. Grounds: the maintainer rule (L280, REG-181) and the migration lint (L396, L414, REG-258, REG-259) apply one principle at two layers (application operations, schema operations); L414 records the lint as the nearest public form of L280, inferred.
3. Positions: P1 explicit opt-in flag (force: correctness against a slip). P2 migration lint with explicit override (force: blocks DDL that locks or destroys; cost: tool niche, T3).
4. Rejected: none competes; they cover different operations. Applying only P2 leaves application-level bulk operations unguarded (best only where no application issues bulk writes).
5. Context: none.
6. Certainty: grounded for each (L280, L396); inferred that they are one principle (L414).
7. Flags: none.
Constraints: MUST require the opt-in at the operation's interface, not in documentation; MUST record an override as an explicit, reviewable assertion in the change.
Links: Refines ASSURANCE.RULES.3 (a gate with an explicit, visible override); CHANGE_FLOW.DATA_CHANGE.

### ASSURANCE.DATA_INTEGRITY.3 Layered Protection and Deletion Form

Intent: which layers protect data against destructive change, and in which form data is deleted so that recovery and integrity both hold.
1. Decision: Defend in layers because every single strategy eventually fails: a first layer that makes deletion reversible for a stated retention window, after which the kept copy is purged (periods for personal data: TRANSVERSE.PRIVACY.2), a second of backups kept and erased as OPERATION.RECOVERY.2 and TRANSVERSE.PRIVACY.3 set, a third of early detection of corruption. A destructive change (drop, delete, truncate) is treated as not reversible by script: its undo is a restore that was prepared and tested before the change ran. Where recovery or audit of deleted records is needed, delete the row and write a copy to an archive in the same transaction; keep a deleted flag on the row only when undelete is a user-facing feature and its costs are paid (every query excludes deleted rows by default, children of a deleted parent are handled explicitly, a legally required purge remains possible). Outcome: a mistaken or malicious destruction is recoverable within a stated window without breaking referential integrity.
2. Grounds: layers and tested restore are consensus and grounded (L417, L416, L388, L1092; REG-250, REG-251, REG-252, REG-1051). REG-250 (T2) states soft deletion as the primary defence against developer error, with a window of 15 to 60 days: that is the case for the layer, reversibility for a window, which both forms give. The form is chosen on referential integrity and query safety: a flag puts a predicate in every query and stops foreign keys protecting parent and child (L1255, REG-1145, T3), an archive keeps the live table clean and its keys working (L1256, REG-1142, REG-1145).
3. Positions: P1 layers (force: survival of any single failure). P2 destructive = restore, tested (force: honest reversibility). P3 soft deletion or retention window first (force: cheap recovery). P4 soft-deletion costs. P5 hard delete plus same-transaction archive.
4. Rejected: soft deletion as the default form: best when undelete is a product feature (the mitigation of a view or default scope for the predicate is inferred, no row states it). Retention-window reversibility through backups alone: best when deleted rows have no audit value and point-in-time restore is fast enough for the stated window.
5. Context: need for undelete as a feature, or a legal purge obligation (shortens the window or forbids retaining the copy); both move the form, not the layering.
6. Certainty: layer grounded (T2, consensus rows L416, L1092); form inferred.
7. Flags: none.
Constraints: MUST test the restore before a destructive change runs; MUST state the retention window; MUST keep a legally required purge possible.
Links: index to OPERATION.RECOVERY (backup practice); see OPERATION.RECOVERY.2 (how long backups are kept), TRANSVERSE.PRIVACY.2 (retention periods for personal data, backup copies included) and TRANSVERSE.PRIVACY.3 (erasure in backups); Requires ASSURANCE.AVAILABILITY.4 (proving restore); Requires TRANSVERSE (privacy and retention); see DATA_INTEGRITY.5 (third layer, detection).

### ASSURANCE.DATA_INTEGRITY.4 Derived Data Sync and Staleness

Intent: how derived or denormalized data is kept in step with its source and its divergence found.
1. Decision: No derived or denormalized data exists without a synchronisation plan, chosen from a ladder by cost and strength (documentation only, declared constraints, detection queries, scheduled refresh, same-transaction triggers) by the impact of divergence, change frequency and tolerable staleness. The plan answers up front: what, sync level, freshness target, change frequency, impact of divergence, how drift is found and fixed, what alerts. Detection queries run on a schedule set by importance with a stated action on divergence; timestamps for staleness detection and monitoring hooks exist before first production use, and "no invalidation" and "no monitoring" are defects. Outcome: divergence is bounded, found, and fixed by a known action.
2. Grounds: the maintainer ladder (L281, L282, L314; REG-181), L282 and L314 agree with public practice (reconciliation jobs); L281 extends it. Same-transaction versus eventual is a context question, not a rival: always-consistent serves correctness at write latency and coupling; eventual with a stated window serves delivery speed and cost.
3. Positions: P1 ladder (force: proportion). P2 always consistent. P3 eventual with window. P4 scheduled detection. P5 staleness as designed property.
4. Rejected: P2 as universal: best when divergence is costly and writes are few. P3 as universal: best when divergence is cheap and the window is stated and monitored. A plan stated after the data exists: always rejected, since the cost of retrofitting detection is highest then.
5. Context: impact of divergence, change frequency, tolerable staleness (L281: wins by criticality and change rate).
6. Certainty: grounded (single maintainer source, practice agrees).
7. Flags: none.
Constraints: MUST write the plan before the data exists; MUST state the freshness target and the alert; MUST NOT treat "eventual" as unstated.
Links: Requires OPERATION.TELEMETRY.8 (Scheduled Work Signals: duration, failure, backlog, missed runs; L313 sits there); index to CHANGE_FLOW.DATA_CHANGE.

### ASSURANCE.DATA_INTEGRITY.5 Checking Old Against New and Rolling Out Checks

Intent: how a new structure or a new invariant is verified against the old one and brought into force without breaking production.
1. Decision: Before the old structure is removed, the new data is validated against the old (side-by-side read comparison with an alert on mismatch where reads are cut over; out-of-band validation jobs independent of application logic). Conventions are self-auditing: each rule ships with a query or script that finds its violations. A new invariant check is enforced immediately when no known violator exists; when known violators exist in production it first runs observe-only (records findings, autofix is a dry run, nothing raises), and is enforced once the open defects are removed. with an owner (inferred, no row states it) and an exit condition (L284: enforce after open defects are removed). Outcome: a migration or new rule cannot corrupt or block production unseen.
2. Grounds: validation against old and out-of-band jobs (L391, L415; REG-250, REG-257, REG-260, one T3 for shadow reads); self-auditing conventions (L283, REG-181); observe-first (L284, REG-181), agreeing with shadow mode and feature flags. Immediate enforcement (P4) serves correctness and wins when nothing known would trip it.
3. Positions: P1 shadow read. P2 validate old against new, continuous jobs. P3 self-auditing conventions. P4 enforce at once (correctness). P5 observe-only first (reversibility, delivery speed).
4. Rejected: P4 when known violators exist: it blocks production on defects the team knows about. Observe-only without an owner or exit: the maintainer records that a kill-switch defaulting to observe tolerates defects and is not the fix; best never.
5. Context: existence of known violators in production (moves P4 to P5).
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST give observe-only mode an exit condition (L284) and an owner (inferred); MUST NOT remove the old structure before validation passes.
Links: Requires CHANGE_FLOW.DATA_CHANGE (rehearsal, rollout); see DATA_INTEGRITY.3 (detection layer).

---

## ASSURANCE.DOCS_SYNC Documentation in Sync

Intent: which mechanism keeps documentation true to the system: same-change delivery, gates, owners, executable examples, link checks.
Decision (rolled up), following the maintainer ruling that sync is guaranteed by process, review rules and CI/CD: documentation cannot drift because (a) a fact has one origin and derived forms are generated or checked, (b) documentation travels with the change it describes, (c) a change that needs documentation cannot merge, or ship, without it, with a recorded waiver as the only exception, (d) machines check what they can (examples, references, links, missing edits) and a reviewer verifies accuracy, which machines cannot, (e) every hand-written document has an owner and a dated verification. Outcome: no released behaviour lacks its documentation; accuracy is verified by review, and the residual risk (semantic drift in hand-written text) is owned and scheduled for review. Design-first versus code-first is not a decision here: the origin of each fact is chosen per fact, and only the guarantee is fixed.
Certainty: inferred (the ordering of mechanisms by strength is this judge's synthesis; each part is grounded).
Flags: none.
Links: TRANSVERSE.DOCS holds authoring and organisation (MD-03); ASSURANCE.CONTRACTS.3 holds one source of description for interfaces; ASSURANCE.RULES.3, .5.

### ASSURANCE.DOCS_SYNC.1 Delivery with the Change

Intent: where and when documentation travels relative to the change it describes.
1. Decision: Documentation is plain text in version control, in the repository of the thing it documents, changed through the same review and CI as code. A change that alters documented behaviour carries its documentation in the same merge request. Where documentation ships only with a release (release trains, many contributors, a docs team working in parallel), it may travel in a separate request, and the release gate in DOCS_SYNC.2 then blocks the release of a feature without it. A documentation-only change runs a reduced pipeline so that updating documentation is cheap. Outcome: no window in time between a change and its documentation (accuracy is verified by DOCS_SYNC.2 and .4, not by delivery alone).
2. Grounds: docs as code, consensus (L210; REG-150, REG-153, REG-156); same-request delivery leaves no window of disagreement (L211; REG-148, REG-150, REG-153); reuse of the existing workflow (L230; REG-150, REG-156); reduced pipeline lowers the cost of upkeep (L238; REG-153, motivation inferred).
3. Positions: P1 docs as code. P2 same request (correctness, confidence). P3 separate request on a release branch (control, delivery speed for code). P4 reuse developer workflow. P5 reduced pipeline.
4. Rejected: P3 as default: best when a release train and a docs team make same-request delivery impractical, provided the release gate holds. A parallel documentation process outside the tracker, review and CI: best never; it removes the mechanisms that guarantee sync.
5. Context: continuously deployed product (same request, no gate at release) versus release train (separate request, gate at release). This is the single condition a row shows moving the answer.
6. Certainty: grounded for P1, P2, P4; inferred for P5 motivation.
7. Flags: none.
Constraints: MUST keep documentation in version control beside the code; MUST NOT run a reduced pipeline over checks that execute documentation examples or verify references.
Links: Requires DOCS_SYNC.2; index TRANSVERSE.DOCS.

### ASSURANCE.DOCS_SYNC.2 Gates and Review of Documentation

Intent: which changes need documentation, who checks it, and whether a missing document blocks the change or the release.
1. Decision: The team states which changes require documentation (user- or admin-visible features, interface changes, changed workflows, deprecation and removal; internal-only exempt). Every change declares its documentation impact (updated, or not needed and why), a CI rule fails the merge when the declared trigger is met and no documentation path changed, and review verifies accuracy and that docs of deleted or deprecated code are removed. A waiver is an explicit declaration in the change (documentation deferred, with a follow-up issue opened at once and assigned to author and reviewer), granted by the reviewer who approves the change, independent of its author (RULES.4); it is never a skipped check, and the CI rule passes on that declaration as on an override assertion (DATA_INTEGRITY.2). Accuracy review is blocking and done by someone able to verify it; audience and writing review are non-blocking by default and blocking for customer-facing or cross-boundary documentation. Where documentation ships on a release train, the release gate removes a feature without documentation from the release. Documentation paths map to owners and owner review is required by branch protection where the platform supports it. Outcome: a change that needs documentation does not merge or ship without it, or without a tracked and owned exception.
2. Grounds: the maintainer ruling requires a mechanism that guarantees, not goodwill. The only mechanism that does not rely on goodwill is a blocking gate (L214, REG-153, REG-156), but a path rule detects the absence of an edit, not its accuracy (L226, REG-161), so the gate is paired with reviewer verification (L212, REG-151, REG-153) and a recorded waiver with follow-up issue takes the place of a silent skip (waiver: L214 position (b), REG-153; L239, REG-150, REG-153, grounds only the follow-up issue when documentation merges without the required reviewer); trigger definition (L213, REG-150, REG-151, REG-153); owners (L227, REG-145); who reviews what (L228, REG-150, REG-153); release gate (L237, REG-148). A gate with a recorded, independently granted override is the pattern of RULES.3 and DATA_INTEGRITY.2, not a blend: the soft gate (P4) leaves the outcome to whoever gives way, the waiver records who granted it and why.
3. Positions: P1 trigger. P2 review includes docs check. P3 hard merge gate (correctness, confidence). P4 encouraged and reviewer-enforced with waiver (delivery speed, team load). P5 release gate. P6 follow-up issue. P7 code owners. P8 three kinds of review.
4. Rejected: P4 as the whole policy: it is advisory, so drift passes whenever a reviewer or a deadline gives way; best only where documentation is not part of the product contract and the follow-up is reliably tracked. P5 as the only gate: late, it lets the merge and the docs diverge for the length of a release cycle; best when release trains make merge-time gates impractical, as an addition to the merge check. Writers approving every change: best only for customer-facing or cross-boundary documents (L228).
5. Context: documentation as user-facing contract or regulated (blocking audience review); release train (release gate added).
6. Certainty: grounded for each component; inferred for the combination (declared documentation impact checked by CI plus reviewer verification is this judge's synthesis from L213, L214, L226, L212, L239, and from the maintainer ruling; sources are split on hard versus soft gate, GitLab encourages).
7. Flags: none.
Constraints: MUST define the trigger; MUST make the waiver a visible recorded exception; MUST NOT let a check that only detects absence stand in for accuracy review.
Links: Requires ASSURANCE.RULES.3, ASSURANCE.RULES.4; see DOCS_SYNC.4 (mechanical checks), TRANSVERSE.DOCS.

### ASSURANCE.DOCS_SYNC.3 Ownership, Freshness and Single Source

Intent: who answers for a document, how its truth is dated and checked, and how one explanation per topic is kept.
1. Decision: Each fact has one canonical origin and is stated once; competing copies are consolidated into it. A derived or generated document is read-only and is never copied back into its source; an expanded copy written into a registry that resolves references is not allowed to shadow its source. Every hand-written document has a named owner, carries a date and what it was verified against ("verified live on a date"), is reviewed on a schedule tracked as a bug, and is removed or marked obsolete when it no longer serves a purpose. Fast-moving topics point to the more current tracker; open known violations are recorded with status and mitigation, and a mitigation is never presented as a fix. Outcome: a reader can tell who answers for a document, how old its verification is, and which copy is true.
2. Grounds: owner (L215, REG-150); freshness dates and review as tracked bugs (L216, L217; REG-150, REG-154); dated verification, maintainer (L319, REG-181, agrees with L216 on dating); one canonical document per topic (L218, REG-150); derived is read-only (L320, REG-181). One origin per fact is also MD-03 applied to documentation.
3. Positions: P1 owner. P2 freshness dates, bug-tracked. P3 live-verified stamps, maintainer. P4 one canonical document. P5 derived is read-only.
4. Rejected: dates as a guarantee of truth: a date states when someone last verified, not that the text is true; best never as the only mechanism, which is why DOCS_SYNC.2 and .4 exist. A copy for convenience that is edited by hand: best never.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST name an owner per document; MUST state the verification date and target; MUST NOT edit a generated document or copy it back into its source.
Links: Requires ASSURANCE.CONTRACTS.3 (one source for interface descriptions); OPERATION.RECOVERY (upkeep of recovery plan and runbooks sits there, L1111); index TRANSVERSE.DOCS.

### ASSURANCE.DOCS_SYNC.4 Mechanical Documentation Checks

Intent: which documentation properties are checked by machine so that drift fails a build rather than rotting silently.
1. Decision: CI executes the code examples in documentation, fails the documentation build on warnings and unresolved references, checks links on every change and on a schedule, and runs rules for review chores (changelog entry present when source changed, documentation touched when interface files changed) that comment or fail. Editorial style is a CI rule only when many authors need consistency without reviewer effort; clarity and audience stay with human review. Outcome: breakage a machine can see (a failing example, a dead reference, a dead link, a missing edit) fails a build; semantic drift is left to the reviewer gate in DOCS_SYNC.2, and this node does not claim to catch it.
2. Grounds: executed examples (L219; REG-143, REG-144; cost: exact-output fragility); build fails on warnings (L223, REG-146); links on schedule because external links break without a commit (L224, REG-146, REG-159; reason inferred); chores as rules with the stated limit that path rules detect absence, not inaccuracy (L226, REG-161); style lint serves consistency not correctness (L225, REG-149, REG-150).
3. Positions: P1 executed examples. P2 fail on warnings. P3 link checks. P4 style as failing CI (consistency, many authors). P5 human writing review (quality, high stakes). P6 chore automation.
4. Rejected: P4 as a sync mechanism: it does not test truth; best only with many authors. P5 as the only check on examples and references: best never, since machines do these cheaply and without goodwill.
5. Context: number of authors (style lint); otherwise none.
6. Certainty: grounded for capabilities; inferred for the reasons marked above.
7. Flags: none.
Constraints: MUST keep executed examples readable; MUST run link checks on a schedule as well as on change.
Links: Requires DOCS_SYNC.2 (accuracy review); stack pointers: doctest and rustdoc (examples), Sphinx (build flags), lychee (links), Vale (style), Danger (chores).

---

## ASSURANCE.SECURITY Security

Intent: which verification and enforcement mechanism, at which stage, guarantees security: design review, analysis, tests, scanning, enforced limits on automation.
Decision (rolled up): verification depth is set per application from its risk and written down; each check runs at the earliest stage it can, high-confidence low-noise checks block with an audited waiver and the rest advise; every change passes a floor of security testing whoever wrote it; consumed code and secrets are verified like own code; limits on automation and data access are enforced in tooling, not by instruction; and verification is itself verified. Outcome: security properties are checked on every change at a depth proportioned to risk, and a failed check or a bypass is visible.
Certainty: inferred (roll-up; components grounded; the period of penetration testing open).
Flags: none.
Links: TRANSVERSE.SECURITY holds programme practice (MD-03); ASSURANCE.RULES.3, .5; ASSURANCE.ARTIFACT.

### ASSURANCE.SECURITY.1 Verification Depth and Design Review

Intent: how deep security verification goes for each application and when its design is reviewed.
1. Decision: Verification depth is set per application from its risk profile and the assurance target is written down and revisited when risk changes (new personal data, new regulatory scope). The design is reviewed for security, by a qualified person or by automated processes against the risk model, before implementation proceeds, and the threat-model output selects test cases and the code that gets focused review. Outcome: the effort spent on security matches the risk and the design was reviewed before it was built.
2. Grounds: depth by risk (L1119; REG-1078, REG-1083, REG-1084); written target and revisit (L1122; revisit trigger inferred); design review (L243, REG-004, single source); threat model drives tests and review (L1128, REG-1086); floor is a lower bar to be tailored (L1127, REG-1086).
3. Positions: P1 design review. P2 depth by risk. P3 floor is not best practice. P4 threat-model output selects tests.
4. Rejected: uniform depth for all applications: best never as a policy (under-protects the risky, over-spends on the rest). The floor treated as the target: best only as the minimum for low-risk applications (see SECURITY.3).
5. Context: application risk profile is the variable; it sets depth by definition and is not a separate condition.
6. Certainty: grounded for P2, P3, P4; grounded single source for P1; inferred for the revisit trigger.
7. Flags: none.
Constraints: MUST record the assurance target; MUST review the design before implementation proceeds.
Links: Requires TRANSVERSE.SECURITY (risk model, programme).

### ASSURANCE.SECURITY.2 Stage Placement and Blocking Policy

Intent: at which pipeline stage each security check runs and whether its finding blocks the change.
1. Decision: A recorded policy states, per stage and risk, which checks run and who reviews findings; each check runs at the earliest stage it can (secrets and lint before commit; static, composition and infrastructure scanning at build; dynamic and interactive testing against a running instance; compliance audit after deployment). Whether a finding blocks or advises follows ASSURANCE.RULES.1: a check blocks only while its measured false-positive rate is within the false-alarm budget the team states for it; the one published operating figure is about 10 percent of findings judged not useful, one organisation's (REG-052). A block carries an audited waiver whose categories are recorded; who may waive a block is configured explicitly, since on common platforms anyone with write access can bypass by default (REG-170). For public-facing or regulated software, confirmed exploitable findings above a severity also block at release. Findings are triaged in the normal workflow and tool findings are reviewed by a human who remediates. Outcome: a check that developers trust cannot be bypassed silently, and a noisy check does not erode trust in the others.
2. Grounds: earliest-stage placement (L245; REG-004, REG-169; tool mapping inferred); blocking policy: block on a curated high-confidence set and advise on the rest, which wins when noise is nonzero, almost always (L246, L1131; REG-052, REG-1086, REG-1092), the rule itself held in ASSURANCE.RULES.1; push protection blocks and audited bypass keeps control and speed (L246; REG-170, REG-179); release-time block (L1131, REG-1094); policy decided, not left (L244, REG-004).
3. Positions: P1 policy per stage and risk. P2 earliest stage. P3 blocking gate (security, confidence). P4 advisory (adoption, trust). P5 block with audited waiver. P6 release block on exploitable findings. P7 leave to the team (team cognitive load, costs consistency).
4. Rejected: P3 for every check: erodes trust when noisy; best for high-confidence low-noise checks and regulated contexts. P4 for every check: nothing is guaranteed; best for noisy analyses. P7: loses consistency; best only where one team owns the whole pipeline and still records its policy.
5. Context: noise of the check (moves block/advise); public-facing or regulated (adds release block).
6. Certainty: grounded for positions; inferred for the synthesis; the threshold that makes a check blockable is the team's stated budget (RULES.1), settled.
7. Flags: none.
Constraints: MUST record the policy and the waiver rule; MUST NOT make a check blocking before developers trust its output.
Links: Requires ASSURANCE.RULES.1 (block or advise, under a false-alarm budget), RULES.2 (placement), RULES.3 (gates that cannot be skipped); Realize: CHANGE_FLOW.BUILD.

### ASSURANCE.SECURITY.3 Verification Techniques

Intent: which kinds of test and manual testing are used to find vulnerabilities and to verify security requirements.
1. Decision: Every change passes a floor of security verification whoever produced it, on the assumption that code may carry vulnerabilities: functional tests of the security features themselves in a sandboxed environment where appropriate, tests of the secure default configuration, a static scan, a search for hardcoded secrets, tests derived from specifications, threats and past bugs, builds and test runs that enable the checks and protections the language, compiler and runtime provide, and fuzzing of components that parse untrusted input (pre-release at minimum, continuous where practical); a web interface adds a dynamic or interactive scan against a running instance. Automated testing is combined with manual expert testing, directed first at the highest-risk components, with regular penetration testing where criticality or regulation is high (L1126, fuller programmes). Penetration testing of a high-risk component is triggered by a significant change to its attack surface and repeated on a recorded cycle; no source read gives a period (open). Outcome: a baseline of verification holds on every change, and manual depth goes where the risk is.
2. Grounds: test the security features and use sandbox (L247, REG-004); secure default tested (L248, REG-004); built-in checks and protections (REG-1086, NIST IR 8397: "Run the program with built-in checks and protections (2.5)"); every change, author-neutral (L1055; REG-1035, REG-1044, REG-1048); floor (L1126; REG-1081, REG-1086, REG-1094); fuzz (L1133; REG-1086, REG-1092); web scan (L1134; REG-1086, REG-1094, REG-169); automated plus manual (L1136; REG-1081, REG-1091); manual at highest risk first (L1137, inferred; no frequency given).
3. Positions: P1 test executable code. P2 secure default. P3 test every change. P4 developer floor against fuller programmes. P5 fuzz. P6 dynamic scan if web. P7 automated plus manual. P8 manual at highest risk first.
4. Rejected: the fuller programme (application-specific automation, regular penetration tests) for all applications: best under high criticality or regulation (L1126, SAMM levels 2 and 3). A structural-coverage target stated as a security requirement: this node states no coverage figure; ASSURANCE.BEHAVIOUR.6 decides it (no coverage floor, security-relevant code included; a conformance minimum only where a mandated baseline requires it). Dynamic scan for non-web software: not applicable.
5. Context: criticality or regulation (fuller programme); web interface (dynamic scan); input-parsing components (fuzzing).
6. Certainty: grounded for the floor and the techniques; inferred for the manual-testing sequence and the penetration-test trigger; open: no source gives a penetration-test period, and none supports "as the practice matures" as a trigger.
7. Flags: none.
Constraints: MUST apply the floor to every change; MUST test the default configuration.
Links: Requires ASSURANCE.BEHAVIOUR.3 (levels); see ASSURANCE.BEHAVIOUR.6 (adequacy, the coverage decision); see SECURITY.1 (depth), SECURITY.4.

### ASSURANCE.SECURITY.4 Static and Scheduled Analysis Practice

Intent: when static and slow dynamic analyses run and how their blind spots and noise are handled.
1. Decision: Static analysis runs as soon as code is written and repeats automatically per commit or in code review, so no new weakness goes unreported; an analysis too slow for that (whole-system analysis, sanitizers, run-time assertions) runs on a schedule, nightly or at least daily. Because static analysis has blind spots and false positives, the team standardises on tools, keeps a must-fix list, triages and suppresses deliberately, and uses more than one analyser where weakness classes differ. Outcome: fast checks give feedback within the change and slow checks still run on every day's code, with noise controlled.
2. Grounds: per commit or in review (L1129, REG-052); scheduled slow runs (L1129, L1135; REG-1092, REG-1094); blind spots and noise (L1130; REG-1086, REG-1092). The same sources hold P1 and P2 for different tool speeds, so cost of the analysis is the condition, not a contest.
3. Positions: P1 per change (speed of feedback). P2 nightly or daily (cost of ownership). P3 noise handling.
4. Rejected: running slow analyses on every change: best when the analysis is cheap enough to give feedback inside the change. Per-change only: best never for sanitizers and whole-system runs, which are too slow.
5. Context: runtime cost of the analysis (fast: per change; slow: scheduled).
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST keep a must-fix list; MUST suppress a finding deliberately and visibly.
Links: Refines ASSURANCE.BEHAVIOUR.2 (static layer); Requires SECURITY.2 (blocking policy).

### ASSURANCE.SECURITY.5 Secrets and Consumed Code

Intent: how secrets are kept out of history and how consumed artifacts are verified like own code.
1. Decision: (a) Secret scanning is layered (editor or pre-commit, a blocking check at push time, and CI), and a blocking check before a secret reaches shared history is preferred to alerting after. (b) Consumed libraries, packages and services receive the same verification as own code: scanned for known vulnerabilities, licence and end-of-life status, and at higher maturity for malware, before and after integration. Outcome: a secret does not reach history unnoticed and a consumed component is not trusted more than own code.
2. Grounds: (a) L251 (REG-166, REG-170): push-time blocking beats alerting after; (b) L063 (REG-004, REG-024, REG-035) and L1140 (REG-1086).
3. Positions: P1 scan consumed artifacts. P2 same verification as own code. P3 layered secret scanning (speed of feedback, security; cost: bypass paths).
4. Rejected: alert-after scanning only: best when blocking is impossible on the platform. Pre-commit alone: bypassable, best never as the only layer.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST layer secret scanning; MUST give a bypass the audited waiver of SECURITY.2; a secret found in history is rotated (practice in TRANSVERSE).
Links: the inventory stays in OWNERSHIP.LIFECYCLE (dependency lifecycle); index TRANSVERSE (configuration and secrets).

### ASSURANCE.SECURITY.6 Enforced Limits on Automation and Access

Intent: which limits on automation and on data access are enforced in tooling, not by instruction, and which jobs an automated actor may execute.
1. Decision: Limits on automation and on data access are enforced in the tooling at the lowest layer every path passes through, never by instruction in a prompt; an automated actor does not itself execute a job whose guards cannot be applied or whose effects are irreversible. Two sub-decisions follow. (a) Automation: it gets the least functionality, permission and autonomy its task needs, through a sandbox, scoped credentials, deny rules and deterministic hooks, a scoped workspace and no network egress by default; no single session combines untrusted input, access to sensitive systems or data, and the ability to change state or communicate externally without a human gate; any text an automated actor reads is untrusted input; files that steer an automated actor are versioned and reviewed like code and read-only to it where possible; per-action human approval is paired with enforced boundaries, never the only control. (b) Data access: for a data system, a single sanctioned path with single statements, read-only on production, a statement timeout and an audit log; least-privilege roles separate from application permissions, one standard owner for objects, a catalogue query that finds violations. Starting a job with a large blast radius: the decision to execute under guards or to write only is recorded; execution under enforced guards where the guards can be applied and the effects are reversible; otherwise the job is a reviewed script, and its run is authorized and triggered by the accountable person or named group (RULES.4) through the guarded path, the pipeline wherever it reaches the target; a run from a terminal only where no pipeline reaches the target or supervised ramping is needed, recorded in the same history (a person at their own terminal is an example, not the rule); the database procedure is held in CHANGE_FLOW.DATA_CHANGE.3. Outcome: what an automated actor or an ad-hoc path can touch is bounded by something it cannot argue with, and an executor cannot bypass the guards because the script was reviewed.
2. Grounds: enforce in tooling (L1066, L326; REG-1033, REG-1037, REG-1038, REG-181; consensus); least privilege (L1065, L1067; REG-1033, REG-1034, REG-1036, REG-1037, REG-1039); human approval fades (L1050; REG-1037, REG-1038, REG-1044); the three conditions (L1068; REG-1033, REG-1036, REG-1049, generalisation inferred); untrusted input (L1075); steering files (L1064); lowest-layer data access (L325, REG-181); blast-radius decision (L327, L1071; REG-181, REG-1033, REG-1037).
3. Positions: P1 tooling, not prompts. P2 approval not the only control. P3 least functionality. P4 never all three. P5 untrusted input. P6 steering files reviewed. P7 lowest-layer data access, maintainer. P8 execute versus write-only for large blast radius.
4. Rejected: application-only authorization: serves speed and misses direct paths (best when the store is reachable only through that application). Agent executes under a classifier or sandbox: best when guards can be applied and the effect is reversible. The maintainer's write-only rule is the best when guards cannot be applied or effects are irreversible; it is stated here as an outcome (the executor cannot bypass the guards and the script was reviewed), not as a rule about who writes.
5. Context: blast radius and reversibility of the job (L1071, L327), the one variable that moves P8.
6. Certainty: grounded for the enforcement principles and each position of P8; inferred for the framing of P8 as a recorded decision and for the generalisation of P4.
7. Flags: none.
Constraints: MUST enforce limits in tooling; MUST NOT combine the three conditions in one session without a human gate; MUST record the execute-or-write-only decision for a large-blast-radius job.
Links: Requires TRANSVERSE.SECURITY, CHANGE_FLOW.INTEGRATION (attribution, L1062), ASSURANCE.RULES.4 (the accountable person or named group); see CHANGE_FLOW.DATA_CHANGE.3 (database procedure, an authorization stage of the one pipeline) and DATA_CHANGE.8, ASSURANCE.ARTIFACT.2.

### ASSURANCE.SECURITY.7 Closing the Loop on Findings

Intent: how verification is itself verified and what a found defect changes in the process.
1. Decision: Security verification is itself verified: a penetration test or scan that raises no alert is treated as a detection failure; a regular process tests and evaluates the effectiveness of the measures, including the ability to restore availability and access to data. A bug found by verification is fixed, the process is changed to catch the class earlier, and where possible an approach is chosen that precludes the class. Outcome: each defect improves the process, and a silent failure of detection is itself found.
2. Grounds: detection check (L1138, REG-1090); fix, change the process, preclude the class (L1139, REG-1086); regular effectiveness process including restore (L1160, REG-1095).
3. Positions: P1 detection works. P2 fix, change process, preclude. P3 regular effectiveness process.
4. Rejected: none competes; they are three links of one loop. Fixing the instance without changing the process: best never.
5. Context: none.
6. Certainty: grounded.
7. Flags: none.
Constraints: MUST test that a known probe raises an alert.
Links: Requires ASSURANCE.AVAILABILITY.4 (proving restore); see ASSURANCE.BEHAVIOUR.8 (defect classes); OPERATION.INCIDENTS.

## Review applied

- R1 applied: waiver grounded on L214 position (b); L239 cited only for the follow-up issue on a missing review (DOCS_SYNC.2 grounds).
- R2 applied: DOCS_SYNC roll-up outcome and DOCS_SYNC.1 outcome reworded (no missing documentation; no timing window; accuracy by review).
- R3 applied: DATA_INTEGRITY.1 grounds mark mirror and naming advice inferred; the MUST on naming marked inferred.
- R4 applied: non-relational clause removed from DATA_INTEGRITY.1 Rejected and Context; only "single application owns the store" (L279) remains.
- R6 applied: DATA_INTEGRITY.4 grounds say L282 and L314 agree with public practice, L281 extends it.
- R7 applied: observe-only owner marked inferred (exit condition from L284) in decision and constraint; roll-up certainty restated.
- R8 applied: DATA_INTEGRITY.3 Rejected keeps only "undelete is a product feature"; view or default-scope mitigation marked inferred.
- R9 applied: SECURITY.3 decision now ties regular penetration testing to high criticality or regulation (L1126); frequency stays open.
- R5, R10 to R15: applied in the final pass, see below.

## Final pass applied

Resolutions (final_pass/resolutions.md, section J3):
- R5 (F2), DATA_INTEGRITY.3: applied. First-layer clause, grounds and certainty replaced; form sentence unchanged; flag F2 removed. The quoted "(X8)" marker is written as the pointer to TRANSVERSE.PRIVACY.2.
- R10 (F5), DOCS_SYNC.2: applied. Waiver sentence replaced, grounds added; flag F5 removed from .2 and from the DOCS_SYNC roll-up.
- R11 (F1), DATA_INTEGRITY.1: applied. Grounds added; decision and certainty unchanged; flag F1 removed; roll-up flags now none.
- R12 (F3), SECURITY.2: applied (with X4). Budget and REG-052 figure and waiver configuration (REG-170) added; threshold now the team's stated budget; flag F3 removed.
- R13 (F4), SECURITY.3: applied. Built-in checks item added to the floor list, grounds REG-1086; the 80 percent item stays in BEHAVIOUR.6; flag F4 removed.
- R14 (F7), SECURITY.3: applied. Penetration-test trigger and recorded cycle added, certainty inferred; the period stays open in Certainty; flag F7 removed (settled as to the rule).
- R15 (F6), SECURITY.6: applied (with X6). "automated actor" in intent and decision; Decision restructured as lead principle plus two sub-decisions (automation, data access); no split; flag F6 removed.
- R21 (confirms BEHAVIOUR.6 and SECURITY.3 unchanged), R18 (J2 node BEHAVIOUR.2 with SECURITY.2): nothing further for this unit beyond X4; the other entries of the J3 section do not exist.

Cross-unit lines:
- X1 (J2, J3), SECURITY.3: applied. Points to BEHAVIOUR.6; no coverage figure stated.
- X4 (J2, J3), SECURITY.2: applied. Block or advise points to RULES.1; SECURITY.2 keeps release-time block, who may waive, the REG-052 figure. The R12 sentence is kept as a short statement of the rule with the pointer, not a full restatement.
- X6 (J3, J6), SECURITY.6: applied. Principle and wording held here; pointers to RULES.4 and CHANGE_FLOW.DATA_CHANGE.3 and .8 added in Links.
- X8 (J3, J7, J8, J9), DATA_INTEGRITY.3: applied. Decision and Links point to OPERATION.RECOVERY.2, TRANSVERSE.PRIVACY.2 and .3; no retention number stated.
- X12 (J3, J5, J7), DATA_INTEGRITY.4: applied. Link points to OPERATION.TELEMETRY.8 (node created by J7 at graph build).
- X2, X3, X5, X7, X9, X10, X11, X13, X14: not for this unit (Units column does not name J3).

Nodes added: none. Flags still open: none (the penetration-test period is open in Certainty of SECURITY.3, with no source to ground it). Maintainer point: none for J3.
Observation, not changed: DATA_INTEGRITY.5 Decision has a garbled fragment ("... removed. with an owner (inferred ..."); left as judged.

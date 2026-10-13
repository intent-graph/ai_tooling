# J6_change_flow: result

## L1 headline

Unit J6_change_flow judged: the eight L2 nodes of CHANGE_FLOW and their 34 L3 nodes (42 records, in `judged.md` beside this file). The L1 node CHANGE_FLOW is rolled up in wave 3. Every node carries a decision, and all decisions realize the settled decision nodes (J2 RULES, CONTRACTS, J3 DATA_INTEGRITY, SECURITY.6, J4 AVAILABILITY and ARTIFACT) without re-deciding them. The contested point, the maintainer's manual production lane for database change and routed environment differences against the public same-process-everywhere rule, is decided on the strongest argument: database change travels in the one pipeline as the same reviewed script; ordinary changes reach production automatically, a risky class (long, locking, non-transactional, environment-specific, irreversible) is applied in production by a named group triggering the reviewed script (never hand-typed SQL; the gate form has no public source, inferred), and at large volume with low downtime tolerance every production database change takes that form. Environment parity holds in kind (backing-service type and version) and the differences that cannot be removed in scale, data and permissions are documented and routed to rehearsal on production-shaped data and the gated lane. Certainty: grounded for the principles that carry consensus (build once, small frequent changes, expand-migrate-contract, locks, hand-typed SQL banned); inferred for the risk-based split, the parity-by-axis resolution and every maintainer procedure with no public counterpart.

Pinned:
- Nodes judged: 42 (CHANGE_FLOW.INTEGRATION and .1 to .6; REVIEW and .1 to .4; BUILD and .1, .2; RELEASE and .1 to .5; DEPLOY and .1 to .4; ROLLBACK and .1 to .3; DATA_CHANGE and .1 to .8; MEASURE and .1, .2).
- Decisions marked undecided: none.
- Flags raised: 13 (F1 DATA_CHANGE.3 departs from the maintainer's "production applied manually by a small group" for ordinary changes, maintainer to confirm his context; F2 DATA_CHANGE.3 the unmerged release pull request is a mechanism, not a principle; F3 DATA_CHANGE.3 configuration-like registry content has no public counterpart; F4 DEPLOY.3 L328 versus L165 resolved by splitting axes, maintainer to confirm parity of backing-service type and version stands; F5 DATA_CHANGE.1 idempotent DDL narrowed from the blanket form; F6 DEPLOY.4 infrastructure-as-code is deferred scope and pull versus push is open; F7 REVIEW.1 the five-minute criterion and "senior" are one team's figures; F8 ROLLBACK.3 transaction rule is a tool-specific stack pointer; F9 INTEGRATION.4 no source ranks merge methods; F10 DATA_CHANGE.7 the skip marker can leave a migration unrehearsed; F11 BUILD.1 the maintainer's doctrine may have no automated regression run (L331, carried from J2 F3); F12 RELEASE.5 incident and off-hours block rests on one T3 source; F13 DATA_CHANGE.8 convergence query, ramp ladder and ticket key have no public counterpart).
- Settled decisions disagreed with: none.
- Review fixes applied: 6 of 6 (FX1 to FX6; flag findings FL1 to FL9 left to the final Opus pass).

## L2 claims

Each claim is marked G (grounded), I (inferred) or O (open).

INTEGRATION (I as roll-up)
- Everything needed to build, deploy and restore is in version control, one version of each shared component holds, whatever repository layout is chosen (G; layout debate on one T2 source: O).
- Integrate at least daily with branches of hours to days; unfinished work is hidden on the mainline, not held in a branch; sparse or untrusted contributors keep feature branches merged when complete (G; the daily bound I).
- Branching follows the release model: trunk with fix forward for one live version, a just-in-time release branch with cherry-picks for several supported versions (G).
- One logical, revertable change per integration, one merge method recorded per repository; squash is the default for small units (I, no source ranks the methods: O); structured messages only when history is parsed by automation (G).
- A broken mainline is reverted before new work merges; batches stay small as volume rises (G).
- Each change has a platform-recorded trail, automation identities are distinct, an unattributed change needs a named approver; no disclosure rule, the same bar for everyone (G for the trail, I for dropping disclosure).

REVIEW (I as roll-up)
- Realizes RULES.4: independent check before integration, mechanism by team and risk, show-after-merge only for the low-risk tier; depth set by risk and by evidence the submitter understands; large-blast-radius changes need qualified named approvers, who runs is held at DATA_CHANGE.3 and RELEASE.5 (G; the escalation criterion I).
- Units of about 100 lines, answered within a business day (G; thresholds I).
- Approve what improves code health and can be understood; a catalog of defect patterns by change type, with an owner (G; catalog I).
- Automation runs first; a second model assists but never approves (G; vendor-only evidence for the extra layer, O).

BUILD (G as roll-up)
- Scripted, hermetic, visible build with a self-testing suite on every push (G; the maintainer's possible lack of an automated regression run is F11, O).
- Build once, promote the same artifact, configuration outside it (G; wording I).

RELEASE (I as roll-up)
- Small, frequent releases; cadence follows the release model (G).
- An identifier promises only what is true: Semantic Versioning for consumed public API, a release identifier for a single live service (G, I for the service rule).
- Flags where a feature must be turned off without redeploying; every toggle has an expiry and a removal task (G, single source for the inventory rule).
- One staged pipeline, automatic authorization after a reviewed merge, a human gate only where the change class warrants it (G, I for placing irreversible data change under a gate).
- Restricted release operations with self-service teams; deploy only when responders are available, remediation allowed during an incident (G for the first, I for the second: F12).

DEPLOY (I as roll-up)
- The same scripted process in every environment, production included; a human trigger on a risky class is a gate inside it, not a second process (G; compatibility with the maintainer's lane I).
- Progressive rollout by blast radius; a canary judged on a concurrent control and user-impact metrics (G).
- Parity in kind everywhere; differences that cannot be removed in scale, data and permissions are documented and routed to rehearsal and the gated lane (G for parity, I for the split by axis: F4).
- Replace instances, declare state as code; pull-reconcile and scripted push with drift detection are two forms, no switch decided (G for replacement, O for pull versus push: F6).

ROLLBACK (I as roll-up)
- Roll back automatically for changes reversible by redeploy, fix forward otherwise; decided per change class beforehand (G for both positions, I for the rule).
- Every change is backward compatible and reversible through version control (G).
- Every data change records its undo before it ships: leave the structure, a prepared reverse change, or the tested restore; the last reversible point is named (G for the compatibility and restore path, I for the prepared reverse as general form).

DATA_CHANGE (I as roll-up)
- Every change is a reviewed, versioned, once-only, history-recorded script, never hand-typed; the reviewed script is the deployed script (G).
- One pipeline for database change; ordinary changes automatic to production, a risky class run by a named group from the reviewed script, all production changes so at large volume with low downtime tolerance (G for the pipeline and the ban on hand-typed SQL; I for the risk split, the named-group gate form and its condition: F1, F2, F3); configuration-like content keeps one history, an authoring script allowed.
- Schema first and compatible with both versions; expand, migrate, contract with an owned contract step; a minimum-schema-version deploy gate (G; the gate I).
- Know the lock, session lock timeout with retry, non-blocking forms, online schema change by write rate, no sharded schema change (G).
- Bulk work over very large data in bounded, throttled, re-runnable batches; the place it runs is recorded (G for the batch rules; the four-decision procedure I).
- Rehearse on production-shaped data, keep the measurements, time-budget by class, mask personal data in copies; a skipped migration is rehearsed elsewhere (G; the skip condition I: F10).
- A production bulk job is done only when its convergence query returns zero; checklist, ramp, halt on first failure, pacing on replica lag, ticket key in statements (I; F13).

MEASURE (I as roll-up)
- Delivery is judged by the five DORA outcome metrics, not by output volume, and not to rank people (G).
- Automation gains are verified against an independent baseline; fundamentals are preconditions (G for preconditions, I for the baseline principle); the net effect of automation on delivery is contested and not decided (O).

## L3 full

Full records, in tree order with positions, rejected alternatives, context, certainty and flags: `judged.md` in this folder. This section holds the reasoning for the contested nodes and one line per node.

### The contested point: DATA_CHANGE.3, DEPLOY.1, DEPLOY.3, RELEASE.4 (I)

Positions. Public: automate every change through one pipeline, hand-typed SQL banned (L168, L159, L290 a, L410; DORA, GitLab, Fowler/Sadalage). Maintainer: split by risk, long, locking, environment-specific or non-transactional changes are manual migrations outside the automatic path, production applied by a small authorized group, release pull request approved but not merged (L290, L291, L298, L328). Rival forces: delivery speed and consistency against reversibility and control.

Decision and reasoning.
- The guarantee the settled nodes require is "what runs is what was reviewed" (ARTIFACT) and "a risky change does not start unwatched" (SECURITY.6: a large-blast-radius job runs under enforced guards or by a person from a reviewed script). A risk-based gate in the one pipeline delivers both.
- The public rule bans hand-typed SQL, not a human-triggered run of an automated script (L410): the maintainer's lane is a human trigger on the same script, which L159 permits ("any authorized person can deploy any version on demand"). The recorded contradictions (L290, L328 against L159, L165, L156) dissolve once "automatic" and "same process" are separated.
- Manual production for every change is not best as the general rule: it adds delay and a path unexercised in routine, the failure the maintainer's own L286 names for manual change. It is best when data volume is large and downtime tolerance low, where no change can be trusted to be short; adopted under that condition.
- The unmerged release pull request is a mechanism that keeps the mainline equal to what is applied in production, best when a merge triggers deployment. Configuration-like registry content keeps one history; an authoring script may be its source (no public counterpart, open).
- Environment parity: the same type and version of backing services everywhere (cheap, prevents "passes on a lighter database"); scale, data volume and permissions cannot be replicated, so they are documented and the changes they affect are routed to rehearsal on production-shaped data and the gated lane. L328 and L165 apply to different axes.

Disagreement with the maintainer on the ordinary class is flagged (F1, F4) for confirmation; no settled decision is disagreed with.

### One line per node (certainty G, I or O)

INTEGRATION.1 everything to rebuild in version control, one version of shared components, layout is a means (G, layout O). INTEGRATION.2 integrate daily, short branches, unfinished work hidden, feature branches for sparse contributors (G). INTEGRATION.3 trunk and fix forward for one live version, just-in-time release branch for several (G). INTEGRATION.4 one revertable unit, one merge method recorded, squash default (I, O on a winner). INTEGRATION.5 revert a broken mainline first, small batches (G). INTEGRATION.6 platform trail, distinct automation identities, named approver for unattributed change, no disclosure rule (G, I for the last).
REVIEW.1 mechanism by team and risk, depth by risk and evidence of understanding, qualified approvers for high blast radius (G, I for the criterion). REVIEW.2 small units, answer within a business day (G). REVIEW.3 improve code health, understandable by a second reader, maintained catalog with owner (G, I for catalog). REVIEW.4 automation first, a second model assists and never approves (G, O on vendor evidence).
BUILD.1 scripted hermetic visible build on every push (G; F11). BUILD.2 build once, promote by identity (G).
RELEASE.1 small frequent releases, cadence by model (G). RELEASE.2 identifier promises only what is true (G, I). RELEASE.3 flags where needed, toggles expire (G). RELEASE.4 staged pipeline, human gates by class (G, I). RELEASE.5 restricted release operations, deploy only when responders exist (G, I; F12).
DEPLOY.1 same scripted process everywhere, human trigger is a gate (G). DEPLOY.2 progressive rollout, canary against a concurrent control (G). DEPLOY.3 parity in kind, documented and routed differences (G, I; F4). DEPLOY.4 replace instances, declared state, pull versus push open (G, O; F6).
ROLLBACK.1 roll back if reversible by redeploy, else fix forward (I). ROLLBACK.2 backward compatible, reversible through version control (G). ROLLBACK.3 undo recorded before shipping, tested restore for destructive change, last reversible point named (G, I; F8).
DATA_CHANGE.1 versioned once-only scripts, reviewed script is the deployed one, safe re-run where partial application is possible (G, I; F5). DATA_CHANGE.2 history in the target, never edit an applied migration (G). DATA_CHANGE.3 one pipeline, risk-based human trigger (G, I; F1, F2, F3). DATA_CHANGE.4 schema first, expand-migrate-contract, minimum-schema gate, compatibility surface by consumers (G, I). DATA_CHANGE.5 locks and online schema change (G). DATA_CHANGE.6 bounded re-runnable batches, size gate, place recorded (G, I). DATA_CHANGE.7 rehearsal on production-shaped data, time budget, masking (G, I; F10). DATA_CHANGE.8 convergence query as done, checklist, ramp, pacing, ticket key (I; F13).
MEASURE.1 five DORA metrics, outcomes not volume, net effect of automation contested (G, O). MEASURE.2 independent baseline, fundamentals as preconditions (G, I).

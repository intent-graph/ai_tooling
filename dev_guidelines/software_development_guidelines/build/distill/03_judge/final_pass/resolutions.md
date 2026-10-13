# Final pass: resolutions of flagged points (MD-06)

One entry per flag, grouped by unit so one applier per unit can apply it. Each entry: flag id(s)
merged | node uid | verdict | change to the record (quoted text replaces the named part; "unchanged"
when the record stands) | grounds. Verdicts: **settle** (decided here), **cross-unit** (the fix is a
line X4 onwards of `../cross_unit_fixes.md`; apply that line), **maintainer** (in
`maintainer_points.md`, with the default applied if unanswered).

Flag ids are those of each unit's `review/findings.md` (R, FL, flag-, T, F numbers) and, in brackets,
the judge's own flag the review carried. Row ids Lnnn are ledger ids, REG-nnn source register ids.
"Fetched here" marks a source this pass read; "fetched in review" a source the unit's reviewer read and
quoted. Judge flags the reviews had already closed were checked and are listed at the end of each unit.

Rules applied: MD-01 (the best for the node's purpose; a weaker practice only with the condition under
which it is best), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact).

---

## J1_ownership

- **R08, R19 (F5)** | OWNERSHIP.CONTAINMENT.2 | settle. Decision, first and third sentences replaced:
  "Put a thin wrapper, containing only what the project needs, between the code and a dependency or
  external system when substitution is plausible, or the dependency is volatile, security-sensitive or
  single-vendor, or its model differs from the domain (an anti-corruption layer that keeps business
  rules out); a rented service reached through a proprietary interface falls under these conditions,
  while a backing service reached through a stable standard interface (SQL, SMTP) is an attached
  resource (`CONTAINMENT.3`) and gets no wrapper of its own. Key the team's own data and public
  interfaces on its own identifiers and types: a vendor's identifier is stored only as an attribute of
  the team's entity that refers out (that attribute is the mapping the team owns), never as the key of
  the team's data or as a type in its public interface." Constraint: "where a wrapper exists, MUST NOT
  let a vendor type cross the team's public interface" (inferred). Grounds: L068's own condition (not
  wrapping wins for a stable, standard interface); REG-186 fetched in review ("might not be suitable
  when ... no significant semantic differences"); L343 for attached resources. For R19: REG-186 states
  translation at the boundary, not a storage rule; the defensible core is that the foreign model stays
  out of the team's keys and interfaces, while storing an external reference is unavoidable and is
  itself the owned mapping. Certainty: inferred for the identifier rule.

- **R09** | OWNERSHIP.LIFECYCLE.3 | settle. Replace "where verification is weak or deployment costly,
  strengthen the tests first rather than upgrade rarely" by: "where verification is weak or deployment
  costly, update on need (security fixes, end of life, a needed change) rather than routinely, and
  record the weak verification as debt to repay (`EVOLUTION.DEBT`): the low cadence is a consequence of
  missing tests, never a policy." Rejected P1b: "best while verification is weak or deployment costly
  and exposure is lower than the risk of change, as a temporary state (now in the Decision)". Grounds:
  L052's own condition; "strengthen first" had no row and cannot happen at once, so the interim best
  needs its condition stated (MD-01).

- **R11 (F2)** | OWNERSHIP.LIFECYCLE.3 | settle. Cooldown sentence replaced: "Hold routine
  (non-security) updates of deployables for a release-age cooldown of at least seven days, never for
  security fixes; the cooldown complements lock, hashes and review and replaces none of them. Its
  benefit rests on one analysis of ten attacks (eight of ten malicious versions removed within a week,
  nine within fourteen days) and is otherwise unmeasured: inferred." Grounds: REG-036 fetched in review
  (recommends seven days minimum, "not a panacea"); L1543 (benefit unmeasured).

- **R10 (F6)** | OWNERSHIP.LIFECYCLE.2 | settle. The "Resolution rule:" sentence replaced: "The
  guarantee does not depend on the resolution rule: whichever rule the ecosystem's tool applies, a
  version changes only through an explicit, reviewable change to the lock. The rule matters only where
  ranges are resolved without the team's lock, that is for a library's consumers: there the library
  tests both the lowest and the newest versions its ranges admit, so a consumer resolving by either rule
  (minimal version selection or newest compatible) gets a tested set." Rejected: "ranking the two rules:
  the rule comes with the ecosystem, not from the team, and testing both range edges makes either
  safe." Grounds: L047 (both rules, each with its condition), L049 and L051 (lock and ranges), the
  node's own "test the range edges". Certainty: inferred. F6 closed.

- **R12** | OWNERSHIP.STANCE.2 | settle. Replace "in this order: a platform built-in that meets the
  stated capability is preferred over custom code;" by "a capability the platform already in use
  provides (a built-in) is preferred over both new code and a new dependency when it meets the stated
  need, because it adds no new owner (the lowest-ownership case of the cost test);". No ranking across
  modes remains. Certainty: built-in preference inferred from L001 and L037 (cost of ownership,
  consensus); the maintainer's L310 agrees.

- **R13** | OWNERSHIP.STANCE.1 | settle. The layer reasons become examples: "(for example reuse across
  consumers, hiding internals behind a business-level verb, keeping a query tunable by its owner,
  enforcing integrity once)". Certainty: "grounded for the dependency half (L001, L037); the layer
  reasons are the maintainer's formulation (L308), inferred as general."

- **R14** | OWNERSHIP.LICENCE.2 | settle. Second sentence replaced: "Where the team ships client or
  embedded software or holds code it must keep closed, the classes are conservative; one organisation's
  published policy is the example (notice licences allowed, strong copyleft only server-side or
  internal, network copyleft, SSPL and non-commercial licences prohibited), not a standard." Grounds:
  L373 ("one organization's choice, not a standard").

- **R15** | OWNERSHIP.SERVICES.1, OWNERSHIP.SERVICES.5 | settle. Sentences kept, marked inline:
  SERVICES.1 "compare the remedy to the team's loss ... (inferred, L347)" and "monitor reachability,
  latency and errors of each service ... (inferred, L033 has no source)"; SERVICES.5 "Treat third-party
  assurance reports ... (inferred, L365 has no source)" and "Evaluate non-library tools and platforms ...
  (inferred, composed, L378)". Grounds: each follows from a grounded rule of its node (the SLA is a
  commercial instrument; CI and hosting are supply chain, `SERVICES.6`), but none is sourced, so the
  graph build must not carry them as grounded.

- **R16** | OWNERSHIP.CONTAINMENT.1 | settle. Replace "require a tested exit and an alternative for
  regulated or critical functions" by "require a tested exit and an alternative where regulation
  requires them (for example EU financial entities; primary text not read) and for critical functions,
  where the expected loss of being unable to leave exceeds the cost of testing the exit (inferred from
  the pricing rule above)". Grounds: L075 (b), certainty "inferred for DORA (primary text unread)".

- **R17** | OWNERSHIP.LIFECYCLE.3 with TRANSVERSE.CONFIG.6 | cross-unit **X10**.

- **R18** | OWNERSHIP.SELECTION.2 | settle. Add after the default sentence: "An organisation with
  standing capacity for experiments and tolerance for churn may run a standing trial ring (assess,
  trial, adopt, hold) and spend more novelty, still through the staged, reversible entry; a small,
  operations-heavy or long-lived system stays at the default." Grounds: L024 positions (boring wins
  small, operations-heavy, long-lived; staged novelty wins with capacity and churn tolerance).

- **F1 (judge, marked settled by review)** | OWNERSHIP.STANCE.4 | settle, unchanged. The
  reconciliation uses the maintainer's own condition (L330: probable use wins when structural change is
  costly), so it does not go against the maintainer's practice and needs no confirmation.

- Judge flags closed by the review, checked and confirmed: F3 (R05; placement now superseded by X7),
  F4 (R06).

## J2_assurance_core

- **R15, R26 (F1)** | ASSURANCE.RULES.1, ASSURANCE.BEHAVIOUR.7 | settle. RULES.1 Decision: replace
  "isolate each test and rebuild its state" by "isolate each test: each test establishes the state it
  needs instead of relying on another test's clean-up; where rebuilding per test costs too much, the
  undo is done by the platform (a rolled-back transaction, a snapshot restore), never by hand-written
  clean-up code". Positions add "P8 hand-written clean-up of shared state (L1560)". Rejected add: "P8:
  a bug in clean-up code shows up as a failure in another test (REG-054); best only where neither a
  rebuild nor a platform undo is available, and then each test checks its precondition at its start
  (inferred)." BEHAVIOUR.7: unchanged in substance (the maintainer's rollback is the platform undo, under
  d1's own condition); production itself is settled by X5. Grounds: REG-054 fetched in review ("with
  clean-up, however, one test will contain the bug, but another test will fail"); REG-1570 F.10 says
  order-dependent tests were fixed by cleaning shared state, which shows the state must be clean, not
  that hand-written clean-up is the better mechanism. The rule "no durable effect anywhere" is the
  maintainer's own (L265), so this is not against the maintainer's practice.

- **R16** | ASSURANCE.RULES.4 | settle. Tier sentence: "only a tier the team defines in advance
  (changes that follow an established pattern, an unremarkable fix, documentation), in a team whose
  mainline is kept releasable by automated gates and fast revert, may be checked after merge".
  Rejected, first sentence replaced: "Review only for uncertain changes: it leaves the classification
  to the author at the moment of the change; a tier defined in advance removes that discretion
  (inferred). 'Ship' with no review at all: best never under this node, since every change gets an
  independent check before or after merge." Certainty: tier conditions grounded in REG-098 (one
  practitioner source, fetched in review); rejection reason inferred. See X14 for CHANGE_FLOW.REVIEW.1.

- **R17** | ASSURANCE.BEHAVIOUR.1 | settle. Constraint replaced: "MUST a written test policy exist (new
  functionality and every fix come with automated tests); the evidence that it is followed is the tests
  in each change, visible in its review, with no separate artefact." Grounds: L1551 (REG-1563); the
  policy costs one line and makes the rule reviewable, while a separate evidence artefact would be the
  most demanding reading, not the best.

- **R18** | ASSURANCE.BEHAVIOUR.2 with ASSURANCE.SECURITY.2 | cross-unit **X4**.

- **R19** | ASSURANCE.BEHAVIOUR.3 | settle. First sentence replaced: "The mix follows from RULES.2 (each
  check at the lowest level that catches its failure): where logic lives inside units this gives many
  small, fast tests and progressively fewer broader ones; where failures arise in interactions between
  services, the weight moves to integration tests; for user-interface code, to static checks plus
  integration tests. End-to-end tests stay few, on critical journeys, and the proportions are recorded
  as a team decision with the reason." Rest unchanged. Grounds: no shape is the default by popularity;
  each follows from where failures arise (L090 conditions per shape), and RULES.2 is settled. Certainty:
  inferred for the mapping.

- **R20** | ASSURANCE.BEHAVIOUR.5 | settle. Decision clause: "a scheduled job is tested before it is
  scheduled like any other unit, and its first runs on real data are bounded and inspected (for example
  a reduced-scope test mode)". Constraint: "MUST a scheduled job pass its tests before it is scheduled".
  Grounds: L316 is maintainer-only; the outcome holds, the mechanism is one example.

- **R21 (F10)** | ASSURANCE.BEHAVIOUR.6, ASSURANCE.SECURITY.3 | settle, unchanged (coordinator decision
  confirmed). NIST IR 8397 (REG-1086), fetched here: "Add cases as necessary to reach at least 80 %
  coverage (2.7)", in a document stating minimum standards; the number is a mandated minimum, met as
  conformance where a baseline imposes it (the node's Context). The residual "for the maintainer" is
  closed: regulated contexts are deferred (MD-05).

- **R22 (F5, second half)** | ASSURANCE.BEHAVIOUR.7, ASSURANCE.BEHAVIOUR.4 | settle. BEHAVIOUR.7 keeps
  d1, d2, d3, d7 and d9 (they keep tests free of durable effect and re-runs identical). d5 (self-reported
  verdict), d6 (where tests live) and d8 (named fixture values) move to BEHAVIOUR.4 as sub-decisions of
  test construction; d4 is a stack pointer only. Certainty of the moved items: inferred (maintainer
  practice only).

- **R23** | ASSURANCE.BEHAVIOUR.8 | settle. First sentence replaced: "Passing review, static analysis
  and deployment is not evidence that code works: code whose behaviour depends on the shape of the data
  (queries, parsing, conversions, code on platforms that coerce or truncate) is exercised on
  production-shaped data, its edge values included, before it ships; inputs are guarded at boundaries
  always." Constraint "MUST every branch be exercised with production-shaped data" becomes "MUST
  data-dependent code be exercised on production-shaped data before it ships". Grounds: "every branch"
  is a coverage target, which BEHAVIOUR.6 rejects; the scope is L274's own defect classes.

- **R24** | ASSURANCE.CONTRACTS.1 | cross-unit **X7**.

- **R25** | ASSURANCE.CONTRACTS.2 | settle. Context, second clause replaced: "A single-team application
  whose client and server always deploy together, with no old client left in use, verifies its own seam
  with integration tests and the description diff of CONTRACTS.3, without consumer-driven contracts;
  where old clients stay in use after a server deploy (cached web clients, installed applications),
  client and server release independently in effect and the independent-release rule applies. Doubles of
  external services follow the contract-test rule in both cases." Certainty: inferred (L1187 open); the
  test that decides is whether an old client can stay live, which follows from the node's own principle.

- **R27 (F2)** | ASSURANCE.RULES.4 | **maintainer** (point 1 of `maintainer_points.md`). Default applied
  if unanswered: the recommendation there (independence is a property of the reviewer's context, not of
  its kind; a named person stays accountable and approves).

- **R28 (F3)** | ASSURANCE.BEHAVIOUR.1 | settle, unchanged. The decision does not depend on whether the
  maintainer's practice has an automated trigger (L331): self-testing code on every change is consensus
  (L081, L106, L144). Listed under "Settled against your practice" in case the gap is real.

- **R29 (F4)** | ASSURANCE.BEHAVIOUR.5, ASSURANCE.BEHAVIOUR.1 | settle, unchanged. L080 is a consensus
  row, not a maintainer row; reading it as "tests exist before the change is trusted" is consistent with
  L101 and needs no confirmation.

- **R30 (F6)** | ASSURANCE.CONTRACTS.1 | settle, unchanged in scope (X7 adds detail). The maintainer's
  "no version numbers" holds for few, in-house, reachable consumers only; listed under "Settled against
  your practice".

- **R31 (F8)** | ASSURANCE.BEHAVIOUR.8 | settle, unchanged. Both practices (pitfall catalogue, no
  blanket search-and-replace) catch defect classes that review misses, which is the node's purpose;
  OPERATION.FEEDBACK links here rather than holding them.

- **R32 (F9)** | ASSURANCE | cross-unit, already **X2** (wave-3 re-roll); no new line.

- Judge flags closed by the review, checked and confirmed: F7 (numeric defaults stated as one
  organisation's), F11 (skipped check, REG-114 fetched in review).

## J3_assurance_integrity

- **R5 (F2)** | ASSURANCE.DATA_INTEGRITY.3 | settle. First-layer clause: "a first layer that makes
  deletion reversible for a stated retention window, after which the kept copy is purged (X8)"; the form
  sentence is unchanged (archive in the same transaction by default; a flag only when undelete is a
  user-facing feature). Grounds replaced: "REG-250 (T2) states soft deletion as the primary defence
  against developer error, with a window of 15 to 60 days: that is the case for the layer, reversibility
  for a window, which both forms give. The form is chosen on referential integrity and query safety: a
  flag puts a predicate in every query and stops foreign keys protecting parent and child (L1255,
  REG-1145, T3), an archive keeps the live table clean and its keys working (L1256, REG-1142,
  REG-1145)." Certainty: layer grounded (T2, consensus rows L416, L1092); form inferred.

- **R10 (F5)** | ASSURANCE.DOCS_SYNC.2 | settle. Waiver sentence replaced: "A waiver is an explicit
  declaration in the change (documentation deferred, with a follow-up issue opened at once and assigned
  to author and reviewer), granted by the reviewer who approves the change, independent of its author
  (RULES.4); it is never a skipped check, and the CI rule passes on that declaration as on an override
  assertion (DATA_INTEGRITY.2)." Grounds: a gate with a recorded, independently granted override is the
  pattern of RULES.3 and DATA_INTEGRITY.2, not a blend: the soft gate (P4) leaves the outcome to
  whoever gives way, the waiver records who granted it and why.

- **R11 (F1)** | ASSURANCE.DATA_INTEGRITY.1 | settle, decision unchanged. Grounds added: "a declarative
  constraint is checked by the engine on every write path and cannot be forgotten by one of them; a
  procedural mechanism can be disabled, mis-ordered or bypassed by bulk paths; so the least powerful
  form that expresses a cross-writer rule wins." Certainty: inferred, as recorded.

- **R12 (F3)** | ASSURANCE.SECURITY.2 | settle (see also X4). Add: "A check blocks only while its
  measured false-positive rate is within the false-alarm budget the team states for it (RULES.1); the
  one published operating figure is about 10 percent of findings judged not useful, one organisation's
  (REG-052). Who may waive a block is configured explicitly, since on common platforms anyone with write
  access can bypass by default (REG-170)." F3 closed: the threshold is the team's stated budget.

- **R13 (F4)** | ASSURANCE.SECURITY.3 | settle. Add to the floor list: "builds and test runs enable the
  checks and protections the language, compiler and runtime provide". Grounds: NIST IR 8397 (REG-1086),
  fetched here: "Run the program with built-in checks and protections (2.5)". The 80 percent item stays
  decided in BEHAVIOUR.6 (confirmed, R21 of J2).

- **R14 (F7)** | ASSURANCE.SECURITY.3 | settle. Add: "Penetration testing of a high-risk component is
  triggered by a significant change to its attack surface and repeated on a recorded cycle; no source
  read gives a period (open)." Certainty: inferred.

- **R15 (F6)** | ASSURANCE.SECURITY.6 | cross-unit **X6** for the large-blast-radius clause. Within the
  node: "automated author" becomes "automated actor" in intent and decision; the outcome moves into the
  Decision; no split (both subjects share one principle, limits enforced at the lowest layer every path
  passes through): the lead states the principle, followed by two sub-decisions, automation and data
  access.

## J4_assurance_runtime

- **flag-1 (F3)** | ASSURANCE.PERFORMANCE.4, ASSURANCE.AVAILABILITY.3 | cross-unit **X5**.

- **flag-2** | ASSURANCE.PERFORMANCE.4, ASSURANCE.AVAILABILITY.3 | settle. AVAILABILITY.3 holds the
  guardrails shared by every production test (X5 lists them). PERFORMANCE.4 keeps only the load-specific
  ones (off-peak, ramped from a small share of traffic, capacity reserved); its constraints become "MUST
  apply the production-test guardrails of AVAILABILITY.3; MUST, for load, run off-peak, ramp from a small
  share and reserve capacity". Grounds: MD-03; each MUST still stands alone in the graph.

- **flag-3** | ASSURANCE.AVAILABILITY.3, ASSURANCE.AVAILABILITY.5 | cross-unit **X13**.

- **flag-4 (F2)** | ASSURANCE.ARTIFACT.1 | settle, decision unchanged. Grounds: the uncited "near zero
  marginal cost" is replaced by a fetched fact: GitHub documentation, fetched here, "Artifact
  attestations by itself provides SLSA v1.0 Build Level 2" (one workflow step, three permissions, one
  CLI command to verify): one platform's fact, inferred for others. The L2 floor is not the most
  demanding option (L3 and reproducible rebuilds stay conditional); it is the floor because on a hosted
  platform it costs one step, while L1 provenance can be produced by whoever runs the build. L1 stays
  best only without a hosted build platform. Certainty: grounded for one platform, inferred in general.

- **flag-5 (F7)** | ASSURANCE.AVAILABILITY.5 | settle. Replace "unannounced game days are added once the
  procedure is proven" by "unannounced game days are added once the procedure has passed announced
  exercises (inferred: a surprise drill of an unproven procedure shows only that it is unproven, at the
  risk of a real outage)"; cadence: "regularly and after changes to the system or the plan; sources give
  no number for production drills (REG-1056: regularly, regardless of need; REG-1064 reviews the plan
  about every six months)". Grounds: REG-1056, REG-1064 fetched in review.

- **flag-6 (F4)** | ASSURANCE.PERFORMANCE.5 | settle, decision unchanged. Certainty: "the rule that a
  belief about implementation internals becomes a rule only after measurement is an instance of measure
  before optimising (P1, grounded); the T2 body (REG-1571 to REG-1577) shows the case for internals
  advice. Warm-up separation is a scope (it applies where warm-up exists), inferred." F4 closed.

- **flag-7** | ASSURANCE.AVAILABILITY.2 | settle. Breaker trigger replaced: "when the dependency fails
  slowly (calls hang until the timeout and hold resources even with timeouts sized to its latency
  percentile) or is shared by many callers"; add "a long timeout is shortened first (the first rule of
  this node); a breaker does not protect against timeouts left long (REG-185)". Grounds: REG-185 and
  REG-209 fetched in review.

- Judge flags closed by the review, checked and confirmed: F1 (ladder grounded in REG-228), F5
  (REG-242), F6 (retry caps stated once), F8 (REG-239 mechanism).

## J5_construction

- **R17 (F1)** | CONSTRUCTION.BOUNDARY.5 | settle. First sentence replaced: "Choose the form of an
  interface by who composes the result: an operation with a signature (parameters, optional parameters)
  where the consumer asks a question or requests a change and the owner composes the answer, which lets
  the owner change how the result is produced and add inputs; a shape-bound read surface where consumers
  must filter, join and aggregate the result themselves (reporting, several readers), since a signature
  cannot be composed by the caller or planned with the caller's own query. Writes always go through
  operations." The "prefer a signature" default is removed. Certainty: inferred. Grounds: L309 is the
  maintainer's alone and its own sub-position (a) is the shape-bound case; a view also hides how its
  result is produced, so the remaining differences are input parameters and caller-side composition,
  and those decide by who composes.

- **R18** | CONSTRUCTION.BOUNDARY.4 (CONSTRUCTION.HIDING.4 unchanged) | settle. Third sentence replaced:
  "When several consumers need the data, the owner publishes an interface: an application interface by
  default; a dedicated published layer in the store, with the base structures private, where consumers
  need direct query access (set queries, reporting) or privileges must be separated in the store itself.
  Both are interfaces the owner publishes (HIDING.4); neither is an integration database, which binds
  consumers to the base structures." Grounds: REG-1133 fetched in review (integration databases
  avoided, application-level interfaces preferred); REG-1156 (T3, the store layer with no conditions);
  conditions inferred.

- **R19 (F2)** | CONSTRUCTION.PARADIGM.2 | settle. Scheduler sentence: "Scheduled work runs where the
  data lives when it acts only on that store's state as bounded statements or batches, and needs no
  operating-system commands, no retries beyond a rerun and no cross-system dependencies or backfills;
  otherwise it runs in the application tier or an orchestrator." ("and is small" is replaced by these
  limits, which are the row's own.) Team skill stays a tie-breaker: it is a cost-of-ownership force
  (cognitive load), not a rule about who writes code (MD-02). Placement by property is confirmed: it
  extends the settled split of DATA_INTEGRITY.1. Certainty: inferred.

- **R20 (F3)** | CONSTRUCTION.SYSTEM_SHAPE.3 | settle, unchanged. Independent deployability is the
  purpose of a boundary (L171, consensus); the coordinated breaking change of CONTRACTS.1 remains
  legitimate as an exception. Listed under "Settled against your practice".

- **R21 (F4)** | CONSTRUCTION.DESIGN.4 | settle. First sentence: "Size the structures that are costly to
  reverse (stored data layout, partitioning, system shape, published interfaces) for a stated growth
  horizon (a common heuristic: about 10x the present need) and write the horizon and the measured signal
  that will end it down; parts cheap to change are sized to the present need (OWNERSHIP.STANCE.4)."

- **R22** | CONSTRUCTION.DESIGN.1 | settle. Add: "The order is the order in which the decisions depend on
  each other; when each is taken is governed by DESIGN.2 (no earlier than the product is understood) and
  SYSTEM_SHAPE.3."

- **R23 (F5)** | CONSTRUCTION.STATE.5 | settle, kept as a conditional principle (not reduced to a stack
  pointer). Grounds added: the isocpp FAQ, fetched here, describes the same class in C++ (the "static
  initialization order fiasco": an initialisation that uses another unit's object before it is
  constructed fails depending on the order units are initialised), so the hazard is shown in two
  unrelated language families. Certainty: grounded for the hazard class in two languages, inferred for
  the general rule; the mechanics stay stack pointers.

- **R24 (F7)** | CONSTRUCTION.STATE.2 | settle, unchanged. The Boyce-Codd clause follows from the
  definition of the forms, a definitional fact that needs no empirical source. Certainty: "grounded by
  definition".

- **R25 (F9)** | CONSTRUCTION.BOUNDARY.6 | settle, unchanged. Grounds added: OWASP Error Handling Cheat
  Sheet, fetched here: "the error details are logged server side for investigation, and not returned to
  the user". Certainty: grounded for withholding internals from untrusted callers; inferred for returning
  the stable code and field names. Listed under "Settled against your practice" (narrows L315).

- Judge flags closed by the review, checked and confirmed: F6 (R12), F8 (R07). The seam note
  (OWNERSHIP.SERVICES.2 against CONTRACTS.1) goes to cross-unit **X7**.

## J6_change_flow

- **FL1** | CHANGE_FLOW.DATA_CHANGE.3 | cross-unit **X6**; the record's text: replace "Changes in the
  risky class are applied in production by a named authorized group triggering the run of the reviewed
  script with the tooling (never hand-typed SQL), after the production run is approved on the exact
  script" by "Changes in the risky class pass an authorization stage of the same pipeline: a named,
  qualified group approves the production run on the exact script and a member of it triggers the
  stage, which runs the script with the same tooling, credential scope and audit trail as every other
  change. A run started outside the pipeline is allowed only where the pipeline cannot reach the target
  or the job needs supervised ramping (DATA_CHANGE.8), and is then recorded in the same history." Grounds:
  Fowler's deployment pipeline (REG-107, fetched in review: a stage that requires human authorization)
  and DORA (REG-245, fetched in review: database changes through automated, version-controlled scripts).
  Under this wording the split is a gate of the one pipeline (RELEASE.4), not a second track.

- **FL2** | CHANGE_FLOW.DATA_CHANGE.3 | settle. Delete the large-volume sentence ("At large data volume
  ... takes the human-triggered form") and extend the criterion: "... is irreversible, touches a table
  above a size the team records, or has not had its duration measured on production-shaped data
  (DATA_CHANGE.7)". Context replaced: "Data volume moves the classification: in a store where most
  tables exceed the recorded size, most changes fall in the risky class through the criterion, with no
  separate rule." Grounds: L290 (b)'s condition is kept, carried by evidence per change instead of a
  blanket rule with no threshold.

- **FL3** | CHANGE_FLOW.DEPLOY.3 | settle. In "parity of scale, data volume, permissions or schema",
  replace "schema" by "external or shared schemas present only in production". Grounds: schema parity is
  guaranteed by DATA_CHANGE.1 and .2; L328's "missing schemas" can only mean schemas an environment does
  not host.

- **FL4** | CHANGE_FLOW.ROLLBACK.3 | settle. Reversible-form clause replaced: "a change whose reversal by
  script is faster than a restore (a data correction on few rows with its prior values saved, a
  metadata-only change) carries a written reverse prepared ahead and rehearsed with the forward script
  (DATA_CHANGE.7); a reverse that was not rehearsed does not count as the undo; otherwise the recorded
  undo is a roll-forward fix or the tested restore". Rejected: delete "P2 without the prepared undo for a
  reversible change: costs an incident to learn the undo" (no source); add "a written reverse for every
  change: reverse migrations are not worth writing all the time (REG-244) and work poorly for data
  changes (REG-251); best for packaged software with many installed versions (DISTRIBUTION)". Grounds:
  REG-244, REG-251 fetched in review. Certainty: inferred for the faster-than-restore condition.

- **FL5 (F1)** | CHANGE_FLOW.DATA_CHANGE.3 | settle, closed by FL2: the criterion carries the volume
  condition, so the decision no longer depends on which context the maintainer's store is in. Listed
  under "Settled against your practice".

- **FL6 (F4)** | CHANGE_FLOW.DEPLOY.3 | settle, unchanged. Twelve-Factor, fetched in review, confirms
  parity of backing-service type and version and says nothing on data volume. Listed under "Settled
  against your practice" for the case where L328 was meant to cover type or version.

- **FL7 (F11)** | CHANGE_FLOW.BUILD.1 | settle, unchanged (same point as J2 R28).

- **FL8 (F12)** | CHANGE_FLOW.RELEASE.5 | settle, decision unchanged. Certainty: "inferred: one T3 source
  (REG-115), plus the argument that a change needs someone able to respond to its failure". The MUST on
  the incident exception path stays: without it the block would stop the remediation itself.

- **FL9 (F13)** | CHANGE_FLOW.DATA_CHANGE.8 | settle. Constraints: keep "MUST a convergence query be
  written before the job starts"; replace "MUST a long-running statement carry the ticket key" by "MUST a
  long-running statement be identifiable to its change in activity views and logs (for example the
  ticket key in a comment)"; the ramp steps (one batch by hand, one worker, a modest default) become a
  recommendation, while "concurrency is raised only with a reason and a metric" stays a MUST. Grounds:
  the convergence argument (a returning process proves only that the process finished); identification
  is the outcome query tagging serves (L306, inferred).

- Judge flags agreed by the review, checked and confirmed: F2, F3 (closed by FX1), F5, F6, F7, F8, F9,
  F10. F5 (idempotent DDL narrowed) and F10 (skip marker conditioned) go against the maintainer's
  practice and are listed there.

## J7_operation

- **R-08** | OPERATION.ALERTING.2 | settle. Replace "where no objective exists or the service is small,
  simple threshold alerts on the symptom are enough" by "where no objective exists, simple threshold
  alerts on the symptom are enough; where traffic is too low for a burn rate to be meaningful, use the
  source's remedies (synthetic traffic, combining services under one objective) rather than simple
  thresholds". Rejected: "thresholds when an objective exists and false pages cost much: best where no
  objective exists". Context: drop "service size". Grounds: REG-132 fetched in review.

- **R-09 (F4)** | OPERATION.TELEMETRY.6 | settle. "MUST state a volume or series bound per service"
  becomes a recommendation (inferred, L460 has no normative source); "MUST bound label cardinality"
  stays.

- **R-10 (F9)** | OPERATION.RECOVERY.4 | settle. Second and fourth sentences replaced: "Every recovery
  path relied on is exercised (ASSURANCE.AVAILABILITY.4, .5). A standby that cannot be exercised
  realistically is either converted to failover, with both paths carrying traffic continuously, where
  the objectives justify running everything everywhere (latency, global audience, near-zero recovery
  time; L1106), or removed, recovery then relying on the tested restore. A fallback that is neither
  exercised nor removed is a liability: it must be exercised or removed." Grounds: REG-1075 fetched in
  review ("convert fallback to failover: exercise both code paths continuously"); REG-1055 (active/active
  only when business requirements necessitate it).

- **R-11** | OPERATION.INCIDENTS.1 | settle. Rejected P3 replaced: "a high declaration bar: best never
  as a declaration rule (unsourced; REG-127 prefers early activation to delay); in a tiny team the
  process cost is cut by scaling the response (one person holds several roles, a shorter incident
  document), not by raising the bar."

- **R-12 (F2)** | OPERATION.TELEMETRY.1 | cross-unit **X12** for the split. Within the node, first
  sentence: "The standard set is latency, traffic, errors and saturation: latency, traffic and errors
  are the request signals every service exposes alike, so anyone can be on call for code they did not
  write, and saturation is read per resource (utilisation, saturation, errors)."

- **R-13 (F1)** | OPERATION.RELIABILITY.2 with ASSURANCE.PERFORMANCE.1 | cross-unit **X11**.

- **R-14** | OPERATION.RELIABILITY.1 with ASSURANCE.PERFORMANCE.1 | cross-unit **X11**.

- **R-15** | OPERATION.RECOVERY.2 with ASSURANCE.DATA_INTEGRITY.3 | cross-unit **X8** (the retention
  clause for RECOVERY.2 is written there).

- **R-16 (F5)** | OPERATION.RECOVERY.5 | settle, decision unchanged. Certainty: "the default toward
  hardening is inferred (one T3 source states and accepts the trade-off, REG-1074); the stated
  per-system decision is the rule".

- **R-17 (F8)** | OPERATION.RECOVERY.3 | settle. Replace "and deletion needs dual authorisation" by "and
  no single credential or person can delete every copy or shorten its retention: deletion needs dual
  authorisation, or retention is enforced as immutable by the platform"; constraint likewise. Grounds:
  the outcome of L1090 holds for a team of one, where dual authorisation is impossible.

- **R-18 (F9)** | OPERATION.CAPACITY.3 | settle. MUST kept, marked inferred: dropping an index that a
  monthly workload uses costs far more than waiting one full cycle.

- Judge flags closed by the review, checked and confirmed: F3, F6, F7, F10, F11.

## J8_evolution

- **R14** | EVOLUTION.DECISIONS.2 | settle. Decision replaced: "Write a record for an architecturally
  significant decision whose reason a later maintainer could not recover from an existing policy or
  standard: several options were weighed, or no existing basis supplied the answer. A decision a
  recorded policy settles points to the policy; a workaround or an experiment gets no record; a
  deliberate, temporary shortcut is recorded as a debt item (DEBT.3)." Context: "none: with many
  contributors or a long life more decisions meet the test, since what is obvious to the team today is
  not to a newcomer; the test scales, no second bar is needed." Rejected P1 as stated: "recording what a
  policy already carries restates its reason (MD-03); best only where the policy itself is not recorded
  where readers find it." Constraint unchanged. Certainty: inferred.

- **R15** | EVOLUTION.INCREMENTAL.6 | settle. Replace "mark a deprecated item in its name" by "mark a
  deprecated item where its consumers and their tools see it: in machine-readable metadata of the item
  (DECOMMISSION.3), and in its name only where renaming it breaks no consumer"; constraint likewise.
  Grounds: CONTRACTS.1 (settled) classes a rename as breaking.

- **R16 (F5)** | EVOLUTION.INCREMENTAL.6 | settle, unchanged in text. Grounds: the few-consumer
  exception follows from settled CONTRACTS.1 (few, in-house, reachable consumers: a breaking change is
  coordinated and deployed together) and INCREMENTAL.4; it extends the maintainer's practice, it does
  not go against it.

- **R17 (F6)** | EVOLUTION.INCREMENTAL.3 | settle. Drop "or no seam exists" from the decision; the
  constraint reads "a full rewrite carries a recorded reason that the platform is obsolete". Grounds:
  Fowler's strangler fig article (REG-033), fetched here: seams are "seams that we can insert into the system",
  with transitional architecture whose cost "the reduced risk and earlier value from the gradual
  approach outweigh"; a missing seam is a cost to pay, not a condition for a rewrite.

- **R18** | EVOLUTION.INCREMENTAL.2, .4, EVOLUTION.DECOMMISSION.1, .5, .6 | settle. DECOMMISSION.1 holds
  the principle: "removal and migration work has a named owner and capacity in the plan; without them it
  stalls (REG-1002)". The others keep only what is their own and point to it: INCREMENTAL.2 "the
  removal step belongs to the change (owner and capacity: DECOMMISSION.1)"; INCREMENTAL.4 "usually the
  party that wants the change; a finish condition"; DECOMMISSION.5 "a firm deadline"; DECOMMISSION.6
  "removal is the owner's primary objective, with measurable milestones". Each constraint ends "(owner
  and capacity: DECOMMISSION.1)".

- **R19** | EVOLUTION.DEBT.2 | settle. Replace "record it, and repay it promptly" by "record it, and
  repay it as DEBT.5 sets, or drop it with the deliverable". Grounds: REG-1130 and REG-1001 fetched in
  review (interest paid only when working in the area).

- **R20** | EVOLUTION.DEBT.3 | settle. Second sentence opens: "Because no validated automatic metric
  predicts where debt hinders (L1022), a periodic survey of engineers is the main signal of where debt
  hurts ..."; Context: "where a validated metric exists for a kind of debt, it replaces the survey for
  that kind (L1022's condition)". Certainty unchanged (inferred, T4 summary).

- **R21 (F1, undecided)** | EVOLUTION.DEBT.3 | settle (no longer undecided). Replace the Undecided
  paragraph by a decision clause: "The inventory is one list kept where the team plans its work, so
  repayment competes with features in the same plan (DECOMMISSION.1, DEBT.5); a marker in the code
  carries only the item's id as a pointer; a decision record holds a debt item only where the debt came
  from a recorded decision." Grounds: the node's purpose is repayment chosen with evidence and planned;
  the marker's force (proximity to the code) is kept by the pointer and the record's by the link, so
  nothing either serves is lost: not a genuine trade-off. "Where the team plans its work" avoids naming
  a tool. Certainty: inferred.

- **R22** | EVOLUTION.DECOMMISSION.4 (and .3, .5 links) | cross-unit **X7**.

- **R23 (F3)** | EVOLUTION.DECOMMISSION.6 | cross-unit **X8**.

- **R24** | EVOLUTION.TECHNOLOGY.1 | settle. Add: "How firmly this holds follows TECHNOLOGY.3: for few,
  independently operated components, fit to the problem counts as the stated need that allows adding
  alongside." Context: "see TECHNOLOGY.3".

- **R25** | EVOLUTION.TECHNOLOGY.2 | settle. Add: "The register holds technologies (languages,
  frameworks, stores, platforms) and the team's position on each. It is neither the sanctioned list of
  admitted dependencies (OWNERSHIP.SELECTION.1, the gate) nor the inventory of what is deployed
  (OWNERSHIP.LIFECYCLE.5): position, admission and presence are three facts, each held once."

- **R26 (F8 residual)** | EVOLUTION.TECHNOLOGY.3 | settle. Decision replaced: "Hold the set as firmly as
  the cost of a departure is shared. Wherever a platform or on-call is shared, keep a supported default
  set: a departure whose whole operating cost stays with the team that chose it is permitted and
  unsupported (paved path); a departure whose cost would land on the shared platform or on-call needs a
  recorded decision naming who carries it (mandate). Where components run independently and nothing is
  shared, choose per component by fit within the default of OWNERSHIP.SELECTION.2." Context: "where the
  operating cost of a departure lands (L1040)". Rejected updated: "P1 for a departure whose cost stays
  with its team; P2 for a departure that would land on a shared on-call; P3 for a shared platform."
  Grounds: the three positions of L1040 differ on one variable, who carries the operating cost, which
  the row names as the force; the "between the two" condition, stated by no source, disappears.
  Certainty: inferred.

- Judge flags closed by the review, checked and confirmed: F2 (R10), F4, F7.

## J9_transverse

- **T1** | TRANSVERSE.DOCS.3 | settle, unchanged. Grounds: one origin per fact (MD-03, DOCS_SYNC.3) and
  commits carrying what and why (L133) put history in version control; the maintainer's own condition
  (L318: readers who cannot see the repository history) is honoured, and covers definitions read where
  they are deployed, such as a function read from a database catalogue (inferred). Listed under "Settled
  against your practice" for code read inside the repository.

- **T5** | TRANSVERSE.SECURITY_MONITORING.1 | settle, unchanged; certainty raised to grounded. The OWASP
  Logging Cheat Sheet, fetched in review, says to log these events without levels; ASVS levels set what
  is verified, not what is needed; ASSURANCE.SECURITY.1 (depth by risk) governs verification depth, not
  whether security events are recorded.

- **T6** | TRANSVERSE.PRIVACY.3 | cross-unit **X8** (the erasure-in-backups text is written there).

- **T7** | TRANSVERSE.CONFIG.1 to CONSTRUCTION.BOUNDARY.2 | cross-unit **X9**.

- **T8** | TRANSVERSE.CONFIG.2 | settle. (a) Second sentence replaced: "Secrets live in a managed store
  (CONFIG.4) and reach the process by runtime injection as mounted files or through the store API; an
  environment variable is used only where the platform offers neither, or where the process environment
  is shown not to leak (no child process inherits it, no diagnostics or dumps include it) and a restart
  suffices to rotate." Rejected P1: "environment variables as the default channel for secrets: they are
  'generally accessible to all processes and may be included in logs or system dumps' (REG-166, OWASP,
  fetched in review); best only under the condition above." (b) Rejected P3 replaced: "configuration
  packaged per environment with the binary: best never (the artifact would differ per environment);
  non-secret configuration of every environment packaged with the binary and selected at deploy: best
  where it must change and roll back atomically with the code that reads it (L1193; condition inferred),
  the artifact staying one."

- **F11** | TRANSVERSE.DOCS.5 | settle, decision unchanged. Certainty: "grounded for the override note
  (L323); the basis record and the 'deduced, unconfirmed' marker are inferred from the guideline's own
  method: a rule without a stated basis cannot be re-judged (MD-01)." Flags line: "inferred parts noted".

- **F12** | TRANSVERSE.ENVIRONMENTS.2 | settle, unchanged. The added conditions follow by contraposition
  from L262; certainty stays inferred, as recorded.

- **F13** | TRANSVERSE.SECURITY.1 | settle. Replace "a prescriptive maturity model (SAMM) or outcome
  framework (SSDF) to assess and plan a programme across many teams" by "a prescriptive maturity model
  (SAMM) to assess and plan a programme across many teams, with an outcome framework (SSDF) as the list
  of outcomes the programme covers (P1)". Grounds: L1120 places only SAMM there; L240 treats SSDF as an
  outcome list.

- Judge flags closed by the review, checked and confirmed: T2, T3, T4.

---

## Sources fetched in this pass

| source | point it settles | result |
|---|---|---|
| GitHub docs, artifact attestations (concepts page) | ARTIFACT.1 L2 floor cost | confirmed: "Artifact attestations by itself provides SLSA v1.0 Build Level 2." |
| GitHub docs, using artifact attestations (how-to page) | same | setup confirmed (one step, three permissions); no SLSA level stated on that page |
| NIST IR 8397 (REG-1086) | SECURITY.3 built-in checks; BEHAVIOUR.6 80 percent | confirmed: "Run the program with built-in checks and protections (2.5)"; "at least 80 % coverage (2.7)" |
| isocpp FAQ, static initialization order | STATE.5 language-neutral hazard | confirmed (C++ static initialisation order fiasco) |
| OWASP Error Handling Cheat Sheet | BOUNDARY.6 audience scoping | confirmed: details "logged server side ... and not returned to the user" |
| Fowler, Strangler Fig Application (REG-033) | INCREMENTAL.3 "no seam exists" | confirmed: seams are inserted; gradual approach outweighs transitional cost |

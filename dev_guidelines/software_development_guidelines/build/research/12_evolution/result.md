# 12_evolution (EVOL): decision records, incremental change, technical debt and refactoring, decommissioning, number of technologies

## L1 headline

Best practice for evolving a system over time is well established on four of the five topics (record the reasons behind significant decisions in short, version-controlled, superseded-not-edited records; change in releasable increments and finish the removal step; treat debt as a cost of future change that is paid where code is touched; retire software through announced, reversible, owned steps) and is open on how debt should be measured and how far the set of technologies should be mandated; certainty: grounded for the process claims (T1/T2 read), inferred for syntheses across them, open for empirical measurement.

Pinned: 40 sources (T1 = 5, T2 = 20, T3 = 11, T4 = 4); 41 claims; contested = "immutable vs living decision records", "rewrite vs incremental replacement", "deliberate debt for speed vs design stamina", "measure debt by tool metrics vs engineer perception", "opportunistic refactoring vs dedicated debt capacity", "advisory vs compulsory deprecation", "mandated stack vs paved path vs polyglot autonomy"; no failed T1 fetch (the SEC order PDF was unreadable through the fetch tool and was read page by page as images instead); failed or partial fetches on lower tiers: c2 wiki and a video transcript (Cunningham, replaced by his 1992 report), Fowler "Preparatory Refactoring" and GOV.UK service-manual pages (404), Beck's essay (paywalled, partial), Google's debt paper (abstract only; figures via a T4 summary).

## L2 claims

Pinned (same as L1): 40 sources (T1 = 5, T2 = 20, T3 = 11, T4 = 4); 41 claims; contested = "immutable vs living decision records", "rewrite vs incremental replacement", "deliberate debt for speed vs design stamina", "measure debt by tool metrics vs engineer perception", "opportunistic refactoring vs dedicated debt capacity", "advisory vs compulsory deprecation", "mandated stack vs paved path vs polyglot autonomy"; no failed T1 fetch (SEC order PDF read as page images after the fetch tool could not parse it).

Reuse note: the sibling web-architecture slot already holds boring technology, ADR basics (numbered, superseded, in version control), evolutionary architecture, strangler fig and the debt quadrant (its claim ids ARCH-C27 to C43). Not repeated here; this slot adds what happens after the choice: scope and lifecycle of records, retirement, debt handling, and the total number of technologies.

Clusters:
1. Record the reasons for significant decisions (context, options, rejected alternatives, consequences), short, one decision per record, next to the code, with a status and an owner. Consensus, grounded. EVOL-C01, C02, C03, C06, C07.
2. What is significant enough to record, and proposal versus record. Majority (thresholds differ), grounded. EVOL-C04, C08, C09.
3. Records are not edited once accepted; a reversal is a new record that supersedes. Contested (living-document minority), grounded. EVOL-C05.
4. Change in steps that keep the system releasable; expand, migrate, contract, and finish the contract; unfinished migrations are debt. Consensus, grounded (C12 inferred). EVOL-C10, C11, C12.
5. Change at scale needs sharding, automation, and a named owner, because consumers multiply the cost of change (Hyrum). Majority (one deep source plus corroboration), grounded. EVOL-C13, C14, C15, C16.
6. Rewrite versus incremental replacement. Contested, grounded for the positions; the winner is not settled by evidence. EVOL-C17.
7. Technical debt is expedient construction that raises the cost of future change; interest accrues where code is changed; it is wider than code. Consensus, grounded. EVOL-C18, C19, C21.
8. Taking debt on purpose and measuring it. Contested (speed versus stamina; metrics versus perception); empirical support thin. Grounded for positions, open for effect sizes. EVOL-C20, C22, C23.
9. Refactoring: small behaviour-preserving steps with a check, timed by cost comparison; opportunistic by default, dedicated capacity contested. Majority, grounded. EVOL-C24, C25, C26, C27.
10. Code is a liability; removing what is not used is a first-class activity; dead code left running is a documented hazard. Consensus (one T1 incident, one T2 principle), grounded. EVOL-C28, C29, C41.
11. Retire in announced stages, with machine-readable signals, support windows by stability tier, usage check, reversible switch-off, backups, owner and milestones. Majority, grounded. EVOL-C30 to C36.
12. Keep the number of technologies small by pairing every addition with a retirement, keeping an explicit position per technology, and choosing how hard to mandate. Majority on the first two, contested on mandate; grounded. EVOL-C37, C38, C39, C40.

Live debates (forces in tension):
- Immutable versus living decision records: fidelity of history, audit versus accuracy of the current picture, authoring friction (EVOL-C05).
- Rewrite versus incremental replacement: continuity of delivery, preserved bug-fix knowledge versus ability to change at all, second-system risk (EVOL-C17).
- Debt taken deliberately for speed versus design stamina: delivery speed now versus cost of change later; Fowler himself calls the payoff point a conjecture (EVOL-C20).
- Debt measured by tool metrics versus engineer perception: objectivity and automation versus validity; Google found no single metric among 117 predicted perceived debt (T4 summary of a T3 paper) (EVOL-C22).
- Opportunistic refactoring versus dedicated debt capacity: flow, small risk versus visibility, protection from feature pressure (EVOL-C26).
- Advisory versus compulsory deprecation: consumer autonomy versus completion; compulsory only works with a staffed migration team (EVOL-C33).
- Mandated stack versus supported path versus polyglot choice: cognitive load, upgrade cost, cost of ownership versus team autonomy and local fit (EVOL-C39).
- One version of each dependency versus several: ability to change at scale versus consumer friction (EVOL-C40, boundary ADOPT).

Candidate central decisions (choices every team must make first):
- D1. Which decisions get a record, who owns it, and whether accepted records are immutable (C04, C05, C06).
- D2. Default way to change: increments that stay releasable, and what finishes a migration (C10, C11, C12, C14).
- D3. Where debt is recorded and how its impact is assessed; who may take deliberate debt (C20, C22, C23).
- D4. When refactoring happens: inside feature work, as dedicated capacity, or both (C25, C26).
- D5. Retirement policy: stages, support windows per stability tier, who owns removal (C30, C31, C33, C35).
- D6. How the set of technologies is governed: radar position, mandate versus paved path, retire-on-adopt (C37, C38, C39).

Not covered: Parnas "Software Aging", Lehman's laws read from the original (only a T4 summary); the full Google debt paper and Dagstuhl working-group chapters (only the executive summary and abstract); SQALE and tool-based debt indices; regulated-context retention obligations on retirement (deferred by the maintainer); mobile and on-device end of life (out of scope); legal and contractual end-of-life of services consumed (EXT); ADR tooling comparisons; quantitative thresholds for support windows beyond Kubernetes and SemVer.

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| EVOL-S01 | T2 | Technical Debt | Martin Fowler | https://martinfowler.com/bliki/TechnicalDebt.html | interest and principal, where to pay |
| EVOL-S02 | T2 | Deprecation (ch. 15, Software Engineering at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch15.html | code as liability, advisory vs compulsory deprecation, ownership |
| EVOL-S03 | T2 | Large-Scale Changes (ch. 22, SWE at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch22.html | sharded, automated change, ownership |
| EVOL-S04 | T2 | Parallel Change | Martin Fowler | https://martinfowler.com/bliki/ParallelChange.html | expand, migrate, contract |
| EVOL-S05 | T2 | Branch by Abstraction | Martin Fowler | https://martinfowler.com/bliki/BranchByAbstraction.html | replacing a supplier without a long-lived branch |
| EVOL-S06 | T2 | The WyCash Portfolio Management System (experience report, 1992) | Ward Cunningham | https://c2.com/doc/oopsla92.html | origin of the debt metaphor |
| EVOL-S07 | T2 | Managing Technical Debt in Software Engineering (Dagstuhl Seminar 16162 report) | Avgeriou, Kruchten, Ozkaya, Seaman | https://utupub.fi/bitstream/10024/169748/1/dagrep_v006_i004_p110_s16162.pdf (executive summary and definition read, pages 1 to 6) | consensus definition and model of debt |
| EVOL-S08 | T2 | Design Stamina Hypothesis | Martin Fowler | https://martinfowler.com/bliki/DesignStaminaHypothesis.html | design payoff line, status as conjecture |
| EVOL-S09 | T2 | Opportunistic Refactoring | Martin Fowler | https://martinfowler.com/bliki/OpportunisticRefactoring.html | refactoring inside feature work |
| EVOL-S10 | T2 | Refactoring Malapropism | Martin Fowler | https://martinfowler.com/bliki/RefactoringMalapropism.html | strict definition of refactoring |
| EVOL-S11 | T2 | First, After, Later, Never | Kent Beck | https://newsletter.kentbeck.com/p/first-after-later-never (partial, paywalled) | timing of tidying |
| EVOL-S12 | T2 | Documenting Architecture Decisions | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | origin and form of ADRs |
| EVOL-S13 | T2 | Architectural decision record process | AWS Prescriptive Guidance | https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | scope, states, ownership, review, immutability |
| EVOL-S14 | T2 | Architecture decision records | Google Cloud Architecture Center | https://docs.cloud.google.com/architecture/architecture-decision-records | when to write, where to store |
| EVOL-S15 | T2 | PEP 1, PEP Purpose and Guidelines | Python project | https://peps.python.org/pep-0001/ | proposal documents as decision record, statuses |
| EVOL-S16 | T2 | What Is Software Engineering? (ch. 1, SWE at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch01.html | time, change, Hyrum's Law |
| EVOL-S17 | T2 | Version Control and Branch Management (ch. 16, SWE at Google) | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch16.html | one-version rule |
| EVOL-S18 | T2 | Code maintainability | DORA | https://dora.dev/capabilities/code-maintainability/ | maintainability as a capability and its metrics |
| EVOL-S19 | T2 | Microservices (article) | Fowler and Lewis | https://martinfowler.com/articles/microservices.html (decentralized governance section) | polyglot choice position |
| EVOL-S20 | T2 | Semantic Versioning 2.0.0 | Tom Preston-Werner | https://semver.org/ | deprecation before removal |
| EVOL-S21 | T1 | RFC 8594, The Sunset HTTP Header Field | IETF | https://www.rfc-editor.org/rfc/rfc8594.html | signalling decommissioning |
| EVOL-S22 | T1 | RFC 9745, The Deprecation HTTP Response Header Field | IETF | https://www.rfc-editor.org/rfc/rfc9745.html | signalling deprecation; ordering with Sunset |
| EVOL-S23 | T1 | Kubernetes Deprecation Policy | Kubernetes project | https://kubernetes.io/docs/reference/deprecation-policy/ | support windows per stability tier |
| EVOL-S24 | T1 | Order, In the Matter of Knight Capital Americas LLC (Release 34-70694) | US Securities and Exchange Commission | https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf (pages 1 to 4) | finding on code left on servers |
| EVOL-S25 | T1 | COST04-BP02 Implement a decommissioning process | AWS Well-Architected | https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_implement_process.html | decommissioning steps |
| EVOL-S26 | T3 | MADR, Markdown Architectural Decision Records | ADR community | https://adr.github.io/madr/ | considered options, drivers, confirmation |
| EVOL-S27 | T3 | Rust RFC template | Rust project | https://github.com/rust-lang/rfcs/blob/master/0000-template.md | drawbacks, alternatives, unresolved questions |
| EVOL-S28 | T3 | Things You Should Never Do, Part I | Joel Spolsky | https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/ | case against rewrites |
| EVOL-S29 | T3 | Choose Boring Technology (talk) | Dan McKinley | https://boringtechnology.club/ | replace, do not add; retire older tool |
| EVOL-S30 | T3 | Choose Boring Technology (essay) | Dan McKinley | https://mcfunley.com/choose-boring-technology | long-term cost of heterogeneity |
| EVOL-S31 | T3 | How We Use Golden Paths to Solve Fragmentation | Spotify Engineering | https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/ | supported-not-mandated path |
| EVOL-S32 | T3 | Technology Radar FAQ | Thoughtworks | https://www.thoughtworks.com/radar/faq | rings and own-radar use |
| EVOL-S33 | T3 | Lightweight Architecture Decision Records (Radar entry) | Thoughtworks | https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records | ADRs in source control; Adopt in 2018, not on current edition |
| EVOL-S34 | T3 | Defining, Measuring, and Managing Technical Debt | Jaspan and Green, IEEE Software 2023 | https://research.google/pubs/defining-measuring-and-managing-technical-debt (abstract only) | peer-reviewed Google study of debt |
| EVOL-S35 | T3 | Guide to our approach to the retirement of API endpoints | UK Office for National Statistics developer site | https://developer.ons.gov.uk/retirement/ | staged retirement with blackouts |
| EVOL-S36 | T3 | Self-admitted technical debt studies (Potdar and Shihab and replications) | academic | read through a search-result summary only, no paper fetched | removal rates of debt marked in comments |
| EVOL-S37 | T4 | Architecture decision record (repository) | Joel Parker Henderson | https://github.com/joelparkerhenderson/architecture-decision-record | mutable ADR minority view; when to skip |
| EVOL-S38 | T4 | Getting away with rewriting code from scratch | programming is terrible (personal blog) | https://programmingisterrible.com/post/73023853878/getting-away-with-rewriting-code-from-scratch | case for rewriting under conditions |
| EVOL-S39 | T4 | How Google Measures and Manages Tech Debt | DX newsletter | https://newsletter.getdx.com/p/measuring-and-managing-tech-debt | figures of the Google paper (secondary) |
| EVOL-S40 | T4 | Lehman's Laws of Software Evolution | lawsofsoftwareengineering.com | read through a search-result summary only | continuing change, increasing complexity |

### Claims

**EVOL-C01**
- claim: Record the reasons behind each significant decision (the forces at play, the decision, its consequences), because the motivation of past decisions is among the hardest things to recover, and its absence makes a team either obey outdated decisions or reverse them blindly.
- level: principle; stack: neutral
- sources: S12 (Why, Context), S13 (intro, ADR contents), S14 (Benefits)
- agreement: consensus; certainty: grounded
- note: ADR basics are held by the sibling slot (ARCH-C35 to C39); this claim restates only the reason, as the root of the cluster.

**EVOL-C02**
- claim: A decision record should state the options considered and why the rejected ones were rejected, including dissent, so the same discussion is not reopened without new information.
- level: practice; stack: neutral
- sources: S13 (rejected state keeps its reason "to prevent future discussions on the same topic"), S15 (Rationale, Rejected Alternatives, dissenting opinions), S26 (Considered Options), S27 (Rationale and alternatives, Drawbacks)
- agreement: consensus; certainty: grounded

**EVOL-C03**
- claim: Keep each record short (one or two pages), about one decision, numbered without reuse, written as prose to a future reader, and stored in version control beside the code it governs (mirrored to a wiki only for wider reach).
- level: practice; stack: neutral (Markdown text is the common vehicle)
- sources: S12 (Key principles), S14 (Storage), S33 (How), S15 (versioned repository as historical record), S37 (singular focus)
- agreement: consensus; certainty: grounded

**EVOL-C04**
- claim: Decide a significance threshold for what gets a record; sources converge on structure, non-functional requirements, dependencies, interfaces and construction techniques (libraries, frameworks, tools, processes), and on skipping limited-scope, temporary or already-policy decisions.
- level: decision; stack: neutral
- sources: S13 (Scope, citing Richards and Ford), S14 (When to write), S37 (when to skip)
- agreement: majority; certainty: grounded for the lists, inferred that one threshold fits all
- positions: (a) record every architecturally significant decision (S13): serves later confidence and onboarding, costs authoring time; wins when many contributors or long life. (b) record only when no existing basis for the decision or several options were weighed (S14): serves low overhead; wins when the team is small and standards exist. (c) skip workarounds and experiments (S37, T4). Forces: cost of ownership, team cognitive load, reversibility.

**EVOL-C05**
- claim: Once a record is accepted, do not rewrite it; reverse a decision by a new record that supersedes it and keep the old one marked superseded.
- level: decision; stack: neutral
- sources: S12 (Key principles), S13 (ADR review process: immutable, Superseded), S14 (Lifecycle: keep previous choice beside the new one), S37 (immutability vs living documents)
- agreement: contested; certainty: grounded for the positions
- positions: (a) immutable, supersede (S12, S13): serves an honest history and audit; wins when many readers rely on the record, or regulated review. (b) mutable "living document" with dated additions (S37, T4: "immutability is ideal; in practice mutability has worked better for our teams"): serves an accurate current picture and less authoring friction; wins when the record is the only place readers look and a few people own it. Note (inferred): when records sit in version control, history survives edits, which narrows the cost of (b); (a) still keeps the current status machine-readable.

**EVOL-C06**
- claim: Give each record a status (proposed, accepted, rejected, superseded, deprecated), a named owner, and a review before acceptance.
- level: practice; stack: neutral
- sources: S12 (Status), S13 (ADR adoption process, owner, 10 to 15 minutes reading), S15 (statuses: Draft, Accepted, Provisional, Final, Rejected, Withdrawn, Deferred)
- agreement: consensus; certainty: grounded

**EVOL-C07**
- claim: Consult the accepted records during code and design review; a reviewer who finds a change violating a record links it.
- level: practice; stack: neutral
- sources: S13 (ADR adoption process, validation of component changes)
- agreement: consensus (single source, no dissent found); certainty: grounded
- boundary: DELIVER

**EVOL-C08**
- claim: For changes with many stakeholders, separate the proposal document (written before the decision, with drawbacks, alternatives, unresolved questions, a backward-compatibility section, a named decider) from the decision record (the outcome and its reason).
- level: decision; stack: neutral
- sources: S15 (Rationale, Backwards Compatibility, Steering Council and delegate), S27 (Drawbacks, Rationale and alternatives, Prior art, Unresolved questions)
- agreement: majority; certainty: inferred (two open-source projects; the proposal-versus-record split is my synthesis)
- positions: (a) one document serves both roles, as PEPs do (S15): fewer artifacts, history in version control; wins in open projects with many contributors. (b) a lightweight record only (S12, S14): lowest overhead; wins for small teams. Forces: speed, cognitive load, confidence.

**EVOL-C09**
- claim: Name the forces behind a decision (technical, political, social, project-local) so that a change in those forces is visible and signals when to revisit.
- level: principle; stack: neutral
- sources: S12 (Context, "forces at play"), S26 (Decision Drivers)
- agreement: consensus; certainty: inferred (the revisit-trigger reading is mine; sources state the forces, not the trigger)

**EVOL-C10**
- claim: Change in steps that keep the system releasable at every step (an interface supporting both versions, an abstraction with two suppliers) rather than on a long-lived branch or in one switch-over.
- level: principle; stack: neutral
- sources: S04 (Primary Benefits), S05 (Why use it instead of long-lived branches)
- agreement: consensus; certainty: grounded
- boundary: DELIVER

**EVOL-C11**
- claim: Run incompatible interface changes as expand, migrate, contract, and treat the contract step (removal of the old form) as part of the change, because supporting two versions is a recurring cost that only ends there.
- level: practice; stack: neutral (applies to code interfaces, remote APIs, schemas)
- sources: S04 (three phases, Notable Drawback), S05 (step 5, remove obsolete code)
- agreement: consensus; certainty: grounded
- boundary: DATA (schema form), DELIVER

**EVOL-C12**
- claim: A migration without its removal step is debt in its own right; track it until the old form is gone.
- level: principle; stack: neutral
- sources: S04 ("without disciplined completion of the contract phase, the situation worsens"), S39 (Google's ranking: "migration needed or in progress" first, "poorly executed or abandoned migration" ninth among ten debt categories; secondary summary)
- agreement: consensus; certainty: inferred (S04 grounds the mechanism; the framing as debt joins S04 with the Google survey ranking)

**EVOL-C13**
- claim: As codebase and contributor count grow, the largest change that can be made atomically shrinks; so mechanical changes across many owners should be generated by tools and split into independently testable and reviewable shards, with the old pattern then blocked from reappearing.
- level: practice; stack: neutral
- sources: S03 (Why LSCs Matter, Process Phases, Sharding Strategy, Cleanup)
- agreement: consensus (one deep source, no dissent found); certainty: grounded
- context where it wins: large shared codebase, many owners; small single-owner code can change in one step.

**EVOL-C14**
- claim: A migration that touches many consumers needs one accountable owner with staffed capacity (usually the team that wants the change), not an unfunded mandate on each consumer, or it stalls as organic migration.
- level: decision; stack: neutral
- sources: S02 (Process Ownership, Compulsory Deprecation), S03 (Ownership Structure)
- agreement: majority; certainty: grounded
- positions: (a) central team owns migration (S02, S03): serves completion and low consumer load; costs central capacity; wins with many consumers and mechanical changes. (b) consumers migrate themselves (implicit in advisory deprecation, S02): serves autonomy; wins when the replacement is transformatively better. See C33.

**EVOL-C15**
- claim: Treat a system's life as a series of changes it must absorb: it is sustainable when it can respond to whatever valuable change arrives within its expected lifespan, which for code spans orders of magnitude, and this expectation decides how much to invest in changeability.
- level: principle; stack: neutral
- sources: S16 (Sustainability and Change: "programming integrated over time"), S40 (continuing change, increasing complexity unless worked against; secondary)
- agreement: consensus; certainty: grounded for S16; S40 not read from the original

**EVOL-C16**
- claim: The more consumers a system has, the more observable behaviours are depended upon, so the cost of any change or removal grows with consumer count; counter it with tests in CI that capture what consumers rely on, so infrastructure owners need not track consumers.
- level: principle; stack: neutral
- sources: S02 (Hyrum's Law), S16 (Hyrum's Law, Beyonce Rule)
- agreement: consensus; certainty: grounded
- boundary: VERIFY (the test part, VERIFY-C26)

**EVOL-C17**
- claim: Replace a system incrementally while it keeps running; a full rewrite from scratch is justified only under stated conditions, and then needs parallel running and slow migration.
- level: decision; stack: neutral
- sources: S28 (rewrite as the single worst strategic mistake; old code carries real-world bug fixes; do architectural refactoring instead), S38 (rewrite can work when feature cost is prohibitive, the platform is obsolete, the code is genuinely bad; old code still maintained meanwhile), S05 (replacing a supplier behind an abstraction); sibling ARCH-S21 (strangler fig) for the middle path
- agreement: contested; certainty: grounded for the positions; open whether either wins in general
- positions: (a) never rewrite, refactor in place (S28, T3): serves delivery continuity and preserved hidden knowledge; wins when the system is shipping and its behaviour is poorly specified. (b) rewrite when changing the old code costs more than new (S38, T4; the claim of "25 percent" is a rule of thumb from that source, unverified): serves ability to change and removal of dead platforms; wins when the platform is obsolete and the old system keeps running in parallel. (c) incremental replacement behind an interface (S05, ARCH-S21): serves both continuity and replacement; cost is two systems in the interim. Forces: delivery continuity, reversibility, cost of ownership.

**EVOL-C18**
- claim: Technical debt is a set of design or implementation constructs that are expedient in the short term but set up a technical context that makes future change more costly or impossible; it is a contingent liability limited to internal qualities (maintainability, evolvability), and it is often incurred unintentionally.
- level: principle; stack: neutral
- sources: S07 (16162 definition, executive summary), S06 (shipping first-time code is like going into debt; every minute on not-quite-right code is interest), S01
- agreement: consensus; certainty: grounded

**EVOL-C19**
- claim: Interest accrues only where code is changed; pay principal gradually in areas of high activity and leave crufty but stable areas alone.
- level: decision; stack: neutral
- sources: S01 (Decision Logic), S07 (principal and interest; recurring versus accruing interest)
- agreement: consensus; certainty: grounded
- context: valid while those areas stay stable; Beck's "never tidy" reason is the same (C25).

**EVOL-C20**
- claim: Take debt deliberately only for functionality below the point where good design pays off, and repay it promptly; above that point the speed gain is illusory.
- level: decision; stack: neutral
- sources: S06 ("a little debt speeds development so long as it is paid back promptly"), S08 (design payoff line, "usually weeks not months", a conjecture without objective proof), S01 (most teams exceed the line in weeks)
- agreement: contested; certainty: inferred (the payoff point is explicitly unproven)
- positions: (a) a little debt speeds development if repaid promptly (S06): serves delivery speed now; wins for a short-lived or exploratory deliverable. (b) payoff arrives in weeks, so quality is not a trade-off for anything beyond the smallest scope (S08, S01): serves cost of change later; wins for anything that will be changed. Fowler's own caveat: no objective proof (S08). Sibling holds the quadrant (ARCH-S27).

**EVOL-C21**
- claim: Debt is wider than code quality: the most significant debt comes from design trade-offs not visible in code metrics, and covers migrations, documentation, tests, dead code, dependencies, team expertise and release process; inventory all of these.
- level: principle; stack: neutral
- sources: S07 (How do we manage technical debt: "most significant technical debt is caused by design trade-offs, which are not detectable by measuring code quality"), S34 (abstract: human and technical), S39 (Google's ten categories, secondary)
- agreement: consensus; certainty: grounded for S07, inferred for the full list (secondary source)

**EVOL-C22**
- claim: Identify debt from engineers' reported experience as well as from tool metrics, because no known automatic metric reliably predicts where debt hurts.
- level: decision; stack: neutral
- sources: S07 ("effective tooling to assess technical debt remains a challenge"), S34 (abstract, "difficult without being able to define or measure it"), S39 (117 metrics for three debt types, none predicted reported debt; a quarterly survey became the measure; secondary)
- agreement: contested; certainty: grounded for S07, inferred for the Google figures (T4 summary of a T3 paper not read in full)
- positions: (a) tool-detected smells, coupling, dependency analysis (the Dagstuhl-reported research stream, S07): serves automation and trend tracking; costs validity, misses design debt. (b) periodic survey of engineers about hindrance, deliberate debt, investment in reduction (S39): serves validity; costs subjectivity and survey fatigue. Forces: validity, cost, visibility. Wins: (b) as the primary signal when no validated metric exists, (a) as supplement for specific smells.

**EVOL-C23**
- claim: Keep an inventory of debt items, each with its cause, consequence, affected artefact and impact, and manage it by recognizing, analyzing, monitoring and measuring; decide where items live (issue tracker, decision record, code comment).
- level: decision; stack: neutral
- sources: S07 (conceptual model; "How do we manage technical debt"), S39 (management framework for inventorying debt and assessing impact; maturity model; tooling for stale docs, deprecated dependencies), S36 (debt marked in code comments exists in up to 31 percent of files; 26 to 63 percent of it is later removed; secondary summary), S37 (decision todo list beside the product todo list)
- agreement: majority; certainty: inferred (no source compares storage places)
- positions: tracker (visible to planning), in-code marker (travels with the code, cheap), record (ties debt to a decision). Forces: visibility versus authoring cost. Open: which place gets items repaid soonest.

**EVOL-C24**
- claim: Refactor only in small behaviour-preserving steps, with the system never broken for more than minutes and the checks green; larger rearrangement is restructuring and needs different controls.
- level: principle; stack: neutral
- sources: S10 (small behaviour-preserving transformations, "not broken for more than a few minutes"), S09 ("only refactor when your tests are green")
- agreement: consensus; certainty: grounded
- boundary: VERIFY (the check that detects behaviour change)

**EVOL-C25**
- claim: Time each tidying by cost comparison: tidy first when tidying plus the changed behaviour costs less than the behaviour change alone; tidy after, later, or never otherwise, and never when the code will not change again.
- level: decision; stack: neutral
- sources: S11 (first, after, later, never; the "never" reason; the cost inequality quoted in a search summary, rest of the essay paywalled), S09 (preparatory refactoring before a feature)
- agreement: majority; certainty: grounded for the options and for "never", inferred for the inequality (search summary only)

**EVOL-C26**
- claim: Refactor opportunistically, by whoever touches the code, as part of ordinary work; dedicated, scheduled refactoring is the exception.
- level: decision; stack: neutral
- sources: S09 (campsite rule; "should hardly ever need to plan refactoring"; barriers such as code ownership and feature branches), S39 (Google adds survey-tracked investment in reduction, a coalition, and a maturity model; secondary), S18 (maintainability as capability)
- agreement: contested; certainty: grounded for Fowler's position, inferred for the alternative
- positions: (a) opportunistic only (S09): serves flow, small risk; wins when tests are strong and ownership is shared. (b) opportunistic plus explicit capacity or programme for structural debt (S39, secondary; and migrations, C14): serves visibility and protection from feature pressure; wins when debt is cross-team, so no one touches it in passing. Fowler himself allows "a day or two" for a gnarly lump.

**EVOL-C27**
- claim: Treat maintainability as a measurable capability: ease of finding, reusing and changing code across the organization, and ease of adding and migrating dependency versions; track searchability, time to change code in another team's area, duplicate and unused code, version consistency, and length of dependency upgrade cycles.
- level: practice; stack: neutral
- sources: S18 (Definition, Key Practices, Measurement Approaches, Findings)
- agreement: consensus (single source); certainty: grounded
- boundary: ADOPT (dependency upgrades)

**EVOL-C28**
- claim: Code is a liability, not an asset: value lies in functionality, so aim for more functionality per unit of code, and removing obsolete systems is one of the most efficient ways to improve that ratio.
- level: principle; stack: neutral
- sources: S02 (Why Deprecate, Code as Liability)
- agreement: consensus; certainty: grounded

**EVOL-C29**
- claim: Do not leave code that is no longer intended for use on production systems: a regulator found that lacking controls to prevent activation of code no longer intended for use, left on servers that accessed the market, was a contributing control failure in an incident that lost over 460 million dollars in 45 minutes.
- level: principle; stack: neutral
- sources: S24 (introduction, paragraph 9.D, paragraph 10)
- agreement: consensus (one T1 case); certainty: grounded for the finding; the claim "removal prevents this class" is inferred
- boundary: DELIVER (orderly deployment)

**EVOL-C30**
- claim: Announce retirement in two distinct stages with distinct signals: deprecation (no longer recommended, still working) and sunset (will stop responding at a stated time), where the sunset time is never earlier than the deprecation time; for HTTP interfaces use the Deprecation and Sunset header fields.
- level: practice; stack: HTTP APIs (the two-stage principle is neutral)
- sources: S21 (Relationship to Deprecation, hints), S22 (Relationship to Sunset: "MUST NOT be earlier"), S35 (Deprecation, Link, Sunset headers; agreement, migration guide, end-of-life date, blackouts, final retirement)
- agreement: consensus; certainty: grounded

**EVOL-C31**
- claim: Set a support window before removal that depends on the stability tier of what is removed, and put it in a published policy: stable interfaces are deprecated but not removed within a major version; pre-release interfaces get a fixed period (9 months or 3 releases, whichever is longer); experimental ones may go at any release; and at least one minor release carrying the deprecation precedes removal in a major release.
- level: decision; stack: neutral (the numbers are Kubernetes-specific)
- sources: S23 (Rule 4a, rationale: covers version skew), S20 (Deprecation FAQ)
- agreement: majority; certainty: grounded
- positions: tiered fixed windows (S23, S20): serves consumer predictability; costs maintainers carrying old forms; wins with many external consumers. Case-by-case (implicit in S35, which gives no durations): serves speed; wins with few known consumers. Forces: reversibility, consumer friction, cost of ownership.

**EVOL-C32**
- claim: Deprecation warnings must be actionable and relevant, because excess causes alert fatigue; also expose them in machine-readable form (response warning header, audit annotation, a usage metric labelled with the removal release) so remaining users are found.
- level: practice; stack: neutral (the machine forms are Kubernetes and HTTP)
- sources: S02 (Deprecation Warnings), S23 (Deprecation Announcements)
- agreement: consensus; certainty: grounded

**EVOL-C33**
- claim: Choose advisory or compulsory deprecation deliberately: advisory (no deadline) rarely completes unless the replacement is transformatively better; compulsory needs a firm deadline plus a staffed migration team.
- level: decision; stack: neutral
- sources: S02 (Advisory, Compulsory Deprecation)
- agreement: contested; certainty: grounded (one source states both sides)
- positions: advisory serves consumer autonomy and no central load, wins when the replacement sells itself; compulsory serves completion and removal of the old cost, wins when the old form has real upkeep cost or risk. Forces: autonomy versus completion; risk of unfunded mandate.

**EVOL-C34**
- claim: Before switching off, verify who or what still uses the system, restrict access reversibly for a period to flush out remaining users (controlled blackouts, restrictive controls with a way back), keep restorable backups and recorded metadata, then remove.
- level: practice; stack: neutral
- sources: S25 (Implementation steps: verify use, record metadata and create backups, prevent access with ability to revert), S35 (usage assessment, rolling blackouts)
- agreement: consensus; certainty: grounded
- boundary: RECOV (backup retention), SECD (data retention)

**EVOL-C35**
- claim: A retirement has an explicit project owner for whom removal is the primary objective, and measurable intermediate milestones (for example deleting key sub-components), not only the final removal.
- level: practice; stack: neutral
- sources: S02 (Process Ownership, Incremental Milestones)
- agreement: consensus (single source); certainty: grounded

**EVOL-C36**
- claim: A retirement covers everything attached to the system: licences, attached storage, DNS entries, domain membership, and entries in configuration, monitoring, automation and security tooling, and is checked against compliance requirements.
- level: practice; stack: neutral
- sources: S25 (Create and implement a decommissioning process, Follow your internal decommissioning process)
- agreement: consensus (single source); certainty: grounded

**EVOL-C37**
- claim: Decide to retire on stated grounds (a replacement of comparable or better function exists, upkeep cost exceeds value, the technology is out of date, the strategy changed, or use is low), and record the decision like any other.
- level: decision; stack: neutral
- sources: S02 (Why Deprecate), S35 (Rationale for Retiring), S12 and S13 (the record form)
- agreement: consensus; certainty: grounded for the grounds, inferred for "record the retirement decision" (join of S35 and S12)

**EVOL-C38**
- claim: Add a technology as a replacement, not as an addition: when adopting a new tool, commit to replacing the older one and plan its retirement, since the long-term costs of keeping an extra system reliable exceed the inconvenience of building with it.
- level: principle; stack: neutral
- sources: S29 (selection and retirement strategy), S30 (Hidden Burden of Diversity, When to Add New Tech), S02 (reducing redundancy and cognitive burden)
- agreement: majority; certainty: grounded
- note: complements the sibling's boring-technology claims (ARCH-C27 to C33), which cover the choice, not the retirement of the replaced tool.

**EVOL-C39**
- claim: Keep an explicit, shared position per technology (adopt, trial, assess, hold) with a decision trail, so a team knows what to standardize on, evaluate and stop using.
- level: practice; stack: neutral
- sources: S32 (the four rings and building one's own radar), S33 (decisions recorded in source control)
- agreement: majority; certainty: grounded for the rings, inferred for "decision trail" (stated in a search summary only)

**EVOL-C40**
- claim: Decide how firmly the stack is held: a mandated list, an opinionated supported path with unsupported departures allowed, or free choice per component.
- level: decision; stack: neutral
- sources: S31 (golden path: supported, not mandated; fewer decisions, higher chance of automatic upgrades), S19 (polyglot choice per service, standards that "become standards" through use), S17 (one-version rule: developers never choose which version), S30 (locally optimal solutions proliferate without governance)
- agreement: contested; certainty: grounded for positions
- positions: (a) mandate a small set (S17 for dependency versions, S30): serves low cognitive load, upgrade cost, shared operations; costs local fit; wins with many teams sharing platform and on-call. (b) paved path, departure allowed but unsupported (S31): serves autonomy with a cheap default; costs a tail of unsupported variants. (c) polyglot freedom per component (S19): serves local fit and learning; costs heterogeneity; wins with few, independently operated components. Forces: cognitive load, cost of ownership, autonomy, delivery speed.
- boundary: ADOPT for dependency version choice (one-version rule, S17: "must never have a choice of what version to depend upon"; position (c) variant is multiple versions, which S17 rejects)

**EVOL-C41**
- claim: Removing obsolete code and systems is ordinary engineering work with a declared owner and budget, not leftover work after features.
- level: principle; stack: neutral
- sources: S02 (Process Ownership: "teams require removal as their primary objective"), S03 (infrastructure teams own LSCs), S28 and S09 contrast (feature-first culture), S07 (debt as managed, not ignored)
- agreement: majority; certainty: inferred (synthesis of S02, S03, S07; no source states it as one rule)

### Gaps

- Original Lehman papers, Parnas "Software Aging" and Brooks's second-system argument not read; C15 and C17 lean on T2 and T4 summaries. Open.
- Empirical effect of ADRs on delivery, onboarding or defects: no source found measuring it; the ADR benefits in S13, S14 and S12 are practitioner claims. Open.
- Empirical comparison of debt-repayment policies (opportunistic versus dedicated capacity): none read; C26 positions rest on practitioner texts and a secondary summary. Open.
- Google's debt paper figures come from a T4 summary and the abstract; the full text (IEEE Software) was not read. Certainty of C21, C22 and C23 figures is therefore inferred.
- No source read on retirement of software the team owns that is not an API, service or cloud resource (libraries, CLIs, internal tools): C30 to C36 generalize from API, platform and cloud sources. Inferred.
- Quantitative guidance on support-window length beyond Kubernetes and SemVer: open; the Kubernetes numbers are one project's choice.
- Fowler "Preparatory Refactoring" (404) and Beck's full economic argument (paywall) not read; C25 uses the free excerpt.
- Cost of diversity in numbers (cost per additional technology): no source; McKinley's three-token figure is an assertion (already held by the sibling).

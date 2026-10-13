# rollup: judge records of the ROOT node and the seven L1 nodes

Unit: the top of the tree. ROOT (the L0 goal) and the seven L1 nodes OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE, in the order the maintainer decided (`target_hierarchy.md`). Each L1 record is a roll-up of its judged L2 records (units J1 to J9, final after review and final pass); ROOT is a roll-up of the seven L1 records. A roll-up states no fact of its own (MD-03): every fact is held at its L2 or L3 node, and the links point there. Binding: MD-01 (the best, not the average), MD-02 (outcomes, whoever does the work), MD-03 (one location per fact), MD-04 (EVOLUTION is a top-level branch), MD-05 (scope).

Certainty words: grounded = named sources or a maintainer decision support it; inferred = follows from them; open = what is missing is stated. A roll-up carries its own certainty, never its children's.

Re-rolls done here: ASSURANCE is re-rolled from all nine L2 nodes (cross-unit fix X2), replacing the three-of-nine roll-up of J2; CONSTRUCTION, OPERATION, OWNERSHIP, EVOLUTION and TRANSVERSE replace the provisional L1 records of their units; CHANGE_FLOW has no earlier L1 record and is written here from its eight L2 records.

Pinned:
- Records written: 8 (ROOT, OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE).
- Decisions marked undecided: none.
- Open items found across units: 41 (2 flags still open on a record, 39 open items kept in a Certainty field); listed at the end in "Still open".
- Settled decisions disagreed with: none.

---

## ROOT Software Development Philosophy

Intent: a team delivers, and keeps delivering, a system that does what is intended, at a cost it can sustain.

1. **Decision.** A team owns the outcome by deciding, for each capability, whether it writes, adopts or rents it, and by pricing the way out before it depends on it (OWNERSHIP). It knows each property holds because each property has a named mechanism, at a named stage, that runs on every change, has a trustworthy signal and cannot be skipped (ASSURANCE). It constructs code that is correct at its boundaries and changes in few places (CONSTRUCTION); changes the system in small, reviewed, reversible steps that promote one built artifact (CHANGE_FLOW); operates it against stated objectives, with recovery proven before it is needed (OPERATION); and lets it evolve by recorded decisions, incremental change, repaid debt, announced retirement and a small set of technologies (EVOLUTION); documentation, security practice, configuration and secrets, and development environments carry the same discipline across all of these (TRANSVERSE). Outcome, whoever does the work (MD-02): the design was good, the testing was good, the review was trustworthy, and what runs is what was reviewed.
2. **Grounds.** Roll-up of the seven L1 records below; the order and the split are the maintainer's decisions (MD-01 to MD-05, `target_hierarchy.md`). The unifying claim, that no single control is relied on and a pass is believable, rests on the ASSURANCE grounds (L1538, L1550, L1558, L1562, L1546).
3. **Positions.** The choices made at this height, from the maintainer's decisions: P1 two decision branches first (OWNERSHIP, ASSURANCE), then the realization branches in the order construct, change, operate, evolve, then the cross-cutting branch last. P2 one branch per lifecycle stage (code, build, release, operate) with each property's checks inside the stage that runs them. P3 one branch per quality property with its practice inside it. P4 a branch for who does the work (human team or AI agent contributors).
4. **Rejected.** P2 as the top split: the guarantee of one property (documentation, security, data, availability) would be spread over several stages and have no single home, which breaks one location per fact (MD-03); it is best as the realization view, which CHANGE_FLOW and OPERATION already give. P3 as the top split: it merges "how we know it holds" with "how we do it" for each property, which MD-03 keeps apart; best for a guideline about one property only. P4: who writes the code is not a principle (MD-02); AI contributors enter as the outcomes the other branches require when change arrives at volume or from a non-human author. EVOLUTION folded into CHANGE_FLOW: ruled out by MD-04; change over time, decisions and retirement are a branch of their own. Regulated contexts and software that is not a hosted service: deferred (MD-05); best in a guideline written for them.
5. **Context.** None at this level. There is no default team (MD-02); the conditions that move a decision (criticality, consumer reach, change volume, team and platform sharing, threat model) are on the L2 and L3 nodes that carry them.
6. **Certainty.** Grounded for the order and the split (maintainer decisions). Inferred for the whole as one claim: no source states the seven-branch guideline, and the unification rests on each branch's own certainty. The 41 open items (see "Still open") are cadences, numeric thresholds, one-source minority views and two flags; none contradicts a decision at this height.
7. **Flags.** none at this height; the two flags still open sit on ASSURANCE.RULES.4 and EVOLUTION.TECHNOLOGY.4.

Constraints: no property that must hold lacks a mechanism, a stage and a recurring trigger; no capability enters without a recorded decision; no change reaches production except through the reviewed, gated path; no guideline decision depends on who wrote the code.
Links: children OWNERSHIP, ASSURANCE, CONSTRUCTION, CHANGE_FLOW, OPERATION, EVOLUTION, TRANSVERSE.

---

## OWNERSHIP Ownership

Intent: for each capability, the team writes it, adopts it (a library or tool it runs) or rents it (an external service or API) only when a stated reason outweighs the ongoing cost, and keeps the choice reversible in proportion to what it would cost to be wrong.

1. **Decision.** Nothing is added by default: every external capability enters through a recorded, per-need decision (STANCE, SELECTION). Once in, it is declared, locked, watched and updated as a managed liability, and licence obligations are known before the code is used (LIFECYCLE, LICENCE). Its effect is bounded and its exit is priced in proportion to what failure would cost, not assumed (CONTAINMENT); a rented service is chosen on commitments, stability promise, exit and contract terms and vendor posture (SERVICES). Outcome: the team knows what it depends on, why, and what leaving would cost.
2. **Grounds.** Roll-up of the six L2 records (29 L3 records): the cost-of-ownership default, the lifecycle and licence mechanics and the rented-service checks are consensus rows; the proportionality scaling (criticality, switching likelihood) is inferred.
3. **Positions.** Choices at this height: the six sub-questions are ordered by the life of a dependency (need, choice, upkeep, bounding and exit, rented services, licence); P1 the default is not to add; P2 add where it saves time (speed-first). The competing practices per question are at the L3 nodes.
4. **Rejected.** P2 as a default: it counts the benefit and omits the lasting cost; best where the capability is neither core nor critical and the exit is cheap, which STANCE.2 already treats as the lowest-ownership case of the cost test. Splitting services and licences into other branches: a rented service is one of the three ways to hold a capability, so it stays with the other two.
5. **Context.** Criticality and replaceability of the component set vetting depth, exit capability and vendor assessment; recorded at the L2 and L3 nodes.
6. **Certainty.** Inferred as a roll-up. Grounded for the lifecycle, licence-reading and rented-service mechanics; inferred for the scaling; open at four nodes (CONTAINMENT.4, SERVICES.2, SERVICES.5, LICENCE.3).
7. **Flags.** none.

Constraints: no dependency, layer or service is adopted without a recorded reason; no adopted artifact is installed from anything but the lock; no rented service is adopted without a tested way out proportional to its criticality.
Links: children STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES, LICENCE; carried out by EVOLUTION (decommissioning, technology count), CHANGE_FLOW, TRANSVERSE.CONFIG.

---

## ASSURANCE Assurance

Intent: for each property that must hold, which mechanism, at which stage, guarantees it, running on every change so that it stays true; one placement node per property, plus the rules common to every property.

1. **Decision.** Every property that must hold has a named mechanism at a named stage that runs on every change, and none rests on one control or on the author's own judgement. A check blocks while its measured false-alarm rate is within the budget the team states, and a check that needs judgement advises in review under a budget; a pass can be believed, gates cannot be skipped, review is independent and binds the exact content, and every change meets one bar with evidence (RULES). Behaviour is pinned by self-testing code whose power is measured (BEHAVIOUR); interface compatibility has a definition, a contract test and one source of description (CONTRACTS); stored data is protected where every write path converges (DATA_INTEGRITY); documentation cannot drift because it travels with the change and is gated (DOCS_SYNC); security is verified at a depth set by risk and limits on automation are enforced in tooling (SECURITY); speed and capacity are verified against the real workload with a baseline (PERFORMANCE); a degraded mode, a bounded call and a proven restore guarantee availability and recovery (AVAILABILITY); and what runs is tied to reviewed source by a protected mainline and verified build provenance (ARTIFACT). Outcome: the design was good, the testing was good, the review was trustworthy, and what runs is what was reviewed (MD-02).
2. **Grounds.** Roll-up of all nine L2 records (RULES, BEHAVIOUR, CONTRACTS from J2; DATA_INTEGRITY, DOCS_SYNC, SECURITY from J3; PERFORMANCE, AVAILABILITY, ARTIFACT from J4), 44 L3 records under nine L2 records, as cross-unit fix X2 requires. The shared claim "no single control is relied on and a pass is believable" rests on L1538, L1550, L1558, L1562, L1546; the untested-is-absent rule on L032, L1097, L451, L120; the artifact claim on L1063 (REG-1037, REG-114), L151, L1244.
3. **Positions.** Choices at this height: P1 one placement node per property (decision), with the practice in a realization branch (MD-03); P2 one assurance practice per lifecycle stage; P3 a single global quality gate. The competing practices per property are at the L3 nodes.
4. **Rejected.** P2 and P3: they leave a property without one owner of its guarantee, so a gap in one stage is invisible; P3 also makes the signal a single point of failure; best as the realization view (CHANGE_FLOW) and as the floor RULES.5 sets for every change. A property list without the common rules: each property would re-decide trust, placement and skippability.
5. **Context.** Criticality, change volume, consumer reach and suite maturity move individual decisions (RULES.2, RULES.4, CONTRACTS.1, BEHAVIOUR.1, BEHAVIOUR.6); recorded at the L3 nodes. None at this height.
6. **Certainty.** Inferred as a roll-up: no source states the nine-property set as a whole. Grounded for the principle that a pass is believable and no control stands alone; grounded for the nine children's cores, with inferred numeric defaults. Open at eight places (RULES.4 two, BEHAVIOUR.1, BEHAVIOUR.6, SECURITY.3, AVAILABILITY.4, AVAILABILITY.5, ARTIFACT.1).
7. **Flags.** The maintainer point on RULES.4 (can an automated reviewer be the independent check; default applied) is open; see "Still open". The earlier flag F9 (re-roll after J3 and J4) is closed by this record.

Constraints: MUST every property have a mechanism, a stage and a recurring trigger; MUST every check have a measured false-alarm budget; MUST no gate be skippable; MUST every approval bind the exact content that ships.
Links: children RULES, BEHAVIOUR, CONTRACTS, DATA_INTEGRITY, DOCS_SYNC, SECURITY, PERFORMANCE, AVAILABILITY, ARTIFACT; carried out by CONSTRUCTION, CHANGE_FLOW, OPERATION, TRANSVERSE.

---

## CONSTRUCTION Construction

Intent: how code is structured, in its language-neutral form, so that it is correct and stays changeable; it carries out what OWNERSHIP and ASSURANCE decide and re-decides none of it.

1. **Decision.** Design is derived from usage down to code in the order of the cost of reversing each decision, and effort goes where error is costly (DESIGN). The system starts as the simplest shape that serves and is cut by the decision each module hides and by business concept (SYSTEM_SHAPE, HIDING). What crosses a trust boundary is parsed once into a precise form under a positive definition of valid, and never reaches an interpreter as code (BOUNDARY, DATA_NOT_CODE). Each fact has one place, dependencies flow one way and are checked, names carry concepts (STATE, DEPENDENCY_DIRECTION, NAMING); logic is placed by the property it must have (PARADIGM); and a process can be stopped and replaced at any time (PROCESS). Outcome: the code is correct at its boundaries and a change touches few places.
2. **Grounds.** Roll-up of the ten L2 records (37 L3 records, 87 rows). Grounded core: parse at the edge (consensus, two T1 sources), data kept from becoming code (T1 consensus); the rest is practitioner essay and maintainer practice.
3. **Positions.** Choices at this height: P1 language-neutral principles with the scope condition stated where the evidence is one language's; P2 per-language rules. The competing practices per question are at the L3 nodes.
4. **Rejected.** P2: MD-05 admits code design only where it holds for every language; best in a per-language guideline. Restating decisions of ASSURANCE.CONTRACTS or DATA_INTEGRITY here: BOUNDARY holds the form a boundary takes, CONTRACTS holds how compatibility is verified (MD-03).
5. **Context.** Team count and release independence move SYSTEM_SHAPE; consumer reach moves BOUNDARY; hosted-service scope bounds PROCESS (MD-05).
6. **Certainty.** Inferred as a roll-up: the sources are largely practitioner essays and maintainer practice, with no controlled evidence for the structure rules. Grounded for the parse-at-the-edge and data-not-code cores. Open at four nodes (BOUNDARY.3, STATE.4, DEPENDENCY_DIRECTION.2, DATA_NOT_CODE.3).
7. **Flags.** none.

Constraints: no untrusted data reaches an interpreter as code, command, query, path or object; no module cycle; no effect at module load; a credential or token is accepted only if every step its specification requires passes.
Links: children DESIGN, SYSTEM_SHAPE, HIDING, BOUNDARY, STATE, DEPENDENCY_DIRECTION, NAMING, PARADIGM, DATA_NOT_CODE, PROCESS; realizes ASSURANCE.CONTRACTS, ASSURANCE.DATA_INTEGRITY, ASSURANCE.RULES; related ASSURANCE.SECURITY, TRANSVERSE.SECURITY, TRANSVERSE.CONFIG, EVOLUTION.INCREMENTAL.

---

## CHANGE_FLOW Change Flow

Intent: how a change travels from a developer to production and back out again: version control and integration, review, build, release, deploy, rollback, data and schema change, and the measurement of delivery.

1. **Decision.** Everything needed to build, deploy and restore lives in version control, and work is integrated into one mainline in small, frequent, attributable changes (INTEGRATION). Review is independent, accountable and bound to the exact content, its depth following risk (REVIEW). One scripted, hermetic build produces one artifact that is promoted unchanged (BUILD); releases are small, identified by what the identifier promises and separable from deployment where needed (RELEASE); deployment is automated by the same process in every environment, exposes a release progressively and replaces instances rather than modifying them (DEPLOY). The way back is decided before the change ships (ROLLBACK); every schema and data change is a reviewed, versioned, once-only script, ordered compatibly with the code, rehearsed and watched (DATA_CHANGE); and delivery is judged by outcomes, never by volume of code (MEASURE). Outcome: what ships was reviewed, built once and is reversible, and going back is a rehearsed move.
2. **Grounds.** Roll-up of the eight L2 records (34 L3 records) written here (no L1 record existed in J6); the branch carries out ASSURANCE.RULES, ARTIFACT, DATA_INTEGRITY and AVAILABILITY and re-decides none of them. Build, release and review rest on consensus rows; DATA_CHANGE (48 rows) rests mostly on one maintainer practice that public practice is read as agreeing with.
3. **Positions.** Choices at this height: P1 one mainline with one promoted artifact and one pipeline; P2 long-lived branches or per-environment builds. The competing practices per question are at the L3 nodes.
4. **Rejected.** P2: it delays integration and tests something other than what ships; best where releases are cut from supported maintenance lines, which INTEGRATION.3 holds as the release-branch condition.
5. **Context.** Release model moves INTEGRATION.3 and RELEASE; scale and downtime tolerance move DATA_CHANGE; criticality and test maturity move RELEASE.4; recorded at the L3 nodes.
6. **Certainty.** Inferred as a roll-up. Grounded for build-once, small batches and the review principles; inferred for the numeric defaults and for much of DATA_CHANGE (single-source practice). Open at six nodes (INTEGRATION.1, INTEGRATION.4, REVIEW.4, RELEASE.2, DEPLOY.4, MEASURE.1).
7. **Flags.** none.

Constraints: no change reaches production except from reviewed mainline through the one pipeline; the deployed artifact is the one that was built; every change has a named way back before it ships; no schema or data change is applied as hand-typed SQL.
Links: children INTEGRATION, REVIEW, BUILD, RELEASE, DEPLOY, ROLLBACK, DATA_CHANGE, MEASURE; realizes ASSURANCE.RULES, ASSURANCE.ARTIFACT, ASSURANCE.DATA_INTEGRITY, ASSURANCE.AVAILABILITY; related OPERATION.FEEDBACK, CONSTRUCTION.PROCESS.

---

## OPERATION Operation

Intent: how the running system is kept within its reliability targets and recovered when it fails.

1. **Decision.** The running system is held to a stated reliability objective below 100 percent, measured as users experience it, with the gap governed by an agreed rule (RELIABILITY). A human is paged only for what needs a human now (ALERTING); the system is observable well enough to answer questions nobody planned, at a cost the team can afford (TELEMETRY); incidents are declared on written conditions, run by named roles and learned from (INCIDENTS). Capacity is planned against a measured breaking point (CAPACITY); a workload launches only after a readiness review (READINESS) with procedures that were run before they were needed (RUNBOOKS); recovery is designed backward from stated objectives (RECOVERY); and delivery feedback from production is tracked per service and never made a target (FEEDBACK). Outcome: the system stays within its objectives at a cost and load the team can sustain, and when it fails it is restored within them.
2. **Grounds.** Roll-up of the nine L2 records (31 L3 records, 109 rows); the branch carries out ASSURANCE.AVAILABILITY and PERFORMANCE: AVAILABILITY holds the proof, OPERATION holds the practice (MD-03). Reliability, alerting, incident and recovery mechanics rest on consensus and a few authoritative practitioner sources (SRE literature, cloud-provider guidance, DORA).
3. **Positions.** Choices at this height: P1 reliability stated as an objective users would recognise, traded by rule; P2 maximise availability without a stated target. The competing practices per question are at the L3 nodes.
4. **Rejected.** P2: it has no stopping rule, so cost and speed are traded by argument; best never for a service with any cost of change.
5. **Context.** Objective consequence, team size, load shape, threat model and criticality, at the L3 nodes.
6. **Certainty.** Inferred as a roll-up. Grounded for the objective, symptom-paging, incident-process and recovery-ladder cores; inferred for small-team treatments of large-operator figures; open at nine nodes (RELIABILITY.3, ALERTING.2, TELEMETRY.6, INCIDENTS.1, CAPACITY.2, READINESS.3, RUNBOOKS.2, RECOVERY.5, FEEDBACK).
7. **Flags.** none.

Constraints: no page without a human action needed now; no workload launched without a readiness review; no backup, plan or restore treated as present until tested (ASSURANCE.AVAILABILITY); no target set on the delivery measures of FEEDBACK.
Links: children RELIABILITY, ALERTING, TELEMETRY, INCIDENTS, CAPACITY, READINESS, RUNBOOKS, RECOVERY, FEEDBACK; realizes ASSURANCE.AVAILABILITY, ASSURANCE.PERFORMANCE; related TRANSVERSE.PRIVACY (backup retention), TRANSVERSE.SECURITY_MONITORING.

---

## EVOLUTION Evolution

Intent: how the system and its decisions change over time, so that it keeps working and stays changeable at a cost the team can sustain.

1. **Decision.** The reasons for significant decisions are recorded where the code lives and are superseded, never rewritten (DECISIONS). Change is made in steps that keep the system releasable, and every dual-support phase ends with a removal (INCREMENTAL). Debt is a known, inventoried liability repaid where code changes (DEBT); obsolete forms are retired on stated grounds in two announced stages by an owner with a budget (DECOMMISSION); and the set of technologies stays small because each addition is a replacement (TECHNOLOGY). Outcome: the system keeps working while it changes, the reasons for past decisions can be recovered, and nothing old stays by neglect.
2. **Grounds.** Roll-up of the five L2 records (27 L3 records). Grounded: decision records (consensus across architecture-record sources), expand-migrate-contract, two-stage deprecation and the retirement checklist. Inferred: debt-repayment timing, rewrite conditions, technology-firmness conditions (single-source or contested rows).
3. **Positions.** Choices at this height: P1 a top-level branch (MD-04); P2 a section of CHANGE_FLOW; P3 left to each team's judgment.
4. **Rejected.** P2: change over time is longer-lived than a delivery pipeline and concerns decisions, debt and retirement that no pipeline stage owns; MD-04 rules it out. P3: without recorded decisions and an owner, retirement and debt repayment do not happen; best for a throwaway prototype with a known end.
5. **Context.** Expected lifespan and consumer count move INCREMENTAL; shared platform and on-call move TECHNOLOGY.3; consumer reach moves DECOMMISSION.
6. **Certainty.** Inferred as a roll-up. Grounded for the record, expand-migrate-contract and staged-retirement mechanics; inferred for debt timing and technology firmness. Open at two places (TECHNOLOGY.4 flag, INCREMENTAL.3).
7. **Flags.** The contested single-store row at TECHNOLOGY.4 is open; see "Still open".

Constraints: no significant decision without a record that outlives its author; no incompatible change without a removal step and an owner; no retirement without verified usage and a stated deadline; no technology added without the retirement of what it replaces or a stated reason none exists.
Links: children DECISIONS, INCREMENTAL, DEBT, DECOMMISSION, TECHNOLOGY; realizes OWNERSHIP.STANCE, SELECTION, LIFECYCLE, SERVICES, ASSURANCE.BEHAVIOUR, ASSURANCE.CONTRACTS; see CHANGE_FLOW.INTEGRATION, DATA_CHANGE, ROLLBACK, REVIEW, TRANSVERSE.PRIVACY.

---

## TRANSVERSE Transverse

Intent: the practices that cut across every branch: documentation practice, security practice (including monitoring, privacy and retention), configuration and secrets, development environments.

1. **Decision.** Each cross-cutting concern is an owned, recorded practice whose guarantee is held elsewhere (documentation sync and security verification are in ASSURANCE). Documentation is sized by its readers and organised by their need (DOCS). Security is anchored in a published framework, modelled at design time, owned, and answered by one vulnerability loop (SECURITY); security events are logged, protected, detected on and kept apart from the business audit trail (SECURITY_MONITORING). Personal data is minimised, retained on a recorded schedule and erasable (PRIVACY). Configuration and secrets stay out of code and artifact and reach the process through short-lived, audited custody (CONFIG); development environments are code, separated from production and hardened (ENVIRONMENTS). Outcome: the guarantees ASSURANCE decides have a practice that can be carried out and checked.
2. **Grounds.** Roll-up of the six L2 records (29 L3 records). Grounded in published frameworks and cheat sheets (OWASP, regulator guidance, platform documentation); each branch states only what ASSURANCE.DOCS_SYNC and ASSURANCE.SECURITY do not (MD-03).
3. **Positions.** Choices at this height: P1 one cross-cutting branch after the realization branches; P2 each concern inside the branch it touches (config in CHANGE_FLOW, privacy in OPERATION, and so on).
4. **Rejected.** P2: the same practice would be restated in several branches, or placed in only one of the several that need it; best for a guideline small enough that one team owns every branch. A separate branch for each concern: six branches of two to six nodes each add structure without a distinct outcome.
5. **Context.** Regulated contexts are deferred (MD-05); the EU legal text is restated neutrally; criticality and platform shape move CONFIG.2.
6. **Certainty.** Inferred as a roll-up of grounded components. Open at eight nodes (DOCS.4, SECURITY.1, SECURITY.2, SECURITY.6, PRIVACY.2, PRIVACY.3, PRIVACY.4, CONFIG.1).
7. **Flags.** none.

Constraints: no configuration or secret in code or artifact; no exposed secret treated as safe; no personal data kept without a recorded purpose and period; no development environment that can reach production by accident.
Links: children DOCS, SECURITY, SECURITY_MONITORING, PRIVACY, CONFIG, ENVIRONMENTS; realizes ASSURANCE.DOCS_SYNC, ASSURANCE.SECURITY; see OPERATION.TELEMETRY, OPERATION.ALERTING, OPERATION.RECOVERY, CHANGE_FLOW.BUILD, CHANGE_FLOW.DEPLOY.

---

## Still open

Found by reading every `judged.md` (Flags fields, Certainty fields, closing sections). 41 items: 2 flags open on a record (F), 39 open points kept in a Certainty field (C). Every other flag of every unit is settled; no record contradicts a decision above.

OWNERSHIP (4)
- C OWNERSHIP.CONTAINMENT.4: how far sandboxing of a risky dependency is practical is not sourced; the decision applies it where practical for the ecosystem.
- C OWNERSHIP.SERVICES.2: no source says whether consumers act on a provider's deprecation signals.
- C OWNERSHIP.SERVICES.5: the third and fourth vendor-assessment positions have no source; composed by the judge.
- C OWNERSHIP.LICENCE.3: where the line falls between a separate component and a linked one stays with legal review (interface test grounded in part, REG-188).

ASSURANCE (8)
- F ASSURANCE.RULES.4: can an automated reviewer in its own context be the independent check? Default applied (option A, different-kind reviewer for high-risk changes); awaiting the maintainer (`final_pass/maintainer_points.md`).
- C ASSURANCE.RULES.4: whether a regulation still requires per-change approval by an external board was not read (regulated contexts deferred, MD-05).
- C ASSURANCE.BEHAVIOUR.1: position P6 is open (inferred absence, not confirmed).
- C ASSURANCE.BEHAVIOUR.6: effect size of mutation testing is unknown.
- C ASSURANCE.SECURITY.3: no source gives a penetration-test period or a trigger tied to maturity.
- C ASSURANCE.AVAILABILITY.4: no source fixes the backup-restore cadence beyond "regular"; left to the team's objectives.
- C ASSURANCE.AVAILABILITY.5: no source gives a production-drill frequency.
- C ASSURANCE.ARTIFACT.1: what the archived build record must contain is open (REG-004 names it only).

CONSTRUCTION (4)
- C CONSTRUCTION.BOUNDARY.3: the checklist reading of L1287 is open.
- C CONSTRUCTION.STATE.4: no preference between immutability and restriction is established.
- C CONSTRUCTION.DEPENDENCY_DIRECTION.2: layering is grounded only through the settled enforcement rule; as a standalone principle it is open in the origin.
- C CONSTRUCTION.DATA_NOT_CODE.3: the clause "checked after resolution and used without a race" has no grounding claim (kept as inferred).

CHANGE_FLOW (6)
- C CHANGE_FLOW.INTEGRATION.1: which repository layout wins in general is open (one T2 source).
- C CHANGE_FLOW.INTEGRATION.4: no source ranks squash, merge and rebase; the squash default is inferred.
- C CHANGE_FLOW.REVIEW.4: no study of AI-reviewer accuracy was read; vendor statements only.
- C CHANGE_FLOW.RELEASE.2: the third version-identity position is open.
- C CHANGE_FLOW.DEPLOY.4: no source compares pull-based and push-based deployment.
- C CHANGE_FLOW.MEASURE.1: the net effect of automation on delivery is open (contested, small samples, vendor sources).

OPERATION (9)
- C OPERATION.RELIABILITY.3: the minority position on the error budget (P2) is open.
- C OPERATION.ALERTING.2: burn-rate alerting rests on one authority; no independent measurement.
- C OPERATION.TELEMETRY.6: no source treats telemetry cost as a governed budget per service; adopted as inferred.
- C OPERATION.INCIDENTS.1: the high-bar position on declaring an incident is open.
- C OPERATION.CAPACITY.2: no numeric headroom is sourced.
- C OPERATION.READINESS.3: no source fixes how often the review is repeated.
- C OPERATION.RUNBOOKS.2: cost and risk of automating a wrong runbook are open (one vendor source).
- C OPERATION.RECOVERY.5: hardening against recovery speed rests on one T3 source; the opposite side is argued in no source read.
- C OPERATION.FEEDBACK: the contrary view (set targets on delivery measures) is argued in no source read.

EVOLUTION (2)
- F EVOLUTION.TECHNOLOGY.4: contested row (one general-purpose store for several roles) resting on one-project or commercially interested sources; no final-pass resolution addressed it.
- C EVOLUTION.INCREMENTAL.3: whether any position on replacement versus rewrite wins in general is open; the rewrite conditions are inferred.

TRANSVERSE (8)
- C TRANSVERSE.DOCS.4: the condition under which a generated changelog would be best is inferred and open.
- C TRANSVERSE.SECURITY.1: the ASVS level definitions were not read (L250).
- C TRANSVERSE.SECURITY.2: no evidence that maturity or level scores raise outcomes.
- C TRANSVERSE.SECURITY.6: the commercial case for a bounty is open (vendor documentation not read).
- C TRANSVERSE.PRIVACY.2: no source gives a retention period.
- C TRANSVERSE.PRIVACY.3: whether erasure must reach logs and every copy on request is contested; no source read settles it.
- C TRANSVERSE.PRIVACY.4: the body of the privacy-risk framework was not read.
- C TRANSVERSE.CONFIG.1: the clause "drawn, compared, stored and logged only through audited platform mechanisms" has no claim grounding it beyond CONFIG.4 and SECURITY_MONITORING.3.

Closed by this roll-up (not counted): J2 flag F9 (ASSURANCE re-roll, cross-unit X2) and the "provisional, re-rolled in wave 3" notes on the L1 records of CONSTRUCTION, OPERATION, OWNERSHIP and EVOLUTION; CHANGE_FLOW now has its L1 record.
For the maintainer, not open: 20 decisions that go against the maintainer's codified practice are listed in `final_pass/maintainer_points.md`.

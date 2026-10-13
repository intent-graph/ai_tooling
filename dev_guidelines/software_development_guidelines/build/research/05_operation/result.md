# OPERATE research result (slot 05_operation)

## L1 headline

Best practice for running and watching shipped software is well settled at principle level (user-centric SLIs and SLOs, error budgets, symptom-based paging, blameless postmortems, vendor-neutral instrumentation) and contested at implementation level (how to store telemetry, how to sample, how hard to enforce budgets); certainty is high where Google SRE, OpenTelemetry and DORA agree, and moderate on the contested points because several T2/T3 sources could not be read.

Pinned:
- Sources by tier: T1 = 7, T2 = 16, T3 = 6, T4 = 0 (29 read in total).
- Claims: 38.
- Contested topics: telemetry storage model (three pillars vs wide events); sampling (head, tail, none); how hard an exhausted error budget binds releases; whether SLO targets may start from current performance; chaos experiments in production vs pre-production; incident-declaration threshold (early vs high bar).
- Failed fetches on a T1 source: none failed outright. NIST SP 800-61 Rev. 3 was read at its landing-page level only (scope and CSF 2.0 alignment, no body text); claims drawn from it are limited accordingly.
- Failed fetches on non-T1 sources: Rob Ewaschuk "My Philosophy on Alerting" (Google Doc, unreadable, only a search snippet seen), Etsy debriefing guide and blameless-postmortem post (HTTP 403), Atlassian incident handbook pages (page body not extracted); none is used as ground for a claim.

## L2 claims

Clusters
1. Reliability is a negotiated target below 100%, expressed as SLOs on user-centric SLIs, never as "maximum uptime". Consensus, grounded. OPERATE-C01, C02, C03, C04, C05, C06.
2. An error budget turns the SLO into a decision rule between velocity and reliability, and needs a written policy to bind. Majority (strength of enforcement contested), grounded. C07, C08, C09, C10.
3. Page only on urgent, actionable, user-visible symptoms; route everything else to tickets or logs; alert on budget burn rate with multiple windows. Consensus on symptoms, majority on burn-rate form, grounded. C11, C12, C13, C14, C15, C16.
4. Instrument every service with a small standard signal set (golden signals / RED for services, USE for resources), with percentiles not averages. Consensus, grounded. C17, C18, C19.
5. Observability means being able to ask new questions of production without shipping new code; monitoring (predefined) and observability (exploratory) are both required. Majority, grounded. C20, C21, C22.
6. Telemetry format and plumbing should be vendor-neutral and standardized (OpenTelemetry, semantic conventions, W3C Trace Context); applications emit, the platform routes. Consensus, grounded. C23, C24, C25, C26.
7. Telemetry has a cost; sampling and retention are explicit decisions. Contested, grounded. C27, C28.
8. Incident response is a rehearsed role-based process with a live record, declared early, with written severity and handoffs. Majority, grounded. C29, C30, C31.
9. Blameless postmortems with owned, tracked action items are the feedback path from production into development. Consensus, grounded (Etsy and Atlassian practice not read). C32, C33.
10. Human cost of operation is bounded: toil cap, on-call load limits, alert-to-incident ratio near 1:1. Majority (Google numbers are for large teams), grounded. C34 (plus C13).
11. Resilience is verified by experiment, not assumed. Contested on production vs pre-production, single T3 source. C28b.
12. Changes cause most outages; production feeds delivery through recovery-time and failure-rate measures, within a risk-management frame. Majority, grounded. C35, C36, C37.

Live debates (forces in tension)
- Three pillars vs wide structured events as the single store: cost of ownership and tooling maturity vs exploratory power and high-cardinality querying (C21).
- Head sampling vs tail sampling vs no sampling: cost and simplicity vs completeness of rare-error traces and operational complexity (C27).
- Error budget exhausted: hard release freeze (control, reliability) vs self-regulation (delivery speed, team autonomy) (C09).
- SLO target set from current performance (speed of adoption) vs from user need (avoids locking in heroics) (C06).
- Chaos experiments in production (confidence, realism) vs only in pre-production (blast radius, reversibility) (C28b).
- Declare an incident early and cheaply (speed, shared load) vs reserve it for severe events (cognitive load, process cost) (C30).
- Alert on imminent causes (early warning) vs symptoms only (low noise) (C12).

Candidate central decisions (every team must make first, others depend on them)
- D1: What are the critical user journeys and their SLIs, and who owns the SLO numbers (C02, C03, C05).
- D2: Is there an error budget policy and what does exhaustion trigger (C08, C09). Delivery area (release freezes) depends on it.
- D3: What counts as a page vs a ticket vs a log line, and what is the on-call and severity model (C11, C13, C29, C31).
- D4: Telemetry standard and storage model: OpenTelemetry or not, pillars vs events, sampling and retention budget (C21, C23, C27).
- D5: What triggers a postmortem and who tracks action items to closure (C32, C33).

Not covered: cost and FinOps of telemetry beyond sampling; security monitoring and SIEM (NIST 800-61 body not read); capacity planning and performance testing; feature flags and progressive rollout mechanics (boundary: DELIVER); synthetic monitoring tooling comparison; incident tooling products; the "new view" of human error (Etsy source unreadable); AIOps and anomaly detection; privacy and data-retention law for telemetry.

## L3 full

### Source register

| id | tier | title | author / body | URL read | authoritative on |
|---|---|---|---|---|---|
| OPERATE-S01 | T1 | Observability primer | OpenTelemetry | https://opentelemetry.io/docs/concepts/observability-primer/ | definitions of observability, telemetry, SLI, SLO, trace, span, log |
| OPERATE-S02 | T1 | Signals | OpenTelemetry | https://opentelemetry.io/docs/concepts/signals/ | signal set and stability (traces, metrics, logs, baggage, profiles) |
| OPERATE-S03 | T1 | Sampling | OpenTelemetry | https://opentelemetry.io/docs/concepts/sampling/ | head vs tail sampling, when to sample |
| OPERATE-S04 | T1 | Semantic conventions | OpenTelemetry | https://opentelemetry.io/docs/concepts/semantic-conventions/ | common naming across signals |
| OPERATE-S05 | T1 | Instrumentation | OpenTelemetry | https://opentelemetry.io/docs/concepts/instrumentation/ | zero-code vs code-based, library instrumentation |
| OPERATE-S06 | T1 | Trace Context | W3C (Recommendation, 2021) | https://www.w3.org/TR/trace-context/ | cross-vendor trace propagation headers |
| OPERATE-S07 | T1 | SP 800-61 Rev. 3, Incident Response Recommendations (landing page only) | NIST | https://csrc.nist.gov/pubs/sp/800/61/r3/final | incident response as part of risk management (CSF 2.0) |
| OPERATE-S08 | T2 | Monitoring Distributed Systems | Google SRE book | https://sre.google/sre-book/monitoring-distributed-systems/ | symptoms vs causes, golden signals, paging rules |
| OPERATE-S09 | T2 | Service Level Objectives | Google SRE book | https://sre.google/sre-book/service-level-objectives/ | SLI/SLO/SLA, target-setting |
| OPERATE-S10 | T2 | Postmortem Culture: Learning from Failure | Google SRE book | https://sre.google/sre-book/postmortem-culture/ | blameless postmortems, triggers |
| OPERATE-S11 | T2 | Managing Incidents | Google SRE book | https://sre.google/sre-book/managing-incidents/ | incident command roles, declaration, handoff |
| OPERATE-S12 | T2 | Embracing Risk | Google SRE book | https://sre.google/sre-book/embracing-risk/ | cost of reliability, error budgets |
| OPERATE-S13 | T2 | Eliminating Toil | Google SRE book | https://sre.google/sre-book/eliminating-toil/ | toil definition and 50% cap |
| OPERATE-S14 | T2 | Being On-Call | Google SRE book | https://sre.google/sre-book/being-on-call/ | on-call load, team size, alert/incident ratio |
| OPERATE-S15 | T2 | Practical Alerting from Time-Series Data | Google SRE book | https://sre.google/sre-book/practical-alerting/ | rule maintainability, black-box vs white-box |
| OPERATE-S16 | T2 | Introduction | Google SRE book | https://sre.google/sre-book/introduction/ | SRE tenets, monitoring outputs, playbooks, change as outage source |
| OPERATE-S17 | T2 | Alerting on SLOs | Google SRE workbook | https://sre.google/workbook/alerting-on-slos/ | burn-rate alerting strategies and thresholds |
| OPERATE-S18 | T2 | Example Error Budget Policy | Google SRE workbook | https://sre.google/workbook/error-budget-policy/ | budget exhaustion consequences |
| OPERATE-S19 | T2 | Implementing SLOs | Google SRE workbook | https://sre.google/workbook/implementing-slos/ | SLI specification vs implementation, journeys, windows |
| OPERATE-S20 | T2 | Postmortem Culture: Learning from Failure (workbook) | Google SRE workbook | https://sre.google/workbook/postmortem-culture/ | postmortem best practices and anti-patterns |
| OPERATE-S21 | T2 | DORA's software delivery metrics | DORA (Google Cloud) | https://dora.dev/guides/dora-metrics/ | five delivery metrics incl. failed deployment recovery time |
| OPERATE-S22 | T2 | Monitoring and observability capability | DORA | https://dora.dev/capabilities/monitoring-and-observability/ | monitoring vs observability, link to delivery performance |
| OPERATE-S23 | T2 | The Twelve-Factor App, XI. Logs | Heroku / Adam Wiggins | https://12factor.net/logs | logs as event streams |
| OPERATE-S24 | T3 | Principles of Chaos Engineering | Netflix et al. | https://principlesofchaos.org/ | chaos engineering definition and principles |
| OPERATE-S25 | T3 | The USE Method | Brendan Gregg | https://www.brendangregg.com/usemethod.html | resource-level checks |
| OPERATE-S26 | T3 | The RED Method | Grafana Labs (Tom Wilkie) | https://grafana.com/blog/the-red-method-how-to-instrument-your-services/ | service-level standard metrics, on-call for code you did not write |
| OPERATE-S27 | T3 | Time to version observability (observability 2.0) | Honeycomb (Charity Majors) | https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes | wide-events position; a vendor-interested source |
| OPERATE-S28 | T3 | Rethinking observability (news report of Sigelman, Sridharan, Majors debate) | InfoQ | https://www.infoq.com/news/2019/02/rethinking-observability | the three-pillars critique and cost trade-off |
| OPERATE-S29 | T3 | Incident response documentation (landing page) | PagerDuty | https://response.pagerduty.com/ | role names and structure of a practiced process |

Fetch notes: Google SRE Workbook and book chapters were read through the fetch tool's page summarizer, not as raw text; quotes in claims are those the summarizer returned and should be checked verbatim by the judge if used in the final text. Unread, so not cited as ground: Ewaschuk alerting philosophy, Etsy debriefing guide, Atlassian incident handbook (only a search-result snippet on SEV1-SEV3 and "blameless postmortems for severity 2 or higher" was seen).

### Claims

**OPERATE-C01**
- claim: Treat 100% reliability as the wrong target; choose a target below it from user need and weigh its cost.
- level: principle | stack: neutral | sources: S12 (Reliability vs cost; "cost does not increase linearly"), S19 ("100% reliability is the wrong target") | agreement: consensus | certainty: grounded.

**OPERATE-C02**
- claim: Define reliability through SLIs measured from the user's point of view, not through infrastructure metrics.
- level: principle | stack: neutral | sources: S09 (Choosing indicators), S01 (SLI), S19 (User journeys) | agreement: consensus | certainty: grounded.

**OPERATE-C03**
- claim: Anchor SLOs on critical user journeys (sequences of tasks essential to the user).
- level: practice | stack: neutral | sources: S19 | agreement: consensus | certainty: grounded (single source; same direction as S09).

**OPERATE-C04**
- claim: Measure latency with percentiles or histograms, never averages alone, because the tail dominates user experience and compounds across dependencies.
- level: principle | stack: neutral | sources: S08 (Addressing the long tail), S09 (Aggregation and percentiles) | agreement: consensus | certainty: grounded.

**OPERATE-C05**
- claim: Keep few SLOs, with simple SLIs; add more only for coverage gaps.
- level: practice | stack: neutral | sources: S09 (Setting targets) | agreement: consensus | certainty: grounded.

**OPERATE-C06**
- claim: Do not copy current performance as the SLO without a way to iterate; refine targets as you learn.
- level: decision | stack: neutral | sources: S09 ("Don't anchor to current performance"), S19 ("first attempt ... doesn't have to be correct"; starting from current performance acceptable with iteration) | agreement: contested | certainty: grounded.
- positions: (a) set from user need, not history; held by S09; serves reliability-fit and avoids heroics; wins when users or contracts have known needs. (b) start with what is measurable and cheap (existing logs), iterate; held by S19; serves delivery speed and feedback loop; wins when no SLOs exist yet. Both sources are Google; they are reconciled by "start, then review", so the disagreement is on starting point.

**OPERATE-C07**
- claim: Use an error budget (the gap between 100% and the SLO) as the shared, objective mechanism that trades release velocity against reliability.
- level: decision | stack: neutral | sources: S12 (Error budgets), S16 (Error budget framework) | agreement: majority | certainty: grounded.
- positions: held by Google SRE; serves velocity and reliability jointly; wins when product and operations are separate parties and need a depoliticized rule. Minority view (no error budget, reliability by judgment): not found in a read source; open.

**OPERATE-C08**
- claim: Write the error budget policy down and have product and operations agree to it; without it the SLO is only a report.
- level: practice | stack: neutral | sources: S19 (Error budget policy must be documented), S18 | agreement: consensus | certainty: grounded.

**OPERATE-C09**
- claim: Decide in advance what budget exhaustion does to releases.
- level: decision | stack: neutral | sources: S18 ("halt all changes and releases other than P0 issues or security fixes"), S12 (teams "self-regulate" when budget is depleted) | agreement: contested | certainty: grounded.
- positions: (a) hard freeze of changes except P0 and security fixes, disputes escalated to a named executive; serves control and reliability; wins with many consumers, strict SLAs, or a weak safety culture. (b) self-regulation: team slows and adds testing voluntarily; serves delivery speed and autonomy; wins in small, high-trust teams.

**OPERATE-C10**
- claim: Set postmortem triggers from budget consumption (for example one incident consuming over 20% of the budget over four weeks requires a postmortem with a top-priority action item).
- level: practice | stack: neutral | sources: S18 | agreement: majority | certainty: grounded (one example policy; numbers illustrative).

**OPERATE-C11**
- claim: Page a human only for a condition that is urgent, actionable, and actively or imminently user-visible; everything else goes to a ticket or a log.
- level: principle | stack: neutral | sources: S08 (Alerting principles), S16 (Monitoring output categories: alerts, tickets, logging) | agreement: consensus | certainty: grounded.

**OPERATE-C12**
- claim: Alert on user-visible symptoms; keep cause-level signals for diagnosis, and use white-box signals to catch imminent or retry-masked failures.
- level: principle | stack: neutral | sources: S08 (Symptoms vs causes; White-box vs black-box), S15 (Alert on symptoms) | agreement: majority | certainty: grounded (Ewaschuk's formulation not read).
- positions: symptom-only paging (low noise, cognitive load; wins with limited on-call capacity); plus white-box cause alerts for imminent failures (early warning; S08 says combine "heavy white-box with modest but critical black-box"). The tension is early warning vs noise.

**OPERATE-C13**
- claim: Every page must require human judgment; a page answerable by a robotic response should be automated or removed.
- level: principle | stack: neutral | sources: S08 | agreement: consensus | certainty: grounded.

**OPERATE-C14**
- claim: Alert on the rate at which the error budget is being consumed (burn rate), using multiple long and short windows, with severity tiers: page for fast burn, ticket for slow burn.
- level: practice | stack: neutral | sources: S17 (Multiwindow, multi-burn-rate; thresholds 14.4x/1h, 6x/6h to page, 1x/3d to ticket for 99.9%) | agreement: majority | certainty: grounded (one authority; simpler strategies documented as inferior on precision, recall, reset time).
- positions: simple threshold alerts (fewest parameters, easiest to maintain; wins for small services) vs multiwindow multi-burn-rate (best precision/recall/reset time; wins when an SLO exists and false pages cost a lot).

**OPERATE-C15**
- claim: Remove alerting rules and collected signals that are rarely exercised or never exposed; keep rules that catch real incidents simple and predictable.
- level: practice | stack: neutral | sources: S08 (Simplicity) | agreement: consensus | certainty: grounded.

**OPERATE-C16**
- claim: Combine black-box probing with white-box monitoring, because internal views cannot see what never reached the service (for example DNS failures).
- level: practice | stack: neutral | sources: S15, S08 | agreement: consensus | certainty: grounded.

**OPERATE-C17**
- claim: For user-facing services measure latency, traffic, errors and saturation.
- level: principle | stack: neutral | sources: S08 (Four golden signals) | agreement: consensus | certainty: grounded.

**OPERATE-C18**
- claim: Standardize a minimal metric set per service (rate, errors, duration) so that anyone can be on call for code they did not write; use utilization, saturation, errors per resource for infrastructure.
- level: practice | stack: neutral | sources: S26 (RED), S25 (USE) | agreement: majority | certainty: grounded (T3 sources; golden signals in S08 are the T2 counterpart).

**OPERATE-C19**
- claim: Treat USE as a quick first check for bottlenecks and errors, one tool among others, not a full diagnostic method.
- level: practice | stack: neutral | sources: S25 | agreement: consensus | certainty: grounded.

**OPERATE-C20**
- claim: Distinguish monitoring (watching predefined metrics) from observability (exploring properties not defined in advance to debug unknown unknowns) and provide both.
- level: principle | stack: neutral | sources: S22, S01 | agreement: majority | certainty: grounded.
- positions: S22 and S01 treat them as complementary; S27 argues the old pillars model should be replaced (see C21).

**OPERATE-C21**
- claim: Choose the telemetry storage model deliberately: separate metrics, logs and traces ("three pillars") or arbitrarily wide structured events aggregated at read time.
- level: decision | stack: neutral | sources: S27 (Observability 2.0), S28 (Rethinking observability), S02 (signals as separate types) | agreement: contested | certainty: grounded.
- positions: (a) pillars, with OpenTelemetry signals: T1 standard, mature tooling, cheap aggregated metrics for alerting; serves cost of ownership and ecosystem fit; wins where metric alerting dominates and cardinality is low. (b) wide events as single source of truth: exploratory power, high-cardinality questions, one store; held by Honeycomb (a vendor with an interest, T3); serves speed of diagnosis; wins in complex distributed systems with frequent novel failures. (c) Sigelman: the issue is trade-offs among throughput, cardinality, retention and unsampled data; "positive-ROI" systems; Majors disputes the cost premise. Evidence is argued, not measured.

**OPERATE-C22**
- claim: Make all developers proficient with monitoring; observability is a shared responsibility, not an operations-only task.
- level: principle | stack: neutral | sources: S22 | agreement: consensus | certainty: grounded.

**OPERATE-C23**
- claim: Adopt a vendor-neutral instrumentation API and standard semantic conventions so naming is consistent across code, libraries and platforms.
- level: decision | stack: neutral (OpenTelemetry is the reference realization) | sources: S04, S05 | agreement: majority | certainty: grounded.
- positions: vendor-neutral standard (exit risk, interoperability) vs vendor SDK or agent (less setup, deeper vendor features). Alternatives not argued in a read source; inferred.

**OPERATE-C24**
- claim: Combine zero-code instrumentation (fast start, library and edge telemetry) with code-based instrumentation (application-specific detail).
- level: practice | stack: OpenTelemetry | sources: S05 | agreement: consensus | certainty: grounded.

**OPERATE-C25**
- claim: Libraries should depend only on the instrumentation API, not the SDK, so they add no cost to applications that do not collect telemetry.
- level: practice | stack: OpenTelemetry | sources: S05 (Native library instrumentation) | agreement: consensus | certainty: grounded. boundary: ADOPT (library wrapping and dependencies).

**OPERATE-C26**
- claim: Propagate trace context between services with the standard W3C traceparent/tracestate headers so traces from different vendors correlate.
- level: practice | stack: HTTP | sources: S06 | agreement: consensus | certainty: grounded.

**OPERATE-C27**
- claim: Decide explicitly whether to sample traces and where: head sampling (simple, cheap, cannot guarantee error traces) vs tail sampling (criteria-based, stateful and operationally heavy); do not sample at low volume, with aggregate-only metrics, or under retention obligations.
- level: decision | stack: neutral | sources: S03, S28 | agreement: contested | certainty: grounded.
- positions: head (cost, simplicity; wins above about 1,000 traces/s with healthy predictable traffic); tail (completeness of rare-error traces; wins when errors are rare and must all be kept, and the team can run the infrastructure); none (control, no missed signal; wins at low volume or under regulation).

**OPERATE-C28**
- claim: Applications write logs as an unbuffered event stream to standard output and do not manage routing or storage; the environment collects and routes it.
- level: practice | stack: neutral (process-based apps) | sources: S23 | agreement: majority | certainty: grounded.
- positions: S23 (platform routes) vs structured logging libraries writing direct to files or collectors in non-container contexts; the latter not argued in a read source; inferred.

**OPERATE-C28b**
- claim: Verify resilience with experiments built on a steady-state hypothesis over measurable outputs, with minimized blast radius, ideally automated and continuous.
- level: decision | stack: neutral | sources: S24 | agreement: contested | certainty: grounded (single T3 source; no counter-source read).
- positions: run in production on real traffic (confidence; S24 says sampling real traffic is the only reliable way) vs pre-production only (reversibility, blast radius; wins with low maturity, safety-critical or regulated systems). Counter-position inferred, not sourced.

**OPERATE-C29**
- claim: Run major incidents with named roles (commander, operations, communications, planning/scribe), the commander keeping a live incident document; only the operations lead changes the system.
- level: practice | stack: neutral | sources: S11, S29 (role names: IC, scribe, deputy, liaisons) | agreement: consensus | certainty: grounded.

**OPERATE-C30**
- claim: Declare an incident on clear, written conditions (second team needed, customer-visible, unresolved after an hour of focused analysis) and make declaring cheap.
- level: decision | stack: neutral | sources: S11 (When to declare) | agreement: contested | certainty: grounded (one source for the criteria; "make declaring cheap" is inferred).
- positions: early, low-threshold declaration (shared load, faster response; S11); high bar reserved for severe events (lower process cost and fatigue wins in tiny teams). Second position not found in a read source; open.

**OPERATE-C31**
- claim: Define severity levels and the response each gets before an incident, and rehearse the process until routine; hand over command explicitly.
- level: practice | stack: neutral | sources: S11 (Handoff, Practice), S29 (Before an incident, severity) | agreement: consensus | certainty: grounded.

**OPERATE-C32**
- claim: Write blameless postmortems for significant incidents, whether or not they paged, with written triggers (user-visible downtime, data loss, manual intervention, slow resolution, monitoring failure).
- level: principle | stack: neutral | sources: S10, S16, S20 | agreement: consensus | certainty: grounded.

**OPERATE-C33**
- claim: Give every postmortem action item an owner, priority and tracker entry, make items measurable and preventative, publish within days, and reward closeout, not only writing.
- level: practice | stack: neutral | sources: S20 | agreement: consensus | certainty: grounded.

**OPERATE-C34**
- claim: Bound the human cost of operation: cap operational work (toil) at 50% of an engineer's time, limit on-call to about 25% and about two incidents per 12-hour shift, aim for a near 1:1 alert-to-incident ratio, and keep engineers on call occasionally to keep familiarity.
- level: practice | stack: neutral | sources: S13, S14, S16 | agreement: majority | certainty: grounded (numbers come from Google-scale SRE teams; for small teams inferred to need scaling or a different structure).
- positions: Google numbers assume dedicated SRE teams of 6 to 8 or more per site; the force served is team cognitive load and retention; small teams where developers own operations must decide their own limit.

**OPERATE-C35**
- claim: Treat changes as the main source of outages and automate progressive rollout, fast problem detection and safe rollback; use playbooks, which Google reports improve time to repair about threefold over ad-hoc response.
- level: principle | stack: neutral | sources: S16 (Emergency response; Change management, "about 70% of outages stem from changes") | agreement: consensus | certainty: grounded. boundary: DELIVER.

**OPERATE-C36**
- claim: Track failed deployment recovery time and change fail rate as production feedback on delivery, at the level of one service, shared across development and operations, and never as targets.
- level: practice | stack: neutral | sources: S21 | agreement: majority | certainty: grounded. boundary: DELIVER.
- positions: DORA warns that metric targets invite gaming; contrary view (set targets to drive improvement) is not argued in a read source.

**OPERATE-C37**
- claim: Incident response should be integrated with the organization's risk management and aim to reduce both the number and the impact of incidents and improve detection, response and recovery.
- level: principle | stack: neutral | sources: S07 (landing page only) | agreement: consensus | certainty: grounded at abstract level; body unread.

### Gaps (open)

- No minority school argued against error budgets or SLOs found in a read source (for example teams that reject quantitative SLOs).
- No read source argues the case for pre-production-only chaos testing, or for a high incident-declaration threshold.
- "Root cause" vs "contributing factors" (Etsy, New View on human error) not read; the postmortem claims rest on Google only.
- NIST SP 800-61r3 body, security incident detection, and SIEM not read.
- Rob Ewaschuk's alerting philosophy not read; symptom-based paging rests on Google SRE.
- Costs of telemetry are argued, not measured, in the sources read; no peer-reviewed empirical study on alert fatigue, SLO adoption or postmortem effectiveness was read (T3 empirical evidence missing).
- Feature-flag and dark-launch feedback from production, synthetic monitoring, and capacity planning not covered.

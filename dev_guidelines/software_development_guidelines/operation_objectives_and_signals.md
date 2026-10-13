# Operation: Objectives and Signals

## Table of Contents

1. [Reliability Targets](#reliability-targets) _(Lines 30-36)_
   1. [Indicators](#indicators) _(Lines 39-49)_
   1. [Objective Level and Starting Point](#objective-level-and-starting-point) _(Lines 52-64)_
   1. [Error Budget as Trade Mechanism](#error-budget-as-trade-mechanism) _(Lines 67-83)_
   1. [Budget Exhaustion Consequence](#budget-exhaustion-consequence) _(Lines 86-98)_
1. [Alerting](#alerting) _(Lines 101-104)_
   1. [Paging Criterion and Rule Hygiene](#paging-criterion-and-rule-hygiene) _(Lines 107-120)_
   1. [Alert Basis](#alert-basis) _(Lines 123-140)_
1. [Telemetry](#telemetry) _(Lines 143-149)_
   1. [What Is Measured - Service and Resource Signals](#what-is-measured---service-and-resource-signals) _(Lines 152-163)_
   1. [Observability Model and Pipeline Health](#observability-model-and-pipeline-health) _(Lines 166-179)_
   1. [Instrumentation and Log Emission](#instrumentation-and-log-emission) _(Lines 182-199)_
   1. [Correlation and Context Propagation](#correlation-and-context-propagation) _(Lines 202-217)_
   1. [Trace Sampling](#trace-sampling) _(Lines 220-237)_
   1. [Telemetry Cost](#telemetry-cost) _(Lines 240-253)_
   1. [Vantage Points](#vantage-points) _(Lines 256-268)_
   1. [Scheduled Work Signals](#scheduled-work-signals) _(Lines 271-280)_


---

Part of [Operation](operation.md). Reliability objective and error budget, paging, and the telemetry that shows user harm and resource strain.

## Reliability Targets
<!-- Lines 30-36 -->

Reliability is an objective below 100 percent on a few indicators measured as users experience
them. The gap to the objective is a written, agreed rule that trades release speed against
reliability, with its consequence decided beforehand. Speed and reliability are traded by rule,
not by argument. The objectives and budget are what the availability proof is read against
([Availability and Recovery](assurance_performance_availability.md#availability-and-recovery)). `OPERATION.RELIABILITY`

### Indicators
<!-- Lines 39-49 -->

Define reliability through a handful of simple indicators measured from the user's side and
anchored on critical user journeys; add one only for a coverage gap. State latency as a percentile
or distribution, never as an average alone.

- MUST measure from the user's side, keep the set small, and state latency as a percentile or distribution.

Best instead when: infrastructure metrics are not the definition of reliability, but are the right
diagnostic signals (see [What Is Measured](#what-is-measured---service-and-resource-signals)).
An average alone is best never. `OPERATION.RELIABILITY.1`

### Objective Level and Starting Point
<!-- Lines 52-64 -->

Set the objective below 100 percent from user need and the cost of each extra step, never copied
from current performance as a final value. Where user need is not yet known, a provisional
objective from what is cheaply measurable (existing logs) is allowed, marked provisional and
reviewed on a fixed cadence until one derived from user need replaces it. Requires an indicator
from [Indicators](#indicators).

- MUST NOT set the objective at 100 percent.
- MUST derive it from user need, or mark it provisional with a review date.

Best never: 100 percent, an objective fixed from history with no review, or waiting for a perfect
user-need study before setting any objective. `OPERATION.RELIABILITY.2`

### Error Budget as Trade Mechanism
<!-- Lines 67-83 -->

The gap between 100 percent and the objective is an error budget. A written policy, agreed by
those who decide release speed and those who answer for reliability, states how the remaining
budget governs release decisions; without that agreement the objective is only a report. Budget
consumption is one of the written postmortem triggers
([Learning From Incidents](operation_response_and_readiness.md#learning-from-incidents)). Requires [Objective Level and Starting Point](#objective-level-and-starting-point).

- MUST write the budget policy and have it agreed.
- MUST name the consumption levels that trigger a postmortem.

Illustration only, not a threshold: one published policy triggers a postmortem when a single
incident consumes more than 20 percent of the budget within four weeks.

Best instead when: judgment without a budget fits when one party owns both speed and reliability
and the choice is its own (inferred; no source records it). An unwritten or unagreed budget is
best never. `OPERATION.RELIABILITY.3`

### Budget Exhaustion Consequence
<!-- Lines 86-98 -->

Decide the consequence of exhausting the budget in advance, write it in the budget policy and make
it binding, so the response is automatic and not a negotiation. Requires [Error Budget as Trade Mechanism](#error-budget-as-trade-mechanism).

- With many consumers, strict commitments or a weak safety culture: freeze changes except
  top-priority and security fixes, with disputes escalated to a named person.
- In a small, high-trust team: self-regulation (the team slows and adds testing), still stated beforehand.
- MUST state the consequence before exhaustion; MUST name the escalation owner where a freeze applies.

Best instead when: a freeze in a small high-trust team costs speed it does not need; self-regulation
with many consumers or strict commitments gives no assurance. Open: the culture condition is
inferred from a thin base and neither form was measured. `OPERATION.RELIABILITY.4`

## Alerting
<!-- Lines 101-104 -->

A human is paged only for what needs a human now, on the symptom users feel. The rule set is
pruned to that, so every page is worth waking someone for. `OPERATION.ALERTING`

### Paging Criterion and Rule Hygiene
<!-- Lines 107-120 -->

Page only for a condition that is urgent, actionable and actively or imminently user-visible;
everything else is a ticket or a log. Every page needs human judgment: a page answerable by a
mechanical response is automated or removed. Remove rules and signals never exercised; keep rules
that catch real incidents simple and predictable. A page links its playbook
([Form, Ownership and Validation](operation_response_and_readiness.md#form-ownership-and-validation)).

- MUST classify every alert as page, ticket or log.
- MUST automate or remove a page answerable by script.
- MUST review rules for never-exercised ones.

Best never: paging on any threshold breach or on every cause signal (keep them as tickets or for
diagnosis), or retaining rarely exercised rules for completeness. `OPERATION.ALERTING.1`

### Alert Basis
<!-- Lines 123-140 -->

Page on user-visible symptoms; keep cause signals for diagnosis. A cause signal pages only when it
predicts imminent user-visible failure the symptom cannot yet show (a failure masked by retries,
a resource about to run out). Requires [Objective Level and Starting Point](#objective-level-and-starting-point)
and [Error Budget as Trade Mechanism](#error-budget-as-trade-mechanism) for burn-rate alerts.

| Condition | Alert form |
|---|---|
| Objective exists and false pages are costly | Budget burn rate over several windows: page for fast burn, ticket for slow burn |
| No objective exists | Simple threshold alerts on the symptom |
| Traffic too low for a burn rate to mean anything | Synthetic traffic, or combine services under one objective; not simple thresholds |

- MUST page on a symptom, or on a cause with a stated imminent user-visible consequence.
- MUST NOT use burn-rate alerts without an objective.

Open: burn-rate alerting rests on a single authority with no independent measurement; the
reconciliation of symptom and cause alerts is inferred. `OPERATION.ALERTING.2`

## Telemetry
<!-- Lines 143-149 -->

Every service exposes the signals that show user harm and resource strain, observed from inside,
from outside and from real users. They are emitted through a vendor-neutral path, joined by one
correlation context, sampled by an explicit rule and bounded as a cost; scheduled work is watched
on its own signals. Any incident can then be reconstructed and any slow query or silent failure
found, at a volume the team can afford. `OPERATION.TELEMETRY`

### What Is Measured - Service and Resource Signals
<!-- Lines 152-163 -->

The standard set is latency, traffic, errors and saturation. The first three are the request
signals every service exposes alike, so anyone can be on call for code they did not write;
saturation is read per resource (utilisation, saturation, errors). Read resources this way as a
quick first check; for a bottleneck, enumerate resources first and check each. Enable
per-statement database statistics so slow queries are found by measurement.

- MUST expose latency, traffic, errors and saturation per user-facing service.

Best instead when: the per-resource method is not a complete diagnostic method on its own. Open:
the minimal per-service set rests on lower-tier sources. `OPERATION.TELEMETRY.1`

### Observability Model and Pipeline Health
<!-- Lines 166-179 -->

Provide both monitoring (predefined questions, for alerting) and observability (questions nobody
defined, for unknown failures), designed in across every tier as correlated signals of one system;
every developer is proficient with them. Choose the storage model by condition, and check the
pipeline itself so its silence is detected. Relies on [Correlation and Context Propagation](#correlation-and-context-propagation).

- Separate metrics, logs and traces: where metric alerting dominates and cardinality is low.
- Wide structured events as a single store: where failures are novel and distributed and high-cardinality questions are routine.
- MUST design correlation in; MUST detect a silent failure of the telemetry pipeline.

Best never: observability as an operations-only task (code authors hold the context). Open: the
pipeline check (a heartbeat or known test event that must arrive) and the storage condition split
are argued, not measured. `OPERATION.TELEMETRY.2`

### Instrumentation and Log Emission
<!-- Lines 182-199 -->

Instrument code against a vendor-neutral API with standard semantic conventions: automatic
instrumentation for framework, HTTP and database-client coverage, code-based only for business
logic. Libraries depend on the instrumentation API only, never on an implementation (this
specialises [Containment and Exit](ownership_lifecycle_containment.md#containment-and-exit)). The application writes
logs as an unbuffered, structured event stream to the channel its environment provides and does
not own routing or storage; the environment collects and routes them. Example: a process writes
its event stream to standard output and the platform's collector routes and stores it.

- MUST use a vendor-neutral instrumentation API.
- MUST NOT make a library depend on an instrumentation implementation.
- MUST NOT route or store logs in application code where the environment does.

Best instead when: a vendor SDK fits when one backend is fixed and a vendor feature outweighs
exit cost (then behind the neutral API where possible). Application-managed log files fit only
where no execution environment collects output, with routing configured outside the code. Both
conditions are inferred. `OPERATION.TELEMETRY.3`

### Correlation and Context Propagation
<!-- Lines 202-217 -->

Propagate one trace context, carrying no personal data
([Minimisation, Classification and Design-In](transverse_privacy.md#minimisation-classification-and-design-in)),
across every tier and process boundary in the standard format of the transport. Put trace and span
ids in every log record; every event of one user interaction carries a shared correlation id (the
trace id serves); client error and real-user events are stamped with the release version and the
trace or request id. One request can then be reconstructed from browser to database. Example: for
HTTP the standard format is the W3C `traceparent` header, with `tracestate` for vendor data.

- MUST propagate trace context at every boundary.
- MUST put trace and span ids in every log record.
- MUST NOT put personal data in trace context.

Best instead when: proprietary per-vendor headers fit only inside a closed single-vendor system
(inferred). Correlation by timestamp matching is best never as primary. `OPERATION.TELEMETRY.4`

### Trace Sampling
<!-- Lines 220-237 -->

Decide sampling explicitly. Keep every trace while volume is low, metrics are aggregate-only or
retention obligations apply. When volume forces sampling, use head sampling for healthy,
predictable traffic; use tail sampling (or a hybrid) where rare error and slow traces must all be
kept, accepting a heavier, stateful pipeline. The decision travels with the propagated context
([Correlation and Context Propagation](#correlation-and-context-propagation)) and carries out the
volume control of [Telemetry Cost](#telemetry-cost).

- MUST state the sampling rule.
- MUST NOT honour an untrusted caller's sampling flag at a public boundary unexamined.

Illustration only, not a threshold: one documentation shows head sampling above about 1,000 traces
per second.

Best instead when: head sampling cannot guarantee that every error trace is kept; tail sampling
is best when the team can run its infrastructure; no sampling is best at low volume or under
retention obligation. The order of the ladder is inferred. `OPERATION.TELEMETRY.5`

### Telemetry Cost
<!-- Lines 240-253 -->

Treat telemetry volume and cardinality as a designed cost. Bound metric label cardinality (no
unbounded values such as user ids; per-entity detail goes to logs or traces). Filter low-value
telemetry and coarsen detail with a stated loss of granularity. Keep instrumentation broad: the
bound is on labels, not on metrics. Each service should have a stated, reviewed bound on volume,
series count and retention.

- MUST bound label cardinality.
- SHOULD state a volume or series bound per service.

Best instead when: dropping instrumentation instead of bounding labels fits only on the hottest
code paths. Open: no source treats telemetry cost as a governed budget; the per-service bound is a
recommendation without a normative source. `OPERATION.TELEMETRY.6`

### Vantage Points
<!-- Lines 256-268 -->

Combine internal measurement with external probing of real customer routes on a schedule from
several vantage points (payload validated, latency kept as a time series, credentials secured),
plus real-user measurement for experienced performance. A failure is then seen from where it
hurts, including failures that never reached the service. Specialises
[What Is Measured](#what-is-measured---service-and-resource-signals).

- MUST have a probe from outside for each critical user route.
- MUST secure probe credentials.

Best instead when: synthetic-only fits where real-user data cannot be collected. White-box only is
best never alone. Open: real-user measurement rests on a lower-tier source. `OPERATION.TELEMETRY.7`

### Scheduled Work Signals
<!-- Lines 271-280 -->

Monitor scheduled and derived-data work on four signals: duration against a documented
expectation, any failure, backlog (queue size and age of the oldest entry), and missed runs (not
run within twice the interval). A job reports its failure to the scheduler instead of swallowing
it. A job that did not run, ran too long or failed is then noticed. Specialises
[What Is Measured](#what-is-measured---service-and-resource-signals) for work that is not request-driven.

- MUST monitor scheduled work on duration, failure, backlog and missed runs.

Treating a completed job as success is best never. `OPERATION.TELEMETRY.8`

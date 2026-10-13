# Transverse: Security

The security programme, and the logging, detection and audit trail that carry it out. Part of [Transverse](transverse.md).

## Table of Contents

1. [Security Practice](#security-practice) _(Lines 22-28)_
   1. [Anchor Framework](#anchor-framework) _(Lines 31-50)_
   1. [Maturity Targets and Cycle](#maturity-targets-and-cycle) _(Lines 53-67)_
   1. [Design-Time Risk Modelling](#design-time-risk-modelling) _(Lines 70-86)_
   1. [Responsibility and Training](#responsibility-and-training) _(Lines 89-97)_
   1. [Vulnerability Response Loop](#vulnerability-response-loop) _(Lines 100-113)_
   1. [Disclosure Policy and Bounty](#disclosure-policy-and-bounty) _(Lines 116-131)_
1. [Security Monitoring and Audit Trail](#security-monitoring-and-audit-trail) _(Lines 134-141)_
   1. [Events Logged](#events-logged) _(Lines 144-159)_
   1. [Entry Content, Time and Format](#entry-content-time-and-format) _(Lines 162-175)_
   1. [Log Protection and Sanitising](#log-protection-and-sanitising) _(Lines 178-194)_
   1. [Detection and Escalation](#detection-and-escalation) _(Lines 197-213)_
   1. [Business Audit Trail](#business-audit-trail) _(Lines 216-232)_
## Security Practice
<!-- Lines 22-28 -->

The security programme is anchored in a published framework chosen by the question asked, risk is
modelled at design time at a depth set by risk, responsibility is explicit and owned from the top,
and every vulnerability follows one loop with a published intake. Realizes
[Security](assurance_docs_security.md#security), which holds verification depth, blocking, tests, scanning and
limits on automation. `TRANSVERSE.SECURITY`

### Anchor Framework
<!-- Lines 31-50 -->

The secure-development practice is anchored in a published framework used as a list of outcomes to
cover, not as a prescription of tools. The framework is chosen by the question the team needs
answered.

| Question | Anchor |
|---|---|
| Specify and verify the technical requirements of one application or a supplier | A requirements standard, level chosen from the application's risk |
| Assess and plan a programme across many teams | A prescriptive maturity model, with an outcome framework as the list of outcomes to cover |
| What do peers do | A descriptive benchmark: evidence only |

- MUST name the anchor framework and the question it answers.
- MUST NOT use a descriptive benchmark as the verdict on what to adopt; it is best only to justify
  investment to a sponsor.
- The depth chosen per application from risk selects the requirement level
  ([Verification Depth and Design Review](assurance_docs_security.md#verification-depth-and-design-review)).

Open: the mapping of framework to question is inferred; level definitions of the requirements
standard were not read. `TRANSVERSE.SECURITY.1`

### Maturity Targets and Cycle
<!-- Lines 53-67 -->

A maturity model is run as a cycle: assess, set a target per practice from context, build a
roadmap, take the prescriptive activities. A maturity score or requirement level measures activity
and coverage, not security outcomes.

- MUST set targets per practice; one uniform level everywhere is best never.
- MUST NOT present a score as an outcome measure; pair it with outcome measures (time to detect,
  see [Detection and Escalation](#detection-and-escalation); defects found per stage and closed
  findings, inferred).
- Runs the model anchored in [Anchor Framework](#anchor-framework); its effectiveness is tested by
  [Closing the Loop on Findings](assurance_docs_security.md#closing-the-loop-on-findings).

Open: no source shows that higher maturity scores or requirement levels reduce incidents.
`TRANSVERSE.SECURITY.2`

### Design-Time Risk Modelling
<!-- Lines 70-86 -->

Security risk is modelled during design and again whenever a design change touches data
sensitivity, authentication, access control, credentials or a trust boundary, at a depth set by
risk. Each model answers four questions (what are we working on, what can go wrong, what will we
do about it, did we do a good enough job); risks and mitigations are tracked in the team's
workflow.

- MUST track mitigations in the team's workflow.
- MUST remodel on a design change that touches a trust boundary.

Best instead: continuous lightweight modelling alone suits fast-changing products with moderate
risk; a deeper risk-triggered model alone suits criticality or regulation but goes stale on the
lower-risk changes between. The default combines them: lightweight per change, deeper for
high-risk areas. The model is what the design review reviews against
([Verification Depth and Design Review](assurance_docs_security.md#verification-depth-and-design-review)).
`TRANSVERSE.SECURITY.3`

### Responsibility and Training
<!-- Lines 89-97 -->

Security responsibility is explicit and owned from the top: roles are defined, training is
role-based, management commits and the producer owns the security outcomes its customers
experience.

- MUST name an owner per security outcome. Responsibility by goodwill is best never.

`TRANSVERSE.SECURITY.4`

### Vulnerability Response Loop
<!-- Lines 100-113 -->

A vulnerability, reported or found, in own or consumed code, follows one loop: confirm, assess,
prioritize by a stated rule, remediate within a stated time, then analyse root causes and fix the
process as well as the instance. Live incidents are handled in [Incidents](operation_response_and_readiness.md#incidents);
this loop covers the vulnerability.

- MUST state the prioritization rule and the remediation time.
- The process change and class-precluding approach are held in
  [Closing the Loop on Findings](assurance_docs_security.md#closing-the-loop-on-findings).
- Fed by [Disclosure Policy and Bounty](#disclosure-policy-and-bounty); a leaked secret is one case
  ([Response to a Leaked Secret](transverse_config_environments.md#response-to-a-leaked-secret)).

`TRANSVERSE.SECURITY.5`

### Disclosure Policy and Bounty
<!-- Lines 116-131 -->

Any system reachable by outsiders publishes a disclosure policy: a private reporting channel, a
stated acknowledgement time, a stated fix time for known medium-or-higher vulnerabilities, and the
contact in a standard place. A paid bounty is added only after weighing cost, competence and
maturity.

- MUST publish a private reporting channel.
- MUST state response and fix times only the team can meet.
- Reports received are the intake of the [Vulnerability Response Loop](#vulnerability-response-loop).

Best instead: a paid bounty suits mature triage and a wide attack surface; a periodic penetration
test alone suits a system that cannot be exposed to outside researchers.

Open: no source read compares bounty yield; the commercial case for a bounty is unsettled.
`TRANSVERSE.SECURITY.6`

## Security Monitoring and Audit Trail
<!-- Lines 134-141 -->

Security-relevant events are logged with enough content to reconstruct who did what, when and
where; logs are protected and free of what must not be in them; active attacks and the stopping of
logging are detected and escalated; and the business audit trail is a separate artifact. An attack
is then seen in time, can be reconstructed, and a change to data can be accounted for. Carries out
the verification target of [Security](assurance_docs_security.md#security) and relies on the pipeline that
[Telemetry](operation_objectives_and_signals.md#telemetry) shares. `TRANSVERSE.SECURITY_MONITORING`

### Events Logged
<!-- Lines 144-159 -->

Security-relevant events are logged: authentication, authorization, validation and session
failures, administrative actions, sensitive data access, higher-risk functionality, errors,
control failures and bypass attempts. Every action of an automated actor is logged in a trail a
person can review.

- MUST log authentication, authorization and validation failures.
- MUST log automation actions to a trail a person can review; this is how the limits in
  [Enforced Limits on Automation and Access](assurance_docs_security.md#enforced-limits-on-automation-and-access)
  are shown to hold.
- Logging does not depend on the verification level a standard asks for: verification level sets
  what is verified, not what is needed to detect and bound a breach.
- Data-change events are business audit, not security events ([Business Audit Trail](#business-audit-trail)).

`TRANSVERSE.SECURITY_MONITORING.1`

### Entry Content, Time and Format
<!-- Lines 162-175 -->

Every entry records who, what, when and where (timestamp, application and address, source address
and authenticated identity, event type, severity, affected object, result and reason), with one
event vocabulary and one format across systems, synchronized server clocks, an inventory of what
is logged at each layer, and only documented destinations.

- MUST use UTC-anchored ISO 8601 timestamps.
- MUST keep one event vocabulary; free-text entries are best never where monitoring keys on terms.
- Where clocks cannot be synchronized (remote clients), also record the server's receipt time
  (inferred).
- These entries are the data that answers a breach ([Privacy Risk, Impact Assessment and Breach](transverse_privacy.md#privacy-risk-impact-assessment-and-breach)).

`TRANSVERSE.SECURITY_MONITORING.2`

### Log Protection and Sanitising
<!-- Lines 178-194 -->

Logs are protected at rest and in transit against modification, injection and unauthorized access,
and shipped to a logically separate system where possible. Secrets, session identifiers and
unneeded personal data are never logged; client-supplied text is untrusted.

- MUST NOT log secrets or session identifiers (passwords, tokens, keys, connection strings,
  payment data; a hash of the identifier where tracking is needed).
- MUST sanitize client-supplied text before writing (line breaks, delimiters, output encoding).
- MUST keep the log writer unable to modify what it has written (an early copy beyond its reach).
- Log retention is bounded by [Retention Periods](transverse_privacy.md#retention-periods); pseudonymisation of
  investigation logs is held in [Minimisation, Classification and Design-In](transverse_privacy.md#minimisation-classification-and-design-in).

Best instead: without a central collector, logs apart from application data (a separate partition
or a write-only account) are the minimum, best on a small single-host system. Logs in the
application's own store under application permissions are best never as protection.
`TRANSVERSE.SECURITY_MONITORING.3`

### Detection and Escalation
<!-- Lines 197-213 -->

Logging without alerting and response is a failure: active attacks are detected and escalated in
near real time, and the stopping of logging is itself detected. Time to detect is a managed figure
with a target, measured on the team's own exercises and incidents, not taken from a quoted average.

- MUST detect when logging stops.
- MUST be able to show that a known probe raises an alert
  ([Closing the Loop on Findings](assurance_docs_security.md#closing-the-loop-on-findings)).
- Escalation relies on [Alerting](operation_objectives_and_signals.md#alerting); time to detect is the outcome measure
  of the [Maturity Targets and Cycle](#maturity-targets-and-cycle).
- Keep detection rules tool-neutral where the platform may change.

Best instead: tool-native rules suit a stable, deliberate platform dependency with a small rule
set (inferred). Logging with review after the fact only is best never.

Open: the often-quoted dwell-time figure is dated and not a current value. `TRANSVERSE.SECURITY_MONITORING.4`

### Business Audit Trail
<!-- Lines 216-232 -->

The security event log (what was attempted, for detection) and the business audit trail (what
changed, for accountability and queries) are two artifacts designed apart: they differ in storage,
integrity and retention. One log for both purposes is best never.

- MUST write the audit record in the transaction of the change, so both commit or roll back
  together (declared in the store: [Where Integrity Rules Live](assurance_interfaces_data.md#where-integrity-rules-live)).
- MUST give a high-value trail append-only integrity and tamper detection; entries carry the actual
  date and the record date.
- The reason a trail is kept bounds when [Erasure and Deletion Mechanism](transverse_privacy.md#erasure-and-deletion-mechanism)
  may delete it.

Best instead: an audit log is the default; temporal properties or objects are best when history is
queried tightly and integrated with current data.

Open: the split into two artifacts is stated by no source (inferred). `TRANSVERSE.SECURITY_MONITORING.5`


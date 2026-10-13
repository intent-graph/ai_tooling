# Result: unit J7_operation

## L1 headline

All 39 nodes of OPERATION are judged: no decision is undecided, no settled decision is contested, and 11 flags go to the Opus pass. Marks: grounded for the core of most L3 decisions, inferred for the roll-ups and the parts flagged below, open where a source is missing (budget, hardening against speed, headroom figure).

Pinned:
- Nodes judged: 39 (OPERATION; RELIABILITY .1-.4; ALERTING .1-.2; TELEMETRY .1-.6; INCIDENTS .1-.3; CAPACITY .1-.3; READINESS .1-.3; RUNBOOKS .1-.2; RECOVERY .1-.6; FEEDBACK), 109 rows.
- Decisions marked undecided: none.
- Flags raised: 11 (F1 PERFORMANCE.1 wording against L179, F2 TELEMETRY.1 split and job-design placement, F3 TELEMETRY.2 storage model evidence, F4 TELEMETRY.6 budget unsourced, F5 RECOVERY.5 hardening against speed, F6 INCIDENTS.3 small teams, F7 READINESS.2 no effectiveness evidence, F8 RECOVERY.3 extension and dual authorisation boundary, F9 inferred reconciliation in RECOVERY.4 and CAPACITY.3 caveats, F10 L1 record overlap with wave 3, F11 sampling volume hint).
- Settled decisions disagreed with: none.
- Review fixes applied: 7 of 7 (R-01 to R-07); flags R-08 to R-18 left to the Opus pass.

## L2 claims

Marks: G grounded, I inferred, O open. Pins as in L1.

Reliability and alerting
- G: reliability is an objective below 100 percent on a few user-view indicators, latency stated as percentiles (RELIABILITY.1, .2).
- G: a provisional objective from measurable history is allowed only as marked, reviewed provisional; this reconciles L179 (a) and (b) as one rule with a start condition (F1).
- G/O: the error budget is a written, agreed rule (G); a no-budget view is unsourced (O). Budget exhaustion consequence is decided in advance: freeze with many consumers, strict commitments or weak safety culture, self-regulation in small high-trust teams (RELIABILITY.3, .4; I for the culture condition).
- G: page only on urgent, actionable, user-visible conditions needing judgment; prune dead rules (ALERTING.1).
- G/I: page on symptoms; a cause alert pages only for imminent user-visible failure (I: this resolves the early-warning-against-noise tension); burn-rate alerts where an objective exists, thresholds otherwise (G on one authority, REG-132).

Telemetry
- G: golden signals per user-facing service, internal plus external probing, per-statement database statistics (TELEMETRY.1). The maintainer's four job signals (duration, failure, backlog, missed runs) are best for scheduled work and are required by DATA_INTEGRITY.4 (G, F2).
- G/I: monitoring and observability both, correlated and designed in; storage model chosen by condition (I, F3); pipeline checked (G one T2; mechanism I).
- G: vendor-neutral instrumentation, automatic plus code-based, libraries depend on the API; stdout event stream where the environment collects it (I: file or collector otherwise).
- G/I: one trace context across every tier; ids in every log; client events stamped (I).
- G/I: sampling is explicit: all traces at low volume, head for healthy predictable traffic, tail where rare errors must be kept (I for the ladder, F11).
- G/I/O: label cardinality bounded, volume treated as cost (G); a per-service bound is adopted (I, O: no source, F4).

Incidents, capacity, readiness, runbooks
- G: declare on written conditions, named roles, rehearsed severities; blameless postmortems on written triggers with tracked actions (INCIDENTS.1, .2).
- G/I: operating load is bounded by stated limits; the numbers are Google-scale, small teams set their own (F6).
- G/I: plan capacity in resources before predicted change; declared requirements at scale, spreadsheet for small teams; headroom from the tested breaking point (O: no numeric headroom).
- G/I: storage health routine adopted from the maintainer; caveats inferred (F9).
- G/I: launch gate with an own-history checklist; review form scales with criticality (I, F7).
- G: runbooks validated by another person; playbooks separate; automation staged from low-risk procedures (O: risk of automating a wrong runbook).

Recovery and feedback
- G: objectives per workload from impact, data and service recovery stated separately (RECOVERY.1).
- G: replication is not recovery; classify data, back up the rebuild set and keys apart from the data (RECOVERY.2).
- G/I: one copy independent of production credentials, always; immutable or offline form by threat model; 3-2-1-1-0 where destructive attack is in scope (I, F8).
- G/I: strategy by tier against objectives; an unexercised fallback is not allowed; failover is human-started unless the objective is shorter than a human can meet (I for the reconciliation, F9).
- G/O: recovery independent of what failed, rebuilt from source; hardening is preferred to recovery speed by default (O: one T3 source, F5).
- G/I: a named durability owner, verified alert path, plan reviewed on every change, roles assigned beforehand (G for upkeep and roles, I for owner and monitoring).
- G: delivery measures feed back to development and are never targets (O for the contrary view).

Review fixes (all applied)
- G: INCIDENTS.3 on-call familiarity is per engineer of the rotation (R-01); INCIDENTS.1 lets the operations lead and the team they direct change the system (R-02); the L1 roll-up now includes FEEDBACK (R-03); personal data in trace context is left to TRANSVERSE.PRIVACY (R-04); RECOVERY.6 points to AVAILABILITY.4 and applies the four job signals (R-05); RELIABILITY links to AVAILABILITY (R-06); RELIABILITY.3 cites REG-134 and REG-128 for the agreement rule (R-07).

Binding to decided units
- G: RECOVERY realizes AVAILABILITY.4 and .5 (objectives are the criteria its proof fixes in advance); CAPACITY.2 consumes PERFORMANCE.2; TELEMETRY.1 supplies DATA_INTEGRITY.4; RUNBOOKS and RECOVERY.6 apply DOCS_SYNC.3 without restating it.

## L3 full

Pinned, word for word:
- Nodes judged: 39 (OPERATION; RELIABILITY .1-.4; ALERTING .1-.2; TELEMETRY .1-.6; INCIDENTS .1-.3; CAPACITY .1-.3; READINESS .1-.3; RUNBOOKS .1-.2; RECOVERY .1-.6; FEEDBACK), 109 rows.
- Decisions marked undecided: none.
- Flags raised: 11 (F1 PERFORMANCE.1 wording against L179, F2 TELEMETRY.1 split and job-design placement, F3 TELEMETRY.2 storage model evidence, F4 TELEMETRY.6 budget unsourced, F5 RECOVERY.5 hardening against speed, F6 INCIDENTS.3 small teams, F7 READINESS.2 no effectiveness evidence, F8 RECOVERY.3 extension and dual authorisation boundary, F9 inferred reconciliation in RECOVERY.4 and CAPACITY.3 caveats, F10 L1 record overlap with wave 3, F11 sampling volume hint).
- Settled decisions disagreed with: none.
- Review fixes applied: 7 of 7 (R-01 to R-07); flags R-08 to R-18 left to the Opus pass.

Method
- Read: the brief, `maintainer_decisions.md`, `target_hierarchy.md`, units.md row J7, the OPERATION branch record, the resolution of routing objections, all 109 ledger rows in full (L174 to L209, L313, L317, L436 to L460, L1079 to L1118, L1148, L1163 to L1181, L1253), and the J4 and J3 judged records for the nodes OPERATION realizes or is linked from (J4: PERFORMANCE.1 to .5, AVAILABILITY.1 to .5; J3: DATA_INTEGRITY.3, .4, DOCS_SYNC.3, SECURITY.6, .7) with J4's review result. Sources were not re-fetched; where a position needed more than the ledger row, the claim is marked inferred.
- Not done: no source read beyond the ledger, so every "grounded" rests on the ledger's stated grounding, including its single-source notes.

Judged by node, one line each (full records in `judged.md`)
- OPERATION (L1, F10) and the nine L2 roll-ups: I, index only.
- RELIABILITY.1 G user-view indicators, percentiles. .2 G below 100 percent, from user need, provisional start allowed with review (F1). .3 G written, agreed budget policy; O for the no-budget view. .4 decided in advance; freeze or self-regulation by consumers, commitments, safety culture.
- ALERTING.1 G one paging criterion, human judgment, pruning. .2 G symptoms; I cause alerts only for imminent harm; burn rate with an objective, thresholds without.
- TELEMETRY.1 G signals by vantage point and workload, with the four job signals (F2). .2 both monitoring and observability, store by condition (F3). .3 neutral API, stdout stream. .4 one context, ids in logs. .5 explicit sampling (F11). .6 cost bounded, per-service bound I/O (F4).
- INCIDENTS.1 written declaration and roles. .2 blameless postmortems, tracked actions, risk integration. .3 stated load limits (F6).
- CAPACITY.1 resources, before change, scale condition. .2 headroom from the tested breaking point. .3 maintainer storage routine (F9).
- READINESS.1 gate and own-history checklist. .2 form by criticality (F7). .3 periodic re-run, guardrails.
- RUNBOOKS.1 validated runbooks, separate playbooks. .2 staged automation.
- RECOVERY.1 objectives. .2 backup scope. .3 isolation, credential-holding attacker (F8). .4 strategy, failover rule, failback (F9). .5 independence, rebuild, hardening default (F5). .6 owner, monitoring, upkeep, roles.
- FEEDBACK G feedback, not targets.

Rejected positions that carry a condition (the ones a reviewer is most likely to want back)
- No error budget: best when one party owns speed and reliability (O).
- High declaration bar: best in a team too small to staff roles (I, O).
- Vendor SDK for instrumentation: best when one backend is fixed and a vendor feature outweighs exit cost (I).
- Wide events as universal store, separate stores as universal store: each best in its stated condition (G on the conditions, evidence argued).
- Pre-provision against autoscale; independent against self-service review; offline against immutable backup; automatic against human-started failover: each best in the stated condition.
- Favour recovery speed over hardening: best when the objective cannot be met by the hardened path (I, O).

Review applied
- R-01 to R-07: applied, 7 of 7; detail in the last section of `judged.md`. R-08 to R-18 are flags, not acted on.

Notes for the graph build
- TELEMETRY.1 (eleven rows, seven subjects) and RECOVERY.4 (eight positions, five subjects) are candidates to split.
- The L2 and L1 records hold index text only (MD-03); constraints are on the L3 records.
- Stack pointers kept off the decisions: L1177, L454, L196 to L198, L199, L1164, L1170, L457 to L459, L317, L1094, L1118, L1088.

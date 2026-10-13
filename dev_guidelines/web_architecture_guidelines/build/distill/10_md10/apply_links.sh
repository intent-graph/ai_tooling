#!/bin/zsh
# Link edits of MD-10, run from the guideline folder. One command per link: apply --batch does not dispatch inter links.
set -e
PIG=intent_graphs/web_defaults.ig.yaml
PH=intent_graphs/web_app_philosophy.ig.yaml
SW=software-development-philosophy
set_link() { # graph uid intent
  ig-tool link set -g "$1" --uid "$2" --intent "$3" -o "$1" --role steward -m "MD-10: link intent follows the aligned node" > /dev/null
}
new_link() { # graph src dst shape intent note
  ig-tool link create -g "$1" --src "$2" --dst "$3" --shape "$4" --intent "$5" -o "$1" --role steward -m "$6" > /dev/null
}

set_link $PIG "pig-web-defaults:PIG-WEB-TRANSVERSE.SECURITY.4_${SW}:TRANSVERSE.CONFIG.2" "A secret reaches the process at start by runtime injection, as a mounted file readable only by the service account or through the store's interface; an environment variable is a recorded exception where the platform offers neither or the process environment is shown not to leak."
set_link $PIG "pig-web-defaults:PIG-WEB-TRANSVERSE.SECURITY.5_${SW}:ASSURANCE.ARTIFACT.1" "Signed provenance from a hosted build platform is verified before deploy, at SLSA Build L2 as the floor and Build L3 where insider or credential-compromise risk matters or the software is distributed to others; the level is recorded per project."
set_link $PIG "pig-web-defaults:PIG-WEB-LOGIC.SECURE.7_${SW}:CONSTRUCTION.DATA_NOT_CODE.3" "Every server-side fetch of a client- or agent-named URL goes through one helper that matches the host against an allowlist where the hosts are known and refuses private, loopback and link-local addresses where users may name any public host, connects only to the validated address and re-checks every redirect hop; an egress proxy or outbound rules back it where the hosting can enforce them."
set_link $PIG "pig-web-defaults:PIG-WEB-LOGIC.SECURE.7_web-app-philosophy:LOGIC.SECURE" "Realizes the rule that server-side fetches reach only allowed destinations and cannot reach internal addresses."
set_link $PIG "pig-web-defaults:PIG-WEB-DATA.MAINTAIN.5_${SW}:OPERATION.RECOVERY.2" "Point-in-time copies are kept: where the objective on data loss is shorter than the interval between base backups, base backups plus continuous WAL archiving give recovery to a chosen moment, with retention and tracked chains; logical dumps serve portability only, fsync is never off and synchronous_commit is relaxed only for data that may be lost on a crash."
set_link $PIG "pig-web-defaults:PIG-WEB-DATA.MAINTAIN.5_${SW}:OPERATION.RECOVERY.3" "At least one copy of the base backups and WAL archive lies outside the failure and attack domain of production and cannot be reached with production credentials; no single credential or person can delete every copy or shorten its retention."
set_link $PIG "pig-web-defaults:PIG-WEB-DATA.MAINTAIN.5_web-app-philosophy:DATA.MAINTAIN" "Realizes recovery from per-workload objectives, with a copy out of reach of production credentials, proven by automated restore tests."
set_link $PIG "pig-web-defaults:PIG-WEB-LOGIC.PROCESS.3_${SW}:ASSURANCE.AVAILABILITY.2" "Every outbound call has a timeout shorter than its caller's remaining deadline, retries run at exactly one layer (at most three attempts and a 10% retry budget per client in the request path) only for idempotent or keyed calls, and a circuit breaker with logged state changes guards a request-path dependency only where it fails slowly or is shared by many callers."
set_link $PIG "pig-web-defaults:PIG-WEB-TRANSVERSE.SECURITY.1_${SW}:TRANSVERSE.SECURITY.1" "The requirements standard is ASVS 5.0, cited by versioned id, at a level recorded per project by risk (Level 2 by default, Level 3 for critical data, never Level 1) and paired with outcome measures."
set_link $PIG "pig-web-defaults:PIG-WEB-TRANSVERSE.EVOLUTION.3_${SW}:EVOLUTION.DECISIONS.4" "An accepted ADR is not rewritten to change its decision, only superseded by a new ADR that it links to; corrections that do not change the decision (a typo, a broken link) edit it."
set_link $PH "web-app-philosophy:DATA.MAINTAIN_${SW}:ASSURANCE.AVAILABILITY.4" "Recovery follows objectives set per workload, and a backup counts only once a restore from it was tested end to end, regularly and automatically, against criteria fixed beforehand."
set_link $PH "web-app-philosophy:TRANSVERSE.EVOLUTION.3_${SW}:CONSTRUCTION.SYSTEM_SHAPE.1" "Each backend is one deployable modular by business concept and is split into services only when a named force requires it (independent scaling, independent release by separate teams, fault isolation that matters, a different runtime need); web adds that several backends may share one database."
set_link $PH "web-app-philosophy:TRANSVERSE.EVOLUTION.4_${SW}:EVOLUTION.TECHNOLOGY.1" "Few mature technologies are adopted, and a new one enters as a replacement with the retirement of the older one planned and owned, only when an existing one's measured limit is reached and its perpetual operating cost is budgeted; runtimes, stores, services and frameworks are counted."

# S1 to S3: deferred web nodes depend on the principle owned by the software guideline
N="MD-10: deferred web node points to the software guideline"
new_link $PIG pig-web-defaults:PIG-WEB-TRANSVERSE.OPERABILITY.7 ${SW}:OPERATION.INCIDENTS '{"type":"requires"}' "The web realization of incident response is deferred; it depends on the incident rules (declaration on written conditions, named roles, blameless review) that the software guideline owns." "$N"
new_link $PIG pig-web-defaults:PIG-WEB-TRANSVERSE.OPERABILITY.7 ${SW}:OPERATION.READINESS '{"type":"requires"}' "The web realization of incident response is deferred; it depends on the operational readiness review that the software guideline owns." "$N"
new_link $PIG pig-web-defaults:PIG-WEB-TRANSVERSE.OPERABILITY.7 ${SW}:OPERATION.RUNBOOKS '{"type":"requires"}' "The web realization of incident response is deferred; it depends on the owned, validated runbooks that the software guideline owns." "$N"
new_link $PIG pig-web-defaults:PIG-WEB-DATA.MAINTAIN.6 ${SW}:TRANSVERSE.PRIVACY.3 '{"type":"requires"}' "The web realization of personal data erasure is deferred; it depends on the erasure and deletion mechanism (deletion decided per entity, an inventory of copies, erased data in a backup put beyond use) that the software guideline owns." "$N"
new_link $PIG pig-web-defaults:PIG-WEB-DATA.MAINTAIN.7 ${SW}:OPERATION.RECOVERY.4 '{"type":"requires"}' "The web realization of high availability and replication is deferred; it depends on the recovery strategy, failover and failback rules that the software guideline owns." "$N"
new_link $PIG pig-web-defaults:PIG-WEB-DATA.MAINTAIN.7 ${SW}:ASSURANCE.AVAILABILITY.1 '{"type":"requires"}' "The web realization of high availability and replication is deferred; it depends on the degraded-mode and overload rules for dependencies that the software guideline owns." "$N"

# links for the aligned nodes that now state a software rule not yet linked
N2="MD-10: aligned node links the software node it now follows"
new_link $PIG pig-web-defaults:PIG-WEB-DATA.MAINTAIN.5 ${SW}:OPERATION.RECOVERY.1 '{"type":"refines"}' "Recovery point and recovery time objectives are set per workload or data class from the impact of loss and downtime, and the strategy is never stricter than they need." "$N2"
new_link $PIG pig-web-defaults:PIG-WEB-LOGIC.EXPOSE.7 ${SW}:ASSURANCE.CONTRACTS.1 '{"type":"refines"}' "Versioning follows consumer reach: the JSON interface is versioned under /v1 for many, external or independently released consumers (open pages and agent clients in the default context), and additive with a coordinated deploy for few in-house consumers." "$N2"
new_link $PIG pig-web-defaults:PIG-WEB-TRANSVERSE.SECURITY.1 ${SW}:TRANSVERSE.SECURITY.2 '{"type":"refines"}' "The ASVS level measures activity and coverage, not outcomes: it is recorded beside outcome measures and never reported as proof that the system is safer." "$N2"
echo done

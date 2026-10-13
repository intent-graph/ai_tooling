## L1 headline

- Applied MD-10: ten web positions (K3 to K12) now match the software development guideline while keeping the stack realization; K1 and K2 unchanged; three deferred nodes (S1 to S3) point to the software guideline; G1 recorded as a gap on two delivery nodes, no rule added.
- Nodes changed: 7 in `web_app_philosophy.ig.yaml` (2 core, 4 propagation, 1 gap) and 22 in `web_defaults.ig.yaml` (9 core, 9 propagation, 3 deferred, 1 gap); 29 in all. Links: 9 inter links created (6 for S1 to S3, shape `requires`; 3 for K6, K8, K12, shape `refines`), 13 link intents rewritten where they stated the old rule.
- Checks: `ig-tool validate -g <graph> -m intent_graphs/intent_resources.yaml` gives 0 errors, 0 warnings, 0 issues on both graphs (philosophy 80 nodes, 66 inter links; defaults 132 nodes, 176 inter links). Relative link and anchor check over the 11 web markdown files: 641 links, 0 broken. Longest file 490 lines (`allocation.md`); `md-structure-sync --max-level 2` run on the 8 edited files that carry a TOC.
- Markdown: sections showing a changed node re-rendered in `philosophy.md`, `allocation.md`, `stack_defaults_data.md`, `stack_defaults_logic.md`, `stack_defaults_logic_security.md`, `stack_defaults_agents.md`, `stack_defaults_transverse.md`; README gains decision 10 (and "Ten maintainer decisions"); `CLAUDE.md` says "ten" instead of "nine".
- Judgment calls to confirm: the file fallback for secrets without a store is kept as the recorded exception (MD-06 stands); three links beyond S1 to S3 were added (K6, K8, K12); each software node named for S1 to S3 got its own link (6 links); the default context is stated to count as "many, external or independently released consumers" for K8 (inferred). The Obsidian export under `intent_graphs/obsidian_export/` was not regenerated and is now stale.

## L2 claims

K items (web node, new position):
- K3 `PIG-WEB-TRANSVERSE.SECURITY.4`: managed store primary; delivery by runtime injection (mounted file or store interface); environment variable only as a recorded exception; file fallback kept as the recorded exception without a store (MD-06).
- K4 `PIG-WEB-TRANSVERSE.SECURITY.5`: signed provenance from a hosted platform verified before deploy; Build L2 the floor; hardened isolated build (Build L3) where insider or credential-compromise risk matters or the software is distributed; level recorded per project.
- K5 `PIG-WEB-LOGIC.SECURE.7`: host allowlist where the destinations are known; private, loopback, link-local and metadata refusal where users may name any public host; connect only to the validated address; every redirect target re-checked.
- K6 `PIG-WEB-DATA.MAINTAIN.5`: objectives per workload first, strategy never stricter than needed; point-in-time recovery where the data-loss objective is shorter than the base-backup interval (usual for the system of record, inferred); one copy out of reach of production credentials; restore tests end to end, regular, automatic, with fixed criteria.
- K7 `PIG-WEB-LOGIC.PROCESS.3`: circuit breaker, state changes logged, only for a dependency that fails slowly or is shared by many callers.
- K8 `PIG-WEB-LOGIC.EXPOSE.7`: versioning follows consumer reach; `/v1` from the start for many, external or independently released consumers (the default context); additive change and a coordinated deploy for few in-house consumers released with the API.
- K9 `TRANSVERSE.EVOLUTION.3` and `PIG-WEB-TRANSVERSE.EVOLUTION.1`: a split needs a named force (independent scaling, independent release by separate teams, fault isolation, a different runtime need), stated in the ADR, on a proven boundary with a budgeted premium.
- K10 `TRANSVERSE.EVOLUTION.4`: a new technology enters as a replacement, the older one's retirement planned and owned (or the record says why it replaces nothing), plus the unchanged measured-limit and cost conditions; applied to the move of a role out of Postgres (`PIG-WEB-ALLOCATION.POSTGRES_FIRST`).
- K11 `PIG-WEB-TRANSVERSE.EVOLUTION.3`: an accepted ADR is not rewritten to change its decision (superseded, marked, linked to its successor); typo and broken-link corrections may edit it.
- K12 `PIG-WEB-TRANSVERSE.SECURITY.1`: the ASVS level measures coverage, not outcomes; recorded beside per-project outcome measures; never reported as proof of safety.
- K1, K2: nothing changed (reads on base tables, MD-05; default soft delete, MD-04).

S and G items:
- S1 `PIG-WEB-TRANSVERSE.OPERABILITY.7`: still deferred; intent and notes name the owning software nodes (`OPERATION.INCIDENTS`, `OPERATION.READINESS`, `OPERATION.RUNBOOKS`); 3 `requires` links.
- S2 `PIG-WEB-DATA.MAINTAIN.6`: still deferred; principle owned by `TRANSVERSE.PRIVACY.3`; 1 `requires` link; MD-04 deletion default untouched.
- S3 `PIG-WEB-DATA.MAINTAIN.7`: still deferred; principle owned by `OPERATION.RECOVERY.4` and `ASSURANCE.AVAILABILITY.1`; 2 `requires` links.
- G1 `TRANSVERSE.OPERABILITY.3` and `PIG-WEB-TRANSVERSE.OPERABILITY.6`: epistemic annotation `gap: no rollback or fix-forward rule for releases or data changes; principle in software-development-philosophy:CHANGE_FLOW.ROLLBACK (MD-10)`; "Gap:" line in both rendered sections; no rule added.

## L3 full

### Method

- Graph edits: two `ig-tool apply --batch` files (`batch_pig.yaml`, `batch_phil.yaml`, kept in this folder) with `--role steward`, one message per batch; links by `apply_links.sh` (this folder), one `ig-tool link set` or `link create` per link with qualified uids. The shell variable in that script is written `${SW}` because zsh reads `$SW:A` as a path modifier.
- Every changed core node got a design-notes paragraph that names the software node ("aligned with software-development-philosophy:<UID> by MD-10"), says which earlier Decision or Rejected lines it supersedes, records the replaced position as a rejected option with the condition under which it would still be best, and lists what is kept. Epistemic states carry "MD-10" where it settled the position; clauses I derived are marked "(inferred)" in the node and in the markdown.
- Propagation followed PRIMER_03A: parents and the philosophy or PIG counterpart that restates the rule (wave 1), then link intents and rendered sections (wave 2). It quiesced at wave 2.

### K3 secrets delivery: `PIG-WEB-TRANSVERSE.SECURITY.4`

- Old: store is the authority; delivery at start by a file readable only by the service account or an environment variable no other process can read, the two treated as equal; a file fallback without a store on self-managed hosting.
- New: store is the authority and the primary source; delivery by runtime injection, as a mounted file readable only by the service account or through the store's interface, never inside the artifact; an environment variable only where the platform offers neither or the process environment is shown not to leak, with channel and reason recorded as an ADR. Without a store on self-managed hosting, the file outside source control is the recorded exception (MD-06; the software node does not cover a host without a store).
- Rejected option recorded: environment variable as an equal channel; still best (simplest, most portable) where neither a mounted file nor a store interface exists, or the environment is shown not to leak.
- Propagation: `PIG-WEB-TRANSVERSE.SECURITY` (intent, constraint), `PIG-WEB-TRANSVERSE` (security constraint), `PIG-WEB-TRANSVERSE.EVOLUTION.3` (ADR list: each environment variable used for a secret); link to `TRANSVERSE.CONFIG.2` rewritten. `OPERABILITY.6` ("secrets come from the store") unchanged. Rendered: Secrets, Decision Records.

### K4 build provenance: `PIG-WEB-TRANSVERSE.SECURITY.5`

- Old: signed provenance at SLSA Build L3 by default; Build L2 only when the platform cannot isolate runs or keep the signing key from build steps.
- New: signed provenance from a hosted platform verified before deploy, Build L2 the floor, hardened isolated build (Build L3) where insider or credential-compromise risk matters or the software is distributed to others; level recorded per project as an ADR with the gap to the floor where below it. Hash pinning, SBOM, official sources unchanged.
- Rejected option recorded: Build L3 for every project; best, and then required, under the risk condition above.
- Propagation: `PIG-WEB-TRANSVERSE.SECURITY` (intent, constraint), `PIG-WEB-TRANSVERSE` (constraint), `PIG-WEB-TRANSVERSE.EVOLUTION.3` (ADR list: build level by risk); link to `ASSURANCE.ARTIFACT.1` rewritten. Rendered: Supply Chain (the "Acceptable when" line now names the Build L3 condition).

### K5 server-side fetch: `PIG-WEB-LOGIC.SECURE.7`

- Old: one helper refusing private, loopback and link-local ranges for every fetch, every other host allowed.
- New: one helper that fetches only allowed destinations: allowlist where the hosts are known; range refusal (private, loopback, link-local, metadata) where users may name any public host; validated address only; redirect targets re-checked. Network guard and its "required when" condition, timeout, size cap unchanged. Forbidden clause now "fetching without a destination rule".
- Rejected option recorded: range refusal alone; the only possible rule where any public host may be named.
- Propagation: `PIG-WEB-LOGIC.SECURE` (intent, constraint), `LOGIC.SECURE` (philosophy constraint), `PIG-WEB-INTERACTION.AGENT.2` (client metadata document: any public host may be named, so the range refusal applies; through the helper); links to `CONSTRUCTION.DATA_NOT_CODE.3` and `LOGIC.SECURE` rewritten. Rendered: Secured Entry, Backend Security Overview, Server-Side Fetch, Discovery and Registration.

### K6 backup and recovery: `PIG-WEB-DATA.MAINTAIN.5`

- Old: point-in-time recovery by default (base backups plus continuous WAL archiving to a repository on another host); restores rehearsed on a schedule; gap "recovery objectives have no row".
- New: objectives per workload or data class, strategy never stricter than needed; point-in-time recovery where the data-loss objective is shorter than the base-backup interval (usual for the shared system of record, inferred), rebuild or periodic backup for rebuildable data (inferred); at least one copy outside production's failure and attack domain and out of reach of production credentials, no single credential or person able to delete every copy or shorten retention, encrypted; restore tested end to end, regularly and automatically, against criteria fixed beforehand, by its own path independent of migration tooling, integrity verified before restore. Logical-dump, configuration, fsync and synchronous_commit rules unchanged. The gap is closed by `OPERATION.RECOVERY.1` and replaced by "objective values set per project; no restore-test tool chosen".
- Rejected options recorded: point-in-time recovery as an unconditional default (best for the system of record whenever the data-loss objective is shorter than the base-backup interval, inferred); "another host" as the independence rule (enough only where production credentials cannot reach it and none can delete every copy); a schedule without automation or fixed criteria (acceptable for loose objectives and recreatable data, inferred).
- Propagation: `DATA.MAINTAIN` (philosophy constraint), `PIG-WEB-DATA.MAINTAIN` (intent, constraint, epistemic state), `PIG-WEB-DATA` (constraint); links to `OPERATION.RECOVERY.2`, `OPERATION.RECOVERY.3`, `DATA.MAINTAIN` and, in the philosophy graph, `ASSURANCE.AVAILABILITY.4` rewritten; new link to `OPERATION.RECOVERY.1`. Rendered: Maintained Over Time, Data Tier Overview gap line, Data Maintenance, Backup and Recovery.

### K7 circuit breaker: `PIG-WEB-LOGIC.PROCESS.3`

- Old: a circuit breaker per external dependency called from the request path.
- New: a breaker, state changes logged, only where a dependency fails slowly or is shared by many callers. Timeouts, one retry layer, retry budget, idempotency keys unchanged.
- Rejected option recorded: breaker on every dependency; still best wherever a failing dependency can exhaust workers or connections despite its timeout (with synchronous workers a slow dependency holds a worker until timeout, inferred).
- Propagation: no parent states the breaker (`PIG-WEB-LOGIC.PROCESS` rolls it up as "bounded and retried at one layer"); link to `ASSURANCE.AVAILABILITY.2` rewritten. Rendered: Resilience.

### K8 versioning: `PIG-WEB-LOGIC.EXPOSE.7`

- Old: JSON under `/v1` from the start for every JSON interface; unversioned JSON paths forbidden until the first break.
- New: versioning follows consumer reach (`ASSURANCE.CONTRACTS.1`, `CHANGE_FLOW.RELEASE.2`): `/v1` from the start for many, external or independently released consumers, which the node now says the default context is (pages open in tabs outlive a deploy; agent clients run code the team does not release; inferred); additive change and a coordinated deploy without version numbers for few, in-house, reachable consumers released with the API. The `/v2`-beside-`/v1` break rule now reads "of a versioned interface"; the Forbidden clause is "unversioned JSON paths for consumers the team does not release together with the API". The CI gate (MD-02), skew window, server-first fields, deprecation signals unchanged.
- Rejected options recorded: version numbers whatever the consumers (best in the default context); unversioned JSON (acceptable for few in-house consumers released with the API).
- Propagation: `PIG-WEB-LOGIC.EXPOSE` (constraint points to EXPOSE.7); new link to `ASSURANCE.CONTRACTS.1`. Rendered: API Evolution (Principle gains "What Counts as Compatible"). The HTTP Interface overview line still says "under `/v1`", true for the default context.

### K9 reasons to split: `TRANSVERSE.EVOLUTION.3` and `PIG-WEB-TRANSVERSE.EVOLUTION.1`

- Old: split only when a team needs independent releases (philosophy); when size, complexity or the number of teams make the single unit the bottleneck (PIG).
- New: both state the same rule: a named force (independent scaling, independent release by separate teams, fault isolation that matters, a different runtime need), stated in the ADR, on a proven boundary with a budgeted premium; the PIG adds that independent scaling is first sought through process types of one deployable (inferred). Data seam, function API with own role, no second system of record, domain schemas unchanged.
- Rejected options recorded: independent release as the only reason (best where scaling, fault isolation and runtime needs are met inside one deployable); the bottleneck test alone (still the trigger to look for a split).
- Propagation: the statements "each backend is one deployable, not split into services without a measured need" in `TRANSVERSE.EVOLUTION`, `PIG-WEB-TRANSVERSE.EVOLUTION`, `PIG-WEB-TRANSVERSE`, `PIG-WEB-LOGIC` and `PIG-WEB-LOGIC.ENFORCE` stay: a named force with a measured benefit is the need, so they are consistent and were not rewritten. Link `TRANSVERSE.EVOLUTION.3` to `CONSTRUCTION.SYSTEM_SHAPE.1` rewritten. ADR list gains "every split of a deployable, with its named force". Rendered: Deployable Boundaries, Deployables ("Changes when").

### K10 new technology: `TRANSVERSE.EVOLUTION.4`

- Old: a new technology enters only when an existing one's measured limit is reached and its perpetual operating cost is budgeted.
- New: it enters as a replacement, the older one's retirement planned and owned (the record names what it replaces, or why it replaces nothing); the two old conditions and the scope (runtimes, stores, services, frameworks; not paradigm) unchanged.
- Rejected option recorded: addition without a retirement plan; best when the technology replaces nothing because it serves a role no adopted technology serves. The software allowance for a few independently operated components (`EVOLUTION.TECHNOLOGY.3`) is not carried (default context shares one database, platform and on-call, inferred); the register of positions (`EVOLUTION.TECHNOLOGY.2`) is not added, as MD-10 does not ask for it.
- Propagation: `TRANSVERSE.EVOLUTION` (constraint), `PIG-WEB-ALLOCATION.POSTGRES_FIRST` (constraint: a move out of Postgres retires the Postgres implementation by plan, or the ADR says why not), ADR list ("what it replaces and who retires it"); link `TRANSVERSE.EVOLUTION.4` to `EVOLUTION.TECHNOLOGY.1` rewritten. `PIG-WEB-INTERACTION.REALTIME.3` (Redis at a measured limit) examined and left as is. Rendered: Few Mature Technologies, Postgres First for Backing Roles.

### K11 editing an accepted record: `PIG-WEB-TRANSVERSE.EVOLUTION.3`

- Old: accepted ADRs are never edited, only superseded.
- New: an accepted ADR is not rewritten to change its decision; a changed decision is a new ADR that supersedes it, the old one stays marked superseded with a link to its successor; corrections that do not change the decision (a typo, a broken link) may edit it. The per-project ADR list also covers the build level, environment variables for secrets, outcome measures, retirement owners and named split forces.
- Rejected option recorded: the absolute never-edit rule; best where the ADR set must be a tamper-evident record (inferred).
- Propagation: `PIG-WEB-TRANSVERSE.EVOLUTION` (constraint "superseded rather than rewritten"); link to `EVOLUTION.DECISIONS.4` rewritten. Rendered: Decision Records.

### K12 ASVS level: `PIG-WEB-TRANSVERSE.SECURITY.1`

- Old: ASVS 5.0 at a level recorded per project by risk (Level 2 default, Level 3 for critical data, never Level 1).
- New: same, plus: the level measures activity and coverage, not outcomes; it is recorded beside outcome measures chosen per project (examples inferred: open findings by severity and age, time to fix, incidents and causes; no target values) and never reported as proof of safety.
- Rejected option recorded: the level alone; acceptable as the reporting form where a contract or regulation demands the level as such (inferred).
- Propagation: `PIG-WEB-TRANSVERSE.SECURITY` (intent, constraint), `TRANSVERSE.SECURITY` (philosophy constraint), `PIG-WEB-TRANSVERSE` (constraint); link to `TRANSVERSE.SECURITY.1` rewritten; new link to `TRANSVERSE.SECURITY.2`. Rendered: Security Across Tiers, Security Defaults, Security Requirement Catalogue.

### K1, K2

- `ALLOCATION.RECORD.2`, `PIG-WEB-ALLOCATION.DB_API`, `PIG-WEB-DATA.MAINTAIN.2`: not touched. README decision 10 states that decisions 4 and 5 stand and that the software guideline is asked to scope its own rules.

### S1 to S3 (deferred nodes, kept deferred)

- S1 `PIG-WEB-TRANSVERSE.OPERABILITY.7`: old "out of scope for this guideline, recorded only"; new: principle owned by `OPERATION.INCIDENTS`, `OPERATION.READINESS`, `OPERATION.RUNBOOKS`; web-specific realization deferred, no web practice decided. Epistemic state `deferred: web-specific realization not researched or judged; the principle is decided in software-development-philosophy (MD-10)`. Links (shape `requires`, from `pig-web-defaults:` to `software-development-philosophy:`): one to each of the three nodes, intents say the web realization is deferred. Rendered section gains the "Principle:" line.
- S2 `PIG-WEB-DATA.MAINTAIN.6`: principle owned by `TRANSVERSE.PRIVACY.3`; one `requires` link; Deferred Topics bullet gains the pointer. The deletion default (MD-04) is unchanged.
- S3 `PIG-WEB-DATA.MAINTAIN.7`: principle owned by `OPERATION.RECOVERY.4` and `ASSURANCE.AVAILABILITY.1` (names taken from the linking pass; the second covers degraded dependencies and fits only loosely); two `requires` links; Deferred Topics bullet gains the pointers. `PIG-WEB-DATA.MAINTAIN` epistemic state now says the web realization is deferred and the principle owned by the software guideline.
- Shape: the link semantics primer defines `requires` as "Y depends on X's capability being available"; `refines` was not used because the web node adds nothing.

### G1 rollback gap

- `TRANSVERSE.OPERABILITY.3` and `PIG-WEB-TRANSVERSE.OPERABILITY.6`: the annotation was appended to the epistemic state in the exact wording given; the rendered sections (`philosophy.md` Reproducible Delivery, `stack_defaults_transverse.md` Delivery and Configuration) show a "Gap:" line pointing to the software Rollback section. No constraint, link or rule added.

### Rendered files touched

- `README.md`: "Ten maintainer decisions"; decision 10 as one paragraph (aligned positions, unchanged decisions 4 and 5, deferred nodes, rollback gap), linking the MD-10 section of the maintainer decisions file; glossary links at first use of SLSA and ASVS; TOC ranges re-synced.
- `philosophy.md`: Maintained Over Time, Secured Entry, Security Across Tiers, Reproducible Delivery, Deployable Boundaries, Few Mature Technologies.
- `allocation.md`: Postgres First for Backing Roles.
- `stack_defaults_data.md`: Data Maintenance intro, overview table row and gap line, Backup and Recovery, Deferred Topics.
- `stack_defaults_logic.md`: Resilience, API Evolution. `stack_defaults_logic_security.md`: overview bullet, Server-Side Fetch. `stack_defaults_agents.md`: Discovery and Registration.
- `stack_defaults_transverse.md`: Security Defaults intro, Security Requirement Catalogue, Secrets, Supply Chain, Delivery and Configuration, Incident Response, Deployables, Decision Records.
- `CLAUDE.md`: "nine" changed to "ten" (one word). Each edited section keeps its closing uid; no file above 500 lines.

### Not done, and why

- `intent_graphs/obsidian_export/` not regenerated (outside the scope list); run `intent_graphs/export_to_obsidian.sh` to refresh it.
- `build/distill/maintainer_decisions.md` and the 09 result were left unchanged (history).
- No git command was run; nothing under the software guideline or other guidelines was edited.

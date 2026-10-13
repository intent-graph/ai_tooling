# J6_change_flow: review result

## L1 headline

Pin: records reviewed: 42 (all of J6_change_flow, eight L2 and 34 L3). Findings fix: 6 (FX1 to FX6). Findings flag: 9 (FL1 to FL9; FL5 to FL9 carry judge flags F1, F4, F11, F12, F13). Sources fetched: 7, confirmed: 6 (one partial: the GitLab guide).

The unit is sound and consistent with the settled records; no contradiction with J2, J3, J4 or the cross-unit fixes. The central split passes the MD-01 test in part. Environment parity by axis is the best, not a blend (grounded: Twelve-Factor fixes kind and version and is silent on data volume). The database-change split by risk class is not an average, but its human-triggered production run for the risky class rests on the maintainer alone; the public form is a human authorization stage inside the one pipeline. The wording should make the gate a pipeline stage (flag FL1, for the Opus pass). Six clear defects are for the judge to apply: the missing decision on configuration-like content, an overstated GitLab ground, an unconditional urgent-fix stream, a restated run restriction, an unsupported pull-or-push condition, and roll-up flag lists.

## L2 claims

Pin: records reviewed: 42. Findings fix: 6. Findings flag: 9. Sources fetched: 7, confirmed: 6.

Marks: G grounded, I inferred, O open.

- Database change split by risk class: ordinary changes automatic is the public best (G: DORA says 100% of database changes go through an automated, version-controlled process). The risky class needs a person's authorization on the exact script before production (I: Fowler allows human authorization stages; the criterion list is the maintainer's). That a named group must trigger the run, rather than the pipeline after authorization, has no public source (O); as worded it risks becoming the "separate manual track" the node rejects (FL1). The large-volume clause adopts the maintainer's rule whole with no threshold (I; FL2).
- The GitLab ground for a human gate is overstated: its post-deployment migrations run automatically daily at a release manager's discretion for work of about 10 minutes at most (G, fetched; FX2).
- Environment parity by axis: kind and version everywhere (G: Twelve-Factor "same type and version of each of the backing services"; lightweight stand-ins warned against); scale, data volume and permissions documented and routed (I). Not a compromise: the sources do not speak to the second axis. One strain: "schema" listed as unaffordable contradicts same-migrations-everywhere (FL3, I). Maintainer confirmation of F4 stays open (O).
- Rollback of data change: compatibility plus tested restore is the public position (G: Fowler and Sadalage, Flyway); the written reverse for every reversible-form change is a maintainer addition, so the Decision blends two positions (I; FL4).
- Judge flags: F2, F5, F6, F7, F8, F9, F10 agreed (G/I as the judge marks); F3 not settled in the Decision (FX1); F1, F4, F11, F12, F13 carried (O).
- Other clear defects: FX3 urgent-fix stream unconditional against its own Rejected line (G); FX4 run restriction stated in three places (G); FX5 pull-or-push condition without a row (G, the node admits it); FX6 roll-up flag lists inconsistent (G).
- No finding on author rules, missed positions, or consistency with settled records (G, checked rows and sources).

## L3 full

Pin: records reviewed: 42. Findings fix: 6. Findings flag: 9. Sources fetched: 7, confirmed: 6.

Scope and method. All 42 records of J6_change_flow were read against the maintainer decisions (MD-01 to MD-03), the target hierarchy, the skeleton branch records and the ledger rows named in each Grounds line. Eight checks applied to every record. A script compared the ledger ids of each skeleton node with the judged node: no row of the skeleton is absent from a judged node. The judge's 13 flags were assessed one by one. Consistency was checked with the settled RULES.1 to .5, CONTRACTS.1, DATA_INTEGRITY.1 to .5, SECURITY.6, AVAILABILITY.3 to .5, ARTIFACT.1 and .2, and with cross-unit fixes X1 to X3. The fetch tool summarises pages, so quotes are as returned by it, not read in the raw page.

Sources fetched (7) and what they confirmed:
1. DORA database change management (REG-245): confirmed "manage database changes in the same way you manage application changes: through an automated process that uses version control as its source of truth"; unique sequence numbers; DBAs consulted on proposed changes; visibility of pending changes; "100% of database changes are made in this way".
2. Twelve-Factor dev/prod parity (REG-103): confirmed the three gaps and "the same type and version of each of the backing services"; lightweight stand-ins cause "tiny incompatibilities".
3. GitLab migration style guide (REG-255): partial. Post-deployment migrations "executed on a daily basis at the discretion of release manager through the post-deploy migration pipeline", at most a few minutes of data work, about 10 minutes; reversibility required throughout. Does not support a named group triggering long or locking runs (FX2).
4. Fowler and Sadalage, Evolutionary Database Design (REG-244): confirmed smallest possible change, DBA pairing, separate folder for more frequently released data fixes; reverse migrations not "cost effective and beneficial enough to try all the time".
5. Fowler, Deployment Pipeline (REG-107): confirmed stages "can be automatic, or require human authorization to proceed"; says nothing on who triggers.
6. SRE Workbook, Canarying Releases (REG-104): confirmed before-and-after canary comparison is unreliable because time changes metrics; choose "the top few metrics ... perhaps no more than a dozen".
7. Flyway undo migrations (REG-251): confirmed undo "not so well for undoing data changes"; recommends backward compatibility plus "a proper, well tested, backup and restore strategy".
Confirmed in full: 6 (1, 2, 4, 5, 6, 7); partial: 1 (3). Not fetched: the other cited sources; their grounds stand as the judge wrote them.

Test of the two central calls against MD-01.
Database change by risk class. The judge's own question is the right one: which guarantee is needed. The guarantees are "what runs is what was reviewed" and "a risky change does not start unwatched". A criterion-based split delivers both and keeps automation where it is safe; that is a best-for-purpose argument, not an average (the average would be "manual for everything" or "automatic for everything with a small exception list" chosen by popularity). Three weak points remain. (a) The public authority (DORA) wants 100% of changes through the automated process; its human element is an authorization stage (Fowler), not a person triggering a run. The node says "triggering the run of the reviewed script with the tooling", which can mean a run outside the pipeline, contradicting "not a separate manual track" and the judge's own argument about paths nobody exercises (FL1). (b) SECURITY.6 is cited as requiring such a job to run from a reviewed script by a person; that clause governs a job an automated author executes, so it supports the gate only by extension. (c) The large-volume clause turns the split into the maintainer's rule without a threshold (FL2). If FL1 is resolved as a pipeline authorization stage, the split is the best practice the strongest sources establish and the maintainer's lane is one implementation of it; otherwise it is the maintainer's practice narrowed to a class, marked inferred.
Environment parity by axis. The two positions apply to different axes: Twelve-Factor fixes the kind and version of backing services and says nothing on data volume; the maintainer's rule concerns volume, permissions, missing schemas and performance. Keeping both is not blending. The judge marks the split inferred, correctly. Residuals: "schema" in the unaffordable list conflicts with same migrations everywhere (FL3); the written list of known differences is maintainer-only practice, inferred.

Judge flags. F1 (FL5), F4 (FL6), F11 (FL7), F12 (FL8), F13 (FL9) cannot be settled here and are carried. F2 agreed. F3 shows a real defect: the Decision omits it (FX1). F5 agreed: the narrowed idempotent-DDL rule serves the stated purpose and the maintainer's row records its internal tension. F6 agreed and FX5 removes the unsupported condition. F7, F8 agreed. F9 agreed: no source ranks merge methods, the default is inferred and marked so. F10 agreed.

Findings fix (6): FX1 DATA_CHANGE.3 decision on configuration-like content missing; FX2 DATA_CHANGE.3 GitLab ground overstated; FX3 DATA_CHANGE.1 urgent-fix stream unconditional against Rejected; FX4 REVIEW.1 run restriction restated, hold in DATA_CHANGE.3 and RELEASE.5; FX5 DEPLOY.4 context without a row; FX6 roll-up flag lists. Full lines in findings.md.
Findings flag (9): FL1 gate form for the risky class; FL2 large-volume clause; FL3 "schema" among unaffordable axes; FL4 written reverse for every reversible-form change; FL5 to FL9 carried judge flags. Full lines in findings.md.

No finding: author rules (check 5), missed positions (check 3), contradiction with settled records (check 7) other than the strain in FL1. Each Rejected position carries a condition or is explained as best never; two exceptions noted in FX3 and FL4. The judge's DEPLOY.3 and RELEASE.2 handle open positions (calendar versioning) as open, not rejected, which is acceptable.

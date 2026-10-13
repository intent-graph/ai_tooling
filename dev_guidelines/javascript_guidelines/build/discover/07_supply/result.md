# Discovery result: 07 SUPPLY (dependencies and supply chain)

## L1 headline

Authoritative coverage of the area is good and mostly current: npm CLI v12 docs, Node.js docs, OpenSSF, SLSA, OWASP and about ten peer-reviewed npm studies cover all seven sub-topics, but the T1 base is thin on typosquatting and on audit-tool limits, and evidence for update-delay ("cooldown") efficacy is vendor-only (certainty: grounded on what I fetched, inferred on tier proposals, which the auditor decides).

Pinned:
- Candidates by proposed tier: T1 20, T2 19, T3 3 (total 42; above the 15-35 aim because every row is admissible, none is padding; the auditor may trim).
- Sub-topics with no T1 candidate: none. T1 is thin (mention-level or limitation-only) for typosquatting, audit tooling limits, and update policy efficacy; the evidence there is T2 or T3.
- Failed fetches on a T1 candidate: none. Failed fetches on non-T1 candidates: the original dependency-confusion post (HTTP 403, T3, K42, no admissible copy found) and the publisher page of the trivial-packages paper (HTTP 403, T2, K33, only secondary listings read).

## L2 claims

Fetch method note: pages were fetched through a summarizing fetch tool, so author, date and covered topics are confirmed from the page, but wording is not verbatim. Stage 3 must read the sources in full.

Sub-topics (grounded unless marked):
- Dependency minimalism: T1 K15 (OpenSSF evaluation guide: every dependency widens attack surface), K13 (Node threat model: the runtime fully trusts installed npm code). T2 evidence K21 (few maintainers reach most packages), K33 (trivial packages; primary copy not fetched), K26 (least privilege per package). Has T1.
- Lockfiles and pinning: T1 K04, K05, K14, K18, K12. T2 K27 (design space), K28 (pinning study). Has T1. Authorities disagree (see below).
- Install scripts: T1 K06, K07, K08 (npm 12 blocks dependency lifecycle scripts, git and remote-URL dependencies by default), K12, K18. T2 K24 (install scripts as weak-link signal). Has T1. Currency risk: K12 and K18 predate or ignore the v12 default.
- Provenance and signatures: T1 K01, K02, K09, K16. T2 K34 (Sigstore design), K38 (GitHub changelog, facts only). Has T1.
- Typosquatting and name confusion: T1 K12, K15, K18, K11 (mention-level, or scope namespace facts). T2 K25 (13 confusion mechanisms, 1,200 incidents). T3 K42 (origin of dependency confusion, fetch failed). Has T1, thin; mechanism evidence is T2.
- Update policy (cadence, delay, automation): T1 K06 (min-release-age, allow-git, allowScripts config facts), K18, K12, K14. T2 K32 (why developers do not update). T3 K40 (Dependabot 3-day cooldown, vendor claim), K41 (pnpm). Has T1 for the mechanism; no T1 for whether delay works (inferred gap).
- Audit tooling limits: T1 K03 (states only that some fixes need manual work and results depend on the lockfile), K17 (Scorecard checks are GitHub-limited). T2 K29 (most package-level alerts are unreachable code), K30 (under 1% of installed dependencies reach production; most alerts hit non-production dependencies). Has T1, thin.
- Incident evidence (supports all): T1 K20 (advisory for debug 4.4.2). T2 K35 (event-stream), K36 (eslint-scope), K37 (Shai-Hulud, CISA), K22 and K31 (attack taxonomies and malicious-package review). Grounded.

Disagreements and tensions (each opens a stage-4 item):
- Pinning: K12, K14, K18 and K37 recommend pinning or lockfiles; K28 (FSE 2025) reports that pinning direct dependencies raises exposure to malicious updates in larger npm graphs. Both admissible; later stages need both.
- Shrinkwrap: K14 recommends publishing npm-shrinkwrap.json; K08 records npm 12 removing shrinkwrap support. Currency conflict (G2), not a true dispute.
- Install scripts: K12 tells users to opt out with ignore-scripts; K07 and K08 make blocking the default. K12 is superseded for npm 12 and later, still valid for older npm.
- Update speed: K32 and K18 favor prompt updates; K40 and K06 (min-release-age) favor delay. Resolution may be "delay version updates, not security fixes" (K40 says so; inferred for K06).
- Audit: K35 tells users to run npm audit; K29 and K30 show alert noise. Tension, not contradiction.

Gaps (open):
- No T1 document found that quantifies audit false positives, or that tests cooldown efficacy; both rest on T2 (K29, K30) or T3 (K40).
- Dependabot and Renovate product docs, Yarn and Bun lockfile or script docs, and the NSA/CISA/ODNI developer supply-chain guide (found by search, PDF not fetched) were not opened; Deno and Bun are named-only per plan.
- Version split: K03, K05 (npm v11.21, marked legacy by the site) were fetched; the v12 versions of those pages were not. K03 and K05 content may have changed.
- OpenSSF malicious-packages dataset (OSV format, active) was seen but not listed; the auditor may add it as dataset (T2, facts only).
- The venue of K26 (ICSE 2021) and K24 (ICSE-SEIP 2022) is confirmed by search results, not by the conference page; arXiv pages were fetched.

## L3 full

Fields per row: title; author or body; standing; url; fetched; date; kind; proposed tier; gates; covers; boundary. All fetches succeeded unless stated. Dates are page-stated.

### T1

- SUPPLY-K01: Generating provenance statements; npm CLI docs team; official npm documentation; https://docs.npmjs.com/generating-provenance-statements; fetched yes; last updated 2026-05-04; official-doc; T1; gates G1-G6 pass, G5 low risk (registry operator, facts about its own feature); covers provenance and signatures; states limitation that provenance does not prove code is safe; boundary none.
- SUPPLY-K02: Trusted publishing for npm packages; npm docs; official-doc; https://docs.npmjs.com/trusted-publishers; fetched yes; last updated 2026-10-06; T1; gates pass, G2 fast-moving page; covers provenance, publisher credentials (OIDC instead of long-lived tokens).
- SUPPLY-K03: npm audit command; npm docs; official-doc; https://docs.npmjs.com/cli/v11/commands/npm-audit; fetched yes; v11.21.0 (site marks legacy), edited 2026-03-18; T1; gates pass, G2 unsure (v12 page not read); covers audit tooling limits (submits dependency description to registry; some fixes manual), signature verification.
- SUPPLY-K04: npm ci; npm docs; official-doc; https://docs.npmjs.com/cli/v11/commands/npm-ci; fetched yes; v11.21.0 legacy; T1; gates pass, G2 unsure as K03; covers lockfiles (frozen install, errors on mismatch).
- SUPPLY-K05: package-lock.json; npm docs; official-doc; https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json; fetched yes; v11.21.0 legacy; T1; gates pass, G2 unsure as K03; covers lockfiles, integrity hashes; boundary none.
- SUPPLY-K06: npm config (v12); npm docs; official-doc; https://docs.npmjs.com/cli/v12/using-npm/config; fetched yes; v12 (current); T1; gates pass; covers install scripts (ignore-scripts, allow-scripts, allowScripts), update policy (min-release-age, before), allow-git default none.
- SUPPLY-K07: npm install-scripts command (v12.2.0); npm docs; official-doc; https://docs.npmjs.com/cli/v12/commands/npm-install-scripts/; fetched yes; v12.2.0; T1; gates pass; covers install scripts (approve, deny, pin-by-version policy).
- SUPPLY-K08: npm CLI v12.0.0 changelog; npm CLI team; official-doc; https://docs.npmjs.com/cli/v12/using-npm/changelog/; fetched yes; 2026-07-08; T1; gates pass; covers install scripts, git and remote dependencies blocked by default, shrinkwrap removal.
- SUPPLY-K09: ECDSA registry signatures; npm docs; official-doc; https://docs.npmjs.com/about-registry-signatures; fetched yes; edited 2024-04-09; T1; gates pass; covers provenance and signatures (tamper detection against mirrors and proxies).
- SUPPLY-K10: About access tokens; npm docs; official-doc; https://docs.npmjs.com/about-access-tokens; fetched yes; page states Nov 2025 legacy-token end and Jan 2027 deprecation of direct publishing with 2FA-bypass tokens; T1; gates pass; covers publisher side update/publish controls; boundary: partly publishing, not consuming.
- SUPPLY-K11: About scopes; npm docs; official-doc; https://docs.npmjs.com/about-scopes; fetched yes; updated 2023-10-23; T1; gates pass; covers name confusion (namespaces).
- SUPPLY-K12: Node.js Security Best Practices, malicious third-party modules; OpenJS Foundation and Node.js contributors; official-doc; https://nodejs.org/en/learn/getting-started/security-best-practices; fetched yes; date not stated; T1, expect-restricted: one bullet names a commercial scanner (G5), and ignore-scripts advice predates npm 12 (G2); covers install scripts, lockfiles, pinning, npm ci, typosquatting, dependency confusion, cooldown.
- SUPPLY-K13: Node.js threat model (SECURITY.md); Node.js project; official-doc; https://github.com/nodejs/node/blob/main/SECURITY.md; fetched yes; main branch, date not stated; T1; gates pass; covers minimalism (runtime trusts all installed code); boundary: RUNSEC (06).
- SUPPLY-K14: npm best practices guide v1.1; OpenSSF Best Practices WG; https://github.com/ossf/package-manager-best-practices/blob/main/published/npm.md; fetched yes; repo archived, last update 2023-10-09; T1, expect-restricted: archived, predates npm 12 (shrinkwrap advice), no provenance section; covers lockfiles, scopes, Dependabot or Renovate, npm audit; G2 unsure.
- SUPPLY-K15: Concise Guide for Evaluating Open Source Software; OpenSSF Best Practices WG; https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software; fetched yes; 2025-03-28, updated 2025-04-23; T1; gates pass; covers minimalism, typosquatting, maintenance checks.
- SUPPLY-K16: SLSA specification v1.2; Linux Foundation, OpenSSF project; spec; https://slsa.dev/spec/v1.2/; fetched yes; v1.2 approved (v1.1 retired); T1; gates pass; covers provenance (Build and Source tracks); boundary: web_architecture_guidelines (build pipeline).
- SUPPLY-K17: OpenSSF Scorecard checks; OpenSSF; https://github.com/ossf/scorecard/blob/main/docs/checks.md; fetched yes; main branch; T1; gates pass; covers dependency selection checks (Pinned-Dependencies, Dependency-Update-Tool, Signed-Releases, Vulnerabilities), limitation: many checks GitHub-only, false negatives.
- SUPPLY-K18: OWASP NPM Security Cheat Sheet; OWASP Cheat Sheet Series; https://cheatsheetseries.owasp.org/cheatsheets/NPM_Security_Cheat_Sheet.html; fetched yes; date not stated; T1; gates pass (G2 unsure: check 13 items against npm 12); covers lockfile, ignore scripts, health assessment, audit, 2FA, tokens, typosquatting and slopsquatting, trusted publishers, dependency confusion.
- SUPPLY-K19: OWASP Software Supply Chain Security Cheat Sheet; OWASP; https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html; fetched yes; date not stated; T1; gates pass; covers SBOM, pinning, supplier assessment, tooling limits; boundary: sibling guideline for CI.
- SUPPLY-K20: GHSA-4x49-vf9v-38px / CVE-2025-59144, debug@4.4.2 malware; GitHub Security Advisory; advisory; https://github.com/advisories/GHSA-4x49-vf9v-38px; fetched yes; published 2025-09-15; T1 (advisory record as fact); gates pass; covers incident facts (account takeover by phishing 2025-09-08, browser-only payload).

### T2

- SUPPLY-K21: Small World with High Risks: A Study of Security Threats in the npm Ecosystem; Zimmermann, Staicu, Tenny, Pradel; first-author TU Darmstadt, USENIX Security 2019; https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman; fetched yes; 2019-08; paper; T2; gates pass, G2 unsure (2019 data); covers minimalism (maintainer concentration, unmaintained dependencies).
- SUPPLY-K22: Taxonomy of Attacks on Open-Source Software Supply Chains; Ladisa, Plate, Martinez, Barais; IEEE S&P 2023; https://arxiv.org/abs/2204.04008 (venue stated on page); fetched yes; 2022 preprint, 2023 proceedings; paper; T2; gates pass; covers attack vectors (107) mapped to 33 safeguards; all sub-topics.
- SUPPLY-K23: Towards Measuring Supply Chain Attacks on Package Managers for Interpreted Languages; Duan et al.; NDSS 2021; https://ndss-symposium.org/ndss-paper/towards-measuring-supply-chain-attacks-on-package-managers-for-interpreted-languages; fetched yes; 2021; paper; T2; gates pass; covers malicious packages (339 found, 278 confirmed), registry feature comparison.
- SUPPLY-K24: What are Weak Links in the npm Supply Chain?; Zahan, Zimmermann, Godefroid, Murphy, Maddila, Williams; ICSE-SEIP 2022 (venue by search only, arXiv page fetched); https://arxiv.org/abs/2112.10165; fetched yes; 2021-12, rev. 2022-02; paper; T2; gates pass; covers install scripts as signal, expired maintainer domains.
- SUPPLY-K25: Beyond Typosquatting: An In-depth Look at Package Confusion; Neupane, Holmes, Wyss, Davidson, De Carli; USENIX Security 2023; https://www.usenix.org/conference/usenixsecurity23/presentation/neupane; fetched yes; 2023-08; paper; T2; gates pass; covers typosquatting (13 mechanisms, 1,200+ incidents).
- SUPPLY-K26: Containing Malicious Package Updates in npm with a Lightweight Permission System; Ferreira, Jia, Sunshine, Kästner; ICSE 2021 (venue by search only); https://arxiv.org/abs/2103.05769; fetched yes; 2021-03; paper; T2; gates pass; covers minimalism and least privilege per package (31.9% protectable per search snippet, not checked in full).
- SUPPLY-K27: The Design Space of Lockfiles Across Package Managers; Gamage, Tiwari, Monperrus, Baudry; Empirical Software Engineering 2026 (as stated on page); https://arxiv.org/abs/2505.04834; fetched yes; v. 2025-10-27; paper; T2; gates pass; covers lockfiles (7 managers, 15 interviews).
- SUPPLY-K28: Pinning Is Futile: You Need More Than Local Dependency Versioning to Defend against Supply Chain Attacks; He, Vasilescu, Kästner; PACMSE (FSE) 2025; https://arxiv.org/abs/2502.06662; fetched yes; 2025-02; paper; T2; gates pass; covers pinning and update policy; opposes simple pinning advice; boundary none.
- SUPPLY-K29: From Noise to Signal: Precisely Identify Affected Packages of Known Vulnerabilities in npm Ecosystem; Pu, Ying, Gu; NDSS 2026; https://www.ndss-symposium.org/ndss-paper/from-noise-to-signal-precisely-identify-affected-packages-of-known-vulnerabilities-in-npm-ecosystem/; fetched yes; 2026; paper; T2; gates pass, G5 note: authors from a security vendor institute, claims are measurement-based; covers audit tooling limits (npm audit false positives reduced 94% by function-level analysis; 68% figure from search snippet, verify in full).
- SUPPLY-K30: Not All Dependencies are Equal: An Empirical Study on Production Dependencies in NPM; Latendresse, Mujahid, Costa, Shihab; ASE 2022; https://arxiv.org/abs/2207.14711; fetched yes; 2022-08; paper; T2; gates pass; covers audit tooling limits and prioritization.
- SUPPLY-K31: Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks; Ohm, Plate, Sykosch, Meier; DIMVA 2020; https://arxiv.org/abs/2005.09535; fetched yes; 2020-05; paper; T2; gates pass; covers 174 malicious packages (npm, PyPI, RubyGems), attack trees.
- SUPPLY-K32: A Qualitative Study of Dependency Management and Its Security Implications; Pashchenko, Vu, Massacci; ACM CCS 2020; https://research.vu.nl/en/publications/a-qualitative-study-of-dependency-management-and-its-security-imp/; fetched yes; 2020-10-30; paper; T2; gates pass; covers update policy (25 interviews, why updates stall).
- SUPPLY-K33: Why Do Developers Use Trivial Packages? An Empirical Case Study on npm; Abdalkareem, Nourry, Wehaibi, Mujahid, Shihab; ESEC/FSE 2017; https://dl.acm.org/doi/10.1145/3106237.3106267; fetched failed (HTTP 403 from the publisher; doi.org redirects there); alternative copy: only secondary listings read (not admissible), no preprint found; 2017; paper; T2; gates G2 unsure (2017), G4 unverified; covers minimalism. Auditor: reject unless a primary copy is obtained.
- SUPPLY-K34: Sigstore: Software Signing for Everybody; Newman, Meyers, Torres-Arias; ACM CCS 2022; https://par.nsf.gov/biblio/10470793; fetched yes; 2022-11-07; paper; T2; gates pass; covers provenance and signatures (design basis of npm provenance).
- SUPPLY-K35: Details about the event-stream incident; Adam Baldwin, npm security; https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident; fetched yes; 2018-11-27; maintainer-writing (incident report); T2, expect-restricted: incident facts only; gates G2 unsure (2018), remedies superseded; covers incident (social-engineered maintainer takeover).
- SUPPLY-K36: Postmortem for Malicious Packages Published on July 12th, 2018; ESLint team (author "Henry"); https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes; fetched yes; 2018-07; maintainer-writing; T2, expect-restricted: incident facts; covers incident (reused password, no 2FA, postinstall token theft); G2 unsure.
- SUPPLY-K37: Widespread Supply Chain Compromise Impacting npm Ecosystem; CISA; https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem; fetched yes; 2025-09-23; advisory; T2 (government agency; policy has no tier for it); gates pass; covers incident (Shai-Hulud, 500+ packages), response measures.
- SUPPLY-K38: npm install-time security and GAT bypass2fa deprecation; GitHub changelog (npm team); https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/; fetched yes; 2026-07-08; official-doc (announcement); T2, expect-restricted: facts about npm behavior and dates only (G5, GitHub operates npm); covers install scripts defaults, token changes. Related: 2026-06-09 changelog "Upcoming breaking changes for npm v12" (fetched, not listed separately).
- SUPPLY-K39: Our plan for a more secure npm supply chain; Xavier René-Corail, GitHub Security Research; https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/; fetched yes; 2025-09-22; research-blog; T2, expect-restricted: registry policy facts only (G5); covers response to Shai-Hulud (token lifetimes, trusted publishing).

### T3

- SUPPLY-K40: The case for a cooldown: why Dependabot now waits before issuing version updates; Carlin Cherry, GitHub product manager; https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/; fetched yes; 2026-07-23; research-blog; T3, expect-restricted: facts only (G5, vendor describing its own feature); gates G3 partial (cites incident durations, no study); covers update policy, cooldown rationale.
- SUPPLY-K41: Supply chain attack mitigation in pnpm (and install-script settings); pnpm maintainers; https://pnpm.io/supply-chain-security and https://pnpm.io/settings/build; fetched yes (both); pnpm v10+; official-doc (maintainer documentation of a concerned tool); T3; gates pass for facts about pnpm; covers install scripts (blocked by default since v10), minimumReleaseAge default 24 hours, trustPolicy; boundary: tool choice belongs to 08 QUALITY/tooling, listed here once.
- SUPPLY-K42: Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies; Alex Birsan (security researcher); https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610; fetched failed (HTTP 403); no admissible alternate copy found (only press coverage, not admitted); published 2021-02-09 per press; research-blog; T3; gates G1 pass (named author, origin of the attack class), G4 origin; covers typosquatting and name confusion. Auditor: admit only if a primary copy is obtained; K11 and K18 cover mitigations.

ID note: in L2 the ids refer to this table; the table order is authoritative where a one-line gloss differs from the row.

### Dismissed on sight (approximate counts from search-result titles)

- Security-vendor blogs and advisories (Socket, Snyk, Semgrep, Endor Labs, ReversingLabs, Sonatype, Checkmarx, Anchore, Codacy, Corgea, NodeSource, JFrog, Datadog): about 16. Their incident write-ups were replaced by origin records (K20, K35, K36, K37, K39).
- News and trade press (SD Times, heise, BleepingComputer, SecurityWeek, The Hacker News, TechRadar, Dark Reading, CSO, TechTarget, BGR, Gizmodo, others): about 20.
- Personal or unattributed blogs, gists and aggregators on min-release-age, install scripts, lockfiles: about 12.
- Community or listicle repositories (npm security best-practices lists by individuals): 2.
- Paper mirrors and indexers when an origin existed (alphaxiv, deepai, ar5iv, secrss, gitea): about 12.
- Wikipedia: 2; dev.to: 2; government-contractor or lesson pages restating others: 3.

### Searches run

- OpenSSF npm best practices guide dependency management supply chain security
- npm min-release-age config docs
- GitHub blog plan for a more secure npm supply chain Shai-Hulud trusted publishing
- Zimmermann Small World with High Risks; Ladisa taxonomy; Duan NDSS 2021
- Zahan weak links; Ferreira permission system; Pashchenko dependency management; Abdalkareem trivial packages
- typosquatting npm Neupane; lockfiles empirical study; npm audit false positives reachability
- Wermke Committed to Trust (found, not listed: maintainer practices, marginal)
- event-stream incident / ESLint eslint-scope postmortem
- GitHub advisory chalk debug compromise September 2025
- CISA Shai-Hulud npm alert; left-pad incident (found, not listed: 2016, policy since changed)
- npm install scripts ignore-scripts pnpm; npm v12 install scripts default; github.blog changelog npm v12
- Sejfia Amalfi; Ohm Backstabber's Knife; Alfadel Dependabot (found, not listed: weak fetch, marginal); Decan dependency networks (dropped: covered by K21)
- dependency cooldown Dependabot; Birsan dependency confusion; NSA CISA ODNI developer guide (found, not fetched); Sigstore CCS 2022; Pashchenko CCS 2020 pdf
- Fetch-only checks: OWASP NPM and supply-chain cheat sheets, OWASP Top 10 A03 2025 (fetched, not listed: not in the T1 list, overlaps K18 and K19), npm docs pages K01 to K11, GitHub changelog 2026-06-09 and GitHub blog 2026-07-28 (fetched, dropped as restatements of K38 and K40), OpenSSF malicious-packages repository (seen, not listed).

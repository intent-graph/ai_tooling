# 02_adoption (ADOPT) — research result

## L1 headline

Best practice on adopting and living with dependencies is firm on the mechanics (declare, lock, hash-verify, inventory, patch known vulnerabilities, never trust a version number alone) and genuinely split on four policy choices (build vs reuse vs rent, exact pins vs ranges, update fast vs delay, wrap vs accept lock-in); certainty is high on mechanics (grounded in T1 docs) and moderate on the policy splits (positions grounded, "when it wins" partly inferred).

Pinned:
- Sources by tier: 18 T1, 7 T2, 4 T3, 0 T4 (29 total).
- Claims: 51.
- Contested topics: build vs reuse vs rent; exact pins vs ranges; update fast vs update delayed (cooldown); live at head vs pinned versions; wrap dependencies vs accept lock-in; vendor/mirror vs registry plus lockfile; trust in SemVer numbers.
- Failed T1 fetches: EUR-Lex text of the Cyber Resilience Act (Regulation 2024/2847) returned empty, so the CRA is recorded from a non-official annotated copy (S25, tiered T3, certainty lowered); the NIST SP 800-218 landing page was abstract-only and the PDF could not be parsed by the fetcher, so the PDF was downloaded and read as extracted text (S05: only the PW.4 rows were inspected).

## L2 claims

Clusters
1. Adopt, build or rent is a recorded decision, with a cost-of-ownership test: a dependency is a liability that outlives the day it saves; reuse is the default for non-core, building for core or tiny needs, renting needs an exit plan. Agreement: majority (contested at the margin). Certainty: grounded. C01-C07.
2. Evaluate before adopting: necessity, maintainer health, security posture, tests, licence, transitive reach, authenticity of source. Agreement: consensus. Certainty: grounded. C08-C12 (boundary: SRC, kept minimal).
3. Declare everything, lock the resolved tree, commit the lockfile, verify by hash. Agreement: consensus. Certainty: grounded. C13-C18.
4. Pin exactly for deployables, range for libraries; locks complement, not replace, constraints. Agreement: majority. Certainty: grounded. C19-C21.
5. Update policy: continuous small updates, vulnerabilities urgently, automated by a tool, with a deliberate delay for non-security updates as a supply-chain defence. Agreement: contested (speed vs delay). Certainty: grounded for each position, win conditions inferred. C22-C28.
6. Never trust a version number alone: SemVer is an estimate, Hyrum's Law holds, tests are the evidence. Agreement: majority. Certainty: grounded. C29-C31.
7. Supply-chain integrity of what is consumed: trusted sources, provenance, signed artifacts, malware scan, recursive application, rebuild for the highest tier. Agreement: consensus on direction, tiered on depth. Certainty: grounded. C32-C36.
8. Inventory and continuous monitoring: SBOM, transitive coverage, known-vulnerability feeds, end-of-life tracking with a plan. Agreement: consensus. Certainty: grounded. C37-C39.
9. Contain the dependency: thin wrapper at the boundary, isolate or sandbox, copy tiny pieces, fork or vendor as last resort; against it, wrapping has its own cost. Agreement: contested. Certainty: grounded. C40-C44.
10. Lock-in is a spectrum to be priced, not eliminated: accept it for commensurate pay-off, avoid it only where switching probability times cost justifies. Agreement: majority. Certainty: grounded. C45-C47.
11. Availability and exit: mirror or vendor to survive upstream removal; plan for unmaintained components; give back fixes. Agreement: majority. Certainty: grounded. C48-C50 (C50 inferred, no direct source).
12. Regulation makes third-party due diligence a legal duty in some contexts. Agreement: consensus where it applies. Certainty: grounded in a secondary copy only. C51.

Live debates (forces in tension)
- Build vs reuse vs rent: cost of ownership and delivery speed vs control and exit risk.
- Exact pins vs ranges: reproducibility and confidence vs duplicate dependencies and consumer friction (apps vs libraries).
- Update fast vs delay (cooldown): window of known-vulnerability exposure vs window of malicious-release exposure; security fixes bypass the delay in tooling.
- Live at head vs pinned: feedback speed and shared upgrade cost vs control; needs visibility of dependents and compute, unproven in open source.
- Wrap vs accept lock-in: reversibility and exit risk vs cost of ownership and cognitive load (extra layer, lowest-common-denominator API).
- Vendor/mirror vs registry plus lockfile: availability and control vs cost of ownership (diff noise, storage, update lag).
- SemVer trust: delivery speed (cheap range updates) vs correctness (numbers are human estimates).

Candidate central decisions of the area (other areas depend on them)
- D1 Default stance and per-case rule for adopt / build / rent, and where each is recorded.
- D2 Pin policy per artifact kind (deployable vs library) and the lockfile contract (committed, hash-verified, CI installs from lock only).
- D3 Update cadence and delay policy, with the explicit exception path for security fixes.
- D4 Trust boundary for consumption: allowed sources, mirror or not, provenance and malware checks, rebuild or not.
- D5 Containment rule: when a wrapper or adapter is mandatory (high lock-in, high replacement probability, security-sensitive).
- D6 Inventory contract: SBOM produced and where, transitive coverage, who watches the feeds.
- D7 Exit and end-of-life rule for each critical dependency or rented service.

Not covered
- Discovery and health signals in depth (slot SRC); only the adoption-time checklist is recorded.
- Licence compliance detail (copyleft, obligations); only mentioned.
- Rented-service specifics (SLAs, data portability law, pricing risk, API deprecation policies); evidence is thin, see gaps.
- Secrets, build-pipeline hardening, signing key management (slot TRANS and DELIVER).
- Ecosystem-specific tooling beyond examples (Maven, Cargo features, system packages, containers base images).
- Empirical studies on update lag and breakage rates (no peer-reviewed study read).

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| ADOPT-S01 | T2 | Software Engineering at Google, ch. 21 Dependency Management | Winters, Manshreck, Wright | https://abseil.io/resources/swe-book/html/ch21.html | cost of dependency, SemVer limits, Hyrum's Law, MVS, live at head, vendoring |
| ADOPT-S02 | T3 | Our Software Dependency Problem | Russ Cox | https://research.swtch.com/deps | pre-adoption checks, options to reduce dependency risk |
| ADOPT-S03 | T1 | SLSA v1.0 threats overview | OpenSSF SLSA | https://slsa.dev/spec/v1.0/threats-overview | compromised or unavailable dependency threats |
| ADOPT-S04 | T1 | SLSA v1.0 about | OpenSSF SLSA | https://slsa.dev/spec/v1.0/about | scope: SLSA level independent of dependencies' levels |
| ADOPT-S05 | T1 | NIST SP 800-218 SSDF v1.1 | NIST | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf | PW.4 reuse and verify third-party components |
| ADOPT-S06 | T2 | The Twelve-Factor App, II Dependencies | Wiggins / Heroku | https://12factor.net/dependencies | explicit declaration plus isolation |
| ADOPT-S07 | T1 | OpenSSF Scorecard checks | OpenSSF | https://github.com/ossf/scorecard/blob/main/docs/checks.md | pinned dependencies, update tool, vulnerabilities, maintained, signed releases |
| ADOPT-S08 | T1 | Concise Guide for Evaluating Open Source Software | OpenSSF Best Practices WG | https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software | adoption-time evaluation |
| ADOPT-S09 | T1 | OWASP Dependency-Check | OWASP | https://owasp.org/www-project-dependency-check/ | software composition analysis |
| ADOPT-S10 | T1 | OWASP Top 10:2025 A03 Software Supply Chain Failures | OWASP | https://top10.owasp.org/2025/A03_2025-Software_Supply_Chain_Failures/ | prevention list for supply chain failures |
| ADOPT-S11 | T2 | Don't get locked up into avoiding lock-in | Gregor Hohpe, martinfowler.com | https://martinfowler.com/articles/oss-lockin.html | lock-in as spectrum, cost model |
| ADOPT-S12 | T2 | In Defense of Not-Invented-Here Syndrome | Joel Spolsky | https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/ | build-own for core functions |
| ADOPT-S13 | T1 | Renovate docs, Dependency Pinning | Renovate maintainers | https://docs.renovatebot.com/dependency-pinning/ | pin apps, range libraries, lockfile limits |
| ADOPT-S14 | T1 | Dependabot options reference | GitHub | https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference | cooldown and groups |
| ADOPT-S15 | T1 | Semantic Versioning 2.0.0 | semver.org | https://semver.org/ | what SemVer promises |
| ADOPT-S16 | T1 | npm package-lock.json | npm | https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json | lockfile purpose, commit, integrity |
| ADOPT-S17 | T1 | pip Secure installs | PyPA | https://pip.pypa.io/en/stable/topics/secure-installs/ | hash-checking mode |
| ADOPT-S18 | T2 | Strangler Fig Application | Martin Fowler | https://martinfowler.com/bliki/StranglerFigApplication.html | incremental replacement vs rewrite |
| ADOPT-S19 | T2 | Yagni | Martin Fowler | https://martinfowler.com/bliki/Yagni.html | costs of building what is not needed |
| ADOPT-S20 | T1 | Secure Supply Chain Consumption Framework (S2C2F) | OpenSSF | https://github.com/ossf/s2c2f/blob/main/specification/framework.md | consumption practices and maturity levels |
| ADOPT-S21 | T3 | We should all be using dependency cooldowns | William Woodruff | https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns | cooldown argument and data |
| ADOPT-S22 | T1 | Go Modules Reference | Go project | https://go.dev/ref/mod | MVS, go.sum, proxy immutability, vendoring |
| ADOPT-S23 | T1 | cargo-vet book | Mozilla | https://mozilla.github.io/cargo-vet/ | shared audits of dependencies |
| ADOPT-S24 | T2 | Hexagonal Architecture | Alistair Cockburn | https://alistair.cockburn.us/hexagonal-architecture/ | isolating the application from external technology |
| ADOPT-S25 | T3 (T1 content, unofficial copy) | Cyber Resilience Act, Art. 13 as annotated | cyberresilienceact.eu | https://www.cyberresilienceact.eu/the-cyber-resilience-act/ | due diligence on third-party components (EUR-Lex fetch failed) |
| ADOPT-S26 | T1 | Reproducible Builds, Definition | reproducible-builds.org | https://reproducible-builds.org/docs/definition/ | verifying binaries against source |
| ADOPT-S27 | T1 | SBOM | CISA | https://www.cisa.gov/sbom | SBOM definition and use |
| ADOPT-S28 | T3 | Choose Boring Technology | Dan McKinley | https://mcfunley.com/choose-boring-technology | cost of each new technology |
| ADOPT-S29 | T1 | Renovate, Minimum Release Age | Renovate maintainers | https://docs.renovatebot.com/key-concepts/minimum-release-age/ | delay of updates, security bypass |

### Claims

Each claim: id; claim; level; stack; sources; agreement; positions (if not consensus); certainty.

**Cluster 1: adopt, build, rent**

ADOPT-C01. Treat every dependency as an ongoing liability (maintenance, upgrade, security, platform shifts), not a one-time saving; decide to adopt only after weighing that cost. Level: principle. Stack: neutral. Sources: S01 "Importing vs. Forking", "Cost of Dependency"; S08 "Initial Assessment" (every new dependency increases attack surface); S02 "Costs & Risk". Agreement: consensus. Certainty: grounded.

ADOPT-C02. Prefer reusing existing, well-vetted components over duplicating functionality, especially for security-critical functions such as cryptography. Level: principle. Stack: neutral. Sources: S05 PW.4 ("Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality"). Agreement: majority. Positions: (a) reuse by default: forces cost of ownership, correctness, security; wins when function is non-core, well-understood, widely used (S05). (b) build own when it is a core business function: force control, differentiation, quality; wins when the function carries competitive advantage (S12 "If it's a core business function — do it yourself"). (c) copy or rewrite when only a tiny part is needed: force exit risk and attack surface; wins when the used surface is small ("a little copying is better than a little dependency", S02 "Avoid or Reduce"). Certainty: grounded.

ADOPT-C03. Build in-house only what third-party components cannot better meet, and then maintain it under the same secure-development process as acquired code. Level: practice. Stack: neutral. Sources: S05 PW.4.2. Agreement: consensus. Certainty: grounded.

ADOPT-C04. Do not build speculative functionality; building, delaying other work, carrying complexity and repairing wrong guesses are four distinct costs. Applies to writing a substitute "in case" as much as to features. Level: principle. Stack: neutral. Sources: S19 (four costs). Agreement: consensus. Certainty: grounded for the Yagni costs; the application to dependency substitution is inferred (S19, S11).

ADOPT-C05. Treat each new technology (language, datastore, service) as spending a scarce budget; prefer the technology the team already operates unless the existing one demonstrably cannot solve the problem. Level: decision. Stack: neutral. Sources: S28. Agreement: majority. Positions: boring-by-default (S28; forces team cognitive load, cost of ownership; wins for small teams, long-lived systems); adopt new where the need is real and an exit/migration plan exists (S28 itself admits). Certainty: grounded (T3 source, one voice; mark majority as inferred from S01 and S05 aligning on cost).

ADOPT-C06. When the work is replacing an adopted or home-grown component, replace incrementally behind the existing interface instead of rewriting wholesale. Level: practice. Stack: neutral. Sources: S18. Agreement: majority. Positions: incremental (S18; force reversibility, delivery speed; wins when behaviour is poorly specified and users cannot wait); big-bang rewrite (no source argued for it here; open). Certainty: grounded.

ADOPT-C07. Renting a service (SaaS, hosted API) is an adoption decision with the same cost test plus a control cost: for a core function the loss of control may not be acceptable. Level: decision. Stack: neutral. Sources: S12 (outsourcing core functions loses control); S11 ("accept some lock-in if commensurate pay-off"). Agreement: contested. Positions: rent non-core, build or keep control for core (S12; force control, differentiation); rent broadly and accept lock-in where pay-off is commensurate (S11; force delivery speed, cost of ownership). Certainty: inferred (S12 and S11 do not address SaaS directly beyond outsourcing; see gaps).

**Cluster 2: evaluate before adopting** (boundary: SRC)

ADOPT-C08. Before adopting, first ask whether the dependency is needed at all. Level: principle. Stack: neutral. Sources: S08 "Initial Assessment"; S02 "Avoid or Reduce". Agreement: consensus. Certainty: grounded.

ADOPT-C09. Verify authenticity of the component: that it comes from the authorised source, not a fork or look-alike, and obtain it over secure links from official sources. Level: practice. Stack: neutral. Sources: S08 "Initial Assessment"; S10 prevention list ("Only obtain components from official (trusted) sources over secure links"). Agreement: consensus. Certainty: grounded.

ADOPT-C10. Evaluate maintenance and sustainability: recent activity within 12 months and more than one maintainer, ideally from different organisations. Level: practice. Stack: neutral. Sources: S08 "Maintenance & Sustainability"; S07 Maintained, Contributors; S02 Maintenance. Agreement: consensus. Certainty: grounded.

ADOPT-C11. Evaluate the component in the context of its intended use and re-evaluate when that use changes substantially; require tests that run and pass, clear API documentation, secure defaults, and a licence compatible with yours. Level: practice. Stack: neutral. Sources: S05 PW.4.1 Example 1; S02 Design, Testing, Licensing; S08 "Usability & Security", "Adoption & Licensing". Agreement: consensus. Certainty: grounded.

ADOPT-C12. Judge risk as the sum over bad outcomes of cost times probability, so the same dependency can be acceptable in a hobby project and unacceptable in production; scale the rigour of vetting to criticality. Level: principle. Stack: neutral. Sources: S02 "Costs & Risk Calculation"; S25 (level of due diligence informed by risk). Agreement: consensus. Certainty: grounded.

**Cluster 3: declare, lock, verify**

ADOPT-C13. Declare all dependencies explicitly in a manifest and run in an isolated environment; never rely on implicit system-wide packages. Level: principle. Stack: neutral. Sources: S06. Agreement: consensus. Certainty: grounded.

ADOPT-C14. Commit a lockfile that records the exact resolved tree (direct and transitive) so teammates, CI and deployment install identical dependencies regardless of newer releases. Level: practice. Stack: neutral (npm, Cargo, Go go.sum, pip hashes as realisations). Sources: S16 "Why lock files exist", "Committing"; S22 go.sum, build list does not change when new versions appear. Agreement: consensus. Certainty: grounded.

ADOPT-C15. Install in CI and production from the lock only (fail if the lock and manifest disagree); an out-of-sync lock gives no guarantee. Level: practice. Stack: npm `npm ci`, generalises. Sources: S13 ("If a lock file gets out of sync... can no longer be guaranteed"); S16 (npm ci designed to install lock versions; not detailed in the section read). Agreement: consensus. Certainty: grounded for the guarantee; the generalisation is inferred.

ADOPT-C16. Verify downloaded artifacts by cryptographic hash recorded in the lock; where the tool supports a require-hashes mode, enable it for deploys. Level: practice. Stack: pip `--require-hashes`, npm integrity, Go checksum database. Sources: S17; S16 integrity field; S22 go.sum and sum.golang.org. Agreement: consensus. Certainty: grounded.

ADOPT-C17. Prefer a resolution rule that keeps builds close to what the author tested, such as minimal version selection, which does not change when new releases appear. Level: decision. Stack: Go (MVS), contrasts with newest-compatible resolvers. Sources: S01 "Minimum Version Selection"; S22. Agreement: contested. Positions: MVS (S01, S22; force correctness, confidence; wins when reproducibility matters more than automatic fixes, since upgrades become explicit); newest-compatible resolution plus lock (S13, S16; force delivery speed; wins when a tool updates the lock automatically). Certainty: grounded.

ADOPT-C18. Make builds reproducible, so any party can verify by bit-identical rebuild that a binary corresponds to its source. Level: practice. Stack: neutral. Sources: S26. Agreement: majority (adopted at the highest tier only, S20 Rebuild It). Positions: reproducible rebuild (S26; force security, control; wins for high-assurance or widely distributed artifacts, costs build discipline); trust signed provenance without rebuild (S04; force cost of ownership; wins for most teams). Certainty: grounded. boundary: DELIVER.

**Cluster 4: pin policy**

ADOPT-C19. Pin all dependency types exactly in applications and services that nobody else installs; a faulty release then shows as a reviewable change instead of a production surprise. Level: decision. Stack: neutral (examples npm). Sources: S13 "For Applications"; S07 Pinned-Dependencies (pinning mitigates compromised versions). Agreement: majority. Positions: exact pins plus update bot (S13, S07; force confidence, security; wins for deployables); ranges plus lockfile only (S16; force low noise; wins when review capacity is scarce, but a lock only delays a bad range, S13). Certainty: grounded.

ADOPT-C20. Libraries consumed by others should declare ranges, not exact pins, to avoid forcing duplicates and conflicts on consumers; the library's own CI should test the range edges. Level: practice. Stack: neutral. Sources: S13 "For Libraries"; S01 diamond dependency. Agreement: majority. Positions: ranges for libraries (S13; force consumer cognitive load, correctness of the shared graph); exact pins in libraries (no source defends it; open). The "test range edges" half is inferred from S13 and S01. Certainty: grounded / inferred as stated.

ADOPT-C21. A lockfile does not replace constraints: the manifest range must still exclude known-broken versions, because the lock only delays the problem. Level: principle. Stack: neutral. Sources: S13. Agreement: consensus. Certainty: grounded.

**Cluster 5: update policy**

ADOPT-C22. Keep dependencies current with small, frequent, automated updates instead of rare large jumps; small steps are safer and keep the cost of upgrade predictable. Level: decision. Stack: neutral. Sources: S02 "Upgrade Strategically"; S07 Dependency-Update-Tool (High risk if absent); S20 "Update It"; S01 hidden costs of dormant dependencies. Agreement: majority. Positions: update continuously (S02, S07, S20; force security, cost of ownership; wins when tests are trustworthy); upgrade only when there is need (S10 "Deliberately choose which version... upgrade only when there is need"; force control, stability; wins when verification is weak or deployments are costly and risk of change exceeds exposure). Certainty: grounded.

ADOPT-C23. Apply fixes for known vulnerabilities urgently, bypassing any scheduled delay. Level: principle. Stack: neutral. Sources: S02 ("every day you wait is another day..."); S07 Vulnerabilities ("should be fixed immediately"); S20 "Update It", "Fix It" (within 3 days at the top tier); S29 and S14 (security updates bypass or are excluded from delay). Agreement: consensus. Certainty: grounded.

ADOPT-C24. For routine (non-security) updates, a deliberate release-age delay (cooldown) of days to two weeks reduces exposure to malicious releases, because most observed attacks were detected within a week. Level: decision. Stack: neutral; tools Dependabot cooldown, Renovate minimumReleaseAge, pnpm minimumReleaseAge, uv exclude-newer. Sources: S21 (8 of 10 attacks under one week; 14 days stops all but xz-utils); S29 ("reduce risk supply chain security risks"); S14 cooldown options. Agreement: contested. Positions: cooldown (S21, S29; force security; costs staleness of fixes that ship as ordinary releases; wins when exposure to supply-chain attack outweighs staleness, i.e. most deployables); update immediately (S20 "Deploy updated external artifacts soon after an update becomes publicly available"; force security via speed to patch; wins when most updates are security fixes or when the pipeline detects malicious content itself). Note the data in S21 is one author's analysis of 10 attacks (T3). Certainty: grounded as to positions; the context-of-win is inferred.

ADOPT-C25. Automate update proposals with a tool and group related updates to limit noise; pinning raises PR volume and should be mitigated by scheduling, automerge of safe packages and grouping, not by abandoning pinning. Level: practice. Stack: neutral (Dependabot, Renovate). Sources: S13 "The Noise Tradeoff"; S14 groups; S07 Dependency-Update-Tool. Agreement: consensus. Certainty: grounded.

ADOPT-C26. Review release notes and diffs when upgrading and rerun the project's tests, including integration tests specific to your usage. Level: practice. Stack: neutral. Sources: S02 "Test Thoroughly", "Upgrade Strategically". Agreement: consensus. Certainty: grounded. boundary: VERIFY.

ADOPT-C27. Deploy dependency updates through staged rollouts rather than to every system at once. Level: practice. Stack: neutral. Sources: S10 (patch management). Agreement: consensus. Certainty: grounded. boundary: DELIVER.

ADOPT-C28. "Live at Head": depend on the current version of internal or visible dependencies and make providers responsible for not breaking dependents, proven by running dependents' tests; viable only with comprehensive tests, CI visibility and compute. Level: decision. Stack: neutral; organisation-scale. Sources: S01 "Live at Head" ("largely unproven at scale" in open source). Agreement: contested. Positions: live at head (S01; force speed of feedback, shared upgrade cost; wins in a monorepo with provider-run downstream tests); version-pinned SemVer consumption (S01, S13, S15; force control; wins for external open-source consumption where dependents are invisible). Certainty: grounded.

**Cluster 6: versions are estimates**

ADOPT-C29. Treat a version number as the maintainer's estimate of compatibility, not a guarantee; with enough users every observable behaviour is depended upon (Hyrum's Law). Level: principle. Stack: neutral. Sources: S01 "SemVer Limits", "Foundation Problem"; S15 requires declaring a public API (the promise is only about the declared API). Agreement: majority. Positions: SemVer ranges are a usable contract (S15; force delivery speed; wins when API is narrow and well declared); SemVer is an estimate and tests are the evidence (S01; force correctness, confidence; wins as consumers and surface grow). Certainty: grounded.

ADOPT-C30. Producers: declare the public API precisely, start at 0.1.0 in early development, and deprecate through at least one minor release before removal in a major. Level: practice. Stack: neutral. Sources: S15 (public API, 0.y.z, deprecation). Agreement: consensus. Certainty: grounded.

ADOPT-C31. When two dependencies need incompatible versions of a shared one (diamond dependency), the options are to move versions forward or backward, or to patch locally; tolerance differs by language. Level: practice. Stack: neutral with language variance. Sources: S01 "Dependency Hell". Agreement: consensus. Certainty: grounded.

**Cluster 7: supply-chain integrity of consumption**

ADOPT-C32. Obtain artifacts only through controlled, trusted channels: a standardised package manager and an internal cache or repository of sanctioned components, which also protects against upstream unavailability. Level: decision. Stack: neutral. Sources: S20 "Ingest It", "Enforce It"; S05 PW.4.1 Example 4. Agreement: majority. Positions: managed repository or mirror (S20, S05; force control, availability; wins for larger orgs and regulated products); direct pull from public registry with lock and hashes (S16, S17, S22; force cost of ownership; wins for small teams). Certainty: grounded.

ADOPT-C33. Scan consumed artifacts for known vulnerabilities, licence and end-of-life status, and, at higher maturity, for malware, before and after integration. Level: practice. Stack: neutral. Sources: S20 "Scan It"; S09; S05 PW.4.4 Example 2 ("automatic detection of known vulnerabilities" in the toolchain). Agreement: consensus. Certainty: grounded.

ADOPT-C34. Obtain and check provenance information (SBOM, source composition, signatures) per component and apply integrity checks; prefer components with signed releases. Level: practice. Stack: neutral. Sources: S05 PW.4.1 Example 3, PW.4.4 Example 6; S07 Signed-Releases (High risk); S20 L3-L4. Agreement: majority. Positions: require provenance for all (S20 Audit/Enforce; force security; wins for high-criticality); provenance as preferred signal only (S07; force cost of ownership; ecosystem coverage still partial, inferred). Certainty: grounded.

ADOPT-C35. SLSA protects integrity of what a producer built; it does not say anything about the levels of its dependencies and does not address a dependency being removed. Apply provenance verification recursively to dependencies to counter compromised ones; address unavailability separately (mirror, vendor). Level: principle. Stack: neutral. Sources: S04 "What SLSA Does NOT Cover"; S03 "Compromised Dependency", "Dependency Unavailability". Agreement: consensus. Certainty: grounded.

ADOPT-C36. For the highest assurance, rebuild every deployed open-source artifact from source in your own infrastructure, mirror source, and be able to privately patch within days. Level: decision. Stack: neutral. Sources: S20 "Rebuild It", "Fix It + Upstream", Maturity L4. Agreement: contested. Positions: rebuild everything (S20; force security, control; wins for critical infrastructure, supply-chain-targeted orgs; costs large engineering effort); consume prebuilt verified artifacts (S16, S17, S22; force cost of ownership). Certainty: grounded.

**Cluster 8: inventory and monitoring**

ADOPT-C37. Maintain an inventory of every dependency, transitive included, and where it is deployed; centrally generate the SBOM. Level: practice. Stack: neutral. Sources: S10 ("Centrally generate and manage the SBOM", "Track... transitive"); S20 "Inventory It"; S27 (SBOM as nested inventory); S02 Transitive; S07 SBOM check. Agreement: consensus. Certainty: grounded.

ADOPT-C38. Continuously monitor vulnerability databases (CVE, NVD, OSV) against the inventory for as long as the software is in service, with a plan for triage and update. Level: practice. Stack: neutral. Sources: S10; S05 PW.4.4 Example 1; S09. Agreement: consensus. Certainty: grounded. boundary: OPERATE.

ADOPT-C39. Track whether each component is still maintained and has not reached end of life, and set a plan of action for components that are abandoned or about to disappear. Level: practice. Stack: neutral. Sources: S05 PW.4.4 Examples 4-5; S01 (orphaned packages become critical infrastructure; checklists fail at scale). Agreement: consensus. Certainty: grounded.

**Cluster 9: containing the dependency**

ADOPT-C40. Put a thin wrapper or adapter, containing only what the project needs, between your code and a dependency whose substitution is plausible, so a swap does not touch the whole codebase; keep external types out of the inside. Level: decision. Stack: neutral. Sources: S02 "Abstract the Dependency"; S24 ("code pertaining to the inside part should not leak into the outside part"). Agreement: contested. Positions: wrap (S02, S24; force reversibility, exit risk, testability; wins for volatile, security-sensitive or single-vendor dependencies and for external services); do not wrap, use directly (S11: investment into reducing lock-in can raise total cost; S19: a speculative abstraction carries cost; forces cost of ownership, cognitive load; wins when switching probability is low and the dependency is a stable, standard interface). Certainty: grounded; the tie-breaking by switching probability is from S11 and inferred as applied to code.

ADOPT-C41. Isolate risky dependencies at runtime (sandbox, least privilege) to bound the damage from bugs or compromise. Level: practice. Stack: neutral. Sources: S02 "Isolate the Dependency" (author notes isolation is hard and underused); S08 test in isolated environments. Agreement: majority. Certainty: grounded; practicality open.

ADOPT-C42. For a tiny used surface, copy or reimplement the needed code instead of depending. Level: practice. Stack: neutral. Sources: S02 "Avoid or Reduce". Agreement: contested (against: lost upstream fixes, see S01 cost of forks and S12 only on core). Positions: copy (S02; force attack surface, exit risk); depend (S05 PW.4, particularly for cryptography; force correctness). Certainty: grounded for S02, inferred for the opposing arguments.

ADOPT-C43. Prefer source-control problems over dependency-management problems: bring code inside the organisational boundary where visibility of use makes problems visible. Level: decision. Stack: neutral; organisation-scale. Sources: S01 "When to Import", "Vendoring and Monorepos". Agreement: contested. Positions: vendor or monorepo (S01; force control, visibility; wins with large codebases and the tooling to carry it); consume from registry with lock (S16, S22; force cost of ownership). Certainty: grounded.

ADOPT-C44. Upstream rather than carry private forks: contribute fixes to the maintainers, and report vulnerabilities found in a component to its maintainer. Level: practice. Stack: neutral. Sources: S20 "Fix It + Upstream"; S25 Art. 13(6); S01 (externally shared code is costly to modify). Agreement: majority. Certainty: grounded.

**Cluster 10: lock-in**

ADOPT-C45. Treat lock-in as a spectrum with at least eight kinds (vendor, product, version, architecture, platform, skills, legal, mental); avoiding one often creates another, and open source does not by itself remove it. Level: principle. Stack: neutral. Sources: S11. Agreement: majority (single authoritative source; consistent with S02 and S01). Certainty: grounded.

ADOPT-C46. Evaluate lock-in by two separate quantities, cost to switch and likelihood of switching; high cost with low likelihood needs insurance only if worthwhile, low cost with high likelihood buys agility. Level: decision. Stack: neutral. Sources: S11 ("Switching Cost Versus Likelihood"). Agreement: majority. Certainty: grounded.

ADOPT-C47. Accept lock-in when it buys a commensurate pay-off; investing in portability beyond the optimum raises total cost. Level: principle. Stack: neutral. Sources: S11 ("Decision Framework: The Optimum Point"). Agreement: contested. Positions: accept priced lock-in (S11; force delivery speed, cost of ownership); minimise via wrapping and open standards (S02, S24; force exit risk, control; wins for long-lived or regulated systems, critical rented services). Certainty: grounded.

**Cluster 11: availability, exit**

ADOPT-C48. Plan for an upstream package or version disappearing: keep a local cache, mirror or vendored copy so builds do not depend on the registry staying intact. Level: practice. Stack: neutral. Sources: S03 "Dependency Unavailability" (SLSA does not address); S20 "Ingest It" (cache local copies), Private Source Code Mirror; S22 vendoring and immutable proxy. Agreement: majority. Positions: mirror or vendor (force availability; wins for production-critical builds); rely on immutable public proxy/registry (S22 proxy immutability; force cost of ownership; wins where registry guarantees immutability). Certainty: grounded.

ADOPT-C49. Delegate audit effort: reuse audits by trusted organisations and review only version differences, since full manual audit of every dependency is too much work. Level: practice. Stack: Rust cargo-vet realisation; concept neutral. Sources: S23. Agreement: majority (one tool source; consistent with S05 Example 3 "use existing results from commercial services"). Certainty: grounded.

ADOPT-C50. For a rented service, define the exit path before adopting (data export, replacement candidate, contract notice) in proportion to criticality. Level: decision. Stack: neutral. Sources: none read directly; synthesis of S11 (switching cost) and S05 PW.4.4 Example 5 (plan for components no longer available). Agreement: not assessable. Certainty: inferred.

**Cluster 12: regulation**

ADOPT-C51. Where law applies (for example the EU Cyber Resilience Act for products with digital elements), exercising due diligence on integrated third-party components, keeping an SBOM and reporting component vulnerabilities to their maintainers are legal duties, not options. Level: principle. Stack: neutral; jurisdiction EU. Sources: S25 (Art. 13(5), 13(6), Annex I Part II via annotated copy). Agreement: consensus where it applies. Certainty: grounded in S25 but the primary text was not read (EUR-Lex fetch failed), so treat as inferred for exact wording.

### Gaps
- Rented services (SaaS, hosted APIs): no source read addresses SLAs, API deprecation policy, pricing risk or data-portability law directly; C07 and C50 are inferred from lock-in and outsourcing sources. Open.
- No peer-reviewed empirical study read on update lag, breakage rates or the effectiveness of cooldowns; C24 rests on one T3 analysis (S21) and tool documentation.
- CRA primary text (EUR-Lex) not read; C51 rests on an annotated copy (S25).
- No source defending exact pins in libraries or big-bang rewrites was found (C20, C06 record the absence).
- SSDF PDF was read through extracted text; only PW.4 rows were inspected, not PS.3.2 or RV.1.1.
- Licence compliance, base images and system packages, and monorepo-vs-polyrepo effects on dependency policy were not covered.

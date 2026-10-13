# Research result: 13_change_authors (area AUTH)

Slot boundary: what the outcomes (good design, good testing, trustworthy review, what runs is what was reviewed) require when change arrives at high volume or from a non-human author. Claims are author-neutral (maintainer ruling MD-02); where an authority argues the author changes the mechanism, that is recorded in L3 section "Author-sensitive positions". Reading date for web sources: 2026-10-13.

## L1 headline

Best practice here is not a separate rulebook for AI: the authorities (OpenSSF, Linux kernel, GitHub, DORA) say the same engineering bar applies to every author, and what changes with a non-human author or high volume is the mechanism, not the outcome: smaller reviewable batches, an executable check per change, a reviewer independent of the author, enforced (not instructed) least privilege and network and credential limits, and attributable provenance; certainty is high for the permission and review-independence mechanisms (vendor docs, OWASP), moderate for the effect sizes (a few small or vendor studies, mixed results), and open for what makes AI-assisted review trustworthy.

Pinned: 21 sources (T1: 9, T2: 3, T3: 9, T4: 0); 36 claims; contested: review depth scaled by provenance, AI reviewer as gate versus human required, net effect of AI on delivery, agent executes versus only writes on high-blast-radius jobs, mandatory disclosure of tool use; fetch failures on T1: OWASP Top 10 for Agentic Applications (landing page read, document body not obtainable: guessed PDF URL returned 404, so its mitigations are known only from search-result summaries), NIST SP 800-218A (landing page only, document body not read), dora.dev landing pages (no figures, replaced by the Google Cloud DORA pages).

## L2 claims

### Claim clusters

1. One bar for every author: design, tests and review requirements do not drop for generated change; a person or role stays accountable and must be able to defend what they submit. Consensus, grounded. AUTH-C01, C02.
2. Intent before generation: scope, interfaces, out-of-scope and the acceptance check are fixed before the change is produced; fast generation without a user or intent anchor moves quickly in the wrong direction. Majority, grounded (one vendor guide, one DORA capability). AUTH-C04.
3. Review stays trustworthy at volume by independence and bounded size: approver is not the pusher or requester, approval binds to the final content, the unit of review is kept small; a second model may add a layer but is not shown to replace accountable review. Consensus on independence and binding, contested on AI reviewers. AUTH-C05, C06, C07, C08, C09, C03.
4. Every change carries an executable pass/fail check and shows evidence, not assertion; tests and code ideally come from independent contexts; quality gates (static analysis, complexity, security tests) stay on because measured quality drift is persistent. Majority, grounded for the principle, inferred for test independence. AUTH-C10, C11, C12, C13, C14, C15.
5. Volume control: small batches, frequent commits, rollback; measure delivery outcomes, not code produced; developers' own perception of speedup is unreliable; AI amplifies the strength or weakness of the existing delivery system. Majority; the net effect on delivery is contested. AUTH-C16, C17, C18, C19.
6. Provenance: record who or what authored, who approved, which tool and session; automation identities are distinct and signed; enforced gates apply to bots and administrators so what runs is what was reviewed; agent instruction and configuration files are reviewed like code. Majority, grounded. AUTH-C20, C21, C22, C23, C36.
7. Permissions and blast radius: least privilege and least agency, enforced in tooling not prompts, default-deny network and scoped filesystem, short-lived scoped credentials kept out of the execution environment, no bypass of branch protection, never combining untrusted input, sensitive access and state change without a gate. Consensus on the principle, majority on specific mechanisms. AUTH-C24 to C29, C34.
8. High-blast-radius execution: who may execute a production-affecting job (agent under enforced guards versus agent writes, human runs). Contested. AUTH-C30, C31.
9. Accountability infrastructure around automation: audit log of every automated action, reversibility through version control (tool checkpoints are not a substitute), the automation's own tool supply chain pinned and reviewed, a stated organizational policy on who may do what. Majority, grounded. AUTH-C31, C32, C33, C35.

### Live debates (forces in tension)

- Uniform bar versus scrutiny proportional to how much was generated: simplicity and fairness of one rule versus review effort spent where error probability is highest (AUTH-C01 versus C03).
- AI reviewer as a gate versus human review mandatory: review capacity and speed of feedback versus trustworthy accountability and independence of failure modes (AUTH-C08).
- Net effect of AI-assisted change on delivery: individual speed and perceived gain versus measured stability, review load and quality drift; studies disagree and differ in sample (AUTH-C17, C18).
- Agent executes high-blast-radius jobs under enforced guards versus agent only writes: delivery speed versus control and audit (AUTH-C30; maintainer MAINT-C63).
- Per-action human approval as the control versus enforced sandbox boundaries: control by attention versus control that does not fatigue (AUTH-C09, C25).
- Mandatory disclosure of tool use versus recommended disclosure: reviewer calibration and provenance versus friction and unenforceability (AUTH-C36).

### Candidate central decisions

1. Which unit of change is reviewed and how big may it be (batch bound), because review independence, rollback and evidence all hang on it.
2. Which actors (human, bot, agent) hold which identities and which scopes, with enforcement in tooling (the permission model every other control depends on).
3. Which gates are mandatory for every change whatever the author (executable check, static analysis, independent approval) and whether depth varies with provenance or risk.
4. What the provenance record contains (author identity, tool, session, approver) and whether tool use must be disclosed.
5. What automation may execute versus only write, per blast radius.

### Not covered

- No T1 normative text found that addresses AI-generated code review directly: NIST SP 800-218A is scoped to AI model development, and its body was not read. Open.
- OWASP Top 10 for Agentic Applications: the document body was not read; mitigations come from search-result summaries and from OWASP LLM06:2025 (read in full).
- Effects of AI on mutation-test adequacy, AI-reviewer accuracy and false-negative rates: no study read. Open.
- Regulated contexts and legal ownership or licence status of generated code (boundary: EXT licences). Not read.
- Open-source projects that ban AI contributions; maintainer burden from low-quality submissions. Not read.
- DORA 2025 report PDF body (figures read only through the Google Cloud and InfoQ pages).

## L3 full

### Source register

| id | tier | title | author or body | URL read | authoritative on |
|---|---|---|---|---|---|
| AUTH-S01 | T1 | NIST SP 800-218A, SSDF Community Profile for Generative AI and dual-use foundation models (July 2024) | NIST | https://csrc.nist.gov/pubs/sp/800/218/a/final (landing page) | scope: AI model development; no AI-generated-code statement seen |
| AUTH-S02 | T1 | OWASP LLM06:2025 Excessive Agency | OWASP GenAI Security Project | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | excessive functionality, permissions, autonomy; prevention list |
| AUTH-S03 | T1 | OWASP Top 10 for Agentic Applications for 2026 (published 9 Dec 2025) | OWASP GenAI Security Project | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (landing page only; body not read) | agentic risk taxonomy (ASI01 goal hijack, ASI02 tool misuse, ASI03 identity and privilege, ASI04 supply chain, ASI05 unexpected code execution); mitigations known from search-result summaries only |
| AUTH-S04 | T1 | Security-Focused Guide for AI Code Assistant Instructions (1 Aug 2025) | OpenSSF Best Practices and AI/ML Working Groups | https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions | AI output does not bypass review, testing, static analysis; accountability stays with the developer |
| AUTH-S05 | T1 | GitHub Copilot cloud agent: risks and built-in protections | GitHub Docs | https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations | vendor risk list and controls: human merge, requester cannot approve, single branch, firewall, workflow approval, signed commits and session logs |
| AUTH-S06 | T1 | About protected branches | GitHub Docs | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | required reviews, approval by someone other than the pusher, stale-approval dismissal, required checks, signed commits, apply to admins |
| AUTH-S07 | T1 | Claude Code: Security | Anthropic docs | https://code.claude.com/docs/en/security | permission modes, sandbox, cloud isolation, credential proxy, push restrictions, audit logging, user responsibility to review |
| AUTH-S08 | T1 | Claude Code: Best practices | Anthropic docs | https://code.claude.com/docs/en/best-practices | give the agent a check to run, evidence over assertion, hooks versus advisory instructions, writer/reviewer fresh context, approval fatigue, checkpoints versus git |
| AUTH-S09 | T1 | Codex: Agent approvals and security | OpenAI docs | https://learn.chatgpt.com/docs/agent-approvals-security (redirect from developers.openai.com) | default sandbox, network off by default, protected paths, prompt-injection note |
| AUTH-S10 | T2 | Linux kernel documentation: tool-generated content | Linux kernel project | https://docs.kernel.org/process/generated-content.html | disclosure and defend-what-you-submit rule; scrutiny proportional to generated share |
| AUTH-S11 | T2 | Introducing DORA's inaugural AI Capabilities Model (23 Sep 2025), with dora.dev 2025 landing and InfoQ summary (Sep 2025) | DORA / Google Cloud; InfoQ (T3 secondary for the stability sentence) | https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model ; https://dora.dev/research/2025/dora-report/ ; https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025 | seven capabilities; AI as amplifier; throughput now positive, instability still rising |
| AUTH-S12 | T2 | Announcing the 2024 DORA report | DORA / Google Cloud | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report | 2024: AI adoption associated with -1.5% throughput and -7.2% stability, with the hedged batch-size explanation |
| AUTH-S13 | T3 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (July 2025, arXiv preprint) | METR | https://arxiv.org/abs/2507.09089 (abstract) | randomized trial, 16 developers, 246 tasks: 19% slower with AI; expected -24%, believed -20% |
| AUTH-S14 | T3 | Do Users Write More Insecure Code with AI Assistants? (ACM CCS 2023, peer reviewed) | Perry, Srivastava, Kumar, Boneh | https://arxiv.org/abs/2211.03622 (abstract) | user study, 47 participants: less secure code, more confidence |
| AUTH-S15 | T3 | We Have a Package for You! Package hallucinations in code-generating LLMs (USENIX Security 2025, peer reviewed) | Spracklen et al. | https://arxiv.org/abs/2406.10279 (abstract) | 576,000 samples, 16 models: at least 5.2% (commercial) and 21.7% (open) hallucinated packages |
| AUTH-S16 | T3 | Does AI-Assisted Coding Deliver? A difference-in-differences study of Cursor adoption (MSR 2026) | arXiv 2511.04427 | https://arxiv.org/abs/2511.04427 (abstract) | transient velocity gain, persistent rise in static-analysis warnings and complexity |
| AUTH-S17 | T3 | AI Productivity Paradox (July 2025) | Faros AI (vendor telemetry, 10,000+ developers, 1,255 teams) | https://www.faros.ai/blog/ai-software-engineering | PRs +98%, review time +91%, PR size +154%, bugs per developer +9%, no company-level correlation |
| AUTH-S18 | T3 | 2025 GenAI Code Security Report (30 Jul 2025) | Veracode (vendor) | via search-result summaries only; vendor page not read | 80 tasks, 100+ models: insecure in 45% of cases (secondary; not read directly) |
| AUTH-S19 | T3 | Agents Rule of Two (31 Oct 2025) | Meta | https://ai.meta.com/blog/practical-ai-agent-security/ | no more than two of: untrusted input, sensitive access, state change or external communication |
| AUTH-S20 | T3 | Stack Overflow Developer Survey 2025, AI section | Stack Overflow | https://survey.stackoverflow.co/2025/ai | 46% distrust vs 33% trust AI accuracy; "almost right" is the top frustration |
| AUTH-S21 | T3 | Maintainer claims, entered as internal inputs: MAINT-C62, MAINT-C63 (07_maintainer_doctrine), DELIVER-C49 (04_delivery) | this repository's research | internal | agent limits enforced in tooling; agent writes but does not run high-blast-radius jobs; small batches with AI volume |

Counted as T3: S21 is an internal input, not an outside source. Tier counts above (T1 9, T2 3, T3 9) include it as one T3 item; outside sources are 20.

### Claims

**AUTH-C01**
- claim: Every change, whatever its author, should meet the same bar for design, testing and review; generated change gets no exemption from engineering process.
- level: principle; stack: neutral; sources: S04 ("not a shortcut around code reviews, testing, static analysis, documentation, and version control discipline"), S10, S05 (human review required before merge); agreement: consensus; certainty: grounded.

**AUTH-C02**
- claim: A named person or role should remain accountable for each change and able to explain and defend it; accountability attaches to the submitter, not to the tool.
- level: principle; stack: neutral; sources: S10 ("expected to understand and to be able to defend everything you submit"), S04 ("you are responsible for any harms"), S07 ("You're responsible for reviewing proposed code"); agreement: consensus; certainty: grounded.

**AUTH-C03**
- claim: Review depth should scale with risk and with the evidence that the submitter understands the change; where much of a change was produced automatically, expect and apply proportionally more scrutiny.
- level: decision; stack: neutral; sources: S10 ("expect additional scrutiny in proportion to how much of it was generated"), S14, S13; agreement: contested; certainty: grounded for the kernel statement, inferred for the generalisation.
- positions: (a) one uniform bar, depth set only by risk (S04, maintainer ruling): serves simplicity and fairness, wins when the bar is already high and enforced. (b) depth scaled by generated share (S10, supported by S14: users with an assistant wrote less secure code and believed it more secure): serves correctness and review effort placement, wins when submitter understanding cannot be assumed (high volume, many contributors, public intake). Author-neutral restatement: depth tracks evidence of understanding, whoever authored.

**AUTH-C04**
- claim: Intent, scope, interfaces, out-of-scope items and the acceptance check should be fixed before a change is produced, especially when production is cheap and fast.
- level: practice; stack: neutral; sources: S08 ("Explore first, then plan, then code"; specs name files and interfaces, state out of scope, end with an end-to-end verification step), S11 (without a user-centric focus, AI-assisted teams "may just be moving quickly in the wrong direction"); agreement: majority; certainty: grounded (vendor guide and one DORA capability).

**AUTH-C05**
- claim: The approver of a change should be a different party from whoever authored, pushed or requested it.
- level: principle; stack: neutral (mechanism GitHub); sources: S06 ("most recent reviewable push must be approved by someone other than the person who pushed it"), S05 ("prevents the user who asked ... from approving it"); agreement: consensus; certainty: grounded. boundary: DELIVER.

**AUTH-C06**
- claim: An approval should bind to the exact final content: new commits that change the diff should invalidate earlier approvals.
- level: practice; stack: neutral (mechanism GitHub); sources: S06 (dismiss stale approvals); agreement: consensus; certainty: grounded. boundary: DELIVER.

**AUTH-C07**
- claim: Keep the unit of review small enough for a meaningful review, and treat review capacity as the constraint when production volume rises.
- level: principle; stack: neutral; sources: S17 (review time +91%, PR size +154% at high adoption), S12 (batch size offered as the explanation of lower stability), S11 (working in small batches as a capability), S21 (DELIVER-C49); agreement: majority; certainty: grounded for the measurements, inferred for the causal reading (S12 itself hedges: "our data suggest").
- positions: some sources argue verification capacity is the binding constraint (S17); S11 argues small batches turn AI from neutral into positive. No source read argues the reverse.

**AUTH-C08**
- claim: A second model reviewing in a fresh context may be added as an extra review layer, but accountable review of the change should still be done by an independent responsible party.
- level: decision; stack: neutral; sources: S08 (writer/reviewer in separate sessions; "a reviewer prompted to find gaps will usually report some, even when the work is sound"), S05 (draft PRs from the agent must be reviewed and merged by a human), S04; agreement: contested; certainty: grounded as vendor statements, inferred as to the decision; open: no study read on AI-reviewer accuracy.
- positions: (a) AI reviewer as additional layer: serves speed of feedback and review capacity (S08); wins when volume exceeds human capacity and risk is low or the human review stays in force. (b) human-only gate for approval: serves independence of failure modes and accountability (S05, S10); wins when risk is high.

**AUTH-C09**
- claim: Per-action human approval should not be the only control on automation, because attention fades; pair it with enforced boundaries.
- level: principle; stack: neutral; sources: S08 ("After the tenth approval you're clicking through rather than reviewing"; allowlists and sandboxing cut interruptions), S07 (prompt-fatigue mitigation), S14 (more trust in the assistant went with less secure code); agreement: majority; certainty: grounded (vendor statements), inferred as principle.

**AUTH-C10**
- claim: Every change should come with an executable pass/fail check that does not depend on the author's own judgement that the work is done.
- level: principle; stack: neutral; sources: S08 ("Without a check it can run, 'looks done' is the only signal available"; "If you can't verify it, don't ship it"), S12 (small batches and robust testing as preconditions); agreement: consensus; certainty: grounded.

**AUTH-C11**
- claim: Completion should be shown as evidence (test output, command and result, screenshot), not asserted.
- level: practice; stack: neutral; sources: S08 ("show evidence rather than asserting success"); agreement: majority (single source, aligns with general verification practice in VERIFY); certainty: grounded.

**AUTH-C12**
- claim: Tests and the code they check should come from independent contexts where practicable, so that one set of assumptions does not validate itself.
- level: practice; stack: neutral; sources: S08 (one session writes tests, another writes code to pass them; fresh context reduces bias toward code just written); agreement: majority; certainty: inferred (a vendor recommendation; no study of effect read). boundary: VERIFY.

**AUTH-C13**
- claim: Static analysis and complexity gates should run on every change and their trend be watched, because volume-driven drift in warnings and complexity is persistent and slows later work.
- level: practice; stack: neutral; sources: S16 (transient velocity increase, persistent increase in static-analysis warnings and complexity, major factors in later slowdown; authors call for QA as first-class), S04; agreement: majority; certainty: grounded for the finding (one observational study of open-source projects using one tool), inferred for the practice. boundary: VERIFY.

**AUTH-C14**
- claim: Security testing should apply to every change, on the assumption that produced code may carry vulnerabilities, not only to changes known to be generated.
- level: principle; stack: neutral; sources: S04 ("Assume AI-written code contains vulnerabilities"), S14 (47 participants, less secure code), S18 (45% of tasks insecure; secondary, vendor, not read directly); agreement: majority; certainty: grounded for S04 and S14, inferred for the author-neutral form. boundary: SECD, TRANS.

**AUTH-C15**
- claim: Before a new dependency enters a change, verify that its name resolves to the intended, vetted package; a generated or suggested name is not evidence the package exists or is safe.
- level: practice; stack: neutral; sources: S15 (hallucinated packages in at least 5.2% of commercial-model and 21.7% of open-model samples; "a novel supply chain threat"), S04 (verify dependencies, use package managers, SBOM); agreement: majority; certainty: grounded. boundary: ADOPT.

**AUTH-C16**
- claim: Keep batches small, commit frequently, and keep rollback routine; high-volume production makes version control the safety net.
- level: practice; stack: neutral; sources: S11 ("frequent commits amplify AI's positive influence on individual effectiveness, while the frequent use of rollback features boosts the performance of AI-assisted teams"; small batches), S21 (DELIVER-C49); agreement: consensus (one program, plus the maintainer's input); certainty: grounded. boundary: DELIVER.

**AUTH-C17**
- claim: Judge change flow by delivery outcomes (stability, lead time, failures), not by the volume of code or pull requests produced.
- level: principle; stack: neutral; sources: S11/InfoQ (throughput now positively correlated with AI adoption but "software delivery instability continues to rise"), S12 (-1.5% throughput, -7.2% stability per estimate), S17 (individual gains, no company-level correlation), S13 (19% slower in a controlled trial); agreement: contested (on the net effect); certainty: grounded for each finding, inferred for the principle.
- positions: (a) AI raises throughput and satisfaction, instability is a fixable side effect (S11: capabilities model). (b) Gains vanish at organisation level (S17), or are negative for experienced developers in mature code (S13, 16 developers). Forces: delivery speed versus stability. Wins: (a) in teams with the foundation practices (S11 clusters 6 and 7); (b) elsewhere. Sample and vendor caveats apply to S13 and S17.

**AUTH-C18**
- claim: Do not rely on self-reported speed or security gains from automation; measure them against an independent baseline.
- level: principle; stack: neutral; sources: S13 (developers expected -24% time, believed -20% after, measured +19%), S14 (participants with the assistant were more likely to believe their code was secure), S20 (46% distrust AI accuracy, "almost right" the top frustration); agreement: majority; certainty: grounded for the findings (small samples), inferred for the principle.

**AUTH-C19**
- claim: Treat the delivery system's fundamentals (version control, small batches, testing, platform, clear policy) as preconditions: automation magnifies existing strengths and weaknesses.
- level: principle; stack: neutral; sources: S11 ("AI's primary role ... is that of an amplifier"; seven capabilities), S12 ("does not appear to be a panacea"); agreement: majority; certainty: grounded.

**AUTH-C20**
- claim: Each change should carry an attributable record: who or what authored it, who approved it, and which tool and session produced it.
- level: principle; stack: neutral; sources: S05 (commits authored by the agent with developer co-authorship, signed, with links to session logs), S10 (disclose which tool and which portions), S06 (signed commits); agreement: majority; certainty: grounded.

**AUTH-C21**
- claim: Automation identities should be distinct from human ones, and changes not attributed to a person should need an additional approval.
- level: practice; stack: neutral (mechanism GitHub); sources: S05 ("An additional approval is required when pull requests aren't attributed to a person"; commits signed); agreement: majority (one vendor); certainty: grounded.

**AUTH-C22**
- claim: What runs should be what was reviewed: required reviews, required checks and signed-commit rules should bind every actor, including bots and administrators.
- level: principle; stack: neutral (mechanism GitHub); sources: S06 ("apply the restrictions to admins and roles with the 'bypass branch protections' permission, too"; restrict who and what can push), S07 (a rule that the connected access can bypass does not block a session's push); agreement: consensus; certainty: grounded. boundary: DELIVER.

**AUTH-C23**
- claim: Files that steer an automated author (instruction files, prompts, hooks, tool configuration) should be versioned and reviewed like code, and made read-only to the author where possible.
- level: practice; stack: neutral; sources: S09 (`.git`, `.agents`, `.codex` stay read-only even in writable mode), S08 (instruction file checked into git; hooks deterministic versus advisory instructions), S07 (audit or block settings changes with hooks), S03 (ASI01 baseline: lock and version goal and prompt configuration, review changes like code; known from search summaries only); agreement: majority; certainty: grounded for S07 to S09, inferred for the OWASP part.

**AUTH-C24**
- claim: Give automation the least functionality, permissions and autonomy its task needs.
- level: principle; stack: neutral; sources: S02 (three root causes: excessive functionality, permissions, autonomy; prevention: minimise extensions, limit functionality and permissions, avoid open-ended extensions, user context, approval for significant actions, complete mediation), S03 ("least agency", search summaries), S07, S21 (MAINT-C62); agreement: consensus; certainty: grounded (S02 read in full).

**AUTH-C25**
- claim: Enforce automation's limits in the tooling (sandbox, scoped credentials, deny rules, deterministic hooks), not by instruction in a prompt.
- level: principle; stack: neutral; sources: S08 ("CLAUDE.md instructions ... are advisory, hooks are deterministic"), S07 (sandbox, fail-closed matching, managed settings), S02 ("complete mediation"), S21 (MAINT-C62); agreement: consensus; certainty: grounded.

**AUTH-C26**
- claim: Default automation to a scoped workspace and no network egress, and open egress per need.
- level: practice; stack: neutral; sources: S09 ("By default, the agent runs with network access turned off"; read-only sandbox outside version-controlled folders), S05 (firewall limits internet access), S07 (cloud sessions: network limited by default); agreement: consensus (three vendors); certainty: grounded.

**AUTH-C27**
- claim: In one session, do not combine all three of untrusted input, access to sensitive systems or data, and the ability to change state or communicate externally without a human gate or equivalent control.
- level: principle; stack: neutral; sources: S19 (Agents Rule of Two), S05 (prompt injection and data exposure listed as risks), S02; agreement: majority; certainty: grounded for the statement (one T3 source), inferred as generalisation.

**AUTH-C28**
- claim: Credentials available to automation should be short-lived and narrowly scoped, and kept out of the environment that executes generated code.
- level: practice; stack: neutral; sources: S07 (repository credentials never enter the session VM, which holds a short-lived session-scoped credential; short-lived narrowly scoped credentials in remote control); agreement: majority (one vendor); certainty: grounded.

**AUTH-C29**
- claim: Automation should push only to a restricted, non-protected target (one branch), never directly to protected branches or by tag or deletion, and repository rules should not be bypassable by the access it holds.
- level: practice; stack: neutral (mechanism GitHub); sources: S05 ("only has the ability to push to a single branch"), S07 (proxy rejects branch deletions and tag pushes; branch protection applies unless the access can bypass); agreement: majority; certainty: grounded. boundary: DELIVER.

**AUTH-C30**
- claim: For a job with a large blast radius (production data, irreversible effect), decide and record whether an agent may execute it under enforced guards or may only write it for a person to run.
- level: decision; stack: neutral; sources: S21 (MAINT-C63: agent writes, human executes), S02 (approval for high-impact actions; excessive autonomy as a root cause), S07 (auto mode: a classifier reviews actions and blocks the unsafe ones); agreement: contested; certainty: grounded for each position, inferred for the decision framing.
- positions: (a) agent executes with a classifier or sandbox: serves delivery speed; wins when guards can be applied and effects are reversible. (b) agent writes only, human runs: serves control and audit; wins when guards cannot be applied or effects are irreversible. boundary: DELIVER.

**AUTH-C31**
- claim: Every automated change should be reversible through version control; tool-level checkpoints are not a substitute for it.
- level: practice; stack: neutral; sources: S08 (checkpoints do not capture changes made through shell commands or external processes; "isn't a replacement for git"), S11 (rollback use boosts AI-assisted team performance); agreement: majority; certainty: grounded. boundary: DELIVER.

**AUTH-C32**
- claim: Log every automated action (commands, tool calls, plan changes) in a reviewable audit trail.
- level: practice; stack: neutral; sources: S07 (all cloud-session operations logged; usage monitoring via OpenTelemetry), S05 (session logs linked from commits), S03 (log plan deltas and tool-call sequences; search summaries); agreement: consensus; certainty: grounded for S05 and S07. boundary: OPERATE.

**AUTH-C33**
- claim: The automation's own tool and plugin supply chain (extension servers, plugins, tool descriptors) should be pinned, vetted, and not auto-updated without review.
- level: practice; stack: neutral; sources: S07 (MCP: write your own or use trusted providers; the vendor does not audit servers; managed MCP configuration), S03 (ASI04 and its mitigations, search summaries); agreement: majority; certainty: grounded for S07, inferred for the pinning rule. boundary: ADOPT.

**AUTH-C34**
- claim: Treat any text an automated author reads (issues, comments, web pages, tool output) as untrusted instructions-bearing input.
- level: principle; stack: neutral; sources: S05 (prompt injection via hidden messages in issues and comments), S09 ("Treat web results as untrusted"), S07 (prompt injection safeguards), S02; agreement: consensus; certainty: grounded.

**AUTH-C35**
- claim: State which actors (human, bot, agent) may do what in the change flow and which boundaries apply, so that ambiguity does not become risk.
- level: decision; stack: neutral; sources: S11 (first capability: "clear and communicated AI stance"), S04, S07 (managed settings enforce organizational standards); agreement: majority; certainty: grounded for the DORA capability as named; the author-neutral phrasing is inferred.

**AUTH-C36**
- claim: Decide whether tool use must be disclosed on a change, and if so what (tool, inputs, which parts).
- level: decision; stack: neutral; sources: S10 (disclose tools and inputs and which portions were affected, in cover letters and changelogs; maintainers keep discretion), S05 (authorship and session links recorded by the platform); agreement: contested; certainty: grounded for S10 and S05, inferred for the contest.
- positions: (a) mandatory or recorded disclosure: serves reviewer calibration and provenance (S10, S05); wins where reviewer time is scarce and intake is public. (b) no disclosure rule, same bar for all (S04, maintainer ruling): serves simplicity, and wins where the bar and gates are enforced regardless of origin. A platform-recorded trail (C20) gives (a)'s benefit without relying on declarations.

### Author-sensitive positions (authorities arguing the author or the volume changes the mechanism)

Each line: authority, tier, date; the argument; what mechanism changes; what stays the same.

- Linux kernel project (S10, T2, undated): "expect additional scrutiny in proportion to how much of it was generated". Review depth. Same: submitter must understand and defend the change.
- GitHub (S05, T1, read 2026-10-13): agent PRs need human merge; the requester cannot approve; unattributed PRs need an extra approval; workflows do not run until a person approves; push to one branch; firewall. Review independence, permissions, provenance. Same: branch protection and checks (S06) apply to all.
- DORA 2024 and 2025 (S11, S12, T2): AI volume raises batch size and instability unless small batches, version control and rollback are strong; version control "more crucial than ever". Batch bound, rollback. Same: the practices are long-standing DORA practices, not new.
- Faros telemetry (S17, T3, July 2025): human review absorbs the volume (review time +91%, PR size +154%). Review capacity and batch size.
- OWASP LLM06 and Agentic Top 10 (S02, T1; S03, T1 body not read): agents add a class of risk (excessive agency, goal hijack by untrusted text, tool misuse, unexpected code execution) beyond ordinary privilege rules. Permissions, egress, approvals, sandbox. Same: least privilege.
- Anthropic and OpenAI docs (S07, S08, S09, T1): vendors state that approvals, sandbox and network defaults are the control layer, and that the user reviews proposed changes. Permissions, blast radius.
- Meta (S19, T3, Oct 2025): the Rule of Two as a design constraint specific to agents. Permissions.
- Empirical (S13, S14, S15, S16, T3): perceived gains and confidence exceed measured; new failure type (hallucinated dependencies); persistent quality drift. Verification and dependency checks.
- Counter-position: OpenSSF (S04, T1, 1 Aug 2025) and the maintainer ruling hold that the same practices apply and no separate rule is needed; the sources above change the mechanism and its parameters, not the outcome required.

### Gaps (open)

- AUTH-G1: no T1 text found on review obligations for AI-generated code; NIST SP 800-218A body not read (scoped to AI model development; open whether any task addresses generated code).
- AUTH-G2: OWASP Agentic Top 10 body not read; mitigations are from search summaries.
- AUTH-G3: no study on AI-reviewer precision and recall, or on whether independent test authorship improves defect detection (C08, C12).
- AUTH-G4: the evidence on net effect (C17) is a vendor telemetry study, one 16-developer trial and observational studies; no large peer-reviewed study read.
- AUTH-G5: no source read on licence and ownership of generated code, or on project bans of AI contributions.
- AUTH-G6: Veracode figures only from secondary summaries; treat as unverified.

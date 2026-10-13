# Discovery result: slot 06 RUNSEC (injection and runtime security)

## L1 headline

Authoritative sources cover most of the eight sub-topics well (prototype pollution, eval and Function, command injection, permission model, ReDoS) with primary T1 runtime and MDN text plus strong peer-reviewed T2 evidence; deserialization has no JavaScript-specific T1, and path injection and secrets are thin. Certainty: grounded for what was fetched, inferred where a page was only partly read (see Pinned).

Pinned:
- Candidates by proposed tier: T1 23, T2 12, T3 1 (total 36).
- Sub-topics with no T1 candidate: unsafe deserialization (JavaScript-specific). Searched: OWASP Deserialization cheat sheet (covers PHP, Python, Java, .NET only), OWASP Node.js and JS/TS cheat sheets (no deserialization section seen), Node `v8` module docs (serialize/deserialize carry no untrusted-data warning). Thin, not empty: path injection (only a Node `path.isAbsolute` note and an OWASP Node.js cheat-sheet paragraph) and secrets in code (OWASP Secrets cheat sheet is language-neutral).
- Failed or partial fetches on T1 candidates: K22 (NVD record for CVE-2025-55130: fetch returned only the NVD home page; facts known only from search results, alternative copy not found); K11 (ECMA-262 draft: page fetched, but the `__proto__` Annex B sections were not extracted; the browser-only Annex B status is unverified); K19 (OWASP ASVS 5.0: only the repository chapter listing was read, not requirement text).

## L2 claims

Per sub-topic (best candidates; T1 present?):

- Prototype pollution: K07, K10, K12, K03, K01, K06 (T1) plus K23, K27, K35 (T2, T3). T1 yes. grounded.
- `eval` and `Function`: K08, K09, K06, K05, K14 (T1), K25 (T2, empirical). T1 yes. grounded.
- ReDoS: K15, K20, K13 (T1, guidance), K24, K26, K31, K34 (T2, evidence and mechanism). T1 yes for guidance; mechanism evidence is T2 only. grounded.
- Unsafe deserialization: K18 (T1, but no JS content, expect-restricted), no JS-specific source; only adjacent evidence in K25 (eval and exec injection). T1 NO. grounded gap (searched, see Pinned).
- Command injection in Node: K04 (T1), K17 (T1, principles only), K25, K30 (T2). T1 yes. grounded.
- Path injection in Node: K36, K13, K15 (T1, thin), K33 (T2, language-neutral), K19 (T1, unread). T1 yes but thin. inferred (depth of K13 and K19 not confirmed).
- Permission model: K02, K06, K01, K03, K22 (T1), K29 (T2, research precursor). T1 yes. grounded (K22 via search only).
- Secrets in code: K16 (T1, language-neutral), K28 (T2, empirical on GitHub leaks), K19 (T1, unread). T1 yes, thin for JavaScript. grounded for K16 and K28.

Disagreements between candidates:
- K03 (Node threat model) excludes prototype pollution from Node vulnerabilities ("sanitization is the app's responsibility"), while K01, K07 and K12 treat it as a threat to mitigate and K23 shows RCE gadgets in Node core APIs. Both positions are needed.
- K02 and K03 say the permission model is a "seat belt" and no boundary against malicious code; K22 (a critical bypass via symlinks) and K29 (per-package sandbox proposal) bear on how far it can be relied on.
- K08 offers `Function()` as a "safer alternative" to `eval`, while K09 labels `Function()` an injection sink; the two MDN pages differ in emphasis.
- K12 prefers Map/Set, null-prototype objects, and notes `--disable-proto` does not remove `constructor.prototype` paths; K07 lists schema validation first. Ordering of defences differs.
- K26 finds the usual ReDoS anti-pattern heuristics have many false positives and developers prefer rewriting the regex; K31 and K20 favour non-backtracking engines or input caps. Different remedies.

Gaps:
- Deserialization (JavaScript): no T1; candidate origins to look for in a later stage: `JSON.parse` reviver and `__proto__` key semantics in ECMA-262, node-serialize and YAML-loader advisories (not searched for individually).
- Path traversal in Node: no dedicated T1 text; ASVS V5 (file handling) must be read in full.
- Secrets: no JavaScript-specific T1 (no Node doc says "do not commit .env"; the Node environment-variables page was read and has no security statement).
- No spec-level T1 on ReDoS mechanism (ECMA-262 does not address it); only V8 blog K31.
- The Node security advisories feed (GitHub) lists none; the Node vulnerability blog posts exist (checked index only) and could give T1 CVE facts for the permission model and path issues.

## L3 full

Date column: publication or last update, or software version. `fetched: partial` means the page loaded but the relevant text was not fully read.

### Candidate table

| id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RUNSEC-K01 | Node.js Security Best Practices | Node.js project (named contributors incl. Ulises Gascon, Michael Dawson, Facundo Tuesca) | official Node.js learn docs, contributors are Node security-working-group members | https://nodejs.org/en/learn/getting-started/security-best-practices | yes | no date shown on page | official-doc | T1 | G1-G6 pass; G2 date not shown (unsure) | prototype pollution, permission model; lists CWE-mapped threats (no ReDoS, eval, child_process, path, secrets sections) | |
| RUNSEC-K02 | Node.js API: Permissions | Node.js project | official API doc | https://nodejs.org/api/permissions.html | yes | v26.11.1 docs; Stable (v23.5.0, v22.13.0) | official-doc | T1 | all pass | permission model: "seat belt", not a defence against malicious code; symlink and file-descriptor limits | |
| RUNSEC-K03 | Node.js Security Policy and threat model (SECURITY.md) | Node.js project | maintainers' threat model | https://github.com/nodejs/node/blob/main/SECURITY.md | yes | current main (2026) | official-doc | T1 | all pass; G2 date only "current repository" | trust boundaries; excludes prototype pollution, permission model, vm from vulnerabilities | |
| RUNSEC-K04 | Node.js API: child_process | Node.js project | official API doc | https://nodejs.org/api/child_process.html | yes | v26.11.1 | official-doc | T1 | all pass | command injection (`exec`, `shell` option, Windows batch files) | |
| RUNSEC-K05 | Node.js API: vm | Node.js project | official API doc | https://nodejs.org/api/vm.html | yes | v26.11.1 | official-doc | T1 | all pass | "node:vm is not a security mechanism" (eval-like sandboxing) | |
| RUNSEC-K06 | Node.js CLI documentation | Node.js project | official API doc | https://nodejs.org/api/cli.html | yes | v26.11.1 | official-doc | T1 | all pass | `--disable-proto`, `--disallow-code-generation-from-strings` (does not affect vm), permission flags | |
| RUNSEC-K07 | MDN: Prototype pollution | MDN Web Docs (Mozilla and contributors) | MDN reference | https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution | yes | last modified 2025-10-17 | official-doc | T1 | all pass | pollution mechanism, null-prototype objects, `Object.hasOwn`, Map, schema validation, freeze | |
| RUNSEC-K08 | MDN: eval() | MDN Web Docs | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval | yes | page date not shown | official-doc | T1 | all pass | eval risks, direct vs indirect, alternatives, TrustedScript | DOMSEC (Trusted Types, CSP) |
| RUNSEC-K09 | MDN: Function() constructor | MDN Web Docs | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function | yes | page date not shown | official-doc | T1 | all pass | Function constructor as injection sink | DOMSEC |
| RUNSEC-K10 | MDN: Object.prototype.__proto__ | MDN Web Docs | MDN reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto | yes | page date not shown | official-doc | T1 | all pass | `__proto__` deprecated, pollution risk, null-prototype behaviour | LANG |
| RUNSEC-K11 | ECMAScript Language Specification (Annex B: `__proto__`, object initializers) | Ecma TC39 | the normative spec | https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html | partial: page loaded (ECMAScript 2027 draft), `__proto__` sections not extracted by two attempts; raw spec fetch via shell was denied | 2027 draft | spec | T1 | G1-G6 pass in principle; content not verified | prototype pollution mechanism (`__proto__` accessor, literal `__proto__`, JSON.parse own-property behaviour) | LANG |
| RUNSEC-K12 | Prototype Pollution Prevention Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Prototype_Pollution_Prevention_Cheat_Sheet.html | yes | no date shown | official-doc | T1 | G1-G6 pass; G4 partly restates MDN (unsure) | Map/Set, `Object.create(null)`, freeze, `--disable-proto`, limit of that flag | |
| RUNSEC-K13 | NodeJS Security Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html | yes | no date or author shown | official-doc | T1 | G3 unsure (short statements), G4 unsure (restates runtime docs) | eval, `child_process.exec`, ReDoS, path traversal, injection | |
| RUNSEC-K14 | JavaScript and TypeScript Security Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/JavaScript_and_TypeScript_Security_Cheat_Sheet.html | yes | no date shown | official-doc | T1 | G2 date not shown (unsure); G3 passes | "never build code from strings", ReDoS, prototype pollution, `any`/`unknown`, runtime validation | TYPES (validation), DOMSEC (DOM sinks) |
| RUNSEC-K15 | Input Validation Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | yes | no date shown | official-doc | T1 | language-neutral; G3 passes | regex safety (bound length, non-backtracking, timeouts), file name handling | TYPES |
| RUNSEC-K16 | Secrets Management Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | yes | no date shown | official-doc | T1 | language-neutral | no hardcoded secrets, env variables as weaker option, pre-commit detection, rotation | |
| RUNSEC-K17 | OS Command Injection Defense Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html | yes | no date shown | official-doc | T1 expect-restricted: principles only; no Node.js or JavaScript example | G3 passes | command injection principles (avoid shell, parameterize, allowlist) | |
| RUNSEC-K18 | Deserialization Cheat Sheet | OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html | yes | no date shown | official-doc | T1 expect-restricted: principles only; JavaScript not covered | G3 passes | deserialization principles (prefer data formats, sign, allowlist) | |
| RUNSEC-K19 | OWASP Application Security Verification Standard 5.0 | OWASP (141 contributors per project page) | OWASP flagship standard | https://owasp.org/www-project-application-security-verification-standard/ (chapters: https://github.com/OWASP/ASVS/tree/master/5.0/en) | partial: project page and chapter listing read; requirement text not read | 5.0.0 | spec | T1 | G1-G6 pass in principle; content not verified | chapters V1 encoding and sanitization, V2 validation, V5 file handling, V13 configuration, V15 secure coding | |
| RUNSEC-K20 | Correctly Using Regular Expressions for Secure Input Validation | OpenSSF Best Practices Working Group | OpenSSF | https://best.openssf.org/Correctly-Using-Regular-Expressions | yes | no date shown | official-doc | T1 | G2 date not shown (unsure) | ReDoS mitigations (non-backtracking engines, length limits), anchoring, JavaScript anchor semantics | |
| RUNSEC-K21 | GHSA-jf85-cpcp-j695 / CVE-2019-10744: Prototype Pollution in lodash | GitHub Advisory Database | advisory record | https://osv.dev/vulnerability/GHSA-jf85-cpcp-j695 | yes (via OSV mirror) | published 2019-07-10 | advisory | T1 (fact only) | G2 old but a dated fact | prototype pollution real-world instance via `defaultsDeep` constructor path | |
| RUNSEC-K22 | CVE-2025-55130: Node.js permission model bypass via crafted symlinks | Node.js CNA / NVD | CVE record | https://nvd.nist.gov/vuln/detail/cve-2025-55130 | failed: only the NVD home page was returned; facts (CVSS 9.1, affects v20, v22, v24, v25, published 2026-01-20) come from search snippets only; alternative copy not found | 2026-01-20 | advisory | T1 (fact only) | G1 and G3 pass for a CVE record; unverified here | permission model limits | |
| RUNSEC-K23 | Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js | M. Shcherbakov, M. Balliu (KTH), C.-A. Staicu (CISPA) | USENIX Security 2023 | https://www.usenix.org/conference/usenixsecurity23/presentation/shcherbakov | yes (abstract page) | 2023-08 | paper | T2 | G1-G6 pass | prototype pollution to RCE; eleven universal gadgets in Node core APIs; eight RCE exploits | |
| RUNSEC-K24 | Freezing the Web: A Study of ReDoS Vulnerabilities in JavaScript-based Web Servers | C.-A. Staicu, M. Pradel (TU Darmstadt) | USENIX Security 2018 | https://www.usenix.org/conference/usenixsecurity18/presentation/staicu | yes (abstract page) | 2018-08 | paper | T2 | G2 pre-2020 but ReDoS mechanism unchanged (unsure) | ReDoS in Node servers: 25 new flaws, 339 of 2,846 sites vulnerable | |
| RUNSEC-K25 | Synode: Understanding and Automatically Preventing Injection Attacks on Node.js | C.-A. Staicu, M. Pradel, B. Livshits | NDSS 2018 | https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_07A-2_Staicu_paper.pdf | yes (PDF first page read: title, authors, abstract) | 2018-02 | paper | T2 | G2 unsure (2018, but `eval` and `exec` APIs unchanged) | eval and exec injection in 235,850 modules; template-based runtime policy | |
| RUNSEC-K26 | The Impact of ReDoS in Practice: An Empirical Study at the Ecosystem Scale | J. C. Davis, C. A. Coghlan, F. Servant, D. Lee (Virginia Tech) | ESEC/FSE 2018 | https://researchconnect.stonybrook.edu/en/publications/the-impact-of-regular-expression-denial-of-service-redos-in-pract/ (DOI 10.1145/3236024.3236027) | partial: publisher page 403; a mirrored PDF returned an unrelated summary and was not trusted; abstract read from the institutional record | 2018-11 | paper | T2 | G2 unsure (2018) | ReDoS prevalence in npm; heuristics have false positives; developers prefer rewriting regexes | |
| RUNSEC-K27 | Detecting Node.js Prototype Pollution Vulnerabilities via Object Lookup Analysis | S. Li, M. Kang, J. Hou, Y. Cao (Johns Hopkins) | ESEC/FSE 2021 | https://2021.esec-fse.org/details/fse-2021-papers/12/Detecting-Node-js-Prototype-Pollution-Vulnerabilities-via-Object-Lookup-Analysis | yes (conference page) | 2021 | paper | T2 | pass; G4: detector paper, evidence for prevalence only | prototype pollution prevalence: 61 new vulnerabilities, 11 CVEs | |
| RUNSEC-K28 | How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories | M. Meli, M. R. McNiece, B. Reaves | NDSS 2019 | https://www.ndss-symposium.org/ndss-paper/how-bad-can-it-git-characterizing-secret-leakage-in-public-github-repositories/ | yes (abstract page) | 2019 | paper | T2 | G2 unsure (2019); language-neutral | secrets in code: over 100,000 repos affected, thousands of new leaks daily | |
| RUNSEC-K29 | Containing Malicious Package Updates in npm with a Lightweight Permission System | G. Ferreira, L. Jia, J. Sunshine, C. Kästner | ICSE 2021 | https://arxiv.org/abs/2103.05769 | yes (arXiv abstract) | 2021-03 | paper | T2 | pass | per-package least-privilege design, precursor to a permission model | SUPPLY |
| RUNSEC-K30 | SecBench.js: An Executable Security Benchmark Suite for Server-Side JavaScript | M. H. M. Bhuiyan, A. S. Parthasarathy, N. Vasilakis, M. Pradel, C.-A. Staicu | ICSE 2023 | https://conf.researchr.org/details/icse-2023/icse-2023-technical-track/99/SecBench-js-An-Executable-Security-Benchmark-Suite-for-Server-Side-JavaScript | yes (conference page) | 2023-05 | paper | T2 | pass | 600 npm vulnerabilities in five classes (injection, path traversal, prototype pollution, ReDoS, code injection per the abstract summary), 168 mislabeled advisory versions | |
| RUNSEC-K31 | An experimental non-backtracking RegExp engine | M. Bidlingmaier (V8 team) | V8 project blog | https://v8.dev/blog/non-backtracking-regexp | yes | 2021-01-11 | maintainer-writing | T2 | G2 unsure: flag still experimental per post, current state not checked | ReDoS mechanism in V8's Irregexp; `l` flag; no backreferences or lookaround | RUNTIME |
| RUNSEC-K32 | Developing a minimally HashDoS resistant, yet quickly reversible integer hash for V8 | J. Cheung (Node.js and V8 contributor, Igalia) | Node.js blog (vulnerability section) | https://nodejs.org/en/blog/vulnerability/march-2026-hashdos | yes | 2026-03-24 | maintainer-writing | T2 | pass; vendor-sponsorship noted, no conflict on claims | algorithmic DoS from deterministic hashing (CVE-2026-21717), JSON payload hang | RUNTIME |
| RUNSEC-K33 | CWE-22: Path Traversal | MITRE | CWE catalogue | https://cwe.mitre.org/data/definitions/22.html | yes | CWE 4.20, 2026-04-30 | dataset | T2 expect-restricted: language-neutral taxonomy, facts and mitigations only | G4 unsure (a catalogue, not an origin) | path traversal: canonicalize, allowlist, avoid denylists | |
| RUNSEC-K34 | Regular expression Denial of Service (ReDoS) | OWASP Community (author Adar Weidman) | OWASP wiki | https://community.owasp.org/attacks/Regular_expression_Denial_of_Service_-_ReDoS | yes | no date shown | official-doc | T2 expect-restricted: community wiki, examples in .NET; mechanism only | G3 passes | ReDoS definition and evil-regex shapes | |
| RUNSEC-K35 | Server-side prototype pollution: Black-box detection without the DoS (Web Security Academy) | G. Heyes, PortSwigger Research | PortSwigger | https://portswigger.net/web-security/prototype-pollution/server-side | yes | no date shown | research-blog | T3 | G5 unsure (vendor scanner promoted, facts only) | gadgets to RCE via `child_process` options and `NODE_OPTIONS`, persistence in the process lifetime | |
| RUNSEC-K36 | Node.js API: path (`path.isAbsolute` note) | Node.js project | official API doc | https://nodejs.org/api/path.html | yes | v26.11.1 | official-doc | T1 | all pass; thin: only one security sentence | path traversal: `path.isAbsolute` is not safe for mitigating traversal | |

### Dismissed on sight (T4 tally)

- Secure-coding blog posts on Node path traversal (hosted by tutorial or security-vendor sites): 6 (a vendor blog, a tutorial site and four others; the search surfaced them, none opened)
- Vendor SCA pages and CVE-mirror aggregators (fluidattacks, acunetix, corgea hub, stack.watch, cvefeed, tuxcare, cyberdetails exploit page): 9
- Third-party GitHub issues quoting advisories: 4
- Medium post on selective memoization (author of the paper, but a restatement): 1
- Slide decks and talk summaries of Synode (Morning Paper blog): 2
- Press coverage of the OpenSSF npm guide (CSO Online, VentureBeat, ciso2ciso): 4
- Non-JavaScript regex guides (Microsoft .NET best practices, Okta blog, ASP.NET article): 3

### Searches run

- Fetched directly: Node.js docs (security best practices, permissions, SECURITY.md, child_process, vm, cli, v8, path, environment_variables, vulnerability blog index), MDN (prototype pollution, eval, Function, `__proto__`), OWASP cheat sheets (prototype pollution, Node.js, JS/TS, input validation, secrets, command injection, deserialization), OWASP community pages, ASVS, CWE-1321 and CWE-22, OpenSSF Concise Guide and regex guide.
- `Davis "The Impact of Regular Expression Denial of Service (ReDoS) in Practice" FSE 2018 empirical study`
- `Detecting Node.js prototype pollution vulnerabilities via object lookup analysis FSE 2021`
- `Staicu Pradel Leveraging "Synode" understanding and automatically preventing injection attacks on Node.js NDSS 2018`
- `Ferreira "Containing Malicious Package Updates in npm with a Lightweight Permission System" ICSE 2021`
- `"Using Selective Memoization to Defeat Regular Expression Denial of Service" Davis IEEE S&P 2021` (found, not fetched, not listed: unread)
- `Node.js injection detection Affogato OR "SecBench.js" OR "Mininode" security Node.js packages paper` (Affogato is a workshop paper, found, not fetched, not listed)
- `Node.js path traversal prevention path.resolve startsWith fs docs OR nodejs.org learn security directory traversal`
- `OpenSSF best practices working group guide JavaScript secure coding npm prototype pollution ReDoS guide`
- `GitHub Advisory lodash prototype pollution GHSA-p6mc-m468-83gw CVE-2019-10744`
- `Node.js permission model bypass symlink OR path traversal security release 2026 CVE nodejs.org blog vulnerability`
- `best.openssf.org "Correctly Using Regular Expressions for Secure Input Validation"`
- Dropped after fetching as weak or derivative: Node environment-variables doc (no security statement), OpenSSF Concise Guide (one sentence on secrets), CWE-1321 (restates OWASP and MDN mitigations), OWASP community Path Traversal page (PHP examples, no JavaScript).
- Failed or empty fetches: NDSS paper page on ndss-symposium.org (404, alternative PDF used), imperial college mirror of Synode (404), Davis personal-site PDF (404), ACM DL (403), a mirrored PDF at an NSF repository (returned an unrelated summary, discarded), `@ossf/secure-coding-guide-for-javascript` repo (404, may not exist), Node GitHub security advisories page (none listed), NVD CVE page (home page only), OpenSSF regex guide under a longer URL (404).

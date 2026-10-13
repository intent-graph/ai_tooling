# Slot 11_coverage: what the claim base covers, and what it misses

## L1 headline

The claim base (544 claims, 10 slots) is solid where Node and MDN documentation, OWASP and the web specifications speak (language semantics, async, DOM XSS, prototype pollution, supply chain, process lifecycle), but it has five high-criticality holes in server-side security that no claim grounds or grounds only by inference, and 60 percent of its claims rest on a single source; certainty: grounded for the counts and for every gap confirmed against the claim tables and the register, inferred for the criticality ratings and for what the unread parts of admitted sources contain.

Pinned:
- High-criticality gaps: 5: (1) randomness and crypto API misuse, including constant-time comparison; (2) query injection (SQL, NoSQL, ORM raw queries); (3) SSRF and outbound requests from Node; (4) JavaScript-specific unsafe deserialization; (5) path containment in Node (inferred-only recipe).
- Late candidates: 41 (collated from slots 01 to 10, deduplicated; none admitted; 3 fill a high gap, and 3 of the 5 high gaps have no candidate at all).
- Checker summary line: `total: 544 claims {'consensus': 193, 'single-source': 326, 'contested': 17, 'majority': 8}; errors 0; restricted citations 491`

## L2 claims

Gaps (grounded unless marked; criticality is my judgement, inferred):
- High, 5 (see Pinned). Gaps 1 to 3 were reported by no slot: searched the 544 claims and the register titles, no hit. Gaps 4 and 5 were reported by 06_runsec (RUNSEC-C43 to C45 are language-neutral; RUNSEC-C29 is single-source, inferred).
- Extraction misses, grounded: the admitted, unrestricted-for-06 Node security best-practices page (SRC-078) has headings on DNS rebinding, request smuggling, timing attacks, exposure of sensitive information, uncontrolled search path and memory access violation; no claim cites them. Timing attacks would partly close high gap 1. The admitted OWASP JS/TS cheat sheet (SRC-134, unrestricted) backs only 10 claims; whether it covers more is open.
- Medium, 31 and low, 20 across areas (table in L3): browser and Node async limits (retry, backoff, long tasks), WebSocket origin checks, server-side output encoding, javascript: URLs, secrets in client bundles, logging and information disclosure, CI workflow hardening, package managers other than npm and pnpm, JS-specific test evidence, container sizing, framework evidence (usage, governance, escaping for Lit and Solid), dates and Unicode, browser support policy.
- Evidence quality, grounded: ECMA-262 and the HTML Standard could not be read through the fetch tool (slots 01, 02, 03, 04, 06, 09); mechanism cells rest on MDN and Node docs.

Overlaps (grounded): 19 clusters, details in L3.
- Same fact, two owners: unhandled rejection (ASYNC-C04, RUNTIME-C40), uncaughtException (ASYNC-C05, RUNTIME-C37), emitter error listener (ASYNC-C23, RUNTIME-C31), HTTP timeouts (ASYNC-C55, RUNTIME-C42), ReDoS (ASYNC-C40, RUNSEC-C36, TYPES-C32), eval from strings (RUNSEC-C14, DOMSEC-C03, LANG-C49, ASYNC-C33), throw only Error (ASYNC-C18, LANG-C45), Node ESM facts (LANG-C60 to C63 versus STRUCT-C11, C13, C16, C18), cooldown (SUPPLY-C12 versus QUALITY-C46), `npm ci` (SUPPLY-C04, QUALITY-C42), Trusted Types (DOMSEC-C15, FW-C48, FW-C06), escape hatches (DOMSEC-C55, FW-C02), trust of dependencies (SUPPLY-C01, RUNSEC-C41).
- Same fact, different agreement label: LANG-C60 and C61 are single-source while their twins STRUCT-C11 and C16 are consensus.
- Conflict not marked contested: LANG-C64 states "avoid cycles" while STRUCT-C09 is contested on it; STRUCT-C45 accepts hasOwnProperty while LANG-C55 and RUNSEC-C07 say Object.hasOwn.
- Duplicate contested topics: private-member marking (LANG-C12, STRUCT-C41).

Boundary items (grounded): 101 claims carry `boundary:`: 84 point to another slot of this guideline, 16 to the web architecture guideline, 0 to the Python or CLI guidelines.
- Hold in the sibling instead, or split: DOMSEC-C35, C59, C60 (token storage, JSONP, CORS), DOMSEC-C26, C28, C29 (CSP deployment), TYPES-C29, RUNTIME-C39, C41 (supervisor side), FW-C04, C13, C14, C44, C45, C07 (framework deployment and usage by rendering strategy). Candidate, inferred: STRUCT-C50 to C54 (API shape) against the sibling's API contract.
- Tag format is inconsistent (`04_struct`, `04 STRUCT`, `STRUCT`, `tier: T1;` prefixes): normalise before consolidation.

Late candidates (grounded as collation): 41 rows in L3; 3 fill high gap 4 or 5; slot-11 leads for gaps 1 to 3 are listed apart and not counted.

Threshold check (grounded): checker exit clean, 0 errors, 491 restricted-citation notes. Mostly single-source: 08_quality (87 percent), 10_frameworks (94), 09_runtime (83), 02_types (58), 07_supply (57), 03_async (53); 01_lang is half (50). Least solid for consolidation: 08, 09, 10.

## L3 full

### 1. Gaps

Method: read every slot's L2, gaps and late candidates in full; loaded all 544 claims into one table and searched it by keyword (random, crypto, timing, SQL, SSRF, path, deserial, encoding, WebSocket, javascript:, Intl, logging, CSRF, upload, Actions, cookie, DNS, smuggling); searched the register titles for the same terms. One page was fetched (SRC-078 headings, tool-extracted). Criticality is inferred from the plan's stance (security rests on predictability) and is my rating, not a source's.

#### 1.1 High criticality (5)

| id | gap | area | origin | certainty | what exists | lead |
|---|---|---|---|---|---|---|
| G-H1 | Randomness and crypto API misuse: Math.random for tokens, Web Crypto and node:crypto use, constant-time comparison, password hashing | 06_runsec, 05_domsec | slot 11 (new) | grounded that no claim states it (only LANG-C34, BigInt timing); inferred that it is a hole | SRC-078 has a timing-attack heading, unextracted; no register row on randomness or cryptography | slot-11 leads below |
| G-H2 | Query injection from Node code: SQL parameterization, NoSQL operator injection, ORM raw queries | 06_runsec | slot 11 (new) | same | RUNSEC-C23 to C26 cover command injection only; TYPES-C34 mass assignment | slot-11 leads |
| G-H3 | SSRF and outbound requests: URL allowlists, internal address blocking, DNS rebinding, redirect following | 06_runsec | slot 11 (new) | same | SRC-078 has a DNS rebinding heading, unextracted; DOMSEC-C56 and C57 are client-side redirect and URL checks | slot-11 leads |
| G-H4 | JavaScript-specific unsafe deserialization (node-serialize, js-yaml before 4, v8.deserialize, structuredClone limits) | 06_runsec | 06 | grounded | RUNSEC-C43 to C45 language-neutral only (SRC-133 does not cover JavaScript) | LC-18, LC-21 |
| G-H5 | Path containment in Node: resolve, realpath, prefix test; zip-slip style extraction | 06_runsec | 06 | grounded | RUNSEC-C27 to C29, C29 single-source inferred; one sentence on path.isAbsolute | LC-19 |

Slot-11 leads for G-H1 to G-H3 (not fetched, not admitted, URLs follow the site's naming pattern and are unverified, therefore not counted among the 41): OWASP SQL Injection Prevention cheat sheet; OWASP SSRF Prevention cheat sheet; OWASP Cryptographic Storage cheat sheet (all T1 per the plan); Node.js `crypto` API page (T1; randomBytes, timingSafeEqual); MDN `Crypto.getRandomValues` (T1); OWASP ASVS 5.0 cryptography and encoding chapters (SRC-132 is restricted to four read requirements, so a broader read needs an audit decision). Also re-read SRC-134 and SRC-078 in full (admitted, extraction retry).

#### 1.2 Medium and low, merged (slot-reported unless "new")

| id | crit | area | gap | origin |
|---|---|---|---|---|
| G-M01 | medium | 01 | Exact decimal and money arithmetic; TC39 decimal stage not in the finished list | 01 |
| G-M02 | medium | 01 | Automatic semicolon insertion, `typeof`/`instanceof`/realms, getters and setters, Symbol, iterators and generators, destructuring and spread have no claim | 01 |
| G-M03 | medium | 01 | Dates, time zones, Unicode and string handling, Intl (ECMA-402 is T1 in the plan, no claim) | new |
| G-M04 | medium | 01-10 | ECMA-262 and HTML Standard clause text unread (tool returns table of contents): modules, Annex B, JSON.parse, Promise jobs, WeakRef | 01, 02, 03, 04, 06, 09 |
| G-M05 | medium | 02 | Type layer "none" has no admitted holder; JSDoc-checked JS has facts only | 02 |
| G-M06 | medium | 02 | Unsoundness of user-defined type guards (TYPES-C20 open) | 02 |
| G-M07 | medium | 03 | Operational versus programmer errors; error disclosure to callers | 03, 11 |
| G-M08 | medium | 03 | Concurrency limits, retry, backoff with jitter, Retry-After | 03 |
| G-M09 | medium | 03, 05 | Browser long tasks, yielding to the main thread | 03 |
| G-M10 | medium | 04 | Dependency direction and layering (STRUCT-C60 open); state design in applications | 04 |
| G-M11 | medium | 05 | `javascript:` URL as a code sink (DOMSEC-C57 inferred, no normative text); `Element.setHTML` has no register page | 05 |
| G-M12 | medium | 05 | WebSocket origin checking and cross-site WebSocket hijacking | new |
| G-M13 | medium | 05, 06 | Server-side contextual output encoding and serialising state into script blocks (SSR hydration); only client-side and framework claims exist | new |
| G-M14 | medium | 06 | Secrets in Node and npm (.env, `--env-file`, secrets in client bundles) | 06 |
| G-M15 | medium | 06 | Regex timeout mechanism in JavaScript; V8 non-backtracking engine status beyond 2021 | 06 |
| G-M16 | medium | 06, 09 | Logging: sensitive data, log injection, error messages and stack traces to clients | new |
| G-M17 | medium | 06 | Request-size and parser limits at the HTTP layer; HTTP request smuggling, exposure of sensitive information (SRC-078 headings, unextracted) | new |
| G-M18 | medium | 07 | Release-age cooldown efficacy (SUPPLY-C13 open) | 07 |
| G-M19 | medium | 07 | yarn, bun, Deno install behaviour; only npm and pnpm covered | 07 |
| G-M20 | medium | 07, 08 | CI workflow hardening (action pinning, untrusted-trigger workflows); SUPPLY-C38 covers tokens only | new |
| G-M21 | medium | 08 | JavaScript-specific testing evidence (flakiness, strategy); fuzzing for JavaScript | 08 |
| G-M22 | medium | 09 | Container memory and heap sizing; production process configuration | 09, new |
| G-M23 | medium | 09 | cluster and child_process lifecycle; supervisor shutdown contract (boundary: web architecture) | 09 |
| G-M24 | medium | 10 | Measured usage for Angular, Vue, Svelte, Solid, Lit, htmx; governance for Angular, Svelte, htmx; support policy for Svelte and Solid; default escaping for Lit and Solid | 10 |
| G-M25 | medium | cross | Browser support policy, transpilation, polyfills, browserslist | new |
| G-M26 | medium | cross | Browser-side workers and service workers at code level (only DOMSEC-C58 touches service workers) | new |
| G-M27 | medium | 04 | Function API design for application code (parameter objects, flags, return shapes) | 04 |
| G-M28 | medium | 02 | Choosing between schema-validation approaches: no admitted comparison | 02 |
| G-M29 | medium | 01 | Immutability as a design preference (no T1 or paired T2) | 01 |
| G-M30 | medium | 05 | Trusted Types deployment evidence beyond a 13-developer study; verbatim default-policy text | 05 |
| G-M31 | medium | 09 | Independent T2 for engine internals and for JavaScript benchmarking | 09 |
| G-L01 | low | 01 | `parseInt` radix advice (outdated in the one source) | 01 |
| G-L02 | low | 03 | Async iteration, `for await`, structured concurrency, Promise.try guidance | 03 |
| G-L03 | low | 04 | Naming transfer to JavaScript; casing conventions unrecorded | 04 |
| G-L04 | low | 04 | Composition versus inheritance; barrel-file load cost | 04 |
| G-L05 | low | 05 | Clickjacking and frame embedding at code level (boundary mostly web architecture) | new |
| G-L06 | low | 05 | SRC-316 class count (14 versus 16), SRC-268 and SRC-270 figures unread | 05 |
| G-L07 | low | 06 | Windows .bat and .cmd with execFile; lint rule docs not in register | 06 |
| G-L08 | low | 07 | Typosquatting second T2; audit false-positive evidence; update batching and automerge; SLSA Source track, SBOM formats | 07 |
| G-L09 | low | 08 | Formatting normative ground; coverage thresholds; property-based and mutation evidence; snapshot and mocking policy; pre-commit wiring | 08 |
| G-L10 | low | 09 | Leak prevalence studies; AsyncLocalStorage cost; default highWaterMark value; WeakRef spec notes | 09 |
| G-L11 | low | 10 | htmx 4.0.0 release year; htmx type support; JSX typing page | 10 |
| G-L12 | low | 02 | Standard Schema adoption list; JSON Schema stability note | 02 |
| G-L13 | low | cross | Documentation comments (JSDoc), deprecation and versioning of one's own API | new |
| G-L14 | low | 01 | Class design: getters and setters (single Google position) | 01 |
| G-L15 | low | 03 | SRC-079 `--unhandled-rejections` entry text unreliable across three digests | 03 |
| G-L16 | low | 03 | DrAsync count 2.5k versus 2.6k (register versus paper) | 03 |
| G-L17 | low | 09 | Container and diagnostics_channel stability statements | 09 |
| G-L18 | low | 06 | `eval` and CSP deployment side (boundary: web architecture, deliberately not extracted) | 06 |
| G-L19 | low | 03 | SRC-250 gives 2018 ReDoS prevalence; no current figure | 03 |
| G-L20 | low | 08 | Typed linting cost numbers (SRC-181 gives none) | 08 |

Totals: high 5, medium 31, low 20 (56 rows). Ratings of rows marked "new" and of all criticalities are inferred.

### 2. Overlaps

| # | topic | ids | better owner | note |
|---|---|---|---|---|
| O01 | Unhandled rejection raised as uncaught exception | ASYNC-C04, RUNTIME-C40 | ASYNC-C04 | both consensus; RUNTIME-C40 also cites SRC-079, whose text slot 03 judged unreliable (SRC-082 alone suffices); both carry the folklore tag |
| O02 | uncaughtException last resort | ASYNC-C05, RUNTIME-C37 | RUNTIME-C37 | same source SRC-082; ASYNC-C05 adds the unhandledRejection hook |
| O03 | Emitter without error listener crashes | ASYNC-C23, RUNTIME-C31 | ASYNC-C23 | three sources against one |
| O04 | HTTP server timeouts | ASYNC-C55, RUNTIME-C42 | RUNTIME-C42 for values, ASYNC-C55 for the DoS ground | merge into one claim |
| O05 | ReDoS blocks the event loop | ASYNC-C40, RUNSEC-C36, TYPES-C32 (input bound) and RUNSEC-C30 to C37 | RUNSEC | ASYNC-C40 keeps the 2018 figures |
| O06 | Code from strings | RUNSEC-C14, C15; DOMSEC-C03; LANG-C49 (Google); ASYNC-C33 (string timers) | RUNSEC-C14, with DOMSEC-C03 as browser sink list | LANG-C49 is a position only |
| O07 | Throw and reject only Error objects | ASYNC-C18, LANG-C45 (Google), TYPES-C12 (caught values unknown) | ASYNC-C18 | TYPES-C12 is a distinct typing claim, keep as link |
| O08 | Node ESM facts: extensions, CJS globals, require(esm), JSON attribute, top-level await | LANG-C60 to C63 versus STRUCT-C11, C13, C16, C18 (also LANG-C58, C59 browser and format) | STRUCT (plan puts modules there); LANG keeps strict and module scope (C57) | agreement labels differ: LANG-C60 and C61 single-source, STRUCT-C11 and C16 consensus |
| O09 | Dependency-update cooldown | SUPPLY-C12 to C14, QUALITY-C46 | SUPPLY | QUALITY-C46 is a position with an open origin |
| O10 | `npm ci` in CI | SUPPLY-C04 (consensus), QUALITY-C42 | SUPPLY-C04 | |
| O11 | Trusted Types enforcement | DOMSEC-C15, FW-C48, FW-C06, RUNSEC-C19 (eval variant) | DOMSEC-C15 | FW claims are framework facts, keep as links |
| O12 | Framework escape hatches are the XSS entry | DOMSEC-C55, FW-C02 | DOMSEC-C55; FW-C02 holds the per-framework list | |
| O13 | Dependencies are fully trusted code | SUPPLY-C01, SUPPLY-C02, RUNSEC-C41 | SUPPLY-C01 | RUNSEC-C41 adds the in-process eval and write-access argument |
| O14 | JSON.parse and `__proto__` | RUNSEC-C13 (consensus), TYPES-C50 (inferred), TYPES-C49 (precision) | RUNSEC-C13 | TYPES-C49 pairs with LANG-C33 (BigInt in JSON) |
| O15 | Own-property test | STRUCT-C45, LANG-C55, RUNSEC-C07 | LANG-C55 | not an exact conflict: STRUCT-C45 accepts `hasOwnProperty`, the other two require `Object.hasOwn` |
| O16 | Freezing and shared mutable exports | LANG-C38, STRUCT-C02, DOMSEC-C52, RUNSEC-C09 | LANG-C38 for mechanics | |
| O17 | Cancellation with AbortSignal | ASYNC-C26 to C30, STRUCT-C53 (W3C TAG), RUNTIME-C06, C34 | ASYNC | |
| O18 | Secrets and tokens | RUNSEC-C46 to C48, SUPPLY-C38 | RUNSEC | |
| O19 | Prototype and built-in modification | LANG-C14 (Google), STRUCT-C44 (consensus), STRUCT-C43 | STRUCT-C44 | |

Conflicts not marked contested:
- LANG-C64 ("MDN advises avoiding" cycles) against STRUCT-C09 (contested: MDN avoid, Google ban, Node supported). Fold LANG-C64 into STRUCT-C09.
- LANG-C12 and STRUCT-C41 both mark the private-member convention contested, with different holder lists; keep STRUCT-C41 (fuller).
- Mild tension, not a conflict: STRUCT-C67 (minor releases break) against SUPPLY-C06 (pin or range, contested); link them.

### 3. Boundary items (101 claims)

Grouped by the owner the tag names (my normalisation of inconsistent tag spellings).

| owner named | n | ids |
|---|---|---|
| 01_lang | 6 | TYPES-C22, TYPES-C49, STRUCT-C02, STRUCT-C21, STRUCT-C45, STRUCT-C66 |
| 02_types | 12 | LANG-C33, LANG-C53, STRUCT-C25, C27, C28, C37, C38, C50, C51, C52, RUNSEC-C06, RUNSEC-C42 |
| 03_async | 16 | LANG-C45, TYPES-C12, STRUCT-C53, RUNSEC-C36, QUALITY-C10, RUNTIME-C06, C16, C19, C20, C23, C31, C32, C33, C34, C37, C40 |
| 04_struct | 3 | LANG-C15, LANG-C64, TYPES-C06 |
| 05_domsec | 6 | ASYNC-C33, RUNSEC-C19, FW-C02, C06, C45, C48 |
| 06_runsec | 20 | LANG-C34, C49; TYPES-C31, C32, C34, C50; ASYNC-C23, C40, C55; DOMSEC-C03; SUPPLY-C02, C38; QUALITY-C45; RUNTIME-C13, C15, C18, C42, C44, C51, C52 |
| 07_supply | 9 | TYPES-C07, STRUCT-C33, C34, C67, RUNSEC-C11, C21, C41, QUALITY-C42, C46 |
| 08_quality | 5 | LANG-C56, TYPES-C44, STRUCT-C30, RUNSEC-C18, C48 |
| 09_runtime | 7 | TYPES-C45, ASYNC-C04, C05, C34, C38, C47, STRUCT-C42 |
| web_architecture_guidelines | 16 | TYPES-C29, DOMSEC-C15, C26, C27, C28, C29, C35, C59, C60, RUNTIME-C39, C41, FW-C04, C07, C13, C14, C44 |
| none (version-scope note) | 1 | SUPPLY-C09 |
| python or cli guidelines | 0 | |

Flags (inferred; the owner decides):
- Sibling should hold, with an inter intentlink here: DOMSEC-C35 (token storage is session and token architecture), DOMSEC-C59 and C60 (JSONP, CORS policy), DOMSEC-C26, C28, C29 (CSP as deployment policy; DOMSEC-C27, the code that survives a strict CSP, stays), TYPES-C29 (server-side validation as architecture), RUNTIME-C39 and C41 (shutdown contract; the Node API side stays), FW-C44 (usage by rendering strategy), FW-C04 and C14 (CSP and CSRF deployment options), FW-C07 and C13 (framework advisories are facts; the update policy is deployment), FW-C45 (CSP and SRI prevalence).
- Split: DOMSEC-C15 and FW-C48 (code half here, header half in the sibling).
- Possible untagged boundary: STRUCT-C50 to C54 (declared API shape, W3C TAG) touches the sibling's API contract; FW-C21 to C30 release policies are framework facts.
- Intra-guideline tags are fine as inter intentlinks, but 84 of 101 point at a slot rather than at a different guideline; after consolidation they should become links between nodes of this guideline, not boundary tags.
- Tag spelling varies (`04_struct`, `04 STRUCT`, `STRUCT`, `web-architecture`, `../web_architecture_guidelines`, a leading `tier: T1;`): normalise.

### 4. Late candidates (41, deduplicated, none admitted)

Fills: the high gap the candidate would close, or "none". "Located" says whether the slot gave a URL.

| id | slot | title | url | proposed tier | located | fills |
|---|---|---|---|---|---|---|
| LC-01 | 01 | TC39 proposal-decimal repository | https://github.com/tc39/proposal-decimal | T1 | yes | none (G-M01) |
| LC-02 | 01 | MDN Using classes (guide) | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes | T1 | yes | none |
| LC-03 | 01 | MDN Data structures, primitive coercion | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures | T1 | yes | none |
| LC-04 | 01 | MDN Number.isNaN | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN | T1 | yes | none |
| LC-05 | 02 | MDN Object initializer, object literal syntax versus JSON | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer | T1 | yes | none |
| LC-06 | 02 | TypeScript Design Goals (wiki) | https://github.com/microsoft/TypeScript/wiki/TypeScript-Design-Goals | T1 restricted | yes | none (G-M06) |
| LC-07 | 02 | TypeScript issue 60582, unsound primitive-to-object assignment | https://github.com/microsoft/TypeScript/issues/60582 | T1 restricted | yes | none (G-M06) |
| LC-08 | 03 | Error Handling in Node.js, operational versus programmer errors (Pacheco) | not located | T2 | no | none (G-M07) |
| LC-09 | 03 | MDN Promise reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise | T1 | yes | none |
| LC-10 | 03 | RFC 9110, Retry-After (boundary: web architecture) | https://www.rfc-editor.org/rfc/rfc9110 | T1 | yes | none (G-M08) |
| LC-11 | 03 | Timeouts, retries and backoff with jitter (Amazon Builders' Library) | https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ | T3 | yes | none (G-M08); T3 cannot make a node known |
| LC-12 | 03 | MDN Scheduler.yield | https://developer.mozilla.org/en-US/docs/Web/API/Scheduler/yield | T1 | yes | none (G-M09) |
| LC-13 | 04 | Parnas 1979, Designing Software for Ease of Extension and Contraction | not located | T2 | no | none (G-M10) |
| LC-14 | 05 | MDN Element.setHTML | https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTML | T1 | yes | none (G-M11) |
| LC-15 | 05 | HTML Standard, navigate to a javascript: URL | https://html.spec.whatwg.org/multipage/browsing-the-web.html | T1 | yes | none (G-M11) |
| LC-16 | 05 | MDN page on the javascript: scheme | not located | T1 | no | none (G-M11) |
| LC-17 | 06 | ESLint rule no-eval (and no-implied-eval, no-new-func) | https://eslint.org/docs/latest/rules/no-eval | T1 | yes | none (grounds RUNSEC-C18) |
| LC-18 | 06 | Node.js API v8 (serialize, deserialize) | https://nodejs.org/api/v8.html | T1 | yes | G-H4 |
| LC-19 | 06 | Node.js API fs (realpath, symlinks) | https://nodejs.org/api/fs.html | T1 | yes | G-H5 |
| LC-20 | 06 | MDN JSON.parse | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse | T1 | yes | none |
| LC-21 | 06 | GitHub advisories for node-serialize (CVE-2017-5941) and js-yaml before 4 | https://github.com/advisories | T1 as facts | partly (ids unverified) | G-H4 |
| LC-22 | 07 | OpenSSF malicious-packages dataset | https://github.com/ossf/malicious-packages | T1 | yes | none (G-M18) |
| LC-23 | 07 | OSV malware records | https://osv.dev | T1 | yes | none (G-M18) |
| LC-24 | 07 | NSA, ODNI, CISA: Securing the Software Supply Chain, developer guide | not verified | T2 | no | none |
| LC-25 | 08 | OpenSSF Best Practices Badge criteria, Silver | https://www.bestpractices.dev/en/criteria/1 | T1 | yes | none |
| LC-26 | 08 | OpenSSF Best Practices Badge criteria, Gold | https://www.bestpractices.dev/en/criteria/2 | T1 | yes | none |
| LC-27 | 08 | An Empirical Study of Flaky Tests in JavaScript (Hashemi et al., ICSME 2022) | arXiv 2207.01047 (not fetched) | T2 | partly | none (G-M21) |
| LC-28 | 08 | Does mutation testing improve testing practices? (Petrovic et al., ICSE 2021) | not fetched | T2 | no | none |
| LC-29 | 08 | StrykerJS docs root | https://stryker-mutator.io/docs/ | T1 restricted | yes | none |
| LC-30 | 08 | SWEBOK v4, Software Testing knowledge area | not fetched | T2 | no | none |
| LC-31 | 09 | Rigorous Benchmarking in Reasonable Time (Kalibera and Jones, ISMM 2013) | not retrieved | T2 | no | none (G-M31) |
| LC-32 | 09 | Kubernetes Pod Lifecycle (boundary: web architecture) | https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ | T1 restricted | yes | none (G-M23) |
| LC-33 | 09 | Node.js async_context and diagnostics_channel API pages | https://nodejs.org/api/async_context.html ; https://nodejs.org/api/diagnostics_channel.html | T1 | yes | none |
| LC-34 | 09 | Node.js diagnostics guides (poor performance, live debugging) | https://nodejs.org/en/learn/diagnostics/poor-performance ; https://nodejs.org/en/learn/diagnostics/live-debugging | T1 | yes | none |
| LC-35 | 09 | Node.js cluster and child_process API pages | https://nodejs.org/api/cluster.html ; https://nodejs.org/api/child_process.html | T1 | yes | none (G-M23) |
| LC-36 | 09 | Node.js documentation on default heap limit in containers | not located | T1 | no | none (G-M22) |
| LC-37 | 10 | Lit templates and expressions | https://lit.dev/docs/templates/expressions/ | T1 restricted | yes | none (G-M24) |
| LC-38 | 10 | Solid documentation, JSX and rendering | https://docs.solidjs.com/ | T1 restricted | yes | none (G-M24) |
| LC-39 | 10 | HTTP Archive technology report data | https://httparchive.org/reports/cwv-tech | T2 as data | yes | none (G-M24) |
| LC-40 | 10 | TypeScript handbook, JSX | https://www.typescriptlang.org/docs/handbook/jsx.html | T1 | yes | none |
| LC-41 | 10 | htmx GitHub releases (year of 4.0.0) | https://github.com/bigskysoftware/htmx/releases | T1 restricted | yes | none |

Not counted, grounded: slot leads that only ask to re-read an already admitted source with a reader that does not truncate: ECMA-262 clause bodies (01, 02, 04, 06: SRC-027, SRC-001, SRC-122), Trusted Types section 5 (05, SRC-115), Node stream page (03, SRC-196). These are retries, not new sources. The slot 04 and 07 claim that "no late candidates" or no new search was run is noted: 07 ran no web search (its list is from the audit's gap list).

Count by slot: 01: 4, 02: 3, 03: 5, 04: 1, 05: 3, 06: 5, 07: 3, 08: 6, 09: 6, 10: 5 (total 41). Only 3 of 41 (LC-18, LC-19, LC-21) fill a high gap; G-H1, G-H2, G-H3 have no slot-reported candidate.

### 5. Threshold check

Command run from the guideline root: `python3 build/research/check_claims.py`. Summary line:

`total: 544 claims {'consensus': 193, 'single-source': 326, 'contested': 17, 'majority': 8}; errors 0; restricted citations 491`

Per slot (claims; consensus, majority, contested, single-source; single-source share):

| slot | claims | cons | maj | cont | single | share |
|---|---|---|---|---|---|---|
| 01_lang | 64 | 29 | 0 | 3 | 32 | 50% |
| 02_types | 50 | 19 | 1 | 1 | 29 | 58% |
| 03_async | 55 | 26 | 0 | 0 | 29 | 53% |
| 04_struct | 67 | 31 | 0 | 5 | 31 | 46% |
| 05_domsec | 60 | 33 | 0 | 3 | 24 | 40% |
| 06_runsec | 48 | 27 | 1 | 1 | 19 | 40% |
| 07_supply | 42 | 12 | 5 | 1 | 24 | 57% |
| 08_quality | 46 | 3 | 1 | 2 | 40 | 87% |
| 09_runtime | 63 | 11 | 0 | 0 | 52 | 83% |
| 10_frameworks | 49 | 2 | 0 | 1 | 46 | 94% |

- Mostly single-source (above half): 02, 03, 07, 08, 09, 10; 01 sits at half. Strongest corroboration: 05 and 06 (security, where OWASP, MDN and Node docs overlap) and 04.
- Reading, inferred: single-source here mostly means one T1 page per fact (tool documentation), which passes the plan's threshold only when the source is T1; the checker found no consensus claim below threshold. In 08, 09 and 10 single-source also means vendor or tool pages restricted to facts, so no node there can be `known` beyond tool behaviour.
- Open certainty claims: 6 (plain `open`) and 39 inferred in the claim tables; contested topics: 17 (slot 12 owns them).
- 491 restricted-citation notes are expected (184 of 321 register sources are restricted) and were not reviewed one by one here.

### 6. What the consolidation can trust

- Solid (grounded, consensus, T1): strict mode and equality, numbers and BigInt, promise handling and unhandled rejections, AbortSignal, DOM XSS sinks and Trusted Types mechanism, postMessage, prototype pollution, shell injection, lockfile and install-script facts, stream backpressure, process lifecycle, memory-leak diagnosis.
- Thin (single-source or inferred): path containment, framework comparison, testing strategy and coverage, benchmarking, engine internals, naming, state design.
- Absent: the five high gaps; every item in 1.2 marked medium.
- Audit action list (inferred): (a) extraction retry on SRC-078 and SRC-134 for G-H1, G-H3, G-M17; (b) audit the slot-11 leads for G-H1 to G-H3; (c) LC-18, LC-19, LC-21 for G-H4 and G-H5.

Read-in-full caveat for this slot: I read each slot's L1 to L2, gaps and late candidates in full and searched the claim tables by keyword; I did not read every claim row. SRC-078 was read only as a heading list through a fetch digest (tool-extracted).

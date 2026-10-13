# Skeleton: branch DEFENSE (step 5b)

Both graphs, the L1 node first, breadth-first. Ledger rows are numbers of `DEFENSE-nnn` rows in `ledger.md`. Links to other branches name the branch keyword; the integrator resolves them to uids.


## js-philosophy nodes

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| DEFENSE | Defense | Input from outside the trust boundary is hostile and every sink that interprets data as code, markup, query, path, destination or object key is dangerous; JavaScript sharpens this because a permissive language shares one runtime with untrusted code, so hostile data is narrowed at each sink and what slips through is contained by a second layer. | known | - |
| DEFENSE.DOM | Hostile data in the document | Hostile data must never become live markup, script or navigation in the page, and no verdict about it outlives the parse it was made for. | known | - |
| DEFENSE.ORIGIN | Boundaries between origins | Code and content from another origin stays behind explicit, verified boundaries, because every script in a page, first-party or not, holds the whole page's authority. | known | 001 |
| DEFENSE.INJECTION | Data becoming instruction or location | Hostile data must not become an instruction or a location for an interpreter outside the page: code, shell command, query, file path, network destination or serialized object. | known | - |
| DEFENSE.PROTOTYPE | Hostile keys and the shared object model | A permissive object model lets a hostile key rewrite what every object inherits; keys from outside are untrusted data, and the application, not the runtime, answers for them. | known | - |
| DEFENSE.SECRETS | Secrets and cryptographic primitives | Secrets are never committed and are drawn, compared, stored and logged only through audited platform mechanisms, since hand-rolled randomness, comparison or storage leaks them in ways nobody sees. | known | 002 |
| DEFENSE.HOST | The process under hostile input | One hostile input or one hostile peer must not exhaust the single-threaded process or reach what the process can reach; availability and exposure are part of safety. | known | - |
| DEFENSE.DOM.1 | Sources and sinks | Every injection is a flow from an attacker-controlled source to a dangerous sink, so both ends of every flow are audited. | known | 003 |
| DEFENSE.DOM.2 | A verdict holds only for its parse | A filter, sanitizer or gate decides about one parse of the data; safety is lost when a later parse differs, so verdicts are validated in the consumer. | known | 004 |
| DEFENSE.DOM.3 | Script tags are not the only way in | Disabling script execution or blocking handlers does not make markup safe; HTML alone can rewrite the page's names and behaviour. | known | 005-006 |
| DEFENSE.INJECTION.1 | Strings never become code | Data is never compiled or evaluated as code, whatever the API that offers it. | known | 007 |
| DEFENSE.INJECTION.2 | Commands are not built from input | A process is started without a shell and without input-chosen programs, so arguments stay arguments. | known | 008-009 |
| DEFENSE.INJECTION.3 | Queries keep code and data apart | A query reaches its engine as fixed text plus separately passed values, in every store, SQL or not. | known | 010-014 |
| DEFENSE.INJECTION.4 | Paths stay inside their base | A file location chosen from input is confined to a base directory, checked after resolution and used without a race. | known | 015 |
| DEFENSE.INJECTION.5 | Serialized data carries no behaviour | Data crossing a trust boundary is a pure data format, integrity-checked, and never revived into executable structures. | known | 016-017 |
| DEFENSE.INJECTION.6 | Destinations are chosen by the server | A server fetches only destinations it allows, checked at the address it will actually connect to. | known | 018-020 |
| DEFENSE.PROTOTYPE.1 | The application answers for keys | The runtime trusts application input, so validating attacker-influenced keys is the application's job and cannot be left to the platform. | known | 021 |
| DEFENSE.PROTOTYPE.2 | Pollution can be code execution | A polluted shared prototype is read later by legitimate code, so the worst outcome is remote code execution, not a logic error. | known | 022 |
| DEFENSE.HOST.1 | One request can stall the process | Single-threaded execution means CPU spent on one request is stolen from all; untrusted input must not control the cost of a match. | known | 023 |
| DEFENSE.HOST.2 | Heuristics are not proofs | A pattern check that flags or misses vulnerable code is a signal, never a proof either way. | known | 024 |
| DEFENSE.HOST.3 | Two parsers must agree | Where a proxy and a server read the same bytes, any disagreement is an attack; the defence belongs at both parsers. | known | 025 |

## pig-js-defaults nodes

| uid | name | intent | epistemic_state | ledger rows |
|---|---|---|---|---|
| PIG-JS.DEFENSE | Defense defaults | Treat all data from outside the trust boundary as hostile and every interpreting sink as dangerous; use the platform's safe API for each sink, check what cannot be avoided against an allowlist, enforce the check in the language runtime where an API exists, and add a second layer for what slips through. | known | - |
| PIG-JS.DEFENSE.DOM | Document sinks and sanitizing | Untrusted data enters the page as text or built nodes, never as parsed markup, script, event-handler attribute or script URL; the rare HTML that must be rendered is sanitized last and passed through Trusted Types enforced in the page. | known | - |
| PIG-JS.DEFENSE.ORIGIN | Origin boundaries | Messages, frames, third-party scripts and storage are each treated as an origin boundary: verified senders, sandboxed and separate-origin untrusted content, integrity-pinned external code, no secrets in storage, and code that a strict CSP can run. | known | - |
| PIG-JS.DEFENSE.INJECTION | Injection classes | Each interpreter outside the page gets its own safe channel: no code from strings, no shell, parameters for queries, confined resolved paths, pure-data serialization and allowlisted resolved destinations. | known | 026-027 |
| PIG-JS.DEFENSE.PROTOTYPE | Prototype pollution defaults | Untrusted keys never reach a nested write, a merge or an inherited-property read, and dictionaries keyed by untrusted strings are Maps, Sets or null-prototype objects. | known | - |
| PIG-JS.DEFENSE.SECRETS | Secrets and cryptography defaults | Randomness comes from the platform CSPRNG, comparison of secrets is constant-time through the built-in function, passwords use a slow salted function, secrets stay out of code and responses, and crypto designs are reviewed. | known | - |
| PIG-JS.DEFENSE.HOST | Node process hardening | The Node process limits what hostile input can exhaust and what hostile code can reach: bounded regex work, parser limits, a strict HTTP parser, no exposed inspector, a seat-belt permission model and trusted module directories. | known | - |
| PIG-JS.DEFENSE.DOM.1 | Markup and attribute sinks | Untrusted data is inserted as text or built nodes; HTML-parsing sinks, event-handler attributes and unquoted attribute values never carry it. | known | conflict: setAttribute unconditionally safe, OWASP DOM XSS sheet | unvalidated: MDN TrustedScript condition inferred | 028-034 |
| PIG-JS.DEFENSE.DOM.2 | URL and navigation sinks | A URL that selects code to load or a page to navigate to is a sink: only allowlisted or Trusted values reach it. | known | - |
| PIG-JS.DEFENSE.DOM.3 | Sanitizing HTML | Untrusted HTML that must be rendered goes through the native Sanitizer API where available, otherwise a reputable library, immediately before insertion and never modified afterwards. | known | conflict: library-first sanitizing, OWASP and MDN naming DOMPurify | unvalidated: advice to keep the sanitizer current is inferred | 035-040 |
| PIG-JS.DEFENSE.DOM.4 | Trusted Types enforcement | Injection sinks accept only typed values produced by named policies, rolled out in report-only mode, then enforced; Trusted Types is a gate, not a sanitizer. | known | conflict: default policy as normal practice, Roth et al. USENIX 2024, for third-party code | 041-050 |
| PIG-JS.DEFENSE.DOM.5 | DOM clobbering | Application state never lives on window or document, named-property reads are type-checked, and sanitizers neutralize id and name. | known | 051-054 |
| PIG-JS.DEFENSE.DOM.6 | Framework output and escape hatches | Framework default encoding is relied on and every documented escape hatch is a sink that receives sanitized input only. | known | - |
| PIG-JS.DEFENSE.ORIGIN.1 | Cross-origin messages | A page listens only for messages it expects, verifies origin by exact match, validates every message and names an exact target origin. | known | 055-059 |
| PIG-JS.DEFENSE.ORIGIN.2 | Frames and window links | Untrusted and vendor content lives in sandboxed iframes from a separate origin; target=_blank links carry rel=noopener noreferrer explicitly. | known | conflict: explicit rel unnecessary because the HTML Standard implies noopener, HTML Standard | 060-064 |
| PIG-JS.DEFENSE.ORIGIN.3 | Third-party and service worker code | External scripts are pinned and integrity-checked, a data layer is not mistaken for a sandbox, and service workers come only from the own origin. | known | 065-069 |
| PIG-JS.DEFENSE.ORIGIN.4 | Web storage | Web Storage holds no secrets because every script of the origin reads it, and what is read from it or from messages is validated. | known | unvalidated: validation rule inferred from a T2 finding and a T3 catalogue | 070-072 |
| PIG-JS.DEFENSE.ORIGIN.5 | CSP-ready code and policy handoff | Code runs under a strict CSP without exceptions; the policy and its deployment, CORS and JSONP rules belong to web_architecture. | known | deferred: policy deployment owned by web_architecture | 073-080 |
| PIG-JS.DEFENSE.INJECTION.1 | No code from strings | Browser and Node code never compiles untrusted strings, whether through eval, Function, string timers or node:vm, and lint rules enforce it. | known | - |
| PIG-JS.DEFENSE.INJECTION.2 | OS commands | A child process receives a program and an argument array, never a shell string built from input. | known | 081-082 |
| PIG-JS.DEFENSE.INJECTION.3 | SQL and NoSQL queries | Values go through the driver's parameter channel, MongoDB filters take typed scalars, server-side JavaScript in the database is off. | known | conflict: escape dynamic identifiers with pg-format, node-postgres docs | 083-088 |
| PIG-JS.DEFENSE.INJECTION.4 | File paths and archives | A path from input is resolved and checked inside its base, archive entries never choose their location, and the file is opened without a prior check. | known | unvalidated: Node-specific recipe inferred, one T2 ground for canonicalization | - |
| PIG-JS.DEFENSE.INJECTION.5 | Deserialization | Untrusted data is parsed with data-only parsers; code-reviving serializers are rejected. | known | - |
| PIG-JS.DEFENSE.INJECTION.6 | Outbound requests | Outbound requests go to allowlisted hosts, are connected to the validated address and follow no unvetted redirects. | known | - |
| PIG-JS.DEFENSE.PROTOTYPE.1 | Key writes and reads | No nested write with untrusted keys, no unfiltered merge, own-property reads, no __proto__ accessor. | known | 089-092 |
| PIG-JS.DEFENSE.PROTOTYPE.2 | Dictionaries for untrusted keys | Map or Set first, null-prototype objects when a plain object is required, parsed JSON keys untrusted. | known | 093-095 |
| PIG-JS.DEFENSE.PROTOTYPE.3 | Hardening and evidence | Application configuration is frozen, built-ins are locked down only where tested, and --disable-proto is never the only defence. | known | conflict: never modify built-ins, SUBSET branch | 096-099 |
| PIG-JS.DEFENSE.SECRETS.1 | Randomness | Tokens and keys come from the platform CSPRNG with at least 128 bits; Math.random and non-v4 UUIDs are rejected. | known | 100-102 |
| PIG-JS.DEFENSE.SECRETS.2 | Cryptographic API use | SubtleCrypto designs are reviewed by a knowledgeable person; authenticated encryption is the position of the one source that states it. | known | unvalidated: single T1 source; Node crypto page truncated in every fetch | 103-104 |
| PIG-JS.DEFENSE.SECRETS.3 | Password storage | Passwords use Argon2id, else scrypt, bcrypt or PBKDF2 at OWASP minimums. | known | unvalidated: quote tool-extracted | unvalidated: single T1 position | 105-106 |
| PIG-JS.DEFENSE.SECRETS.4 | Constant-time comparison | Secrets are compared with timingSafeEqual on equal-length digests; no hand-written constant-time code, no BigInt for crypto. | known | 107-113 |
| PIG-JS.DEFENSE.SECRETS.5 | Secret handling | Secrets stay out of code, environment variables are a weaker fallback, and detection and rotation are routine. | known | 114-115 |
| PIG-JS.DEFENSE.SECRETS.6 | Leakage through output and memory | Errors reach clients generically, uninitialized Buffers and diagnostic reports do not leak, and a secure heap limits shared-host exposure. | known | 116-120 |
| PIG-JS.DEFENSE.HOST.1 | Permission model | The permission model is a seat belt for trusted code with narrow grants, known symlink and descriptor limits and a patched Node. | known | conflict: permission model contains hostile or compromised dependencies, Node best-practices page | 121-124 |
| PIG-JS.DEFENSE.HOST.2 | Inspector exposure | The inspector is never public, never in production and never activated by SIGUSR1. | known | unvalidated: single T1 source, quote tool-extracted | 125 |
| PIG-JS.DEFENSE.HOST.3 | HTTP parsing and smuggling | The strict HTTP parser stays on and the front end normalizes ambiguous requests. | known | 126-128 |
| PIG-JS.DEFENSE.HOST.4 | Regex cost | Input length and repetition are bounded, nested quantifiers avoided, a non-backtracking engine preferred where one exists. | known | 129-133 |
| PIG-JS.DEFENSE.HOST.5 | Parser resource limits | Parsers have size, depth and number limits and Node is patched against parser hash collisions. | known | unvalidated: single T2 source for the Node patch rule | 134-135 |
| PIG-JS.DEFENSE.HOST.6 | Module load path | Directories Node loads modules from are trusted and hardened. | known | unvalidated: single T1 source | 136 |
| PIG-JS.DEFENSE.DOM.2.1 | Script URL sinks | script.src, Worker constructors, importScripts and serviceWorker.register receive only allowlisted or Trusted URLs. | known | 137 |
| PIG-JS.DEFENSE.DOM.2.2 | Redirect targets | Automatic redirects go only to destinations on an allowlist. | known | unvalidated: quote tool-extracted | unvalidated: mechanism from a T3 catalogue only | 138 |
| PIG-JS.DEFENSE.DOM.2.3 | URL validation by parsing | URLs are validated by parsing and allowlisting scheme and origin rather than by substring tests. | undecided | missing: no admitted source states the scheme and origin allowlist rule or the javascript: scheme case | 139 |
| PIG-JS.DEFENSE.DOM.6.1 | Escape hatches | Escape hatches of React, Angular, Lit, Vue and Svelte are treated as sinks needing sanitized input; the per-framework documentation facts are recorded here. | known | 140-146 |
| PIG-JS.DEFENSE.DOM.6.2 | Framework default encoding | Angular and Vue document their default encoding; rely on it for interpolation and bindings. | known | unvalidated: single T1 source, vendor facts only | 147-148 |
| PIG-JS.DEFENSE.DOM.6.3 | htmx hardening facts | htmx documents escaping, scrubbing, hx-disable and configuration options as its security tools; recorded as facts. | known | unvalidated: single T1 source, vendor facts only | 149-151 |
| PIG-JS.DEFENSE.INJECTION.1.1 | Strings as code | Untrusted strings never reach eval, Function or string timers; JSON.parse replaces eval for data. | known | 152-157 |
| PIG-JS.DEFENSE.INJECTION.1.2 | The vm module | node:vm is never used to run untrusted code. | known | unvalidated: single T1 source, quote tool-extracted | 158-159 |
| PIG-JS.DEFENSE.INJECTION.4.1 | Containment check | A path is canonicalized, symlinks resolved, and only then compared to the base directory. | known | unvalidated: Node-specific recipe inferred, one T2 ground for canonicalization | 160-165 |
| PIG-JS.DEFENSE.INJECTION.4.2 | Archive extraction | Archive entry names and symlinks never decide where files land. | known | 166-167 |
| PIG-JS.DEFENSE.INJECTION.4.3 | Check then use | A file is opened directly and errors handled, never pre-checked. | known | unvalidated: single T1 source on a v10 page, extension inferred | 168 |
| PIG-JS.DEFENSE.INJECTION.4.4 | Node containment recipe | The resolve, realpath and separator-terminated prefix recipe is not stated by any admitted source. | undecided | missing: no admitted source states the Node containment recipe | 169 |
| PIG-JS.DEFENSE.INJECTION.5.1 | Structured clone | Structured clone is a data-only copy; its fitness for untrusted input is open. | known | 170 |
| PIG-JS.DEFENSE.INJECTION.5.2 | YAML and legacy serializers | Untrusted YAML goes to js-yaml 4 or later; node-serialize unserialize never sees untrusted input. | known | unvalidated: single T1 source, facts only, advice partly inferred | 171-172 |
| PIG-JS.DEFENSE.INJECTION.5.3 | v8.deserialize | Whether v8.deserialize is safe for untrusted buffers is not grounded. | undecided | missing: no admitted source states whether v8.deserialize is safe for untrusted buffers | 173 |
| PIG-JS.DEFENSE.INJECTION.6.1 | Destination rules | Hosts are matched against an allowlist, URLs are parsed with the WHATWG URL class, and a deny-list is the weaker fallback. | known | 174-176 |
| PIG-JS.DEFENSE.INJECTION.6.2 | Connection to the validated address | The address is resolved once, checked, and connected to; DNS rebinding is the attack this closes. | known | unvalidated: pinned-connection recipe inferred from three rows | 177-179 |
| PIG-JS.DEFENSE.INJECTION.6.3 | Redirect handling | Redirects are off by default and revalidated when followed. | known | 180-181 |
| PIG-JS.DEFENSE.INJECTION.6.4 | Node fetch redirect semantics | How Node's fetch handles redirect manual and redirect limits is not grounded. | undecided | missing: no admitted source states Node fetch redirect semantics | 182 |

## Intentlinks inside the branch, js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | DEFENSE.DOM.2 | DEFENSE.DOM.1 | requires | A verdict about a filter or gate presupposes the flow it guards, so the flow is known before the verdict is trusted. |
| 2 | DEFENSE.ORIGIN | DEFENSE.DOM.1 | dataflow | Messages, storage reads and third-party output are sources whose data ends at the same DOM sinks. |
| 3 | DEFENSE.INJECTION.5 | DEFENSE.INJECTION.1 | requires | Reviving types or functions from serialized data is building code from strings, so the code rule must hold first. |
| 4 | DEFENSE.PROTOTYPE.2 | DEFENSE.INJECTION.1 | dataflow | A polluted shared prototype feeds gadgets that compile or run attacker-shaped values, ending in code execution. |

## Intentlinks inside the branch, pig-js-defaults

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.DEFENSE.DOM.1 | PIG-JS.DEFENSE.DOM.3 | requires | HTML that must be rendered is handed to the sanitizer rather than inserted through a sink. |
| 2 | PIG-JS.DEFENSE.DOM.4 | PIG-JS.DEFENSE.DOM.3 | requires | A Trusted Types createHTML policy wraps a vetted sanitizer; the gate is only as good as that function. |
| 3 | PIG-JS.DEFENSE.DOM.5 | PIG-JS.DEFENSE.DOM.3 | requires | The sanitizer neutralizes id and name, which is the HTML-only injection route to clobbering. |
| 4 | PIG-JS.DEFENSE.DOM.6.1 | PIG-JS.DEFENSE.DOM.1 | refines | A framework escape hatch is a markup sink and obeys the sink rules. |
| 5 | PIG-JS.DEFENSE.ORIGIN.1 | PIG-JS.DEFENSE.DOM.1 | dataflow | Validated message data is still a source that ends at DOM sinks. |
| 6 | PIG-JS.DEFENSE.ORIGIN.4 | PIG-JS.DEFENSE.DOM.1 | dataflow | Data read from web storage is a source that ends at DOM sinks. |
| 7 | PIG-JS.DEFENSE.ORIGIN.5 | PIG-JS.DEFENSE.DOM.1 | requires | Strict-CSP code needs addEventListener and no inline handlers, which the markup sink rules already enforce. |
| 8 | PIG-JS.DEFENSE.INJECTION.1.1 | PIG-JS.DEFENSE.DOM.4 | requires | In browsers string compilation is gated by Trusted Types and the trusted-types-eval keyword. |
| 9 | PIG-JS.DEFENSE.DOM.2.3 | PIG-JS.DEFENSE.INJECTION.6.1 | dataflow | Parsing a URL with the standard parser before judging scheme and origin is one rule in browser and server. |
| 10 | PIG-JS.DEFENSE.INJECTION.4.1 | PIG-JS.DEFENSE.INJECTION.4.3 | requires | A containment check is sound only if the file is opened without a gap between check and use. |
| 11 | PIG-JS.DEFENSE.INJECTION.6.2 | PIG-JS.DEFENSE.INJECTION.6.1 | requires | Pinning the connection to a validated address applies to hosts that passed the destination rules. |
| 12 | PIG-JS.DEFENSE.INJECTION.6.3 | PIG-JS.DEFENSE.INJECTION.6.2 | requires | Each redirect target is checked by the same resolved-address validation. |
| 13 | PIG-JS.DEFENSE.INJECTION.6.2 | PIG-JS.DEFENSE.HOST.2 | dataflow | The rebinding attack closed for outbound requests also reaches a local inspector. |
| 14 | PIG-JS.DEFENSE.PROTOTYPE.2 | PIG-JS.DEFENSE.INJECTION.5 | dataflow | Keys in parsed JSON reach merges and assignments, which is where pollution happens. |
| 15 | PIG-JS.DEFENSE.HOST.1 | PIG-JS.DEFENSE.INJECTION.4.1 | requires | Permission grants are paths with documented symlink and prefix limits, so containment checks remain needed. |
| 16 | PIG-JS.DEFENSE.HOST.4 | PIG-JS.DEFENSE.HOST.5 | requires | Bounding input length before matching relies on size limits at the parsing boundary. |

## Inter links, pig-js-defaults to js-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.DEFENSE | js-philosophy:DEFENSE | refines | The default renders the principle in JavaScript. |
| 2 | PIG-JS.DEFENSE.DOM | js-philosophy:DEFENSE.DOM | refines | The default renders the principle in JavaScript. |
| 3 | PIG-JS.DEFENSE.ORIGIN | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 4 | PIG-JS.DEFENSE.INJECTION | js-philosophy:DEFENSE.INJECTION | refines | The default renders the principle in JavaScript. |
| 5 | PIG-JS.DEFENSE.PROTOTYPE | js-philosophy:DEFENSE.PROTOTYPE | refines | The default renders the principle in JavaScript. |
| 6 | PIG-JS.DEFENSE.SECRETS | js-philosophy:DEFENSE.SECRETS | refines | The default renders the principle in JavaScript. |
| 7 | PIG-JS.DEFENSE.HOST | js-philosophy:DEFENSE.HOST | refines | The default renders the principle in JavaScript. |
| 8 | PIG-JS.DEFENSE.DOM.1 | js-philosophy:DEFENSE.DOM.1 | refines | The default renders the principle in JavaScript. |
| 9 | PIG-JS.DEFENSE.DOM.3 | js-philosophy:DEFENSE.DOM.2 | refines | The default renders the principle in JavaScript. |
| 10 | PIG-JS.DEFENSE.DOM.4 | js-philosophy:DEFENSE.DOM.2 | refines | The default renders the principle in JavaScript. |
| 11 | PIG-JS.DEFENSE.DOM.5 | js-philosophy:DEFENSE.DOM.3 | refines | The default renders the principle in JavaScript. |
| 12 | PIG-JS.DEFENSE.ORIGIN.2 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 13 | PIG-JS.DEFENSE.ORIGIN.3 | js-philosophy:DEFENSE.ORIGIN | refines | The default renders the principle in JavaScript. |
| 14 | PIG-JS.DEFENSE.INJECTION.1 | js-philosophy:DEFENSE.INJECTION.1 | refines | The default renders the principle in JavaScript. |
| 15 | PIG-JS.DEFENSE.INJECTION.2 | js-philosophy:DEFENSE.INJECTION.2 | refines | The default renders the principle in JavaScript. |
| 16 | PIG-JS.DEFENSE.INJECTION.3 | js-philosophy:DEFENSE.INJECTION.3 | refines | The default renders the principle in JavaScript. |
| 17 | PIG-JS.DEFENSE.INJECTION.4 | js-philosophy:DEFENSE.INJECTION.4 | refines | The default renders the principle in JavaScript. |
| 18 | PIG-JS.DEFENSE.INJECTION.5 | js-philosophy:DEFENSE.INJECTION.5 | refines | The default renders the principle in JavaScript. |
| 19 | PIG-JS.DEFENSE.INJECTION.6 | js-philosophy:DEFENSE.INJECTION.6 | refines | The default renders the principle in JavaScript. |
| 20 | PIG-JS.DEFENSE.PROTOTYPE.1 | js-philosophy:DEFENSE.PROTOTYPE.1 | refines | The default renders the principle in JavaScript. |
| 21 | PIG-JS.DEFENSE.PROTOTYPE.2 | js-philosophy:DEFENSE.PROTOTYPE.1 | refines | The default renders the principle in JavaScript. |
| 22 | PIG-JS.DEFENSE.PROTOTYPE.3 | js-philosophy:DEFENSE.PROTOTYPE.2 | refines | The default renders the principle in JavaScript. |
| 23 | PIG-JS.DEFENSE.SECRETS.5 | js-philosophy:DEFENSE.SECRETS | refines | The default renders the principle in JavaScript. |
| 24 | PIG-JS.DEFENSE.HOST.3 | js-philosophy:DEFENSE.HOST.3 | refines | The default renders the principle in JavaScript. |
| 25 | PIG-JS.DEFENSE.HOST.4 | js-philosophy:DEFENSE.HOST.1 | refines | The default renders the principle in JavaScript. |
| 26 | PIG-JS.DEFENSE.HOST.4 | js-philosophy:DEFENSE.HOST.2 | refines | The default renders the principle in JavaScript. |

## Inter links, js-philosophy to python-kb-philosophy

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | DEFENSE | python-kb-philosophy:DEFENSIVE | refines | Defensive design (assume failure, validate at boundaries, trust after validation) is the language-neutral base; this branch adds the JavaScript hazards. |
| 2 | DEFENSE.INJECTION | python-kb-philosophy:DEFENSIVE | refines | Boundary validation and fail-fast apply to every interpreter the data can reach. |

## Proposed links to other branches (the integrator resolves the keyword)

| # | from | to | type | sentence |
|---|---|---|---|---|
| 1 | PIG-JS.DEFENSE.PROTOTYPE.1 | SUBSET | refines | The own-property read (Object.hasOwn, LANG-C55) is owned by SUBSET; this node holds the security reason for untrusted keys. |
| 2 | PIG-JS.DEFENSE.PROTOTYPE.3 | SUBSET | conflicts | Lockdown of built-in prototypes in high-sensitivity code conflicts with never modifying built-ins (LANG-C14), scope: hardening versus patching; freeze is shallow (LANG-C38) in both. |
| 3 | PIG-JS.DEFENSE.PROTOTYPE.3 | STRUCTURE | refines | Frozen application configuration and exported mutable state (STRUCT-C01 to C03) rest on the same shallow-freeze fact. |
| 4 | PIG-JS.DEFENSE.PROTOTYPE.3 | DEPENDENCIES | requires | Third-party pollution flaws (RUNSEC-C11 evidence) need the update policy owned by DEPENDENCIES. |
| 5 | PIG-JS.DEFENSE.INJECTION.1.1 | VERIFICATION | requires | The no-eval, no-implied-eval and no-new-func rules are enforced by the lint rule set owned by VERIFICATION. |
| 6 | PIG-JS.DEFENSE.SECRETS.5 | VERIFICATION | requires | Secret detection before commit is a gate owned by VERIFICATION. |
| 7 | PIG-JS.DEFENSE.SECRETS.5 | DEPENDENCIES | refines | Secrets in published package contents (SUPPLY-C38, SRVSEC-C62) are the same leak class. |
| 8 | PIG-JS.DEFENSE.SECRETS.6 | RUNTIME | refines | Buffer.allocUnsafe is a measured speed choice in RUNTIME; this node states the leakage cost. |
| 9 | PIG-JS.DEFENSE.HOST.1 | DEPENDENCIES | refines | Dependencies are fully trusted code and give no in-process isolation (SUPPLY-C01, RUNSEC-C41); the permission model is a seat belt on top. |
| 10 | PIG-JS.DEFENSE.HOST.4 | CONTROL | requires | A blocked event loop is the failure CONTROL's timeout and load rules contain. |
| 11 | PIG-JS.DEFENSE.HOST.5 | CONTRACTS | refines | Parser limits are part of parsing untrusted data at every trust boundary. |
| 12 | PIG-JS.DEFENSE.HOST.6 | DEPENDENCIES | requires | Module resolution trust rests on the dependency and install policy of DEPENDENCIES. |
| 13 | PIG-JS.DEFENSE.INJECTION.4.3 | CONTROL | requires | Handling the error of a direct open is the explicit-failure rule of CONTROL. |
| 14 | PIG-JS.DEFENSE.INJECTION.5 | CONTRACTS | requires | Parsing untrusted data into validated shapes is the boundary rule of CONTRACTS. |
| 15 | PIG-JS.DEFENSE.DOM.6 | DEPENDENCIES | dataflow | Framework security facts recorded here feed the framework choice evidence in DEPENDENCIES. |

## Planned boundary links to web_architecture (planned, not created)

| # | from | note |
|---|---|---|
| 1 | PIG-JS.DEFENSE.DOM.4 | code half here, CSP header and policy deployment in web_architecture (DOMSEC-C15, FW-C48) |
| 2 | PIG-JS.DEFENSE.ORIGIN.4 | token and session architecture in web_architecture (DOMSEC-C35) |
| 3 | PIG-JS.DEFENSE.ORIGIN.5 | CSP deployment, JSONP, CORS and framework CSP and CSRF options in web_architecture (DOMSEC-C26, C28, C29, C59, C60, FW-C04, FW-C14) |
| 4 | PIG-JS.DEFENSE.INJECTION.6.1 | cloud metadata service configuration in web_architecture (SRVSEC-C38) |
| 5 | PIG-JS.DEFENSE.HOST.3 | front-end proxy normalization is deployment, with the Node parser side kept here (SRVSEC-C58) |

## Judge records

One per defaults node holding a decision. Fields: positions, forces, decision, rejected with the condition under which each would win.

**PIG-JS.DEFENSE.INJECTION** Injection classes
- Positions: Document dangerous functionality and encode logs (ASVS 15.1.5, 16.4.1). Claims RUNSEC-C45, SRVSEC-C46, SRVSEC-C61.
- Forces: Review visibility against documentation effort.
- Decision: Document where deserialization, dynamic code, raw parsing and memory manipulation are used; encode data in every logging component.
- Rejected: No documentation of dangerous functionality: loses under ASVS Level 3 verification.

**PIG-JS.DEFENSE.DOM.1** Markup and attribute sinks
- Positions: Text-only insertion (OWASP, MDN, ASVS) against sanitizer-everywhere; setAttribute as safe construction (OWASP DOM XSS sheet) against setAttribute as a TrustedScript sink (MDN). Claims DOMSEC-C01, C02, C04, C05, C25.
- Forces: Safety against convenience of building markup from strings; encoding is context specific and unreliable in script and handler contexts.
- Decision: Insert text with textContent or built nodes, keep untrusted data out of HTML sinks, script, style and event-handler attributes, quote attributes, and never set event-handler attributes from untrusted data.
- Rejected: setAttribute as unconditionally safe (OWASP DOM XSS sheet): loses where the attribute name is an event handler, the condition inferred and to be read verbatim. Encoding into script contexts: rejected by OWASP itself as unreliable.

**PIG-JS.DEFENSE.DOM.3** Sanitizing HTML
- Positions: Native setHTML (MDN, HTML Standard) against sanitizer library (OWASP names DOMPurify) against hand-written filters. Claims DOMSEC-C08, C09, C11, C12, C14, C23.
- Forces: Safety against availability: setHTML is limited-availability, a library is a security-critical dependency with a bypass history.
- Decision: setHTML where available, a reputable library as fallback, sanitize last, never modify afterwards, treat Unsafe-suffixed methods as sinks.
- Rejected: Library-first: wins where the target browsers lack setHTML, which is the stated condition for the fallback. Hand-written sanitizing: rejected by OWASP as hard to get right.

**PIG-JS.DEFENSE.DOM.4** Trusted Types enforcement
- Positions: Enforce with named policies (MDN, W3C, DOMSEC-C15 and C17) against default policy as normal practice (Roth et al., USENIX 2024). Claims DOMSEC-C15, C16, C17, C18, C19, RUNSEC-C19, FW-C48.
- Forces: Strength of the gate against the cost of retrofitting third-party code that cannot pass typed values.
- Decision: Enforce require-trusted-types-for 'script', named policies, report-only rollout, trusted-types-eval in place of unsafe-eval, no sanitizer reuse for script sinks.
- Rejected: Default policy as normal practice: wins only for third-party code that cannot be changed, as MDN and web.dev already allow. Trusted Types as sanitizer: refuted by MDN.

**PIG-JS.DEFENSE.DOM.5** DOM clobbering
- Positions: Local variables and type checks (OWASP clobbering sheet, ASVS 3.2.3) against globals on window. Claims DOMSEC-C49, C50, C51.
- Forces: Safety against the habit of globals.
- Decision: No globals on window or document, instanceof checks, neutralize id and name when sanitizing.
- Rejected: Globals on window: wins nowhere once untrusted HTML is possible.

**PIG-JS.DEFENSE.ORIGIN.1** Cross-origin messages
- Positions: Verified origin by exact match, validated payload, exact target (MDN, HTML Standard, ASVS 3.5.5, OWASP). Claims DOMSEC-C30 to C34.
- Forces: Safety against open messaging between windows.
- Decision: No listener without need, exact origin match, validate syntax and type, exact targetOrigin for confidential data (MDN says always).
- Rejected: Substring or indexOf origin tests: rejected by OWASP as very insecure. Wildcard target: loses when any confidential data is sent.

**PIG-JS.DEFENSE.ORIGIN.2** Frames and window links
- Positions: Sandboxed iframe, separate origin, explicit noopener (MDN, OWASP) against implied noopener only (HTML Standard). Claims DOMSEC-C43 to C47.
- Forces: Containment strength against markup brevity.
- Decision: Sandbox untrusted content, separate origin, no allow-scripts with allow-same-origin, explicit rel=noopener noreferrer.
- Rejected: Implied noopener only (HTML Standard): wins on browsers that implement the default, so explicit rel is harmless extra. Sandbox without separate origin: loses if the content can be opened outside the frame.

**PIG-JS.DEFENSE.ORIGIN.3** Third-party and service worker code
- Positions: Pin and SRI, separate origin for vendor scripts, own-origin service workers (MDN, W3C, OWASP). Claims DOMSEC-C38 to C40, C42, C58.
- Forces: Integrity of third-party code against the convenience of unpinned vendor updates.
- Decision: Pin versions with SRI (sha384 or stronger plus crossorigin), do not treat a data layer as a sandbox, register service workers from own origin only.
- Rejected: Unpinned third-party scripts: wins nowhere for pages with authority over user data.

**PIG-JS.DEFENSE.ORIGIN.4** Web storage
- Positions: No secrets in Web Storage (OWASP, MDN, DOMSEC-C36) against tokens in storage for convenience. DOMSEC-C35 is owned by web_architecture.
- Forces: Safety against client-side session convenience.
- Decision: Web Storage holds no secrets; validate what is read from it and from messages.
- Rejected: Tokens in localStorage: rejected by OWASP session management as always readable by script.

**PIG-JS.DEFENSE.ORIGIN.5** CSP-ready code and policy handoff
- Positions: Strict-CSP-compatible code (CSP3, OWASP) against inline script and handlers; policy design is owned by web_architecture. Claims DOMSEC-C27, C28 and the deferred rows.
- Forces: Safety against inline-code convenience.
- Decision: No inline script, no inline handlers, no string eval, so the strict policy can be deployed.
- Rejected: Domain-allowlist CSP as XSS protection: refuted by a 2016 measurement of 94.72 percent bypassable policies; the nonce or hash policy itself belongs to web_architecture.

**PIG-JS.DEFENSE.INJECTION.2** OS commands
- Positions: spawn or execFile with an argument array against exec with a sanitized string (Node docs, OWASP, Synode). Claims RUNSEC-C23, C24.
- Forces: Safety against convenience of shell strings.
- Decision: Argument array, no shell option with input; prefer built-in library functions.
- Rejected: exec with escaped input: wins where a shell feature is truly needed, and then OWASP's allowlist and least privilege apply.

**PIG-JS.DEFENSE.INJECTION.3** SQL and NoSQL queries
- Positions: Parameters (OWASP, ASVS 1.2.4, driver docs) against escaping (node-postgres pg-format for identifiers, OWASP discouraged); validated scalars for MongoDB. Claims SRVSEC-C16, C18, C20, C21, C24 to C27.
- Forces: Strength of the separation against the need for dynamic identifiers.
- Decision: Parameterized values always; identifiers by fixed allowlist or redesign; MongoDB scalar types, no client operators, no client server-side JavaScript.
- Rejected: pg-format escaping: wins only for names that are genuinely dynamic, such as DDL.

**PIG-JS.DEFENSE.PROTOTYPE.1** Key writes and reads
- Positions: Reject prototype keys, own-property reads, avoid __proto__ (MDN, OWASP, Node threat model). Claims RUNSEC-C02, C03, C07, C12.
- Forces: Safety against terse dynamic code.
- Decision: No untrusted nested writes or merges, Object.hasOwn, avoid __proto__ in new code.
- Rejected: hasOwnProperty on the instance: SUBSET owns the choice of Object.hasOwn.

**PIG-JS.DEFENSE.PROTOTYPE.2** Dictionaries for untrusted keys
- Positions: Map or Set first, Object.create(null) second, literal __proto__ null last (OWASP, MDN, ASVS 15.3.6). Claims RUNSEC-C04, C05, C13, TYPES-C50.
- Forces: Strength of the defence against keeping plain-object ergonomics.
- Decision: Map or Set for untrusted-keyed dictionaries; Object.create(null) when an object is required.
- Rejected: Plain object with filtered keys: weaker, allowed with key rejection.

**PIG-JS.DEFENSE.PROTOTYPE.3** Hardening and evidence
- Positions: Freeze app-owned configuration; lockdown only where tested (MDN, OWASP) against never modifying built-ins (SUBSET). Claims DOMSEC-C52, RUNSEC-C08, C09, C11.
- Forces: Hardening depth against breakage of polyfills and libraries.
- Decision: Freeze configuration (shallow), lock down only in high-sensitivity tested environments, never rely on --disable-proto alone.
- Rejected: Never freeze built-ins: wins for general code, loses in high-sensitivity code where lockdown is tested.

**PIG-JS.DEFENSE.SECRETS.1** Randomness
- Positions: CSPRNG with 128 bits (ASVS 11.5.1, MDN, OWASP) against Math.random. Claims SRVSEC-C01 to C04.
- Forces: Unpredictability against convenience.
- Decision: crypto.randomBytes, randomInt, randomUUID in Node; getRandomValues in browsers; version 4 UUIDs only.
- Rejected: Math.random: refuted by MDN. Version 1 UUIDs: embed time and MAC.

**PIG-JS.DEFENSE.SECRETS.2** Cryptographic API use
- Positions: Review of SubtleCrypto designs (MDN); authenticated mode (OWASP only). Claims SRVSEC-C12, C13, C14.
- Forces: Safety against developer discretion on low-level crypto.
- Decision: Have a knowledgeable person review any SubtleCrypto design.
- Rejected: Self-reviewed crypto: refuted by MDN's warning.

**PIG-JS.DEFENSE.SECRETS.3** Password storage
- Positions: Argon2id first, scrypt, bcrypt, PBKDF2 for FIPS (OWASP Password Storage). Claims SRVSEC-C10, C11.
- Forces: Brute-force cost against compatibility constraints.
- Decision: Argon2id at 19 MiB, 2 iterations, parallelism 1, with the OWASP fallbacks by condition.
- Rejected: bcrypt, scrypt, PBKDF2: acceptable by OWASP's conditions, FIPS or legacy.

**PIG-JS.DEFENSE.SECRETS.4** Constant-time comparison
- Positions: timingSafeEqual on equal-length digests (Node docs, ASVS 11.2.4, CWE-208) against === comparison. Claims SRVSEC-C05 to C09, LANG-C34.
- Forces: Side-channel resistance against code simplicity.
- Decision: Use the built-in constant-time comparison and keep surrounding code branch-free on secrets; no hand-written constant-time JavaScript.
- Rejected: Ordinary comparison: leaks through timing.

**PIG-JS.DEFENSE.SECRETS.5** Secret handling
- Positions: No hardcoded secrets (OWASP, NDSS 2019 evidence) with environment variables as a weaker fallback. Claims RUNSEC-C47, C48.
- Forces: Safety against operational convenience.
- Decision: Secrets from a dedicated mechanism; environment variables only when nothing else is possible; detect before commit; rotate.
- Rejected: Environment variables as safe store: refuted as restricted by OWASP and by the Node threat model.

**PIG-JS.DEFENSE.SECRETS.6** Leakage through output and memory
- Positions: Generic errors, zero-filled buffers, protected reports, secure heap (ASVS 16.5.1, Node docs). Claims SRVSEC-C60, C63, RUNTIME-C13, C15, C52.
- Forces: Confidentiality against debuggability.
- Decision: Return generic error text, use Buffer.alloc, treat reports as sensitive, use --secure-heap on shared hosts.
- Rejected: Verbose errors to clients: rejected by ASVS.

**PIG-JS.DEFENSE.HOST.1** Permission model
- Positions: Seat belt (Node permissions docs, threat model) against containment of hostile dependencies (Node best-practices page). Claims RUNSEC-C38 to C40, SRVSEC-C54.
- Forces: Realism about guarantees against the appeal of a sandbox.
- Decision: Seat belt for trusted code only, narrow grants, patched Node, never the only control.
- Rejected: Permission model as sandbox: wins nowhere given the documented limits and CVEs.

**PIG-JS.DEFENSE.HOST.2** Inspector exposure
- Positions: Never public, never in production, no SIGUSR1 activation (Node docs). Claims RUNTIME-C51, SRVSEC-C40.
- Forces: Safety against live debugging.
- Decision: No exposed inspector; attach a SIGUSR1 listener to block activation.
- Rejected: Inspector on a public address: documented as insecure.

**PIG-JS.DEFENSE.HOST.3** HTTP parsing and smuggling
- Positions: Strict parser plus front-end normalization (Node best practices, CVE-2026-58044). Claims SRVSEC-C57, C58, C59.
- Forces: Strictness against interoperability with sloppy clients.
- Decision: Never set insecureHTTPParser; normalize at the front end; HTTP/2 end to end where possible.
- Rejected: Lenient parser: accepts requests the strict one rejects.

**PIG-JS.DEFENSE.HOST.4** Regex cost
- Positions: Bounded input and patterns, non-backtracking engine where available (OpenSSF, V8 blog, OWASP). Claims RUNSEC-C30 to C35, TYPES-C32.
- Forces: Availability against expressive patterns.
- Decision: Bound length and repetition, avoid nested quantifiers, anchor, prefer a non-backtracking engine where one exists.
- Rejected: Assuming V8 has a non-backtracking engine: restricted, experimental and flagged.

**PIG-JS.DEFENSE.HOST.5** Parser resource limits
- Positions: Parser limits (OWASP input validation) and a patched Node (CVE-2026-21717). Claims TYPES-C31, RUNSEC-C37.
- Forces: Availability against unlimited request bodies.
- Decision: Set size, depth and number limits; keep Node patched.
- Rejected: Unlimited parsing: wins nowhere for hostile input.

**PIG-JS.DEFENSE.HOST.6** Module load path
- Positions: Trusted module directories (Node best practices, threat model). Claim SRVSEC-C64.
- Forces: Integrity of the load path against deployment ease.
- Decision: Treat module directories as trusted and harden them.
- Rejected: Writable module directories: outside Node's vulnerability scope.

**PIG-JS.DEFENSE.DOM.2.1** Script URL sinks
- Positions: Allowlisted or Trusted script URLs (OWASP, MDN, DOMSEC-C24) against loading any URL a component computes.
- Forces: Safety against flexibility of plugin and worker loading.
- Decision: Pass only allowlisted or Trusted URLs to script and worker sinks.
- Rejected: Free-form script URLs: would win only for code that never receives input, where the question does not arise.

**PIG-JS.DEFENSE.DOM.2.2** Redirect targets
- Positions: Redirect only to an allowlist (ASVS 3.7.2) against redirect to any validated-looking URL. DOMSEC-C56.
- Forces: Safety against convenient return-URL parameters.
- Decision: Redirect automatically only to allowlisted destinations.
- Rejected: Denylist or syntax checks on the destination: would win never on safety, since encodings defeat them.

**PIG-JS.DEFENSE.DOM.6.1** Escape hatches
- Positions: Default encoding plus escape hatches as sinks (OWASP XSS sheet, consensus). Claims DOMSEC-C55, FW-C02.
- Forces: Safety against framework convenience.
- Decision: Treat every documented escape hatch as a sink that receives sanitized input.
- Rejected: Framework output as safe in all paths: refuted by the hatches the framework documentation itself names.

**PIG-JS.DEFENSE.INJECTION.1.1** Strings as code
- Positions: No code from strings (MDN, OWASP, CSP3, Synode study) against Google's code-loader exception and indirect eval as mitigation. Claims DOMSEC-C03, ASYNC-C33, RUNSEC-C15 to C18, LANG-C49.
- Forces: Safety against the few legitimate dynamic-evaluation uses.
- Decision: Never evaluate untrusted strings, JSON.parse for data, enforce no-eval, no-implied-eval and no-new-func.
- Rejected: Google's code-loader exception: wins for loaders the application itself writes. Indirect strict eval: only when evaluation is unavoidable, cuts scope exposure not injection.

**PIG-JS.DEFENSE.INJECTION.1.2** The vm module
- Positions: node:vm is not a security mechanism (Node vm docs, RUNSEC-C22).
- Forces: Safety against the misreading of separate contexts as isolation.
- Decision: Never run untrusted code in node:vm.
- Rejected: vm as sandbox: refuted by the module's own warning.

**PIG-JS.DEFENSE.INJECTION.4.1** Containment check
- Positions: Canonicalize then compare (CWE-22, Node docs on isAbsolute and normalize, Express root option). Claims RUNSEC-C27, C29, SRVSEC-C47, C48, C49, C51.
- Forces: Safety against lexical convenience.
- Decision: Resolve symlinks and normalize, then check containment; validate the result of fileURLToPath; set root in Express.
- Rejected: path.normalize or isAbsolute alone: refuted by the Node docs. Prefix-stripping sanitization: broken by the node-tar advisory.

**PIG-JS.DEFENSE.INJECTION.4.2** Archive extraction
- Positions: Ignore archive-supplied paths, reject symlinked archives (ASVS 5.3.3, 5.2.5, Zip Slip). Claims SRVSEC-C50, C52.
- Forces: Safety against extraction convenience.
- Decision: Compute destination paths yourself; refuse symlinks unless required, then allowlist.
- Rejected: Trusting entry names: refuted by Zip Slip.

**PIG-JS.DEFENSE.INJECTION.4.3** Check then use
- Positions: Open and handle the error (Node fs docs) against access-then-open. Claims RUNTIME-C18, SRVSEC-C53.
- Forces: Race freedom against a friendly pre-check.
- Decision: Open directly and handle the error.
- Rejected: Pre-check with fs.access: wins nowhere for a guard; allowed only to report, never to authorize.

**PIG-JS.DEFENSE.INJECTION.5.2** YAML and legacy serializers
- Positions: js-yaml 4 safe by default (changelog) against js-yaml 3 load and node-serialize. Claims SRVSEC-C41, C42.
- Forces: Safety against legacy compatibility.
- Decision: js-yaml 4 or later for untrusted YAML; node-serialize never for untrusted input.
- Rejected: js-yaml 3 or the js-types package: would win only for trusted input.

**PIG-JS.DEFENSE.INJECTION.6.1** Destination rules
- Positions: Allowlist (OWASP SSRF, ASVS 1.3.6) against deny-list fallback; WHATWG URL against url.parse (Node docs). Claims SRVSEC-C29, C31.
- Forces: Strength against the cases where destinations are not enumerable.
- Decision: Match hosts against an allowlist and parse with the WHATWG URL class.
- Rejected: OWASP minimum deny-list: only when an allowlist is impossible.

**PIG-JS.DEFENSE.INJECTION.6.2** Connection to the validated address
- Positions: Resolve once, validate, connect to that address (OWASP SSRF, Node dns and net docs). Claims SRVSEC-C33, C34, C39.
- Forces: Rebinding resistance against code simplicity.
- Decision: Resolve to an address, check it, connect to the address.
- Rejected: Hostname check alone: refuted by DNS rebinding.

**PIG-JS.DEFENSE.INJECTION.6.3** Redirect handling
- Positions: Redirects off or revalidated (ASVS 15.3.2, OWASP SSRF). Claims SRVSEC-C35, C36.
- Forces: Safety against transparent following.
- Decision: Disable redirects or revalidate each target.
- Rejected: Automatic following: wins only for known-trusted destinations.


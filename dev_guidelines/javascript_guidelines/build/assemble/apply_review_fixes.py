"""Stage 7 fixes: apply the decided corrections upstream of the graphs, once.

Reads and edits  build/distill/skeleton.md, build/distill/claims_ledger.md,
                 build/research/{06_runsec,13_srvsec,08_quality}/result.md (quote corrections, F18 only)
Writes           build/assemble/bookkeeping_log.md (build bookkeeping moved out of the engineer-facing fields)

This is a record of a one-time edit: every replacement asserts that the old text is present exactly once, so a second
run stops at the first assertion. Order of use (guideline root):
    python3 build/assemble/apply_review_fixes.py        # this file
    python3 build/assemble/apply_flags.py               # F05 and F17 flags, computed from the claim tables
    python3 build/assemble/build_batches.py && zsh build/assemble/build_graphs.sh && python3 build/assemble/check_complete.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batches as b  # noqa: E402

ROOT = b.ROOT
LEDGER, SKEL = b.LEDGER, b.SKEL
LOG = []


# ----------------------------------------------------------------------------- ledger helpers
class Ledger:
    def __init__(self):
        self.lines = LEDGER.read_text().split("\n")

    def idx(self, row):
        for n, l in enumerate(self.lines):
            if l.startswith(f"| {row} |"):
                return n
        raise SystemExit(f"ledger row not found: {row}")

    def cells(self, row):
        return b.split_cells(self.lines[self.idx(row)])

    def put(self, row, cells):
        self.lines[self.idx(row)] = "| " + " | ".join(cells) + " |"

    def statement(self, row, new):
        c = self.cells(row)
        c[4] = new
        self.put(row, c)

    def replace(self, row, old, new):
        c = self.cells(row)
        assert c[4].count(old) == 1, (row, old)
        c[4] = c[4].replace(old, new)
        self.put(row, c)

    def role(self, row, new):
        c = self.cells(row)
        c[6] = new
        self.put(row, c)

    def next_id(self, prefix):
        nums = [int(m.group(1)) for l in self.lines for m in [re.match(rf"\| {prefix}-(\d+) \|", l)] if m]
        return f"{prefix}-{max(nums) + 1:03d}"

    def add(self, prefix, node, graph, statement, agreement, role, after=None, before=None):
        rid = self.next_id(prefix)
        line = f"| {rid} | - | {node} | {graph} | {statement} | {agreement} | {role} |"
        if before:
            at = self.idx(before)
        elif after:
            at = self.idx(after) + 1
        else:
            rows = [n for n, l in enumerate(self.lines) if re.match(rf"\| {prefix}-\d+ \|", l) and f"| {node} |" in l]
            at = rows[-1] + 1
        self.lines.insert(at, line)
        return rid

    def save(self):
        LEDGER.write_text("\n".join(self.lines))


# ----------------------------------------------------------------------------- skeleton helpers
class Skeleton:
    def __init__(self):
        self.text = SKEL.read_text()
        self.lines = self.text.split("\n")

    def node(self, uid):
        for n, l in enumerate(self.lines):
            if l.startswith(f"| {uid} | "):
                return n
        raise SystemExit(f"skeleton node not found: {uid}")

    def set_cell(self, uid, col, value):
        n = self.node(uid)
        c = b.split_cells(self.lines[n])
        c[col] = value
        self.lines[n] = "| " + " | ".join(c) + " |"

    def epistemic(self, uid, state):
        self.set_cell(uid, 3, state.replace(" | ", " \\| "))

    def intent(self, uid, text):
        self.set_cell(uid, 2, text)

    def replace(self, old, new):
        t = "\n".join(self.lines)
        assert t.count(old) == 1, old[:80]
        self.lines = t.replace(old, new).split("\n")

    def save(self):
        SKEL.write_text("\n".join(self.lines))


L = Ledger()
S = Skeleton()


def first_row(node):
    for l in L.lines:
        c = b.split_cells(l) if re.match(r"\| [A-Z]+-\d+ \|", l) else []
        if c and c[2] == node:
            return c[0]
    raise SystemExit(node)


FIRST_LINT21 = first_row("PIG-JS.VERIFICATION.LINT.2.1")
FIRST_STRICT1 = first_row("PIG-JS.CONTRACTS.STRICT.1")
P, D = b.P_ID, b.D_ID

# ============================================================================= F09 / F21: "MUST hold:" rows
# Each row becomes a verb-first rule (the build prefixes MUST), or a fact (role changes, the text stays in the notes).
RULES = {
    "SUBSET-033": "Transport 64-bit ids as strings, or convert them with an explicit replacer and reviver, because JSON.stringify throws a TypeError on a BigInt and JSON.parse corrupts integers beyond the safe range.",
    "SUBSET-041": "Call super() before touching this in a derived class; the derived class's field initialisers run right after super() returns, the base class's at the start of its constructor.",
    "CONTRACTS-001": "Check run-time data with run-time code: a type layer is erased before run time, types and assertions emit no check, so values arriving at run time are never checked by them.",
    "CONTRACTS-003": "Do not treat a passing type check as proof of safety: a checker may be intentionally unsound in places.",
    "CONTRACTS-009": "Make input handling a recognizer of valid inputs and keep input languages simple; do not hand-write ad-hoc recognizers (regex allow or deny lists) for complex input languages, which are unreliable (Sassaman et al., position of a 2011 technical report).",
    "CONTRACTS-013": "Check JavaScript with TypeScript where no compile step exists: enable checkJs for the project (or ts-check per file), types coming from JSDoc.",
    "CONTRACTS-019": "Avoid syntax needing code generation (enum, runtime namespaces, parameter properties, import aliases) when TypeScript runs through Node type stripping, and enforce it with erasableSyntaxOnly.",
    "CONTRACTS-020": "Use the settings Node documents for type stripping (noEmit, target esnext, module nodenext, rewriteRelativeImportExtensions, erasableSyntaxOnly, verbatimModuleSyntax) with TypeScript 5.8 or newer; Node ignores tsconfig at run time, so they steer only the checker.",
    "CONTRACTS-021": "Enable isolatedModules when files are transpiled one at a time (Babel, swc, esbuild), so code needing cross-file information is reported.",
    "CONTRACTS-039": "Make the body of a user-defined type predicate perform an explicit run-time check: the compiler trusts a predicate as a narrowing assertion with the same standing as a type assertion.",
    "CONTRACTS-040": "Declare object types by interface rather than type alias, because an interface can be extended and re-opened and an alias cannot (Google TS position, used as a position and not as evidence); const enum is already excluded by LAYER.4.",
    "CONTRACTS-043": "Use optional trailing parameters in declared APIs instead of overloads that differ only in trailing parameters, because overloads let a wrongly typed function pass compatibility and break explicit undefined under strict null checks.",
    "CONTRACTS-044": "Use a union type in declared APIs instead of overloads that differ in the type of one argument position, so a caller passing a value of the union type is accepted.",
    "CONTRACTS-045": "Type a callback whose result is ignored as void, not any, and do not make its parameters optional, because a callback accepting fewer arguments is always legal.",
    "CONTRACTS-050": "Declare boundary schemas as run-time schemas from which the static type is inferred (Zod parse, safeParse and z.infer; Valibot InferOutput), so parse and type cannot drift; decided at the class level, no library is preferred over another (vendor facts only; Valibot size claim not recorded).",
    "CONTROL-020": "Do not use the void operator to handle a promise: it silences the lint rule only, and the rejection stays unhandled.",
    "CONTROL-024": "Use Promise.allSettled when every operation must finish: Promise.all rejects on the first rejection while the other operations keep running with outcomes unavailable.",
    "CONTROL-036": "Wrap with a more specific message and pass the original as the cause option when catching and rethrowing; do not assume the cause is an Error.",
    "CONTROL-043": "Create a new AbortController per operation: an AbortSignal is one-shot, once aborted it stays aborted and the abort event fires once.",
    "CONTROL-046": "Prefer timers/promises with a signal option for cancellable waiting in Node, and clear or unref timers that must not keep the process alive.",
    "CONTROL-049": "Listen for abort with events.addAbortListener in Node, not signal.addEventListener, which a third party can defeat with stopImmediatePropagation and which makes forgotten removal and leaks likely.",
    "CONTROL-061": "Transfer large buffers through the transfer list (the sender loses them) or share memory with SharedArrayBuffer, because thread messages are copied by structured clone; expect no DOM access in browser workers.",
    "CONTROL-070": "Pass cleanup: true to stream.finished if dangling listeners are unwanted, because it leaves error, end, finish and close listeners attached after settling.",
    "CONTROL-075": "Do not assume an unhandled rejection only prints a warning in Node: it is raised as an uncaught exception by default (mode throw, since Node 15) and can terminate the process.",
    "CONTROL-076": "Handle unhandled rejections in a browser through the cancelable unhandledrejection event on the global scope (window or worker); preventDefault suppresses the console report, and cross-origin script rejections do not fire it.",
    "CONTROL-082": "Make a SIGTERM or SIGINT listener finish cleanup and end the process itself, because it replaces the default handler (inferred from the default-removal fact; the shutdown contract side belongs to the web-architecture sibling).",
    "STRUCTURE-014": "Load modules in the browser with script type module: import and export work only in modules, which are fetched under CORS and same-origin rules, so file:// loading fails.",
    "STRUCTURE-015": "Configure the type checker to match the host that runs the code: module resolution is defined by the host, not by ECMAScript, so a specifier can mean different things in Node, a browser and a bundler.",
    "STRUCTURE-017": "Write the file extension on every relative specifier in Node ESM and spell out directory indexes, as in browsers; import with the real extension (import './file.ts' under type stripping). Google JS concurs as holder position only.",
    "STRUCTURE-018": "Replace the CommonJS globals in Node ESM: import.meta.dirname and import.meta.filename (or new URL with import.meta.url) for __dirname and __filename, module.createRequire where require is needed, and the with { type: 'json' } attribute for JSON, which Node makes mandatory.",
    "STRUCTURE-019": "Use require() from CommonJS only for synchronous ES modules (no top-level await anywhere in the graph) and dynamic import() for the rest, which works in both module systems.",
    "STRUCTURE-021": "Use the default import when importing CommonJS from ESM (always the module.exports object) and do not depend on named imports for unusual export patterns: Node finds named exports by static analysis of common syntax and does not always detect them.",
    "STRUCTURE-046": "Order the keys of conditional exports from most specific to least specific and put default last, because earlier entries take priority.",
    "STRUCTURE-047": "Use the package.json imports field (keys starting with a hash character) for package-internal aliases: Node resolves them natively and they cannot collide with external package names.",
    "STRUCTURE-048": "Import files of the same logical project by relative path, so a project can move without rewriting imports. Holder position of Google TS.",
    "DEFENSE-009": "Allowlist the executable and the arguments and run the process with the least privilege required when an OS command is unavoidable.",
    "DEFENSE-017": "Sign serialized data and verify before deserializing (an HMAC where feasible) when the set of expected messages is known; populate a new object from validated fields instead of deserializing into the application's own types. Language-neutral grounds only.",
    "DEFENSE-018": "Match the host of an outbound request against an allowlist and build the request yourself when the destination is known.",
    "DEFENSE-032": "Never set event-handler attributes from untrusted data with setAttribute, which is not unconditionally safe. Position held against OWASP's DOM XSS sheet, which lists setAttribute as a safe construction method; the MDN Trusted Types page lists its value argument as a TrustedScript sink, the condition (event-handler names) is inferred.",
    "DEFENSE-046": "Pass TrustedScript objects instead of strings to eval and Function in browsers, and prefer the trusted-types-eval CSP keyword to unsafe-eval.",
    "DEFENSE-053": "Neutralize id and name attributes when sanitizing (DOMPurify SANITIZE_NAMED_PROPS, or Sanitizer removeAttribute); quoted as OWASP's advice, not a DOMPurify preference.",
    "DEFENSE-056": "Verify event.origin (and source where relevant) in message handlers before acting, and discard messages from untrusted origins.",
    "DEFENSE-058": "Validate the syntax and type of every message after verifying the origin; a trusted sender can itself be compromised.",
    "DEFENSE-120": "Start Node with --secure-heap=n (not on Windows) and do not run a production app on a shared machine, to limit leaks from pointer overruns.",
    "DEFENSE-122": "Ensure that no path granted under --permission contains a relative symlink, and do not rely on the permission model to restrict code already holding open file descriptors (CVE-2025-55130 as the fact).",
    "DEFENSE-162": "Build the absolute path from trusted parts, or set the root option, with Express res.sendFile or res.download; with root set Express validates that the path resolves within it, even with '..'. Express facts, no framework preference.",
    "DEFENSE-166": "Ignore path information supplied by the archive when extracting archives: an entry named ../../evil.sh writes outside the target (Zip Slip, 5 June 2018, npm libraries adm-zip and unzipper).",
    "DEPENDENCIES-001": "Treat every dependency, direct or transitive, as trusted code running with the application's full privileges: a malicious or compromised dependency is a first-order application risk.",
    "DEPENDENCIES-010": "Ask whether existing components suffice before adding a dependency, and test the candidate in isolation for unexpected indirect dependencies in production.",
    "DEPENDENCIES-013": "Check a package's name for typos and for a more popular look-alike before adding it, and verify that it exists and is authentic.",
    "DEPENDENCIES-030": "Review lockfiles, rotate all developer credentials and pin to versions published before the incident date after a worm-style compromise (CISA's position).",
    "DEPENDENCIES-035": "Set allow-git or allow-remote to root rather than all when a project needs git-referenced or tarball-URL dependencies, which npm 12 refuses unless allowed.",
    "DEPENDENCIES-043": "Prefer trusted publishing (OIDC, short-lived workflow-specific credentials) over long-lived tokens when publishing an npm package from CI.",
    "DEPENDENCIES-046": "Review exactly which files go out before publishing (all files in the directory are published unless an ignore file or the package.json files field excludes them) with npm publish --dry-run, keep secrets out of repositories and tarballs, give CI tokens least privilege, and unpublish on exposure.",
    "VERIFICATION-012": "Run mutation testing incrementally on changed code during code review and filter mutants, instead of mutating the whole code base, when adopting it at scale. Abstract-level source, Google setting (24,000+ developers, 1,000+ projects).",
    "VERIFICATION-019": "Make the merge gate always run: a skipped required check must not let a merge through.",
    "VERIFICATION-036": "Pair Prettier with ESLint by disabling conflicting rules through eslint-config-prettier and running Prettier separately when Prettier is the formatter; eslint-plugin-prettier is generally not recommended. The project's own integration position, applied because Prettier is the chosen formatter.",
    "VERIFICATION-037": "Do not gate on node:test's coverage flag (--experimental-test-coverage) as a stable feature: it is experimental (Stability 1). Gating advice inferred.",
    "RUNTIME-001": "Treat performance advice that rests on engine internals as dated single-body evidence that can describe a mechanism but cannot prescribe (no T1 specifies engine performance); make a performance belief a rule only through a measurement of the real workload.",
    "RUNTIME-005": "Keep long-lived state (caches, sessions) bounded: most objects die young, so the collector reclaims young objects often and cheaply and old objects rarely and at higher cost, and long-lived state is promoted to the costlier region.",
    "RUNTIME-016": "Record Node version and OS, the observed symptoms, reproduction steps and recent changes before investigating, then pick the diagnostic path by symptom: behaviour, memory, or latency and CPU.",
    "RUNTIME-023": "Let the process warm up, take a snapshot, exercise the suspect path, take a second snapshot, load both in order in DevTools, switch to Comparison and follow large positive deltas to their retainers, to find a leak.",
    "RUNTIME-024": "Use the sampling heap profiler in production (low overhead) and keep the allocation timeline out; take a heap snapshot only where the process can crash without harming availability (it stops the main thread and needs about twice the heap in memory) and never expose the trigger endpoint publicly.",
}
for row, text in RULES.items():
    L.statement(row, text)

# ============================================================================= F09: Merged and similar bookkeeping in rule text
MERGED = re.compile(r"\s*Merged(?: at integration)?[^.]*\.")
for i, line in enumerate(L.lines):
    m = re.match(r"\| ([A-Z]+-\d+) \|", line)
    if not m:
        continue
    c = b.split_cells(line)
    if c[6] not in ("decision", "acceptable-when"):
        continue
    found = MERGED.findall(c[4])
    if found:
        LOG.append(f"- {c[0]} ({c[2]}): removed from the rule text: {' '.join(f.strip() for f in found)}")
        c[4] = MERGED.sub("", c[4]).strip()
        L.lines[i] = "| " + " | ".join(c) + " |"
L.replace("DEPENDENCIES-037", " Claim SUPPLY-C12 is labelled consensus; its effect rests on one T1 assertion and is relabelled single-source (12_dissent X5).", "")
LOG.append("- DEPENDENCIES-037 (PIG-JS.DEPENDENCIES.UPDATE.1): removed from the rule text: Claim SUPPLY-C12 is labelled consensus; its effect rests on one T1 assertion and is relabelled single-source (12_dissent X5).")

# ============================================================================= F01 OS command injection
L.statement("DEFENSE-081", "Never build a shell command string from untrusted input, sanitized or not: pass the program and an argument array, never pass untrusted input to child_process.exec or execSync, and do not enable the shell option of spawn, execFile and their sync forms with untrusted input.")
S.epistemic("PIG-JS.DEFENSE.INJECTION.2", "known | unvalidated: the stronger form (no shell string from input, sanitized or not) is inferred from OWASP's parameterization principle; Node's own sentence states only the unsanitized case")
S.replace("- Decision: Argument array, no shell option with input; prefer built-in library functions.\n- Rejected: exec with escaped input: wins where a shell feature is truly needed, and then OWASP's allowlist and least privilege apply.",
          "- Decision: Argument array, no shell string built from untrusted input (sanitized or not), no shell option with input; prefer built-in library functions. The sanitized-exec exclusion is stronger than Node's sentence and rests on OWASP's parameterization principle (inferred).\n- Rejected: exec with escaped input: refused, because sanitizing does not remove the shell parse; where a shell feature is truly needed, an allowlist of the executable and arguments and least privilege apply.")

# ============================================================================= F02 consider -> MUST kept, flagged
S.epistemic("PIG-JS.CONTRACTS.STRICT.2", "known | unvalidated: source says consider (TypeScript documentation, typescript-eslint); the MUST is the build's choice under the max rule; mechanism only, no admitted source mandates the flag | conflict: friction cost (typescript-eslint)")
S.epistemic("PIG-JS.CONTRACTS.STRICT.3", "known | unvalidated: source says consider (TypeScript documentation); the MUST is the build's choice under the max rule; mechanism only, quote tool-extracted")
S.epistemic("PIG-JS.DEFENSE.SECRETS.5", "known | unvalidated: source says consider (secrets detection at the developer level); the MUST is the build's choice under the max rule; rotation has no quote of its own, single source")

# ============================================================================= F03 framework short list
S.epistemic("PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST", "risky | unvalidated: gates are the build's judgment, no admitted source states them | conflict: keep Vue and drop the platform baseline, an earlier proposal (inferred)")
S.epistemic("PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1", "known | unvalidated: the platform-first default is the build's judgment, no claim states it (FW-C46 says only that the platform offers components)")
g = L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST", D,
          "Admit a framework to the short list only if it states which versions receive security fixes (gate A, mandatory) and also has a documented escape and sanitization model (gate B) or a stated governance or maintenance body (gate C); the gates are the build's judgment, no admitted source states them.",
          "-", "decision", before="DEPENDENCIES-076")
p = L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST.1", D,
          "Make the platform, with Web Components and no framework, the default and the first candidate; adopt a framework only when a requirement is not met by the platform (the isolation test of SUPPLY-C27 confirms it).",
          "-", "decision", before="DEPENDENCIES-076")

# ============================================================================= F04 timingSafeEqual
S.epistemic("PIG-JS.DEFENSE.SECRETS.4", "known | unvalidated: Node crypto text read in v6 docs only; the current timingSafeEqual entry could not be re-read (page truncated in every fetch, browser tool did not answer)")

# ============================================================================= F06 holder positions
S.epistemic("PIG-JS.STRUCTURE.SURFACE.1", "known | conflict: default export for single-export modules, Airbnb | unvalidated: holder position only (Google JS, Google TS)")
S.epistemic("PIG-JS.STRUCTURE.SURFACE.3", "known | unvalidated: holder position only (Google JS, Google TS, Airbnb) for the strongest form (no mutable export); the mechanism is T1")
S.epistemic("PIG-JS.STRUCTURE.SURFACE.5", "known | conflict: stateless groupings as static methods, W3C TAG | unvalidated: holder position only (Google JS, Google TS)")
S.epistemic("PIG-JS.STRUCTURE.LOADING.6", "risky | unvalidated: single T3 source, one synthetic measurement on one machine | unvalidated: holder position only (the barrel-file article's author) | conflict: barrels are a documented use of aggregation, MDN (no recommendation)")
S.epistemic("PIG-JS.STRUCTURE.DIRECTION.2", "risky | unvalidated: single T3 source (the rule's own documentation) | unvalidated: holder position only (eslint-plugin-import maintainers)")
S.epistemic("PIG-JS.SUBSET.OBJECTS.4", "known | unvalidated: holder position only (Google JS), no mechanism evidence")
S.epistemic("PIG-JS.SUBSET.EVOLUTION.5", "known | unvalidated: holder position only (Google JS); insertion hazards not extracted")
S.epistemic("PIG-JS.CONTRACTS.ESCAPE.6", "known | unvalidated: holder position only (Google TS), single T2 source")
S.epistemic("PIG-JS.CONTRACTS.MODEL.5", "known | unvalidated: holder position only (Google TS); the alias exception is inferred")
S.epistemic("VERIFICATION.TEST_SUITE.3", "risky | unvalidated: holder position only (Google), single T3 source")
S.epistemic("VERIFICATION.TEST_STABILITY.3", "risky | unvalidated: holder position only (Google figures), single T3 source")
S.epistemic("STRUCTURE.NAMING.2", "known | unvalidated: holder position only (Google JS, Google TS, W3C TAG, Airbnb)")
S.epistemic("PIG-JS.STRUCTURE.SURFACE.2", "known | unvalidated: holder position only (Google TS)")
S.epistemic("PIG-JS.STRUCTURE.FORMAT.4", "known | unvalidated: holder position only (Google TS)")
S.epistemic("PIG-JS.STRUCTURE.PACKAGE.4", "known | unvalidated: holder position only (Google TS)")

# ============================================================================= F08 type layer
L.statement("CONTRACTS-011", "Use TypeScript with strict checking as the type layer whenever the project can adopt a build or type-check step (compilation, or Node type stripping)")
L.add("CONTRACTS", "PIG-JS.CONTRACTS.LAYER.1", D,
      "Acceptable only when no build or type-check step can be adopted: JSDoc-checked JavaScript with checkJs, accepting weaker checks (open objects, optional parameters, any initialisers) and the removal of some JSDoc forms in TypeScript 7.0.",
      "-", "acceptable-when", after="CONTRACTS-011")
S.intent("PIG-JS.CONTRACTS.LAYER.1", "Write JavaScript projects in TypeScript with strict checking when a build or type-check step can be adopted; JSDoc-checked JavaScript is the stated alternative when none can")
S.epistemic("PIG-JS.CONTRACTS.LAYER.1", "risky | conflict: JSDoc-checked JavaScript, none | unvalidated: decided by the build on T1 mechanism facts and one T2 holder")
S.replace("Decision: TypeScript with strict. Rejected: JSDoc-checked JavaScript,",
          "Decision: TypeScript with strict. Condition table: TypeScript wins when a build or type-check step can be adopted (compilation, or Node type stripping); JSDoc-checked JavaScript wins when none can (LAYER.2); no type layer wins under no admitted condition; native type syntax is not planned on (Stage 1, no run-time enforcement). The choice among them is the build's judgment (the claim reads: decision for the maintainer), flagged. Rejected: JSDoc-checked JavaScript,")

# ============================================================================= F10 AEAD
L.role("DEFENSE-104", "decision")
L.statement("DEFENSE-104", "Use authenticated encryption modes only (AES in GCM or CCM, key of at least 256 bits); the advice rests on one source, OWASP, restricted to principles.")
S.intent("PIG-JS.DEFENSE.SECRETS.2", "SubtleCrypto designs are reviewed by a knowledgeable person, and encryption uses authenticated modes.")
S.epistemic("PIG-JS.DEFENSE.SECRETS.2", "known | unvalidated: single T1 source; Node crypto page truncated in every fetch | unvalidated: authenticated-encryption rule rests on one source (OWASP), restricted to principles")
S.replace("- Decision: Have a knowledgeable person review any SubtleCrypto design.", "- Decision: Have a knowledgeable person review any SubtleCrypto design; encrypt only with authenticated modes (one source, flagged).")

# ============================================================================= F11 empty catch
L.role("CONTROL-035", "decision")
L.statement("CONTROL-035", "Do not leave a catch block empty without a comment stating why taking no action is right (Google JS guide position).")
S.epistemic("PIG-JS.CONTROL.ERRORS.2", "known | unvalidated: single T1 sources; the no-empty-catch rule rests on one style-guide position (Google JS)")
S.replace("A catch that does nothing is acceptable only with its reason in a comment.", "A catch that does nothing is forbidden unless a comment states why taking no action is right.")

# ============================================================================= F12 coverage
L.statement("VERIFICATION-006", "SHOULD NOT gate on a coverage number or use one as a quality target; use coverage to find under-tested code. Study: correlation with suite effectiveness is low to moderate once suite size is controlled (31,000 suites, five large Java systems); transfer to JavaScript inferred.")
L.add("VERIFICATION", "VERIFICATION.TEST_SUITE.2", P,
      "Rejected position (OpenSSF passing criteria, T1): cover most or all branches, as a suggestion and not a numeric target; it would win for a project that adopts those criteria, and it is compatible with using coverage to locate code no test executes.",
      "-", "fact", after="VERIFICATION-006")

# ============================================================================= F13 maintainership, audit
L.statement("DEPENDENCIES-007", "Include takeover of maintainer accounts or maintainership among the threats planned for, next to vulnerable libraries: event-stream handover 2018, eslint-scope token theft 2018, debug phishing 2025 and the Shai-Hulud worm 2025 show that it recurs.")
S.intent("DEPENDENCIES.THREATS.1", "Four incidents show that control of a maintainer account or of maintainership is a recurring route of compromise, so who maintains a package is a risk to weigh beside flaws in its code.")
S.epistemic("DEPENDENCIES.THREATS.1", "known | unvalidated: four incidents; their weight against code flaws is not measured")
L.statement("DEPENDENCIES-040", "Run any known-vulnerability audit against the committed lockfile, never without one (results can differ on every run), and read findings as triage input (js-philosophy DEPENDENCIES.EVIDENCE.2).")
L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.UPDATE.3", D,
      "Acceptable only when a team adopts npm audit as its known-vulnerability check: set audit-level to define the failing severity; no admitted source states running it in CI as a practice.",
      "-", "acceptable-when", after="DEPENDENCIES-040")
S.epistemic("PIG-JS.DEPENDENCIES.UPDATE.3", "known | unvalidated: no admitted source states running npm audit in CI as a practice (SRC-149 gives behaviour facts only)")
S.replace("kept as a decision for that reason. Threshold value", "the lockfile and triage rules are decisions on that ground; running npm audit as the check is acceptable-when, since no admitted source states it as a practice. Threshold value")

# ============================================================================= F14 ESCAPE.6 vs LINT.1.2
L.replace("CONTRACTS-034", "(Google TS guide, one T2 holder)", "; enforce it with the typescript-eslint rule ban-ts-comment set to ban ts-expect-error, ts-ignore and ts-nocheck, overriding the allow-with-description default of the recommended set (Google TS guide, one T2 holder)")
L.replace("VERIFICATION-021", " Baseline suitability is inferred from the markers.", " The one override is ban-ts-comment, set to ban the three suppression directives (PIG-JS.CONTRACTS.ESCAPE.6). Baseline suitability is inferred from the markers.")

# ============================================================================= F15
L.role("DEFENSE-171", "decision")
L.statement("DEFENSE-171", "Never pass untrusted input to node-serialize unserialize(): versions up to 0.0.4 execute code through an immediately invoked function expression and no patched version exists (CVE-2017-5941, critical). Derived from advisory facts only.")
L.statement("DEFENSE-172", "Use js-yaml 4 or later if js-yaml parses untrusted YAML (load, loadAll and dump safe by default from 4.0.0; unsafe tags moved to js-yaml-js-types, which must not be installed for untrusted input, inferred).")
L.add("DEFENSE", "PIG-JS.DEFENSE.INJECTION.6.1", D, "Match the host of an outbound request against an allowlist when the destination is known, and build the request yourself.", "-", "decision", after="DEFENSE-174")

# ============================================================================= F16 framework-specific and dated facts out of the rules
L.statement("DEFENSE-140", "Rely on framework default output encoding and treat every documented escape hatch of the framework in use as a sink that needs sanitized input.")
L.add("DEFENSE", "PIG-JS.DEFENSE.DOM.6.1", D, "Escape hatches by framework (dated evidence, framework documentation): React dangerouslySetInnerHTML, Angular bypassSecurityTrust, Lit unsafeHTML, Vue v-html, Svelte @html.", "single-source", "fact", after="DEFENSE-140")
S.intent("PIG-JS.DEFENSE.DOM.6.1", "Escape hatches of a framework are treated as sinks needing sanitized input; the per-framework documentation facts are recorded here.")
L.replace("DEFENSE-041", "; the API is Baseline since February 2026", "")
L.statement("DEPENDENCIES-038", "Run production Node.js on an Active or Maintenance LTS only.")
L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.UPDATE.2", D, "Dated evidence at reading: Node v24 and v22 were LTS and v26 was Current; recheck against the release schedule.", "single-source", "fact", after="DEPENDENCIES-038")
L.statement("DEPENDENCIES-039", "Pin the toolchain (TypeScript and Node versions) to the compatibility table of the framework version in use, and lock the current minor where typings may change in minor releases.")
L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.UPDATE.2", D, "Dated evidence: Angular 22 lists TypeScript >=6.0.0 <6.1.0 with Node ^22.22.3, ^24.15.0 or ^26.0.0; Vue typings may change in minor releases.", "single-source", "fact", after="DEPENDENCIES-039")
L.statement("DEPENDENCIES-048", "Pin the framework major to one its policy lists as supported and read the documentation set of that major; for a new adoption take the newest supported major.")
L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE.1", D, "Dated evidence (htmx): its policy lists 4.x, 2.x and 1.9.x as supported and versions below 1.9 as unsupported, while the main docs site documents 2.x and the policy and release page show 4.x.", "single-source", "fact", after="DEPENDENCIES-048")
L.statement("SUBSET-062", "Check runtime support on every target before using Temporal, and cover a target that lacks it with a polyfill.")
L.add("SUBSET", "PIG-JS.SUBSET.EVOLUTION.2", D, "Dated evidence, recheck both pages before citing: the proposal repository lists Temporal shipping in Firefox 139, Chrome 144 and Node.js 26 while MDN marked it not Baseline; polyfills exist.", "consensus", "fact", after="SUBSET-062")

# ============================================================================= F18 wording of rules after the quote corrections
L.replace("DEFENSE-135", "hang a machine 30+ seconds", "hang a machine for about half a minute")
L.statement("DEFENSE-133", "Require the regex to match the entire value when validating: use anchors at both ends. That ECMAScript $ does not accept a trailing newline is inferred, not stated on the cited page.")

# ============================================================================= F19 philosophy rows made language- and tool-neutral
L.statement("DEFENSE-007", "Never build code from strings: dynamic code evaluation executes attacker-influenced input as code with the caller's privileges, whatever API offers it.")
L.add("VERIFICATION", "PIG-JS.VERIFICATION.LINT.2", D, "Make the CI job that runs the lint gate always run: GitHub required status checks pass on successful, skipped or neutral conclusions, so a skipped job lets a merge through.", "-", "decision", before=FIRST_LINT21)
L.replace("DEPENDENCIES-024", " (caret, tilde)", "")
L.replace("DEPENDENCIES-024", "as the archived OpenSSF npm guide v1.1 allows, ", "")
L.statement("DEPENDENCIES-017", "Read supply-chain assurance as graded: provenance alone is the lowest level, a hosted platform signing it the middle, hardened builds that resist tampering during the build the highest.")
L.add("DEPENDENCIES", "PIG-JS.DEPENDENCIES.PUBLISH.1", D, "Fact (SLSA levels): Build L1 provenance exists, L2 a hosted platform signs it, L3 hardened builds resist tampering during the build.", "single-source", "fact", after="DEPENDENCIES-045")
L.add("CONTRACTS", "PIG-JS.CONTRACTS.STRICT", D, "Fact: TypeScript documents intentional unsoundness, for example primitives satisfying object-shaped types.", "single-source", "fact", before=FIRST_STRICT1)

# ============================================================================= F21 sample size behind 74%
L.replace("VERIFICATION-017", "74% of order-dependent flaky tests in the study were fixed that way.", "74% (14 of 19) of order-dependent flaky tests in the study were fixed that way.")

# ============================================================================= F09: integration notes and row lists leave the engineer-facing notes (kept in the skeleton as record)
LOG.append("- Integration notes of the skeleton (lines starting 'Integration note') no longer reach design_notes; they stay in build/distill/skeleton.md. build_batches.py skips them.")
LOG.append("- The 'Rows:' line (ledger row ids with role and agreement) and the row ids inside 'Rejected', 'Fact' and 'Deferred' lines no longer reach design_notes; the ledger is the record.")

# ----------------------------------------------------------------------------- skeleton: ledger rows column, convention line
rows_of = {}
for l in L.lines:
    m = re.match(r"\| ([A-Z]+-\d+) \|", l)
    if m:
        c = b.split_cells(l)
        rows_of.setdefault((c[3], c[2]), []).append(c[0])
LIMIT = next(i for i, l in enumerate(S.lines) if l.startswith("## Planned boundary links"))
for n, l in enumerate(S.lines[:LIMIT]):
    c = b.split_cells(l) if l.startswith("| ") else []
    if len(c) == 5 and re.match(r"^(PIG-JS\.)?[A-Z][A-Z0-9_.]*$", c[0]) and c[0] != "uid":
        # graph by position: philosophy uids carry no PIG-JS prefix, except nothing else shares the table shape
        gid = D if c[0].startswith("PIG-JS.") else P
        new = ", ".join(rows_of.get((gid, c[0]), [])) or "-"
        if new != c[4]:
            c[4] = new
            S.lines[n] = "| " + " | ".join(c) + " |"
S.replace("- Nodes relabelled `risky` (decision on one T3 source): `PIG-JS.STRUCTURE.LOADING.6`, `PIG-JS.STRUCTURE.DIRECTION.2`, `VERIFICATION.TEST_SUITE.3`, `VERIFICATION.TEST_STABILITY.3`.",
          "- Nodes relabelled `risky` (decision on one T3 source): `PIG-JS.STRUCTURE.LOADING.6`, `PIG-JS.STRUCTURE.DIRECTION.2`, `VERIFICATION.TEST_SUITE.3`, `VERIFICATION.TEST_STABILITY.3`. Relabelled `risky` at stage 7: `PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST` (gates are the build's judgment), `PIG-JS.CONTRACTS.LAYER.1` (decided by the build on mechanism facts and one holder).")

# ----------------------------------------------------------------------------- ledger header count
n_rows = sum(1 for l in L.lines if re.match(r"\| [A-Z]+-\d+ \|", l))
n_cl = sum(len(b.CID.findall(b.split_cells(l)[1])) for l in L.lines if re.match(r"\| [A-Z]+-\d+ \|", l))
n_free = sum(1 for l in L.lines if re.match(r"\| [A-Z]+-\d+ \|", l) and not b.CID.findall(b.split_cells(l)[1]))
txt = "\n".join(L.lines)
txt, k = re.subn(r"Rows: \d+ \(\d+ carry \d+ claim ids, \d+ are claim-less folklore rows\)\.",
                 f"Rows: {n_rows} ({n_rows - n_free} carry {n_cl} claim ids, {n_free} are claim-less: folklore rows and rows added at stage 7).", txt)
assert k == 1
L.lines = txt.split("\n")

L.save()
S.save()

# ============================================================================= claim tables: F18 quote wording, F21 sample size
def edit_table(slot, claim, pairs):
    p = ROOT / f"build/research/{slot}/result.md"
    lines = p.read_text().split("\n")
    for n, l in enumerate(lines):
        if l.startswith(f"| {claim} |"):
            for old, new in pairs:
                assert l.count(old) == 1, (claim, old)
                l = l.replace(old, new)
            lines[n] = l
            p.write_text("\n".join(lines))
            return
    raise SystemExit(f"claim not found {claim}")


edit_table("06_runsec", "RUNSEC-C37", [
    ("hung a powerful machine for 30+ seconds", "hung a powerful machine for about half a minute"),
    ('"Remote attacker can cause significant performance degradation (30+ seconds hang on powerful machines) via JSON parsing with ~2 MB adversarial payload."',
     '"With a ~2 MB payload, this can significantly slow down the JSON parsing - even on a powerful MacBook, this can hang for about half a minute."'),
])
edit_table("06_runsec", "RUNSEC-C35", [
    ("Require the regex to match the entire value when validating; JavaScript ^ and $ are anchors where $ is not permissive about a trailing newline.",
     "Require the regex to match the entire value when validating, with anchors at both ends; that JavaScript $ does not accept a trailing newline is not stated on the cited page (inferred)."),
    ("OpenSSF table marks ECMAScript $ as not permissive, unlike Python where \\Z is required; unanchored validation accepts partial matches.",
     "Unanchored validation accepts partial matches. The statement about ECMAScript $ and a trailing newline is not on the cited OpenSSF page (checked at review); it is inferred from ECMA-262, where without the multiline flag $ matches only at the end of the input."),
    ("| single-source | grounded |", "| single-source | grounded for the entire-value rule; inferred for the $ statement |"),
])
edit_table("13_srvsec", "SRVSEC-C27", [
    ('"Disallow client-controlled query operators unless validated" (tool-extracted)',
     '"Disallow client-controlled query operators (like $where, $regex, or $expr ...) unless strictly required and validated" (tool-extracted digest; the ellipsis is the digest\'s)'),
])
edit_table("13_srvsec", "SRVSEC-C07", [
    ("SRC-078 §Information Exposure through Timing Attacks (CWE-208)",
     "SRC-078 §Information Exposure through Timing Attacks (CWE-208), for the principle only: that page does not carry the surrounding-code sentence"),
])
edit_table("08_quality", "QUALITY-C35", [
    ("because 74% of order-dependent flaky tests", "because 74% (14 of 19) of order-dependent flaky tests"),
])
LOG.append("- Quote wording corrected in the claim tables (F18): RUNSEC-C37 (about half a minute), RUNSEC-C35 (the $ statement is inferred, not on the cited page), SRVSEC-C27 (full operator sentence), SRVSEC-C07 (SRC-078 carries the principle only). QUALITY-C35 states 14 of 19. The SRC-341 URL note (one chapter URL for five chapters) is left as is in the source register.")

(ROOT / "build/assemble/bookkeeping_log.md").write_text(
    "# Build bookkeeping moved out of the engineer-facing fields (stage 7)\n\n"
    "Constraints and design notes of the graphs hold rules, their reasons and the evidence only. What the build did to reach them\n"
    "is recorded here and in the ledger and skeleton.\n\n" + "\n".join(LOG) + "\n")
print("applied;", len(LOG), "log lines")

"""Patch of slot 14_secgap2 (second security gap round) into the integrated files.

Edits build/distill/claims_ledger.md, build/distill/skeleton.md and build/distill/decisions_for_review.md in place,
with assertions; it stops on a second run (the first new row id already exists). Never runs integrate.py.

Run from the guideline root:  python3 build/patch/14_secgap2/apply_patch.py
Then: python3 build/assemble/apply_flags.py, python3 build/assemble/build_batches.py, zsh build/assemble/build_graphs.sh,
python3 build/assemble/check_complete.py, python3 build/distill/check_ledger.py, ig-tool validate for both graphs.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "build/distill/claims_ledger.md"
SKEL = ROOT / "build/distill/skeleton.md"
DEC = ROOT / "build/distill/decisions_for_review.md"
HERE = Path(__file__).resolve().parent

P, D = "js-philosophy", "pig-js-defaults"
S = "SECGAP2-"


def c(*nums):
    return ", ".join(f"{S}C{n:02d}" for n in nums)


# ------------------------------------------------------------------------------------------------ ledger rows
# (row, claim_ids, node, graph, statement, agreement, role)
NEW = []


def row(r, ids, node, graph, stmt, agr, role):
    assert "|" not in stmt, r
    NEW.append((r, ids, node, graph, stmt, agr, role))


# philosophy
row("DEFENSE-185", c(3), "DEFENSE.SECRETS", P, "Reject the entire JWT if any cryptographic operation in it fails to validate, and reject it if any validation step of the token specification fails.", "consensus", "decision")
row("DEFENSE-186", c(18), "DEFENSE.INJECTION.5", P, "Disable document type definitions (reject DOCTYPE) when parsing untrusted XML; where DTDs are required, disable external entity resolution and external DTD loading and limit entity expansion.", "consensus", "decision")
row("DEFENSE-187", c(23), "DEFENSE.HOST.3", P, "Never let CR, LF or NUL reach an HTTP field value: they are invalid and dangerous, and a recipient must reject the message or replace each with a space.", "single-source", "decision")
row("DEFENSE-188", c(31), "DEFENSE.INJECTION.1", P, "Template injection is a server-side code-execution class, unlike XSS: it reaches server internals and can give remote code execution; one published case study reached arbitrary command execution through a template context (T3 research evidence).", "single-source", "fact")
row("DEFENSE-189", c(59), "DEFENSE.ORIGIN", P, "Do not treat CSRF defences as sufficient where cross-site scripting exists: script running in the page can read tokens and send same-origin requests, so it defeats every CSRF mitigation.", "single-source", "decision")
# defaults: tokens
N21, N22 = "PIG-JS.DEFENSE.SECRETS.2.1", "PIG-JS.DEFENSE.SECRETS.2.2"
row("DEFENSE-190", c(1), N21, D, "Verify a JWT against an algorithm allowlist fixed by the caller or by configuration, and never let the token's own header choose the verification algorithm.", "consensus", "decision")
row("DEFENSE-191", c(2), N21, D, "Never accept an unsecured JWT (alg none); the verifier's allowlist must not contain None.", "consensus", "decision")
row("DEFENSE-192", "-", N21, D, "Belief rejected: a JWT with a valid-looking header can be trusted without a signature check (refuted by four sources on algorithm confusion and unsecured tokens).", "-", "rejected")
row("DEFENSE-193", c(4), N21, D, "Take the key material for validating a token from trusted pre-configured sources for the issuer, never from a source the token itself names.", "single-source", "decision")
row("DEFENSE-194", c(5), N21, D, "Validate that the keys used for a token belong to its issuer when it carries an iss claim, and reject a token whose iss is missing where the deployment relies on it.", "consensus", "decision")
row("DEFENSE-195", c(6), N21, D, "Validate the audience: accept a token only if the recipient is named in aud, and reject it when aud is absent.", "consensus", "decision")
row("DEFENSE-196", c(7), N21, D, "Accept a token only while the verification time lies inside its validity span, and require exp where tokens grant API access.", "consensus", "decision")
row("DEFENSE-197", c(8), N21, D, "Check that a token is of the correct type and meant for the intended purpose before accepting its contents.", "single-source", "decision")
row("DEFENSE-198", c(9), N21, D, "Do not let one verification call accept both symmetric and asymmetric algorithms for the same key material; prefer signatures over MACs.", "consensus", "decision")
row("DEFENSE-199", c(15), N21, D, "Do not use a human-memorizable password directly as the key of a keyed MAC such as HS256.", "single-source", "decision")
row("DEFENSE-200", c(17), N21, D, "Belief rejected: the JWT specification requires accepting alg none. RFC 7519 section 8 makes HS256 and none mandatory to implement for libraries; RFC 8725 narrows what a consumer accepts, so a stand-alone read of section 8 does not settle algorithm policy.", "consensus", "rejected")
row("DEFENSE-201", c(16), N21, D, "Revocation and logout are a separate design question: a JWT stays valid until it expires, so a denylist of server-issued identifiers or a token status list is needed to cut it short. Session architecture is owned by web_architecture.", "consensus", "deferred")
row("DEFENSE-202", c(10), N22, D, "Run jsonwebtoken 9.0.0 or later and do not set allowInvalidAsymmetricKeyTypes, which exists only for backwards compatibility.", "consensus", "decision")
row("DEFENSE-203", c(11), N22, D, "Pass an explicit algorithms option to jsonwebtoken verify: when it is omitted the accepted set is inferred from the key type (inferred from the library's documented defaults and the caller-fixed allowlist rule).", "consensus", "decision")
row("DEFENSE-204", c(12), N22, D, "Never use jsonwebtoken decode on untrusted tokens as if it were verification: it does not check the signature.", "single-source", "decision")
row("DEFENSE-205", "-", N22, D, "Belief rejected: reading a decoded JWT payload is safe without verifying it; decode only parses (jsonwebtoken documentation).", "-", "rejected")
row("DEFENSE-206", c(13), N22, D, "Fact (jose v6 documentation): in jwtVerify the algorithms option is optional and defaults to all algorithms applicable to the key, alg none is never accepted, and the issuer and audience options require the claim to be present.", "single-source", "fact")
row("DEFENSE-207", c(14), N22, D, "Pass algorithms to jose jwtVerify so the accepted set is the one the application chose rather than everything the key allows (inferred from the jose default and the caller-fixed allowlist rule).", "consensus", "decision")
# defaults: templates
T13, T14 = "PIG-JS.DEFENSE.INJECTION.1.3", "PIG-JS.DEFENSE.INJECTION.1.4"
row("DEFENSE-208", c(30), T13, D, "Never build a template from untrusted input; where there is no alternative, sanitize or strictly validate whatever untrusted input enters template creation.", "consensus", "decision")
row("DEFENSE-209", c(38), T13, D, "Sanitize or disable user-supplied scriptable or expression template-language content such as Markdown, CSS or XSL stylesheets, and BBCode.", "single-source", "decision")
row("DEFENSE-210", c(32), T13, D, "Acceptable only when user-supplied templates cannot be avoided: use a trivial template engine such as Mustache and sandbox the engine in a locked-down container as a complementary measure (the author's position at T3; the Handlebars guide names isolation and allowlisted helpers instead).", "single-source", "acceptable-when")
row("DEFENSE-211", c(33), T14, D, "Do not use triple-stash or return SafeString for untrusted values in Handlebars, and do not relax prototype-property access or enable allowCallsToHelperMissing.", "single-source", "decision")
row("DEFENSE-212", c(34), T14, D, "Treat Handlebars escaping as covering the HTML context only, and give templates from users size and depth limits and process isolation, since they are untrusted programs for resource consumption.", "consensus", "decision")
row("DEFENSE-213", c(35), T14, D, "Compile only ASTs that Handlebars produced from trusted template source, validate that compile arguments are strings, use the runtime-only build when templates are precompiled, and run Handlebars 4.7.9 or later.", "consensus", "decision")
row("DEFENSE-214", c(36), T14, D, "Never give end users direct access to EJS rendering, templates or render options: EJS is effectively a JavaScript runtime, so this is misuse and out of scope of its security policy; its default escape covers HTML and quoted attributes only.", "single-source", "decision")
row("DEFENSE-215", c(37), T14, D, "Run EJS 3.1.7 or later: an attacker-controlled settings[view options][outputFunctionName] overwrote the output function name with an OS command executed at template compilation (CVE-2022-29078).", "single-source", "decision")
row("DEFENSE-216", c(39), T14, D, "Open: no admitted T1 states injection rules for template engines other than Handlebars and EJS (Pug, Nunjucks and others), so engine-specific rules can be given only for those two.", "single-source", "fact")
# paths
N41 = "PIG-JS.DEFENSE.INJECTION.4.1"
row("DEFENSE-217", c(76), N41, D, "Never test containment by a raw string-prefix comparison of resolved paths: a sibling directory sharing the prefix passes, as /app/static-secret passes against /app/static (CVE-2026-48049 in @hapi/inert, fixed in 7.1.1).", "single-source", "decision")
row("DEFENSE-218", c(78), N41, D, "Do not assume path.resolve(base, input) stays under base: segments are processed right to left and an absolute input replaces everything before it, so check the resolved result against the base.", "single-source", "decision")
row("DEFENSE-219", c(80), N41, D, "Fact (Node threat model): untrusted file paths passed to fs APIs without validation are not counted as a Node vulnerability; path validation is the application's job.", "single-source", "fact")
# uploads
U5, U6 = "PIG-JS.DEFENSE.INJECTION.4.5", "PIG-JS.DEFENSE.INJECTION.4.6"
row("DEFENSE-220", c(40), U5, D, "Allow only listed file extensions, check that content matches the extension, and never trust the client-supplied Content-Type.", "consensus", "decision")
row("DEFENSE-221", c(46), U5, D, "Decode and re-encode images and scan or sandbox untrusted files before serving or processing them.", "consensus", "decision")
row("DEFENSE-222", c(48), U5, D, "Open: no admitted source gives a JavaScript recipe for checking an upload's content signature; only language-neutral rules exist.", "single-source", "fact")
row("DEFENSE-223", c(41), U6, D, "Name stored files with a server-generated name and never build a path from the uploaded file name; if a client name must be used, validate it strictly.", "consensus", "decision")
row("DEFENSE-224", c(42), U6, D, "Store uploads on a different server or outside the web root, and never execute files uploaded by untrusted input as server-side code.", "consensus", "decision")
row("DEFENSE-225", c(43), U6, D, "Set explicit upload limits (file size, file count, fields, parts, quotas), because busboy and multer default fileSize, files and parts to Infinity.", "consensus", "decision")
row("DEFENSE-226", c(44), U6, D, "Never add multer as global middleware: an attacker could upload files to a route the application did not anticipate.", "single-source", "decision")
row("DEFENSE-227", c(45), U6, D, "Check compressed uploads against a maximum uncompressed size and file count before uncompressing, and bound the pixel size of uploaded images.", "single-source", "decision")
row("DEFENSE-228", c(47), U6, D, "Validate or ignore user-submitted file names, give an explicit Content-Disposition file name, and encode or sanitize names served in headers or attachments.", "single-source", "decision")
# XML
X54 = "PIG-JS.DEFENSE.INJECTION.5.4"
row("DEFENSE-229", c(19), X54, D, "Treat a parser's missing or unsupported security setting as a configuration failure, and also restrict external access in XInclude, schema validation and style sheet processing, not only in parsing.", "single-source", "decision")
row("DEFENSE-230", c(20), X54, D, "Prefer XSD over DTD for schema validation of XML input.", "single-source", "decision")
row("DEFENSE-231", c(21), X54, D, "Keep fast-xml-parser at 4.5.4 or 5.3.6 or later and set processEntities to false when DOCTYPE entities are not needed, because unlimited text-entity expansion lets a small input freeze the process (CVE-2026-26278, a denial of service, not a file read).", "single-source", "decision")
row("DEFENSE-232", c(22), X54, D, "Open: which JavaScript XML parsers resolve external entities by default, and which options turn this off, is grounded by no admitted T1 source; no Node-specific XXE rule can be stated.", "single-source", "fact")
# v8.deserialize
N53 = "PIG-JS.DEFENSE.INJECTION.5.3"
row("DEFENSE-233", c(83), N53, D, "Fact: v8.deserialize(buffer) uses a DefaultDeserializer, calls readHeader then readValue, and its host-object reader takes a type index and byte length from the buffer and builds a typed array over the buffer or an aligned copy; the Node page and the source carry no trust requirement.", "consensus", "fact")
row("DEFENSE-234", c(84), N53, D, "Fact (V8 header comments): ValueDeserializer reads data written by ValueSerializer or a compatible implementation, the format is built for the HTML structured clone algorithm, and ReadHeader may fail if the format is invalid; no comment says the input may be hostile.", "single-source", "fact")
row("DEFENSE-235", c(85), N53, D, "Open: whether v8.deserialize is safe for untrusted bytes is stated by no admitted source (Node's v8 page, its security policy and the V8 header carry no statement); the decision above applies the general deserialization rules and claims no more.", "single-source", "fact")
# headers
H31, H32 = "PIG-JS.DEFENSE.HOST.3.1", "PIG-JS.DEFENSE.HOST.3.2"
row("DEFENSE-236", c(24), H31, D, "Rely on response.setHeader to throw ERR_INVALID_CHAR for illegal header names or values, and call http.validateHeaderName and http.validateHeaderValue to apply the same check before using a value elsewhere.", "consensus", "decision")
row("DEFENSE-237", c(25), H31, D, "Fact (Node source, main branch at extraction): the strict header-value check rejects every character outside HTAB, 0x20 to 0x7e and 0x80 to 0xff; the lenient check rejects only NUL, LF, CR and characters above 0xff.", "single-source", "fact")
row("DEFENSE-238", c(26), H31, D, "Sanitize every application-supplied string put into response.writeEarlyHints and other Node API arguments: Node counts CRLF in a link value as application misuse, not a Node vulnerability.", "single-source", "decision")
row("DEFENSE-239", c(27), H31, D, "Sanitize a user-influenced headers.host before passing it to undici, and run undici 5.19.1 or later (CVE-2023-23936).", "single-source", "decision")
row("DEFENSE-240", c(28), H31, D, "Validate input against an accept-known-good list, canonicalize and decode it once before validating, and construct HTTP headers carefully from non-validated data.", "single-source", "decision")
row("DEFENSE-241", c(29), H32, D, "Accept HTTP/2 and HTTP/3 requests only when header fields and values contain no CR, LF or CRLF, and neither send nor accept connection-specific fields such as Transfer-Encoding (ASVS 4.2.3 and 4.2.4, Level 3).", "single-source", "decision")
# framing
F21, F22 = "PIG-JS.DEFENSE.ORIGIN.2.1", "PIG-JS.DEFENSE.ORIGIN.2.2"
row("DEFENSE-242", c(63), F21, D, "Prevent framing with the CSP frame-ancestors directive on every response; where both frame-ancestors and X-Frame-Options are sent, browsers that support frame-ancestors ignore X-Frame-Options.", "consensus", "decision")
row("DEFENSE-243", c(64), F21, D, "Send frame-ancestors as an HTTP response header, never in a meta element: CSP does not support it there.", "single-source", "decision")
row("DEFENSE-244", c(67), F21, D, "Fact (RFC 7034): X-Frame-Options has the values DENY and SAMEORIGIN; ALLOW-FROM was an Internet Explorer extension never uniformly implemented, so it is not a way to name allowed framers.", "single-source", "fact")
row("DEFENSE-245", c(68), F21, D, "Send X-Frame-Options (DENY or SAMEORIGIN) as a fallback beside frame-ancestors, only where it states the same policy ('none' or 'self'); where frame-ancestors names other origins, omit it, because ALLOW-FROM cannot express them.", "contested", "decision")
row("DEFENSE-246", c(65), F22, D, "Do not rely on frame-busting JavaScript against clickjacking; simple scripts are defeated by double framing, onBeforeUnload manipulation and the sandbox attribute.", "single-source", "decision")
row("DEFENSE-247", "-", F22, D, "Belief rejected: a frame-busting script stops clickjacking; the script runs inside the frame context that the attacker controls (OWASP Clickjacking sheet).", "-", "rejected")
row("DEFENSE-248", c(66), F22, D, "Guard a sensitive double-click action with server-enforced transaction authorization, because DoubleClickjacking targets a top-level window where framing restrictions do not apply.", "single-source", "decision")
# CSRF
C61, C62, C63 = "PIG-JS.DEFENSE.ORIGIN.6.1", "PIG-JS.DEFENSE.ORIGIN.6.2", "PIG-JS.DEFENSE.ORIGIN.6.3"
row("DEFENSE-249", c(55), C61, D, "Protect every state-changing request that authenticated cookies can trigger with at least one primary CSRF defence: a synchronizer token, a signed double-submit cookie bound to the session, or a Fetch Metadata check.", "consensus", "decision")
row("DEFENSE-250", c(56), C61, D, "Allow a state-changing request only when Sec-Fetch-Site is same-origin or same-site and otherwise leave state unchanged, and keep an Origin or Referer check for browsers that do not send the header.", "consensus", "decision")
row("DEFENSE-251", c(58), C61, D, "Compare CSRF tokens with a constant-time function.", "single-source", "decision")
row("DEFENSE-252", c(69), C61, D, "Do not rely on a Sec-Fetch-Site check alone: make a synchronizer or signed double-submit token the primary defence and layer the Sec-Fetch-Site check and the Origin or Referer fallback behind it.", "contested", "decision")
row("DEFENSE-253", "-", C61, D, "Acceptable only when every browser the application supports sends Sec-Fetch-Site: a Sec-Fetch-Site check as the only primary defence (MDN's position).", "-", "acceptable-when")
row("DEFENSE-254", c(57), C62, D, "Never use GET, HEAD or OPTIONS for state-changing operations.", "consensus", "decision")
row("DEFENSE-255", c(60), C62, D, "Rely on a custom request header or a non-simple Content-Type for an API endpoint, and so on a CORS preflight instead of a token, only when no request that triggers no preflight can reach the functionality.", "consensus", "decision")
row("DEFENSE-256", c(61), C63, D, "Use SameSite as defence in depth, set per cookie purpose, and do not rely on Lax for protection against anything but unsafe methods.", "consensus", "decision")
row("DEFENSE-257", c(62), C63, D, "Do not use csurf for new Express code: the repository is archived and read-only with no replacement named, and the Express Technical Committee calls it long difficult to maintain and better handled through frameworks or custom implementations.", "single-source", "decision")
row("DEFENSE-258", "-", C63, D, "Belief rejected: csurf is the standard CSRF middleware for Express; its repository is archived and read-only.", "-", "rejected")
# URL validation
N23 = "PIG-JS.DEFENSE.DOM.2.3"
row("DEFENSE-259", c(70), N23, D, "Parse an untrusted URL with the WHATWG URL API and treat URL.canParse as a test of parsability only, not of permission: it returns true exactly where the URL constructor would succeed.", "consensus", "decision")
row("DEFENSE-260", c(71), N23, D, "Allow a destination only by comparing the parsed scheme, canonical host and effective port with an explicit allowlist, reject userinfo and ambiguous input, never match by raw prefix or suffix, and redirect with the validated URL rather than a transformed one.", "consensus", "decision")
row("DEFENSE-261", c(72), N23, D, "Prefer a server-side mapping from a short id or token to the full target URL over accepting a URL from the user, and avoid redirects and forwards where possible.", "single-source", "decision")
row("DEFENSE-262", c(73), N23, D, "Disallow dangerous URL protocols such as javascript: and data: when building URLs from untrusted data, and encode the data for its URL context.", "single-source", "decision")
row("DEFENSE-263", c(74), N23, D, "Use a URL parser that agrees with the consumer of the URL, meaning the redirect API and browser URL interpretation, because a validator and a consumer that parse differently can be made to disagree (inferred; no admitted source documents specific differentials).", "consensus", "decision")
row("DEFENSE-264", c(75), N23, D, "Open: parser differential examples for URL validation (specific inputs that two parsers read differently) are grounded by no admitted source; the rules above are stated without examples.", "single-source", "fact")
# fetch redirects
N64 = "PIG-JS.DEFENSE.INJECTION.6.4"
row("DEFENSE-265", c(86), N64, D, "Fact (Node globals page): Node's built-in fetch is based upon undici, the bundled undici version is given by process.versions.undici, and the page documents no redirect or header-stripping behaviour for fetch.", "single-source", "fact")
row("DEFENSE-266", c(87), N64, D, "Fact (undici main branch, unpinned): the fetch redirect step returns a network error at redirect count 20, removes authorization, proxy-authorization, cookie and host on a cross-origin redirect, and turns POST on 301 or 302 and any method other than GET or HEAD on 303 into GET with a null body.", "single-source", "fact")
row("DEFENSE-267", c(88), N64, D, "Keep undici current and do not assume redirect header stripping covers every credential header: fetch did not clear cookie (before 5.26.2) or Proxy-Authorization (up to 5.28.2 and 6.0.0 to 6.6.0), and undici.request, stream, pipeline and dispatch did not clear Authorization or Proxy-Authorization (before 5.28.4 and 6.11.1).", "consensus", "decision")
row("DEFENSE-268", c(89), N64, D, "Fact (undici documentation): RedirectHandler follows 300, 301, 302, 303, 307 and 308 up to maxRedirections, does not replay consumed bodies, strips headers that refer to the original URL on every hop, and offers stripHeadersOnRedirect, stripHeadersOnCrossOriginRedirect (default null) and throwOnMaxRedirect (default false); it describes the dispatcher handler, not Node's global fetch.", "single-source", "fact")
# dependencies
row("DEPENDENCIES-085", c(49), "DEPENDENCIES.THREATS.2", P, "Typosquatting is the main technique in published malicious-package data: 61 percent of 174 malicious packages mimicked existing names, across three package ecosystems taken together (DIMVA 2020, T2).", "single-source", "fact")
row("DEPENDENCIES-086", c(51), "PIG-JS.DEPENDENCIES.INSTALL.5", D, "Maintain an inventory or SBOM of third-party libraries that checks components come from trusted repositories, and include dependencies and their transitive dependencies only from the expected repository, with no dependency confusion risk (ASVS 15.1.2, Level 2, and 15.2.4, Level 3).", "single-source", "decision")
row("DEPENDENCIES-087", c(50), "PIG-JS.DEPENDENCIES.SCREEN.3", D, "Fact (npm documentation): the registry states that it detects typosquat attacks and blocks the publishing of such packages, and encourages scoped packages so a private package is not substituted from the public registry; the same page says it cannot detect dependency confusion directly.", "single-source", "fact")
row("DEPENDENCIES-088", c(52), "PIG-JS.DEPENDENCIES.SCREEN.3", D, "Fact (T3 preprint, venue unconfirmed): one published screening method flags a package whose name is lexically close to a popular package while its own popularity is below a threshold, and reported warnings on about 0.5 percent of installs with 2.5 percent time overhead; no claim that a tool should be used.", "single-source", "fact")
row("DEPENDENCIES-089", c(53), "PIG-JS.DEPENDENCIES.SCREEN.3", D, "Fact (T3 preprint, venue unconfirmed): name similarity alone is not enough, since package confusion includes names that resemble the original semantically as well as syntactically; one metadata-based detector cut false positives from 80 to 28 percent at 14 seconds of added analysis.", "single-source", "fact")
row("DEPENDENCIES-090", c(54), "PIG-JS.DEPENDENCIES.SCREEN.3", D, "Open: no admitted T1 states a typosquatting screening procedure for adding a dependency; the T1 sources give registry facts and repository provenance only, and the screening methods rest on one T3 paper and one T3 preprint.", "single-source", "fact")

# existing rows rewritten or extended: row id -> new line cells
REWRITE = {
    "DEFENSE-015": dict(claim_ids=f"RUNSEC-C28, {c(81)}"),
    "DEFENSE-139": dict(statement="Validate URLs by parsing with the URL parser and allowlisting scheme and origin, not by substring tests.", role="decision"),
    "DEFENSE-161": dict(claim_ids=f"RUNSEC-C27, {c(77)}, {c(79)}",
                        statement="Belief rejected: path.normalize or path.isAbsolute sanitizes user paths. isAbsolute tests only whether the literal path is absolute (and /baz/.. is absolute); normalize resolves .. and . lexically and on POSIX may remove .. segments in ways that change how the file system resolves the path, so a normalized string is not a canonical path; neither checks containment or symlinks."),
    "DEFENSE-169": dict(claim_ids=f"SRVSEC-C55, {c(82)}",
                        statement="Open: the canonical containment recipe (resolve, follow symlinks with realpath, then test that the result starts with the base directory plus a separator) is stated by no admitted source: the pieces are placed on the containment check node (a raw prefix test passes a sibling directory, resolve lets an absolute input replace the base, normalize is lexical), the realpath and O_NOFOLLOW entries of the Node fs page could not be read, and the separator-aware test is stated nowhere; the recipe stays inferred, as the canonicalization row records."),
    "DEFENSE-173": dict(statement="Never pass an untrusted buffer to v8.deserialize unless a trusted party's integrity check (for example an HMAC) over it has been verified, and copy the result into a new object from validated fields instead of using it directly.", role="decision"),
    "DEFENSE-182": dict(claim_ids=f"SRVSEC-C37, {c(90)}",
                        statement="Pass redirect: 'error' to fetch when the destination derives from untrusted input and no redirect is expected, and redirect: 'manual' with revalidation of every Location target when one is, because fetch follows redirects by default.", role="decision"),
}

# ------------------------------------------------------------------------------------------------ skeleton nodes
# uid: (name, intent, epistemic)
NODES = {
    N21: ("Token and JWT verification", "A token is accepted only after the verifier applies its own fixed policy: allowed algorithms, trusted pre-configured keys bound to the issuer, audience, validity time and type; nothing in the token chooses any of them.", "known"),
    N22: ("Token library settings", "The JavaScript token libraries accept more than the policy allows unless told otherwise: the verify call gets an explicit algorithm list, the library is current, and decoding is never verification.", "known"),
    T13: ("Template injection", "A template is code: untrusted input never becomes template source, and user-supplied expression content is sanitized or off.", "known \\| unvalidated: the acceptable-when row rests on one T3 source (the author's position)"),
    T14: ("Handlebars and EJS", "The two template engines with admitted security guidance are used within what their own documents state: no unescaped output of untrusted values, no untrusted ASTs, no end-user access to EJS, current versions.", "known"),
    U5: ("Upload content checks", "An uploaded file is accepted by an extension allowlist and a server-side content check and is re-encoded or scanned before use; the client's Content-Type is never trusted.", "known"),
    U6: ("Upload storage, names and limits", "Uploads get server-generated names, live outside the web root, are never run as code, and are bounded in size, count and unpacked size before the file is accepted.", "known"),
    X54: ("XML and external entities", "XML from outside is parsed with DTDs and external entity resolution off, schema validation uses XSD, and a missing hardening setting is a failure, not a fallback.", "known"),
    H31: ("Header field values", "No CR, LF or NUL reaches a header name or value, whether the application sets a header or passes a value to a client library; Node's own check is relied on and applied before a value is reused.", "known"),
    H32: ("Connection-specific fields", "HTTP/2 and HTTP/3 requests are accepted only without CR, LF or CRLF in fields and without connection-specific fields.", "known"),
    F21: ("Framing of the own page", "The page forbids being framed by other origins with frame-ancestors on every response, sent as a header, with X-Frame-Options only as a fallback that states the same policy.", "known \\| conflict: frame-ancestors alone, ASVS 3.4.6 and CSP3 with RFC 7034 (the directive supersedes the header) \\| unvalidated: the same-policy condition for the fallback is inferred from the ALLOW-FROM support gap (SECGAP2-C67)"),
    F22: ("Frame-busting and double clicks", "Frame-busting scripts are not a defence, and a sensitive action behind a double click needs server-enforced transaction authorization.", "known"),
    "PIG-JS.DEFENSE.ORIGIN.6": ("Cross-site request forgery", "A state-changing request that authenticated cookies can trigger from another site is accepted only with an unforgeable token or a trusted origin signal, never through a safe method, and never on one layer where script injection exists.", "known"),
    C61: ("Primary defence", "A synchronizer or signed double-submit token is the primary defence, layered with the Sec-Fetch-Site check and an Origin or Referer fallback; tokens are compared in constant time.", "known \\| conflict: a Sec-Fetch-Site check alone is a primary defence, MDN"),
    C62: ("Methods and API endpoints", "Safe methods never change state, and an API that relies on CORS preflight makes sure no request can reach it without one.", "known"),
    C63: ("SameSite and CSRF libraries", "SameSite is defence in depth set per cookie purpose, and csurf is not adopted for new code.", "known"),
    "PIG-JS.DEPENDENCIES.INSTALL.5": ("Expected repository and inventory", "Third-party components, direct and transitive, are inventoried and each is checked to come from its expected repository, with no dependency confusion risk.", "known"),
    "PIG-JS.DEPENDENCIES.SCREEN.3": ("Typosquatting screening", "Whether and how a package name is screened against popular names before adoption; the evidence is recorded and no procedure is chosen.", "undecided \\| missing: no admitted T1 source states a screening procedure for adding a dependency; the screening methods rest on one T3 paper and one T3 preprint"),
}
# insert each new node after this existing node row (breadth-first keeps L3 before L4)
AFTER = {
    "PIG-JS.DEFENSE.ORIGIN.6": "PIG-JS.DEFENSE.ORIGIN.5",
    N21: "PIG-JS.DEFENSE.INJECTION.6.4", N22: N21, T13: N22, T14: T13, U5: T14, U6: U5, X54: U6, H31: X54, H32: H31,
    F21: H32, F22: F21, C61: F22, C62: C61, C63: C62,
    "PIG-JS.DEPENDENCIES.INSTALL.5": "PIG-JS.DEPENDENCIES.INSTALL.4",
    "PIG-JS.DEPENDENCIES.SCREEN.3": "PIG-JS.DEPENDENCIES.SCREEN.2",
}

# existing node rows edited: uid -> dict(name/intent/epistemic)
EDIT = {
    "PIG-JS.DEFENSE.DOM.2.3": dict(
        name="URL validation by parsing",
        intent="A URL is validated by parsing it and comparing scheme, canonical host and effective port with an explicit allowlist, with userinfo and dangerous protocols refused, rather than by substring tests.",
        epistemic="known \\| unvalidated: inferred from DOMSEC-C57, SECGAP2-C70, C71, C73 and C74, each step grounded by a claim but the composed rule stated whole by no source; parser-differential examples are open (SECGAP2-C75)"),
    "PIG-JS.DEFENSE.INJECTION.4.4": dict(
        epistemic="undecided \\| missing: no admitted source states the symlink-resolving Node call (fs.realpath) or the separator-aware containment test; the pieces that are grounded sit on PIG-JS.DEFENSE.INJECTION.4.1"),
    "PIG-JS.DEFENSE.INJECTION.5.3": dict(
        intent="A buffer reaches v8.deserialize only after a trusted party's integrity check has been verified, and the result is copied into a new object from validated fields; whether the function is safe on its own is stated by no admitted source.",
        epistemic="known \\| unvalidated: inferred from SECGAP2-C83, C84, C85, SRVSEC-C44 and the general deserialization rules (SRVSEC-C45, RUNSEC-C44); whether v8.deserialize is safe for untrusted bytes is open"),
    "PIG-JS.DEFENSE.INJECTION.6.4": dict(
        intent="Node's fetch is told what to do with a redirect (error when none is expected, manual with revalidation otherwise), its automatic header stripping is not relied on, and undici is kept current.",
        epistemic="known \\| unvalidated: inferred from SECGAP2-C86, C87, C88, C90 and SRVSEC-C35, C36, C37; how Node's fetch treats redirect manual and which undici version a release bundles are stated by no Node page"),
    "PIG-JS.DEFENSE.SECRETS.2": dict(
        intent="SubtleCrypto designs are reviewed by a knowledgeable person, encryption uses authenticated modes, and tokens are verified on the verifier's terms."),
    "PIG-JS.DEFENSE.HOST.3": dict(
        intent="The strict HTTP parser stays on, the front end normalizes ambiguous requests, and no control character reaches a header."),
    "PIG-JS.DEFENSE.ORIGIN.2": dict(
        intent="Untrusted and vendor content lives in sandboxed iframes from a separate origin; target=_blank links carry rel=noopener noreferrer explicitly; the own page refuses to be framed."),
    "PIG-JS.DEFENSE.INJECTION.4": dict(
        intent="A path from input is resolved and checked inside its base, archive entries never choose their location, uploaded files are named, stored and bounded by the server, and the file is opened without a prior check."),
    "PIG-JS.DEFENSE.INJECTION.4.1": dict(
        intent="A path is canonicalized, symlinks resolved, and only then compared to the base directory, never by a raw string-prefix test."),
    "DEFENSE.SECRETS": dict(
        intent_append=" A token is accepted only on the recipient's terms, never on the token's own."),
    "DEFENSE.INJECTION.5": dict(
        intent_append=" Its parser loads nothing from outside the data."),
    "DEFENSE.HOST.3": dict(
        intent_append=" A control character in a header value is such a disagreement."),
    "PIG-JS.DEFENSE.ORIGIN": dict(
        intent_append=" Forged cross-site requests are refused by the page's own checks."),
}

# ------------------------------------------------------------------------------------------------ links
WITHIN = [
    (N22, N21, "refines", "The library settings carry the algorithm allowlist and the key rules of the verification policy into each call."),
    (C61, "PIG-JS.DEFENSE.SECRETS.4", "requires", "A CSRF token is a secret compared in constant time with the same built-in function."),
    (C62, C61, "refines", "Method discipline and preflight reliance narrow what the token or origin check has to cover."),
    (F22, F21, "refines", "A double click acts in a top-level window, where the framing restrictions of the page do not apply."),
    (T14, T13, "refines", "The engine-specific rules apply the no-untrusted-template rule to the two engines with admitted guidance."),
    (U6, N41, "requires", "A client file name that must be used goes through the containment check before any path is built."),
    (U6, "PIG-JS.DEFENSE.INJECTION.4.2", "requires", "Size and file-count limits on compressed uploads apply before the archive is extracted."),
    ("PIG-JS.DEFENSE.DOM.2.2", N23, "requires", "A redirect target is compared with the allowlist only after it is parsed."),
    (N64, "PIG-JS.DEFENSE.INJECTION.6.3", "refines", "The fetch redirect modes are how the revalidation rule is applied in Node."),
    (H32, H31, "refines", "HTTP/2 and HTTP/3 add the connection-specific fields to what must never reach a header."),
    ("PIG-JS.DEPENDENCIES.INSTALL.5", "PIG-JS.DEPENDENCIES.INSTALL.4", "requires", "The expected-repository check covers the namespaces that an owned scope does not close."),
    ("PIG-JS.DEPENDENCIES.SCREEN.3", "PIG-JS.DEPENDENCIES.INSTALL.5", "requires", "A package that passes a name screen still has to come from the expected repository."),
]
ACROSS = [
    (N21, "PIG-JS.CONTRACTS.BOUNDARY", "requires", "Token claims are untrusted data, parsed and validated at the trust boundary before they are used."),
    (X54, "PIG-JS.CONTRACTS.BOUNDARY", "requires", "XML is parsed into validated shapes at the boundary, and XSD validation is the shape check."),
    (T14, "PIG-JS.DEPENDENCIES.UPDATE.3", "requires", "The version floors for Handlebars and EJS are enforced by the audit and update policy owned by DEPENDENCIES."),
    (N64, "PIG-JS.DEPENDENCIES.UPDATE.3", "requires", "Keeping undici current is the update policy owned by DEPENDENCIES."),
]
INTER_SENT = "The default renders the principle in JavaScript."
INTER = [
    (N21, "DEFENSE.SECRETS"), (N22, "DEFENSE.SECRETS"), (T13, "DEFENSE.INJECTION.1"), (T14, "DEFENSE.INJECTION.1"),
    (U5, "DEFENSE.INJECTION.4"), (U6, "DEFENSE.INJECTION.4"), (X54, "DEFENSE.INJECTION.5"), (H31, "DEFENSE.HOST.3"),
    (H32, "DEFENSE.HOST.3"), (F21, "DEFENSE.ORIGIN"), (F22, "DEFENSE.ORIGIN"), ("PIG-JS.DEFENSE.ORIGIN.6", "DEFENSE.ORIGIN"),
    (C61, "DEFENSE.ORIGIN"), (C62, "DEFENSE.ORIGIN"), (C63, "DEFENSE.ORIGIN"), (N23, "DEFENSE.DOM.2"),
    (N53, "DEFENSE.INJECTION.5"), (N64, "DEFENSE.INJECTION.6"),
    ("PIG-JS.DEPENDENCIES.INSTALL.5", "DEPENDENCIES.THREATS.2"), ("PIG-JS.DEPENDENCIES.SCREEN.3", "DEPENDENCIES.THREATS.2"),
    ("PIG-JS.DEPENDENCIES.SCREEN.3", "DEPENDENCIES.ADMISSION.3"),
]
PLANNED = [
    (F21, "pig-web-defaults", "response header deployment of frame-ancestors and the CSP policy around it in web_architecture (SECGAP2-C63, C64)"),
    (C63, "pig-web-defaults", "cookie attribute design and session architecture beside SameSite in web_architecture (SECGAP2-C61)"),
    (N21, "pig-web-defaults", "token revocation, logout and session design in web_architecture (SECGAP2-C16)"),
]

# ------------------------------------------------------------------------------------------------ judge records
JUDGE_DEFENSE = """
**PIG-JS.DEFENSE.SECRETS.2.1** Token and JWT verification
- Positions: (a) the verifier fixes algorithm, key source, issuer, audience, validity and type (RFC 8725 3.1, 3.3, 3.8, 3.9; ASVS 9.1.2, 9.1.3, 9.2.1 to 9.2.3; OWASP JWT sheets); (b) trust the token's own alg and key hints. Claims SECGAP2-C01, C02, C04 to C09, C15, C17 (C16 deferred).
- Forces: Forgery resistance against the convenience of letting tokens describe themselves.
- Decision: (a), every check as a MUST; an unsecured token never; one call never accepts both symmetric and asymmetric algorithms for one key.
- Rejected: (b): refuted by the algorithm-confusion and alg-none attacks; wins under no grounded condition. Reading RFC 7519 section 8 alone as the algorithm policy: it states what libraries implement, not what a consumer accepts.

**PIG-JS.DEFENSE.SECRETS.2.2** Token library settings
- Positions: (a) pass an explicit algorithms list to jsonwebtoken verify and to jose jwtVerify; (b) rely on the per-key-type default (jsonwebtoken) or all algorithms applicable to the key (jose). Claims SECGAP2-C10 to C14.
- Forces: The caller-fixed allowlist rule of the node above against less code.
- Decision: (a); jsonwebtoken 9.0.0 or later; decode is never verification. C11 and C14 are inferred from the library defaults plus the allowlist rule, since no source tells the caller to always pass the option.
- Rejected: (b): wins only where the key type already fixes the single algorithm the application intends.

**PIG-JS.DEFENSE.INJECTION.1.3** Template injection
- Positions: (a) never build a template from untrusted input; (b) allow user templates in a trivial engine inside a sandbox (Kettle, T3); (c) isolation and allowlisted helpers (Handlebars guide). Claims SECGAP2-C30, C32, C38 (C31 on the philosophy node).
- Forces: Removal of the code-execution class against products that let users write templates.
- Decision: (a) as the MUST; (b) kept as acceptable-when user templates cannot be avoided, flagged as one T3 position that concedes execution may happen.
- Rejected: (b) as the rule: it accepts code execution and rests on one T3 author; wins when the product requires user-written templates. (c): kept as the Handlebars-specific rule of the next node.

**PIG-JS.DEFENSE.INJECTION.1.4** Handlebars and EJS
- Positions: engine documents and advisories: Handlebars (security page, CVE-2026-33937), EJS (security policy, CVE-2022-29078). Claims SECGAP2-C33 to C37 (C39 open).
- Forces: Exact vendor statements against the lack of guidance for other engines.
- Decision: each statement as a MUST on its engine; version floors as MUST. Engine facts about those two engines only.
- Rejected: Extending the rules to Pug, Nunjucks or others: no admitted T1 states them (C39); wins when such a source is admitted.

**PIG-JS.DEFENSE.INJECTION.4.5** Upload content checks
- Positions: (a) extension allowlist plus content check plus re-encoding or scanning (OWASP File Upload, ASVS 5.2.2, 5.4.3); (b) trust Content-Type or name. Claims SECGAP2-C40, C46 (C48 open).
- Forces: Server-side proof against client-supplied labels.
- Decision: (a). The JavaScript signature-check recipe is open (C48), so the rule is language-neutral.
- Rejected: (b): the client controls both; wins under no condition.

**PIG-JS.DEFENSE.INJECTION.4.6** Upload storage, names and limits
- Positions: (a) server-generated names, storage outside the web root, explicit limits, no global multer, decompression bounds, encoded served names (OWASP File Upload, ASVS 5.2.1, 5.2.3, 5.2.6, 5.3.1, 5.3.2, 5.4.1, 5.4.2, busboy and multer documentation); (b) library defaults. Claims SECGAP2-C41 to C45, C47.
- Forces: Containment and bounded cost against defaults of Infinity for file size, files and parts.
- Decision: (a), each as a MUST.
- Rejected: (b): the defaults are unbounded; wins under no grounded condition.

**PIG-JS.DEFENSE.INJECTION.5.4** XML and external entities
- Positions: (a) DTDs off, external entities and external DTDs off, partial hardening a failure, XSD over DTD (OWASP XXE and XML Security sheets, ASVS 1.5.1); (b) parser defaults. Claims SECGAP2-C19 to C21 (C18 on the philosophy node, C22 open).
- Forces: Safety against not knowing which Node parsers resolve entities (C22).
- Decision: (a); fast-xml-parser version floor and processEntities false as a separate denial-of-service rule.
- Rejected: (b): Node parser defaults are not grounded, so they cannot be relied on; wins when a source states a parser's defaults.

**PIG-JS.DEFENSE.HOST.3.1** Header field values
- Positions: (a) reject CR, LF and NUL, rely on Node's setHeader throw, validate before reuse, sanitize arguments to other APIs (RFC 9110 5.5, Node http page, Node source, Node threat model, undici advisory, CWE-113). Claims SECGAP2-C24 to C28 (C23 on the philosophy node); (b) strip or replace characters silently.
- Forces: Rejection against repair; the application owns validation (C26).
- Decision: (a).
- Rejected: (b): RFC 9110 allows replacing with a space for a recipient, but a sender that repairs hides the injection; wins for a recipient that must tolerate legacy clients.

**PIG-JS.DEFENSE.HOST.3.2** Connection-specific fields
- Positions: (a) accept HTTP/2 and HTTP/3 requests only without CR, LF, CRLF and without connection-specific fields (ASVS 4.2.3, 4.2.4, Level 3); (b) no rule. Claim SECGAP2-C29.
- Forces: Downgrade and smuggling safety against compatibility.
- Decision: (a), flagged single-source.
- Rejected: (b): wins for HTTP/1.1-only services, where 4.2.4 does not apply.

**PIG-JS.DEFENSE.ORIGIN.2.1** Framing of the own page
- Positions: (a) frame-ancestors on every response as a header (ASVS 3.4.6, OWASP Clickjacking sheet, CSP3); (b) frame-ancestors and X-Frame-Options together (OWASP lists both); (c) X-Frame-Options alone. Claims SECGAP2-C63, C64, C67, C68 (contested, C68).
- Forces: Coverage of older browsers against a second header that cannot express allowed framers.
- Decision (max rule): (a) plus a matching X-Frame-Options fallback where the policy is none or self; where other origins are allowed, omit it. The condition is inferred from the ALLOW-FROM support gap (C67).
- Rejected: frame-ancestors alone (ASVS, CSP3 and RFC 7034 hold that the directive supersedes): wins where every supported browser implements frame-ancestors. X-Frame-Options alone: ALLOW-FROM unsupported, loses to the directive.

**PIG-JS.DEFENSE.ORIGIN.2.2** Frame-busting and double clicks
- Positions: (a) no frame-busting reliance, server-enforced authorization for sensitive double-click actions (OWASP Clickjacking sheet). Claims SECGAP2-C65, C66; (b) a frame-busting script.
- Forces: A defence outside the attacker's frame context against a script inside it.
- Decision: (a).
- Rejected: (b): defeated by double framing, onBeforeUnload and the sandbox attribute; wins under no condition.

**PIG-JS.DEFENSE.ORIGIN.6.1** Primary defence
- Positions: MDN: at least one primary defence, a Fetch Metadata check being one; OWASP: token primary, Fetch Metadata as depth with an Origin or Referer fallback for browsers without the header. Claims SECGAP2-C55, C56, C58, C69 (contested, C69).
- Forces: Independence from browser support against one fewer mechanism.
- Decision (max rule): a synchronizer or signed double-submit token as the primary defence, the Sec-Fetch-Site check and the Origin or Referer fallback layered behind it; tokens compared in constant time. The first claim is the floor, the layering the choice.
- Rejected: a Sec-Fetch-Site check as the only primary defence (MDN): kept as acceptable-when every supported browser sends the header, a build judgment about the condition.

**PIG-JS.DEFENSE.ORIGIN.6.2** Methods and API endpoints
- Positions: (a) no state change through GET, HEAD or OPTIONS; preflight reliance only when no preflight-free request reaches the functionality (OWASP, MDN, ASVS 3.5.1 to 3.5.3). Claims SECGAP2-C57, C60.
- Forces: Safe methods and simple requests skip the cross-site protections.
- Decision: (a).
- Rejected: state change through a safe method: wins under no condition.

**PIG-JS.DEFENSE.ORIGIN.6.3** SameSite and CSRF libraries
- Positions: (a) SameSite as depth, per cookie purpose; csurf not for new code (archive notice, Express blog); (b) SameSite Lax as the defence; (c) csurf. Claims SECGAP2-C61, C62.
- Forces: Defence in depth against reliance on one cookie attribute; a maintained dependency against an archived one.
- Decision: (a).
- Rejected: (b): Lax withholds cookies only on cross-site requests with unsafe methods and does not cover client-side CSRF. (c): archived, no replacement named; wins under no condition for new code, and is a maintenance decision for existing code.

**PIG-JS.DEFENSE.DOM.2.3** URL validation by parsing
- Positions: (a) parse with the WHATWG URL API, compare parsed scheme, canonical host and effective port with an allowlist, reject userinfo, refuse javascript: and data:, use a parser that agrees with the consumer (URL Standard, OWASP Unvalidated Redirects sheet, ASVS 1.2.2); (b) substring or prefix tests; (c) legacy url.parse. Claims DOMSEC-C57, SECGAP2-C70 to C74 (C75 open).
- Forces: One parse, one verdict, against the cost of an allowlist.
- Decision: (a), composed from grounded steps; the former gap on the javascript: scheme is closed by C73.
- Rejected: (b): a prefix or suffix test accepts attacker hosts that begin or end with an allowed string. (c): see INJECTION.6.1. Specific parser differentials stay open (C75).

**PIG-JS.DEFENSE.INJECTION.5.3** v8.deserialize
- Positions: (a) apply the general deserialization rules to it: integrity check first, new object from validated fields (CWE-502, ASVS 15.1.5, SRVSEC-C45, RUNSEC-C44); (b) treat it as safe; (c) treat it as unsafe and forbid it. Claims SRVSEC-C44, SECGAP2-C83 to C85.
- Forces: Safety on an unstated question against forbidding a built-in on no evidence.
- Decision: (a). It claims no more than the sources: whether the function is safe for untrusted bytes stays open (C85).
- Rejected: (b): no source says so. (c): no source says so; wins if the Node or V8 documentation states that the format is unsafe.

**PIG-JS.DEFENSE.INJECTION.6.4** Node fetch redirect semantics
- Positions: (a) error when no redirect is expected, manual with revalidation otherwise, keep undici current, do not rely on header stripping (Fetch Standard modes via SRVSEC-C36, MDN values, undici redirect code and advisories, ASVS 15.3.2); (b) follow redirects automatically. Claims SRVSEC-C37, SECGAP2-C86 to C90.
- Forces: Revalidation of each hop against transparent following; the advisories show header stripping has been incomplete.
- Decision: (a); undici follows the Fetch Standard steps (C87), which carries the browser semantics of the modes over to Node by inference; Node's own pages are silent.
- Rejected: (b): wins only for known-trusted destinations.

**PIG-JS.DEFENSE.INJECTION.4.1** Containment check (slot 14 addition)
- Added: never a raw string-prefix comparison (CVE-2026-48049, claim SECGAP2-C76); path.resolve lets an absolute input replace the base (C78); isAbsolute and normalize facts merged into the rejected belief (C77, C79); Node leaves validation to the application (C80).
"""

JUDGE_DEPENDENCIES = """
#### PIG-JS.DEPENDENCIES.INSTALL.5 (Expected repository and inventory)

- Positions: (a) an inventory or SBOM that checks every component, direct and transitive, comes from its expected repository (ASVS 15.1.2, 15.2.4); (b) no inventory. Claim SECGAP2-C51.
- Forces: Repository provenance against the upkeep of an inventory.
- Decision: (a), flagged single-source (one ASVS pair, Levels 2 and 3). It states provenance, not a name-screening method.
- Rejected: (b): wins for a project with no third-party runtime dependencies.
"""

# ------------------------------------------------------------------------------------------------ decisions text
DECISIONS = """## Slot 14_secgap2: second security gap round (90 claims folded by patch)

Folded by `build/patch/14_secgap2/apply_patch.py` (never by `integrate.py`). Every claim is placed once: 90 of 90, 0 dropped. Rules
follow the fix conventions: constraints are rules only, facts go to design notes, single-source, inferred or open grounds carry
`unvalidated:`, and the philosophy graph names no JavaScript tools. Where every step of a rule is grounded by a claim, the rule is composed
and marked `known | unvalidated: inferred from <claims>`; where a step has no ground the node stays `undecided` with what is missing.

### G1. Placement under the six-child limit (weighty, inferred)

- Decision: no new L2 node under `PIG-JS.DEFENSE` (it already has six: DOM, ORIGIN, INJECTION, PROTOTYPE, SECRETS, HOST; I4 and A1 hold that
  seven is over the limit). The new topics sit under the nearest existing parent that has room: tokens under `SECRETS.2` (`.2.1`, `.2.2`),
  template injection under `INJECTION.1` (`.1.3`, `.1.4`), uploads under `INJECTION.4` (`.4.5`, `.4.6`, the sixth child is now full), XML
  under `INJECTION.5` (`.5.4`), header injection under `HOST.3` (`.3.1`, `.3.2`), clickjacking under `ORIGIN.2` (`.2.1`, `.2.2`), CSRF as the sixth
  child `ORIGIN.6` with three children, typosquatting under `DEPENDENCIES.SCREEN` (`.3`) and the repository inventory under `INSTALL` (`.5`).
  Philosophy: no new node; principle-level claims (C03, C18, C23, C31, C49, C59) became rows of `DEFENSE.SECRETS`, `DEFENSE.INJECTION.5`,
  `DEFENSE.HOST.3`, `DEFENSE.INJECTION.1`, `DEPENDENCIES.THREATS.2` and `DEFENSE.ORIGIN`, whose intents gained one clause where the new row needed it.
- Rejected: a seventh L2 `DEFENSE` child (for example `PROTOCOL`) holding tokens, headers and CSRF: cleaner by topic, but over the limit and
  it would split the tree again. Wins if the maintainer accepts seven L2 children or folds PROTOTYPE (3 children) elsewhere.
- Grounds: inferred (a judgment on cohesion). Placement of tokens under `SECRETS` and CSRF under `ORIGIN` is the weakest fit.

### G2. Nodes resolved from `undecided` (three decided, one kept)

- `PIG-JS.DEFENSE.DOM.2.3` (URL validation): decided. Steps all grounded: parse with the WHATWG URL API (C70, DOMSEC-C57), compare parsed scheme, host and port
  with an allowlist and reject userinfo and prefix matching (C71), refuse javascript: and data: (C73, which closes the former gap), parser agreement (C74, inferred). Marked
  `known | unvalidated: inferred from DOMSEC-C57, SECGAP2-C70, C71, C73 and C74`. Open: parser differential examples (C75).
- `PIG-JS.DEFENSE.INJECTION.5.3` (v8.deserialize): decided on the general rule only. No source says whether the function is safe (C85), so the rule applies the
  deserialization principle (integrity check first, new object from validated fields; SRVSEC-C45, RUNSEC-C44) and claims nothing more. Rejected: a ban (no source), a safe label (no source).
- `PIG-JS.DEFENSE.INJECTION.6.4` (fetch redirects): decided: redirect `error` or `manual` with revalidation, undici kept current, header stripping not relied on (C86 to C90, SRVSEC-C35 to C37).
  Flagged: the semantics of `manual` in Node are carried over from the Fetch Standard by inference (undici follows its steps, C87); Node documents none of it.
- `PIG-JS.DEFENSE.INJECTION.4.4` (Node containment recipe): stays undecided. The steps with a ground (never a raw prefix test, resolve lets an absolute input replace the base, normalize is lexical,
  canonicalize before comparing) are placed on `INJECTION.4.1`; the symlink-resolving Node call and the separator-aware test have none (C82; the Node fs `realpath` and `O_NOFOLLOW`
  entries could not be read). Settled by: a readable Node fs `realpath` entry plus a source stating the comparison, for example the hapi fix commit (late candidate LC-01).
  Note: the task named SRVSEC-C44 to C46 among the containment grounds; they are the deserialization claims and ground node 5.3, not 4.4.

### G3. Contested topic: X-Frame-Options beside frame-ancestors (C68; node `ORIGIN.2.1`)

- Decision (max rule): `frame-ancestors` on every response as a header, plus an `X-Frame-Options` fallback (`DENY` or `SAMEORIGIN`) only where it states the same policy; omit it where other origins are allowed.
- Positions: OWASP Clickjacking sheet: frame-ancestors preferred, X-Frame-Options also listed for older browsers; ASVS 3.4.6: frame-ancestors only; CSP3 and RFC 7034: the directive supersedes the header.
- Rejected: frame-ancestors alone, which wins where every supported browser implements the directive; X-Frame-Options alone, which loses to the directive and cannot name allowed framers (ALLOW-FROM unsupported, C67).
- Epistemic: `known | conflict: frame-ancestors alone, ASVS 3.4.6 and CSP3 with RFC 7034 | unvalidated: matching-policy condition inferred from C67`.

### G4. Contested topic: Sec-Fetch-Site alone as a CSRF defence (C69; node `ORIGIN.6.1`)

- Decision (max rule): a synchronizer or signed double-submit token is the primary defence; the Sec-Fetch-Site check and the Origin or Referer fallback are layers behind it.
- Positions: MDN: Fetch Metadata is one of the primary defences; OWASP: defence in depth behind a token, with an Origin or Referer fallback for browsers without the header.
- Rejected: Sec-Fetch-Site alone, kept as an `acceptable-when` row (every supported browser sends the header; the condition is the build's judgment, row without a claim). The consensus claim C55 (at least one primary defence) is the floor.
- Epistemic: `known | conflict: a Sec-Fetch-Site check alone is a primary defence, MDN`.

### G5. Other decisions

- Tokens (`SECRETS.2.1`, `.2.2`): every RFC 8725 and ASVS check is a MUST (consensus on the core); `jsonwebtoken` and `jose` settings are `.2.2`, with C11 and C14 inferred (no source says to always pass `algorithms`). Revocation (C16) is deferred to web_architecture, planned boundary link added.
- Template injection (`INJECTION.1.3`, `.1.4`): "never build a template from untrusted input" is the MUST; Kettle's trivial-engine-and-sandbox position (C32, one T3 source) is an `acceptable-when` row so the node does not become `risky`; engine rules exist for Handlebars and EJS only (C39 open).
- XML (`INJECTION.5.4`): DTDs off is on the philosophy node (principle level); the defaults node holds the three practice rules and records that no Node parser default is grounded (C22 open). fast-xml-parser's advisory is a denial of service by entity expansion, not an external-entity read.
- Uploads (`INJECTION.4.5`, `.4.6`): language-neutral rules (level `practice`, stack `principle`) are placed in the defaults graph by the extraction level, as in A2; the JavaScript signature-check recipe is open (C48).
- Header injection (`HOST.3.1`, `.3.2`): the CR, LF, NUL rule (C23, principle) is on `DEFENSE.HOST.3`; Node facts are rows of `.3.1`; the HTTP/2 and HTTP/3 rule is a separate leaf (ASVS Level 3, not a general HTTP/1.1 rule).
- Typosquatting: `DEPENDENCIES.SCREEN.3` stays `undecided` (no T1 screening procedure; one T3 paper and one T3 preprint are facts); the repository-provenance rule (C51) is decided on `INSTALL.5`; the philosophy node `THREATS.2` gained the 61 percent figure as a fact.
- `csurf` (C62) and the folklore beliefs C02, C12, C17, C62, C65 are rejected rows; clickjacking and `SameSite` rows tagged for web_architecture stay as code-level rules, with planned boundary links for the header deployment, the cookie attributes and token revocation.
- Merges (all claim ids kept): C81 into the philosophy row on `DEFENSE.INJECTION.4` (same ASVS 5.3.2 requirement as RUNSEC-C28); C77 and C79 into the rejected belief row on `INJECTION.4.1` (same Node pages as RUNSEC-C27).

### G6. Tooling touched (not graph content)

- `build/assemble/build_batches.py`, `build/assemble/apply_flags.py`, `build/distill/check_ledger.py`: the claim id pattern accepted letters only before `-C`, so `SECGAP2-C01` was invisible to them; it now accepts digits (`[A-Z]+\\d*-C\\d+`). `build_batches.py` also reads slot 14's claim table directly for the pointer path, because `claims_index.md` (frozen, 608 claims) has no slot 14 rows. `claims_index.py`, `routing.md` and the branch folders are history and were not touched.

### G7. Open after this slot

- Node XML parser defaults (C22), typosquatting screening procedure (C54), URL parser differential examples (C75), Node containment recipe (C82), whether `v8.deserialize` is safe (C85), SSTI rules for other engines (C39), a JavaScript upload signature check (C48). Late candidates LC-01 to LC-03 are in the slot's result file, not register sources.
"""


def die(msg):
    sys.exit("ERROR " + msg)


# ================================================================================================ apply
def main():
    ledger = LEDGER.read_text().split("\n")
    if any(l.startswith("| DEFENSE-185 |") for l in ledger):
        die("already applied (DEFENSE-185 exists)")

    # ---- ledger: rewrite existing rows
    for rid, ch in REWRITE.items():
        idx = [i for i, l in enumerate(ledger) if l.startswith(f"| {rid} |")]
        assert len(idx) == 1, rid
        cells = [x.strip() for x in ledger[idx[0]].strip().strip("|").split("|")]
        assert len(cells) == 7, (rid, len(cells))
        for k, v in ch.items():
            cells[["row", "claim_ids", "node", "graph", "statement", "agreement", "role"].index(k)] = v
        ledger[idx[0]] = "| " + " | ".join(cells) + " |"
    # ---- ledger: new rows after the last row of each prefix
    for prefix in ("DEFENSE", "DEPENDENCIES"):
        last = max(i for i, l in enumerate(ledger) if re.match(rf"\| {prefix}-\d+ \|", l))
        block = [f"| {r} | {ids} | {n} | {g} | {s} | {a} | {ro} |" for (r, ids, n, g, s, a, ro) in NEW if r.startswith(prefix)]
        ledger[last + 1:last + 1] = block
    text = "\n".join(ledger)
    rows = [l for l in text.split("\n") if re.match(r"\| [A-Z]+-\d+ \|", l)]
    withc = [l for l in rows if re.findall(r"[A-Z]+\d*-C\d+", l.split("|")[2])]
    nclaims = sum(len(re.findall(r"[A-Z]+\d*-C\d+", l.split("|")[2])) for l in rows)
    text = re.sub(r"Rows: \d+ \(\d+ carry \d+ claim ids, \d+ are claim-less: folklore rows and rows added at stage 7\)",
                  f"Rows: {len(rows)} ({len(withc)} carry {nclaims} claim ids, {len(rows) - len(withc)} are claim-less: folklore rows and rows added at stage 7 and in the slot 14 patch)", text)
    assert f"Rows: {len(rows)}" in text
    LEDGER.write_text(text)
    ledger_rows = rows

    # ---- skeleton
    sk = SKEL.read_text().split("\n")

    def node_idx(uid):
        pat = re.compile(r"\| " + re.escape(uid) + r" \| ")
        hit = [i for i, l in enumerate(sk) if pat.match(l)]
        assert len(hit) == 1, (uid, hit)
        return hit[0]

    def cells_of(i):
        l = sk[i]
        return [x.strip() for x in re.split(r"(?<!\\)\|", l.strip()[1:-1])]

    for uid, ch in EDIT.items():
        i = node_idx(uid)
        cl = cells_of(i)
        if "name" in ch:
            cl[1] = ch["name"]
        if "intent" in ch:
            cl[2] = ch["intent"]
        if "intent_append" in ch:
            cl[2] = cl[2] + ch["intent_append"]
        if "epistemic" in ch:
            cl[3] = ch["epistemic"]
        sk[i] = "| " + " | ".join(cl) + " |"
    for uid, (name, intent, epi) in NODES.items():
        assert not any(re.match(r"\| " + re.escape(uid) + r" \| ", l) for l in sk), uid
        i = node_idx(AFTER[uid])
        sk.insert(i + 1, f"| {uid} | {name} | {intent} | {epi} | - |")

    # ledger rows column, regenerated for every node from the ledger order
    by_node = {}
    for l in ledger_rows:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        by_node.setdefault(c[2], []).append(c[0])
    end_nodes = next(i for i, l in enumerate(sk) if l.startswith("## Planned boundary links"))
    changed = []
    for i, l in enumerate(sk[:end_nodes]):
        m = re.match(r"\| ((?:PIG-JS\.)?[A-Z][A-Z0-9_.]*) \| ", l)
        if not m or m.group(1) == "uid":
            continue
        cl = cells_of(i)
        if len(cl) != 5:
            continue
        want = ", ".join(by_node.get(m.group(1), [])) or "-"
        if cl[4] != want:
            changed.append((m.group(1), cl[4], want))
            cl[4] = want
            sk[i] = "| " + " | ".join(cl) + " |"
    print("ledger-rows column changed for", len(changed), "nodes:")
    for u, o, n in changed:
        print("  ", u, "|", o, "->", n[:60])

    def append_rows(heading, rows_):
        h = next(i for i, l in enumerate(sk) if l == heading)
        j = h + 1
        while not sk[j].startswith("| "):
            j += 1
        while j < len(sk) and sk[j].startswith("|"):
            j += 1
        n = int(re.match(r"\| (\d+) \|", sk[j - 1]).group(1))
        new = [f"| {n + k + 1} | {a} | {b} | {t} | {s} |" for k, (a, b, t, s) in enumerate(rows_)]
        sk[j:j] = new

    append_rows("### Intentlinks inside pig-js-defaults: within branches", WITHIN)
    append_rows("### Intentlinks inside pig-js-defaults: across branches (resolved from proposals)", ACROSS)
    append_rows("### Inter links from pig-js-defaults to js-philosophy",
                [(a, f"js-philosophy:{b}", "refines", INTER_SENT) for a, b in INTER])
    # planned boundary links
    h = next(i for i, l in enumerate(sk) if l.startswith("## Planned boundary links"))
    j = next(i for i in range(h, len(sk)) if sk[i].startswith("| 10 |"))
    sk[j + 1:j + 1] = [f"| {11 + k} | {a} | {g} | {t} |" for k, (a, g, t) in enumerate(PLANNED)]
    # conventions line
    k = next(i for i, l in enumerate(sk) if l.startswith("- Nodes relabelled `risky`"))
    sk.insert(k + 1, "- Slot 14_secgap2 (second security gap round) was folded by patch (`build/patch/14_secgap2/`): 17 defaults nodes added, "
                     "`DOM.2.3`, `INJECTION.5.3` and `INJECTION.6.4` decided from `undecided`, `INJECTION.4.4` kept undecided; decisions in `decisions_for_review.md` section `Slot 14_secgap2`.")
    # judge records: DEFENSE before the integration note, DEPENDENCIES before ### VERIFICATION of the judge part
    jr = next(i for i, l in enumerate(sk) if l == "## Judge records")
    note = next(i for i in range(jr, len(sk)) if sk[i].startswith("Integration note (DEFENSE)"))
    # extend the 4.1 record in place instead of repeating the node: it is the last block of the DEFENSE additions text
    sk[note:note] = JUDGE_DEFENSE.strip("\n").split("\n") + [""]
    ver = next(i for i in range(note, len(sk)) if sk[i] == "### VERIFICATION")
    sk[ver:ver] = JUDGE_DEPENDENCIES.strip("\n").split("\n") + [""]
    SKEL.write_text("\n".join(sk))

    # ---- decisions
    d = DEC.read_text()
    marker = "## Decisions by branch"
    assert d.count(marker) == 1
    d = d.replace(marker, DECISIONS + "\n" + marker)
    # undecided list: the three resolved nodes leave the tables, 4.4 is revised, SCREEN.3 joins
    d = re.sub(r"\| `PIG-JS\.DEFENSE\.DOM\.2\.3` \|[^\n]*\n", "", d)
    d = re.sub(r"\| `PIG-JS\.DEFENSE\.INJECTION\.5\.3` \|[^\n]*\n", "", d)
    d = re.sub(r"\| `PIG-JS\.DEFENSE\.INJECTION\.6\.4` \|[^\n]*\n", "", d)
    d = re.sub(r"\| `PIG-JS\.DEFENSE\.INJECTION\.4\.4` \|[^\n]*\n",
               "| `PIG-JS.DEFENSE.INJECTION.4.4` | What is the Node recipe for path containment (SRVSEC-C55, RUNSEC-C29, SECGAP2-C82)? The grounded pieces moved to `INJECTION.4.1` in the slot 14 patch; missing: the symlink-resolving Node call and the separator-aware test | A readable Node `fs.realpath` entry and a source stating the comparison, for example the hapi fix commit (late candidate LC-01) |\n", d)
    d = d.replace("`PIG-JS.DEPENDENCIES.PUBLISH.4`, ", "`PIG-JS.DEPENDENCIES.PUBLISH.4`, `PIG-JS.DEPENDENCIES.SCREEN.3`, ", 1)
    d = d.replace("`PIG-JS.DEFENSE.DOM.2.3`, ", "").replace("`PIG-JS.DEFENSE.INJECTION.5.3`, `PIG-JS.DEFENSE.INJECTION.6.4`, ", "")
    d = d.replace("##### DEPENDENCIES: PIG-JS.DEPENDENCIES.UPDATE.1.1: cooldown length beyond the tool defaults",
                  "##### DEPENDENCIES: PIG-JS.DEPENDENCIES.SCREEN.3: typosquatting screening procedure\n- State: undecided | missing: no admitted T1 source states a screening procedure for adding a dependency (SECGAP2-C54); one T3 paper (C52) and one T3 preprint (C53) describe name-similarity methods.\n- Settled by: a T1 statement of a screening procedure (npm, OpenSSF or a registry operator), or a measurement of such a method's precision at T2.\n\n##### DEPENDENCIES: PIG-JS.DEPENDENCIES.UPDATE.1.1: cooldown length beyond the tool defaults", 1)
    DEC.write_text(d)
    print("applied; new ledger rows:", len(NEW), "; ledger total rows:", len(rows))


if __name__ == "__main__":
    main()

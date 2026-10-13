# Discovery result: slot 05 DOMSEC (browser code security)

All fetches made 2026-10-12. Certainty marks: grounded = fetched and checked; inferred = follows from fetched material; open = not established.

## L1 headline

Authoritative sources cover every sub-topic of DOMSEC well, with a T1 for each (grounded, 35 candidates read or checked); the weak spots are three T1-level gaps in detail (no normative `javascript:` URL text, no primary Google evidence for Trusted Types production results, Sanitizer API text now living inside the WHATWG HTML spec and not yet located) and a few dated currency questions.

Pinned:
- Candidates by proposed tier: T1 23, T2 10, T3 2 (35 total).
- Sub-topics with no T1 candidate: none. (Thin T1 coverage, not absent: `javascript:` URL scheme handling; see gaps.)
- Failed fetches on a T1 candidate: none. (Failed on non-T1: the mXSS paper K34, both the Ruhr-University page and the ACM page, so K34 is listed from search results and the venue record only; the IEEE page for K31, covered by the CISPA record instead.)

## L2 claims

Sub-topics (each line: best candidates, T1 present?)

- DOM XSS sinks and sources: K01, K02, K23 (T1), K24 (T3), K28 (T2, measurement: 9.6% of Alexa top 5000 sites carried a DOM XSS). T1 yes. Grounded.
- Trusted Types: K03 (spec, W3C WD), K04 (MDN, Baseline 2026), K05 (T2, spec editor), K32 (T2, usability study), K35 (T2, Mozilla position). T1 yes. Grounded.
- Sanitization: K02, K01, K11, K25 (T1), K13 (T3 maintainer doc), K14 (T1 advisory facts, bypass history), K12 (T2 draft, merged into WHATWG HTML), K34 (T2, mXSS, fetch failed). T1 yes. Grounded, except K34 and the WHATWG HTML sanitizer section, which are open.
- DOM clobbering (part of sinks/sources class): K15 (T1), K18 (T1), K31 (T2). T1 yes. Grounded.
- URL handling: K17 (T1, parsing and origin semantics), K01 and K02 (T1, URL attribute encoding), K18 (T1, allowlisted redirects), K26 (T1, link types). T1 yes, but no normative `javascript:` text found. Grounded for what is covered; the `javascript:` scheme point is open.
- `postMessage`: K06 (T1 spec), K07 (T1 MDN), K08 (T1 OWASP), K18 (T1), K29 (T2, 84 vulnerable popular sites). T1 yes. Grounded.
- Storage of sensitive data (code-level only): K08, K22, K21 (T1; K21 is `boundary: web-architecture`), K18 (T1, cookie and token rules; boundary for the architecture part). T1 yes. Grounded.
- Third-party scripts: K16 (T1), K09 and K10 (SRI), K27 (iframe sandbox), K30 (T2, 88.45% of sites include remote scripts). T1 yes. Grounded.
- SRI: K09 (spec, W3C WD), K10 (MDN), K18 (T1). T1 yes. Grounded.
- Boundary items, tagged `boundary: web-architecture`, listed for what they say about code: K19 (CSP3), K20 (OWASP CSP), K21 (OWASP Session Management), K33 (T2, CSP bypass study). Grounded.

Disagreements and tensions between candidates

- Sanitizer placement: K01 and K02 push encoding plus a sanitizer library (DOMPurify); K11 and K25 push the browser-native `setHTML` as the drop-in for `innerHTML`. Complementary rather than opposed, but later stages need both positions. Grounded.
- K13 (library claims strong mXSS defense) against K14 (a stream of bypass advisories in 2026, one rated High): a sanitizer is not a one-time fix. Grounded.
- Currency conflict inside MDN: K11 says the Sanitizer API has limited availability, K25 says `setHTMLUnsafe` is Baseline 2025. Needs a reconcile at extraction. Grounded.
- K07 says never use `*` as `targetOrigin` except for `data:` URLs; the MDN iframe page K27 shows examples with `'*'`. Teaching examples against rule. Grounded.
- Trusted Types stance: K35 shows Mozilla opposed or held back until December 2023, now positive with open concerns about non-standard Chrome features. History of dissent, no live conflict. Grounded.
- K08 and K21 forbid tokens in Web Storage; K22 gives no stance (neutral API doc). No conflict. Grounded.

Gaps

- `javascript:` scheme handling has no normative T1 statement: K17 explicitly leaves it out (per the fetched summary; inferred, the full text was not read). Searched: URL Standard, OWASP DOM XSS and XSS cheat sheets. Open.
- Google production evidence for Trusted Types (zero DOM XSS across 130 services, VRP share of XSS falling): only press coverage found; the W3C FAQ cites Google data with no primary link. Press is T4 and is not listed. Open: look for the Google Security Blog or a paper in the extraction stage.
- Sanitizer API normative text: K12 says content moved into WHATWG HTML; the exact section was not located or fetched. Open.
- OWASP cheat sheets show no authors or dates in fetched text (G1 and G2 depend on the audit accepting the OWASP body as authority and git history as date). Inferred.

## L3 full

### Candidate table

Gates line format: G1 authority, G2 currency, G3 grounds, G4 primary, G5 conflict, G6 consistency with T1. "ok" means self-checked from the fetched page; named gates are the unsure ones.

| id | title | author or body | standing | url | fetched | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOMSEC-K01 | DOM based XSS Prevention Cheat Sheet | OWASP Cheat Sheet Series | OWASP project; contributors include Mike Samuel (Google, sanitization work) | https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G1 ok (body); G2 unsure (no date shown); G3 ok; G4 ok; G5 ok; G6 ok | sinks and sources, safe DOM methods, URL encoding, eval avoidance | none |
| DOMSEC-K02 | Cross Site Scripting Prevention Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (no date); others ok | encoding contexts, sanitization, Trusted Types mention, safe sinks | none |
| DOMSEC-K03 | Trusted Types | W3C Web Application Security WG; editor Krzysztof Kotowicz (Google), former editor Mike West | spec editors, co-designers of the mechanism | https://www.w3.org/TR/trusted-types/ | yes | W3C Working Draft, 2026-10-07 | spec | T1 | G2 ok; G3 ok; G4 origin; G5 ok (editors at Google, spec is vendor-neutral); G6 ok | Trusted Types, sinks, policies, default policy | boundary: web-architecture for the CSP directives as deployment policy (once) |
| DOMSEC-K04 | Trusted Types API | MDN contributors | MDN reference page | https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API | yes | last modified 2026-05-14, Baseline 2026 | official-doc | T1 | all ok; G4 is derivative of K03 but reference-grade | Trusted Types, default policy, sinks | none |
| DOMSEC-K05 | Trusted Types for DOM XSS Prevention (web.dev) | Krzysztof Kotowicz | spec editor of K03 | https://web.dev/articles/trusted-types | yes | 2020-03-25 | maintainer-writing | T2 | G2 unsure (2020; support list is current but text dated); G4 derivative of K03 | Trusted Types rollout (report-only, fix, enforce) | none |
| DOMSEC-K06 | HTML Standard, Web messaging | WHATWG | normative standard | https://html.spec.whatwg.org/multipage/web-messaging.html | yes | living standard, 2026-10-12 | spec | T1 | all ok | `postMessage`, origin check, targetOrigin, channels | none |
| DOMSEC-K07 | Window: postMessage() | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage | yes | widely available since 2015; page date not shown | official-doc | T1 | G2 unsure (page date not shown) | `postMessage` sender and receiver checks | none |
| DOMSEC-K08 | HTML5 Security Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (it still names AppCache as deprecated, so it was updated; no date shown) | web messaging, storage, sandboxed frames, tabnabbing, service workers | none |
| DOMSEC-K09 | Subresource Integrity | W3C WebAppSec WG; editor Frederik Braun (Mozilla) | spec editor | https://www.w3.org/TR/SRI/ | yes | W3C Working Draft, 2026-03-20 | spec | T1 | all ok | SRI, integrity metadata, Integrity-Policy header | none |
| DOMSEC-K10 | Subresource Integrity (MDN) | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity | yes | page date not shown | official-doc | T1 | G2 unsure (date); G4 derivative of K09 | SRI usage, CORS requirement | none |
| DOMSEC-K11 | HTML Sanitizer API | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/API/HTML_Sanitizer_API | yes | page date not shown; availability "limited" | official-doc | T1 | G2 unsure (conflicts with K25 on availability) | `setHTML`, `Sanitizer`, safe versus unsafe methods | none |
| DOMSEC-K12 | HTML Sanitizer API (WICG draft) | WICG; editors Braun (Mozilla), Heiderich (Cure53), Vogelheim (Google), Schuster (Mozilla) | spec editors; Heiderich is DOMPurify author | https://wicg.github.io/sanitizer-api/ | yes | Draft CG Report, 2026-08-31; content merged into WHATWG HTML | spec | T2 | G2: page says it must no longer be consulted independently, so seek the WHATWG HTML section instead; G4 origin moved | sanitizer design | none |
| DOMSEC-K13 | DOMPurify README | cure53 (Mario Heiderich) | maintainer; co-author of the mXSS research; OpenSSF badge | https://github.com/cure53/DOMPurify | yes | release v3.4.16 | maintainer-writing | T3 | G5 ok (free library); G3 ok (documents attack classes) | sanitization, Trusted Types integration, "sanitize then modify voids it" | none |
| DOMSEC-K14 | DOMPurify security advisories | GitHub Security Advisories (cure53 repository) | advisory records | https://github.com/cure53/DOMPurify/security/advisories | yes | latest listed 2026-10-12 | advisory | T1 | facts only (G4 ok); use as facts, not advice | sanitizer bypass history (GHSA-cg2g-xh64-v4q7, High) | none |
| DOMSEC-K15 | DOM Clobbering Prevention Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (no date) | DOM clobbering, defensive coding, freeze, sanitizer options | none |
| DOMSEC-K16 | Third Party JavaScript Management Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (no date) | third-party risk, SRI, iframe sandbox, data layer | none |
| DOMSEC-K17 | URL Standard | WHATWG | normative standard | https://url.spec.whatwg.org/ | yes | living standard, 2026-10-07 | spec | T1 | all ok | URL parsing, origin, URL API | none |
| DOMSEC-K18 | OWASP ASVS 5.0, V3 Web Frontend Security | OWASP; leaders Daniel Cuthbert, Elar Lang, Josh Grossman | verification standard | https://github.com/OWASP/ASVS/blob/master/5.0/en/0x12-V3-Web-Frontend-Security.md | yes | version 5.0 (master) | official-doc | T1 | G3 ok (requirements without long rationale; unsure); G2 ok | DOM clobbering, `textContent`, `postMessage` origin, SRI, redirects, cookies | boundary: web-architecture for headers and cookies (once) |
| DOMSEC-K19 | Content Security Policy Level 3 | W3C WebAppSec WG; editors Mike West, Antonio Sartori (Google) | spec editors | https://www.w3.org/TR/CSP3/ | yes | W3C Working Draft, 2026-09-16 | spec | T1 | all ok | what CSP says about script execution and defense in depth | boundary: web-architecture |
| DOMSEC-K20 | Content Security Policy Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (no date) | CSP as second layer behind secure coding | boundary: web-architecture |
| DOMSEC-K21 | Session Management Cheat Sheet | OWASP Cheat Sheet Series | as K01 | https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html | yes | undated in page | official-doc | T1 | G2 unsure (no date) | no tokens in `localStorage` or `sessionStorage`: any script in the origin can read them | boundary: web-architecture |
| DOMSEC-K22 | Web Storage API | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API | yes | widely available since 2015 | official-doc | T1 | all ok | storage scoping, third-party script access to storage | none |
| DOMSEC-K23 | Cross-site scripting (XSS) | MDN contributors | MDN security guide | https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS | yes | page date not shown | official-doc | T1 | G4 derivative synthesis, acceptable as MDN reference | browser-side XSS, encoding, sanitizer, Trusted Types, CSP | none |
| DOMSEC-K24 | DOM-based vulnerabilities (Web Security Academy) | PortSwigger | established security firm, author of the Burp suite | https://portswigger.net/web-security/dom-based | yes | undated | research-blog | T3 | G5 unsure (vendor); G3 ok | source and sink catalogue, 16 vulnerability classes | none |
| DOMSEC-K25 | Element: setHTMLUnsafe() | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTMLUnsafe | yes | Baseline 2025 | official-doc | T1 | G2 ok | injection sink status, `TrustedHTML`, safe alternative | none |
| DOMSEC-K26 | HTML Standard, link types noopener and noreferrer | WHATWG | normative standard | https://html.spec.whatwg.org/multipage/links.html#link-type-noopener | yes | living standard, 2026-10-12 | spec | T1 | all ok | `target=_blank` defaults, window.opener, tabnabbing | none |
| DOMSEC-K27 | iframe element (MDN) | MDN contributors | MDN reference | https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe | yes | widely available since 2015 | official-doc | T1 | G2 ok | sandbox attribute, `allow-scripts` plus `allow-same-origin` warning | none |
| DOMSEC-K28 | 25 Million Flows Later: Large-scale Detection of DOM-based XSS | Lekies, Stock, Johns | ACM CCS 2013 paper | https://notify.cispa.uni-saarland.de/papers/lekies2013flows.pdf | yes (PDF text via local extraction) | 2013 | paper | T2 | G2 unsure (2013 measurement; sink and source classes still current, rates may not be) | DOM XSS prevalence, taint flows | none |
| DOMSEC-K29 | The Postman Always Rings Twice: Attacking and Defending postMessage in HTML5 Websites | Sooel Son, Vitaly Shmatikov | NDSS 2013 paper | https://www.ndss-symposium.org/ndss2013/postman-always-rings-twice-attacking-and-defending-postmessage-html5-websites | yes | 2013-04-23 | paper | T2 | G2 unsure (2013) | origin check errors, safe patterns | none |
| DOMSEC-K30 | You Are What You Include: Large-scale Evaluation of Remote JavaScript Inclusions | Nikiforakis et al. (Kruegel, Vigna, Piessens, Joosen) | ACM CCS 2012 paper | https://iseclab.org/publications/nikiforakis2012you_are/ | yes (record page; figures from search result, not from the paper text) | 2012 | paper | T2 | G2 unsure (2012) | remote script trust | none |
| DOMSEC-K31 | It's (DOM) Clobbering Time: Attack Techniques, Prevalence, and Defenses | Soheil Khodayari, Giancarlo Pellegrino | IEEE S&P 2023 paper | https://cispa.de/en/research/publications/71734-it-s-dom-clobbering-time-attack-techniques-prevalence-and-defenses | yes (CISPA record; IEEE page failed) | 2023 | paper | T2 | all ok | DOM clobbering, sanitizer and CSP evaluation | none |
| DOMSEC-K32 | Trust Me If You Can: How Usable Is Trusted Types In Practice? | Roth, Gröber, Baus, Krombholz, Stock | USENIX Security 2024 paper | https://www.usenix.org/conference/usenixsecurity24/presentation/roth | yes | 2024-08 | paper | T2 | all ok | Trusted Types adoption obstacles | none |
| DOMSEC-K33 | CSP Is Dead, Long Live CSP! | Weichselbaum, Spagnuolo, Lekies, Janc | ACM CCS 2016 paper | https://research.google/pubs/pub45542/ | yes | 2016 | paper | T2 | G5 unsure (authors at Google, evidence is measurement); G2 unsure (2016) | CSP allowlist bypasses, strict-dynamic | boundary: web-architecture |
| DOMSEC-K34 | mXSS Attacks: Attacking well-secured Web-Applications by using innerHTML Mutations | Heiderich et al. | ACM CCS 2013 paper | https://www.nds.ruhr-uni-bochum.de/research/publications/mXSS-Attacks/ | failed: connection refused on the Ruhr-University page (two host variants); ACM page returned 403; venue and authorship seen only in a search result | 2013 | paper | T2 | not checked beyond record; fetch the PDF before extraction | mutation XSS, `innerHTML` | none |
| DOMSEC-K35 | Mozilla standards position: Trusted Types | Mozilla (Freddy Bräuning, Martin Thomson) | browser vendor security team | https://github.com/mozilla/standards-positions/issues/20 | yes | position positive since 2023-12-13 | maintainer-writing | T2 | G5 unsure (browser vendor statement, treat as position); G3 ok | Trusted Types, standards stance | none |

Counts by tier: T1 23, T2 10 (K05, K12, K28 to K35), T3 2 (K13, K24). Total 35. Recount for audit: T1 ids are K01, K02, K03, K04, K06, K07, K08, K09, K10, K11, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K25, K26, K27 = 23.

`expect-restricted`: none proposed as a style guide. K24 (vendor) and K13 (maintainer, own tool) should be admitted for facts and mechanism, never for tool recommendation.

### Dismissed on sight (tally of what search results showed)

- News and press coverage of Trusted Types (Security Boulevard, Daily Swig, The Register, InfoQ, Cyware, SecurityLab, CISO2CISO): 7
- Bug-bounty and offensive-guide blogs or note repositories (Intigriti blog, HackTricks mirror): 2
- Vendor or unattributed blog posts (Unveil, BrowserStack, Report URI research page): 3
- Slide decks and talk copies of papers (derivative of K28, K29, K30, K34): 8
- Paper mirrors on academia.edu: 2
- Wikipedia: 1
- Patent document: 1
- Not covered by this tally: no search of the SEO tutorial or listicle class was run, since no query returned them.

### Searches run

- Trusted Types paper Google DOM XSS large-scale evaluation USENIX CCS NDSS
- 25 Million Flows Later large-scale detection of DOM-based XSS CCS 2013
- The Postman Always Rings Twice postMessage origin check NDSS 2013
- You Are What You Include remote JavaScript inclusions CCS 2012
- mutation XSS DOMPurify paper Heiderich mXSS; DOM clobbering USENIX/IEEE paper
- CSP Is Dead, Long Live CSP CCS 2016
- Google Security Blog Trusted Types DOM XSS zero incidence evidence (twice, no primary found)

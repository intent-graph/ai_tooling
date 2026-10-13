# Discovery result: slot 10_frameworks (area code FW)

Fetch date for every row: 2026-10-12. Every fetch went through a summarizing fetch tool (a small model answers a prompt against the page), not a raw download. "Fetched: yes" therefore means the page exists and the summary confirmed author, date and coverage; it does not mean the full text was read. Extraction stage must re-read in full.

## L1 headline

Sources for area 10 are plentiful but almost all vendor-authored: authoritative T1 sources cover only the cross-framework and no-framework ground (WHATWG, MDN, OWASP, GitHub advisory records), while every per-framework criterion (security docs, governance, support policy, TypeScript) rests on the framework's own documentation, proposed T3 with a G5 restriction; measured usage is thin (HTTP Archive Web Almanac has no JavaScript or frameworks chapter in 2025). Certainty: grounded on existence, authorship and coverage of each fetched page; inferred on tier proposals; open on usage for every framework except React, jQuery and custom elements.

Pinned:
- Number of candidates by proposed tier: T1 5, T2 5, T3 30 (total 40; T4 listed 0).
- Sub-topics or candidate frameworks with no T1 source: official security documentation has no T1 for React, Angular, Vue, Svelte, Solid, Lit, htmx (best proposed tier T3; T1 K04 only names React, Angular and Lit escape hatches, K03 and K01 and K02 cover the no-framework option); governance and maintainer body has no T1 for any candidate (T2 only for Lit, K35; no source found for Angular formal governance, Svelte current governance, Solid formal governance beyond a contributing file, htmx); release and support (LTS) policy has no T1 for any candidate and no published policy found for Svelte, Solid, Lit (security-supported versions only) and htmx (stability essay only); TypeScript support has no T1 for any candidate (TypeScript handbook not searched; open); measured usage has no T1 and no measured source at all for Angular, Vue, Svelte, Solid, Lit, htmx individually.
- Failed fetches on a T1 candidate: none. Failed fetches elsewhere: 8 (see L3), none on a proposed T1 or T2 row.

## L2 claims

Pinned:
- Number of candidates by proposed tier: T1 5, T2 5, T3 30 (total 40; T4 listed 0).
- Sub-topics or candidate frameworks with no T1 source: official security documentation has no T1 for React, Angular, Vue, Svelte, Solid, Lit, htmx (best proposed tier T3; T1 K04 only names React, Angular and Lit escape hatches, K03 and K01 and K02 cover the no-framework option); governance and maintainer body has no T1 for any candidate (T2 only for Lit, K35; no source found for Angular formal governance, Svelte current governance, Solid formal governance beyond a contributing file, htmx); release and support (LTS) policy has no T1 for any candidate and no published policy found for Svelte, Solid, Lit (security-supported versions only) and htmx (stability essay only); TypeScript support has no T1 for any candidate (TypeScript handbook not searched; open); measured usage has no T1 and no measured source at all for Angular, Vue, Svelte, Solid, Lit, htmx individually.
- Failed fetches on a T1 candidate: none. Failed fetches elsewhere: 8 (see L3), none on a proposed T1 or T2 row.

Open policy question for the auditor (affects the tier counts): the plan's T1 list does not name framework documentation; "maintainers' documentation of tools concerned" is T3, and G5 admits vendor content for facts only. I proposed T3 with `expect-restricted: facts about own product, no normative preference for it`. If the auditor treats official framework docs as T1 official-doc, the counts become T1 about 32, T3 about 3.

Per sub-topic, best candidates (certainty in brackets):

- Official security documentation
  - Angular: K10 (T3, full XSS, sanitizer, CSP, Trusted Types, CSRF, SSRF guide), K13 policy. No T1. [grounded]
  - React: K14 (innerHTML warning), K19 (Trusted Types passthrough, 19.3), K17 (advisory). No dedicated React security guide found. No T1. [grounded]
  - Vue: K20 (T3; states what Vue does not treat as vulnerabilities). No T1. [grounded]
  - Svelte: K24, K25 (CSP and CSRF config), K27 (policy, 10 moderate advisories, mostly SSR XSS). No T1. [grounded]
  - Solid: K30 (reporting policy and one high XSS advisory, 2025). No security guide found. No T1. [grounded]
  - Lit: K33 (policy only). No Lit security page fetchable; a Trusted Types page at lit.dev returned 404, so claims about Lit's template safety rest on search snippets only. No T1. [grounded on policy; open on guide]
  - htmx: K36, K37 (T3; four rules; config options selfRequestsOnly, allowEval, hx-disable), K39. No T1. [grounded]
  - No framework: K01, K02, K03 (T1), K04 (T1, cross-framework). T1 exists. [grounded]
- Governance and maintainer body
  - React: K18, React Foundation under the Linux Foundation, announced 2025-10, launched 2026-02-24, technical governance stated independent of board and still provisional. No T1. [grounded]
  - Vue: K23 (team page and Team Charter, project lead approves core members). No T1. [grounded]
  - Lit: K35 (OpenJS Foundation, incubation stage; T2). K32 says Google maintainers. [grounded]
  - Angular: only "Super-powered by Google" and a Google bug bounty (K13); no formal governance document found. [grounded as gap]
  - Svelte: K28 (2022 blog, 13 maintainers, creator employed by Vercel, OpenCollective); stale and no governance file (two GitHub paths 404). [grounded; currency weak]
  - Solid: K31 (core team selected by core members only). [grounded]
  - htmx: none found beyond K38 authors. [open]
- Release and support (LTS) policy
  - Angular: K11, strongest in the set: 24 months, 12 active plus 12 LTS, major every 12 months from v22, v22 Active, v21 and v20 LTS. K12: TypeScript range per version. [grounded]
  - React: K15, semver, security backports to all affected majors, explicitly no formal LTS. [grounded]
  - Vue: K21, no fixed schedule, minors every 3 to 6 months, TypeScript typings may break in minors; Vue 2 end of life (stated on v2 site, not a candidate row). [grounded]
  - Lit: K33 supports latest two majors, K38 2.x and 3.x interoperable. [grounded]
  - htmx: K39 supports 4.x, 2.x, 1.9.x; K38 stability commitment, quarterly releases. K44 conflicts with K37 on whether 4.x is stable (below). [grounded on policy; open on 4.x status]
  - Svelte, Solid: no policy found; K27 for Svelte lists nothing on supported versions. [open]
- TypeScript support
  - Vue K22 (written in TypeScript, bundled types, vue-tsc), Angular K12 (TypeScript is the language; range >=6.0 <6.1 for v22), React K16 (needs @types/react), Svelte K26 (type-only syntax by default, enums need preprocessor), Solid K29, Lit K34 (decorator caveats; TS 5.2+ per K38). htmx K37: no TypeScript mentioned. [grounded]. No T1. TypeScript handbook JSX or framework pages not searched. [open]
- Measured usage
  - K06 (T2): jQuery 74% of mobile pages, React 10% (8% in prior edition), custom elements 7.8% (2% in 2022), shadow DOM 2.51%. Vue, Angular, Svelte, Solid, htmx, Lit not reported in the summary I got. [grounded for those numbers; inferred that others are absent]
  - K07 (T2, boundary: web-architecture): meta-framework shares (Next.js, Nuxt, Astro, Hugo) among prerendered and hybrid sites only (0.5% and 5% of web). [grounded]
  - K08 (T2): CSP 21.9%, SRI 23.6% mobile; not framework-segmented. [grounded]
  - K09 (T2): dataset joining CrUX and detected technologies; summary named only WordPress, Drupal, Magento lenses, so framework coverage is unconfirmed. [open]
  - Web Almanac 2025 has no JavaScript, Jamstack, frameworks or web components chapter (table of contents fetched; /en/2025/javascript is 404). Newest JavaScript chapter is 2024. [grounded]
  - No popularity survey admitted.

Disagreements between candidates:
- K37 (htmx.org docs: 2.x current, 1.x supported) versus K39 (security policy: 4.x, 2.x, 1.9.x supported) and K44 (releases page: v4.0.0 stable). The fetched release dates show 2024 years that cannot be right for today (2026-10-12), so K44 is unreliable as summarized. [grounded that they differ; open which is right]
- K36 and K02/K03 versus frameworks on safety posture: htmx essay states template-based apps are "no harder" to secure than JSX apps; K20, K10, K14 place the risk in escape hatches. Not opposite claims, but positions from interested parties (G5). [inferred]
- K15 (React: no LTS, backports to all affected majors) versus K11 (Angular: formal 24-month LTS): different support models, not a contradiction; later stages need both.
- K40 (htmx hypermedia essay) asserts HDA is superior to SPA and MPA with no measurement; position only, `boundary: web-architecture`.

Gaps:
- No T1 per-framework anywhere (pinned above). Framework-specific CVE records (K05) are the only T1 per-framework facts, and only security incidents, not policy.
- Solid and Svelte release policy; Angular, htmx governance; Lit security guide; htmx usage; Vue and Angular measured usage.
- Not searched: TypeScript handbook, Preact, Alpine, Astro, Next.js, Nuxt, SvelteKit docs beyond one page, Baseline "widely available" pages, Stack-level surveys (deliberately excluded).
- Fetch-tool year anomalies on GitHub release pages (Solid, Svelte, htmx): treat any date from K44, and the release dates of Svelte and Solid, as open.

## L3 full

Pinned:
- Number of candidates by proposed tier: T1 5, T2 5, T3 30 (total 40; T4 listed 0).
- Sub-topics or candidate frameworks with no T1 source: official security documentation has no T1 for React, Angular, Vue, Svelte, Solid, Lit, htmx (best proposed tier T3; T1 K04 only names React, Angular and Lit escape hatches, K03 and K01 and K02 cover the no-framework option); governance and maintainer body has no T1 for any candidate (T2 only for Lit, K35; no source found for Angular formal governance, Svelte current governance, Solid formal governance beyond a contributing file, htmx); release and support (LTS) policy has no T1 for any candidate and no published policy found for Svelte, Solid, Lit (security-supported versions only) and htmx (stability essay only); TypeScript support has no T1 for any candidate (TypeScript handbook not searched; open); measured usage has no T1 and no measured source at all for Angular, Vue, Svelte, Solid, Lit, htmx individually.
- Failed fetches on a T1 candidate: none. Failed fetches elsewhere: 8 (see L3), none on a proposed T1 or T2 row.

Gate shorthand: G1 authority, G2 currency, G3 grounds, G4 primary, G5 conflict of interest, G6 consistency with T1. Every framework-doc row has G5 as the live gate (vendor describing own product): admitted for facts about the product, not for claims favouring it. All rows below fetched: yes unless stated. Topics: SEC security docs, GOV governance, REL release and support, TS TypeScript, USE usage, NOFW no-framework.

### Candidate table

| id | title | author or body | standing | url | date | kind | proposed tier | gates | covers | boundary |
|---|---|---|---|---|---|---|---|---|---|---|
| FW-K01 | HTML Living Standard, custom elements | WHATWG | normative spec body for HTML | https://html.spec.whatwg.org/multipage/custom-elements.html | page last updated 2026-10-12 | spec | T1 | all pass | NOFW, web components (Lit) | |
| FW-K02 | Web Components (MDN reference) | MDN contributors | MDN is T1 per plan | https://developer.mozilla.org/en-US/docs/Web/API/Web_components | modified 2026-09-01 | official-doc | T1 | all pass | NOFW, web components, Lit | |
| FW-K03 | Trusted Types API (MDN) | MDN contributors | MDN is T1 per plan | https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API | modified 2026-05-14; Baseline 2026 | official-doc | T1 | all pass | SEC for NOFW, and for React 19.3, Angular, Lit hooks | domsec (area 05) |
| FW-K04 | Cross Site Scripting Prevention Cheat Sheet, "Framework Security" part | OWASP | OWASP cheat sheets are T1 per plan | https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html | no date in summary | official-doc | T1 | pass; G2 date to confirm | SEC: names React dangerouslySetInnerHTML, Angular bypassSecurityTrust*, Lit unsafeHTML as escape hatches; not Vue, Svelte, Solid, htmx | domsec (area 05), primary home there |
| FW-K05 | GitHub Advisory Database (npm advisories, e.g. Svelte entries) and the CVE records cited by maintainers (CVE-2025-55182 and four others for React Server Components) | GitHub, CVE Program, package maintainers | T1 per plan, as facts only | https://github.com/advisories?query=ecosystem%3Anpm+type%3Areviewed+svelte | entries up to 2026-09-17 | advisory | T1 (facts, not advice) | pass; G3 per entry | SEC: per-framework incident history, usable as comparison criterion | supply (area 07) |
| FW-K06 | Web Almanac 2024, JavaScript chapter | HTTP Archive; authors Abdul Haddi Amjad, Nishu Goel | HTTP Archive Web Almanac, community-reviewed annual report from crawl data | https://almanac.httparchive.org/en/2024/javascript | published 2025-03-03, updated 2026-01-16 | dataset | T2 (not named in plan tiers; auditor to confirm) | G1 G3 pass; G2 one edition old | USE: jQuery 74%, React 10%, custom elements 7.8% | |
| FW-K07 | Web Almanac 2024, Jamstack chapter | HTTP Archive | as K06 | https://almanac.httparchive.org/en/2024/jamstack | edition 2024 (date not shown) | dataset | T2 | G3 pass; method is a scoring heuristic, state limits | USE of meta-frameworks (Next.js 23% of hybrid, Astro 3x growth) | boundary: web-architecture |
| FW-K08 | Web Almanac 2025, Security chapter | HTTP Archive; Vik Vanderlinden, Gertjan Franken | as K06 | https://almanac.httparchive.org/en/2025/security | 2026-01-15 | dataset | T2 | pass | USE of CSP 21.9%, SRI 23.6% mobile; not segmented by framework | domsec (area 05) |
| FW-K09 | Core Web Vitals Technology Report | HTTP Archive with Chrome UX Report | joint public datasets | https://httparchive.org/reports/cwv-tech | no date in summary | dataset | T2 | G3 pass; coverage of frameworks unconfirmed (summary named only WordPress, Drupal, Magento) | USE possible, per-technology | |
| FW-K10 | Angular Security Guide | Angular team (Google); doc build v22.2.2 | maintainers of the framework | https://angular.dev/best-practices/security | v22.2.2 | official-doc | T3, expect-restricted: facts about Angular | G5 live; others pass | SEC: sanitization contexts, bypassSecurityTrust, CSP nonces, Trusted Types, CSRF, SSRF | |
| FW-K11 | Angular versioning and release policy | Angular team (Google) | as above | https://angular.dev/reference/releases | v22 era (page current) | official-doc | T3, expect-restricted: facts about Angular | G5 live | REL: 24 months support, 12 active plus 12 LTS, yearly major from v22, deprecation at least one major | |
| FW-K12 | Angular version compatibility | Angular team (Google) | as above | https://angular.dev/reference/versions | v22.0.x row | official-doc | T3, expect-restricted | G5 live | TS: v22 requires TypeScript >=6.0 <6.1; Node ranges; browser baseline | |
| FW-K13 | Angular security policy (GitHub) | Angular team; Google OSS Vulnerability Reward Program | as above | https://github.com/angular/angular/security/policy | none shown | official-doc | T3, expect-restricted | G5 live | SEC reporting and bounty; GOV only that Google runs it | |
| FW-K14 | React DOM common components, dangerouslySetInnerHTML | React team (react.dev) | maintainers | https://react.dev/reference/react-dom/components/common | none shown | official-doc | T3, expect-restricted | G5 live | SEC: XSS warning, Trusted Types note | |
| FW-K15 | React versioning policy | React team | maintainers | https://react.dev/community/versioning-policy | none shown | official-doc | T3, expect-restricted | G5 live | REL: semver, backports to all affected majors, no formal LTS | |
| FW-K16 | React with TypeScript | React team | maintainers | https://react.dev/learn/typescript | none shown | official-doc | T3, expect-restricted | G5 live | TS: types via @types/react (separately maintained package) | |
| FW-K17 | Critical Security Vulnerability in React Server Components | The React Team | maintainers; advisory | https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components | 2025-12-03 (updated to include CVE-2026-23864, 2026-01-26) | advisory | T3, expect-restricted; the CVE records themselves are K05 | G5 live (vendor disclosure, facts with CVE ids) | SEC: RCE CVSS 10.0 in server functions deserialization, 19.0 to 19.2.0 affected; fixed 19.0.1, 19.1.2, 19.2.1 | web-architecture (server tier) for the RSC part |
| FW-K18 | The React Foundation: A New Home for React Hosted by the Linux Foundation | Matt Carroll (React team) | maintainers | https://react.dev/blog/2026/02/24/the-react-foundation | 2026-02-24 | maintainer-writing | T3, expect-restricted | G5 live; G2 pass; status provisional | GOV: board of platinum members, technical governance stated independent, provisional leadership council | |
| FW-K19 | React 19.3 release post, Trusted Types | The React Team | maintainers | https://react.dev/blog/2026/09/09/react-19-3 | 2026-09-09 | official-doc | T3, expect-restricted | G5 live; G6 consistent with K03 | SEC: values no longer coerced to strings, so Trusted Types policies work | |
| FW-K20 | Vue Security guide | Vue team | maintainers | https://vuejs.org/guide/best-practices/security | none shown | official-doc | T3, expect-restricted | G5 live | SEC: template injection, v-html, URL, style, what is not treated as a vulnerability | |
| FW-K21 | Vue release policy | Vue team | maintainers | https://vuejs.org/about/releases | none shown | official-doc | T3, expect-restricted | G5 live | REL: no fixed schedule, semver exceptions for typings | |
| FW-K22 | Vue TypeScript overview | Vue team | maintainers | https://vuejs.org/guide/typescript/overview | none shown | official-doc | T3, expect-restricted | G5 live | TS: bundled types, vue-tsc, strictness | |
| FW-K23 | Vue team page and Team Charter | Vue team; https://github.com/vuejs/governance/blob/master/Team-Charter.md fetched too | maintainers | https://vuejs.org/about/team | none shown | official-doc | T3, expect-restricted | G5 live | GOV: roles, nomination, project lead approves core members; no legal entity or funding stated | |
| FW-K24 | Svelte `{@html}` reference | Svelte team | maintainers | https://svelte.dev/docs/svelte/@html | none shown | official-doc | T3, expect-restricted | G5 live | SEC: raw HTML warning | |
| FW-K25 | SvelteKit configuration, csp and csrf | Svelte team | maintainers | https://svelte.dev/docs/kit/configuration | none shown | official-doc | T3, expect-restricted | G5 live | SEC: CSP hash and nonce modes, CSRF trustedOrigins | web-architecture (CSP as deployment) |
| FW-K26 | Svelte TypeScript | Svelte team | maintainers | https://svelte.dev/docs/svelte/typescript | none shown | official-doc | T3, expect-restricted | G5 live | TS: type-only support by default, preprocessor for enums | |
| FW-K27 | Svelte security policy and advisories | Svelte team (Vercel HackerOne bounty) | maintainers | https://github.com/sveltejs/svelte/security/policy ; https://github.com/sveltejs/svelte/security/advisories | advisories 2026-02 to 2026-05 | advisory | T3, expect-restricted; the records are also K05 | G5 live | SEC: reporting timelines (2 and 4 weeks), 10 moderate advisories, mostly SSR XSS | |
| FW-K28 | Accelerating Svelte's Development | Ben McCann (Svelte maintainer) | maintainer writing | https://svelte.dev/blog/accelerating-sveltes-development | 2022-01-13 | maintainer-writing | T3, expect-restricted; G2 weak (4 years old) | G2 doubtful; G5 live | GOV: maintainer list, independence from Vercel, OpenCollective | |
| FW-K29 | Solid TypeScript configuration | Solid team | maintainers | https://docs.solidjs.com/configuration/typescript | none shown | official-doc | T3, expect-restricted | G5 live | TS: jsx preserve plus jsxImportSource, typed signals | |
| FW-K30 | Solid security policy and advisory | Solid team | maintainers | https://github.com/solidjs/solid/security | advisory published 2025-02-21 | advisory | T3, expect-restricted; record also K05 | G5 live | SEC: security@ contact, embargo rules, one high XSS (GHSA-3qxh-p7jc-5xh6, JSX fragments) | |
| FW-K31 | Solid CONTRIBUTING | Solid team | maintainers | https://github.com/solidjs/solid/blob/main/CONTRIBUTING.md | none shown | official-doc | T3, expect-restricted | G5 live | GOV: core and ecosystem teams chosen by core members | |
| FW-K32 | Lit documentation overview | Lit team (Google); OpenJS footer | maintainers | https://lit.dev/docs/ | v3 | official-doc | T3, expect-restricted | G5 live | GOV: Google team, OpenJS Foundation; Lit components are standard web components | |
| FW-K33 | Lit security policy | Lit team | maintainers | https://github.com/lit/lit/security/policy | none shown | official-doc | T3, expect-restricted | G5 live | SEC and REL: latest two majors supported, 90-day disclosure | |
| FW-K34 | Lit TypeScript and development tools | Lit team | maintainers | https://lit.dev/docs/tools/development/ | v3 | official-doc | T3, expect-restricted | G5 live | TS: tsc, decorators caveats | |
| FW-K35 | OpenJS Foundation projects | OpenJS Foundation | foundation hosting the project | https://openjsf.org/projects | none shown | official-doc | T2 | G1 pass; G5 low | GOV: Lit at Incubation stage; other UI projects Marko, Dojo, jQuery | |
| FW-K36 | Web Security Basics (with htmx) | Alexander Petros (htmx maintainer) | maintainer writing | https://htmx.org/essays/web-security-basics-with-htmx/ | 2024-02-06 | maintainer-writing | T3, expect-restricted | G5 live; G2 predates htmx 2.0 and 4.x | SEC: four rules; compares with SPA security (a position) | web-architecture for the SPA comparison |
| FW-K37 | htmx documentation, security section | htmx team | maintainers | https://htmx.org/docs/#security | page documents 2.x | official-doc | T3, expect-restricted | G5 live | SEC: hx-disable, selfRequestsOnly, allowEval, nonces; REL: 2.x current, 1.x supported; TS: none mentioned | |
| FW-K38 | The Future of htmx | Carson Gross, Alex Petros | maintainers | https://htmx.org/essays/future/ | 2025-01-01 | maintainer-writing | T3, expect-restricted; G3 is intent, not mechanism | G5 live | REL and GOV: stability commitment, quarterly releases | |
| FW-K39 | htmx security policy | htmx team | maintainers | https://github.com/bigskysoftware/htmx/security/policy | none shown | official-doc | T3, expect-restricted | G5 live | REL and SEC: supports 4.x, 2.x, 1.9.x | |
| FW-K40 | Hypermedia-Driven Applications | Carson Gross (htmx creator) | maintainer writing, advocacy | https://htmx.org/essays/hypermedia-driven-applications/ | 2022-02-06 | maintainer-writing | T3, expect-restricted: position only, never evidence; no measurement | G3 weak, G5 live | defines the hypermedia option | boundary: web-architecture |

Count check: T1 = K01 to K05 (5); T2 = K06, K07, K08, K09, K35 (5); T3 = K10 to K34 (25) plus K36 to K40 (5) = 30. Total 40, above the aim of 35 because eight candidates by four criteria were demanded; the extra rows are one-per-criterion framework pages.

Note on K44 (not a candidate row): the GitHub releases pages of Svelte, Solid and htmx were fetched for version and cadence, but the fetch returned release dates in 2024 and an htmx 4.0.0 stable claim that conflict with the current date and with K37, so they are dismissed as unreliable summaries, not candidates. Re-read directly at extraction time (https://github.com/sveltejs/svelte/releases, https://github.com/solidjs/solid/releases, https://github.com/bigskysoftware/htmx/releases). As summarized: Svelte 5.57.x current major 5; Solid 2.0.0-rc.14 (release candidate, not stable); htmx 4.0.0 stable. All three: open.

### Failed fetches (8)

None on a T1 or T2 candidate.
- https://almanac.httparchive.org/en/2025/javascript: 404, the chapter does not exist; alternative: 2025 table of contents (fetched, no JavaScript chapter) and 2024 chapter (K06).
- https://lit.dev/docs/security/trusted-types/: 404; alternative: search snippets only (not admissible as a read); open for a Lit security guide.
- https://github.com/sveltejs/svelte/blob/main/SECURITY.md: 404; alternative: /security/policy (K27).
- https://github.com/sveltejs/svelte/blob/main/GOVERNANCE.md: 404; no alternative found.
- https://svelte.dev/docs/svelte/legacy-at-html: 404; alternative: /docs/svelte/@html (K24).
- https://four.htmx.org/docs/security: 404; alternative: htmx.org docs (K37). Note: search results point to a four.htmx.org site for htmx 4 docs, the essay page there was fetched and matches K36.
- https://github.com/solidjs/solid/blob/main/GOVERNANCE.md was not tried; https://github.com/solidjs/solid/security fetched. The eighth failure: https://svelte.dev/docs/svelte/overview gave no maintainer or version data (fetched, but answered "not found"; counted as a failed fetch for the question asked).

### Dismissed on sight (tally, T4 not listed)

Search-result pages: popularity or "best framework 2026" listicles about 12 results (not fetched); Jamstack marketing posts 5 (scrums.com, ikius, eternitech, gitnexa, dev.to); dev.to articles 2 (one on lit-html internals, one on Jamstack); Wikipedia pages 3 (derivative); third-party mirrors of docs (w3cub, unpkg-hosted copies, Sonatype mirror, kiwix) 6; news and aggregator articles about Vercel and Svelte (thenewstack) 3; Angular secondary explainers (angular.love, angularindepth, mungomash brief) 3: derivatives of K11, used only to confirm the 2026 cadence change, never cited; tutorialspoint htmx page 1; tessl registry and lemmy threads 2; O'Reilly book chapter on htmx 1 (not read). Stack Overflow 0 surfaced. State-of-JS style popularity surveys: deliberately not searched (policy: popularity is not authority).

### Searches run (queries)

1. lit.dev security Trusted Types lit-html docs
2. htmx essays web security basics with htmx
3. Web Almanac 2025 JavaScript chapter frameworks libraries usage HTTP Archive
4. Web Almanac 2025 Jamstack OR "Frameworks" OR "Web Components" chapter
5. Svelte governance maintainers Svelte Society Vercel employs Rich Harris project structure
6. Angular supported versions LTS 12 months "Angular" release schedule v23 date

Direct fetches (not searches) covered the remaining URLs in the table plus: https://react.dev/versions (React 19.3 current as of 2026-09-09), https://react.dev/blog, https://angular.dev/about, https://v2.vuejs.org/ (Vue 2 stated end of life), https://lit.dev/docs/releases/upgrade/ (Lit 3; interoperable with 2.x; TypeScript 5.2+ for standard decorators), https://almanac.httparchive.org/en/2025/{table-of-contents,cms,performance,third-parties} (no framework data; CMS and performance chapters explicitly lack it), https://github.com/facebook/react/security/policy (points to Meta's whitehat program; no supported-version statement), https://github.com/sveltejs/svelte (README), https://docs.solidjs.com/ (no security section), https://github.com/bigskysoftware/htmx/security/policy.

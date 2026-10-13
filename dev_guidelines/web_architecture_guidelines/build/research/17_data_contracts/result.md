# Research result: DCON, data contracts across tiers

## L1 headline

Best practice on data contracts is well established in its parts (explicit schema plus semantics, parse at the boundary, tolerant readers, additive evolution, schema diff and consumer-driven tests in CI, constraints in the database) but no source prescribes the whole chain database schema -> Python models -> OpenAPI/JSON Schema -> TypeScript types; that chain is our synthesis (inferred), and the data-engineering contract standard (ODCS) is useful as a checklist, not as a format, for one application database.

Pinned:
- Sources by tier: T1 6, T2 5, T3 8 (19 in total)
- Claims: 27 (new; matches to ledger rows are cited by id, not recounted)
- Contested topics: code-first vs design-first contract; one model vs separate table and API models; contract tests in a single-team app; database schema as the API (L187)
- Failed T1 fetches: none (PostgREST docs, T3, answered 429 twice; the same page was read from its source copy on GitHub)

## L2 claims

Pinned:
- Sources by tier: T1 6, T2 5, T3 8 (19 in total)
- Claims: 27 (new; matches to ledger rows are cited by id, not recounted)
- Contested topics: code-first vs design-first contract; one model vs separate table and API models; contract tests in a single-team app; database schema as the API (L187)
- Failed T1 fetches: none (PostgREST docs, T3, answered 429 twice; the same page was read from its source copy on GitHub)

Clusters:
1. A contract is schema plus semantics; a schema cannot carry units, time zone, precision or invariants, so those are written down beside it; null and absent are two separate axes. Consensus, grounded. C01-C03
2. One JSON Schema dialect runs through the stack (OpenAPI 3.1 = JSON Schema 2020-12, Pydantic emits it); request and response schemas can differ and both are published. Consensus, grounded. C04, C05
3. Python-side contract is derived from typed models (FastAPI/Pydantic) with separate input and output models, output validated and filtered. Majority, grounded; conflicts with design-first L272. C06-C08
4. Parse, do not validate: turn input into precise types once, at the boundary; keep one source of truth, duplicates drift. Consensus (one T2 source, no dissent), grounded. C09-C11, C16
5. Full derivation chain is not stated by any source; its links are (SQLModel one-class, Pydantic to JSON Schema, OpenAPI to TypeScript types). Inferred. C12, C13
6. Consumers tolerate; schemas are open for readers and closed for writers; codegen from a closed full schema is brittle. Consensus, grounded; extends L057. C14, C15
7. Contract testing: consumer contracts are open and incomplete, provider contract closed and complete; Pact tests what consumers use, a schema diff tests all possible states; cadence and scope differ. Majority; single-team need contested. C17-C21
8. The database is the last-enforced half of the contract: constraints, domains, named constraints; a contract schema of views and functions is one option. Consensus for constraints, contested for database-as-API. C22-C24
9. Data-engineering contracts (ODCS) add ownership, lifecycle status, quality, SLA and a logical/physical type split; adopt as checklist. Inferred applicability. C25-C27

Live debates:
- Code-first (spec derived from typed models) vs design-first (spec written first): FastAPI/Pydantic path vs L272.
- One class for table and validation (SQLModel) vs separate table, input and output models (FastAPI).
- Are contract tests worth it for a single team's own browser client and server (Pact: applicable to client and front-end; L402: schema checks enough)?
- Database schema of views and functions as the API (PostgREST) vs application API (L187).

Not covered: Django forms/serializers as contracts; database-first code generators (reverse from Postgres schema); runtime validation libraries in the browser; GraphQL SDL; Protobuf/Avro schema registries and their compatibility modes; message and event contracts (boundary: consistency/ordering, async); JSONB column contracts; the Postgres-to-Python type mapping details.

## L3 full

Pinned:
- Sources by tier: T1 6, T2 5, T3 8 (19 in total)
- Claims: 27 (new; matches to ledger rows are cited by id, not recounted)
- Contested topics: code-first vs design-first contract; one model vs separate table and API models; contract tests in a single-team app; database schema as the API (L187)
- Failed T1 fetches: none (PostgREST docs, T3, answered 429 twice; the same page was read from its source copy on GitHub)

### Source register

| id | tier | title, author | URL read | authoritative on |
|---|---|---|---|---|
| DCON-S01 | T1 | JSON Schema reference: object (additionalProperties, required, unevaluatedProperties), json-schema.org | https://json-schema.org/understanding-json-schema/reference/object | open vs closed objects, required vs null |
| DCON-S02 | T1 | JSON Schema reference: type, json-schema.org | https://json-schema.org/understanding-json-schema/reference/type | null, integer/number, format as annotation |
| DCON-S03 | T1 | OpenAPI Specification (latest), OpenAPI Initiative | https://spec.openapis.org/oas/latest.html | purpose of an API description, 3.1 and JSON Schema 2020-12 |
| DCON-S04 | T1 | PostgreSQL docs: Constraints | https://www.postgresql.org/docs/current/ddl-constraints.html | what the database enforces, null semantics |
| DCON-S05 | T1 | PostgreSQL docs: CREATE DOMAIN | https://www.postgresql.org/docs/current/sql-createdomain.html | domains, null pitfalls |
| DCON-S06 | T1 | FastAPI docs: Response Model | https://fastapi.tiangolo.com/tutorial/response-model/ | code-first schema from types, output filtering |
| DCON-S07 | T2 | Parse, don't validate, Alexis King | https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/ | parsing at the boundary, illegal states |
| DCON-S08 | T2 | Tolerant Reader, Martin Fowler | https://martinfowler.com/bliki/TolerantReader.html | reader tolerance, codegen brittleness |
| DCON-S09 | T2 | Consumer-Driven Contracts, Ian Robinson on martinfowler.com | https://martinfowler.com/articles/consumerDrivenContracts.html | provider vs consumer contracts |
| DCON-S10 | T2 | Contract Test, Martin Fowler | https://martinfowler.com/bliki/ContractTest.html | verifying test doubles, cadence |
| DCON-S11 | T2 | Open Data Contract Standard (overview, fundamentals, schema pages), Bitol / Linux Foundation | https://bitol-io.github.io/open-data-contract-standard/latest/ (and /fundamentals/, /schema/) | data-engineering contract fields |
| DCON-S12 | T3 | Pydantic docs: JSON Schema | https://pydantic.dev/docs/validation/latest/concepts/json_schema/ | model to JSON Schema, modes |
| DCON-S13 | T3 | Pydantic docs: Strict Mode | https://pydantic.dev/docs/validation/latest/concepts/strict_mode/ | coercion, strict, JSON input |
| DCON-S14 | T3 | PostgREST docs: Schema Isolation (read from source copy on GitHub; docs host returned 429) | https://raw.githubusercontent.com/PostgREST/postgrest-docs/main/docs/explanations/schema_isolation.rst | database as API |
| DCON-S15 | T3 | Pact docs: introduction | https://docs.pact.io/ | consumer-driven contract testing, vs schema |
| DCON-S16 | T3 | Pact docs: how Pact works | https://docs.pact.io/getting_started/how_pact_works | pact file, provider verification |
| DCON-S17 | T3 | oasdiff README | https://github.com/oasdiff/oasdiff | breaking-change detection in CI |
| DCON-S18 | T3 | openapi-typescript docs | https://openapi-ts.dev/introduction | TypeScript types from OpenAPI |
| DCON-S19 | T3 | SQLModel docs, Sebastian Ramirez | https://sqlmodel.tiangolo.com/ | one class for table and validation |

### Claims

Format: level | stack | sources | agreement | certainty. Ledger matches: L009, L019, L040, L056, L057, L171, L174, L187, L214, L272, L273, L274, L401, L402.

- **DCON-C01** A data contract is an explicit artifact stating structure and meaning (names, types, nullability, units, invariants, owner, version), readable without access to the producer's source code. | principle | neutral | S03 (purpose), S11 | consensus | grounded (S03, S11); synthesis for "units, invariants" inferred.
- **DCON-C02** Treat a schema as necessary but not sufficient: JSON `format` is only an annotation unless a validator is told to assert it, JSON has no integer/float or date type, and Pydantic emits Decimal as a string; record units, time zone, precision and rounding in the contract text or in constraints. | practice | http | S02, S12 | consensus | grounded.
- **DCON-C03** Declare "may be null" and "may be absent" separately: in JSON Schema a null value is not the same as a missing property, and a Pydantic Optional field allows null. | practice | http | S01, S12 | consensus | grounded. Related: L171.
- **DCON-C04** Use one schema dialect across tiers: OpenAPI 3.1 adopts JSON Schema 2020-12 in full, and Pydantic emits schemas compliant with both; prefer type arrays to the old OpenAPI-only `nullable`. | practice | python, http | S03, S12 | consensus | grounded.
- **DCON-C05** Publish request and response schemas separately where they differ: Pydantic generates schema in validation mode by default and in serialization mode on request, and the two can differ for custom-serialized fields. | practice | python | S12 | consensus (single source) | grounded.
- **DCON-C06** In Python, a typed model can be the source from which the API description is generated (code-first); the generated description is then a build artifact to be committed or checked, not hand-edited. | decision | python | S06, S12 | contested | positions: code-first via FastAPI/Pydantic (S06, derived schema, less duplication) vs design-first (L272: Zalando, OpenAPI Initiative, flags generated descriptions as incomplete). Code-first fits one team that owns both ends; design-first fits independent consumers. | grounded for the mechanism; the condition is inferred. Extends L272, L273.
- **DCON-C07** Use separate input and output models so the response model limits and filters what leaves the server (e.g. a password field in the input never appears in the output). | practice | python | S06 | consensus (single source) | grounded. boundary: SEC.
- **DCON-C08** A response that fails its response model is a defect in server code, not a client error: the framework returns a server error rather than a malformed body. | practice | python | S06 | consensus (single source) | grounded.
- **DCON-C09** Parse, do not validate: convert untrusted input into the most precise type you need once, at the system boundary, before any of it is acted on; scattered re-checking deeper in the code ("shotgun parsing") lets partly processed invalid data through. | principle | neutral | S07 | consensus (single source, no dissent) | grounded. Related: L019 (server re-validation).
- **DCON-C10** Model data with the most precise structure reasonably available so illegal states cannot be represented; on this stack the precision is carried by Pydantic types at the boundary and by NOT NULL, CHECK, foreign keys and domains in Postgres. | principle | neutral | S07, S04 | consensus | grounded (S07); mapping to the stack inferred. Related: L040, L174.
- **DCON-C11** Keep one source of truth per fact: duplicated representations create "the places getting out of sync" as a representable illegal state, which applies to hand-copied type definitions across database, Python and browser. | principle | neutral | S07 | consensus (single source) | grounded for the sentence; application to cross-tier types inferred.
- **DCON-C12** Single source of truth for types across tiers: no source read recommends the whole chain database schema -> Python models -> OpenAPI/JSON Schema -> TypeScript types; the links exist (SQLModel merges table and validation class, Pydantic emits JSON Schema, openapi-typescript emits types from OpenAPI), so choose and record where the chain starts (database, Python models, or the OpenAPI file). | decision | python, js, postgres | S19, S12, S18, S06 | contested | positions: one class for table and validation (S19, "no need to duplicate models") vs separate table, input and output models (S06 shows separate In/Out; S19 does not discuss separation). Applies: one class for simple CRUD; separate models once API shape differs from storage shape. | inferred.
- **DCON-C13** TypeScript types generated from OpenAPI are runtime-free: they check code at build time and do not validate what the server actually sends, so runtime validation of server responses in the browser is a separate decision. | practice | js | S18 | consensus (single source) | grounded for "runtime-free"; the consequence is inferred. Related: L009 (skew).
- **DCON-C14** Generating consumer code from the full producer schema trades resilience for convenience: Fowler notes schema-driven generation is quick but brittle when the service evolves, and prefers readers that take only the elements they need; apply this to generated clients (read what you use, ignore the rest). | practice | neutral | S08, S09 | consensus | grounded. Extends L057.
- **DCON-C15** Treat object schemas as open for readers and closed for writers: JSON Schema permits additional properties by default; set `additionalProperties: false` on request bodies you control, not on response schemas consumers parse; note `additionalProperties` ignores properties from `allOf` branches, so use `unevaluatedProperties` for composed schemas. | practice | http | S01 | consensus (single source) | grounded for the keyword behavior; the reader/writer rule is inferred (from S01 plus L057).
- **DCON-C16** Decide coercion at the boundary explicitly: Pydantic coerces by default (the string "123" becomes 123), strict mode errors instead, and strict mode is looser for JSON input than for Python input; pick strictness per boundary (JSON API vs form or query string, where coercion is needed). | decision | python | S13 | consensus (single source) | grounded.
- **DCON-C17** Distinguish the two contract kinds: a provider contract is closed, complete, singular and authoritative; consumer contracts are open, incomplete and multiple, and the contract that matters for change is the union of what consumers actually use. Consumer-driven contracts fit a single enterprise or closed community, make hidden coupling explicit rather than removing it, and risk consumer demands eroding the service's conceptual integrity. | principle | neutral | S09 | consensus (single source) | grounded. Extends L401.
- **DCON-C18** A schema or specification describes all possible states of a resource; a Pact contract is generated from consumer tests, covers only what the consumer uses, and is replayed against the provider; use both, for different questions (can the provider shape drift vs does this consumer still work). | practice | neutral | S15, S16 | consensus | grounded.
- **DCON-C19** Whether a single team's own browser client and server need consumer-driven tests is open: Pact states contract testing applies "anywhere you have two services that need to communicate - such as an API client and a web front-end" and shines with many services; the ledger's L402 inferred that schema checks plus a few consumer tests suffice. | decision | neutral | S15, S09 | contested | positions: Pact docs (apply to any client and front-end pair); S09 (closed community, shared channel needed); L402 (inferred, single-team monolith). Applies: the more consumers or independent release cadences, the stronger the case. | open. Extends L402.
- **DCON-C20** Contract tests that verify test doubles of external services run on the rhythm of changes to the external service (often once a day), not on every commit, and a failure triggers a task to realign, possibly a conversation with the supplier. | practice | neutral | S10 | consensus (single source) | grounded. Extends L401.
- **DCON-C21** Run a breaking-change diff between the API description on the main branch and the proposed one in CI; oasdiff offers a `breaking` command, a human-readable `changelog`, a GitHub Action and a pre-commit hook for OpenAPI 3.0 and 3.1. The diff covers description changes only; behavior and semantics need contract tests. | practice | http | S17 | consensus (single source) | grounded for the tool's features; "description only" is inferred. Extends L273, L274.
- **DCON-C22** The database may itself be the contract: expose a dedicated schema of views and functions, not tables, so internals can change while backwards compatibility holds, and the same layer gives a natural way to version the API; private data stays in schemas not exposed. | decision | postgres | S14 | contested | positions: PostgREST-style database-as-API (S14, single source family) vs application API over base tables with migration discipline (L187). Applies: several consumers or strict privilege separation favor the contract schema; a single app server owning the database does not need it. | grounded for S14's statement; condition inferred. Resolves L187's unread source (now read, T3). boundary: DATA.
- **DCON-C23** Constraints are the contract half that holds whichever code writes: violations raise errors even for default values; NOT NULL equals CHECK (col IS NOT NULL); a CHECK passes on NULL; unique does not collide NULLs by default; foreign keys skip null referencing columns. Mirror the Python model's constraints against them, and name constraints explicitly so the application can map a violation to a stable contract error. | practice | postgres | S04 | consensus | grounded for the semantics; mirror and naming advice inferred (Postgres picks a name if none is given). Extends L040, L171, L174, L214. boundary: DATA.
- **DCON-C24** Use domains to define a reusable constraint once (an email or postal-code type); design the domain check to allow NULL and apply NOT NULL on the column, because a column of a NOT NULL domain can still read as null in some conversions; change a domain's check by drop, adjust, re-add so stored data is rechecked. | practice | postgres | S05 | consensus (single source) | grounded. boundary: DATA.
- **DCON-C25** Data contracts in the data-engineering sense (ODCS) are a platform-agnostic YAML document with sections for fundamentals, schema, quality, SLA, team, roles, support and authoritative definitions; for one application database, take the field list as a checklist (owner, meaning, quality rules, freshness or availability promise, lifecycle) and skip the format unless data leaves the application for a platform team. | decision | neutral | S11 | open | inferred (ODCS read; no source states whether it applies to an application database; the sources are aimed at shared data products).
- **DCON-C26** State types logically and map physically: ODCS separates logicalType (string, date, timestamp, number, integer, object, ...) from physicalType (VARCHAR(18)); mirror this by keeping the logical type in the contract and deriving the Postgres, Python and TypeScript types from it. | practice | neutral | S11 | consensus (single source) | grounded for the separation; the derivation is inferred.
- **DCON-C27** Give every contract one owner, a version and a lifecycle status: ODCS requires id and version and lists status values proposed, draft, active, deprecated, retired; Fowler's provider contract is singular and authoritative. | practice | neutral | S11, S09 | consensus | grounded. Related: L056, L275.

Matches only (no new claim): additive evolution L056; tolerant reader L057; skew L009; re-validation on the server L019; breaking-change list L274; OpenAPI conformance L273.

### Gaps (open)

- Django forms/serializers as contract sources and Django REST framework schema generation: not read.
- Database-first generators (sqlacodegen, Atlas, introspection into Pydantic): not read; claim C12 is therefore inferred.
- Runtime schema validation in the browser (Zod, Ajv): not read.
- Schema registries and compatibility modes (Avro, Protobuf, buf breaking): not read; boundary: async/event contracts belong to slot 16.
- Semantics of JSONB columns as contracts: not read.
- Whether ODCS suits an application database: no source addresses it; C25 is open.
- The search summary on oasdiff's severity tiers and 250 checks was not confirmed on a page read, so it is not used.

# J7 PIG-WEB.LOGIC (pig-web-defaults): questions to the maintainer

One question. Every other judged node of the Python backend branch is decided (`records.md`); the deferred node (Email and Push Delivery) is not judged.

## Should the login session cookie be `SameSite=Lax` or `SameSite=Strict`?

**Situation.** Human users stay logged in through a session cookie held by the Python backend. Browsers decide from the cookie's `SameSite` attribute whether to send it when the request comes from another site. Both values are recognised good practice, and the sources admit either. The forgery of state-changing requests is already handled by other layers (a form token, an origin check on unsafe requests), whichever value is chosen. The choice therefore trades two things the session itself is for:
- the session's function: keeping the user logged in when they arrive from a link on another site (an e-mail, a chat message, a search result);
- protection against attacks that open the application in the user's browser from another site with the user's session attached.

**Options and their costs.**
- **Lax.** The cookie is sent when the user follows a link from another site, so they arrive logged in. Cost: an attacker's page can also open or navigate to any page of the application with the session attached. A reflected script injection, or a cross-site leak reached through such a link, then runs as the user. The cookie specification's own draft calls Lax "only a speedbump" against these.
- **Strict.** The cookie is never sent on a request that starts on another site. Those attacks lose the session. Cost: every arrival from an outside link lands logged out on the first page. The user sees a login prompt or must click again, even with a valid session. This breaks the common flow of following a link to a specific record from an e-mail or a chat.
- **Lax plus a navigation check.** Lax, and the backend refuses (or redirects to a safe entry page) any navigation from another site to a logged-in page not declared an entry point. Browsers report the origin of a navigation in standard request headers. Cost: each project must declare its entry pages (home, deep links meant to be shared), and the check has to be built and tested. Browsers that send no such headers fall back to plain Lax.

**Recommendation.** Lax plus the navigation check for user-facing applications, and Strict for operator and administration consoles, which nobody should enter from an outside link. This keeps shared links working and closes most of what Strict closes.

**If unanswered, the guideline records**: the recommendation as the default, marked as awaiting the maintainer, with Strict required for operator consoles. The earlier argument that Strict "only protects requests that change nothing" is withdrawn: a request that changes nothing can still display the user's data or reflect attacker input under the session.

---

Not asked again here, because it is already with the maintainer: who filters reads of rows that carry per-user rules ("a draft is visible only to its author") when several backends share the database. The allocation judge raised it. Until it is answered, the access-control record carries:
- the stated default: each backend filters these reads from one shared written specification of the visibility rules, inside its read statement, with a shared suite of denial tests that every backend runs;
- the fallback, kept as acceptable: database read functions that receive the verified acting user, when a per-user read rule must hold for two or more backends. Under that answer, those reads go through the functions (in a short transaction that carries the acting user) and those tables lose direct reads;
- the consequence, stated so that nothing claims more: database roles that may read the base tables directly (reporting, operators) see every user's rows, comments included, unless their own role is restricted.

It is marked "awaiting maintainer".

Considered and not raised, with the reason:
- **Which Python framework** (Django or FastAPI). The sources give no neutral criteria. The settled verdicts do: sessions held by the server and revocable, CSRF protection from the framework itself, server-rendered HTML with forms, synchronous handlers. Django provides all four; no FastAPI page read documents sessions. FastAPI's native Pydantic models serve the type chain, but Django can use Pydantic as a library, and the always-in-sync rule allows either origin. How Django produces the interface description is still to verify; the candidate is Django Ninja. So the security criteria decide: Django. FastAPI stays "acceptable when the backend serves only programs and agents with bearer tokens".
- **Delegating login to an OpenID Connect server, or keeping an own password store**. No source ranks the two. Delegation removes the password store and brings MFA, passkeys and breached-password checks from a service built for them. Agents as users need OAuth authorization anyway, which such a server supplies. The server can be an external provider or one the team runs itself, which removes cost and data-residency objections. The backend checks on every login that the required second factor was actually used. An own store stays "acceptable when no OpenID Connect server can be used or run", with the full password and throttling bar.
- **Upload path** (bytes straight to object storage, or through the application). Every file is unreadable until its type is verified from its content and a scan comes back clean, whichever path it takes. So the application's synchronous check adds no safety. Through the application, synchronous workers are held by transfers. So direct to storage, under a policy that fixes size, content type and key. Through the application stays "acceptable when a small file must be read within the same request".
- **Where the API version goes**. Five sources hold five positions. Evolution is additive by default, as the database function API's is. The JSON interface is served under `/v1` from the start, so that a later `/v2` never sits beside unversioned paths. A major version in the URL path is visible to links, logs, caches and agent tools. Dated headers with per-account pinning stay "acceptable when many external integrators must keep working indefinitely".
- **Where rate-limiter counters live** (Postgres or a cache service). This is already settled by the Postgres-first placement and its cache-store rule: Postgres until a measured load on the primary, then a cache service.

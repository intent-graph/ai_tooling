# J3 LOGIC (web-app-philosophy): questions to the maintainer

None.

No node of the LOGIC branch holds a genuine trade-off between forces the node itself serves: each of the eight nodes is decided (`records.md`).

Not asked again here, because it is already with the maintainer: who filters reads of rows that carry per-user rules ("a draft is visible only to its author") when several backends share the database. That question was raised by the allocation judge. Until it is answered, the secured-entry record carries:
- the stated default: each backend filters these reads from one shared written specification of the visibility rules, with a shared suite of denial tests that every backend runs;
- the fallback, kept as acceptable: database read functions that receive the verified acting user, when a per-user read rule must hold for two or more backends. Under that answer, those tables are read only through the functions;
- the consequence, stated so that nothing claims more: database roles that may read the base tables directly (reporting, operators) see every user's rows, comments included, unless their own role is restricted.

It is marked "awaiting maintainer".

Considered and not raised, with the reason:
- Whether MFA is required or only offered on human accounts: login friction is not a force the secured-entry node serves, so the max rule decides (required by default); "optional" stays as "acceptable when the application's audience cannot practically be required to use a second factor".
- Whether the JSON interface carries full hypermedia controls: the maintainer's decision that every interface description is always in sync with the implementation already fixes the contract programs and agents read; full hypermedia stays as "acceptable when independently developed clients must keep working over a long horizon without a shared, synchronised description".

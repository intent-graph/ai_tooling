# UID mapping for `pig-web-defaults`

The skeleton and the judge records name projection nodes `PIG-WEB.ROOT`, `PIG-WEB.<AREA>`,
`PIG-WEB.<AREA>.<SUB>...`. `ig-tool` requires the root uid to be exactly `ROOT` and every child
uid to start with its parent's uid, and the IntentGraph primers prescribe projection L1 uids of
the form `PIG-{SEMANTIC}-{COMPONENT}`. The built graph therefore uses:

| Skeleton and judge records | Built graph |
|---|---|
| `PIG-WEB.ROOT` | `ROOT` (display name "Web Defaults") |
| `PIG-WEB.<AREA>` | `PIG-WEB-<AREA>` |
| `PIG-WEB.<AREA>.<rest>` | `PIG-WEB-<AREA>.<rest>` |

Cross-graph references to the projection root read `pig-web-defaults:ROOT`. Judge records and
the skeleton keep the original notation; read them through this table.

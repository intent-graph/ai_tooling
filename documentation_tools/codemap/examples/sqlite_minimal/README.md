# SQLite Minimal Example

This folder contains a small snapshot showing how SQLite structure appears in CodeMap YAML output.

- `focus_users.yaml`: focus on a `db_table` node with `~columns`.

The example shape is:

- database file node under its path in the hierarchy
- table nodes as leaves (or under schema nodes when multiple/non-main schemas exist)
- `~columns` list under each table node

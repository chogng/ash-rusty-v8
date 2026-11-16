# Ash V8 dependency distribution

This repository owns sandbox-enabled V8 archive/binding releases for Ash.
It does not release the Ash application. Release tags use `rusty-v8-v<version>`.

`build-inputs.json` pins the exact build harness and consumer regression suite.
`upstream-source-lock.json` records the upstream revision and source patches for
the initial release. Workflows validate the corresponding source lock from the
pinned harness before building; bump both declarations together.

The initial `rusty-v8-v152.2.0` release imports byte-identical verified archives,
bindings, checksums and build provenance from the original Ash dependency release:
https://github.com/chogng/ash/releases/tag/rusty-v8-v152.2.0
Its native verification records remain linked there. No binaries are rebuilt or
silently replaced during the import. The original release remains available.

The source-validation workflow has its own queue. It runs when pinned build inputs
or upstream source declarations change, or through manual dispatch. Fixed inputs
do not trigger scheduled source rebuilds; workflow-only edits use manual validation. Tagging a
new pinned version builds all eight targets, runs native consumer checks, verifies
provenance and publishes an immutable prerelease without taking over `latest`.
Manual release-workflow runs validate and stage artifacts without publishing.
Consumers adopt a generated runtime-lock only after the release is verified.

Third-party engine code remains under its upstream licenses. Build recipes retain
the repository license; build provenance identifies the exact upstream sources.

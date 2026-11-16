# Ash V8 dependency distribution

This repository owns sandbox-enabled V8 source production, archive/binding pairs,
producer toolchains and native artifact probes. It builds without an Ash checkout.
`upstream-source-lock.json` owns the exact upstream revision, sort backport and
Windows tool inputs. `MODULE.bazel` owns the pinned Bazel C++ graph and Chromium
runtime libraries. The Cargo workspace contains only the independent artifact probe.

The current crate version remains **152.2.0**. Existing immutable release assets
remain unchanged. The original imported release retains its verified build evidence:
https://github.com/chogng/ash/releases/tag/rusty-v8-v152.2.0

## Validation and publication

- Producer-input PRs run recipe contracts and Linux/Windows source checks.
- Main pushes run recipe contracts and version checks. Fixed recipes have no schedule.
- Manual source validation builds Linux/Windows pairs and executes their probes.
- Tags `rusty-v8-v<version>` build all eight targets, execute native probes, verify
  provenance and publish an immutable prerelease without replacing `latest`.
- Manual release runs execute the same full matrix without publishing. Staged inputs
  may be reused only after the existing immutable-source checks pass.

```sh
python3 -B -m unittest -v build.v8.test_release build.v8.test_smoke
python3 -B build/v8/release.py metadata
python3 -B build/v8/release.py bazel-stage --target x86_64-unknown-linux-gnu --output dist/x86_64-unknown-linux-gnu
python3 -B build/v8/smoke.py cargo-test --target x86_64-unknown-linux-gnu --artifacts dist/x86_64-unknown-linux-gnu
python3 -B build/v8/smoke.py bazel --target x86_64-unknown-linux-gnu --artifacts dist/x86_64-unknown-linux-gnu --output .cache/bazel-probe
```

Bazel and the Cargo toolchain are pinned by `.bazelversion` and `rust-toolchain.toml`.
Windows production uses the upstream GN entrypoint and its separately pinned
compiler/toolchain. GNU and musl ARM64 probes are cross-linked and executed on
native ARM64 runners. Every release contains checksums and source/build provenance.
Aggregation rejects incomplete, corrupt or mixed input sets before creating a
candidate `runtime-lock.json`.

Ash owns its consumer lock, verified acquisition and product runtime mitigations.
Consumers adopt a verified candidate lock separately from dependency production;
product CI does not invoke this repository's source builds or release workflow.
Third-party engine code retains its upstream licenses. Local build recipes retain
the repository license.

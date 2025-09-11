# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [1.2.0](https://github.com/pawamoy/mkdocs-coverage/releases/tag/1.2.0) - 2025-09-11

<small>[Compare with 1.1.0](https://github.com/pawamoy/mkdocs-coverage/compare/1.1.0...1.2.0)</small>

### Features

- Add `placeholder` option to insert report in existing page ([f406efa](https://github.com/pawamoy/mkdocs-coverage/commit/f406efa6de548115f3067e8b91717da64b69456a) by HeinrichAD). [PR-11](https://github.com/pawamoy/mkdocs-coverage/pull/11)

### Code Refactoring

- Move submodules under internal folder ([0bb1479](https://github.com/pawamoy/mkdocs-coverage/commit/0bb1479a6ff0d364b4ed6b378138bd19e941029e) by Timothée Mazzucotelli).

## [1.1.0](https://github.com/pawamoy/mkdocs-coverage/releases/tag/1.1.0) - 2024-06-11

<small>[Compare with 1.0.0](https://github.com/pawamoy/mkdocs-coverage/compare/1.0.0...1.1.0)</small>

### Build

- Depend on MkDocs 1.6+ ([d2e93b6](https://github.com/pawamoy/mkdocs-coverage/commit/d2e93b6b23ca714351c09f96cf8dd2c444c77b00) by Timothée Mazzucotelli).

### Code Refactoring

- Use more modern features of MkDocs, rename `page_name` to `page_path` to allow nested pages ([6087394](https://github.com/pawamoy/mkdocs-coverage/commit/60873943a87c88349956efd9fd854f20ff134968) by Timothée Mazzucotelli).

## [1.0.0](https://github.com/pawamoy/mkdocs-coverage/releases/tag/1.0.0) - 2023-08-02

<small>[Compare with 0.2.7](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.7...1.0.0)</small>

### Breaking Changes

- Drop support for Python 3.7

### Code Refactoring

- Stop using deprecated warning filter ([fb4d9e6](https://github.com/pawamoy/mkdocs-coverage/commit/fb4d9e6f7b34ecc66c596b7dc4f475a44ce0404c) by Timothée Mazzucotelli).

## [0.2.7](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.7) - 2023-04-11

<small>[Compare with 0.2.6](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.6...0.2.7)</small>

### Code Refactoring

- Stop using deprecated distutils ([47c129c](https://github.com/pawamoy/mkdocs-coverage/commit/47c129ce783cc5d908ec946d19010adb059fed0d) by Timothée Mazzucotelli).

## [0.2.6](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.6) - 2022-11-13

<small>[Compare with 0.2.5](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.5...0.2.6)</small>

### Bug Fixes
- Fix iframe width for recent Material versions ([67c530b](https://github.com/pawamoy/mkdocs-coverage/commit/67c530be834f2e0af251d3bc1db5138a54e6de72) by Timothée Mazzucotelli).


## [0.2.5](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.5) - 2021-12-16

<small>[Compare with 0.2.4](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.4...0.2.5)</small>

### Bug Fixes
- Support no directory URLs ([e427be0](https://github.com/pawamoy/mkdocs-coverage/commit/e427be0d8089629c23fba1879fb06fb4715d00e7) by Timothée Mazzucotelli). [Issue #5](https://github.com/pawamoy/mkdocs-coverage/issues/5)


## [0.2.4](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.4) - 2021-05-20

<small>[Compare with 0.2.3](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.3...0.2.4)</small>

### Bug Fixes
- Reset iframe height between page changes ([5519c13](https://github.com/pawamoy/mkdocs-coverage/commit/5519c1352759f36b5ff3e1f800ac41fd12cd4acb) by Timothée Mazzucotelli). [Issue #1](https://github.com/pawamoy/mkdocs-coverage/issues/1)


## [0.2.3](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.3) - 2021-05-16

<small>[Compare with 0.2.2](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.2...0.2.3)</small>

### Packaging

- Don't restrict supported Python versions to less than 3.10.


## [0.2.2](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.2) - 2021-05-06

<small>[Compare with 0.2.1](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.1...0.2.2)</small>

### Packaging

- Switch to PDM as project management tool.
- Stop including README.md and pyproject.toml in wheels. It was causing errors in PDM and Poetry when installed in parallel.


## [0.2.1](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.1) - 2021-02-03

<small>[Compare with 0.2.0](https://github.com/pawamoy/mkdocs-coverage/compare/0.2.0...0.2.1)</small>

### Bug Fixes
- Don't replace `index.html` everywhere ([ca1da70](https://github.com/pawamoy/mkdocs-coverage/commit/ca1da7003282b20af4cda72ae0ae62849dab1f63) by Timothée Mazzucotelli). [Issue #2](https://github.com/pawamoy/mkdocs-coverage/issues/2)


## [0.2.0](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.2.0) - 2021-02-03

<small>[Compare with 0.1.0](https://github.com/pawamoy/mkdocs-coverage/compare/0.1.0...0.2.0)</small>

### Features
- Implement coverage integration ([b52ac1d](https://github.com/pawamoy/mkdocs-coverage/commit/b52ac1def13c2dda648f4021b3d81f0e850001e4) by Timothée Mazzucotelli).


## [0.1.0](https://github.com/pawamoy/mkdocs-coverage/releases/tag/0.1.0) - 2021-02-03

<small>[Compare with first commit](https://github.com/pawamoy/mkdocs-coverage/compare/de2b9feab0e3f1a8ff8809a5ef9e9da55e201838...0.1.0)</small>

### Features
- Skeleton ([de2b9fe](https://github.com/pawamoy/mkdocs-coverage/commit/de2b9feab0e3f1a8ff8809a5ef9e9da55e201838) by Timothée Mazzucotelli).

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-09-24

### Added
- Multi-agent collaboration engine for hallucination evaluation.
- WebSocket support for real-time streaming of evaluation progress.
- Redis-based caching layer for repeated queries.
- Prometheus metrics integration for observability.
- MongoDB persistent storage for historical evaluations.
- Batch evaluation API.
- Robust async retry and circuit breaking via Tenacity.
- Comprehensive API and Architecture documentation.

### Changed
- Migrated core framework to FastAPI.
- Upgraded Python requirement to 3.10+.
- Re-architected evaluator pipeline to support DAG-based agent execution.

### Removed
- Deprecated v1 synchronous evaluation endpoints.
- Removed legacy filesystem caching.

## [1.0.0] - 2024-01-15

### Added
- Initial release of MAHE.
- Single-agent hallucination detection using OpenAI GPT-4.
- Basic REST API for evaluation.

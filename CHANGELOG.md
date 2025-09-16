[0.1.1] - 2025-09-12
Fixed
Corrected README typos (e.g., Academic) and spacing (2010 (Part‑Time)).
Added
Clear Modernisation note with original dates and context.
metrics/metrics.csv link in README (headline snapshot for recruiters).
Hardware‑safe RS‑485 smoke test and mock port; CI writes metrics on every run.# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
and this project adheres to [Semantic Versioning](https://semver.org/).

## [v0.1.0] - 2025-09-06
### Added
- Initial release of **Smart Energy Monitoring for Indian Hospitals**.
- RS485 serial logging script (hardware dependent).
- Mock-based test (`tests/test_mock_logger.py`) for CI.
- Demo replay script (`demo/replay_logger.py`) with sample metrics snapshot.
- Documentation (`README.md`, `docs/`) including disclaimer and background.
- Example metrics CSV (`metrics/snapshot.csv`).

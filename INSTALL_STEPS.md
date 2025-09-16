# Smart Energy Monitoring — Final install steps (very simple)

## Files to ADD to the repo (exact paths)
- `.github/workflows/rs485-smoke.yml`
- `src/energy/rs485/mock_port.py` (+ the `__init__.py` files included)
- `tests/test_rs485_smoke.py`
- `docs/BOM.md`
- `docs/wiring-diagram.svg`
- `metrics/metrics.csv`

## Files to EDIT
- `README.md`: paste the contents of `README_P0_block.md` near the top.
- `CHANGELOG.md`: paste the contents of `CHANGELOG_0.1.1.md` at the top.

## GitHub website steps (no command line)
1) Open your repo → **Add file** → **Upload files**.
2) Drag folders from this ZIP so paths are preserved ( `.github/`, `src/`, `tests/`, `docs/`, `metrics/` ). Click **Commit changes**.
3) Edit **README.md** → paste **README_P0_block.md** under the title → **Save**.
4) Edit **CHANGELOG.md** → paste **CHANGELOG_0.1.1.md** at the top → **Save**.
5) Open **Actions** → confirm **RS485-Smoke** turns **green**.
6) **Draft a new release** → Tag `v0.1.1` → Title “docs+tests: smoke test & BOM/wiring diagram; metrics snapshot” → **Publish**.

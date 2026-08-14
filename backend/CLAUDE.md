# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this directory.

## Static files

Static assets (e.g. `robots.txt`, and future files like images) live in
`backend/static/`.

- `app/routers.py` defines `STATIC_DIR = Path(__file__).resolve().parent.parent / "static"`,
  a constant pointing at `backend/static/`. `__file__` here is
  `app/routers.py`, so it takes two `.parent` steps: one to reach `app/`,
  and one more to reach `backend/` (the sibling of `static/`).
- `app/__init__.py` mounts this directory at `/static` via
  `fastapi.staticfiles.StaticFiles`, so any file placed in `backend/static/`
  becomes available at `/static/<filename>` automatically — no route needs
  to be added per file.
- `robots.txt` is the one exception: crawlers expect it at the site root
  (`/robots.txt`), not under `/static/`, so it additionally has a dedicated
  route in `app/routers.py` that returns it via `FileResponse`. It remains
  reachable at `/static/robots.txt` too (harmless duplicate), but `/robots.txt`
  is the canonical URL.

When adding a new static asset that does not need a root-level URL (e.g. an
image), just drop the file into `backend/static/` — no code changes needed.

## Oracle NoSQL Database

The app persists data in Oracle NoSQL Database via the `borneo` SDK
(`app/database.py`), which exposes a `NoSQLHandle` as a `wireup` injectable.
For local development, `docker compose up -d --wait` runs KVLite
(`ghcr.io/oracle/nosql:latest-ce`) as a local emulator; see `README.md` for
the full setup.

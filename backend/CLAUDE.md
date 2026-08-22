# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this directory.

## Static files

Static assets (e.g. `robots.txt`, and future files like images) live in
`backend/static/` and are mounted at `/static` in `app/__init__.py` via
`fastapi.staticfiles.StaticFiles`, so any file dropped in that directory is
served automatically — no route needs to be added per file. `robots.txt` is
the one exception: since crawlers expect it at the site root, it also has a
dedicated route in `app/routers.py` serving it at `/robots.txt`.

## Oracle NoSQL Database

The app persists data in Oracle NoSQL Database via the `borneo` SDK
(`app/database.py`), which exposes a `NoSQLHandle` as a `wireup` injectable.
For local development, `docker compose up -d --wait` runs KVLite
(`ghcr.io/oracle/nosql:latest-ce`) as a local emulator; see `README.md` for
the full setup.

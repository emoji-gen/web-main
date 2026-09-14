# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this directory.

## Commands

```sh
# install dependencies
uv sync
# start local Oracle NoSQL (KVLite)
make up
# run dev server (http://127.0.0.1:8000)
make dev
# run tests
uv run pytest
# stop local Oracle NoSQL (KVLite)
make down
```

## Static files

Static assets (e.g. `robots.txt`, and future files like images) live in
`backend/static/` and are mounted at `/static` in `app/__init__.py` via
`fastapi.staticfiles.StaticFiles`, so any file dropped in that directory is
served automatically — no route needs to be added per file. `robots.txt` is
the one exception: since crawlers expect it at the site root, it also has a
dedicated route in `app/routers.py` serving it at `/robots.txt`.

## Database

The app persists data in Oracle NoSQL Database via the `borneo` SDK
(`app/database.py`). See `docs/nosql.md` for concepts, local setup, and
commands.

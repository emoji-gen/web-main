# Emoji Generator Backend

FastAPI-based backend for Emoji Generator.

## Requirements

- Python `3.14.7` (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) - Python package and project manager

## Setup

Install dependencies:

```sh
$ uv sync
```

## Local Oracle NoSQL Database

The app connects to Oracle NoSQL Database. For local development this repo
uses the KVLite Community Edition Docker image
(`ghcr.io/oracle/nosql:latest-ce`) to emulate Oracle NoSQL Database.

Start it:

```sh
$ docker compose up -d --wait
```

Data persists in a named Docker volume across restarts; run
`docker compose down -v` to wipe it.

Stop it:

```sh
$ docker compose down
```

### Connecting to a different endpoint

Set `NOSQL_ENDPOINT` (default `http://localhost:8080`) to point the app at
a different KVLite instance.

## Development

Start the local NoSQL database (see above), then run the development server:

```sh
$ uv run uvicorn app:app --reload --loop uvloop
```

The API will be available at http://127.0.0.1:8000.

## Testing

```sh
$ uv run pytest
```

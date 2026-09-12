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

## Database

The app connects to Oracle NoSQL Database. See [`docs/nosql.md`](docs/nosql.md)
for concepts, local setup, and commands.

## Development

Start the local NoSQL database (see [`docs/nosql.md`](docs/nosql.md)), then
run the development server:

```sh
$ uv run uvicorn app:app --reload --loop uvloop
```

The API will be available at http://127.0.0.1:8000.

## Testing

```sh
$ uv run pytest
```

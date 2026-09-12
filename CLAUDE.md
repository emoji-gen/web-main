# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Language

- Communicate with the user in Japanese in chat.
- Write commit messages, documentation, and source code comments in English.

## Git

- Never run `git push` unless the user explicitly asks for it.

## About

Emoji Generator — custom emoji/stamp image generator service. Image rendering
uses the Skia graphics library.

## Structure

- `backend/` — active dev. FastAPI + wireup(DI) + Oracle NoSQL(`borneo`). Details: `backend/CLAUDE.md`.
- `server/` — legacy backend (aiohttp + MySQL, Python 2.7/3.7). Don't add new features here.
- `frontend-old/` — legacy frontend (Vue + webpack, Node 12, Yarn). Don't add new features here.
- New frontend for `backend/` doesn't exist yet.

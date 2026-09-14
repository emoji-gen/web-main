.PHONY: up down dev

up:
	docker compose up -d --wait

down:
	docker compose down

dev:
	uv run uvicorn app:app --reload --loop uvloop

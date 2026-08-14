from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse
from wireup.integration.fastapi import WireupRoute

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

router = APIRouter(route_class=WireupRoute)


@router.get("/")
def index():
    return "Hello"


@router.get("/robots.txt", include_in_schema=False)
def robots_txt():
    return FileResponse(STATIC_DIR / "robots.txt")

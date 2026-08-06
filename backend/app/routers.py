from fastapi import APIRouter
from wireup.integration.fastapi import WireupRoute

router = APIRouter(route_class=WireupRoute)


@router.get("/")
def index():
    return "Hello"

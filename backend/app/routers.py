from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from borneo import NoSQLHandle, PutRequest, TableRequest, TimeToLive
from fastapi import APIRouter
from fastapi.responses import FileResponse
from wireup import Injected
from wireup.integration.fastapi import WireupRoute

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

NOSQL_CHECK_TABLE_NAME = "nosql_check"

router = APIRouter(route_class=WireupRoute)


@router.get("/")
def index():
    return "Hello"


@router.get("/robots.txt", include_in_schema=False)
def robots_txt():
    return FileResponse(STATIC_DIR / "robots.txt")


@router.post("/debug/nosql-check", include_in_schema=False)
def nosql_check(nosql_handle: Injected[NoSQLHandle]):
    nosql_handle.do_table_request(
        TableRequest().set_statement(
            f"CREATE TABLE IF NOT EXISTS {NOSQL_CHECK_TABLE_NAME}("
            "id STRING, created_at STRING, PRIMARY KEY(id))"
        ),
        30000,
        1000,
    )
    row_id = str(uuid4())
    nosql_handle.put(
        PutRequest()
        .set_table_name(NOSQL_CHECK_TABLE_NAME)
        .set_value({"id": row_id, "created_at": datetime.now(UTC).isoformat()})
        .set_ttl(TimeToLive.of_hours(1))
    )
    return {"id": row_id}

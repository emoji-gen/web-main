import wireup
import wireup.integration.fastapi
from fastapi import FastAPI

from app import database, routers

app = FastAPI()
app.include_router(routers.router)

#
# DI
#
container = wireup.create_async_container(
    injectables=[wireup.integration.fastapi, database],
)
wireup.integration.fastapi.setup(container, app)

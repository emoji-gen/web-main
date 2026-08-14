from collections.abc import Iterator
import os

from borneo import NoSQLHandle, NoSQLHandleConfig
from borneo.kv import StoreAccessTokenProvider
from wireup import injectable


#
# DI
#
@injectable
def nosql_handle_factory() -> Iterator[NoSQLHandle]:
    endpoint = os.environ.get("NOSQL_ENDPOINT", "http://localhost:8080")
    provider = StoreAccessTokenProvider()
    config = NoSQLHandleConfig(endpoint, provider)
    handle = NoSQLHandle(config)
    try:
        yield handle
    finally:
        handle.close()

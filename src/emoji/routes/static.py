# -*- encoding: utf-8 -*-

from pathlib import Path

from aiohttp.web import FileResponse


async def favicon(request):
    path = str(Path(request.app['config']['assets_path']).joinpath('favicon.ico'))
    return FileResponse(path)



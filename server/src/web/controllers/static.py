# -*- encoding: utf-8 -*-

from pathlib import Path

from aiohttp.web import FileResponse


async def _make_file_response(request, fname):
    path = str(Path(request.app['config']['assets_path']).joinpath(fname))
    return FileResponse(path)


def favicon(request):
    return _make_file_response(request, 'favicon.ico')

def robots(request):
    return _make_file_response(request, 'robots.txt')


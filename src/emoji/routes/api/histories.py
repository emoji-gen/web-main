# -*- encoding: utf-8 -*-

from aiohttp import web
from funcy import project

async def all_v0(request):
    return web.json_response([])


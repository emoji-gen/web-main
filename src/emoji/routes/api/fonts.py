# -*- encoding: utf-8 -*-

from aiohttp import web
from funcy import project

async def all_v0(request):
    fonts = request.app['repos']['fonts'].all()
    return web.json_response(fonts)

async def all_v1(request):
    fonts = request.app['repos']['fonts'].all()
    limited_fonts = [ project(v, ['key', 'name']) for v in fonts ]
    return web.json_response(limited_fonts)

# -*- encoding: utf-8 -*-

from aiohttp import web
from funcy import project


async def all_v0(request):
    fonts = request.app['repos']['font'].all()

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(60 * 10) # 10 minutes
    return web.json_response(fonts, headers=headers)


async def all_v1(request):
    fonts = request.app['repos']['font'].all()
    result = [ project(v, ['key', 'name']) for v in fonts ]

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(60 * 10) # 10 minutes
    return web.json_response(result, headers=headers)

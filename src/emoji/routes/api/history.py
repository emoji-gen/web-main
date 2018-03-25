# -*- encoding: utf-8 -*-

from aiohttp import web
from funcy import project


async def all_v0(request):
    emoji_log_repository = request.app['repos']['emoji_log']
    emoji_logs = await emoji_log_repository.recently(limit=20)

    columns = ['text', 'color', 'back_color', 'font', 'size_fixed', 'align', 'stretch']
    result = [ project(v, columns) for v in emoji_logs ]

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 seconds
    return web.json_response(result, headers=headers)


async def all_v1(request):
    emoji_log_repository = request.app['repos']['emoji_log']
    emoji_logs = await emoji_log_repository.recently(limit=20)

    columns = ['text', 'color', 'back_color', 'font', 'size_fixed', 'align', 'stretch']
    result = [ project(v, columns) for v in emoji_logs ]

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 seconds
    return web.json_response(result, headers=headers)


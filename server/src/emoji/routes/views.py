# -*- encoding: utf-8 -*-

import json

import aiohttp_jinja2

from emoji.repositories import emoji_log_repository

async def index(request):
    return await _render(request, 'home.html')

async def contact(request):
    return await _render(request, 'contact.html')


async def _fetch_emoji_logs(emoji_service):
    emoji_logs_records = await emoji_log_repository.filter_recently()
    emoji_logs = [ {
        'text': v['text'],
        'url': emoji_service.make_url(
            v['text'],
            v['font'],
            v['color'],
            v['back_color'],
            v['size_fixed'],
            v['align'],
            v['stretch'],
        ),
    } for v in emoji_logs_records ]

    return emoji_logs


async def _render(request, template):
    fonts = json.dumps(request.app['repos']['font'].all())

    emoji_service = request.app['services']['emoji']
    emoji_logs = json.dumps(await _fetch_emoji_logs(emoji_service))

    response = aiohttp_jinja2.render_template(template, request, { 'fonts': fonts, 'emoji_logs': emoji_logs })
    if request.app.debug:
        response.headers['Cache-Control'] = 'private, no-store, no-cache, must-revalidate'
    else:
        response.headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 sec

    return response

# -*- encoding: utf-8 -*-

import json

import aiohttp_jinja2

from emoji.repositories import emoji_log

async def index(request):
    fonts = json.dumps(request.app['repos']['font'].all())
    response = aiohttp_jinja2.render_template('home.html', request, { 'fonts': fonts })

    await emoji_log.filter_recently()

    if request.app.debug:
        response.headers['Cache-Control'] = 'private, no-store, no-cache, must-revalidate'
    else:
        response.headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 sec

    return response


async def contact(request):
    fonts = json.dumps(request.app['repos']['font'].all())
    return aiohttp_jinja2.render_template('contact.html', request, { 'fonts': fonts })

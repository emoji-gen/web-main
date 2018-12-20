# -*- encoding: utf-8 -*-

import json

import aiohttp_jinja2


async def index(request):
    fonts = json.dumps(request.app['repos']['font'].all())
    response = aiohttp_jinja2.render_template('index.j2', request, { 'fonts': fonts })

    if request.app.debug:
        response.headers['Cache-Control'] = 'private, no-store, no-cache, must-revalidate'
    else:
        response.headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 sec

    return response



# -*- encoding: utf-8 -*-

import aiohttp_jinja2

@aiohttp_jinja2.template('index.j2')
async def index(request):
    return {}


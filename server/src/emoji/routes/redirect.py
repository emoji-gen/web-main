# -*- encoding: utf-8 -*-

from aiohttp.web_exceptions import HTTPMovedPermanently

async def blog(request):
    return HTTPMovedPermanently(
        '/blog/',
        headers={
            'Cache-Control': 'public, immutable, max-age=31536000',
        },
    )


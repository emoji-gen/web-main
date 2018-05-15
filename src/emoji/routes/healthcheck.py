# -*- encoding: utf-8 -*-

from aiohttp.web import Response


async def ok(request):
    return Response(
        body='OK',
        headers={
            'Cache-Control': 'private, no-store, no-cache, must-revalidate',
        },
        content_type='text/plain',
        charset='utf-8'
    )



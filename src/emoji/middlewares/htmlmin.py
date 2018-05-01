# -*- encoding: utf-8 -*-

import htmlmin
from aiohttp import web


def setup_htmlmin_middleware(app):
    app.middlewares.append(htmlmin_middleware())


def htmlmin_middleware():
    @web.middleware
    async def middleware(request, handler):
        response = await handler(request)
        if response.content_type == 'text/html':
            response.text = htmlmin.minify(
                response.text,
                remove_comments=True,
                remove_empty_space=True,
                reduce_empty_attributes=False,
                remove_optional_attribute_quotes=False,
                keep_pre=True,
            )
        return response
    return middleware

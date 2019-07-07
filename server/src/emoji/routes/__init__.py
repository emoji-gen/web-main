# -*- encoding: utf-8 -*-

from pathlib import Path

from emoji.routes import static, redirect
from emoji.routes.emoji import download, generate
from emoji.routes.api import font, history
from emoji.routes.healthcheck import ok
from emoji.routes.views import index


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/healthcheck', ok)
    app.router.add_get('/emoji', generate)
    app.router.add_get('/emoji_download', download)
    app.router.add_get('/blog', redirect.blog)
    app.router.add_get('/api/fonts', font.all_v0)
    app.router.add_get('/api/v1/fonts', font.all_v1)
    app.router.add_get('/api/histories', history.all_v0)
    app.router.add_get('/api/v1/histories', history.all_v1)
    app.router.add_get('/favicon.ico', static.favicon)
    app.router.add_get('/robots.txt', static.robots)
    _setup_static_routes(app)


def _setup_static_routes(app):
    app.router.add_static(
        '/static',
        str(Path(app['config']['project_path']).joinpath('public')),
        name='static',
        append_version=True,
    )


if __name__ == '__main__':
    pass

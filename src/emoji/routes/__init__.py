# -*- encoding: utf-8 -*-

from pathlib import Path

from emoji.routes.emoji import download, generate
from emoji.routes.api import fonts, histories
from emoji.routes.views import index


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/emoji', generate)
    app.router.add_get('/emoji_download', download)
    app.router.add_get('/api/fonts', fonts.all_v0)
    app.router.add_get('/api/v1/fonts', fonts.all_v1)
    app.router.add_get('/api/histories', histories.all_v0)
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

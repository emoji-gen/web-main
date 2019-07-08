# -*- encoding: utf-8 -*-

from pathlib import Path

from web.controllers import static, redirect
from web.controllers.emoji import download, generate
from web.controllers.api import font
from web.controllers.healthcheck import ok
from web.controllers import views


def startup(app):
    _setup_routes(app)
    _setup_static_routes(app)


def _setup_routes(app):
    # Views : ja
    app.router.add_get('/', views.index_ja)
    app.router.add_get('/result', views.index_ja)
    app.router.add_get('/contact', views.contact_ja)

    # Views :ko
    app.router.add_get('/ko', views.redirect_index_ko)
    app.router.add_get('/ko/', views.index_ko)
    app.router.add_get('/ko/result', views.index_ko)
    app.router.add_get('/ko/contact', views.contact_ko)

    app.router.add_get('/healthcheck', ok)
    app.router.add_get('/emoji', generate)
    app.router.add_get('/emoji_download', download)
    app.router.add_get('/blog', redirect.blog)
    app.router.add_get('/api/fonts', font.all_v0)
    app.router.add_get('/api/v1/fonts', font.all_v1)
    app.router.add_get('/favicon.ico', static.favicon)
    app.router.add_get('/robots.txt', static.robots)


def _setup_static_routes(app):
    app.router.add_static(
        '/assets',
        str(Path(app['config']['project_path']).joinpath('assets')),
        name='static',
        append_version=True,
    )

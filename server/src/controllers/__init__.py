# -*- encoding: utf-8 -*-

from pathlib import Path

from controllers import static, redirect
from controllers.emoji import download, generate
from controllers.api import font
from controllers.healthcheck import ok
from controllers import views


class Controllers():
    def __init__(self, context):
        self._context = context


    async def startup(self):
        app = self._context.app

        self._setup_routes(app)
        self._setup_static_routes(app)


    def _setup_routes(self, app):
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


    def _setup_static_routes(self, app):
        app.router.add_static(
            '/assets',
            str(Path(app['config']['project_path']).joinpath('assets')),
            name='static',
            append_version=True,
        )

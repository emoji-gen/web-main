# -*- encoding: utf-8 -*-

# import aiohttp_jinja2
from pathlib import Path
from aiohttp.web import Application

from emoji.config import Config
from emoji.context_holder import ContextHolder
from emoji.mysql import MySQL

from emoji.config import load_config
from emoji.db import init_db, close_db
from emoji.middlewares import setup_middlewares
from emoji.repos import setup_repos
from emoji.routes import setup_routes
from emoji.services import setup_services


class Context():
    @classmethod
    async def bootstrap(cls):
        if ContextHolder.context() is None:
            context = Context()
            await context.wait_until_complete()
            ContextHolder.set_context(context)
        return ContextHolder.context()


    def __init__(self):
        self._config = load_config()
        app = Application(debug=self._config['debug'])
        app['config'] = self._config

        setup_routes(app)
        setup_middlewares(app)
        setup_repos(app)
        setup_services(app)

        app.on_startup.append(init_db)
        app.on_cleanup.append(close_db)

        self._app = app

        new_config = Config()
        self._mysql = MySQL(new_config.mysql)


    async def wait_until_complete(self):
        await self._mysql.wait_until_complete()


    @property
    def app(self):
        return self._app

    @property
    def config(self):
        return self._config

    @property
    def mysql(self):
        return self._mysql

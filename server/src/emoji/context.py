# -*- encoding: utf-8 -*-

import asyncio
from pathlib import Path
from aiohttp.web import Application

from emoji.config import Config
from emoji.context_holder import ContextHolder
from emoji.mysql import MySQL

from emoji.config import load_config
from emoji.middlewares import setup_middlewares
from emoji.repos import setup_repos
from emoji.routes import setup_routes
from emoji.services import setup_services


class Context():
    @classmethod
    async def get_context(cls):
        if ContextHolder.context() is None:
            context = Context()
            await context.startup()
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

        app.on_cleanup.append(self.cleanup)

        self._app = app

        new_config = Config()
        self._mysql = MySQL(new_config.mysql)


    async def startup(self):
        await self._mysql.startup()


    def cleanup(self, app):
        self._mysql.cleanup()

    @property
    def app(self):
        return self._app

    @property
    def config(self):
        return self._config

    @property
    def mysql(self):
        return self._mysql

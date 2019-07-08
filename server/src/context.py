# -*- encoding: utf-8 -*-

import asyncio
from pathlib import Path
from aiohttp.web import Application

from context_holder import ContextHolder
from locales import Locales
from mysql import MySQL
from web import controllers, htmlmin, jinja2

from emoji.config import Config

from emoji.config import load_config
from emoji.repos import setup_repos
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

        setup_repos(app)
        setup_services(app)

        app.on_cleanup.append(self.cleanup)

        self._app = app

        new_config = Config()
        self._mysql = MySQL(new_config.mysql)
        self._locales = Locales(new_config.locales)


    async def startup(self):
        controllers.startup(self._app)
        jinja2.startup(self._app)
        htmlmin.startup(self._app)

        await self._mysql.startup()
        await self._locales.startup()


    def cleanup(self, app):
        self._mysql.cleanup()

    @property
    def app(self):
        return self._app

    @property
    def config(self):
        return self._config

    @property
    def locales(self):
        return self._locales

    @property
    def mysql(self):
        return self._mysql

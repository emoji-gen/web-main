# -*- encoding: utf-8 -*-

import asyncio
import os
from pathlib import Path
from aiohttp.web import Application

from config import Config
from context_holder import ContextHolder
from locales import Locales
from mysql import MySQL
from web import controllers, htmlmin, jinja2


from emoji.config import load_config
from emoji.repos import setup_repos
from emoji.services import setup_services


class Context():
    @classmethod
    async def get_context(cls):
        if ContextHolder.context is None:
            context = Context()
            await context.startup()
            ContextHolder.set_context(context)
        return ContextHolder.context


    def __init__(self):
        is_dev = os.getenv('PYTHON_ENV') != 'production'

        app = Application(debug=is_dev)
        app.on_cleanup.append(self.cleanup)

        old_config = load_config()
        app['config'] = old_config

        setup_repos(app)
        setup_services(app)



        self._config = Config(is_dev=is_dev)
        self._mysql = MySQL(self._config.mysql_config)
        self._locales = Locales(self._config.locales_config)

        self.is_dev = is_dev
        self.app = app


    async def startup(self):
        controllers.startup(self.app)
        jinja2.startup(self.app, self._config)
        htmlmin.startup(self.app)

        await self._mysql.startup()
        await self._locales.startup()


    def cleanup(self, app):
        self._mysql.cleanup()

    @property
    def is_prod(self):
        return not self.is_dev

    @property
    def config(self):
        return self._config

    @property
    def locales(self):
        return self._locales

    @property
    def mysql(self):
        return self._mysql

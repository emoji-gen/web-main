# -*- encoding: utf-8 -*-

import aiohttp_jinja2
from pathlib import Path
from aiohttp.web import Application

from emoji.config import setup_config
from emoji.middlewares import setup_middlewares
from emoji.repos import setup_repos
from emoji.routes import setup_routes
from emoji.services import setup_services

app = Application(debug=True)

setup_config(app)
setup_routes(app)
setup_middlewares(app)
setup_repos(app)
setup_services(app)


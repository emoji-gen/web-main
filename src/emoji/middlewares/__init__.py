# -*- encoding: utf-8 -*-

from emoji.middlewares.htmlmin import *
from emoji.middlewares.jinja2 import *

def setup_middlewares(app):
    setup_jinja2_middleware(app)

    if app['config']['htmlmin_enabled']:
        setup_htmlmin_middleware(app)


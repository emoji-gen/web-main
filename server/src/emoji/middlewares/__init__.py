# -*- encoding: utf-8 -*-

from emoji.middlewares.htmlmin import *

def setup_middlewares(app):
    if app['config']['htmlmin_enabled']:
        setup_htmlmin_middleware(app)


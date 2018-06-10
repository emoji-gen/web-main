# -*- encoding: utf-8 -*-

import aiohttp_jinja2
import jinja2
import time
from pathlib import Path


def setup_jinja2_middleware(app):
    templates_path = app['config']['templates_path']
    env = aiohttp_jinja2.setup(
        app,
        context_processors=[
            computed_processor(debug=app.debug),
            config_processor(config=app['config']),
        ],
        default_helpers=False,
        loader=jinja2.FileSystemLoader(templates_path)
    )


def computed_processor(debug):
    async def processor(request):
        return {
            'debug': debug,
            'time': time.time(),
        }
    return processor


def config_processor(config):
    async def processor(request):
        return {
            'title': config['templates']['title'],
            'base_url': config['base_url'],
            'js_url': config['assets']['js_url'] if 'assets' in config else None,
        }
    return processor


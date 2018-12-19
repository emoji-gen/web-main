# -*- encoding: utf-8 -*-

import re
import time
from pathlib import Path

import aiohttp_jinja2
import jinja2


def setup_jinja2_middleware(app):
    templates_path = app['config']['templates_path']
    env = aiohttp_jinja2.setup(
        app,
        context_processors=[
            computed_processor(debug=app.debug),
            config_processor(config=app['config']),
        ],
        default_helpers=False,
        filters={
            'squash': do_squash,
        },
        loader=jinja2.FileSystemLoader(templates_path)
    )


def computed_processor(debug):
    async def processor(request):
        return {
            'debug': debug,
            'DEBUG': debug,
            'TS': int(time.time()),
        }
    return processor


def config_processor(config):
    async def processor(request):
        return {
            'title': config['templates']['title'],
            'base_url': config['base_url'],
            'BASE_URL': config['base_url'],
            'CSS_URL': config['assets'].get('css_url') if 'assets' in config else None,
            'JS_URL': config['assets'].get('js_url') if 'assets' in config else None,
        }
    return processor


def do_squash(value):
    return re.sub(r'\s+', ' ', value)


# -*- encoding: utf-8 -*-

import re
import time
from pathlib import Path

import aiohttp_jinja2
import jinja2

from context_holder import ContextHolder
from web.request_utils import get_locale


def startup(app):
    templates_path = app['config']['templates_path']
    env = aiohttp_jinja2.setup(
        app,
        context_processors=[
            computed_processor(debug=app.debug),
            config_processor(config=app['config']),
        ],
        default_helpers=False,
        filters={
            'squash': _squash,
        },
        loader=jinja2.FileSystemLoader(templates_path)
    )


def computed_processor(debug):
    async def processor(request):
        return {
            'debug': debug,
            'DEBUG': debug,
            'TS': int(time.time() * 1000),
        }
    return processor


def config_processor(config):
    async def processor(request):
        return {
            'SITE_URL': config['base_url'],
            'base_url': config['base_url'],
            'BASE_URL': config['base_url'],
            'CSS_URL': config['assets'].get('css_url') if 'assets' in config else None,
            'JS_URL': config['assets'].get('js_url') if 'assets' in config else None,
            'localized': _localized(request),
        }
    return processor


def _squash(value):
    return re.sub(r'\s+', ' ', value)


def _localized(request):
    def do_localized(key, locale=None):
        locales = ContextHolder.context().locales
        if locale is None:
            return locales.get_message(key, get_locale(request))
        return locales.get_message(key, locale)
    return do_localized

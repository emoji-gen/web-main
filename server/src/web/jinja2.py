# -*- encoding: utf-8 -*-

import json
import re
import time
from pathlib import Path

import aiohttp_jinja2
import jinja2

from context_holder import ContextHolder
from web.request_utils import get_locale


def startup(app, config, locales):
    templates_path = app['config']['templates_path']
    env = aiohttp_jinja2.setup(
        app,
        context_processors=[
            computed_processor(debug=app.debug),
            config_processor(config=app['config']),
            locales_processor(locales_config=config.locales_config, locales=locales),
            fonts_processor(
                locales_config=config.locales_config,
                fonts_config=config.fonts_config),
        ],
        default_helpers=False,
        filters={
            'squash': _squash,
        },
        loader=jinja2.FileSystemLoader(templates_path),
        auto_reload=False,
        bytecode_cache=jinja2.FileSystemBytecodeCache()
    )

def _squash(value):
    return re.sub(r'\s+', ' ', value)




def computed_processor(debug):
    async def processor(request):
        return {
            'debug': debug,
            'DEBUG': debug,
            'TS': int(time.time() * 1000),
        }
    return processor

# ---------------------------------------------------------

def config_processor(config):
    async def processor(request):
        return {
            'SITE_URL': config['base_url'],
            'base_url': config['base_url'],
            'BASE_URL': config['base_url'],
            'CSS_URL': config['assets'].get('css_url') if 'assets' in config else None,
            'JS_URL': config['assets'].get('js_url') if 'assets' in config else None,
        }
    return processor


# ---------------------------------------------------------
# Locales
# ---------------------------------------------------------

def locales_processor(*, locales_config, locales):
    # Make JSON for each locale
    messages = {}
    for locale in locales_config.locales:
        messages[locale] = {
            'Home': {
                'title': '{} - {}'.format(
                    locales.get_message('site_name', locale),
                    locales.get_message('site_lead', locale)),
            },
            'Contact': {
                'title': '{} - {}'.format(
                    locales.get_message('contact_title', locale),
                    locales.get_message('site_name', locale)),
            },
        }
    messages_json = json.dumps(messages, ensure_ascii=False, separators=(',',':'))

    async def processor(request):
        return {
            'messages': messages_json,
            'localized': _localized(request),
        }
    return processor

def _localized(request):
    def do_localized(key, locale=None):
        locales = ContextHolder.context.locales
        if locale is None:
            return locales.get_message(key, get_locale(request))
        return locales.get_message(key, locale)
    return do_localized


# ---------------------------------------------------------
# Fonts
# ---------------------------------------------------------

def fonts_processor(*, locales_config, fonts_config):
    # Make JSON for each locale
    fonts = {}
    for locale in locales_config.locales:
        fonts[locale] = [{
            'key': v['key'],
            'name': v['name'],
        } for v in fonts_config.by_locale(locale) ]

    fonts_json = json.dumps(fonts, ensure_ascii=False, separators=(',',':'))

    async def processor(request):
        return {
            'fonts': fonts_json,
        }
    return processor

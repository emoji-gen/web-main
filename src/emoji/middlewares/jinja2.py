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
            request_processor(),
            computed_processor(debug=app.debug),
            config_processor(config=app['config']),
        ],
        default_helpers=False,
        loader=jinja2.FileSystemLoader(templates_path)
    )
    env.globals.update({
        'assets_path': assets_path,
    })


def request_processor():
    async def processor(request):
        protocol = request.headers.get('X-Forwarded-Proto', 'http')
        host = request.host
        return {
            'protocol': protocol,
            'host': host,
            'baseUrl': '{0}://{1}'.format(protocol, host),
        }
    return processor


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
        }
    return processor


@jinja2.contextfunction
def assets_path(context, path, *, resolve=False):
    # TODO: resolve のサポート
    return context['app'].router['static'].url_for(filename=path)


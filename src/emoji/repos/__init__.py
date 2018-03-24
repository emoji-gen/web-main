# -*- encoding: utf-8 -*-

from emoji.repos.fonts import FontRepository

def setup_repos(app):
    app['repos'] = {
        'fonts': FontRepository(app)
    }

# -*- encoding: utf-8 -*-

from emoji.repos.font import FontRepository

def setup_repos(app):
    app['repos'] = {
        'font': FontRepository(app),
    }

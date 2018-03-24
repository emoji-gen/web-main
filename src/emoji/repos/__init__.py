# -*- encoding: utf-8 -*-

from emoji.repos.fonts import FontRepository

def setup_repos(app):
    repos = {}
    repos['fonts'] = FontRepository(app)
    app['repos'] = repos

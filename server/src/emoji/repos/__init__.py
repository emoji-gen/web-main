# -*- encoding: utf-8 -*-

from emoji.repos.font import FontRepository
from emoji.repos.emoji_log import EmojiLogRepository

def setup_repos(app):
    app['repos'] = {
        'font': FontRepository(app),
        'emoji_log': EmojiLogRepository(app),
    }

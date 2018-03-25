# -*- encoding: utf-8 -*-

from emoji.services.emoji import EmojiService

def setup_services(app):
    app['services'] = {
        'emoji': EmojiService(app),
    }

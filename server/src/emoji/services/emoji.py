# -*- encoding: utf-8 -*-

import emojilib
import hashlib
from urllib.parse import urlencode, urljoin

class EmojiService():
    def __init__(self, app):
        self._app = app

    def make_url(
        self,
        text,
        font,
        color,
        back_color,
        size_fixed = False,
        align = 'center',
        stretch = True
    ):
        base_url = self._app['config']['base_url']
        payload = {
            'text': text,
            'font': font,
            'color': color,
            'back_color': back_color,
            'size_fixed': str(size_fixed).lower(),
            'align': align,
            'stretch': str(stretch).lower()
        }
        return urljoin(base_url, 'emoji') + '?' + urlencode(payload)

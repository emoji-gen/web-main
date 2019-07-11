# -*- encoding: utf-8 -*-

from urllib.parse import urlencode, urljoin

import emojilib

from context_holder import ContextHolder


def build(
    text,
    font,
    color,
    back_color,
    size_fixed=False,
    align='center',
    stretch=True,
    locale='ja'
):
    app_config = ContextHolder.context.config.app_config
    payload = {
        'text': text,
        'font': font,
        'color': color,
        'back_color': back_color,
        'size_fixed': str(size_fixed).lower(),
        'align': align,
        'stretch': str(stretch).lower(),
        'locale': locale,
    }
    return urljoin(app_config.site_url, 'emoji') + '?' + urlencode(payload)

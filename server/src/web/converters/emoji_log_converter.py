# -*- encoding: utf-8 -*-

from utils import emoji_url_utils


def convert(emoji_log):
    return {
        'text': emoji_log['text'].replace('\n', ' ').replace('\r', ''),
        'url': emoji_url_utils.build(
            text=emoji_log['text'],
            font=emoji_log['font'],
            color=emoji_log['color'],
            back_color=emoji_log['back_color'],
            size_fixed=emoji_log['size_fixed'],
            align=emoji_log['align'],
            stretch=emoji_log['stretch'],
            locale=emoji_log['locale'],
        ),
    }

# -*- encoding: utf-8 -*-

from ecode import (
    Ecode,
    EcodeAlign,
    EcodeEncoder,
    EcodeFlag,
    EcodeFmt,
    EcodeLocale,
    EcodeSize,
)

from utils import emoji_url_utils
from context_holder import ContextHolder


def convert(emoji_log):
    flags = set()
    if emoji_log['size_fixed']:
        flags.add(EcodeFlag.SIZE_FIXED)
    if emoji_log['stretch']:
        flags.add(EcodeFlag.STRETCH)

    fonts_config = ContextHolder.context.config.fonts_config
    fonts = fonts_config.by_locale(emoji_log['locale'])
    font = next(filter(lambda f: f['key'] == emoji_log['font'], fonts), None)
    if not font:
        raise 'Font not found : locale={}, font={}'.format(
            emoji_log['locale'], emoji_log['font'])

    ecode = Ecode(
        locale=EcodeLocale.from_code(emoji_log['locale']),
        flags=flags,
        align=EcodeAlign.from_code(emoji_log['align']),
        size=EcodeSize.MDPI,
        fmt=EcodeFmt.PNG,
        font_id=font['id'],
        foreground_color=int(emoji_log['color'], 16),
        background_color=int(emoji_log['back_color'], 16),
        text=emoji_log['text'],
    )
    code = EcodeEncoder().encode(ecode)

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
        'code': code,
    }

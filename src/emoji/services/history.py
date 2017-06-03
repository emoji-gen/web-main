# -*- encoding: utf-8 -*-

from emoji import db, app
from emoji.models.emoji_log import EmojiLog

def logging(
            text,
            color,
            back_color,
            font,
            size_fixed=False,
            align='center',
            stretch=True,
            public_fg=True,
            ):
    emoji_log = EmojiLog(
            text,
            color,
            back_color,
            font,
            size_fixed,
            align,
            stretch,
            public_fg
            )
    db.session.add(emoji_log)
    db.session.commit()

def search(limit=30, offset=0):
    if not app.config['MYSQL_ENABLED']:
        return []

    return (EmojiLog.query
        .filter(EmojiLog.public_fg == True)
        .order_by(EmojiLog.generated_at.desc())
        .offset(offset)
        .limit(limit)
        .all())

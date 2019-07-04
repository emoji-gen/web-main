# -*- encoding: utf-8 -*-

from datetime import datetime

from emoji.db.emoji_log import EmojiLog

class EmojiLogRepository():
    def __init__(self, app):
        self._app = app

    async def logging(
        self,
        text,
        color,
        back_color,
        font,
        size_fixed=False,
        align='center',
        stretch=True,
        public_fg=True
    ):
        async with self._app['db'].acquire() as conn:
            await conn.execute(EmojiLog.insert().values(
                text=text,
                color=color,
                back_color=back_color,
                font=font,
                size_fixed=1 if size_fixed else 0,
                align=align,
                stretch=1 if stretch else 0,
                public_fg=1 if public_fg else 0,
                generated_at=datetime.now(),
                updated_at=datetime.now(),
                created_at=datetime.now()
            ))

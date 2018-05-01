# -*- encoding: utf-8 -*-

from datetime import datetime

from emoji.db.emoji_log import EmojiLog

class EmojiLogRepository():
    def __init__(self, app):
        self._app = app

    async def filter(self, limit=20, offset=0):
        async with self._app['db'].acquire() as conn:
            query = (EmojiLog.select()
                .where(EmojiLog.columns.public_fg == 1)
                .order_by(EmojiLog.columns.generated_at.desc())
                .limit(limit)
                .offset(offset))
            itr = conn.execute(query)
            return [ dict(v) async for v in itr ]


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
                size_fixed=size_fixed,
                align=align,
                stretch=stretch,
                public_fg=public_fg,
                generated_at=datetime.now(),
                updated_at=datetime.now(),
                created_at=datetime.now()
            ))

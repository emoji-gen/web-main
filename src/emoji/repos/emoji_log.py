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

            rows = [ dict(v) async for v in itr ]
            for row in rows:
                row['size_fixed'] = bool(row['size_fixed'])
                row['stretch'] = bool(row['stretch'])
                row['public_fg'] = bool(row['public_fg'])
            return rows


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

# -*- encoding: utf-8 -*-

from emoji.db.emoji_log import EmojiLog

class EmojiLogRepository():
    def __init__(self, app):
        self._app = app

    async def recently(self, limit):
      async with self._app['db'].acquire() as conn:
        itr = conn.execute(EmojiLog.select().limit(limit))
        return [ dict(v) async for v in itr ]

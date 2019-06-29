# -*- encoding: utf-8 -*-

from emoji.context_holder import ContextHolder


async def filter_recently():
    context = ContextHolder.context()
    async with context.mysql.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('''
                SELECT *
                FROM `emoji_log`
            ''')
            rows = await cur.fetchall()
            print(rows)

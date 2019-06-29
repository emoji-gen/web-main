# -*- encoding: utf-8 -*-

from emoji.context_holder import ContextHolder


async def filter_recently():
    context = ContextHolder.context()
    async with context.mysql.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('''
                SELECT *
                FROM `emoji_log`
                LIMIT 20
            ''')
            return [ _to_dict(v) for v in await cur.fetchall() ]


def _to_dict(row):
    return {
        'id': row[0],
        'text': row[1],
        'color': row[2],
        'back_color': row[3],
        'font': row[4],
        'size_fixed': row[5] == 1,
        'align': row[6],
        'stretch': row[7] == 1,
        'public_fg': row[8],
        'generated_at': row[9],
        'created_at': row[10],
        'updated_at': row[11],
    }


def to_rows():
    pass

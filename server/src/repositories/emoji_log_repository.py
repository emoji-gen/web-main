# -*- encoding: utf-8 -*-

from datetime import datetime
from context_holder import ContextHolder


async def filter_recently(locale, *, max_rows=20):
    async with ContextHolder.context.mysql.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('''
                SELECT *
                FROM `emoji_log`
                WHERE `locale` = %s AND `public_fg` = 1
                ORDER BY `generated_at` DESC
                LIMIT %s
            ''', (locale, max_rows))
            return [ _to_dict(v) for v in await cur.fetchall() ]


async def add(data):
    async with ContextHolder.context.mysql.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('''
                INSERT INTO `emoji_log`
                (
                    `text`,
                    `color`,
                    `back_color`,
                    `font`,
                    `size_fixed`,
                    `align`,
                    `stretch`,
                    `locale`,
                    `public_fg`,
                    `generated_at`,
                    `updated_at`,
                    `created_at`
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
            ''', _to_tuple(data))


def _to_dict(tpl):
    return {
        'id': tpl[0],
        'text': tpl[1],
        'color': tpl[2],
        'back_color': tpl[3],
        'font': tpl[4],
        'size_fixed': tpl[5] == 1,
        'align': tpl[6],
        'stretch': tpl[7] == 1,
        'locale': tpl[8],
        'public_fg': tpl[9],
        'generated_at': tpl[10],
        'created_at': tpl[11],
        'updated_at': tpl[12],
    }


def _to_tuple(dct):
    return (
        dct['text'],
        dct['color'],
        dct['back_color'],
        dct['font'],
        1 if dct['size_fixed'] else 0,
        dct['align'],
        1 if dct['stretch'] else 0,
        dct['locale'],
        1 if dct['public_fg'] else 0,
        datetime.now(),
        datetime.now(),
        datetime.now(),
    )

# -*- encoding: utf-8 -*-

from aiomysql.sa import create_engine


async def init_db(app):
    app['db'] = await create_engine(
        loop=app.loop,
        user='root',
        db='emoji',
        host='127.0.0.1',
        password='',
        charset='utf8mb4',
        autocommit=True
    )


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


if __name__ == '__main__':
    pass

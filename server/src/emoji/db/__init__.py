# -*- encoding: utf-8 -*-

from aiomysql.sa import create_engine


async def init_db(app):
    app['db'] = await create_engine(
        loop=app.loop,
        user=app['config']['mysql']['user'],
        db=app['config']['mysql']['db'],
        host=app['config']['mysql']['host'],
        password=app['config']['mysql']['password'],
        charset='utf8mb4',
        autocommit=True
    )


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


if __name__ == '__main__':
    pass

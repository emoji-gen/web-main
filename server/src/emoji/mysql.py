# -*- encoding: utf-8 -*-

import asyncio
import aiomysql

class MySQL():
    def __init__(self, config):
        self._config = config
        self._pool = None

    async def startup(self):
        if self._pool is None:
            self._pool = await aiomysql.create_pool(
                host=self._config.host,
                port=self._config.port,
                user=self._config.user,
                password=self._config.password,
                db='emoji',
                charset='utf8mb4',
                autocommit=True,
            )

    def cleanup(self):
        if self._pool is not None:
            self._pool.terminate()

    def acquire(self):
        return self._pool.acquire()


# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import asyncio
from emoji.context import Context

loop = asyncio.get_event_loop()
context = loop.run_until_complete(Context.bootstrap())
app = context.app

if __name__ == '__main__':
    run_app(app, host='0.0.0.0', port=5000)

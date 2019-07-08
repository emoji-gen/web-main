# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from context import Context

async def app_factory():
    context = await Context.get_context()
    return context.app

if __name__ == '__main__':
    run_app(app_factory(), host='0.0.0.0', port=5000)

# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

from emoji import app_provider
app = app_provider()

if __name__ == '__main__':
    run_app(app, host='0.0.0.0', port=5000)

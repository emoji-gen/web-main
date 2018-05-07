# -*- coding: utf-8 -*-

import sys
import os
from aiohttp.web import run_app
from pathlib import Path

src_path = str(Path(__file__).resolve().parent.joinpath('src'))
sys.path.append(src_path)

proto_path = str(Path(__file__).resolve().parent.joinpath('generated'))
sys.path.append(proto_path)

import base64
from Font_pb2 import Font
from InitialState_pb2 import InitialState

state = InitialState()

font = state.fonts.add()
font.id = 12345
font.name = "aaa"

font = state.fonts.add()
font.id = 12345
font.name = "aaa"

print(base64.b64encode(state.SerializeToString()))

# from emoji import app_provider
# app = app_provider()

# if __name__ == '__main__':
#     run_app(app, host='0.0.0.0', port=5000)

# -*- coding: utf-8 -*-

from apps import config
from apps.resources.db import history

import json
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta

# _inflator = Inflator()
# def inflate(obj):
#     return _inflator.inflate(obj)

def search(
        limit=10
        ):
    pass
#     if not config.mysql_enabled:
#         return []

#     obj = inflate(db.search())
#     print(obj[0]['back_color'])

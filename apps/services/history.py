# -*- coding: utf-8 -*-

from apps           import config
from apps.resources import db

from sqlalchemy.ext.declarative import DeclarativeMeta

class Inflator():

    def inflate(obj):
        if isinstance(obj, list):
            return [ inflate(x) for x in obj ]

        if isinstance(obj.__class__, DeclarativeMeta):

_inflator = Inflator()
def inflate(obj):
    return obj.inflate(obj)

def search(
        limit=10
        ):
    if not config.mysql_enabled:
        return []

    obj = inflate(db.search())
    print(obj)

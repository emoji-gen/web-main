# -*- encoding: utf-8 -*-

import json
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta

class Inflator():
    IGNORE_COLUMNS = [ 'created_at', 'updated_at' ]

    def inflate(self, obj):
        if isinstance(obj, list):
            return [ inflate(x) for x in obj ]

        if isinstance(obj.__class__, DeclarativeMeta):
            fields   = {}
            columns  = [ x for x in dir(obj) if not x.startswith('_') and x != 'metadata' ]
            for column in columns:
                if column in self.IGNORE_COLUMNS:
                    continue
                data = obj.__getattribute__(column)

                if isinstance(data, datetime):
                    data = int(data.timestamp()) # epoch

                try:
                    json.dumps(data)
                    fields[column] = data
                except TypeError:
                    fields[column] = None
            return fields

        return None

# -*- encoding: utf-8 -*-

from funcy import project

class FontRepository():
    def __init__(self, app):
        self._app = app

    def all(self):
        items = list(self._app['config']['repos']['fonts'].items())
        public_items = filter(lambda item: item[1]['enabled'] == 'on', items)
        sorted_items = sorted(public_items, key=lambda item: item[1]['order'])
        return [
            dict(project(item[1], [ 'name', 'type' ]), **{ 'key': item[0] })
            for item in sorted_items
        ]

    def all_as_dict(self):
        return self._app['config']['repos']['fonts'] # TODO: enabled



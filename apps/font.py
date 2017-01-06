# -*- coding: utf-8 -*-

from funcy import project

from . import config

def search_font_list():
    items        = list(config.fonts.items())
    public_items = filter(lambda item: item[1]['enabled'] == 'on', items)
    sorted_items = sorted(public_items, key=lambda item: item[1]['order'])
    return [
        dict(project(item[1], ['name', 'type']), **{ 'key': item[0] })
        for item in sorted_items
    ]

def search_font_list_v1():
    keys      = ['key', 'name']
    font_list = search_font_list()
    return [ project(font, keys) for font in font_list ]


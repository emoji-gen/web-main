# -*- encoding: utf-8 -*-

from aiohttp.web import HTTPBadRequest

async def generate(request):
    default_font_key = request.app['config']['routes']['default_font_key']
    default_text = request.app['config']['routes']['default_text']
    default_color = request.app['config']['routes']['default_color']
    default_background_color = request.app['config']['routes']['default_background_color']
    fonts = request.app['repos']['fonts'].all_as_dict()

    font_key = request.query.get('font', default_font_key)
    text = request.query.get('text', default_text)
    color = request.query.get('color', default_color).upper()
    back_color = request.get('back_color', default_background_color).upper()

    if not font_key in fonts:
        raise HTTPBadRequest()


    # size_fixed = request.args.get('size_fixed',default='false',type=str).lower() == 'true'
    # align = request.args.get('align',default='center',type=str).lower()
    # stretch = request.args.get('stretch',default='true',type=str).lower() != 'false'

    # font_file = font_list.get(font_key, default_font_key).get('file')

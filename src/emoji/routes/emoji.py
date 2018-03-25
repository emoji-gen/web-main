# -*- encoding: utf-8 -*-

import emojilib
import re
from aiohttp.web import Response, HTTPBadRequest
from pathlib import Path


async def generate(request):
    return await _execute(request)


async def download(request):
    return await _execute(request, download_fg=True)


async def _execute(request, download_fg=False):
    fonts = request.app['repos']['fonts'].all_as_dict()

    default_font_key = request.app['config']['routes']['default_font_key']
    default_text = request.app['config']['routes']['default_text']
    default_color = request.app['config']['routes']['default_color']
    default_background_color = request.app['config']['routes']['default_background_color']

    font_key = request.query.get('font', default_font_key)
    font_file = fonts.get(font_key, default_font_key).get('file')
    fonts_path = request.app['config']['fonts_path']
    font_path = str(Path(fonts_path).joinpath(font_file))

    text = request.query.get('text', default_text)
    color = request.query.get('color', default_color).upper()
    background_color = request.query.get('back_color', default_background_color).upper()
    size_fixed = request.query.get('size_fixed',default='false').lower() == 'true'
    align = request.query.get('align', 'center').lower()
    disable_stretch = request.query.get('stretch', 'true').lower() == 'false'

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(60 * 60 * 24) # 1 day
    if download_fg:
        desposition = 'attachment; filename=\"{}.png\"'.format(re.sub(r'\s','_',text))
        headers['Content-Disposition'] = desposition

    # TODO: History 記録
    # TODO: Slack 通知

    img_data = emojilib.generate(
        text=text,
        width=128,
        height=128,
        color=color,
        background_color=background_color,
        size_fixed=size_fixed,
        disable_stretch=disable_stretch,
        align=align,
        typeface_file=font_path,
        format='png'
    )
    return Response(
        body=img_data,
        headers=headers,
        content_type='image/png'
    )

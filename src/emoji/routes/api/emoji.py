# -*- encoding: utf-8 -*-

from flask import jsonify, request

from emoji import app
from emoji.services.emoji import url_for

@app.route('/api/v1/emoji', methods=['POST'])
def api_v1_emoji():
    body = request.get_json(True)

    default_font_key = app.config['DEFAULT_FONT_KEY']
    font_list = app.config['FONT_LIST']

    font_key = body.get('font', default_font_key)
    text = body.get('text', app.config['DEFAULT_TEXT'])
    color = body.get('color', app.config['DEFAULT_COLOR'])
    back_color = body.get('back_color', app.config['DEFAULT_BACK_COLOR']).upper()
    size_fixed = body.get('size_fixed', 'false').lower() == 'true'
    align = body.get('align', 'center').lower()
    stretch = body.get('stretch', 'true').lower() != 'false'
    public_fg = body.get('public_fg', 'true') == 'true'

    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    if back_color is False:
        back_color = 'FFFFFF00'
    if align not in ['center','right','left']:
        align = 'center'

    image_url = url_for(text, font_key, color, back_color, size_fixed, align, stretch)
    emoji = {
        'image_url': image_url,
        'parameters': {
            'text': text,
            'font': font_key,
            'color': color,
            'back_color': back_color,
            'align': align,
            'size_fixed': size_fixed,
            'stretch': stretch,
            'public_fg': public_fg,
        },
    }
    return jsonify(emoji)

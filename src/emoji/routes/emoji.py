# -*- encoding: utf-8 -*-

from flask import request, make_response

from emoji import app

@app.route('/emoji')
def emoji():
    default_font_key = app.config['DEFAULT_FONT_KEY']
    font_list = app.config['FONT_LIST']

    font_key = request.args.get('font', default=default_font_key, type=str)
    text = request.args.get('text', default=app.config['DEFAULT_TEXT'], type=str)
    color = request.args.get('color', default=app.config['DEFAULT_COLOR'], type=str).upper()
    back_color = request.args.get('back_color',
            default=app.config['DEFAULT_BACK_COLOR'], type=str).upper()
    size_fixed = request.args.get('size_fixed',default='false',type=str).lower() == 'true'
    align = request.args.get('align',default='center',type=str).lower()
    stretch = request.args.get('stretch',default='true',type=str).lower() != 'false'

    font_file = font_list.get(font_key, default_font_key).get('file')

    # if text is False:
    #     text = ' '
    # if color is False:
    #     color = '000000'
    # if back_color is False:
    #     back_color = 'FFFFFF00'
    # if align not in ['center','right','left']:
    #     align = 'center'
    # img_png = generate_emoji(text,font,color,back_color,size_fixed,align,stretch)

    # if not img_png:
    #     return abort(400)

    res = make_response()
    res.data = ''#img_png
    res.headers['Content-Type'] = 'image/png'
    return res

# -*- encoding: utf-8 -*-

import re

from flask import request, make_response

from emoji import app
from emoji.services import history
from emoji.services.emoji import generate
from emoji.jobs.slack import slack_notify

@app.route('/emoji_download')
def emoji_download():
    font_list = app.config['FONT_LIST']

    font_default = 'mplus-1p-black'
    font_key = request.args.get("font", default=font_default, type=str)
    text = request.args.get("text", default='test', type=str)
    color = request.args.get("color", default='000000', type=str).upper()
    back_color = request.args.get("back_color", default='FFFFFF00', type=str).upper()
    size_fixed = request.args.get('size_fixed',default='false',type=str).lower() == 'true'
    align = request.args.get("align",default='center',type=str).lower()
    stretch = request.args.get("stretch",default='true',type=str).lower() != 'false'
    font = font_list.get(font_key,font_default).get('file')
    public_fg = request.args.get('public_fg', default='true', type=str) == 'true'

    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    if back_color is False:
        back_color = 'FFFFFF00'
    if align not in ['center','right','left']:
        align = 'center'

    img_png = generate(text,font,color,back_color,size_fixed,align,stretch)
    disp = 'attachment;' + \
           'filename=\"' + re.sub(r'\s','_',text) + '.png\"'
    res = make_response()
    res.data = img_png
    res.headers['Content-Type'] = 'image/png'
    res.headers['Content-Disposition'] = disp.encode('utf-8')

    if app.config['SLACK_ENABLED']:
        slack_notify.queue(text,font_key,color,back_color,size_fixed,align,stretch)

    if app.config['MYSQL_ENABLED']:
        history.logging(text, color, back_color, font_key,size_fixed,align,stretch, public_fg)

    return res

import datetime
import io
import os
import re
import hashlib
import json

from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import Response, make_response
from flask import abort
from flask_rq2 import RQ

from apps.String2emoji import String2emoji

from apps       import config
from apps       import history
from apps.cache import create as create_cache
from apps.jobs  import rq, slack_notify

from apps.services import font
from apps.services import history as x_history

app = Flask(__name__)
rq.init_app(app)

# enable debug mode if on development environment
app.debug = config.debug
app.jinja_env.globals['debug']       = config.debug
app.jinja_env.globals['domain']      = config.site_domain
app.jinja_env.globals['description'] = config.site_description

app.jinja_env.globals['history_enabled'] = config.history_enabled

# compute JavaScript checksum
if not config.debug:
    app.jinja_env.globals['js_min_checksum'] = \
            hashlib.md5(open(config.js_min_path, 'rb').read()).hexdigest()

# setup image cache
if config.memcached_enabled:
    print('Use MemcachedCache')

cache = create_cache(
        config.memcached_enabled,
        config.cache_timeout,
        config.memcached_servers
        )

fonts_list = config.fonts

# -----------------------------------------------------------------------------

@app.route('/')
def index():
    if config.debug:
        epoch_f = datetime.datetime.now().timestamp()
        args = { 'js_timestamp': hashlib.md5(str(epoch_f).encode('utf-8')).hexdigest() }
        return render_template('index.j2', **args)
    return render_template('index.j2')

@app.route('/emoji')
def emoji():
    font_default = 'mplus-1p-black'
    font_key = request.args.get("font", default=font_default, type=str)
    text = request.args.get("text", default='test', type=str)
    color = request.args.get("color", default='000000', type=str).upper()
    back_color = request.args.get("back_color", default='FFFFFF00', type=str).upper()
    size_fixed = request.args.get("size_fixed",default='false',type=str).lower() == 'true'
    align = request.args.get("align",default='center',type=str).lower()
    stretch = request.args.get("stretch",default='true',type=str).lower() != 'false'
    font = fonts_list.get(font_key,font_default).get('file')
    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    if back_color is False:
        back_color = 'FFFFFF00'
    if align not in ['center','right','left']:
        align = 'center'
    img_png = generate_emoji(text,font,color,back_color,size_fixed,align,stretch)

    if not img_png:
        return abort(400)

    res = make_response()
    res.data = img_png
    res.headers['Content-Type'] = 'image/png'
    return res

@app.route('/emoji_download')
def emoji_download():
    font_default = 'mplus-1p-black'
    font_key = request.args.get("font", default=font_default, type=str)
    text = request.args.get("text", default='test', type=str)
    color = request.args.get("color", default='000000', type=str).upper()
    back_color = request.args.get("back_color", default='FFFFFF00', type=str).upper()
    size_fixed = request.args.get('size_fixed',default='false',type=str).lower() == 'true'
    align = request.args.get("align",default='center',type=str).lower()
    stretch = request.args.get("stretch",default='true',type=str).lower() != 'false'
    font = fonts_list.get(font_key,font_default).get('file')
    public_fg = request.args.get('public_fg', default='true', type=str) == 'true'
    font = fonts_list.get(font_key,font_default).get('file')
    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    if back_color is False:
        back_color = 'FFFFFF00'
    if align not in ['center','right','left']:
        align = 'center'

    img_png = generate_emoji(text,font,color,back_color,size_fixed,align,stretch)
    disp = 'attachment;' + \
           'filename=\"' + re.sub(r'\s','_',text) + '.png\"'
    res = make_response()
    res.data = img_png
    res.headers['Content-Type'] = 'image/png'
    res.headers['Content-Disposition'] = disp.encode('utf-8')

    if config.slack_web_hook_enable:
        slack_notify.queue(text,font_key,color,back_color,size_fixed,align,stretch)

    if config.mysql_enabled:
        history.logging(text, color, back_color, font_key,size_fixed,align,stretch, public_fg)

    return res

@app.route('/api/fonts')
def api_fonts():
    res = make_response()
    res.headers['Content-Type'] = 'application/json'
    res.data = json.dumps(font.search_font_list())
    return res

@app.route('/api/v1/fonts')
def api_v1_fonts():
    res = make_response()
    res.headers['Content-Type'] = 'application/json'
    res.data = json.dumps(font.search_font_list_v1())
    return res

@app.route('/api/histories')
def api_histories():
    res = make_response()
    res.headers['Content-Type'] = 'application/json'
    rows = history.search(limit=20)
    x_history.search(limit=20)
    if rows is None:
        res.data = json.dumps([])
    else:
        res.data = json.dumps(rows, cls=history.AlchemyEncoder)
    return res

def generate_emoji(text,font,color,back_color, \
                    size_fixed = False, \
                    align = 'center', \
                    stretch = True):
    global cache
    hash_text = text + \
            ':' + color +\
            ':' + back_color +\
            ':' + font +\
            ':' + ('true' if size_fixed else 'false') +\
            ':' + align +\
            ':' + ('true' if stretch else 'false') +\
            ':' + str(config.cache_version)
    r = int(color[0] +color[1],16)
    g = int(color[2] +color[3],16)
    b = int(color[4] +color[5],16)
    if len(color) == 6:
        a = 0xff
    elif len(color) == 8:
        a = int(color[6] + color[7],16)
    br = int(back_color[0] + back_color[1],16)
    bg = int(back_color[2] + back_color[3],16)
    bb = int(back_color[4] + back_color[5],16)
    if len(back_color) == 6:
        ba = 0xff
    elif len(back_color) == 8:
        ba = int(back_color[6] + back_color[7],16)
    cache_id = hashlib.md5(hash_text.encode('utf-8')).hexdigest()
    img_png = cache.get(cache_id)
    if img_png is None:
        lines = text.splitlines()

        if len(text) > 100: # XXX: 100 文字以上
            return None

        if len(lines) == 1 and len(lines[0]) > 10: # XXX: 1 列 10 文字以上
            return None

        if len(lines) > 10: # XXX: 10 行以上
            return None

        emoji = String2emoji(lines, 'assets/fonts/' + font,(r,g,b,a),(br,bg,bb,ba))
        if not size_fixed:
            emojiMode = emoji.MODE_NOMAL
        elif size_fixed:
            emojiMode = emoji.MODE_FONTSIZE_FIXED
        else :
            emojiMode = emoji.MODE_NOMAL
        img = emoji.getEmoji(emojiMode,align,stretch)
        output = io.BytesIO()
        img.save(output,format='png')
        img_png = output.getvalue()
        cache.set(cache_id,img_png)
    return img_png

@app.route('/sitemap.xml')
def sitemap_xml():
    return redirect(url_for('static', filename='sitemap.xml'))

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
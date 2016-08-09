import hashlib
import io
import os

from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import Response, make_response

from String2emoji import String2emoji

from apps       import config
from apps.cache import create as create_cache


app = Flask(__name__)

# enable debug mode if on development environment
app.debug = config.debug
app.jinja_env.globals['debug'] = config.debug

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

# -----------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.j2')

@app.route('/emoji')
def emoji():
    global cache
    font = request.args.get("font", default='NotoSansMonoCJKjp-Bold.otf', type=str)
    text = request.args.get("text", default='test', type=str)
    color = request.args.get("color", default='000000', type=str)
    if font is False:
        font = 'NotoSansMonoCJKjp-Bold.otf'
    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    r = int(color[0] +color[1],16)
    g = int(color[2] +color[3],16)
    b = int(color[4] +color[5],16)
    hash_text = text + ':' + color
    cache_id = hashlib.md5(hash_text.encode('utf-8')).hexdigest()

    try:
        img_png = cache.get(cache_id)
    except:
        img_png = None

    if img_png is None:
        emoji = String2emoji(text.splitlines(),'assets/fonts/' + font,(r,g,b))
        img = emoji.getEmoji()
        output = io.BytesIO()
        img.save(output,format='png')
        img_png = output.getvalue()
        cache.set(cache_id,img_png)
        print('generate emoji!')
    res = make_response()
    res.data = img_png
    res.headers['Content-Type'] = 'image/png'
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

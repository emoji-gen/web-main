import hashlib
import io
import os

from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import Response,make_response
from werkzeug.contrib.cache import MemcachedCache, SimpleCache

from String2emoji import String2emoji
from apps import config

app = Flask(__name__)

# enable debug mode if on development environment
app.debug = config.env == 'development'
app.jinja_env.globals['debug'] = app.debug

class BinarySupportedMemcachedCache(MemcachedCache):
    def import_preferred_memcache_lib(self, servers):
        import pylibmc
        return pylibmc.Client(servers, binary=True)

# setup image cache
if config.memcached_enabled:
    print('Use MemcachedCache')
    cache = BinarySupportedMemcachedCache(
            config.memcached_servers,
            default_timeout=config.cache_timeout
            )
else:
    print('Use SimpleCache')
    cache = SimpleCache(default_timeout=config.cache_timeout)


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

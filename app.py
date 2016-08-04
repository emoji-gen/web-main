import os
from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import Response,make_response
#from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.cache import SimpleCache
import hashlib
from String2emoji import String2emoji
import io

app = Flask(__name__)

#cache = MemcachedCache(['127.0.0.1:11211'])
cache = SimpleCache()

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
    img_png = cache.get(cache_id)
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
    port = os.getenv('PORT', '5000')
    app.debug = True
    app.run(host='0.0.0.0', port=int(port))

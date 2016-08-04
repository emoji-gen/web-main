import os
from flask import Flask, render_template
from flask import request, redirect, url_for
from flask import Response,make_response
from String2emoji import String2emoji
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.j2')

@app.route('/emoji')
def emoji():
    font = request.args.get("font", default='NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf', type=str)
    text = request.args.get("text", default='test', type=str)
    color = request.args.get("color", default='000000', type=str)
    if font is False:
        font = 'NotoSansCJKjp-hinted/NotoSansMonoCJKjp-Bold.otf'
    if text is False:
        text = ' '
    if color is False:
        color = '000000'
    r = int(color[0] +color[1],16)
    g = int(color[2] +color[3],16)
    b = int(color[4] +color[5],16)
    emoji = String2emoji(text.splitlines(), font,(r,g,b))
    img = emoji.getEmoji()
    output = io.BytesIO()
    img.save(output,format='png')
    res = make_response()
    res.data = output.getvalue()
    res.headers['Content-Type'] = 'image/png'
    return res
if __name__ == '__main__':
    port = os.getenv('PORT', '5000')
    app.debug = True
    app.run(host='0.0.0.0', port=int(port))

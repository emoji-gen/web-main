import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.j2')


if __name__ == '__main__':
    port = os.getenv('PORT', '5000')
    app.debug = True
    app.run(host='0.0.0.0', port=int(port))

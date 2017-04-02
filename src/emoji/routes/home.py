# -*- encoding: utf-8 -*-

import hashlib
from datetime import datetime

from flask import render_template, redirect, url_for

from emoji import app

@app.route('/')
def home():
    if app.config['DEBUG']:
        epoch_f = datetime.now().timestamp()
        args = { 'js_timestamp': hashlib.md5(str(epoch_f).encode('utf-8')).hexdigest() }
        return render_template('index.j2', **args)
    return render_template('index.j2')

@app.route('/sitemap.xml')
def sitemap_xml():
    return redirect(url_for('static', filename='sitemap.xml'))

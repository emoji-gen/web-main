# -*- encoding: utf-8 -*-

from flask import jsonify

from emoji import app
from emoji.services.font import *

@app.route('/api/fonts')
def api_fonts():
    font_list = search_font_list()
    return jsonify(font_list)

@app.route('/api/v1/fonts')
def api_v1_fonts():
    font_list = search_font_list_v1()
    return jsonify(font_list)

# -*- encoding: utf-8 -*-

from flask import jsonify

from emoji import app
from emoji.services import history

@app.route('/api/histories')
def api_histories():
    result = []
    rows = history.search(limit=20)
    for row in rows:
        result.append({
            'text': row.text,
            'color': row.color,
            'back_color': row.back_color,
            'font': row.font,
            'size_fixed': row.size_fixed,
            'align': row.align,
            'stretch': row.stretch,
            'public_fg': row.public_fg
        })
    return jsonify(result)

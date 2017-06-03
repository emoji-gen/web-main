# -*- encoding: utf-8 -*-

from flask import jsonify, request

from emoji import app
from emoji.services import history, emoji

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
        })
    return jsonify(result)

@app.route('/api/v1/histories')
def api_v1_histories():
    limit = request.args.get("limit", default=20, type=int)
    offset = request.args.get("offset", default=0, type=int)

    result = []
    rows = history.search(limit=limit, offset=offset)
    for row in rows:
        result.append({
            'id': row.id,
            'generated_at': int(row.generated_at.timestamp()),
            'emoji_url': emoji.url_for(
                row.text,
                row.font,
                row.color,
                row.back_color,
                row.size_fixed,
                row.align,
                row.stretch
            ),
            'parameters': {
                'text': row.text,
                'font': row.font,
                'color': row.color,
                'back_color': row.back_color,
                'align': row.align,
                'size_fixed': row.size_fixed,
                'stretch': row.stretch,
            },
        })
    return jsonify(result)

# -*- encoding: utf-8 -*-

from aiohttp import web
from funcy import project


async def all_v0(request):
    emoji_log_repository = request.app['repos']['emoji_log']
    emoji_logs = await emoji_log_repository.filter(limit=20)

    columns = ['text', 'color', 'back_color', 'font', 'size_fixed', 'align', 'stretch']
    result = [ project(v, columns) for v in emoji_logs ]

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 seconds
    return web.json_response(result, headers=headers)


async def all_v1(request):
    emoji_log_repository = request.app['repos']['emoji_log']
    emoji_service = request.app['services']['emoji']

    limit, offset = _parse_v1_parameters(request)
    emoji_logs = await emoji_log_repository.filter(limit=limit, offset=offset)

    columns = ['text', 'color', 'back_color', 'font', 'size_fixed', 'align', 'stretch']
    result = []
    for emoji_log in emoji_logs:
        result.append({
            'id': emoji_log['id'],
            'generated_at': int(emoji_log['generated_at'].timestamp()),
            'emoji_url': emoji_service.make_url(
                text=emoji_log['text'],
                font=emoji_log['font'],
                color=emoji_log['color'],
                back_color=emoji_log['back_color'],
                size_fixed=emoji_log['size_fixed'],
                align=emoji_log['align'],
                stretch=emoji_log['stretch']
            ),
            'parameters': project(emoji_log, columns)
        })

    headers = {}
    if not request.app.debug:
        headers['Cache-Control'] = 'public, max-age={}'.format(10) # 10 seconds
    return web.json_response(result, headers=headers)


def _parse_v1_parameters(request):
    try:
        limit = int(request.query.get('limit', None))
    except (TypeError, ValueError):
        limit = 20

    try:
        offset = int(request.query.get('offset', None))
    except (TypeError, ValueError):
        offset = 0

    return min(limit, 100), offset # TODO: 定数外だし



if __name__ == '__main__':
    pass

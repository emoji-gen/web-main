# -*- encoding: utf-8 -*-

import slackweb
import urllib.parse

from emoji import app, rq

@rq.job('low')
def slack_notify(text, font, color, back_color, size_fixed, align, stretch):
    if not app.config['SLACK_ENABLED']:
        return

    bar_color = color[:6]
    params = {
        'text': text,
        'font': font,
        'color': color,
        'back_color': back_color,
        'size_fixed':size_fixed,
        'align':align,
        'stretch':stretch
    }
    attachment = {
        'title': 'download emoji',
        'text': str(params),
        'image_url': 'http://emoji.pine.moe/emoji?' + urllib.parse.urlencode(params),
        'color': '#' + bar_color
    }

    slack = slackweb.Slack(url=app.config['SLACK_WEBHOOK_URL'])
    slack.notify(attachments=[attachment])

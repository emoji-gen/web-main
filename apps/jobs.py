# -*- coding: utf-8 -*-
import slackweb
import urllib.parse
from flask_rq2 import RQ

from apps import config

rq = RQ()

# slack notification
slack_enable = config.slack_web_hook_enable
slack = slackweb.Slack(url=config.slack_web_hook_url)

@rq.job('low')
def slack_notify(text, font, color, back_color,size_fixed,align,stretch):
    bar_color = color[:6]
    if not slack_enable:
        return
    attachments = []
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
    attachments.append(attachment)
    slack.notify(attachments = attachments)

@rq.exception_handler
def send_alert_to_ops(job, *exc_info):
    print(job, exec_info)

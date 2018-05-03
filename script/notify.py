#!/usr/bin/env python

import os
import sys
import slackweb

circleci_icon = 'https://i.imgur.com/FLjAA35.png'
pytest_mini_icon = 'https://i.imgur.com/H3RVdT1.png'


def main():
    message = sys.argv[1]
    if message == 'started':
        _notify('Test started', '#66d3e4')
    elif message == 'successful':
        _notify('Deploy successful', '#41aa58')
    elif message == 'failed':
        _notify('Deploy failed', '#d10c20')
    else:
        raise RuntimeError('invalid message')


def _notify(text, color):
    if 'CIRCLE_BUILD_URL' in os.environ:
        text += ' <{}|#{}>'.format(
            os.environ['CIRCLE_BUILD_URL'],
            os.environ['CIRCLE_BUILD_NUM']
        )

    slack = slackweb.Slack(url=os.environ['SLACK_INCOMING_WEBHOOK'])
    attachment = {
        'color': color,
        'text': text,
        'author_name': 'pytest',
        'author_icon': pytest_mini_icon,
    }
    slack.notify(
        username='CircleCI',
        icon_url=circleci_icon,
        attachments=[attachment]
    )


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import slackweb

circleci_icon = 'https://i.imgur.com/FLjAA35.png'
pytest_mini_icon = 'https://i.imgur.com/H3RVdT1.png'


def main():
    _notify('Test started', '#66d3e4')


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

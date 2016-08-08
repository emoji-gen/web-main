#!/bin/bash

ICON_URL="https://dl.dropboxusercontent.com/u/29279948/Slack/Icons/CircleCI.png"

curl -XPOST \
    -d "token=$SLACK_API_TOKEN" \
    -d "channel=emoji" \
    -d "text=start   test   \`Emoji-Web\` *$CIRCLE_BRANCH* <$CIRCLE_BUILD_URL|#$CIRCLE_BUILD_NUM>" \
    -d "username=CircleCI" \
    -d "icon_url=$ICON_URL" \
    "https://slack.com/api/chat.postMessage" > /dev/null 2>&1

#!/bin/bash

set -e

curl -XPOST \
    -d "token=$SLACK_API_TOKEN" \
    -d "channel=emoji" \
    -d "text=start   deploy \`Emoji-Web\` *$CIRCLE_BRANCH* by CircleCI" \
    -d "username=Fabric" \
    -d "icon_emoji=:rocket:" \
    "https://slack.com/api/chat.postMessage"

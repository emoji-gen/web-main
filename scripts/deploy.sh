#!/bin/bash

set -eu

curl -X POST "https://circleci.com/api/v1.1/project/github/pine/Emoji-Private/tree/master?circle-token=$PRIVATE_CIRCLECI_TOKEN" >/dev/null 2>&1

#!/bin/bash

set -eu

git clone --depth 1 -b master --single-branch git@github.com:pine/Emoji-Private.git
cd Emoji-Private/fabric

pip install -r requirements.txt -q
fab production

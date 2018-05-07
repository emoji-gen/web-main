#!/bin/bash

set -eux -o pipefail

pip install -r requirements.txt \
  --index-url https://repo.fury.io/emoji-gen/ --extra-index-url https://pypi.org/simple

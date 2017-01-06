#!/bin/bash

set -eu

if [ -z "$(git diff --raw)" ]; then
  echo "git repository is dirty"
  git diff --raw
  exit 1
fi

if [ -z "$(git diff --cached --raw)" ]; then
  echo "git repository is dirty"
  git diff --cached --raw
  exit 1
fi

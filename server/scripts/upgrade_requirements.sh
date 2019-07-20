#!/bin/bash

set -eu

if [ -n "${VIRTUAL_ENV:-}" ]; then
  printf "[ERROR] Please deactivate virtualenv before run the script.\n" 1>&2
  exit 1
fi


set -x

rm -rf venv-scripts
python3 -m venv venv-scripts
. venv-scripts/bin/activate

pip install -r requirements.in
pip freeze > requirements.txt
git --no-pager diff

rm -rf venv-scripts

printf "\nSuccessful\n"

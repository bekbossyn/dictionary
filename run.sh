#!/usr/bin/env bash \n
source '/home/development/env_dictionary/bin/activate'
pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

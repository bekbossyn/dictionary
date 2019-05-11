#!/usr/bin/env bash
#source '/home/development/env_dictionary/bin/activate'
source '../env_dictionary/bin/activate'
pip install -r requirements.txt
python server.py collectstatic --noinput
python server.py migrate --noinput

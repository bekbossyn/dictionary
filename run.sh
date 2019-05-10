#!/usr/bin/env bash
cd /home/development/env_dictionary/bin && source 'activate'
cd  /home/development/dictionary/ && pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

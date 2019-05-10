#!/usr/bin/env bash
source '../env_dictionary/bin/activate'
cd  /home/development/dictionary/ && pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

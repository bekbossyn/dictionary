#!/usr/bin/env bash
cd /home/development/env_dictionary/bin
ls | grep 'myfile.py'
source '/home/development/env_dictionary/bin/activate'
cd  /home/development/dictionary/ && pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

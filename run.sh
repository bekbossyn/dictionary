#!/usr/bin/env bash
pwd
cd /home/development/env_dictionary/bin
pwd
ls | grep 'myfile.py'
pwd
source '/home/development/env_dictionary/bin/activate'
cd  /home/development/dictionary/ && pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

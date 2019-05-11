#!usr/bin/env bash
source '../home/development/env_dictionary/bin/activate'
which python
pwd
pip install -r requirements.txt
python ocean.py collectstatic --noinput
python ocean.py migrate --noinput

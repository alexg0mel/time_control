#! /usr/bin/bash

virtualenv -p python3.10 .venv
curl -sS https://bootstrap.pypa.io/get-pip.py | ./.venv/bin/python
.venv/bin/pip install -r requirements.txt

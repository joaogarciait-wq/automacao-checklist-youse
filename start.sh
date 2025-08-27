#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/opt/render/project/src

# Inicia o Gunicorn
python -m gunicorn --bind 0.0.0.0:$PORT src.main:app

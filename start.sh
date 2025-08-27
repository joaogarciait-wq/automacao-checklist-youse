#!/bin/bash

export PYTHONPATH=$PYTHONPATH:$(pwd)

# Inicia o Gunicorn
python -m gunicorn --bind 0.0.0.0:$PORT src.main:app
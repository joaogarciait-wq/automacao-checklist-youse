#!/bin/bash

export PYTHONPATH=$PYTHONPATH:/opt/render/project

# Inicia o Gunicorn
python -m gunicorn --bind 0.0.0.0:$PORT main:app

# ESTE É UM TESTE DE ALTERACAO UNICA

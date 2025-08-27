#!/bin/bash

# Inicia o Gunicorn
python -m gunicorn --bind 0.0.0.0:$PORT src.main:app



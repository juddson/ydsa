#!/usr/bin/env bash
# Simple script to run your Flask dev server in Codespaces

source .venv/bin/activate
export FLASK_APP=wsgi:app
export FLASK_ENV=development
export FLASK_DEBUG=1

flask run --host 0.0.0.0 --port 5000

#!/usr/bin/env bash
set -e
flask db upgrade
flask run --host=0.0.0.0 --port=5000
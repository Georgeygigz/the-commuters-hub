#!/bin/bash
# A bash script to create folders with subfolders all in one go.

mkdir -p app/api/{models,views,schemas,utils} | touch app/api/{models,views,schemas,utils}/__init__.py

mkdir -p app/tests/views 

mkdir .github | touch .github/pull_request_template.md

mkdir instance | touch instance/config.py

touch instance/__init__.py

touch app/tests/views/__init__.py

touch app/tests/base_test.py

touch app/__init__.py

touch app/tests/__init__.py

touch app/api/__init__.py

touch .env

python3 -m venv commuters-hub

touch run.py

touch .env_sample.txt

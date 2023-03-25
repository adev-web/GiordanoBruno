#!/usr/bin/env bash
# exit on error
pass_code = 'PASS_DIRS_APP'

rm -r **/__pycache__/
rm -r **/migrations/

mkdir app/migrations/
touch app/migrations/__init__.py

mkdir secure/migrations/
touch secure/migrations/__init__.py

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --no-input

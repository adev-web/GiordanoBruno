#!/usr/bin/env bash
# exit on error
rm -r **/__pycache__/
rm -r **/migrations/

mkdir app/migrations/
touch app/migrations/__init__.py

mkdir secure/migrations/
touch secure/migrations/__init__.py
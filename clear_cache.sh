#!/bin/bash
rm -rf project/__pycache__


data=("app" "secure")
for i in "${data[@]}"
do
rm -rf ${i}/__pycache__
rm -rf ${i}/migrations/__pycache__

#touch ${i}/migrations/__init__.py

done
#!/bin/bash
rm -rf */*/__pycache__
rm -rf */*/migrations/__pycache__
rm -rf */*/migrations/*.pyc
rm -rf */*/migrations/*/*.pyc
rm -rf */*/static_cache/*
rm -rf */*/.webassets-cache/*
rm -rf */*/.sass-cache/*
rm -rf */*/.cache/*

rm -rf './staticfiles/'

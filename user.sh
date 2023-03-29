#!/bin/bash

# Definir las variables necesarias
DJANGO_SETTINGS_MODULE='project.settings'
DJANGO_PROJECT_DIR='.'

# Cambiar al directorio del proyecto Django
cd $DJANGO_PROJECT_DIR

# Crear el superusuario con el comando 'createsuperuser'
python manage.py createsuperuser --settings=$DJANGO_SETTINGS_MODULE \
                                 --username='root_admin' \
                                 --password='admin_root' \
                                 --email='vargas.alessandro12@gmail.com' \
                                 --noinput

# Cambiar de vuelta al directorio original
cd -
